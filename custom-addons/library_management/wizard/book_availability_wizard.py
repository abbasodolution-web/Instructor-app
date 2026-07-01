from odoo import models, fields


class BookAvailabilityWizard(models.TransientModel):
    _name = 'book.availability.wizard'
    _description = 'Book Availability Wizard'

    book_id = fields.Many2one(
        'library.book',
        string='Book',
        required=True
    )

    total_copies = fields.Integer(
        string='Total Copies',
        readonly=True
    )

    available_copies = fields.Integer(
        string='Available Copies',
        readonly=True
    )

    status = fields.Char(
        string='Status',
        readonly=True
    )

    def action_check(self):

        self.total_copies = self.book_id.total_copies
        self.available_copies = self.book_id.available_copies

        if self.book_id.available_copies > 0:
            self.status = "Available"
        else:
            self.status = "Not Available"

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'book.availability.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }