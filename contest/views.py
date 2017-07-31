# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
# -*- coding: utf-8 -*-
from django.views.generic import View
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .form import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Picture


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            current_site = get_current_site(request)
            subject = 'Activate your blog account.'
            message = render_to_string('contest/acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # user.email_user(subject, message)
            toemail = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'contest/signup.html', {'form': form})
def home(request):
    return render(request,"contest/a.html")

def page(request,user_id):
    user=Picture.objects.get(pk=user_id)
    if user.favourite==True:
        user.favourite=False
        user.like-=1
        user.save()
    else:
        user.favourite=True
        user.like+=1
        user.save()
    return redirect("contest:detail")
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        #return redirect('contest/a.html')
    else:
        return HttpResponse('Activation link is invalid!')
class EntryCreate(CreateView):
    model=Picture
    template_name="contest/album_form.html"
    fields=['user','name','image']
def detail(request):
    user=Picture.objects.all()
    return render(request,"contest/page.html",{'user':user})