{
    'name': 'Library Management System',
    'version': '17.0.1.0.0',
    'summary': 'Library Management System',
    'description': 'Manage books, members, book issues and reports.',
    'category': 'Library',
    'author': 'SMAbbasS',
    'sequence': -300,
    'license': 'LGPL-3',
    'depends': ['base','mail','website'],
    'data': [
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/book_views.xml',
        'views/member_views.xml',
        'views/book_issue_views.xml',
        'views/report_views.xml',

        'wizard_views/book_availability_wizard_views.xml',
        'wizard_views/return_book_wizard_views.xml',
        'wizard_views/issue_book_wizard_views.xml',
        'wizard_views/confirm_book_issue_wizard_views.xml',
        'wizard_views/member_issue_book_wizard_views.xml',
        'wizard_views/book_issue_report_wizard_views.xml',

        'menus/menu.xml',

        'report/library_report.xml',
        'report/library_report_template.xml',
        'report/book_issue_report_template.xml',
        'report/book_issue_report_action.xml',

        'website_views/website_menu.xml',
        'website_views/website_book_issue_template.xml',
        'website_views/website_book_return_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}