from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.

STATE_CHOICES=(
    ('Gujarat','Gujarat'),
    ('Maharashtra','Maharashtra'),
    ('Delhi','Delhi'),
    ('MP','MP')
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('BW','Bridal Wear'),
    ('GW','Groom Wear'),
    ('BM','Bridal Makeup'),
    ('MA','Mahendi Artist'),
    ('CS','Catering Service'),
    ('P','Photographers'),
    ('D','Decorations'),
    ('BH','Banquet Hall'),

)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    location=models.CharField(max_length=200)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return  self.product.selling_price

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Cancel','Cancel')

)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Cancel')

    @property
    def total_cost(self):
        return  self.product.selling_price