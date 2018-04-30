import json

import pytz
import tzlocal
from flask import request
from flask import url_for
from flask_admin import BaseView
from flask_admin import expose
from flask_login import login_required
from flask_security.decorators import roles_required

from dashboard.application.dashboard.views.util.view_roles_management import \
    ViewSecurityListeners
from dashboard.domain.entities.ml_model import MlModel
from dashboard.domain.interactor.orchestation.orchestation_interator import \
    OrchestationInteractor
from dashboard.domain.interactor.users.current_user import CurrentUser
from dashboard.domain.interactor.users.users_privileges import UsersPrivileges


class MLModelPublisherView(BaseView, metaclass=ViewSecurityListeners):
    can_edit = True

    def __init__(self, users_privilages: UsersPrivileges,
                 orchestation_interactor: OrchestationInteractor,
                 current_user: CurrentUser, name,
                 menu_icon_type, menu_icon_value):
        super().__init__(name=name, menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value)
        self.current_user = current_user
        self.users_privilages = users_privilages
        self.orchestation_interactor = orchestation_interactor

    @login_required
    @expose()
    def index(self):
        group_of_workers, workers_without_group = self.orchestation_interactor.get_group_workers()
        return self.render('ml_model_publisher/ml_model_publisher.html',
                           group_of_workers=group_of_workers,
                           workers_without_group=workers_without_group,
                           has_active_model_permissions=self.current_user.has_admin_role())

    @expose('/models', methods=('GET',))
    def models(self):
        return json.dumps(
            [(str(model.pk), self._format_model_name(model)) for model in
             MlModel.objects()])

    def _format_model_name(self, model):
        local_time_zone = tzlocal.get_localzone()
        local_time = model.ts.replace(tzinfo=pytz.utc).astimezone(
            local_time_zone)
        return model.name + " - " + local_time.strftime('%Y-%m-%d %H:%M:%S')

    @login_required
    @roles_required('admin', )
    @expose('/change_model', methods=('POST',))
    def change_model(self):
        host_name = request.form.get("host_name")
        model_id = request.form.get("model_id")

        self.orchestation_interactor.load_model_on_host(host_name, model_id)
        return json.dumps({"go": url_for("mlmodelpublisherview.index")}), 200, {
            'ContentType': 'application/json'}

    @login_required
    @roles_required('admin', )
    @expose('/change_group_model', methods=('POST',))
    def change_group_model(self):
        group_name = request.form.get("group_name")
        model_id = request.form.get("model_id")

        self.orchestation_interactor.load_model_on_group(group_name, model_id)
        return json.dumps({"go": url_for("mlmodelpublisherview.index")}), 200, {
            'ContentType': 'application/json'}

    @login_required
    @expose('/groups', methods=('GET',))
    def get_groups(self):
        return json.dumps(self.orchestation_interactor.get_groups())

    @login_required
    @roles_required('admin', )
    @expose('/set_group', methods=('POST',))
    def set_group(self):
        host_name = request.form.get("host_name")
        group = request.form.get("group")

        self.orchestation_interactor.set_group_to_worker(host_name, group)
        return json.dumps({"go": url_for("mlmodelpublisherview.index")}), 200, {
            'ContentType': 'application/json'}
