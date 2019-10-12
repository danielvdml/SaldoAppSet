# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Saldoapp7(http.Controller):

    @http.route('/perfil', auth='public')
    def index(self, **kw):
        return "<h1>Mi Perfil</h1>"


    @http.route("/api/movimientos",auth="user",type="json")
    def movimientos(self,**kw):
        movs = http.request.env["sa.movimiento"].sudo().search([])
        movimientos = [{"id":mov.id,"nombre":mov.name,"monto":mov.name} for mov in movs]
        return movimientos
    

    @http.route("/movimientos",auth="user",type="http",website=True)
    def lista_movimientos(self):    
        movs = http.request.env["sa.movimiento"].search([])
        usuario = request.env.user.name
        return http.request.render("saldoapp7.view_qweb_movimientos",{"movimientos":movs,"usuario":usuario})
