from odoo import models, fields
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta



class IssueBookWizard(models.TransientModel):
    _name = 'issue.book.wizard'
    _description = 'Issue Book Wizard'

    book_issue_id = fields.Many2one(
        'library.book.issue',
        string="Book Return"
    )

    issue_date = fields.Date(
        string="Issue Date",
        default=fields.Date.today,
    )

    due_date = fields.Date(
        string="Due Date",
        default=lambda self: fields.Date.today() + relativedelta(months=1)
    )

    remarks = fields.Text(string="Remarks")


    def action_confirm(self):

        if self.book_issue_id.status == 'issued':
            raise ValidationError("This book has already been issued.")

        self.book_issue_id.write({
            'status': 'issued',
            'issue_date': self.issue_date,
            'due_date' : self.due_date,
        })
        if self.book_issue_id.book_id.available_copies <= 0:
            raise ValidationError("No copies available.")
        self.book_issue_id.book_id.available_copies -= 1
        return {'type': 'ir.actions.act_window_close'}