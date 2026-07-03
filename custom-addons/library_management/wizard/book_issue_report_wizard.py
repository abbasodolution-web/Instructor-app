from odoo import models, fields


class BookIssueReportWizard(models.TransientModel):
    _name = 'book.issue.report.wizard'
    _description = 'Book Issue Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def action_print_pdf(self):
        return self.env.ref('library_management.action_report_book_issue_pdf').report_action(self)

    def action_print_excel(self):
        pass

    def get_report_data(self):
        issues = self.env['library.book.issue'].search([
            ('issue_date', '>=', self.start_date),
            ('issue_date', '<=', self.end_date),
        ])

        data = []
        for issue in issues:
            books = issue.book_id.book_name if issue.book_id else ''
            data.append({
                'member_id': issue.member_id.id or '',
                'member_name': issue.member_id.name or '',
                'member_email': issue.member_id.email or '',
                'issue_id': issue.name or '',
                'book_names': books,
                'issue_date': issue.issue_date or '',
                'due_date': issue.due_date or '',
                'return_date': issue.return_date or '',
            })

        return data
        