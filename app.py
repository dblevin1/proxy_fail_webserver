try:
    from .src.proxy_fail_webserver.app import app
except ImportError:
    from proxy_fail_webserver.app import app
