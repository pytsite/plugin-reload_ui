"""PytSite Reload HTTP API.
"""
from pytsite import routing as _routing, reload as _reload
from plugins import auth as _auth

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class PostReload(_routing.Controller):
    def exec(self) -> dict:
        if not _auth.get_current_user().has_permission('reload_ui@reload'):
            raise self.forbidden()

        _reload.reload()

        return {'status': True}
