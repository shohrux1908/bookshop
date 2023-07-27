from django.contrib import admin
from mysite.models import Contact,Category,Product

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','fullname','email','phone','subject','body']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Category)
admin.site.register(Product)

