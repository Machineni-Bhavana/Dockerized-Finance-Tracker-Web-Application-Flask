from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from flask_login import login_required, current_user
from decimal import Decimal
from app import db
from app.models import Transaction
from datetime import datetime, date
from sqlalchemy.exc import OperationalError

finance_bp = Blueprint('finance', __name__)


@finance_bp.route('/')
@login_required
def dashboard():
    month = request.args.get('month')  # YYYY-MM
    query = Transaction.query
    if current_user.is_authenticated:
        query = query.filter(Transaction.user_id == current_user.id)
    if month:
        try:
            year, mon = map(int, month.split('-'))
            start = date(year, mon, 1)
            end = date(year + (mon // 12), (mon % 12) + 1, 1)
            query = query.filter(Transaction.date >= start, Transaction.date < end)
        except Exception:
            pass

    try:
        # Use COALESCE for robust ordering on SQLite (no NULLS LAST support)
        transactions = query.order_by(
            db.func.coalesce(Transaction.date, db.func.date(Transaction.created_at)).desc(),
            Transaction.created_at.desc()
        ).all()
    except OperationalError:
        # Ensure tables exist, then retry once
        db.session.rollback()
        db.create_all()
        transactions = query.order_by(
            db.func.coalesce(Transaction.date, db.func.date(Transaction.created_at)).desc(),
            Transaction.created_at.desc()
        ).all()
    income_total = sum((t.amount for t in transactions if t.type == 'income'), start=Decimal('0'))
    expense_total = sum((t.amount for t in transactions if t.type == 'expense'), start=Decimal('0'))
    balance = income_total - expense_total

    return render_template(
        'finance/dashboard.html',
        transactions=transactions,
        income_total=income_total,
        expense_total=expense_total,
        balance=balance,
        selected_month=month or '',
        category_labels=_category_labels(transactions),
        category_values=_category_values(transactions)
    )


@finance_bp.route('/add', methods=["POST"])
@login_required
def add_transaction():
    t_type = request.form.get('type')
    category = request.form.get('category')
    amount_str = request.form.get('amount')
    note = request.form.get('note')
    date_str = request.form.get('date')

    try:
        amount = Decimal(amount_str)
        if amount <= 0:
            raise ValueError
    except Exception:
        flash('Please enter a valid positive amount', 'danger')
        return redirect(url_for('finance.dashboard'))

    if t_type not in ('income', 'expense') or not category:
        flash('Type and category are required', 'danger')
        return redirect(url_for('finance.dashboard'))

    tx_date = None
    if date_str:
        try:
            tx_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except Exception:
            tx_date = None

    try:
        tx = Transaction(type=t_type, category=category, amount=amount, note=note, date=tx_date, user_id=current_user.id)
        db.session.add(tx)
        db.session.commit()
    except OperationalError:
        db.session.rollback()
        db.create_all()
        db.session.add(tx)
        db.session.commit()
    flash('Transaction added', 'success')
    return redirect(url_for('finance.dashboard'))


@finance_bp.route('/delete/<int:tx_id>', methods=["POST"])
@login_required
def delete_transaction(tx_id):
    tx = Transaction.query.get(tx_id)
    if tx:
        if tx.user_id and tx.user_id != current_user.id:
            flash('Not allowed', 'danger')
        else:
            db.session.delete(tx)
            db.session.commit()
            flash('Transaction deleted', 'info')
    return redirect(url_for('finance.dashboard'))


@finance_bp.route('/clear', methods=["POST"])
@login_required
def clear_transactions():
    if current_user.is_authenticated:
        Transaction.query.filter_by(user_id=current_user.id).delete()
    else:
        Transaction.query.delete()
    db.session.commit()
    flash('All transactions cleared', 'info')
    return redirect(url_for('finance.dashboard'))


@finance_bp.route('/export')
@login_required
def export_csv():
    query = Transaction.query.filter_by(user_id=current_user.id).order_by(
        db.func.coalesce(Transaction.date, db.func.date(Transaction.created_at)).desc(),
        Transaction.created_at.desc()
    )
    rows = ['Date,Type,Category,Amount,Note']
    for t in query.all():
        d = t.date.isoformat() if t.date else ''
        rows.append(f"{d},{t.type},{t.category},{t.amount},{(t.note or '').replace(',', ' ')}")
    csv_data = '\n'.join(rows)
    return Response(
        csv_data,
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename=transactions.csv'}
    )


# Helpers for category chart
def _category_labels(transactions):
    totals = {}
    for t in transactions:
        if t.type == 'expense':
            totals[t.category] = totals.get(t.category, 0) + float(t.amount)
    return list(totals.keys())


def _category_values(transactions):
    totals = {}
    for t in transactions:
        if t.type == 'expense':
            totals[t.category] = totals.get(t.category, 0) + float(t.amount)
    return list(totals.values())


