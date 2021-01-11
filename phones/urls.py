from django.urls import path

from phones.views import index, edit_phone, details_phone, \
    CreatePhoneView, DeletePhoneView, ShowPhonesView, EditPhoneView

urlpatterns = [
    path('', index, name='index'),
    path('phones/', ShowPhonesView.as_view(), name='phones'),
    path('add/', CreatePhoneView.as_view(), name='add phone'),
    path('delete_phone/<int:pk>/', DeletePhoneView.as_view(), name='delete phone'),
    path('edit_phone/<int:pk>/', edit_phone, name='edit phone'),
    path('details_phone/<int:pk>/',details_phone, name='details phone'),

]
