from .import views
from django.urls import path,include


urlpatterns = [
    path('', views.MainPage, name="Main"),
    path('product/', views.home, name="home"),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('aboutus/', views.Aboutus, name='Aboutus'),
    path('course/', views.course, name='course'),
    # path('', views.home, name='home'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('delete/<int:id>/', views.delete, name='delete'),
    # path('signup/' , views.signup, name= 'signup'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.signout, name='logout'),
#     path('', views.home, name='home'),
#     #path('index/', views.index, name='index'),
#     path('update/<int:id>/', views.update, name='update'),
#     path('delete/<int:id>/', views.delete, name='delete'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.signout, name='logout'),
]