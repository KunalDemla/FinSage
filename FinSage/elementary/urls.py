from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index , name='elem_page'),
    path('module/<str:modules_choice>', views.modules, name='elem_modules'),
]
if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)