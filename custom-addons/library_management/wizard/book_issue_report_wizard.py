from odoo import models, fields


class BookIssueReportWizard(models.TransientModel):
    _name = 'book.issue.report.wizard'
    _description = 'Book Issue Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def action_print_pdf(self):
        pass

    def action_print_excel(self):
        pass