# -*- coding: utf-8 -*-
from odoo import http

# class ModuloVeterinaria(http.Controller):
#     @http.route('/modulo_veterinaria/modulo_veterinaria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_veterinaria/modulo_veterinaria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_veterinaria.listing', {
#             'root': '/modulo_veterinaria/modulo_veterinaria',
#             'objects': http.request.env['modulo_veterinaria.modulo_veterinaria'].search([]),
#         })

#     @http.route('/modulo_veterinaria/modulo_veterinaria/objects/<model("modulo_veterinaria.modulo_veterinaria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_veterinaria.object', {
#             'object': obj
#         })