from django.shortcuts import render

# Create your views here.
from .models import *
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet,GenericViewSet,ViewSet
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView
from .serializers import *
from django.http.response import HttpResponse
from rest_framework.permissions import BasePermission, AllowAny,IsAuthenticated,DjangoModelPermissions,IsAdminUser,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly,DjangoObjectPermissions
from rest_framework.authentication import BaseAuthentication,BasicAuthentication,SessionAuthentication,TokenAuthentication,RemoteUserAuthentication
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination,CursorPagination,BasePagination     #pagination class
from rest_framework.filters import SearchFilter,OrderingFilter            # for cursor pagination


#-------------- Allow any with restrict for particular methods(overriding allow any class)---------------------------------------

class AlbumAPI(ModelViewSet):
    # queryset = Album.objects.all()
    # serializer_class = AlbumSerializer

    permission_classes = (AllowAny,)  # 6 methods -- student operations  -- except list/retrieve/destroy
    queryset =Album.objects.all()
    serializer_class = AlbumSerializer

    def get_permissions(self):  # override the allowany permissions with list, retrive, distroy not allowded
        if self.action == "Create" or self.action == 'Update' or self.action == 'destroy':
            self.permission_classes = (IsAuthenticated,)  # Authorization type is IsAthenticated
        return super().get_permissions()

# --------------------------------IsAuthenticated with Token Authentication--------------------------------------

class SongAPI(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

# ------------------------------------------ListAPIView,CreateAPIView-------------------------------------------------------------------------

class ArtistAPI(ListAPIView,CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# -----------------------------Custom viewset for custom permissions--------------------------------------


class MyOwnPermission(BasePermission):    # Custom viewset for custom permissions

    def has_object_permission(self, request, view, obj):
        print(request.data['exp'])
        print(request.get_json)
        print(request.path)
        print(request.user)
        return request.user and request.user.is_autheticated and request.data['exp']>10

    def has_permission(self, request, view):
        return True
