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

class InstaPostview(viewsets.ModelViewSet):
    queryset = InstaPost.objects.all()
    serializer_class = InstaPostSerializer

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
            'message':f'all data is delete{c}'
        })
    

class LoginView(viewsets.ViewSet):

    def create(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = InstaUser.objects.get(username=username)
        except InstaUser.DoesNotExist:
            return Response({"error": "Invalid Username"})

        if user.password == password:
            request.session['username']=user.username
            return Response({
                "message": "Login successful",
                "user_id": user.id
            })
        else:
            return Response({"error": "Invalid Password"})



class LogoutView(viewsets.ViewSet):
      def create(self, request):
        if request.session.get('username'):
            del request.session['username']
            return Response({"message": "Logout successful"})
        else:
            return Response({"message": "pls Login"})