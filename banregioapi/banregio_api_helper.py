import requests
import json
import urlparse

from urllib import urlencode

class BanregioApiHelper():

    def __init__(self,access_token,base_uri='https://api.banregio.com'):
        print "Hello from BanregioApiHelper..."
        self.base_uri = base_uri
        self.access_token = access_token


    def _build_http_request(self,end_point,method,**kwargs):
        
        req = None

        if method == 'get':
            url =  "{base_uri}/{end_point}".format(
                base_uri=self.base_uri,
                end_point=end_point
            )
            
            url = self._update_url_params(url,kwargs)

            req = requests.get(
                url,
                headers=self._set_headers()
            )

        return req

    def _set_headers(self):

        headers = {
            'Authorization': "Bearer {token}".format(token=self.access_token),
            'Content-Type': "application/json"
        }

        return headers

    def _update_url_params(self,url,params):

        url_parts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urlencode(query)

        return urlparse.urlunparse(url_parts)


    def get_accounts(self):
        
        response = self._build_http_request("v1/accounts/",'get')
        return response.json()

    def get_transactions(self,id,**kwargs):

        response = self._build_http_request(
            "v1/accounts/{id}/transactions".format(id=id),
            'get',
            **kwargs
        )
        return response.json()

    def get_enterprise_transactions(self,id,**kwargs):
        
        response = self._build_http_request(
            "v1/accounts/{id}/transactions".format(id=id),
            'get',
            **kwargs
        )
        return response.json()






