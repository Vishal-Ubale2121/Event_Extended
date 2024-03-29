"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from events import views
from django.contrib.auth import views as auth_views
from events.views import Music,Index2,Show,Formset,Delete,SkinBurn

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^events/$', views.EventsListView.as_view(), name='events'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-details'),
    path('Music', Music.as_view()),
    path('reg_form', Index2.as_view()),
    path('show', Show.as_view()),
    path('formset', Formset.as_view()),
    path('SkinBurn', SkinBurn.as_view()),
    path('delete/<int:id>/', Delete.as_view(), name='show'),
]
