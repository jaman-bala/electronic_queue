from django.shortcuts import render
import json
from django.http import JsonResponse
queue = []


def index(request):
    return render(request, 'queue_app/index.html')


def serve_customer(request):
    response_data = {'success': False}
    if request.method == 'POST':
        called_number_index = request.POST.get('call_number')
        if called_number_index is not None:
            called_number_index = int(called_number_index)
            if 0 <= called_number_index < len(queue):
                queue.pop(called_number_index)
                response_data['success'] = True
                response_data['queue'] = queue
    return JsonResponse(response_data)


def display_queue(request):
    return render(request, 'queue_app/queue_display.html', {'queue': queue})


current_customer_number = 1  # Инициализируем номер клиента
def add_customer(request):
    global current_customer_number  # Объявляем, что используем глобальную переменную
    if request.method == 'POST':
        num_customers = int(request.POST['num_customers'])
        for _ in range(num_customers):
            customer_name = str(current_customer_number)  # Генерируем имя клиента на основе номера
            current_customer_number += 1  # Увеличиваем номер для следующего клиента
            queue.append(customer_name)
    return render(request, 'queue_app/index.html', {'queue': queue})


def call_number(request):
    if queue:
        called_number = queue.pop(0)
    return render(request, 'queue_app/call_number.html', {'called_number': called_number})
