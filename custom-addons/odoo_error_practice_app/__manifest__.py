{
    "name": "Error Practice App",
    "version": "15.0.1.0.0",
    "category": "Training",
    "summary": "Broken Odoo addon for intern debugging practice",
    "description": """
Error Practice App
==================

This module is intentionally broken for Odoo development training.
The learner should install/upgrade it, read each error, find the root cause,
fix it, and document the final result.
""",
    "author": "Odolution",
    "sequence": -59,
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/error_practice_views.xml",
        "views/menu_views.xml",
    ],
    "installable": True,
    "application": True,
}
