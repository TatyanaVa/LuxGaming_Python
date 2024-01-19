from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Contact
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contacts=Contact.objects.all()
    contact_form=ContactForm()
    if request.method=='POST':
        contact_form=ContactForm(data=request.POST) 
        if contact_form.is_valid():
            
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            
            email=EmailMessage(
                "LuxGaming:Mensaje nuevo de contacto",
                f"De {name}<{email}>\n\nEscribió:\n\n{message}",
                f"{email}",
                ["luxgaming@hotmail.com"],
                reply_to=[email]
            )
            
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except Exception as ex:
                print("Excepcion",type(ex))
                return redirect(reverse('contact')+"?fail")
    return render (request,"contacts/contact.html",{'contacts':contacts,'contact_form':contact_form})
    
