from django.urls import path
from . import views

urlpatterns = [
    path('nfcid', views.nfctag_create, name='nfctag_create'),
    path('insertNFCIDList', views.nfc_summon, name='nfc_summon'),
    path('ReloadNFC', views.nfctag_change, name='nfctag_change'),
    path('deleteNFC', views.nfctag_delete, name='nfctag_delete'),
    path('AddPunchIn', views.return_user, name='return_user'),
]
