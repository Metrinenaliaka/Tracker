
from django.urls import path
from .views import FinancialTrackerView, DeleteEntryView

urlpatterns = [
    path('', FinancialTrackerView.as_view(), name='tracker'),
    path('delete/<int:entry_id>/', DeleteEntryView.as_view(), name='delete_entry'),
]

