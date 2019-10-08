# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError



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

    name = fields.Char(string="Nombre",size=150,index = True)
    #monto = fields.Char("Monto")
    monto_total = fields.Float(string = "Monto")
    tipo = fields.Selection(string="Tipo",selection=[('I','Ingreso'),("E","Egreso")],default="I",required=True)
    fecha = fields.Date(string="Fecha de Operción")
    moneda = fields.Selection(string="Moneda",selection=[("PEN","Soles"),("USD","Dólares")])
    categoria_id = fields.Many2one("sa.categoria")
    
    concepto = fields.Html(string="Concepto")
    comprobante = fields.Binary(string="Comprobante")
    puntos = fields.Integer("Puntos",related="categoria_id.puntos")

    
    def get_partner(self):
        res_users_id = self.env.uid
        res_users_obj = self.env["res.users"].search([["id","=",res_users_id]])
        return res_users_obj.partner_id.id
    
    partner_id = fields.Many2one("res.partner","Usuario",default=get_partner)

    #user_id = fields.Many2one("res.users",default=lambda x:x.env.uid)
    
    """
    El self no necesariamente representa un solo registro

    caso 1: para un formulario, self si representa a un registro, y es el que se muestra en el form
    caso 2: para una lista, self representa a todos los registros de la lista.(para validar se debe iterar sobre cada uno de los registros)
    """
    @api.constrains('monto_total')
    def validar_monto(self):
        for record in self:
            if record.monto_total<=0 :
                raise ValidationError("El monto total debe ser mayor a Cero")
            if record.monto_total>1000000:
                raise ValidationError("El monto total debe ser menor a un millón")
            
    
    def action_server_view_wizard(self):
        wizard_form_id = self.env.ref("saldoapp7.wizard_form").id
        return {
            "type":"ir.actions.act_window",     
            "name":"Reporte de movimientos",
            "res_model":"sa.wizard.report",
            "views":[[wizard_form_id,"form"]],
            "view_mode":"form",
            "target":"self"
        }

    def saludo(self,nombre,apellido="*****"):
        return "Hola Mundo | "+nombre+" | "+apellido

    def actualizar_movimientos(self,movs):
        result = []
        for mov in movs:
            msg_error = []
            mov_id = mov["id"]
            
            v = False if type(mov_id) == int else "El id del movimiento debe ser entero"
            if v:
                msg_error.append(v)

            mov_obj = False
            try:
                mov_obj = self.env["sa.movimiento"].search([["id","=",mov_id]])
            except Exception as e:
                msg_error.append(e)
                self.env.cr.commit()

            if mov_obj:
                v = False if mov_obj.exists() else "El registro no existe o no tiene acceso a este"
                if v:
                    msg_error.append(v)
            
                res = mov_obj.write(mov["vals"])

            if len(msg_error):
                result.append({"id":mov["id"],"error":msg_error})
            else:
                result.append({"id":mov["id"],"result":"Se actualizo correctamente"})
            
        return result

class Categoria(models.Model):
    _name = "sa.categoria"
    _description = "Categoria"
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre")
    tipo = fields.Selection(string="Tipo",selection=[('I','Ingreso'),("E","Egreso")])
    active = fields.Boolean(string="Activo",default=True)
    puntos = fields.Integer("Puntos")
