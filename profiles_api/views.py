from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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

    