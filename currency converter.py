import requests
import json

""" Make sure to type in your inputs as a string so use "" for base and to.
For the amount it will be a float so "" is not necessary.
"""
print (" Choose from these types of Currency: BGN, CAD, BRL, HUF, DKK, JPY, ILS, TRY, RON, GBP, PHP, HRK, NOK, USD, MXN, AUD, IDR, KRW, HKD, ZAR, ISK, CZK, THB, MYR, NZD, PLN, SEK, RUB, CNY, SGD, CHF, INR, EUR")

""" This is all possible currencies the API supports"""
base = raw_input("Convert from: ")
to = raw_input("Convert to: ")
amount = float(raw_input("Amount: "))

""" Ensure that when writing the base and to, to insert as a string. The Amount
    is a float so you do not have to add "".
    """
url= "https://api.exchangeratesapi.io/latest?base=" + base

""" This is the URL for the API with live Exchange rates. This is where the
    conversion data will be pulled from.
    """

""" the next lines take the data from the url an make it readable thru python by translating
    the text into a readable format."""
response = requests.get(url) 
data = response.text 
parsed = json.loads(data) 
rates = parsed["rates"]


