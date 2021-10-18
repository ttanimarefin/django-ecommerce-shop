from django.shortcuts import render
from django.http import HttpResponse
from account.forms import RegistrationForm
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return HttpResponse('You Are Redirect to base url ')

    else:
        form=RegistrationForm()
        if request.method == 'post' or request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('Account Created')
    context={
        'form':form
    }
    return  render(request, 'register.html')