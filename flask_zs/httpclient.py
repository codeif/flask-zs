from flask import has_request_context, request
from requests import Session


class HttpClient:
    def __init__(
        self,
        app=None,
        base_url=None,
        headers=None,
        auth=None,
        user_agent=None,
        config_prefix="HTTP_CLIENT",
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

    def create_session(self, headers=None, user_agent=None):
        """生成一个session, headers存在时覆盖默认haeders"""
        return ZSSession(
            base_url=self.base_url,
            headers=headers or self.headers,
            auth=self.auth,
            user_agent=user_agent or self.user_agent,
        )

    def request(self, method, path, **kwargs):
        with self.create_session() as session:
            return session.request(method, path, **kwargs)

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


class ZSSession(Session):
    def __init__(self, base_url, headers=None, auth=None, user_agent=None) -> None:
        super().__init__()
        self.stream = True

        self.base_url = base_url
        if headers:
            self.headers.update(headers)
        self.auth = auth
        if user_agent:
            self.headers["User-Agent"] = user_agent

    def request(self, method, path, **kwargs):
        url = self.base_url + path

        if has_request_context():
            accept_encoding = request.headers.get("Accept-Encoding")
            accept = request.headers.get("Accept")
            if accept_encoding:
                self.headers["Accept-Encoding"] = accept_encoding
            if accept:
                self.headers["Accept"] = accept

        return super().request(method, url, **kwargs)
