# -*- coding: utf-8 -*-
# from odoo import http


# class TransportationManagement(http.Controller):
#     @http.route('/transportation_management/transportation_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transportation_management/transportation_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('transportation_management.listing', {
#             'root': '/transportation_management/transportation_management',
#             'objects': http.request.env['transportation_management.transportation_management'].search([]),
#         })

#     @http.route('/transportation_management/transportation_management/objects/<model("transportation_management.transportation_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transportation_management.object', {
#             'object': obj
#         })
