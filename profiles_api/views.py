from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiview(APIView):
    """Test API View"""

    def get(slef,request,format=None):
        """Returns a list  of APIView features"""
        an_apview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional DjangoView',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!','an_apiview':an_apview})#returns a json.the input must be list or dictionay

