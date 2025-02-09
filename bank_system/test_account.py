import pytest
from decimal import Decimal
from datetime import datetime, timedelta
from src.bank.account import BankAccount

@pytest.fixture
def account():
    return BankAccount("1234567890", "John Doe", Decimal('100.00'))

def test_initial_balance(account):
    assert account.balance == Decimal('100.00')

def test_deposit(account):
    account.deposit(Decimal('50.00'))
    assert account.balance == Decimal('150.00')

def test_withdraw(account):
    account.withdraw(Decimal('50.00'))
    assert account.balance == Decimal('50.00')

def test_insufficient_funds(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(Decimal('150.00'))

def test_negative_deposit(account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(Decimal('-50.00'))

def test_interest(account):
    initial_balance = account.balance
    account.apply_interest()
    expected_balance = initial_balance * Decimal('1.01')
    assert account.balance == expected_balance

def test_statement_filtering(account):
    # Add some transactions
    account.deposit(Decimal('50.00'), "First deposit")
    
    # Wait a second to ensure different timestamps
    import time
    time.sleep(1)
    
    checkpoint_time = datetime.now()
    
    time.sleep(1)
    
    account.withdraw(Decimal('25.00'), "First withdrawal")
    
    # Get filtered statement
    filtered_transactions = account.get_statement(checkpoint_time)
    assert len(filtered_transactions) == 1
    assert filtered_transactions[0].amount == Decimal('25.00')
