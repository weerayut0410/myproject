from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.Index ),
    path('hello/',views.hello ),
    path('db/',views.db)
]
