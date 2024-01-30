from odoo import api, fields, models, _


class SchoolClass(models.Model):

    _name = "school.class"
    _description = "This is model for Class details"

    name = fields.Char(string="Class")
    section = fields.Selection([('Section A','A'),('Section B','B'),('Section C','C')], string="Section")
    class_teacher = fields.Many2one('class.teacher', string="Class Teacher")
    class_students = fields.One2many('school.student', 'student_class_id', string="Students: ")

    _sql_constraints = [('unique_name', 'unique(name,class_teacher)', 'Enter a Unique Name')]
