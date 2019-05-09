
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('',RedirectView.as_view(pattern_name='blog:index')),
	path('user/',include('users.urls',namespace='users')),
	path('blog/',include('blog.urls',namespace='blog')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
