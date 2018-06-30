from django.shortcuts import render

# Create your views here.


def spa_view(request):
    return render(request, 'spa.html')
