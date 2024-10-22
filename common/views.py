from django.shortcuts import render
from .forms import RegisterUserForm

# Create your views here.
def home(request):

    return render(request, 'common/home.html')


def create_user(request):

    if request.method == 'POST':
        form = RegisterUserForm( request.POST or None )
        form.save()
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html',{'form':form})