from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """test API View """
    serializer_class = serializers.HelloSerializer


    def get(self,request,format=None):
        """return a list of API features"""
        an_apiview=[
        'Usees HTTP methods as functions (get,post,patch,put,delete) ',
        'Is simlar to a tradtional django View ',
        'Gives you the most control over you applaication logic',
        'Is Mapped manually to URLs ',
        ]
        return Response({"message":"Hello","an_apiview":an_apiview})


    def post(self,request):

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({"message":message})
        else :
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self,request,pk=None):
        """return updating an object"""
        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        """"handel a partical update of an object"""
        return Response({"method":'PATCH'})


    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSets"""

    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewset=[
        'users actions (list ,create ,retrive ,update ,partial_update)',
        'Automatically maps to urls using Routers',
        "provides more functionality with less code"
        ]
        return Response({'message':"hello!",'a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handele creating and updating Profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset =models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
