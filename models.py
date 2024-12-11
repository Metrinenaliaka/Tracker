from django.db import models

class FinancialEntry(models.Model):
    item = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - ${self.amount}"

