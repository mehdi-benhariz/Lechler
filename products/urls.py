from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',display_products,name="display"),
    path('create/',create_product,name="create"),
    path('delete/<int:p_id>',delete_product,name="delete"),
    path('update/<int:p_id>',update_product,name="update"),
]
urlpatterns += staticfiles_urlpatterns()
