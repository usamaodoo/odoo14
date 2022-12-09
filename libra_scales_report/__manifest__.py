# -*- coding: utf-8 -*-
{
    'name': "Libra Scales Report",
    'description': "Libra Scales PDF Report",
    'sequence': 5,
    'author': 'Usama Shakeel',
    'website': "http://www.xyz.com",
    'category': 'Purchase',
    'version': '14.0.1.0',
    'application': False,
    'depends': ['base', 'purchase','sale_management','sale'],
    'license': 'LGPL-3',
    'data': [
        'wizard/scales_report_wizard.xml',
        'report/report_format.xml',
        'report/report_header_footer.xml',
        'report/weighment_report_template.xml',
        'report/serial_wise_weight_report_template.xml',
        'report/vehicle_wise_report_template.xml',
        'report/customer_weight_report_template.xml',
        'report/products_report_template.xml',
        'report/party_name_report_template.xml',
        'report/product_name_report_template.xml',


    ],
    'installable': True,
    'auto_install': False,

}
