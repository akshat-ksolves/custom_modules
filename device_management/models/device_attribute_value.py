from odoo import api, fields, models

# Device Attribute Value Model
class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'
    _description = 'This is Device Attribute Value Model'

    # Defining Fields for the given Model
    name = fields.Char(string="Name", required=True)
    device_attribute_id = fields.Many2one('device.attribute', string="Device Attribute")

    # SQL Constraints for unique name, device attribute id in the given fields
    _sql_constraints = [('unique_values', 'unique(name, device_attribute_id)', "Enter a unique value")]