from django.db import models
from django.conf import settings
# Create your models here.

# aution

# catgories
# users
# 
user = settings.AUTH_USER_MODEL
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

class Auction(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    starting_bid = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(user,on_delete=models.PROTECT,null=True,blank=True)
    cur_price=models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True )
    publish = models.DateTimeField(auto_now_add=False,auto_now=True,blank=True,null=True)
    active = models.BooleanField(default=True)
class Bid(models.Model):
    user = models.ForeignKey(user,on_delete=models.PROTECT,null=True,blank=True)
    auction = models.ForeignKey(Auction,on_delete=models.PROTECT,null=True,blank=True)
    price=models.CharField(max_length=100,null=True,blank=True)

    # def save(self,*args,**kwargs):
    #     cur_price = self.price 
    #     if self.price <= self.auction.starting_bid:
    #         pass
    #     super().save(*args,*kwargs)

    #user id
    # auction id
    #price
    
class Watchlist(models.Model):
    user = models.ForeignKey(user,on_delete=models.PROTECT)
    auction = models.ForeignKey(Auction,on_delete=models.PROTECT,null=True,blank=True)
    comment = models.CharField(max_length=200,null=True,blank=True)
    #user id
    # auction id


class Comments(models.Model):
    auction = models.ForeignKey(Auction,on_delete=models.DO_NOTHING,null=True,blank=True)
    user = models.ForeignKey(user,on_delete=models.PROTECT,null=True,blank=True)
    comment = models.CharField(max_length=200)
