from django.db import models

class Contact (models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=30)
    subject=models.CharField(max_length=250)
    body=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.fullname}  | {self.subject}'
    
class Category(models.Model):
        cat_name=models.CharField(max_length=50)
        cat_photo=models.ImageField(upload_to='uploads/')
        created_date=models.DateTimeField(auto_now_add=True)
        updated_date=models.DateTimeField(auto_now=True)

        def __str__(self):
            return f'{self.cat_name}'
       
class Product(models.Model):
            cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)
            book_name=models.CharField(max_length=50)
            book_decs=models.TextField()
            book_price=models.FloatField()
            book_year=models.CharField(max_length=20)
            book_author=models.CharField(max_length=100)
            book_img=models.ImageField(upload_to='products/')
            book_isExist=models.BooleanField(default=False)
            created_date=models.DateTimeField(auto_now_add=True)
            updated_date=models.DateTimeField(auto_now=True)
            book_file=models.FileField(upload_to='books/')
            

def __str__(self):
            return f'{self.product_name}'
