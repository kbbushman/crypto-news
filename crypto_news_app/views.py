from django.shortcuts import render
import requests
import json

def home(request):
	# Get Crypto Prices
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
	price = json.loads(price_request.content)

	# Get Crypto News
	news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	news = json.loads(news_request.content)
	return render(request, 'home.html', {'news': news, 'price': price})

def prices(request):
	if request.method == 'POST':
		# Get Crypto Prices
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,EUR")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
	else:
		notfound = "Enter a crypto currency symbol into the form above..."
		return render(request, 'prices.html', {'notfound': notfound})
