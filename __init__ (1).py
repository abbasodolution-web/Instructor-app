{
    'name': 'Contact CNIC Field',
    'version': '17.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Add CNIC field to Contacts',
    'description': """
        Adds a custom CNIC (Computerized National Identity Card) field
        to the Contacts (res.partner) form.
    """,
    'author': 'Your Company',
    'depends': ['contacts', 'base'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
