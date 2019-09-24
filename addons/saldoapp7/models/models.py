# -*- coding: utf-8 -*-

from odoo import models, fields, api


"""
Clase models.Model
===================
Python --> SQL
create() --> Insert
write() --> update
unlink()  --> delete
search(),browse() --> select *
"""

class Movimiento(models.Model):
    _name = "sa.movimiento" # Nombre de la base de datos sa_movimiento (SQL)
    _description = "Movimiento" # Nombre del modelo en Odoo 'Movimiento' 

    name = fields.Char(string="Concepto",size=150,index = True)
    #monto = fields.Char("Monto")
    monto_total = fields.Float(string = "Monto")
    tipo = fields.Selection(string="Tipo",selection=[('I','Ingreso'),("E","Egreso")],default="I",required=True)
    fecha = fields.Date(string="Fecha de Operción")
    moneda = fields.Selection(string="Moneda",selection=[("PEN","Soles"),("USD","Dólares")])
    categoria_id = fields.Many2one("sa.categoria")
    
    concepto = fields.Html(string="Concepto")
    comprobante = fields.Binary(string="Comprobante")
    puntos = fields.Integer("Puntos",related="categoria_id.puntos")

class Categoria(models.Model):
    _name = "sa.categoria"
    _description = "Categoria"
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre")
    tipo = fields.Selection(string="Tipo",selection=[('I','Ingreso'),("E","Egreso")])
    active = fields.Boolean(string="Activo",default=True)
    puntos = fields.Integer("Puntos")
