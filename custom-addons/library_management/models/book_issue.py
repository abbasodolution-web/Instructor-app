from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryBookIssue(models.Model):
    _name = 'library.book.issue'
    _description = 'Book Issue'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string="Issue ID", required=True, copy=False, readonly=True, default="New")

    member_id = fields.Many2one('library.member', string="Member", required=True)
    book_id = fields.Many2one('library.book', string="Book", required=True)

    issue_date = fields.Date(string="Issue Date")
    due_date = fields.Date(string="Due Date")
    return_date = fields.Date(string="Return Date")

    status = fields.Selection([
        ('draft', 'Draft'),
        ('issued', 'Issued'),
        ('returned', 'Returned'),
    ], string='Status', default='draft')

    line_ids = fields.One2many(
        'library.book.issue.line',
        'issue_id',
        string='Issue Lines'
    )

    book_names = fields.Char(string='Books', compute='_compute_book_names', store=True)

    @api.depends('book_id')
    def _compute_book_names(self):
        for rec in self:
            rec.book_names = rec.book_id.name if rec.book_id else ''

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('library.book.issue') or 'New'
        return super().create(vals)

    
    
    def action_return_book(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Return Book',
            'res_model': 'return.book.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_book_issue_id': self.id,
            },
        }
    def action_issue_book(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Issue Book',
            'res_model': 'issue.book.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_book_issue_id': self.id,
            },
        }
    def action_open_confirm_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirm Book Issue',
            'res_model': 'confirm.book.issue.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_book_issue_id': self.id,
                'default_member_id': self.member_id.id,
                'default_book_id': self.book_id.id,
                'default_issue_date': self.issue_date,
                'default_due_date': self.due_date,
            },
        }