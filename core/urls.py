from django.urls import path
from .views import index, produto

urlpatterns = [
    path('', index, name='index'),
    path('produto/<id_produto>/', produto, name='produto')
]