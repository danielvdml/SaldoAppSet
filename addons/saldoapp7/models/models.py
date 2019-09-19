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

    name = fields.Char("Concepto")
    monto = fields.Char("Monto")