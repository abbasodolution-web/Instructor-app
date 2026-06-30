from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re


class ResPartner(models.Model):
    _inherit = 'res.partner'

    cnic = fields.Char(
        string='CNIC',
        size=15,
        help='Computerized National Identity Card number, format: XXXXX-XXXXXXX-X',
        copy=False,
    )

    _sql_constraints = [
        ('cnic_unique', 'unique(cnic)', 'CNIC must be unique. This CNIC is already assigned to another contact.'),
    ]

    @api.constrains('cnic')
    def _check_cnic_format(self):
        cnic_pattern = re.compile(r'^\d{5}-\d{7}-\d{1}$')
        for partner in self:
            if partner.cnic and not cnic_pattern.match(partner.cnic):
                raise ValidationError(
                    "CNIC must be in the format XXXXX-XXXXXXX-X (e.g. 12345-1234567-1)."
                )
