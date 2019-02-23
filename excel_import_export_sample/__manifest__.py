# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{'name': 'Excel Import/Export Samples',
 'version': '11.0.1.0.0',
 'author': 'Ecosoft,Odoo Community Association (OCA)',
 'license': 'AGPL-3',
 'website': 'https://github.com/OCA/server-tools/',
 'category': 'Tools',
 'depends': ['excel_import_export',
             'sale'],
 'data': ['import_export_sale_order/actions.xml',
          'import_export_sale_order/templates.xml',
          'report_sale_order/report_sale_order.xml',
          'report_sale_order/templates.xml',
          ],
 'installable': True,
 'development_status': 'alpha',
 'maintainers': ['kittiu'],
 }