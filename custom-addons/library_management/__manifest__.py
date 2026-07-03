{
    'name': 'Library Management System',
    'version': '17.0.1.0.0',
    'summary': 'Library Management System',
    'description': 'Manage books, members, book issues and reports.',
    'category': 'Library',
    'author': 'SMAbbasS',
    'sequence': -300,
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',

        'data/sequence.xml',

        
        'views/menu.xml',
        'views/book_views.xml',
        'views/member_views.xml',
        'views/book_issue_views.xml',
        'views/report_views.xml',

        'views/book_availability_wizard_views.xml',
        'views/return_book_wizard_views.xml',
        # 'views/issue_book_wizard_views.xml',
        'views/confirm_book_issue_wizard_views.xml',

        'report/library_report.xml',
        'report/library_report_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}