# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .tasks import get_api_data


class GetDataAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        res = get_api_data.delay()
        data = res.get()
        return Response(data=data)