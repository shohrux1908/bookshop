from django.contrib import admin
from django.urls import path
from mysite.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home-page'),
    path('search',search),
    path('searchall',searchall),
    path('maqola',maqola,name="maqola-page"),
    path('about/',about,name='about-page'),
    path('contact/',contact,name='contact-page'),
    path('product-detail/<int:id>',product_detail,name='product_detail_page'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  