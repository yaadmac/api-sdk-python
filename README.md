# Api Banregio - python

A module for using the Api Banregio REST API and generating valid Access Token by OAuth2 protocol.


## Documentation

You can find awesome documentation for Api Banregio REST API [here](https://api.banregio.com/docs/)

## Installation

Install from PyPi using pip, a package manager for Python.


```
pip install banregio-api
```

Don't have pip installed? Try installing it, by running this from the command line:

```
$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
```

## Getting Started

Getting started with the Banregio API couldn't be easier. Create a Token Helper and you're ready to go.

### Oauth2 Helper

You need to implement the ApiBanregioTokenHeper class to get your access_token. There are two ways to do this action:

#### Grant type: Authorization Code (default)

``` python
from banregioapi.banregio_token_helper import BanregioTokenHelper

client_id = 'xxxxxxxxxxxxxxxxxxxx'
secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
redirect_uri = 'http://localhost'

api = BanregioTokenHelper(
    client_id,
    secret_key,
    redirect_uri,
)
# get the authorization url for you app
print api.get_authorize_url()

#output example: https://sandbox.banregio.com/oauth/authorize?redirect_uri=http%3A%2F%2Flocalhost&response_type=code&client_id=Fmaf93Ytqqwp8ZEdHEyBG1meaj1oNB1120ncaq92bcG

# copy and paste the output url in your browser and login
# afther that, copy and paste the value of code parameter

code = "authotization code"
# get your access token
print api.get_access_token(code)
#'lnNDma02maXmQnzS38tQwfKFFL5hUy'

# get your refresh token
print api.get_refresh_token()
#'9idasmkioa92ndaa8m2maldmna28ns'

# if your access_token is expired you can get a new access_token via refresh token
refresh_token = '9idasmkioa92ndaa8m2maldmna28ns'

print api.get_access_token_with_refresh_token(refresh_token)
#'73bc912nday1bndndmdmq101udhj9'

print api.get_refresh_token()
#'83nd910eidnd891hrufnda02bnfma' 

```

#### Grant type: Client Credentials

``` python
from banregioapi.banregio_token_helper import BanregioTokenHelper

client_id = 'xxxxxxxxxxxxxxxxxxxx'
secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
redirect_uri = 'http://localhost'

api = BanregioTokenHelper(
    client_id,
    secret_key,
    redirect_uri,
)
# get your access token via grant type client credentials
print api.get_access_token_with_client_credentials()
# '73bc912nday1bndndmdmq101udhj9'

```

### Api Client Helper

``` python
from banregioapi.banregio_api_helper import BanregioApiHelper

# use your access token 
client = BanregioApiHelper(access_token=access_token)

# get all accounts
client.get_accounts()
#{u'accounts': [{u'id': 277, u'account_number': u'******490787', u'details': None, u'balance': u'200000.00', u'card_number': u'************3219', u'is_credit_card': False}, {u'id': 278, u'account_number': u'******490661', u'details': {u'deferred_balance': u'1064.87', u'due_date': u'2017-08-18T00:00:00', u'last_closing_date': u'2017-01-29T00:00:00', u'non_interest_payment': u'12572.38', u'closing_date': u'2017-07-29T00:00:00', u'minimum_payment': u'493.00', u'cashback_balance': u'1271.03', u'statement_balance': u'12572.38', u'available_balance': 2609.44, u'limit': u'20000.00', u'blocked_balance': u'17310.73', u'annual_percentage_rate': u'36.86', u'product_name': u'VISA GOLD'}, u'balance': u'79.83', u'card_number': u'************2548', u'is_credit_card': True}

# get transactions by account
client.get_transactions(277)
#{u'transactions': [{u'status': u'A', u'reference_number': u'5666820672133655043', u'description': u'fugiat error nisi mollitia expedita', u'business': {u'name': u'ipsa architecto', u'activity': {u'name': u'Doloremque Possimus Eligendi'}}, u'amount': u'-349.29', u'transaction_number': u'6057184068', u'date': u'2017-08-08', u'type': u'2'}, {u'status': u'A', u'reference_number': u'50212160807842917362', u'description': u'sapiente exercitationem hic dolor debiti', u'business': {u'name': u'ullam voluptatibus', u'activity': {u'name': u'Vero Ea Laboriosam'}}, u'amount': u'199.85', u'transaction_number': u'9884237872', u'date': u'2017-08-07', u'type': u'1'}, {u'status': u'A', u'reference_number': u'93378570346745467901', u'description': u'debitis omnis voluptas sint ipsum', u'business': {u'name': u'architecto libero', u'activity': {u'name': u'Quo Eos Accusamus'}}, u'amount': u'-187.21', u'transaction_number': u'4013104787',...
