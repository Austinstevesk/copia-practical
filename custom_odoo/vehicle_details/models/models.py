# -*- coding: utf-8 -*-

from odoo import models, fields, api

VEHICLE_TYPE_SELECTION = [
    ('suv', 'SUV'),
    ('lorry', 'Lorry'),
    ('sedan', 'Sedan')
]

VEHICLE_MAKE_SELECTION = [
    ('toyota', 'Toyota'),
    ('bmw', 'BMW'),
    ('subaru', 'Subaru')
]

FUEL_TYPE_SELECTION = [
    ('petrol', 'Petrol'),
    ('diesel', 'Diesel')
]

VEHICLE_LABEL_SELECTION = [
    ('label1', 'Label1'),
    ('label2', 'Label2')
]

class VehicleDetails(models.Model):
    _name = 'vehicle.details'
    _description = 'Vehicle Details'

    vehicle_reg = fields.Char(string='Vehicle Registration')
    vehicle_type = fields.Selection(VEHICLE_TYPE_SELECTION, string='Vehicle Type')
    vehicle_make = fields.Selection(VEHICLE_MAKE_SELECTION, string='Vehicle Make')
    classic_no = fields.Char(string='Classic Number')
    supplier = fields.Many2one('res.partner', string='Supplier')
    ins_exp_date = fields.Date(string='Insurance Expiry Date')
    fuel_type = fields.Selection(FUEL_TYPE_SELECTION)
    fuel_cons = fields.Float(string='Fuel Consumption')
    vehicle_tag = fields.Char(string='Vehicle Tag', default='_')
    vehicle_labels = fields.Selection(VEHICLE_LABEL_SELECTION, string='Vehicle Label')
    vehicle_status = fields.Boolean(string='Status of Vehicle')
    company = fields.Many2one('res.company')
    node_id = fields.Integer(string='Node ID')
    node_type_id = fields.Integer(string='Node Type ID')
    type = fields.Char(string='Type')
    fleet_no = fields.Char(string='Fleet Number')
    description = fields.Text(string='Description')
    mit = fields.Char(string='MIT')
    serial_no = fields.Char(string='Serial Number')
    cell_no = fields.Char(string='Cellphone Number')
    vehicle_symbol = fields.Integer(string='Vehicle Symbol')
    cost_center = fields.Integer(string='Cost Center')
    last_tracked_at = fields.Datetime(string='Last Tracked At')