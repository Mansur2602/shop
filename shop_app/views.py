from django.shortcuts import render, get_object_or_404
from .models import Customers, Orders
from django.db.models import Sum, Count

def customers(request):

    customers_all = Customers.objects.annotate(total_sum=Sum('orders__price'))
    total_sum = customers_all.aggregate(total=Sum('total_sum'))['total']
    count = Customers.objects.aggregate(total_count = Count('name'))
    context = {
        'customers_all': customers_all,
        'sum': total_sum,
        'count': count['total_count']
    }
    
    return render(request, 'shop.html', context)

def one_customer(request, customer_name=None):
    if customer_name:
        customer = get_object_or_404(Customers, name=customer_name)
        orders = customer.orders.all()
    else:
        orders = Orders.objects.all()

    total_sum = orders.aggregate(total=Sum('price'))['total'] 
    count = orders.count()

    context = {
        'customer': customer if customer_name else None,
        'orders': orders,
        'sum': total_sum,
        'count': count,
    }
    
    return render(request, 'one.html', context)