# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

CHILDREN_SELECTION = [
    ('yes', 'Yes'),
    ('no', 'No')
]

GENDER_SELECTION = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
]

class ResPartner(models.Model):
    _inherit = "res.partner"

    has_children = fields.Selection(CHILDREN_SELECTION, string='Has Children ?')
    no_of_children = fields.Integer(string='No of Children')
    children_ids = fields.One2many('customer.children', 'parent_id', string='children')

    @api.constrains('children_ids')
    def validate_children(self):
        for partner in self:
            if len(partner.children_ids) > partner.no_of_children:
                raise exceptions.ValidationError('Customer cannot have more than {} children'.format(partner.no_of_children))

class PartnerChildren(models.Model):
    _name = 'customer.children'

    name = fields.Char(string='Name')
    age = fields.Integer(string='age')
    gender = fields.Selection(GENDER_SELECTION, string='Gender')
    parent_id = fields.Many2one('res.partner', string='parent')