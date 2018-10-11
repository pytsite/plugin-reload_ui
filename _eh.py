"""PytSite Reload UI Plugin Events Handlers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import router as _router, lang as _lang, reload as _reload
from plugins import auth as _auth


def router_dispatch():
    if _reload.get_flag() and _auth.get_current_user().is_admin:
        _router.session().add_warning_message(_lang.t('reload_ui@reload_required'))
