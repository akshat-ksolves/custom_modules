from odoo import api, fields, models

# Device Brand Model
class DeviceBrand(models.Model):
    _name = 'device.brand'
    _description = 'This is device Brand Model'

    # Defining Fields for the given Model
    name = fields.Char(string="Brand Name", required=True)
    device_model_ids = fields.One2many('device.model', 'device_brand_id', string="Device Model")

    # SQL Constraints for unique name in the given fields
    _sql_constraints = [('unique_name', 'unique(name', 'Enter a unique value')]