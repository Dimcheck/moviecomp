from enjoyers.views import (
    MovieEnjoyersCreate,
    MovieEnjoyersList,
    MovieEnjoyersRetrieve,
    PersonalCompCreate,
    PersonalCompAppend,
    PersonalCompList,
)

from django.urls import path


app_name = 'enjoyers'

urlpatterns = [
    path('enjoyer/', MovieEnjoyersCreate.as_view(), name='enjoyer_create'),
    path('enjoyer/<int:pk>', MovieEnjoyersRetrieve.as_view(), name='enjoyers_get_one'),
    path('enjoyers/', MovieEnjoyersList.as_view(), name='enjoyers_get'),
    path('compilation/', PersonalCompCreate.as_view(), name='personal_comp_create'),
    path('compilation/<int:pk>', PersonalCompAppend.as_view(), name='personal_comp_append'),
    path('compilations/', PersonalCompList.as_view(), name='personal_comp_get'),
]