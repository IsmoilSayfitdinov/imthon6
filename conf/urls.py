from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.views import Products_view_function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls', namespace="news")),
     path('news-details/<int:pk>/', Products_view_function.as_view(), name="news_details"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)