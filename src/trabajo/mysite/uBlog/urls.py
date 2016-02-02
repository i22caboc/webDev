from django.conf.urls import url
from . import views



from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    # Examples:
    #url(r'^$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^login/$', views.login_user, name='login_user'),
    #url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # url(r'^blog/', include('blog.urls')),
	url(r'^register/', CreateView.as_view(
            template_name='uBlog/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
]