from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from .models import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def login(request):
    # print(request.data)
    user = get_object_or_404(User, username__iexact=request.data['username'])
    if not user.check_password(request.data['password']):
        return JsonResponse({'loginExists': False})
        # return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    print(token.key)
    serializer = UserSerializer(user)
    # return JsonResponse({'loginExists': True})
    return JsonResponse({'loginExists': True, 'token': token.key, 'user': serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    # print(request.data)
    if serializer.is_valid():
        try:
            validate_password(password=request.data['password'])
        except ValidationError as err:
            return Response({'signedUp': False, 'error': str(err)})
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return JsonResponse({'signedUp': True, 'token': token.key, 'user': serializer.data})
    return Response({'signedUp': False, 'error': str(serializer.errors)}) 

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    return Response('Passed for {}'.format(request.user.email))