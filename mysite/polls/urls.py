from django.urls import path, include
from . import views
from .views import CustomAuthTokenLogin, register_user

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', CustomAuthTokenLogin.as_view()),
    path('register/', register_user, name='register_user'),
    path('personzx/<str:zx>',views.person_list_str),
    path('person/<int:pk>/', views.person_detail),
    path('person/', views.person_list, name='person_list'),
    path('person_view/<int:pk>', views.person_view),
    path('person/delete/<int:pk>/', views.person_delete),
    path('person/update/<int:pk>/', views.person_update),
    path('team/', views.team_list),
    path('team/<int:pk>/', views.team_detail),
    path('team/<int:pk>/', views.team_detail),
]
