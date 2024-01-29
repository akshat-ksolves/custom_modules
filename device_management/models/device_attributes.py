from odoo import api, fields, models

# Device Attribute Model
class DeviceAttribute(models.Model):
    _name = 'device.attribute'
    _description = 'This is Device Attributes Model'

    # Defining Fields for the given Model
    name = fields.Char(string="Name", required=True)
    device_type_id = fields.Many2one('device.type', string="Device Type")
    required = fields.Boolean(string="Is required or Not")
    device_attribute_value_ids = fields.One2many('device.attribute.value', 'device_attribute_id',
                                                 string="Device Attribute Value")
    custom_setting_visibility = fields.Boolean(compute="check_visibility")

    # SQL Constraints for unique name in the given fields
    _sql_constraints = [('unique_name', 'unique(name)', "Enter a unique value")]

    @api.depends('custom_setting_visibility')
    def check_visibility(self):
        self.custom_setting_visibility = self.env['ir.config_parameter'].get_param('xyz')
        # if res in ['True']:
        #     self.custom_setting_visibility = True
        # else:
        #     self.custom_setting_visibility = False

