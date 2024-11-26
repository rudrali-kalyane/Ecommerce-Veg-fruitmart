from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html',{}) 

def base(request):
    return render(request, 'base.html', {})

def cart(request):
    return render(request, 'cart.html',{}) 

def contact(request):
    return render(request, 'contact.html',{}) 

def chackout(request):
    return render(request, 'checkout.html',{}) 

def shop(request):
    return render(request, 'shop.html',{}) 

def testimonial(request):
    return render(request, 'testimonial.html',{}) 


def _404(request):
    return render(request, '404.html',{}) 