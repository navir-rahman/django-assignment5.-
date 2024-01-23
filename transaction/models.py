from django.db import models
from UserAccount.models import UserAccount
from Books.models import Book
from .constant import TRANSACTION_TYPES

class TransactionModel(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.transaction_type} - {self.amount} - {self.timestamp}'
