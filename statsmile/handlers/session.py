
from tornado.web import authenticated
from bson import ObjectId
from .base import BaseHandler


class SessionHandler(BaseHandler):
    @authenticated
    def delete(self, sid):
        if str(self.current_user['_id']) != sid:
            if ObjectId.is_valid(sid):
                self.application.db['sessions'].remove({'_id': ObjectId(sid)})
        else:
            self.send_error(400)