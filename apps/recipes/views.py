from django.shortcuts import render

def recipe_list(request):
    return render(request, 'recipe_list.html')

def recipe_detail(request, pk):
    return render(request, 'recipe_detail.html')
