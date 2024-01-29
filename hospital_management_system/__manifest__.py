{
    'name': 'Hospital Management',
    'category': 'Medical and Emergency',
    'website': 'www.hospitalmanagement.com',
    'version': '1.0.0',
    'summary': 'This is the first custom module created at the start of the training to learn Odoo Development',
    'author': 'Akshat Mourya',
    'depends': ['mail'],
    'sequence': '-100',
    'data': [
        'security/ir.model.access.csv',
        'security/security_access_data.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/appointments.xml',
        'views/scheduled_action_demo.xml',
        'views/sample_email.xml',
        'wizards/check_appointment_wizard.xml',
        'views/menu.xml',
        'reports/appointment_receipt.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'hospital_management_system/static/src/test.js',
            'hospital_management_system/static/src/**/*',
        ]
    }
}
