"""PytSite Reload UI Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, router
    from plugins import assetman, permissions, http_api
    from . import _http_api_controllers, _eh

    lang.register_package(__name__)

    assetman.register_package(__name__)
    assetman.t_js(__name__ + '@**')
    assetman.js_module('pytsite-reload', __name__ + '@js/pytsite-reload')

    router.on_dispatch(_eh.router_dispatch)

    http_api.handle('POST', 'reload', _http_api_controllers.PostReload, 'reload_ui@reload')

    permissions.define_permission('reload_ui@reload', 'reload_ui@reload_application_permission', 'app')


_init()
