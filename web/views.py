from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from RGCWEB.settings import EMAIL_HOST_USER
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def Home(request):
    return render(request,'index.html')


# def SntEmail(request):
#     if request.POST:
#         username = request.POST['name']
#         email = request.POST['email'] 
#         message = request.POST['message']
#         print("username",username)
#         print("email",email)
#         mail='rgcdynamics@gmail.com'
#         print("message",message)  
#         html_content=render_to_string("mail.html",{'username':username,'email':email,'message':message})
#         text_content = strip_tags(html_content)
#         email =EmailMultiAlternatives("Enquiry from RGC website",text_content,[email],[mail])  
#         email.attach_alternative(html_content,"text/html")
#         email.send()


      
    
#     return HttpResponse('<h1>Page was found</h1>')


def SntEmail(request):
    if request.POST:
        formjs=request.POST
        print(formjs)
        name=formjs['name']
        email=formjs['email']
        message=formjs['message']
        mail='rgcdynamics@gmail.com'
        print("message",message)  
        html_content=render_to_string("mail.html",{'username':name,'email':email,'message':message})
        text_content = strip_tags(html_content)
        email =EmailMultiAlternatives("Enquiry from RGC website",text_content,[email],[mail])  
        email.attach_alternative(html_content,"text/html")
        email.send()
        return JsonResponse("Success",safe=False)

    return JsonResponse("data",safe=False)

