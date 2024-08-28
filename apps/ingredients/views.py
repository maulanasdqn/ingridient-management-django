from django.shortcuts import render

def ingredient_list(request):
    return render(request, 'ingredient_list.html')

def ingredient_detail(request, pk):
    return render(request, 'ingredient_detail.html')
