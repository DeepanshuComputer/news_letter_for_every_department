"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  , include
from django.conf.urls import include
from Headline_Express import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('Subscribe', views.Subscribe, name='Subscribe'),
    path('dep_cat', views.dep_cat, name='dep_cat'),
    path('dep_cat_news', views.dep_cat_news, name='dep_cat_news'),
    path('news_letter', views.news_letter, name='news_letter'),
    path('all_news', views.all_news, name='all_news'),
    path('news_category' , views.news_category, name='news_category'),
    path('Post_news_letter', views.Post_news_letter, name='post_news_letter'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('signupuser', views.signupuser, name='signupuser'),
    path('about_us', views.about_us, name='about_us'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
