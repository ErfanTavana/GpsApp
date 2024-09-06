# این فایل urls.py مسئول مدیریت آدرس‌های اینترنتی مربوط به ویوهای مربوط به احراز هویت است.

from django.urls import path

from . import views

urlpatterns = [
    path('location/', views.SaveUserLocationView, name='SaveUserLocationView_name'),

    path('login/', views.login_view, name='login_view_name'),
    path('', views.home_view, name='home'),
]
