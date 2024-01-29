from odoo import api, fields, models, _


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "This model is for school's student details"

    name = fields.Char(string="Student Name", required=True)
    student_enrolment = fields.Char(string="Sequence Reference", required=True, readonly=True, default=lambda self: _('New'), )
    student_class_id = fields.Many2one('school.class', string="Class")
    student_subject_ids = fields.Many2many('school.subject', string="Section")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('student_enrolment', _('New')) == _('New'):
                vals['student_enrolment'] = self.env['ir.sequence'].next_by_code('school.student.sequence') or _('New')
        return super(SchoolStudent, self).create(vals_list)

