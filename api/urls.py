from django.urls import path
from api import views
# from api.views import ProductList

urlpatterns=[
    path('product/',views.ProductList.as_view()),
]