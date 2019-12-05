from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField( max_length =  50)
    category = models.CharField(max_length = 50 , default = '')
    sub_category = models.CharField(max_length = 50 , default = '')
    prize = models.IntegerField(default=0)
    pub_date = models.DateField()
    product_disc = models.CharField( max_length = 300)
    product_image = models.ImageField(default='', upload_to="shop/image")

    def __str__(self) :
        return self.product_name

