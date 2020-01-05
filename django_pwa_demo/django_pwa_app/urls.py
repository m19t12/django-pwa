from django.urls import path
from django_pwa_demo.django_pwa_app.views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index')
]
