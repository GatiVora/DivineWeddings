# from unicodedata import category
# from django.db.models import Q
# from django.http import JsonResponse
# from django.shortcuts import redirect, render
# from django.views import View
# from .models import Customer,Product,Cart,OrderPlaced
# from .forms import CustomerRegistrationForm,CustomerProfileForm
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# class ProductView(View):
#     def get(self,request):
#         bridal_makeup=Product.objects.filter(category='BM')
#         bridal_wear=Product.objects.filter(category='BW')
#         groom_wear=Product.objects.filter(category='GW')
#         mehendi_artist=Product.objects.filter(category='MA')
#         catering_service=Product.objects.filter(category='CS')
#         photographers=Product.objects.filter(category='P')
#         decor=Product.objects.filter(category='D')
#         hall=Product.objects.filter(category='BH')

#         return render(request,'app/home.html',
#         {'bridal_makeup':bridal_makeup,'bridal_wear':bridal_wear,'groom_wear':groom_wear,'mehendi_artist':mehendi_artist,'catering_service':catering_service,'photographers':photographers,'decor':decor,'hall':hall})

# def home(request):
#  return render(request, 'app/home.html')

# # def product_detail(request):
# #  return render(request, 'app/productdetail.html')

# class ProductDetailView(View):
#     def get(self,request,pk):
#         product=Product.objects.get(pk=pk)
#         item_already_in_cart=False
#         if request.user.is_authenticated:
#             item_already_in_cart=Cart.objects.filter(Q(product=product.id)& Q(user=request.user)).exists()
#         return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})

# def add_to_cart(request):
#     user=request.user
#     product_id= request.GET.get('prod_id')
#     product = Product.objects.get(id=product_id)
#     Cart(user=user,product=product).save()
#     return redirect('/cart')

# def show_cart(request):
#     if request.user.is_authenticated:
#         user =request.user
#         cart=Cart.objects.filter(user=user)
#         # print(cart)
#         amount=0.0
#         total_amount=0.0
#         cart_product=[p for p in Cart.objects.all () if p.user == user]
#         # print(cart_product)
#         if cart_product:
#             for p in cart_product:
#                 tempamount = (p.product.selling_price)
#                 amount+=tempamount
#                 totalamount=amount

#             return render(request,'app/addtocart.html',{'carts':cart, 'totalamount':totalamount, 'amount':amount})
#         else:
#             return render(request,'app/emptycart.html')

# def buy_now(request):
#  return render(request, 'app/buynow.html')

# # def profile(request):
# #  return render(request, 'app/profile.html')



# def remove_cart(request):
#     if request.method == 'GET':
#         prod_id = request.GET['prod_id']
#         c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
#         # c.quantity-=1
#         c.delete()
#         amount =0.0
#         # shipping_amount =70.0
#         cart_product=[p for p in Cart.objects.all() if p.user == request.user]
#         for p in cart_product:
#             tempamount=(p.product.selling_price)
#             amount+=tempamount
#             # totalamount=amount
        
#         data={
#             'amount':amount,
#             'totalamount':amount
#         }
#         return JsonResponse(data)




# def address(request):
#     add = Customer.objects.filter(user=request.user)
#     return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

# def orders(request):
#     op=OrderPlaced.objects.filter(user=request.user)
#     return render(request, 'app/orders.html',{'order_placed':op})

# def change_password(request):
#  return render(request, 'app/changepassword.html')

# def mobile(request,data=None):
#     if data==None:
#         bridal_makeup=Product.objects.filter(category='BM')
#     # elif data=="below":
#     #     bridal_makeup=Product.objects.filter
#     return render(request, 'app/mobile.html',{'bridal_makeup':bridal_makeup})


# def bridal_makeup(request,data=None):
#     if data==None:
#         bridal_makeup=Product.objects.filter(category='BM')
#     # elif data=="below":
#     #     bridal_makeup=Product.objects.filter
#     return render(request, 'app/bridal_makeup.html',{'bridal_makeup':bridal_makeup})

# def bridal_wear(request,data=None):
#     if data==None:
#         bridal_wear=Product.objects.filter(category='BW')
#     # elif data=="below":
#     #     bridal_makeup=Product.objects.filter
#     return render(request, 'app/bridal_wear.html',{'bridal_wear':bridal_wear})

