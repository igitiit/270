import pytest
from decimal import Decimal
from datetime import datetime
from src.bank.transaction import Transaction

def test_transaction_creation():
    transaction = Transaction(Decimal("100.00"), datetime.now(), "Deposit", "deposit")
    assert transaction.amount == Decimal("100.00")
    assert transaction.description == "Deposit"
    assert transaction.transaction_type == "deposit"
