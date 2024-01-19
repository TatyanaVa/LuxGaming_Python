from django.shortcuts import render,get_object_or_404
from .models import Product,Section
# Create your views here.
def product(request):
    product=Product.objects.all()
    return render (request,"product/product.html",{'product':product})

def section(request,section_id):
    #category=Category.objects.get(id=category_id)
    section=get_object_or_404(Section,id=section_id)
    product=Product.objects.filter(section=section)
    return render(request, "product/section.html", {'product':product})