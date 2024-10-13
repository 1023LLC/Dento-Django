from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_subject = request.POST['message_subject']
        message = request.POST['message']
        
        
        # Send an email
        send_mail(
            message_subject,
            message,
            message_email,
            ['nyerereoffice@gmail.com']
        )
        
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})