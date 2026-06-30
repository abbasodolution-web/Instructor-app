from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string="Book ID", required=True, copy=False, readonly=True, default="New")
    book_name = fields.Char(string="Book Name", required=True)
    author = fields.Char(string="Author")
    category = fields.Char(string="Category")
    publisher = fields.Char(string="Publisher")
    isbn = fields.Char(string="ISBN")
    purchase_date = fields.Date(string="Purchase Date")
    price = fields.Float(string="Price")
    available = fields.Boolean(string="Available", default=True)
    total_copies = fields.Integer(string="Total Copies", default=1)
    available_copies = fields.Integer(string="Available Copies", default=1)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('library.book') or 'New'
        return super().create(vals)
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.name} - {record.book_name}"
            result.append((record.id, name))
        return result