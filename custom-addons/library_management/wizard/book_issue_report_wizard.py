from odoo import models, fields
import io
import xlsxwriter
import base64


class BookIssueReportWizard(models.TransientModel):
    _name = 'book.issue.report.wizard'
    _description = 'Book Issue Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def action_print_pdf(self):
        return self.env.ref('library_management.action_report_book_issue_pdf').report_action(self)

    def action_print_excel(self):
        issues = self.env['library.book.issue'].search([
            ('issue_date', '>=', self.start_date),
            ('issue_date', '<=', self.end_date),
        ])

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Book Issue Report')

        title_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 16,
            'border': 1,
        })

        header_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'bg_color': '#D9EAF7',
            'border': 1,
        })
        book_format = workbook.add_format({
            'align': 'left',
            'valign': 'vcenter',
            'border': 1,
        })
        cell_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'border': 1,
        })

        date_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'border': 1,
            'num_format': 'yyyy-mm-dd',
        })

        # Column widths
        sheet.set_column('A:A', 12)
        sheet.set_column('B:B', 20)
        sheet.set_column('C:C', 28)
        sheet.set_column('D:D', 15)
        sheet.set_column('E:E', 40)
        sheet.set_column('F:H', 15)

        # Title
        sheet.merge_range('A1:H1', 'Library Book Issue Report', title_format)

        # Date range
        sheet.write('A3', 'Start Date', header_format)
        sheet.write('B3', str(self.start_date or ''), cell_format)
        sheet.write('D3', 'End Date', header_format)
        sheet.write('E3', str(self.end_date or ''), cell_format)

        # Headers
        row = 5
        headers = [
            'Member ID',
            'Member Name',
            'Email',
            'Issue ID',
            'Book Name',
            'Issue Date',
            'Due Date',
            'Return Date',
        ]

        for col, header in enumerate(headers):
            sheet.write(row, col, header, header_format)

        # Data rows
        row += 1
        for issue in issues:
            # If you use line_ids design:
            books = issue.book_id.book_name if issue.book_id else ''

            sheet.write(row, 0, issue.member_id.id or '', cell_format)
            sheet.write(row, 1, issue.member_id.name or '', cell_format)
            sheet.write(row, 2, issue.member_id.email or '', cell_format)
            sheet.write(row, 3, issue.name or '', cell_format)
            sheet.write(row, 4, books, book_format)
            sheet.write(row, 5, str(issue.issue_date or ''), cell_format)
            sheet.write(row, 6, str(issue.due_date or ''), cell_format)
            sheet.write(row, 7, str(issue.return_date or ''), cell_format)
            row += 1

        workbook.close()
        output.seek(0)

        file_data = base64.b64encode(output.read())
        output.close()

        attachment = self.env['ir.attachment'].create({
            'name': 'book_issue_report.xlsx',
            'type': 'binary',
            'datas': file_data,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }

    def get_report_data(self):
        issues = self.env['library.book.issue'].search([
            ('issue_date', '>=', self.start_date),
            ('issue_date', '<=', self.end_date),
        ])

        data = []
        for issue in issues:
            # If you use line_ids design:
            books = issue.book_id.book_name if issue.book_id else ''

            # If you use direct book_id design instead, use this line and comment the above one:
            # books = issue.book_id.name if issue.book_id else ''

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