"""ArtHeart URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

import Planner.views as plannerViews
import Materials.views as materialsViews

urlpatterns = [
    path('admin/', admin.site.urls, name='url_admin'),
    path('login', authViews.login, name='url_login'),
    path('logout', authViews.logout, name='url_logout'),
    path('', plannerViews.index, name='url_index'),
    path('search/', materialsViews.search, name='url_search'),
    path('delete/<int:pk>', materialsViews.delete, name='url_delete'),
    path('degete_project/<int:pk>', materialsViews.delete_project, name='url_del_project'),
    path('detail/<str:pk>', materialsViews.detail, name='url_detail'),
    path('projects/', materialsViews.projects, name='url_projects'),
    path('edit_project/<int:pk>', materialsViews.edit_project, name='url_edit_project')
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)