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
    2. Add a URL to urlpatterns:  url(r'^post/', include('post.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from post import views as post_view
from spa import views as spa_view



urlpatterns = [
    url(r'^post/', include('post.urls', namespace='post', app_name='post')),
    url(r'^account/', include('login.urls', namespace='login', app_name='login')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_view.root_view),
    url(r'^spa/', spa_view.spa_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

