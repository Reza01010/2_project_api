
from .models import Cryptocurrency1, Cryptocurrency2, Cryptocurrency23

import requests


# _______________________________________________________________________________________________________________________


def c_a_for_retrieving_of_Bitcoin_and_several_other_cryptocurrencies_2(Add_to_default=None, only_these=None):
    # .
    symbols = []

    if None != Add_to_default and None != only_these:
        only_these = None

    if None == Add_to_default and None == only_these:
        symbols = ['bitcoin', 'ethereum', 'litecoin', 'ripple']

    elif None != Add_to_default:
        if isinstance(Add_to_default, list):
            if len(Add_to_default) > 6:
                Add_to_default = Add_to_default[0:7]
            Add_to_default = [item for item in Add_to_default if isinstance(item, str)]
            symbols = Add_to_default.copy() + ['bitcoin', 'ethereum', 'litecoin', 'ripple']
        else:
            return
    elif None != only_these:
        if isinstance(only_these, list):
            if len(only_these) > 10:
                only_these = only_these[0:11]
            only_these = [item for item in only_these if isinstance(item, str)]
            symbols = only_these.copy()
        else:
            return



    # Define the cryptocurrency symbols we want to retrieve prices for
    # symbols = ['bitcoin', 'ethereum', 'litecoin', 'ripple']
    # Send a request to the CoinGecko API to retrieve the current prices
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={",".join(symbols)}&vs_currencies=usd'
    response = requests.get(url)
    # print(response, '.............................................')
    # Parse the response to extract the prices     (('error' or 'error_code') not in response.json()) or
    if (200  == response.status_code):
        prices = {}
        for symbol in symbols:
            data = response.json()[symbol]
            prices[symbol] = data['usd']
        # list_coin_token = []
        # Print the prices
        # print(prices)
        for symbol, price in prices.items():
            # print('......................'*100,price,',,,,',type(price),'......................'*100)
            obj,_ = Cryptocurrency1.objects.get_or_create(name=symbol)
            # print(obj,',,,,,,,,,,,')
            # print(_, ',,,,,,,,,,,')
            if obj:
                obj.usd_price = float(price)
                obj.save()
            if _:
                obj, _ = Cryptocurrency1.objects.get_or_create(name=symbol)
                if obj:
                    obj.usd_price = float(price)
                    obj.save()

            # list_coin_token.append(
            #     {
            #         "name": symbol,
            #         symbol: {'USD': price}
            #     }
            # )

    return


# _______________________________________________________________________________________________________________________

# -------

# _______________________________________________________________________________________________________________________

def c_a_retrieve_top_cryptocurrency_by_market_value_1(nombr=30):
    # print('start >>>  c_a_retrieve_top_cryptocurrency_by_market_value_1()')
    list_coin_token = []
    if nombr > 100:
        nombr = 100

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": nombr,
        "page": 1
    }
    response = requests.get(url, params=params)
    # print('json,.,.,..,.,.,,..,.,.,.,.,.,.,.,\n', response)
    # print(response.status_code)

    # print(response) or (('error' or 'error_code') not in response.json())
    if (200  == response.status_code):
        # print('yes 200')
        response = response.json()
        for coin in response:
            # print('run for line=105 .......\n')
            if coin["name"]:
                # print('run if coin["name"] line=107 .._.._..\n')
                # print(list_coin_token)
                list_coin_token.append({
                    "name": coin['name'],
                    "current_price": coin['current_price']
                })

        # print('line=115 $$$$$$')
        obj,_ = Cryptocurrency2.objects.get_or_create(id=0,)
        # print('run Cryptocurrency2.objects.get_or_create \n','obj =',obj,'+'*100,'_ =',_)
        if obj:
            # print('line:119 >>>> if obj:(line:118)')
            # print('list_coin_token[0:2] = ',list_coin_token[0:2])
            if list_coin_token:
                # print('run >> if list_coin_token: Line = 122')
                obj.response_data = list_coin_token
                obj.save()
                # print('finali if obj.save() line = 125')
        # print('finale proses obj,_ = Cryptocurrency2.objects.get_or_create')

        #  کد های اضافه
        # if _:
        #     print('line:116 >>>> if _:(line:115)')
        #     obj, _ = Cryptocurrency2.objects.get_or_create(d=0, response_data=list_coin_token)
        #     if obj:
        #         print('line:119 >>>> if obj:(line:118)')
        #         print(list_coin_token)
        #         obj.response_data = list_coin_token
        #         obj.save()
        #         print(':::::;')



        list_coins_tokens_detail = response
        # print('start >>>  list_coins_tokens_detail = response')
        if list_coins_tokens_detail:
            # print('run if list_coins_tokens_detail:')
            obj, _ = Cryptocurrency23.objects.get_or_create(id=0,)
            # print('run obj, _ = Cryptocurrency23.objects.get_or_create(id=0, response_datA=list_coins_tokens_detail) /
            # line = 146')
            if obj:
                # print('line:149 >>>> if obj:(line:148)')
                obj.response_datA = list_coins_tokens_detail
                obj.save()
                # print('finali if obj.save() line = 152')

        #  کد های اضافه
        # if _:
        #     print('line:131 >>>> if _:(line:130)')
        #     obj, _ = Cryptocurrency23.objects.get_or_create(d=0, response_datA = list_coins_tokens_detail)
        #     if obj:
        #         print('line:133 >>>> if obj:(line:1132)')
        #         obj.response_datA = list_coins_tokens_detail
        #         obj.save()


        return

