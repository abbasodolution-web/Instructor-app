from odoo import models


class ReportBookIssuePdf(models.AbstractModel):
    _name = 'report.library_management.report_book_issue_pdf'
    _description = 'Book Issue PDF Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['book.issue.report.wizard'].browse(docids)
        report_data = docs.get_report_data()

        return {
            'doc_ids': docids,
            'doc_model': 'book.issue.report.wizard',
            'docs': docs,
            'report_data': report_data,
        }