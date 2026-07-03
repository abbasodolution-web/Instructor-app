from odoo import models, fields


class ConfirmBookIssueWizard(models.TransientModel):
    _name = 'confirm.book.issue.wizard'
    _description = 'Confirm Book Issue Wizard'

    book_issue_id = fields.Many2one('library.book.issue', string='Book Issue')
    member_id = fields.Many2one('library.member', string='Member', required=True)
    book_id = fields.Many2one('library.book', string='Book', required=True)
    issue_date = fields.Date(string='Issue Date')
    due_date = fields.Date(string='Due Date')

    def action_validate(self):
        self.book_issue_id.write({
            'member_id': self.member_id.id,
            'book_id': self.book_id.id,
            'issue_date': self.issue_date,
            'due_date': self.due_date,
            'status': 'issued',
        })

        return {'type': 'ir.actions.act_window_close'}