# -*- coding: utf-8 -*-
from odoo import http

# class Saldoapp7(http.Controller):
#     @http.route('/saldoapp7/saldoapp7/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

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