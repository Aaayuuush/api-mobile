from rest_framework.views import APIView
from rest_framework.response import Response

class SampleView(APIView):
    def get(self, request):
        return Response({"message": "Hello from APIs_FOR_MOBILE!"})
