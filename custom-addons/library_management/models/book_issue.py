from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
    ], default='issued')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('library.book.issue') or 'New'

        book = self.env['library.book'].browse(vals.get('book_id'))

        if vals.get('status', 'issued') == 'issued':
            if book.available_copies <= 0:
                raise ValidationError("No copies available.")
            book.available_copies -= 1

        return super().create(vals)

    def write(self, vals):
        for record in self:
            old_status = record.status

            result = super().write(vals)

            new_status = record.status

            if old_status != 'returned' and new_status == 'returned':
                record.book_id.available_copies += 1

            elif old_status == 'returned' and new_status == 'issued':
                if record.book_id.available_copies <= 0:
                    raise ValidationError("No copies available.")
                record.book_id.available_copies -= 1

            return result