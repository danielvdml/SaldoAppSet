from odoo import api, models 

class MovimientoReport(models.AbstractModel):
    _name = "report.saldoapp7.report_movimiento"

    @api.model
    def _get_report_values(self,docids,data=None):
        #docids => es un arreglo de los ids de registros selecciondas desde la interface
        
        partners = self.env["res.partner"].browse(docids)
        
        def get_ingresos(movs):
            return sum([mov.monto_total for mov in movs if mov.tipo=="I"])

        def get_egrespos(movs):
            return sum([mov.monto_total for mov in movs if mov.tipo=="E"])

        def get_ingresos_soles(partner_id):
            movs = self.env["sa.movimiento"].search([["partner_id","=",partner_id],["moneda","=","PEN"]])
            return get_ingresos(movs)

        return {
            'docs':partners,
            'get_ingresos':get_ingresos,
            "get_egrespos":get_egrespos,
            "get_ingresos_soles":get_ingresos_soles
        }