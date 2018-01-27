"""PytSite Reload HTTP API.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import routing as _routing, reload as _reload
from plugins import auth as _auth


class PostReload(_routing.Controller):
    def exec(self) -> dict:
        if not _auth.get_current_user().has_role(['admin', 'dev']):
            raise self.forbidden()

        _reload.reload()

        return {'status': True}
