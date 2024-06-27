from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'pages'

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('pages/', views.index, name='index'),
    path('testJson/', views.testJson, name='testJson'),
    path('getFakeApiData/', views.get_data_from_api, name='getFakeApiData'),
    path('hello-view/', views.HelloApiView.as_view()),   
    
   
   ]