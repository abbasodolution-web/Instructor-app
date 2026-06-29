{
    'name': 'Error Practice App',
    'version': '17.0.1.0.0',
    'category': 'Training',
    'author': 'Odolution',
    'sequence': -200,
    'summary': 'Broken Odoo addon for intern debugging practice',
    "description": """
        Error Practice App
        ==================

        This module is intentionally broken for Odoo development training.
        The learner should install/upgrade it, read each error, find the root cause,
        fix it, and document the final result.
    """,
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/error_practice_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'autoinstall': False,
    'license': 'LGPL-3',
}
