# -*- coding: utf-8 -*-
{
    'name': "Saldo APP - Setiembre",

    'summary': """
        Aplicación que le permitirá a tus usuarios gestionar sus ingresos y egresos""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Escuela FULLSTACK",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sales_team','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/res_groups.xml',
        'views/views.xml',
        'views/view_res_partner.xml',
        'views/templates.xml',
        'views/view_wizard.xml',
        'templates/movimientos.xml',
        'data/records_movimiento.xml',
        'data/categoria.xml',
        'report/report_templates.xml',
        'report/paperformat.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}