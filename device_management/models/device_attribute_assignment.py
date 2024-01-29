from odoo import api, fields, models

# Device Attribute Assignment Model
class DeviceAttributeAssignment(models.Model):
    _name = 'device.attribute.assignment'
    _description = 'This is Device Attribute Assignment Model'

    # Defining Fields for the given Model
    device_id = fields.Many2one('device.device', string="Device Name")
    device_attribute_id = fields.Many2one('device.attribute', string="Device Attribute")
    device_attribute_value_id = fields.Many2one('device.attribute.value', string="Device Attribute Value")

    # SQL Constraints for unique device id, device attribute id in the given fields
    _sql_constraints = [('unique_values', 'unique(device_id, device_attribute_id)', "Enter Unique Values")]