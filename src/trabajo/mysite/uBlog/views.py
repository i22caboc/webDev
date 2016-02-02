from django.shortcuts import render

from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'uBlog/post_list.html', {'posts': posts})

#def login(request):
#	return render(request, 'uBlog/login.html', {})


def index(request):
	return render(request, 'uBlog/index.html', {})

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/post_list/')
    return render_to_response('uBlog/login.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)