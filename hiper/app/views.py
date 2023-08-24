from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
import json
from datetime import datetime

# Create your views here.

def login(request):
    return HttpResponse("HELLO")


@csrf_exempt
# CREATES TRANSACTION 
def create_transaction(request): 
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            transaction = Transaction.objects.create(
                transaction_id=data['transaction_id'],
                bank_name=data['bank_name'],
                datetime=datetime.now(),  # Use current date and time
                amount=data['amount']
            )
            response_data = {'message': 'Transaction created successfully'}
            return JsonResponse(response_data, status=201)
        except Exception as e:
            error_data = {'error': str(e)}
            return JsonResponse(error_data, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)    
    
# GETS ALL TRANSACTION FROM THE DATABASE    
def all_transactions(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        transaction_list = [
            {
                'transaction_id': transaction.transaction_id,
                'bank_name': transaction.bank_name,
                'datetime': transaction.datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'amount': str(transaction.amount)
            }
            for transaction in transactions
        ]
        return JsonResponse(transaction_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    
 # GETS FILTERED TRANSACTIONS USING BANK NAME 
def filter_transactions(request):
    if request.method == 'GET':
        bank_name = request.GET.get('bank_name')

        if bank_name is None:
            return JsonResponse({'error': 'Please provide a bank_name query parameter'}, status=400)

        transactions = Transaction.objects.filter(bank_name=bank_name)
        transaction_list = [
            {
                'transaction_id': transaction.transaction_id,
                'bank_name': transaction.bank_name,
                'datetime': transaction.datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'amount': str(transaction.amount)
            }
            for transaction in transactions
        ]
        return JsonResponse(transaction_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)