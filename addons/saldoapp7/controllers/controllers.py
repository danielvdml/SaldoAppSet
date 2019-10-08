# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Saldoapp7(http.Controller):

    @http.route('/perfil', auth='public')
    def index(self, **kw):
        return "<h1>Mi Perfil</h1>"


    @http.route("/api/movimientos",auth="user",type="json")
    def movimientos(self,**kw):
        movs = request.env["sa.movimiento"].sudo().search([])
        movimientos = [{"id":mov.id,"nombre":mov.name,"monto":mov.monto_total} for mov in movs]
        return movimientos
        


#     @http.route('/saldoapp7/saldoapp7/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('saldoapp7.listing', {
#             'root': '/saldoapp7/saldoapp7',
#             'objects': http.request.env['saldoapp7.saldoapp7'].search([]),
#         })

#     @http.route('/saldoapp7/saldoapp7/objects/<model("saldoapp7.saldoapp7"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saldoapp7.object', {
#             'object': obj
#         })