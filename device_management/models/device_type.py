from odoo import api, fields, models


# Device Type Model
class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'This is Device Type model'

    # Defining Fields for the given Model
    name = fields.Char(string="Device Name")
    code = fields.Char(string="Device Code")
    sequence = fields.Char(string="Device Sequence ID", readonly=True)
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string="Device Name")
    device_model_ids = fields.One2many('device.model', 'device_type_id', string="Device Name")
    device_ids = fields.One2many('device.device', 'device_type_id', string="Device Type")

    # SQL Constraints for unique name and code in the given fields
    _sql_constraints = [('unique_type', 'unique(name, code)', 'Please enter a unique value')]

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('device.type.sequence')
        return super(DeviceType, self).create(vals)