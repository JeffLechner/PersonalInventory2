from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls', namespace='users')),
]

urlpatterns += [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
