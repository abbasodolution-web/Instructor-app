from odoo import models, fields


class ReturnBookWizard(models.TransientModel):
    _name = 'return.book.wizard'
    _description = 'Return Book Wizard'

    return_date = fields.Date(
        string="Return Date",
        default=fields.Date.today
    )

    remarks = fields.Text(string="Remarks")