{
    'name': 'Multi Module Task',
    'category': 'Long Task 1',
    'version': '1.0.0',
    'summary': 'This is custom module for multiple module connection task',
    'author': 'Akshat Mourya',
    'depends': ['base', 'sale', 'crm', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_inherit_view.xml',
        'views/sale_order_inherit_view.xml',
        'views/crm_inherit.xml',
        'wizards/sale_order_wizard.xml'
    ]
}
