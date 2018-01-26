from flask_admin.contrib.mongoengine import ModelView
from flask_security.core import current_user

from application.dashboard.views.util.view_roles_management import \
    ViewSecurityListeners
from domain.interactor.logs.save_model_log_event import SaveModelLogEvent
from domain.interactor.users.current_user import CurrentUser
from domain.repositories.model_repository import ModelRepository


class MlModelView(ModelView, metaclass=ViewSecurityListeners):
    can_edit = False
    can_view_details = True
    can_view = True
    can_create = False
    details_template = 'mlmodel/details.html'

    def __init__(self, model, model_repository: ModelRepository,
                 save_model_log_event: SaveModelLogEvent, current_user: CurrentUser,
                 name, menu_icon_type,
                 menu_icon_value):
        super().__init__(model, name=name, menu_icon_type=menu_icon_type,
                         menu_icon_value=menu_icon_value)
        self.model_repository = model_repository
        self.current_user = current_user
        self.save_model_log_event = save_model_log_event

    def is_accessible(self):
        return current_user.is_authenticated

    def has_edit_role(self):
        self.can_edit = True

    def has_admin_role(self):
        self.can_edit = True
        self.can_create = True

    def on_model_change(self, form, model, is_created):
        # super().on_model_change(form, mlmodel, is_created)
        model.set_pk()
        self.save_model_log_event.save_new_model_event(model.name, str(model.pk), False,
                                                       self.current_user.get_current_user().pk)
