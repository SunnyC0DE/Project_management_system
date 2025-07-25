from django.shortcuts import render, redirect

from items.models import Categories, Items

from .forms import SignupForm
# Create your views here.
def index(request):
    items = Items.objects.filter(is_sold=False)[0:6]
    category = Categories.objects.all()
    return render(request, 'core/index.html', {
        'categories':category,
        'items':items
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
        
    return render(request, 'core/signup.html',{
        'form':form
    })