from flask_admin import BaseView
from flask_admin import expose
from flask_login import login_required
from flask_security.core import current_user


class HomeView(BaseView):
    def __init__(self, name=None, category=None,
                 endpoint=None, url=None,
                 template='home.html',
                 menu_class_name=None,
                 menu_icon_type=None,
                 menu_icon_value=None):
        super().__init__(name or "Home",
                         category,
                         endpoint or 'admin',
                         '/admin' if url is None else url,
                         'static',
                         menu_class_name=menu_class_name,
                         menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value)
        self._template = template

    @login_required
    @expose()
    def index(self):
        return self.render(self._template)
