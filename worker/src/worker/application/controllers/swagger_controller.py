import falcon


class SwaggerController:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_301
        resp.set_header('Location', '/static/swagger/index.html')
