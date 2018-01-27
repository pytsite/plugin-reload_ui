"""PytSite Reload UI Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from pytsite import lang
    from plugins import assetman

    lang.register_package(__name__)
    assetman.register_package(__name__)

    assetman.t_js(__name__)
    assetman.js_module('pytsite-reload', __name__ + '@js/pytsite-reload')


def plugin_install():
    from plugins import assetman

    assetman.build(__name__)
    assetman.build_translations()


def plugin_load_uwsgi():
    from pytsite import router
    from plugins import http_api
    from . import _http_api_controllers, _eh

    router.on_dispatch(_eh.router_dispatch)

    http_api.handle('POST', 'reload', _http_api_controllers.PostReload, 'reload_ui@reload')
