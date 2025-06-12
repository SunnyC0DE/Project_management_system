from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from items.models import Items
# Create your views here.

@login_required
def index(request):
    items = Items.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html',{
        'items':items,
    })