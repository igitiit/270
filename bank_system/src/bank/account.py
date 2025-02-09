from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional
from datetime import datetime

@dataclass
class Transaction:
    amount: Decimal
    timestamp: datetime
    description: str
    transaction_type: str  # 'deposit' or 'withdrawal'

class BankAccount:
    def __init__(self, account_number: str, owner_name: str, initial_balance: Decimal = Decimal('0.00')):
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = initial_balance
        self._transactions: List[Transaction] = []
        self._interest_rate = Decimal('0.01')  # 1% annual interest
        
        if initial_balance > 0:
            self._add_transaction(initial_balance, "Initial deposit")

    @property
    def balance(self) -> Decimal:
        return self._balance

    def deposit(self, amount: Decimal, description: str = "Deposit") -> bool:
        """Deposit money into account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._add_transaction(amount, description, 'deposit')
        return True

    def withdraw(self, amount: Decimal, description: str = "Withdrawal") -> bool:
        """Withdraw money from account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds")
            
        self._balance -= amount
        self._add_transaction(amount, description, 'withdrawal')
        return True

    def apply_interest(self) -> None:
        """Apply interest to the account balance."""
        interest = self._balance * self._interest_rate
        self.deposit(interest, "Interest payment")

    def get_statement(self, start_date: Optional[datetime] = None) -> List[Transaction]:
        """Get transaction history with optional date filter."""
        if start_date is None:
            return self._transactions
        
        return [t for t in self._transactions if t.timestamp >= start_date]

    def _add_transaction(self, amount: Decimal, description: str, 
                        transaction_type: str = 'deposit') -> None:
        """Add a transaction to the history."""
        transaction = Transaction(
            amount=amount,
            timestamp=datetime.now(),
            description=description,
            transaction_type=transaction_type
        )
        self._transactions.append(transaction)
