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

