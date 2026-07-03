from odoo import models, fields
class ConfirmBookIssueLineWizard(models.TransientModel):
    _name = 'confirm.book.issue.line.wizard'

    wizard_id = fields.Many2one('confirm.book.issue.wizard')
    book_id = fields.Many2one('library.book')
    qty = fields.Integer()