from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    # path('', views.home),
    path('',views.ProductView.as_view(),name="home"),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),

    path('removecart/',views.remove_cart),

    path('paymentdone/',views.payment_done,name='paymentdone'),

    # path('profile/', views.profile, name='profile'),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('bridal_makeup/', views.bridal_makeup, name='bridal_makeup'),


    path('bridal_wear/', views.bridal_wear, name='bridal_wear'),
    path('groom_wear/', views.groom_wear, name='groom_wear'),
    path('mehendi_artist/', views.mehendi_artist, name='mehendi_artist'),
    path('catering_service/', views.catering_service, name='catering_service'),
    path('photographers/', views.photographers, name='photographers'),
    path('decor/', views.decor, name='decor'),
    path('hall/', views.hall, name='hall'),

    # path('login/', views.login, name='login'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm) ,name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('registration/',views.CustomerRegistrationView.as_view(),name="customerregistration")
] + static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
