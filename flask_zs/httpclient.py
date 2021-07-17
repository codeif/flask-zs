import requests
from flask import has_request_context, request
from requests.structures import CaseInsensitiveDict
from requests.utils import DEFAULT_ACCEPT_ENCODING


class HttpClientFactory:
    def __init__(
        self, app=None, base_url=None, headers=None, auth=None, user_agent=None, config_prefix="HTTP_CLIENT",
    ):
        self.base_url = base_url
        self.headers = headers
        self.auth = auth
        self.config_prefix = config_prefix
        self.user_agent = user_agent

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if self.base_url is None:
            self.base_url = app.config[f"{self.config_prefix}_BASE_URL"]
        if self.headers is None:
            self.headers = app.config.get(f"{self.config_prefix}_HEADERS")
        if self.auth is None:
            self.auth = app.config.get(f"{self.config_prefix}_AUTH")
        if self.user_agent is None:
            self.auth = app.config.get(f"{self.config_prefix}_USER_AGENT")

    def client(self, headers=None):
        """生成一个session, headers存在时覆盖默认haeders"""
        return HttpClient(
            base_url=self.base_url, headers=headers or self.headers, auth=self.auth, user_agent=self.user_agent,
        )

    def get(self, path, **kwargs):
        return self.client().request("GET", path, **kwargs)

    def options(self, path, **kwargs):
        return self.client().request("OPTIONS", path, **kwargs)

    def head(self, path, **kwargs):
        return self.client().request("HEAD", path, **kwargs)

    def post(self, path, **kwargs):
        return self.client().request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.client().request("PUT", path, **kwargs)

    def patch(self, path, **kwargs):
        return self.client().request("PATCH", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.client().request("DELETE", path, **kwargs)


class HttpClient:
    def __init__(self, base_url, headers, auth, user_agent) -> None:
        self.base_url = base_url
        self.headers = headers
        self.auth = auth
        self.user_agent = user_agent

    def request(self, method, path, **kwargs):
        url = self.base_url + path

        headers = CaseInsensitiveDict(
            {
                "User-Agent": "flask-zs",
                "Accept-Encoding": DEFAULT_ACCEPT_ENCODING,
                "Accept": "*/*",
                "Connection": "close",
            }
        )
        if has_request_context():
            accept_encoding = request.headers.get("Accept-Encoding")
            accept = request.headers.get("Accept")
            if accept_encoding:
                headers["Accept-Encoding"] = accept_encoding
            if accept:
                headers["Accept"] = accept

        if self.headers:
            headers.update(self.headers)
        if self.user_agent:
            headers["User-Agent"] = self.user_agent

        session = requests.Session()
        session.headers = headers
        session.stream = True
        resp = session.request(method, url, **kwargs)
        session.close()

        return resp

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def options(self, path, **kwargs):
        return self.request("OPTIONS", path, **kwargs)

    def head(self, path, **kwargs):
        return self.request("HEAD", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def patch(self, path, **kwargs):
        return self.request("PATCH", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)
