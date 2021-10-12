from django.contrib import admin
from .models import Contact


from django.urls import path
from contact import views as contact_views


admin.site.register(Contact)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_views.contact_view, name='contact'),
]
