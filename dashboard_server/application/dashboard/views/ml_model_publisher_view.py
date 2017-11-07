import json

from flask import request
from flask import url_for
from flask_admin import BaseView
from flask_admin import expose
from flask_login import login_required
from flask_security.decorators import roles_required

from dashboard_server.application.dashboard.views.util.view_roles_management import \
    ViewSecurityListeners
from dashboard_server.domain.entities.ml_model import MlModel
from dashboard_server.domain.interactor.orchestation.orchestation_interator import \
    OrchestationInteractor


class MLModelPublisherView(BaseView, metaclass=ViewSecurityListeners):
    can_edit = True

    def __init__(self, orchestation_interactor: OrchestationInteractor, name):
        super().__init__(name=name)
        self.orchestation_interactor = orchestation_interactor

    @login_required
    @expose()
    def index(self):
        clusters = list(self.orchestation_interactor.get_clusters())
        return self.render('ml_model_publisher.html', clusters=clusters)

    @expose('/entities', methods=('GET',))
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
