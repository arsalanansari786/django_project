from django.contrib import admin
from django.urls import path, include

from arsalan.members.views import ReactView

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('members.urls')),
     path('wel/',ReactView.as_view(),name="something"),
]
