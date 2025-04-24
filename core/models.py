from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerDetail(models.Model):
    STATE_CHOICES = [
       ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu and Kashmir'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'), 
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    pincode = models.IntegerField(
        default=0,
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.id)
    
class Tool(models.Model):

    CATEGORY_CHOICES = [
        ('PAINTS & MEDIUMS','Paints & Mediums'),
        ('SURFACES & TOOLS', 'Surfaces & Tools'),
        ('CREATIVE TOOLS','Creative Tools'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    small_description = models.CharField(max_length=30)
    description = models.TextField()
    original_price = models.IntegerField()
    discounted_price = models.IntegerField()
    tools_image = models.ImageField(upload_to='tools_images')

    def __str__(self):
        return str(self.name)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Tool, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)        

    def __str__(self):
        return str(self.id)
    
    @property
    def price_and_quantity_total(self):
        return self.product.discounted_price*self.quantity
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    

    def __str__(self):
        return str(self.id)




