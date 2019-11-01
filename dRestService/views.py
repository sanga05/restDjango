
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
# class getUserdet(RetrieveUpdateDestroyAPIView):
from rest_framework.decorators import api_view
@api_view(['GET', 'POST', ])
def getUser(request):

         return Response("everthyng ok", status=status.HTTP_200_OK,template_name='articles.html')