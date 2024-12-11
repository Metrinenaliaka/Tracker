from django.shortcuts import render, redirect
from django.views import View
from .models import FinancialEntry
from .forms import FinancialEntryForm
import boto3

class FinancialTrackerView(View):
    def get(self, request):
        entries = FinancialEntry.objects.all().order_by('-date')
        form = FinancialEntryForm()
        
        # Get AWS ID and Name
        session = boto3.Session()
        sts = session.client('sts')
        identity = sts.get_caller_identity()
        aws_id = identity['UserId']
        aws_name = identity['Arn'].split('/')[-1]

        context = {
            'entries': entries,
            'form': form,
            'aws_id': aws_id,
            'aws_name': aws_name,
        }
        return render(request, 'apps/index.html', context)

    def post(self, request):
        form = FinancialEntryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tracker')

class DeleteEntryView(View):
    def post(self, request, entry_id):
        entry = FinancialEntry.objects.get(id=entry_id)
        entry.delete()
        return redirect('tracker')

