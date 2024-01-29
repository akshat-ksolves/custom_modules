from odoo import api, fields, models

# Device Model
class Device(models.Model):
    _name = 'device.device'
    _description = 'This is Device Model'

    # Defining Fields for the given Model
    name = fields.Char(string="Device Name", required=True)
    shared = fields.Boolean(string="Shared Device or Not")
    device_type_id = fields.Many2one('device.type', string="Device Type")
    device_brand_id = fields.Many2one('device.brand', string="Device Brand")
    device_model_id = fields.Many2one('device.model', string="Device Model")
    attributes = fields.One2many('device.attribute.assignment', 'device_id', string="Attributes")

    # SQL Constraints for unique name in the given fields
    _sql_constraints = [('unique_name', 'unique(name)', 'Please Enter a unique name')]

