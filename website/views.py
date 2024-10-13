from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})