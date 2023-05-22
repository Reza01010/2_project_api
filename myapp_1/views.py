from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Cryptocurrency1, Cryptocurrency2, Cryptocurrency23
from .response_api_coin import (c_a_for_retrieving_of_Bitcoin_and_several_other_cryptocurrencies_2 as def2,
                                c_a_retrieve_top_cryptocurrency_by_market_value_1 as def1)
from django.contrib.auth import get_user_model
from django.http import HttpResponse
# CoinCaCryptocurrencyByMarket1


class CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListView(generic.ListView):
    queryset = Cryptocurrency1.objects.all()
    template_name ='list2.html'
    context_object_name = 'cryptocurrency'



class CoinCaBitcoinAndSeveralOtherCryptocurrencies2DetailView(generic.DetailView):
    queryset = Cryptocurrency1.objects.all()
    template_name ='detail2.html'
    context_object_name = 'cryptocurrency'
# -----------


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


def list_2_view(request):
    # Call function a first
    def2()

    # Call CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListView view
    view = CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListView.as_view()
    return view(request)
# -----------------------------

def detail_2_view(request,pk):
    instance = get_object_or_404(Cryptocurrency1, pk=pk)
    # Call function a first
    def2()

    # Call CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListView view
    view = CoinCaBitcoinAndSeveralOtherCryptocurrencies2DetailView.as_view()
    return view(request, pk=pk)





# class CoinCaBitcoinAndSeveralOtherCryptocurrencies1ListView(generic.ListView):
#     queryset = Cryptocurrency1.objects.all()
#     template_name ='list1.html'
#     context_object_name = 'cryptocurrency'
# def list_1_view(request):
#     # Call function a first
#     def1()
#     get_object_or_404(Cryptocurrency2, id=0)
#     # Call CoinCaBitcoinAndSeveralOtherCryptocurrencies2ListView view
#     view = CoinCaBitcoinAndSeveralOtherCryptocurrencies1ListView.as_view()
#     return view(request)
@login_required
def list_cryptocurrency_by_market_value_1(request):

    def1()
    list_dicts_coin_ptice = get_object_or_404(Cryptocurrency2, id=0)
    # print(list_dicts_coin_ptice.response_data)
    return render(request, 'list1.html', context={'cryptocurrency': list_dicts_coin_ptice}, )

@login_required
def detail_cryptocurrency_by_market_value_1(request, pk):
    #
    list_dicts_coin_ptice = None
    x = ['error']
    b = False
    def1()
    user = get_user_model().objects.get(pk=request.user.id)
    #
    if user.Rating == 'G':
        list_dicts_coin_ptice = get_object_or_404(Cryptocurrency23, id=0)
        for j in list_dicts_coin_ptice.response_datA:
            if pk == j['name']:
                x = j
        b = True
    #
    elif user.Rating == 'S':
        list_dicts_coin_ptice = get_object_or_404(Cryptocurrency2, id=0)
        for j in list_dicts_coin_ptice.response_data:
            if pk == j['name']:
                x = j
        b = False



    return render(request, 'detail1.html', context={'cryptocurrency': list_dicts_coin_ptice, 'x': x, 'b':b}, )



