from django.shortcuts import render

import random

# Create your views here.

def salary_form(request):
    return render(request, 'form.html')

def salary_result(request):
    if request.method == 'POST':
        name = request.POST['name']
        gross_salary = float(request.POST['gross_salary'])
        tax = float(request.POST['tax'])  # percentage
        bonus = float(request.POST['bonus'])  # percentage

        net_salary = gross_salary - (gross_salary * tax / 100) + (gross_salary * bonus / 100)

        context = {
            'name': name,
            'net_salary': round(net_salary, 2),
        }
        return render(request, 'result.html', context)
    return render(request, 'form.html')

def jumble_word(request):
    jumbled = ''
    if request.method == 'POST':
        word = request.POST['word']
        word_list = list(word)
        random.shuffle(word_list)
        jumbled = ''.join(word_list)

    return render(request, 'jumble.html', {'jumbled': jumbled})