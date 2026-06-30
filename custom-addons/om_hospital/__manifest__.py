{
    'name': 'Hospital Management Test',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Odolution',
    'sequence': -100,
    'summary': 'Hospital Management System',
    'description': """hospital management system for managing patients, doctors, appointments, and medical records.""",          
    'depends':['base','mail','base_automation'],
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'data/patient_sequence.xml',
        'views/female_patient.xml',
    ],
    'demo': [],

    'installable': True,
    'application': True,
    'autoinstall': False,
    'license': 'LGPL-3',
}   