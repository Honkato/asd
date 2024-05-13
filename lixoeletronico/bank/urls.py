from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('locais-descarte/', view=views.LocaisDescarteListCreate.as_view()),
    path('locais-descarte/<pk>/', view=views.LocaisDescarteDetail.as_view()),
]+router.urls