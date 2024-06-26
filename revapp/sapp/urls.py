from django.urls import path
from . import views


urlpatterns=[
    path('create/',views.createfun,name='createurl'),
    path('insert/',views.insertfun,name='inserturl'),
    path('select/',views.selectfun,name='selecturl'),
    path('update/<int:eno>/',views.updatefun,name='updateurl'),
    path('delete/<int:eno>/',views.deletefun,name='deleteurl')
]