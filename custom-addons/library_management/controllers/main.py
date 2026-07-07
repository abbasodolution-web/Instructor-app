from odoo import http
from odoo.http import request
from datetime import date
from dateutil.relativedelta import relativedelta


class LibraryWebsiteController(http.Controller):

    @http.route('/book_issue', type='http', auth='public', website=True)
    def book_issue_form(self, **kwargs):
        members = request.env['library.member'].sudo().search([])
        books = request.env['library.book'].sudo().search([])
        success = kwargs.get('success')
        error = kwargs.get('error')
        today = date.today()
        due_date = today + relativedelta(months=1)
        return request.render('library_management.book_issue_website_form', {
            'members': members,
            'books': books,
            'success': success,
            'error': error,
            'today': today,
            'due_date': due_date,
        })

    @http.route('/book_issue/submit', type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def book_issue_submit(self, **post):
        book = request.env['library.book'].sudo().browse(int(post.get('book_id')))

        if not book or book.available_copies <= 0:
            return request.redirect('/book_issue?error=1')

        request.env['library.book.issue'].sudo().create({
            'member_id': int(post.get('member_id')),
            'book_id': book.id,
            'issue_date': post.get('issue_date'),
            'due_date': post.get('due_date'),
            'return_date': False,
            'status': 'issued',
        })

        book.write({
            'available_copies': book.available_copies - 1
        })

        return request.redirect('/book_issue?success=1')
    
        # For Book Return Form

    @http.route('/book_return', type='http', auth='public', website=True)
    def book_return_form(self, **kwargs):
        issues = request.env['library.book.issue'].sudo().search([
            ('status', '=', 'issued')
        ])
        selected_issue = False
        issue_id = kwargs.get('book_issue_id')
        if issue_id:
            selected_issue = request.env['library.book.issue'].sudo().browse(int(issue_id))

        return request.render('library_management.book_return_website_form', {
            'issues': issues,
            'selected_issue': selected_issue,
            'today': date.today(),
            'success': kwargs.get('success'),
            'error': kwargs.get('error'),
        })

    @http.route('/book_return/submit', type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def book_return_submit(self, **post):
        issue_id = int(post.get('book_issue_id'))
        issue = request.env['library.book.issue'].sudo().browse(issue_id)

        if not issue or issue.status != 'issued':
            return request.redirect('/book_return?error=1')

        issue.write({
            'return_date': post.get('return_date'),
            'status': 'returned',
        })

        if issue.book_id:
            issue.book_id.sudo().write({
                'available_copies': issue.book_id.available_copies + 1
            })

        return request.redirect('/book_return?success=1')