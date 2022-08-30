from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.urls import reverse
from .models import Auction,Watchlist,Bid
from .forms import Auctionform
# Create your views here.


def auction_list_view(request):
    qs = Auction.objects.filter(active=True)
    context ={
        "object_list":qs,
    }
    return render(request,"auction/list.html",context)

@login_required
def add_to_watchlist(request,id):
    qs = get_object_or_404(Auction,id=id)
    if request.method=="POST" and request.user:
        obj,watchlist = Watchlist.objects.get_or_create(user=request.user,auction=qs,id=id)
    context = {
        "object":qs,
    }
    return render(request,"auction/watchlist.html",context)
@login_required
def create_list_view(request):
    form = Auctionform(request.POST or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        
        auction_obj = form.save(commit=False)
        auction_obj.user = request.user
        auction_obj.save()
        return HttpResponseRedirect(reverse("list"))
    return render(request,"auction/create.html",context)
def detail_active_view(request,id):
    qs = get_object_or_404(Auction,id=id)
    context={
        "object":qs,
    }
    print(request.user.id == None   )
    if request.method =="POST"  and "bid_form" in request.POST:
        if request.user.id != None:
            bid = request.POST.get("bid")
            curent_price = qs.cur_price
            if bid > curent_price:
                qs.cur_price = bid
                Bid.objects.create(user=request.user,auction=qs,price=bid)
                qs.save()
            else:
                context['bid_error'] = "The bid must be greater than current price ."
        else:
            return HttpResponseRedirect(reverse("login"))
    return render(request,"auction/detail.html",context)