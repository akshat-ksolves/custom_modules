{
    'name': 'Odoo School',
    'category': 'Education',
    'website': 'www.school.com',
    'version': '1.0.0',
    'summary': 'This is the custom Odoo School Module created as per the assignment sheet',
    'author': 'Akshat Mourya',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/class_view.xml',
        'views/fees.xml',
        'views/menu.xml'
    ]
}
