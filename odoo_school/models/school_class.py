from odoo import api, fields, models, _


class SchoolClass(models.Model):

    _name = "school.class"
    _description = "This is model for Class details"

    name = fields.Char(string="Class")
    section = fields.Selection([('Section A','A'),('Section B','B'),('Section C','C')], string="Section")
    class_teacher = fields.Many2one('class.teacher', string="Class Teacher")
    class_students = fields.One2many('school.student', 'student_class_id', string="Students: ")

    _sql_constraints = [('unique_name', 'unique(name)','Enter a Unique Name')]

    # def _calculate_class_strength(self):
    #     strength = 0
    #     for students in self.env['school.student']:


class ClassSection(models.Model):

    _name = "class.section"
    _description = "This is model for sections of the classes students study in"

    name = fields.Selection([('Section A','A'),('Section B','B'),('Section C','C')], string="Section")

class ClassTeacher(models.Model):

    _name = "class.teacher"
    _description = "This is model of Class Teacher details"

    name = fields.Char(string="Teacher Name")
    age = fields.Integer(string="Age")
    teacher_subject = fields.Many2one('school.subject',string="Subject Taught")
    alloted_class = fields.Many2one('school.class')

class SchoolSubjects(models.Model):

    _name = "school.subject"
    _description = "This model defines all the subjects of the school"

    name = fields.Char(string="Subject Name")


