from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    cnic = fields.Char(string="CNIC")