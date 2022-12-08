from django.urls import include, path
from .views import AtivoList, AtivoDetail


urlpatterns = [
   path('ativo/', AtivoList.as_view()),
   path('item/<int:pk>', AtivoDetail.as_view()),

]