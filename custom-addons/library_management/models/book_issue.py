from odoo import models, fields, api


class LibraryBookIssue(models.Model):
    _name = 'library.book.issue'
    _description = 'Book Issue'

    name = fields.Char(string="Issue ID", required=True, copy=False, readonly=True, default="New")

    member_id = fields.Many2one('library.member', string="Member", required=True)
    book_id = fields.Many2one('library.book', string="Book", required=True)

    issue_date = fields.Date(string="Issue Date")
    due_date = fields.Date(string="Due Date")
    return_date = fields.Date(string="Return Date")

    status = fields.Selection([
        ('issued', 'Issued'),
        ('returned', 'Returned'),
        ('late', 'Late'),
    ], string="Status", default='issued')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('library.book.issue') or 'New'
        return super().create(vals)