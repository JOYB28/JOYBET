"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users import views as users_views
from django.contrib.auth.views import login, logout

"""from django.contrib.auth import views as auth_views"""

urlpatterns = [
    url(r'^$', users_views.user_view, name ='index'),
    url(r'^admin/', admin.site.urls),
    #url(r'^$', users_views.IndexView.as_view(), name = "root"),
    url(r'^users/', include('users.urls'), name='users'),
    url(r'^users/signup/', users_views.logout_view, name='signup'),
    url(
        r'^login/',
        login,
        name='login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    url(
        r'^logout/',
        users_views.logout_view,
        name='logout',
    ),
]
