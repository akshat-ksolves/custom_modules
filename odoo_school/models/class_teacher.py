from odoo import api, fields, models

class ClassTeacher(models.Model):

    _name = "class.teacher"
    _description = "This is model of Class Teacher details"

    name = fields.Char(string="Teacher Name")
    age = fields.Integer(string="Age")
    teacher_subject = fields.Many2one('school.subject',string="Subject Taught")
    alloted_class = fields.Many2one('school.class')