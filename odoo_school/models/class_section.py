from odoo import api, fields, models

class ClassSection(models.Model):

    _name = "class.section"
    _description = "This is model for sections of the classes students study in"

    name = fields.Selection([('Section A','A'),('Section B','B'),('Section C','C')], string="Section")