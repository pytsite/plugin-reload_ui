"""PytSite Reload UI Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _register_assetman_resources():
    from plugins import assetman

    if not assetman.is_package_registered(__name__):
        assetman.register_package(__name__)
        assetman.t_js(__name__)
        assetman.js_module('pytsite-reload', __name__ + '@js/pytsite-reload')

    return assetman


def plugin_install():
    assetman = _register_assetman_resources()
    assetman.build(__name__)
    assetman.build_translations()


def plugin_load():
    from pytsite import lang

    lang.register_package(__name__)
    _register_assetman_resources()


def plugin_load_uwsgi():
    from pytsite import router
    from plugins import http_api, permissions
    from . import _http_api_controllers, _eh

    router.on_dispatch(_eh.router_dispatch)

    http_api.handle('POST', 'reload', _http_api_controllers.PostReload, 'reload_ui@reload')

    permissions.define_permission('reload_ui@reload', 'reload_ui@reload_application_permission', 'app')
