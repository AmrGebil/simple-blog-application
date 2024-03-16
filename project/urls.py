from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("accounts.urls"),name="acctouts"),
    path("post/", include("blog.urls"), name="blog"),
]
