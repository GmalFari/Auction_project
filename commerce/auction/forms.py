from django import forms
from .models import Category, Watchlist,Bid,Auction,Comments


class Auctionform(forms.ModelForm):
    required_css_class="required-field"
    error_css_class = "error-field"
    title = forms.CharField(help_text="This is help text <a href='#'>contact us </a>")
    class Meta:
        model = Auction
        fields=['title','description', 'starting_bid','category']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({"placeholder":f"Recipe {str(field)}","class":"form-control-2"})
        self.fields['description'].widget.attrs.update({"rows":'2'})
