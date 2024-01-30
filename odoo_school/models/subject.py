from odoo import api, fields, models

class SchoolSubjects(models.Model):

    _name = "school.subject"
    _description = "This model defines all the subjects of the school"

    name = fields.Char(string="Subject Name")