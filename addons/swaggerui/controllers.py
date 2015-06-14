from openerp import http


class SwaggerUI(http.Controller):

    @http.route("/api/", auth="public")
    def index(self, **kw):
        return http.request.render(
            "swaggerui.index", {"url": "http://petstore.swagger.io/v2/swagger.json"}
        )
