from odoo import models, fields


class MemberIssueBookWizard(models.TransientModel):
    _name = 'member.issue.book.wizard'
    _description = 'Member Issue Book Wizard'

    member_id = fields.Many2one('library.member', string='Member', required=True, readonly=True)
    book_id = fields.Many2one('library.book', string='Book', required=True)
    issue_date = fields.Date(string='Issue Date', default=fields.Date.today)
    due_date = fields.Date(string='Due Date')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('issued', 'Issued'),
        ('returned', 'Returned'),
    ], string='Status', default='confirmed')

    def action_confirm(self):
        self.env['library.book.issue'].create({
            'member_id': self.member_id.id,
            'book_id': self.book_id.id,
            'issue_date': self.issue_date,
            'due_date': self.due_date,
            'status': 'issued',
        })

        return {'type': 'ir.actions.act_window_close'}