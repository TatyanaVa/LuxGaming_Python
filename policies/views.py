from django.shortcuts import render,get_list_or_404
from .models import Policies,Category

# Create your views here.
def policies(request):
    policies=Policies.objects.all()
    return render (request,"policies/policies.html",{'policies':policies})

def category(request,category_id):
    #category=Category.objects.get(id=category_id)
    category=get_list_or_404(Category,id=category_id)
    policies=Policies.objects.filter(category=category)
    return render(request, "policies/category.html", {'policies':policies})