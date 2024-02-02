
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #link the applications with urls
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('chatting/', include('chatting.urls')),
    path('accounts/', include('accounts.urls')),
    # path('fm/', include('fm.urls')),
    path('order/', include('order.urls')),
    path('property/', include('property.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
