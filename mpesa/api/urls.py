from django.urls import path,include
from mpesa.api.views import LNMCallbackAPIView

urlpatterns = [
   
    path('lnm/', LNMCallbackAPIView.as_view(), name='lnm-callback-uel'),
]
