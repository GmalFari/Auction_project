from pydoc import cram
from venv import create
from django.urls import path
from .views import (
    create_list_view,
    auction_list_view,
    detail_active_view,
    add_to_watchlist,
)
urlpatterns = [
    path("",create_list_view,name="create-list"),
    path("list",auction_list_view,name="list"),
    path("list/<int:id>/",detail_active_view,name="detail"),
    path("watchlist/<int:id>",add_to_watchlist,name="watchlist"),


]