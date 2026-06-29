from odoo import api, fields, models


class ErrorPracticeTicket(models.Model):
    _name = "error.practice.ticket"
    _description = "Error Practice Ticket"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    assigned_user_id = fields.Many2one("res.users", string="Assigned To")
    name = fields.Char(required=True, tracking=True)
    partner_id = fields.Many2one("res.partner", string="Customer")
    priority = fields.Selection(
        [
            ("0", "Normal"),
            ("1", "Low"),
            ("2", "High"),
        ],
        default="0",
        tracking=True,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
        ],
        default="draft",
        tracking=True,
    )
    expected_hours = fields.Float()
    spent_hours = fields.Float()
    remaining_hours = fields.Float(compute="_compute_remaining_hours", store=True)
    note = fields.Text()

    @api.depends("expected_hours", "spent_hours")
    def _compute_remaining_hours(self):
        # Error 4: compute method does not assign a value for every record.
        # If expected_hours is empty/zero, Odoo can raise:
        # "Compute method failed to assign ..."
        for record in self:
            # if record.expected_hours:
                record.remaining_hours = record.expected_hours - record.spent_hours

    # Error 5: button in XML calls action_start, but this method is intentionally
    # named differently. Learner should either rename this method or update XML.
    def action_start(self):
        self.write({"state": "in_progress"})

    def action_done(self):
        self.write({"state": "done"})
