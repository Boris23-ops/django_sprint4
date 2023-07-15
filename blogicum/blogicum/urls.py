import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('auth/registration/',
         views.RegistrationCreateView.as_view(),
         name='registration'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('blog.urls')),
    path('', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.e_handler500'
