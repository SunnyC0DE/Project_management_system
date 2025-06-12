from django.urls import path
from . import views

app_name = 'communication'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]