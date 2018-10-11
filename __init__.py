"""PytSite Reload UI Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load_wsgi():
    from pytsite import router
    from plugins import http_api
    from . import _http_api_controllers, _eh

    router.on_dispatch(_eh.router_dispatch)

    http_api.handle('POST', 'reload', _http_api_controllers.PostReload, 'reload_ui@reload')
