{
    'name': 'DB connect',
    'description': 'Module for DB Connection Task',
    'depends': ['base', 'sale', 'contacts'],
    'version': '1.1',
    'author': 'New DB',
    'data': [
        'views/newContactWizard.xml',
        'views/contact_inherit_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            # 'device_management/static/src/js/customButton.xml',
            # 'db_task/static/src/js/customButton.js',
        ]
    }
}
