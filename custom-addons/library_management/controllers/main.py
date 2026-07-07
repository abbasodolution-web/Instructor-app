from odoo import http
from odoo.http import request


class LibraryWebsiteController(http.Controller):

    @http.route('/book_issue', type='http', auth='public', website=True)
    def book_issue_form(self, **kwargs):
        members = request.env['library.member'].sudo().search([])
        books = request.env['library.book'].sudo().search([])
        success = kwargs.get('success')
        error = kwargs.get('error')
        return request.render('library_management.book_issue_website_form', {
            'members': members,
            'books': books,
            'success': success,
            'error': error,
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
            'return_date': post.get('return_date') or False,
            'status': post.get('status'),
        })

        book.write({
            'available_copies': book.available_copies - 1
        })

        return request.redirect('/book_issue?success=1')