# -*- coding: utf-8 -*-
# from odoo import http


# class VehicleDetails(http.Controller):
#     @http.route('/vehicle_details/vehicle_details', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vehicle_details/vehicle_details/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vehicle_details.listing', {
#             'root': '/vehicle_details/vehicle_details',
#             'objects': http.request.env['vehicle_details.vehicle_details'].search([]),
#         })

#     @http.route('/vehicle_details/vehicle_details/objects/<model("vehicle_details.vehicle_details"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vehicle_details.object', {
#             'object': obj
#         })
