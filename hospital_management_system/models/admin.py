# from odoo import api, fields, models
#
# class HositalPatient (models.Model):
#     _name = "hospital.patient"
#     _description = "Record of Patients"
#
#     name = fields.Char(string="Name", required=True)
#     age = fields.Integer(string="Age")
#     isAdult = fields.Boolean(string="Is Adult or Not")
#     notes = fields.Text(string="Notes")
#     gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], string ="Gender")