# def groom_wear(request,data=None):
#     if data==None:
#         groom_wear=Product.objects.filter(category='GW')
#     # elif data=="below":
#     #     bridal_makeup=Product.objects.filter
#     return render(request, 'app/groom_wear.html',{'groom_wear':groom_wear})

# def mehendi_artist(request,data=None):
#     if data==None:
#         mehendi_artist=Product.objects.filter(category='MA')
#     # elif data=="below":
#     #     bridal_makeup=Product.objects.filter
#     return render(request, 'app/mehendi_artist.html',{'mehendi_artist':mehendi_artist})

# def catering_service(request,data=None):
#     if data==None:
#         catering_service=Product.objects.filter(category='CS')
#     # elif data=="below":
#     #     bridal_makeup=Product.objects.filter
#     return render(request, 'app/catering_service.html',{'catering_service':catering_service})

# def photographers(request,data=None):
#     if data==None:
#         photographers=Product.objects.filter(category='P')
#     # elif data=="below":
#     #     bridal_makeup=Product.objects.filter
#     return render(request, 'app/photographers.html',{'photographers':photographers})

# def decor(request,data=None):
#     if data==None:
#         decor=Product.objects.filter(category='D')
#     # elif data=="below":
#     #     bridal_makeup=Product.objects.filter
#     return render(request, 'app/decor.html',{'decor':decor})

# def hall(request,data=None):
#     if data==None:
#         hall=Product.objects.filter(category='BH')
#     # elif data=="below":
#     #     bridal_makeup=Product.objects.filter
#     return render(request, 'app/hall.html',{'hall':hall})

# # def login(request):
# #  return render(request, 'app/login.html')

# # def customerregistration(request):
# #  return render(request, 'app/customerregistration.html')

# class CustomerRegistrationView(View):
#     def get(self,request):
#         form=CustomerRegistrationForm()
#         return render(request, 'app/customerregistration.html',{'form':form})
#     def post(self,request):
#         form=CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             messages.success(request,'Congratulations!! Registered Successfully')
#             form.save()
#         return render(request, 'app/customerregistration.html',{'form':form})

# @login_required    
# def checkout(request):

#     user=request.user
#     add  = Customer.objects.filter(user=user)
#     cart_items= Cart.objects.filter(user=user)
#     amount=0.0
#     totalamount= 0.0
#     cart_product=[p for p in Cart.objects.all() if p.user == request.user]
#     if cart_product:
#         for p in cart_product:
#             tempamount= (p.product.selling_price)
#             amount+=tempamount
#         totalamount=amount
#     return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items})

# def payment_done(request):
#     user=request.user
#     custid=request.GET.get('custid')
#     customer = Customer.objects.get(id=custid)
#     cart= Cart.objects.filter(user=user)
#     for c in cart :
#         OrderPlaced(user=user,customer=customer,product=c.product).save()
#         c.delete()
#     return redirect("orders")

# @method_decorator(login_required,name='dispatch')
# class ProfileView(View):
#     def get(self,request):
#         form=CustomerProfileForm()
#         return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

#     def post(self,request):
#         form=CustomerProfileForm(request.POST)
#         if form.is_valid():
#             usr=request.user
#             name = form.cleaned_data['name']
#             locality =form.cleaned_data['locality']
#             city= form.cleaned_data['city']
#             state= form.cleaned_data['state']
#             reg =Customer(user=usr,name=name, locality=locality, city=city,
#             state=state)
#             reg.save()
#             messages.success (request, 'Congratulations!! Profile Updated Successfully')
#         return render(request, 'app/profile.html', {'form': form,'active':'btn-primary'})




from unicodedata import category
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

class ProductView(View):
    def get(self,request):
        bridal_makeup=Product.objects.filter(category='BM')
        bridal_wear=Product.objects.filter(category='BW')
        groom_wear=Product.objects.filter(category='GW')
        mehendi_artist=Product.objects.filter(category='MA')
        catering_service=Product.objects.filter(category='CS')
        photographers=Product.objects.filter(category='P')
        decor=Product.objects.filter(category='D')
        hall=Product.objects.filter(category='BH')

        return render(request,'app/home.html',
        {'bridal_makeup':bridal_makeup,'bridal_wear':bridal_wear,'groom_wear':groom_wear,'mehendi_artist':mehendi_artist,'catering_service':catering_service,'photographers':photographers,'decor':decor,'hall':hall})

