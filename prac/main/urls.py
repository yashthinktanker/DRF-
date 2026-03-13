from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('Modelfilter',views.Modelfilter,basename='Modelfilter')

router.register('brand',views.BrandV,basename='brand')
router.register('model_name',views.Model_nameV,basename='model_name')

router.register('jwtgetmodel_name',views.jwtgetmodel_name,basename='jwtgetmodel_name')

# Instagram
router.register('Instauserview',views.Instauserview,basename='Instauserview')
router.register('InstaPostview',views.InstaPostview,basename='InstaPostview')
router.register('InstaPostLikeview',views.InstaPostLikeview,basename='InstaPostLikeview')
router.register('LoginView',views.LoginView,basename='LoginView')
router.register('LogoutView',views.LogoutView,basename='LogoutView')




urlpatterns = [
    path('',include(router.urls)),
    path('brandlist',views.brandlist),
    path('branddp/<int:id>',views.branddp),


    path('Brandapiview/',views.Brandapiview.as_view()),
    path('Brandapiview/<int:id>/',views.Brandapiview.as_view()),


    path('Brandlistapi',views.Brandlistapi.as_view()),

    path('brandmix/',views.brandmix.as_view()),
    path('brandmix/<int:pk>',views.brandmix.as_view()),

    path('brandpage/',views.brandpage.as_view()),
   
]
