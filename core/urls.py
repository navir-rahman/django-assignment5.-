from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('books/', include('Books.urls') ),
    path('categories/', include('Categories.urls') ),
    path('account/', include('UserAccount.urls') ),
    path('transaction/', include('transaction.urls') ),

]
