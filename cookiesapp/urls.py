from django.urls import path
from cookiesapp import views
urlpatterns = [
    path('set_cookie/',views.set_cookie,name='get_cookie'),
    path('get_cookie/', views.get_cookie, name='get_cookie')
]