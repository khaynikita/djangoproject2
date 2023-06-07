from django.urls import path
from  bciit_emp_app import views
urlpatterns=[
path('m/',views.index),
path('a/',views.all_emp),
path('add_emp' ,views.add_emp,name='add_emp'),
path('remove_emp' ,views.remove_emp,name='remove_emp'),
path('filter_emp' ,views.filter_emp,name='filter_emp'),




]