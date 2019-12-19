from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField( max_length =  50)
    product_category = models.CharField(max_length = 50 , default = '')
    product_sub_category = models.CharField(max_length = 50 , default = '')
    product_prize = models.IntegerField(default=0)
    product_pub_date = models.DateField()
    product_disc = models.CharField( max_length = 300)
    product_image = models.ImageField(default='', upload_to="shop/image")
    product_rating = models.FloatField(max_length= 5.0 , default= 0.0 )

    def __str__(self) :
        return self.product_name

class Contact(models.Model):
    id = models.AutoField(primary_key= True )
    name = models.CharField(max_length = 70)
    email = models.CharField(max_length = 70)
    phone = models.CharField(max_length = 13)
    disc = models.CharField(max_length = 500)

    def __str__(self):
        return self.name

class Order(models.Model):
    ord_id = models.AutoField(primary_key = True)
    ord_items = models.CharField(max_length = 500)
    ord_name = models.CharField(max_length = 500)
    ord_email = models.CharField(max_length = 500)
    ord_city = models.CharField(max_length = 500)
    ord_state = models.CharField(max_length = 500)
    ord_add1 = models.CharField(max_length = 500)
    ord_add2 = models.CharField(max_length = 500)
    ord_zip = models.CharField(max_length = 500)

    def __str__(self):
        return self.ord_name

class OrderUpdate(models.Model):
    orderUpId = models.AutoField(primary_key=True)
    orderId = models.IntegerField(default= '')
    orderDisc = models.CharField(max_length=500)
    orderUpTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.orderId)
        