def home(request):
 return render(request, 'app/home.html')

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        item_already_in_cart=False
        if request.user.is_authenticated:
            item_already_in_cart=Cart.objects.filter(Q(product=product.id)& Q(user=request.user)).exists()
        return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})

def add_to_cart(request):
    user=request.user
    product_id= request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user =request.user
        cart=Cart.objects.filter(user=user)
        # print(cart)
        amount=0.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all () if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.product.selling_price)
                amount+=tempamount
                totalamount=amount

            return render(request,'app/addtocart.html',{'carts':cart, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request,'app/emptycart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')



def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        # c.quantity-=1
        c.delete()
        amount =0.0
        # shipping_amount =70.0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount=(p.product.selling_price)
            amount+=tempamount
            # totalamount=amount
        
        data={
            'amount':amount,
            'totalamount':amount
        }
        return JsonResponse(data)




def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):
    op=OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'order_placed':op})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
        bridal_makeup=Product.objects.filter(category='BM')
    # elif data=="below":
    #     bridal_makeup=Product.objects.filter
    return render(request, 'app/mobile.html',{'bridal_makeup':bridal_makeup})


def bridal_makeup(request,data=None):
    if data==None:
        bridal_makeup=Product.objects.filter(category='BM')
    # elif data=="below":
    #     bridal_makeup=Product.objects.filter
    return render(request, 'app/bridal_makeup.html',{'bridal_makeup':bridal_makeup})

def bridal_wear(request,data=None):
    if data==None:
        bridal_wear=Product.objects.filter(category='BW')
    # elif data=="below":
    #     bridal_makeup=Product.objects.filter
    return render(request, 'app/bridal_wear.html',{'bridal_wear':bridal_wear})

def groom_wear(request,data=None):
    if data==None:
        groom_wear=Product.objects.filter(category='GW')
    # elif data=="below":
    #     bridal_makeup=Product.objects.filter
    return render(request, 'app/groom_wear.html',{'groom_wear':groom_wear})

def mehendi_artist(request,data=None):
    if data==None:
        mehendi_artist=Product.objects.filter(category='MA')
    # elif data=="below":
    #     bridal_makeup=Product.objects.filter
    return render(request, 'app/mehendi_artist.html',{'mehendi_artist':mehendi_artist})

def catering_service(request,data=None):
    if data==None:
        catering_service=Product.objects.filter(category='CS')
    # elif data=="below":
    #     bridal_makeup=Product.objects.filter
    return render(request, 'app/catering_service.html',{'catering_service':catering_service})

def photographers(request,data=None):
    if data==None:
        photographers=Product.objects.filter(category='P')
    # elif data=="below":
    #     bridal_makeup=Product.objects.filter
    return render(request, 'app/photographers.html',{'photographers':photographers})

def decor(request,data=None):
    if data==None:
        decor=Product.objects.filter(category='D')
    # elif data=="below":
    #     bridal_makeup=Product.objects.filter
    return render(request, 'app/decor.html',{'decor':decor})

def hall(request,data=None):
    if data==None:
        hall=Product.objects.filter(category='BH')
    # elif data=="below":
    #     bridal_makeup=Product.objects.filter
    return render(request, 'app/hall.html',{'hall':hall})

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})

@login_required    
def checkout(request):

    user=request.user
    add  = Customer.objects.filter(user=user)
    cart_items= Cart.objects.filter(user=user)
    amount=0.0
    totalamount= 0.0
    cart_product=[p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount= (p.product.selling_price)
            amount+=tempamount
        totalamount=amount
        totl=amount*100
    return render(request, 'app/checkout.html',{"total":totl,'add':add,'totalamount':totalamount,'cart_items':cart_items})

def payment_done(request):
    user=request.user
    custid=request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart= Cart.objects.filter(user=user)
    for c in cart :
        OrderPlaced(user=user,customer=customer,product=c.product).save()
        c.delete()
    return redirect("orders")

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user
            name = form.cleaned_data['name']
            locality =form.cleaned_data['locality']
            city= form.cleaned_data['city']
            state= form.cleaned_data['state']
            reg =Customer(user=usr,name=name, locality=locality, city=city,
            state=state)
            reg.save()
            messages.success (request, 'Congratulations!! Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form': form,'active':'btn-primary'})



def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 200000

        client = razorpay.Client(
            auth=("rzp_test_ULKXFl3prtGM7z", "IQyDNCHgqTTcZj1SGroTb0Cl"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'checkout.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")
