from odoo import api, fields, models


class SchoolFee(models.Model):

    _name = 'school.fees'
    _description = "This model is for School Fees"

    name = fields.Char()
    fees_due = fields.Integer(string="Fees Due", readonly=True)
    total_fees = fields.Integer(string="Total Fees")
    monthly_fees = fields.Integer(string="Monthly Fees")

