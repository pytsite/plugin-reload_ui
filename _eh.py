"""PytSite Reload UI Plugin Events Handlers
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import router as _router, lang as _lang, reload as _reload
from plugins import auth as _auth, assetman as _assetman


def router_dispatch():
    if _reload.get_flag() and _auth.get_current_user().has_role(['admin', 'dev']):
        _assetman.preload('reload_ui@js/reload.js')
        _router.session().add_warning_message(_lang.t('reload_ui@reload_required'))
