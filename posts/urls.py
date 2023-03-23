from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import index, blog, post, search, create, update, delete, register_request,login_request, logout_request,password_reset_request



urlpatterns = [
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('create/', create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', update, name='post-update'),
    path('post/<id>/delete/', delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path("register", register_request, name="register"),  
    path("accounts/login/", login_request, name="login"),  
    path("accounts/logout/", logout_request, name= "logout"),
    path("password_reset", password_reset_request, name="password_reset"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
