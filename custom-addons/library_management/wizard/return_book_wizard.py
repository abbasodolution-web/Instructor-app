from odoo import models, fields
from odoo.exceptions import ValidationError


class ReturnBookWizard(models.TransientModel):
    _name = 'return.book.wizard'
    _description = 'Return Book Wizard'

    book_issue_id = fields.Many2one(
        'library.book.issue',
        string="Book Return"
    )

    return_date = fields.Date(
        string="Return Date",
        default=fields.Date.today
    )

    remarks = fields.Text(string="Remarks")


    def action_confirm(self):

        if self.book_issue_id.status == 'returned':
            raise ValidationError("This book has already been returned.")

        self.book_issue_id.write({
            'status': 'returned',
            'return_date': self.return_date,
        })
        self.book_issue_id.book_id.available_copies += 1
        return {'type': 'ir.actions.act_window_close'}