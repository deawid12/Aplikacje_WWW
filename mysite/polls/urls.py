# from django.contrib import admin
# from django.urls import path, include
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('admin-tools/', include('admin_tools.urls'),),
#     path('mysite/', include('mysite.urls'),)
# ]

from django.urls import path
from .views import index, person_list, person_detail

urlpatterns = [
    path('', index, name='index'),
    path('osoby/', person_list, name='person-list'),
    path('osoby/<int:pk>/', person_detail, name='person-detail'),
]