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
    book_issue_ids = fields.One2many(
        'library.book.issue',
        'member_id',
        string='Book Issues'
    )

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('library.member') or 'New'
        return super().create(vals)
    
    @api.depends('name', 'member_name')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} - {record.member_name}"

    def action_open_issue_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Issue Book',
            'res_model': 'member.issue.book.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_member_id': self.id,
            },
        }

    def action_view_book_issues(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Book Issues',
            'res_model': 'library.book.issue',
            'view_mode': 'tree,form',
            'domain': [('member_id', '=', self.id)],
            'context': {
                'default_member_id': self.id,
            },
        }
