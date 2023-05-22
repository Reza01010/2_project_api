from django.shortcuts import render
from rest_framework import permissions, authentication, status
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model
from myapp_1.models import Cryptocurrency23, Cryptocurrency2, Cryptocurrency1
from .serializers import Cryptocurrency23Serializer, Cryptocurrency2Serializer, Cryptocurrency1Serializer
from myapp_1.response_api_coin import (c_a_for_retrieving_of_Bitcoin_and_several_other_cryptocurrencies_2 as def2,
                                c_a_retrieve_top_cryptocurrency_by_market_value_1 as def1)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes


# ----=========================================================================⬇ ⏬ 🔻


class CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListViewApi(generics.ListAPIView):
    queryset = Cryptocurrency1.objects.all()
    serializer_class = Cryptocurrency1Serializer
    permission_classes = [AllowAny]


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def list_2_view_api(request):
#     # Call function a first
#     def2()
#     # Call CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListViewApi view
#     view = CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListViewApi.as_view()
#     return view(request)


from django.http import HttpRequest

@api_view(['GET'])
@permission_classes([AllowAny])
def list_2_view_api(request):
    def2()
    http_request = HttpRequest()
    http_request.method = request.method
    http_request.GET = request.GET
    view = CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListViewApi.as_view()
    return view(http_request)

# ----=========================================================================⬆ ⏫ 🔺


# ----=========================================================================⬇ ⏬ 🔻


class CoinCaBitcoinAndSeveralOtherCryptocurrencies2DetailViewApi(generics.RetrieveAPIView):
    queryset = Cryptocurrency1.objects.all()
    serializer_class = Cryptocurrency1Serializer
    permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes([AllowAny])
def detail_2_view_api(request,pk):
    instance = get_object_or_404(Cryptocurrency1, pk=pk)
    # Call function a first
    http_request = HttpRequest()
    http_request.method = request.method
    http_request.GET = request.GET
    def2()
    # Call CoinCaBitcoinAndSeveralOtherCryptocurrencies2DetailViewApi view
    view = CoinCaBitcoinAndSeveralOtherCryptocurrencies2DetailViewApi.as_view()
    return view(http_request, pk=pk)


# ----=========================================================================⬆ ⏫ 🔺


# --------------------------------------------------------


# ----=========================================================================⬇ ⏬ 🔻


class CoinCaBitcoinAndSeveralOtherCryptocurrencies1ListViewApi(generics.RetrieveAPIView):
    queryset = Cryptocurrency2.objects.filter(id=0)
    serializer_class = Cryptocurrency2Serializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = [TokenAuthentication]

    authentication_classes = [TokenAuthentication]

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

@permission_classes([IsAuthenticated])
def list_cryptocurrency_by_market_value_1_api(request):
    # Call def1() function to update information
    def1()
    http_request = HttpRequest()
    http_request.method = request.method
    http_request.GET = request.GET
    # Retrieve Cryptocurrency2 object with id=0
    cryptocurrency = get_object_or_404(Cryptocurrency2, id=0)

    # Call CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListViewApi view
    view = CoinCaBitcoinAndSeveralOtherCryptocurrencies1ListViewApi.as_view()
    return view(http_request)


# ----=========================================================================⬆ ⏫ 🔺


# ----=========================================================================⬇ ⏬ 🔻


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JSONWebTokenAuthentication])
def detail_cryptocurrency_by_market_value_1_api(request, pk):
    http_request = HttpRequest()
    http_request.method = request.method
    http_request.GET = request.GET
    list_dicts_coin_price = None
    x = ['error']
    def1()
    user = get_user_model().objects.get(pk=http_request.user.id)

    if user.Rating == 'G':
        list_dicts_coin_price = get_object_or_404(Cryptocurrency23, id=0)
        if not list_dicts_coin_price:
            raise NotFound("Cryptocurrency23 object does not exist.")
        for j in list_dicts_coin_price.response_datA:
            if pk == j['name']:
                x = j
        serializer = Cryptocurrency23Serializer(x, many=True)
        return Response(serializer.data)

    elif user.Rating == 'S':
        list_dicts_coin_ptice = get_object_or_404(Cryptocurrency2, id=0)
        if not list_dicts_coin_ptice:
            raise NotFound("Cryptocurrency23 object does not exist.")
        for j in list_dicts_coin_ptice.response_data:
            if pk == j['name']:
                x = j
        serializer = Cryptocurrency2Serializer(x, many=True)
        return Response(serializer.data)

    else:
        content = {'message': 'ERROR .!'}
        return Response(content)


# ----=========================================================================⬆ ⏫ 🔺
























