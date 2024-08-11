
from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.index ,name='index.html'),
    path('post/<str:pk>',views.post,name='post')
]
