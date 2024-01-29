from odoo import api, fields, models
from datetime import date

class HospitalPatient (models.Model):
    _name = "hospital.doctor"
    _description = "Record of Doctors"

    name = fields.Char(string="Name", required=True)
    doctor_dob = fields.Date(string="Date of Birth")
    doctor_age = fields.Integer(string="Age")
    doctor_department = fields.Char(string="Department", required=True)
    doctor_education = fields.Char(string="Qualification")
    doctor_advice = fields.Text(string="Advice")
    doctor_gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], string ="Gender")
    doctor_patient = fields.One2many('hospital.patient','doctor_assigned',string="Patient List")

    @api.onchange('doctor_dob')
    def _calculate_age(self):
        for record in self:
            today = date.today()
            if record.doctor_dob:
                record.doctor_age = today.year - record.doctor_dob.year
            else:
                record.doctor_age = 0