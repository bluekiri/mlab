import json

from flask import request
from flask import url_for
from flask_admin import BaseView
from flask_admin import expose
from flask_login import current_user
from flask_login import login_required
from flask_security.decorators import roles_required

from dashboard_server.application.dashboard.views.util.view_roles_management import \
    ViewSecurityListeners
from dashboard_server.domain.entities.ml_model import MlModel
from dashboard_server.domain.interactor.orchestation.orchestation_interator import \
    OrchestationInteractor
from dashboard_server.domain.interactor.users.users_privilages import UsersPrivilages


class MLModelPublisherView(BaseView, metaclass=ViewSecurityListeners):
    can_edit = True

    def __init__(self, users_privilages: UsersPrivilages,
                 orchestation_interactor: OrchestationInteractor, name):
        super().__init__(name=name)
        self.users_privilages = users_privilages
        self.orchestation_interactor = orchestation_interactor

    @login_required
    @expose()
    def index(self):
        group_of_clusters, clusters_without_group = self.orchestation_interactor.get_clusters()
        return self.render('ml_model_publisher.html', group_of_clusters=group_of_clusters,
                           clusters_without_group=clusters_without_group,
                           can_edit=self.users_privilages.can_change_models(current_user))

    @expose('/models', methods=('GET',))
    def models(self):
        return json.dumps([(str(model.pk), model.name) for model in MlModel.objects()])

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
    def change_model(self):
        group_name = request.form.get("group_name")
        model_id = request.form.get("model_id")

        self.orchestation_interactor.load_model_by_group(group_name, model_id)
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

        self.orchestation_interactor.set_group_to_cluster(host_name, group)
        return json.dumps({"go": url_for("mlmodelpublisherview.index")}), 200, {
            'ContentType': 'application/json'}
