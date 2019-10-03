from odoo import api,models,fields

class WizardReportMovimiento(models.TransientModel):
    _name = 'sa.wizard.report'

    fecha_inicio = fields.Date("Fecha de inicio",default=fields.Date.today())
    fecha_fin = fields.Date("Fecha fin",default=fields.Date.today())

    """
    def imprimir_reporte(self):
        if self.fecha_inicio and self.fecha_fin:
            domain = [["fecha",">=",self.fecha_inicio],["fecha","<=",self.fecha]]
            user_id = self.env.uid
            partner_id = self.env["res.users"].sudo().browse(user_id).partner_id.id
            report_obj = self.env.ref("saldoapp7.sa_report_movimiento_partner")
            
            data = {
                "domain":domain
            }
            return report_obj.report_action([partner_id],data)
            
    """


        