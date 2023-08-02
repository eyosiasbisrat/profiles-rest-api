from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    """creates a new field on our serializer which is a chafield with max len of 10"""
