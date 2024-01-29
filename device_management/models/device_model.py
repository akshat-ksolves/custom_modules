from odoo import api, fields, models

# Device Model's Model
class DeviceModel(models.Model):
    _name = 'device.model'
    _description = "This is Device Model's Model"

    # Defining Fields for the given Model
    name = fields.Char(string="Device Model", required=True)
    device_type_id = fields.Many2one('device.type', string="Device Type")
    device_brand_id = fields.Many2one('device.brand', string="Device Brand")

    # SQL Constraints for Unique name, Device type and device brand id in the given fields
    _sql_constraints = [('unique_model', 'unique(name, device_type_id, device_brand_id)',
                         'Field already exists.\nTry with a different value')]
