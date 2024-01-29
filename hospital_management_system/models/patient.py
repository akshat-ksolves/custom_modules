from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Record of Patients"

    # name_id = fields.Many2one('hospital.doctor',string="Name ID", required=True)
    name = fields.Char()
    patient_name = fields.Char(required=True)
    age = fields.Integer(string="Age")
    isAdult = fields.Boolean(string="Is Adult or Not")
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    doctor_assigned = fields.Many2one('hospital.doctor')
    company_id = fields.Many2one('res.company', string="Company")
    medicine_ids = fields.Many2many('hospital.medicine', 'relational_table', 'patient_id', 'medicine_id',
                                    string="Medicines")

    _sql_constraints = [('unique_values','unique(patient_name, doctor_assigned)','Cannot create duplicate record !')]

    def create_record(self):
        # query = f"""INSERT INTO hospital_patient VALUES('{self.patient_name}','{self.age}','{self.isAdult}','{self.notes}','{self.gender}', '{self.doctor_assigned}') """
        query = f"""INSERT INTO hospital_patient(patient_name,age,notes,gender,doctor_assigned) VALUES('{self.patient_name}','{self.age}','{self.notes}','{self.gender}', '{self.doctor_assigned.id}') """
        self.env.cr.execute(query)
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'success',
                'message': "New Record Created",
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }

    def delete_func(self):
        query = """DELETE FROM hospital_patient WHERE patient_name='XYZ'"""
        self.env.cr.execute(query)

    # @api.multi
    # def delete_records_from_new_db(self, vals):
    #     self.env['hospital.patient'].delete_records(self, vals)