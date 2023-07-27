from django.shortcuts import render ,redirect
from django.http import HttpResponse
from mysite.models import Contact,Product,Category


def home (request):
    data=Product.objects.all()
    selec=Category.objects.all()

    print(data)
    context={
       'products':data
    }
    return render(request,'index.html',{"select":selec, "products":data} )
def product_detail(request,id):
   data=Product.objects.get(id=id)
   context={
      'product':data
   }
   
   return render(request,'product_detail.html',context,)
def about (request):
    return render(request, 'about.html')
def contact (request): 
   data=Contact.objects.all().order_by('-id')
   if request.method=='POST':
    name=request.POST['fullname']
    email=request.POST['email']
    phone=request.POST['phone']
    subject=request.POST['subject']
    body=request.POST['body']
    print(name,email,phone,subject,body)
    data=Contact(fullname=name,email=email,phone=phone,subject=subject,body=body)
    data.save()
    
    return redirect("/contact")
   return render(request,'contact.html',{'data': data})

def search(request):
   data=Product.objects.all()
   selec=Category.objects.all()
   nom=request.GET['nom']
   mual=request.GET['mual']
   yil=request.GET['yil']
   cat=request.GET['cat']
   if nom:
      data = data.filter(book_name__icontains=nom)
   if mual:
      data = data.filter(book_author__icontains=mual)
   if yil:
      data = data.filter(book_year__icontains=yil)
   if cat:
      data = data.filter(cat_id=cat)
  
   return render(request,'index.html',{"products":data, "select":selec}  )

def searchall(request):
   data=Product.objects.all()
   
   nom=request.GET['soz']
   
   if nom:
      data = Product.objects.filter(book_name__icontains=nom,
      book_author__icontains=nom,
      book_year__icontains=nom)


   return render(request,'index.html',{"products":data} )


def maqola (request):
    data=Product.objects.filter(cat_id__exact=9)
   
    print(data)
    context={
       'products':data
    }
    return render(request,'maqola.html',context )

