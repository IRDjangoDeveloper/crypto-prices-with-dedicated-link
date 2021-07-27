from django.urls import path
from .views import home, show_price
urlpatterns = [
    path('', home, name='homepage'),
    path('price/<int:link>', show_price)
]