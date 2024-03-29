"""auto_scoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import scoring.views
import account.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scoring.views.home, name='home'),
    path('list/', scoring.views.list, name='list'),
    path('scoring/simple_test', scoring.views.simple_test, name='simple_test'),
    path('scoring/simple_result/<int:list_id>', scoring.views.simple_result, name='simple_result'),
    path('scoring/scoring', scoring.views.scoring, name='scoring'),
    path('scoring/analysis', scoring.views.analysis, name='analysis'),
    path('scoring/select', scoring.views.select, name='select'),
    path('scoring/result/<int:list_id>', scoring.views.result, name='result'),
    path('scoring/image_analysis', scoring.views.image_analysis, name='image_analysis'),
    path('scoring/data_analysis', scoring.views.data_analysis, name='data_analysis'),
    path('account/login', account.views.login, name='login'),
    path('account/signup', account.views.signup, name='signup'),
    path('account/logout', account.views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
