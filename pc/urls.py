from django.urls import path
from . import views


app_name = 'pc'
urlpatterns = [
    path('', views.index, name='index'),
    path('computer/<int:computer_id>', views.single_computer, name='single_computer')
]
