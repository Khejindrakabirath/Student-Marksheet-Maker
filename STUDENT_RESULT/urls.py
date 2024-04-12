from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name = "homepage"),
    path('add/',views.add,name = 'add'),
    path('resultDetails/<int:id>',views.resultDetails, name = 'resultDetails'),
    path('update/<int:id>',views.update,name = 'update'),
    path('delete/<int:id>',views.delete,name = 'delete')
]