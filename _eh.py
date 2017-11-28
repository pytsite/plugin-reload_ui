"""PytSite Reload UI Plugin Events Handlers
"""
from pytsite import router as _router, lang as _lang, reload as _reload
from plugins import auth as _auth, assetman as _assetman

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    if _reload.get_flag() and _auth.get_current_user().has_permission('reload_ui@reload'):
        _assetman.preload('reload_ui@js/reload.js')
        _router.session().add_warning_message(_lang.t(_reload.RELOAD_MSG_ID))
