from odoo import models, fields


class LibraryBookIssueLine(models.Model):
    _name = 'library.book.issue.line'
    _description = 'Library Book Issue Line'

    issue_id = fields.Many2one(
        'library.book.issue',
        string='Book Issue',
        ondelete='cascade'
    )

    book_id = fields.Many2one(
        'library.book',
        string='Book',
        required=True
    )