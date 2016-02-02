from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    #url(r'^$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^login/$', views.login_user, name='login_user'),
    #url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'})
    # url(r'^blog/', include('blog.urls')),
]