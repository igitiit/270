import pytest
from decimal import Decimal
from src.bank.account import BankAccount

def test_initial_balance():
    account = BankAccount("12345", Decimal("100.00"))
    assert account.balance == Decimal("100.00")

def test_deposit():
    account = BankAccount("12345", Decimal("50.00"))
    account.deposit(Decimal("50.00"))
    assert account.balance == Decimal("100.00")

def test_withdrawal():
    account = BankAccount("12345", Decimal("200.00"))
    account.withdraw(Decimal("50.00"))
    assert account.balance == Decimal("150.00")

def test_overdraft():
    account = BankAccount("12345", Decimal("30.00"))
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(Decimal("50.00"))