# _______________________________________________________________________________________________________________________



# coingecko چک کردن سایت
# url = "https://api.coingecko.com/api/v3/ping"
#
# response = requests.get(url).json()
#
# print(response)





















































































#کد های اضافه ی قبلی
#
#
#
# def c_a_for_retrieving_of_Bitcoin_and_several_other_cryptocurrencies_2():
#     # Define the cryptocurrency symbols we want to retrieve prices for
#     symbols = ['bitcoin', 'ethereum', 'litecoin', 'ripple']
#
#     # Send a request to the CoinGecko API to retrieve the current prices
#     url = f'https://api.coingecko.com/api/v3/simple/price?ids={",".join(symbols)}&vs_currencies=usd'
#     response = requests.get(url)
#
#     # Parse the response to extract the prices
#     prices = {}
#     for symbol in symbols:
#         data = response.json()[symbol]
#         prices[symbol] = data['usd']
#     list_coin_token = []
#     # Print the prices
#     for symbol, price in prices.items():
#         print(f'{symbol}: ${price:.2f}')
#         db = Cryptocurrency2.objects.get_or_create(name=symbol)
#         db.usd_price = price
#         db.save()
#
#         list_coin_token.append(
#             {
#                 "name": symbol,
#                 symbol: {'USD': price}
#             }
#         )
#
#     return list_coin_token
#
#
# def c_a_retrieve_top_cryptocurrency_by_market_value_1(numbr=30):
#     # Set up API endpoint and parameters
#     url = "https://api.coingecko.com/api/v3/coins/markets"
#     params = {
#         "vs_currency": "usd,eur,irr",
#         "order": "market_cap_desc",
#         "per_page": numbr
#     }
#
#     # Send API request and retrieve response
#     response = requests.get(url, params=params)
#     data = response.json()
#     list_coin_token = []
#     # Iterate through top 30 coins and print prices
#     for i, coin in enumerate(data):
#         print(f"{i+1}. {coin['name']}:")
#         print(f"    USD: {coin['current_price'][0]}")
#         print(f"    EUR: {coin['current_price'][1]}")
#         print(f"    IRR: {coin['current_price'][2]}")
#
#         db = Cryptocurrency1.objects.get_or_create(name=coin['name'])
#         db.usd_price = coin['current_price'][0]
#         db.eur_price = coin['current_price'][1]
#         db.irr_price = coin['current_price'][2]
#         db.save()
#
#         list_coin_token.append(
#             {
#                 "name": coin['name'],
#                 coin['name']: {'USD': coin['current_price'][0], 'EUR': coin['current_price'][1], 'IRR': coin['current_price'][2]}
#             }
#         )
#
#     return list_coin_token
#
#
#
#
#
# print(c_a_retrieve_top_cryptocurrency_by_market_value_1())
# print(c_a_for_retrieving_of_Bitcoin_and_several_other_cryptocurrencies_2())