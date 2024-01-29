from odoo import api, fields, models

class HospitalMedicine(models.Model):
    _name = "hospital.medicine"

    name = fields.Char(string="Medicine Name")
    medicine_used = fields.Char(string="Disease Cured")
    patient_ids = fields.Many2many("hospital.patient",'relational_table','medicine_id', 'patient_id',string="Patients")
    color = fields.Integer(string="Colour")