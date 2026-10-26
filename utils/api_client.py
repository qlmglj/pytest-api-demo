"""HTTP 客户端封装：统一 URL 拼接、超时、默认 Header 与耗时日志。"""

import logging
import time

import requests

log = logging.getLogger("api")


class ApiClient:
    def __init__(self, base_url: str, timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {"Accept": "application/json", "User-Agent": "pytest-api-demo/1.0"}
        )

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{path}"
        start = time.perf_counter()
        resp = self.session.request(method, url, timeout=self.timeout, **kwargs)
        cost_ms = (time.perf_counter() - start) * 1000
        log.info("%s %s -> %s %.0fms", method.upper(), url, resp.status_code, cost_ms)
        return resp

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        return self.request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.request("DELETE", path, **kwargs)

    def close(self) -> None:
        self.session.close()
