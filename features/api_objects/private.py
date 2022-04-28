import requests.auth
import requests as r
import urllib.parse
import hashlib
import hmac
import base64


class Auth(requests.auth.AuthBase):
    def __init__(self, uri: str, api_key: str, api_secret: str, payload_data: str, otp: str = None):
        # setup any auth-related data here
        self.uri = uri
        self.api_key = api_key
        self.api_secret = api_secret
        self.payload_data = payload_data
        self.otp = otp

    def __call__(self, r):
        r.headers['API-Key'] = self.api_key
        r.headers['API-Sign'] = self._get_signature(self.uri, self.payload_data, self.api_secret)

        return r

    def _get_signature(self, urlpath, data, secret):
        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()


class PrivApiBase:
    def __init__(self, url: str, auth):
        """
        Perform session authorization to API
        """
        self.site_url: str = url
        self.auth = auth

    def _send_request(
        self, method: str, uri: str, **kwargs
    ) -> requests.Response:
        """
        Generic method to send rest api request
        :param method: REST method ie: 'GET', 'POST', 'PUT', 'DELETE'
        :param url_suffix: url part following the uri string: ie: '/{id}/', '/{id}/process'
        :param payload: Optional json payload
        :return: requests.Response
        """

        return r.request(
            method=method,
            url=f"{self.site_url}{uri}",
            auth=self.auth,
            **kwargs,
        )

    def send_request(self, *args, **kwargs) -> requests.Response:
        return self._send_request(*args, **kwargs)


class UserData(PrivApiBase):
    def __init__(self, *args, **kwargs):
        super(UserData, self).__init__(*args, **kwargs)

    def get_data(self, uri, payload) -> requests.Response:
        return self._send_request("POST", f'{uri}', data=payload)
