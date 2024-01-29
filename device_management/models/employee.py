from odoo import api, fields, models

class Employee(models.Model):
    _inherit = 'hr.employee'

    device_ids = fields.One2many('device.assignment','employee_id', string="Device Assigned")