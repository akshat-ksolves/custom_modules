from odoo import api, fields, models, _


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "This model is for school's student details"

    name = fields.Char(string="Student Name", required=True)
    student_enrolment = fields.Char(string="Enrolment Number", readonly=True)
    student_class_id = fields.Many2one('school.class', string="Class")
    student_subject_ids = fields.Many2many('school.subject', string="Section")
    # student_fee = fields.Integer(string="")

    @api.model
    def create(self, vals):
        vals['student_enrolment'] = self.env['ir.sequence'].next_by_code('student.sequence') or 1
        return super(SchoolStudent, self).create(vals)