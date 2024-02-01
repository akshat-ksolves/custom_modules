from odoo import api, fields, models

# Device Assignment Model
class DeviceAssignment(models.Model):
    _name = 'device.assignment'
    _description = 'This is Device Assignment Model'

    # Defining fields for the given model
    name = fields.Char(string="Name")
    device_id = fields.Many2one('device.device', string="Device ID")
    employee_id = fields.Many2one('hr.employee', string="Employee Name")
    date_start = fields.Date(string="Start Date")
    date_expire = fields.Date(string="Expiry Date")
    state = fields.Selection([('new','New'),('draft','Draft'),('approved','Approved'),('returned','Returned'),('rejected','Rejected')], string="State")

    # Defining Sql Constraints for the Given Model
    _sql_constraints = [('unique_name', 'unique(name)', 'Please Enter a unique name')]


    def changeState(self):
        if (len(self.ids)) == 0:
            return False
        else:
            self.write({'state': 'approved'})
            return {
                'type': 'ir.actions.client',
                'tag': "soft_reload",
            }

        # for result_id in self.ids:
        #     print(result_id)
        # selected_ids = self.env.context.get('active_ids', [])
        # selected_records = self.env['device.assignment'].browse(selected_ids)
        # print(selected_records)