from flask_admin import BaseView
from flask_admin import expose
from flask_login import login_required

from dashboard_server.domain.interactor.logs.get_time_line_events import GetTimeLineEvents


class HomeView(BaseView):
    def __init__(self, get_line_time_events: GetTimeLineEvents, name=None, category=None,
                 endpoint=None, url=None, template='home.html', menu_class_name=None,
                 menu_icon_type=None, menu_icon_value=None):
        super().__init__(name or "Home",
                         category,
                         endpoint or 'admin',
                         '/admin' if url is None else url,
                         'static',
                         menu_class_name=menu_class_name,
                         menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value)
        self.get_line_time_events = get_line_time_events
        self._template = template

    @login_required
    @expose()
    def index(self):
        logs = self.get_line_time_events.get_all_time_events()
        return self.render(self._template, logs=logs)
