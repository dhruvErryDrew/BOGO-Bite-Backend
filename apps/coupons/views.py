from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import CouponSerializer, Coupon
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from .models import Coupon
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.core import serializers


@api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def addCoupon(request):
    serializer = CouponSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        id = serializer.validated_data.get('id')
        couponExists = Coupon.objects.filter(id=id).first()
        if couponExists:
            raise ValidationError("A coupon with this ID already exists.")
        else:
            serializer.save()
            return Response({'createdCoupon': True}, status=status.HTTP_201_CREATED)
        serializer.save()
        coopon = Coupon.objects.get(id=serializer.data['id'])
        # coopon.set_password(request.data['password'])
        coopon.save()
        # token = Token.objects.create(user=user)
        # return Response({'token': token.key, 'user': serializer.data})
        return Response({'createdCoupon': True}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_200_OK) 

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def getCoupons(request):
    # print(type(request.user))
    # print(request.user.name)
    coopons = serializers.serialize("json", Coupon.objects.all())
    # print(coopons)
    return Response({'coupon': coopons, 'ritreevdCooponz': True}, status=status.HTTP_201_CREATED)

class CouponList(generics.ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer