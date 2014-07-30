from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from accounts.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import  reverse

# Create your views here.

def register(request):

    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    #Render the template depending on the context

    return render_to_response('register.html',
            {'user_form':user_form,'profile_form':profile_form,
                'registered':registered}, context )


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate the user
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                #login the user
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("The Account Has Been Disabled")
        else:
            return HttpResponse("Invalid Credentials. Go back and try again.")
    else:
        return render_to_response('login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)

    url = reverse('home')
    return HttpResponseRedirect(url)
