from django.shortcuts import render,get_object_or_404,reverse,redirect
from . models import Products,Order
from django.core.paginator import Paginator

from django.views.generic import ListView, CreateView, DetailView, TemplateView


from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseNotFound
import stripe,json
#import json
from .forms import ProductForm,UserRegistrationForm
from django.db.models import Sum
import datetime
 
# Create your views here.

def index(request):
    product_objects = Products.objects.all()  # This code represents the list of all the products

    ######### 👇👇👇👇This is the SEARCH BAR code BELOW 👇👇👇👇 #########

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    ######### ☝️☝️☝️☝️This is the SEARCH BAR code ABOVE ☝️☝️☝️☝️##########




    ######### 👇👇👇👇This is the PAGINATOR code BELOW 👇👇👇👇 ##########

    #paginator = Paginator(product_objects,500)
    #page = request.GET.get('page')
    #product_objects = paginator.get_page(page)

    ######### ☝️☝️☝️☝️This is the PAGINATOR code ABOVE ☝️☝️☝️☝️############


    return render(request,'shop/index.html',{'product_objects':product_objects}) # ":" is read as "as".  dictionary



def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})






def checkout(request):


    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")




        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()



    return render(request,'shop/checkout.html')
    #return render(request,'http://127.0.0.1:8000/')
    #product_page = Products.objects.get(id=id)
    #return render(request,'shop/detail.html',{'product_page':product_page})   






'''

@csrf_exempt
def create_checkout_session(request,id):
    request_data = json.loads(request.body)
    product = Products.objects.get(id=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        customer_email = request_data['email'],
        payment_method_types = ['card'],
        line_items=[
            {
                'price_data':{
                    'currency':'usd',
                    'product_data':{
                        'name':product.name,
                    },
                    'unit_amount':int(product.price * 100)
                },
                'quantity':1,
            }
        ],
        mode='payment',
        success_url = request.build_absolute_uri(reverse('success')) +
        "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url = request.build_absolute_uri(reverse('failed')),
        
    )
    
    order = Order()
    order.customer_email = request_data['email']
    order.product = product
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.amount = int(product.price)
    order.save()
    
    return JsonResponse({'sessionId':checkout_session.id})




def payment_success_view(request):
    session_id = request.GET.get('session_id')
    if session_id is None:
        return HttpResponseNotFound()
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.retrieve(session_id)
    order = get_object_or_404(Order,stripe_payment_intent= session.payment_intent)
    order.has_paid=True
    # updating sales stats for a product
    product = Products.objects.get(id=order.product.id)
    product.total_sales_amount = product.total_sales_amount + int(product.price)
    product.total_sales = product.total_sales + 1
    product.save()
    # updating sales stats for a product
    order.save()
    
    return render(request,'shop/payment_success.html',{'order':order})





def payment_failed_view(request):
    return render(request,'shop/failed.html')






def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return redirect('index')
    user_form = UserRegistrationForm()
    return render(request,'shop/register.html',{'user_form':user_form})





def invalid(request):
    return render(request, 'shop/invalid.html')


        
'''

