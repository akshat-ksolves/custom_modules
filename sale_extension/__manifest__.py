{
    'name': 'sale_extension',
    'summary': 'Sale Extension Module for Sale Order Inheritance',
    'author': 'Akshat',
    'version': '1.1',
    'depends': ['sale'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/extension.xml',
        'wizards/data_wizard_view.xml',
        'views/sale_order_inherit.xml',
        'views/menu.xml',
        'reports/sample_report.xml',
    ]
}
