from django.urls import path
from aquamatix.apps.aquamatix_mvp import views as v

urlpatterns = [
    path('', v.main, name='url_main'),
]