from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Auction , Category ,Watchlist , Bid
# Register your models here.
user = get_user_model
class AuctionAdmin(admin.ModelAdmin):
    list_display=['id','title','description','starting_bid','user','cur_price','category','publish','active']
admin.site.register(Auction,AuctionAdmin)
admin.site.register(Category)
admin.site.register(Watchlist)
admin.site.register(Bid)