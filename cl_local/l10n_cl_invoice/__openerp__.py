# -*- coding: utf-8 -*-
{   'active': False,
    'author': u'Blanco Martín & Asociados',
    'website': 'http://blancomartin.cl',
    'category': 'Localization/Chile',
    'demo_xml': [
       # 'data/partner_demo.xml',
      ],
    'depends': [   
        'account',
        'account_accountant',
        'l10n_cl_base_rut',
        'l10n_cl_partner_activities',
        'decimal_precision'
        ],
    'description': u'''


Módulo de Facturación de la localización Chilena.


Incluye:
- Configuración de libros, diarios (journals) y otros detalles para facturación para Chile.
- Asistente para configurar los talonarios de facturas, boletas, guías de despacho, etc.
''',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'Chile - Sistema de apoyo a la facturación',
    'test': [   
#        'test/products.yml',
#        'test/partners.yml',
#        'test/com_ri1.yml',
#        'test/com_ri2.yml',
#        'test/com_rm1.yml',
#        'test/inv_ri2ri.yml',
#        'test/inv_rm2ri.yml',
#        'test/inv_ri2rm.yml',
#        'test/bug_1042944.yml'
        ],
    'data': [
        'data/document_type.xml',
        'security/l10n_cl_invoice_security.xml',
        'data/responsability.xml',
        'data/sii.document_letter.csv',
        'data/sii.document_class.csv',
        'data/partner.xml',
        'data/country.xml',
        'data/sii.concept_type.csv',
        'data/decimal_precision_data.xml',
        'views/company_view.xml',
        'views/country_view.xml',
        'views/sii_document_letter_view.xml',
        'views/sii_concept_type_view.xml',
        'views/sii_optional_type_view.xml',
        'views/sii_document_type_view.xml',
        'views/sii_responsability_view.xml',
        'views/sii_document_class_view.xml',
        'views/sii_point_of_sale_view.xml',
        'views/account_journal_sii_document_class_view.xml',
        'views/partner_view.xml',
        'views/journal_view.xml',
        'views/invoice_view.xml',
        'views/product_view.xml',
        'views/account_move_view.xml',
        'views/account_move_line_view.xml',
        'views/config_view.xml',
        'views/currency_view.xml',
        # 'views/report_invoice.xml',
        'security/ir.model.access.csv',
        'security/l10n_cl_invoice_security.xml',
        'data/res.currency.csv',
        #'views/sii_menuitem.xml',
        'wizard/journal_config_wizard_view.xml',
    ],
    'version': '8.1.0.0',
}
