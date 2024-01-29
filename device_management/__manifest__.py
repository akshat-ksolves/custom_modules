{
    'name': "Device Managem ent",
    'category': 'Device Management',
    'description': 'This is Device Management Application for the assignment sheet',
    'author': 'Akshat Mourya',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_inherit.xml',
        'views/device_view.xml',
        'views/device_type_view.xml',
        'views/device_assigned_view.xml',
        'views/device_attribute.xml',
        'views/device_attribute_assignment.xml',
        'views/device_attribute_assignment_value.xml',
        'views/custom_settings_view.xml',
        'views/menu.xml'
        
    ]
}
