from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #third-party-apps-urls
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    
    #custom made apps urls
    path("",include("core.urls")),
    path("accounting/",include('accounting.urls')),
    path("branch/",include('branch.urls')),
    path("contact/",include('contacts.urls')),
    path("core/",include('core.urls')),
    path("inventory/",include('inventory.urls')),
    path("orders/",include('orders.urls')),
    path("tables/",include('tables.urls')), 
    path("sales/",include("sales.urls")),
    path("purchase/",include("purchase.urls"))
    
]
