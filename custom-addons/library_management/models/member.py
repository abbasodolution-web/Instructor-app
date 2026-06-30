from odoo import models, fields, api


class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(string="Member ID", required=True, copy=False, readonly=True, default="New")
    member_name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    address = fields.Text(string="Address")
    membership_date = fields.Date(string="Membership Date")
    membership_type = fields.Selection([
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('public', 'Public'),
    ], string="Membership Type")
    active = fields.Boolean(string="Active", default=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('library.member') or 'New'
        return super().create(vals)