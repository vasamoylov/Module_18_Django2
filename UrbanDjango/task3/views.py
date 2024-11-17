from django.shortcuts import render


# Create your views here.

def wellcome(request):
    return render(request, 'main_page.html')


def games(request):
    return render(request, 'games.html')


def cart(request):
    return render(request, 'cart.html')
