from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinLengthValidator , MinValueValidator

# Create your models here.

STATE_CHOICES = (
    ('Andaman & Niconbar Islands' , 'Andaman And Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
)




print(type(STATE_CHOICES))



class Customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES , max_length=50)

    def __str__(self) -> str:
        return str(self.id)



CATEGORY_CHOICES = (
    ('M' , 'Mobile'),
    ('L' , 'Laptop'),
    ('TW' , 'Top Wear'),
    ('BW' , 'Bottom Wear'),
)




class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices = CATEGORY_CHOICES , max_length=2)
    product_image = models.ImageField(upload_to='productimg')
    
        
    def __str__(self) -> str:
        return str(self.id)



class Cart(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted' , 'Accepted'),
    ('Packed' , 'Packed'),
    ('On Way To Delivery' , 'On Way TO Delivery'),
    ('Delivered' , 'Delivered'),
    ('Cancelled' , 'Cancelled'),
    ('Pending' , 'Pending'),
)



class OrderPlaced(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1 )
    ordered_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=50 , choices=STATUS_CHOICES , default='Pending')

    def __str__(self) -> str:
        return str(self.id)
    
        
    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price


























