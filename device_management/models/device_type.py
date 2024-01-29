from odoo import api, fields, models


# Device Type Model
class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'This is Device Type model'

    # Defining Fields for the given Model
    name = fields.Char(string="Device Name")
    code = fields.Char(string="Device Code")
    dev = fields.Char(string="Dummy for sequence")
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string="Device Name")
    device_model_ids = fields.One2many('device.model', 'device_type_id', string="Device Name")
    device_ids = fields.One2many('device.device', 'device_type_id', string="Device Type")

    # SQL Constraints for unique name and code in the given fields
    _sql_constraints = [('unique_type', 'unique(name, code)', 'Please enter a unique value')]
