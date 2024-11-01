from django.contrib import admin
from django.urls import path
from shop_app.views import customers, one_customer
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', customers),
    path('orders/<str:customer_name>/', one_customer, name='customer_orders')
]
