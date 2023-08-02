
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions






class HelloApiview(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    def get(self,request,format=None):
        """Returns a list  of APIView features"""
        an_apview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional DjangoView',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!','an_apiview':an_apview})
        """returns a json.the input must be list or dictionay"""
    
    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        
        """self.seralizer_class comes with the APIview that retives the configured serilizer class for our view.
        When you make a post request the data gets passed in as request.data"""

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
              return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
       """Handel updating an object: updates the entire object with what we provided in the request"""
       return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
       """takes care of partial update of an object.updates only the fields that were provided in the request"""
       return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        
        a_viewset = [
            'Uses actions (list,create,retrieve,update,partial_update)',
            'Authomathically maps to URL using Routers',
            'provides more functionality with less codes',
            
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
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
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() #qurey set we will manage
    authentication_classes = (TokenAuthentication,)
    """created as a tupele"""
    permission_classes = (permissions.UpdateOwnProfile,)
    
    """configures our UserProgileView set to use tokenauthenthication and then add permission
    """

    filter_backends = (filters.SearchFilter,)
    """we can have multiples filter back ends.comes with django rest"""
    search_fields = ('name', 'email',)
    """tells the filter backend which fields we will be searching with"""
    
class UserLoginApiView(ObtainAuthToken):
    """takes care of authenthiation tokens.ObtainAuthToken proovided by django rest_framework.It doesnt enable it self
    in the admin site.Thus we need to customize it"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

