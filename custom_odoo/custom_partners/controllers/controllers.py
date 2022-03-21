# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPartners(http.Controller):
#     @http.route('/custom_partners/custom_partners', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_partners/custom_partners/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_partners.listing', {
#             'root': '/custom_partners/custom_partners',
#             'objects': http.request.env['custom_partners.custom_partners'].search([]),
#         })

#     @http.route('/custom_partners/custom_partners/objects/<model("custom_partners.custom_partners"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_partners.object', {
#             'object': obj
#         })
