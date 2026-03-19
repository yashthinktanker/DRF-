from django.shortcuts import render
from main.serializer import *


# ------------- viewsset ---------------
from rest_framework  import viewsets

class BrandV(viewsets.ModelViewSet):
    queryset=Brand.objects.all()
    serializer_class = Brandserializers

# class Model_nameV(viewsets.ModelViewSet):
#     queryset=Model_name.objects.all()
#     serializer_class = Model_nameserializers


# ------------ @apiview ------------------

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['get','post'])
def brandlist(request):
    if request.method == 'GET':
        b=Brand.objects.all()
        seri=Brandserializers(b,many=True)
        print('seri: ', seri)
        return Response({'data':seri.data})
    if request.method == 'POST':
        data=request.data
        seri=Brandserializers(data=data)
        print('seri: ', seri)
        if seri.is_valid():
            seri.save()
            return Response({'message':"data add",'data':seri.data})
        return Response({'message':seri.error})
    
@api_view(['put','patch','delete'])   
def branddp(request,id):
    b=Brand.objects.get(id=id)
    if request.method == 'PUT':
        data = request.data
        seri = Brandserializers(b,data=data)
        print('seri: ', seri)
        if seri.is_valid():
            seri.save()
            return Response({'message':"data Update",'data':seri.data})
        return Response({'message':seri.error})
    if request.method == 'PATCH':
        data = request.data
        seri = Brandserializers(b,data=data,partial = True)
        print('seri: ', seri)
        if seri.is_valid():
            seri.save()
            return Response({'message':"data Update",'data':seri.data})
        return Response({'message':seri.error})
    if request.method == 'DELETE':
        b.delete()
        return Response({'message':"data delete"})

# -------------- APIView Class ---------------------
from rest_framework.views import APIView

class Brandapiview(APIView):
    def get(self,request,id=None):
        b=Brand.objects.all()
        seri=Brandserializers(b,many=True)
        print('seri: ', seri)
        return Response({'data':seri.data})
    def post(self,request,id=None):
        data=request.data
        seri=Brandserializers(data=data)
        print('seri: ', seri)
        if seri.is_valid():
            seri.save()
            return Response({'message':"data add",'data':seri.data})
        return Response({'message':seri.error})
    def put(self,request,id):
        brand = Brand.objects.get(id=id)
        data=request.data
        seri=Brandserializers(brand,data=data)
        print('seri: ', seri)
        if seri.is_valid():
            seri.save()
            return Response({'message':"data update",'data':seri.data})
        return Response({'message':seri.error})

    def patch(self,request,id):
        brand = Brand.objects.get(id=id)
        data=request.data
        seri=Brandserializers(brand,data=data,partial = True)
        print('seri: ', seri)
        if seri.is_valid():
            seri.save()
            return Response({'message':"data update",'data':seri.data})
        return Response({'message':seri.error})
    
    def delete(self,request,id):
        brand = Brand.objects.get(id=id)
        brand.delete()
        return Response({'message': "Data Deleted"})
    
#  ------------ ListApiView --------------
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView


class Brandlistapi(ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=Brandserializers

# -------- MIXINS AND GENRIC --------------
from rest_framework import mixins,generics

class brandmix(    
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Brand.objects.all()
    serializer_class = Brandserializers

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        return self.list(request)
    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk=pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk=pk)
    

# --------- permission -------------
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
class Model_nameV(viewsets.ModelViewSet):
    queryset=Model_name.objects.all()
    serializer_class = Model_nameserializers
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]

# ----------- JWT Authentication ----------- 

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class jwtgetmodel_name(viewsets.ModelViewSet):
    queryset=Model_name.objects.all()
    serializer_class = Model_nameserializers
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

# ----------- filtering ------------
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class Modelfilter(viewsets.ModelViewSet):
    queryset = Model_name.objects.all()
    serializer_class = Model_nameserializers
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['color']
    search_fields = ['^modelname','color']
    ordering_fields = ['id']

# ---------- pagination  ------------
from main.mypagination import mypaginatior

class brandpage(ListAPIView):
    queryset = Model_name.objects.all()
    serializer_class = Model_nameserializers 
    pagination_class = mypaginatior


# ------------- Throttling ------------------

# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
# class Model_nameV(viewsets.ModelViewSet):
#     queryset=Model_name.objects.all()
#     serializer_class = Model_nameserializers
#     throttle_classes = [AnonRateThrottle,UserRateThrottle]


# ---------------- Insta User ADd ------------------
from django.db.models import Q
class Instauserview(viewsets.ModelViewSet):
    serializer_class = InstaUserSerializer
    def  get_queryset(self):
        username = self.request.session.get('username')

        # if username:
        #     return InstaUser.objects.filter(is_private=False)
        if username:
            return InstaUser.objects.filter(Q(is_private=False) | Q(username=username))

        return InstaUser.objects.none()

from rest_framework.exceptions import PermissionDenied

class InstaPostview(viewsets.ModelViewSet):
    serializer_class = InstaPostSerializer
    queryset = InstaPost.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        print("these functions")
        user_id = self.request.session.get('username')

        if not user_id:
            raise PermissionDenied("Please login first")

        serializer.save(user_id=user_id)    




# class InstaPostLikeview(viewsets.ModelViewSet):
#     queryset = InstaLike.objects.all()
#     serializer_class = InstaPostLikeSerializer

# --------- ALL data deleted -----------
from rest_framework.decorators import action

class InstaPostLikeview(viewsets.ModelViewSet):
    queryset = InstaLike.objects.all()
    serializer_class = InstaPostLikeSerializer



    @action(detail=False, methods=['delete'])
    def delete_all(self,request):
        c=InstaLike.objects.all().delete()
        return Response ({
            'message':f'all data is deletes{c}'
        })
    

import random
from django.core.mail import send_mail,EmailMessage
from rest_framework.reverse import reverse

from rest_framework_simplejwt.tokens import RefreshToken
class LoginView(viewsets.ViewSet):

    def list(self,request):
        user = request.session.get('username',None)
        if user:
            return Response({"message": "ALready Login Pls logout"})
        else:
            return Response({"message": "Enter Username And Password"})
    def create(self, request):
        user = request.session.get('username',None)
        if user:
            return Response({"message": "ALready Login Pls logout"})
        
        username = request.data.get("username")
        password = request.data.get("password")

        if not username and not password:
            return Response({"message": "Enter Username And Password"})
        if not username:
            return Response({"message": "Enter Username "})
        if not password:
            return Response({"message": "Enter Password"})

        
        try:
            user = InstaUser.objects.get(username=username)
        except InstaUser.DoesNotExist:
            return Response({"error": "Invalid Username"})

        if user.password == password:
            refresh = RefreshToken.for_user(user)
            otp = str(random.randint(100000, 999999))
            print('otp: ', otp)
              # store OTP in session
            request.session['otp'] = otp
            request.session['username']=user.id
            request.session.save()

            EmailMessage(
                "Your OTP",
                f"Your login OTP is {otp}",
                None,
                [user.email],
            ).send()
            otp_url = reverse("Otpverification-list", request=request)
            return Response({"message": "OTP sent to email",'url':otp_url,
                             "refresh":str(refresh),
                             "access":str(refresh.access_token)
                             })
        else:
            return Response({"error": "Invalid Password"})



class LogoutView(viewsets.ViewSet):
      def list(self, request):
        if request.session.get('username'):
            del request.session['username']
            return Response({"message": "Logout successful"})
        else:
            return Response({"message": "pls Login"})



class Otpverification(viewsets.ViewSet):
    def list(self,request):
        if not request.session.get('otp'):
            return Response({"message": "Pls Login"})
        else:
            return Response({"message": "Enter Otp:"})
    def create(self,request):
        if request.session.get('otp'):
            data=request.data
            print('data: ', data['otp'])
            otp = request.session['otp']
            if str(otp) == str(data['otp']):
                del request.session['otp']

                return Response({"message": "LogIn successful",'login name':request.session['username']})
            else:
                return Response({"message": "Invalide OTP"})
        else:
            return Response({"message": "Pls Login"})
        



class Regitration(viewsets.ModelViewSet):
    queryset = InstaUser.objects.all()
    serializer_class = InstaUserSerializer
    http_method_names = ['post']


class Displaydataview(viewsets.ModelViewSet):
    serializer_class = DisplayDataSerializer
    def get_queryset(self):
        username = self.request.session.get('username')
        if username:
            return InstaUser.objects.filter(Q(is_private=False) | Q(username=username))

        return InstaUser.objects.none()