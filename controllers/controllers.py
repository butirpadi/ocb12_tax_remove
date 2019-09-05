# -*- coding: utf-8 -*-
from odoo import http

# class TaxRemoveOcb12(http.Controller):
#     @http.route('/tax_remove_ocb12/tax_remove_ocb12/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tax_remove_ocb12/tax_remove_ocb12/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tax_remove_ocb12.listing', {
#             'root': '/tax_remove_ocb12/tax_remove_ocb12',
#             'objects': http.request.env['tax_remove_ocb12.tax_remove_ocb12'].search([]),
#         })

#     @http.route('/tax_remove_ocb12/tax_remove_ocb12/objects/<model("tax_remove_ocb12.tax_remove_ocb12"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tax_remove_ocb12.object', {
#             'object': obj
#         })