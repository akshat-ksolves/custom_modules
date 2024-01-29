from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointments"

    name = fields.Many2one('hospital.patient', string="Patient Name", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender",
                              related="name.gender")
    doctor_assigned = fields.Many2one('hospital.doctor', string="Doctor Assigned", required=True)
    appointment_date = fields.Date(string="Appointment Date", required=True)
    appointment_time = fields.Selection(
        [('slot1', '10 - 11'), ('slot2', '11 - 12'), ('slot3', '1 - 2'), ('slot4', '2 - 3'), ('slot5', '3 - 4'),
         ('slot6', '4 - 5'), ('slot7', '5 - 6'), ('slot8', '6 - 7'), ('slot9', '7 - 8'), ('slot10', '8 - 9')],
        required=True)

    def print_message(self):
        print("Hello World")

    def send_appointment_mail(self):
        mail = self.env["mail.mail"]
        values = {
            'email_from': 'akshat.mourya@ksolves.com',
            'email_to': 'aman.ali@ksolves.com',
            'body_html': f'''Your Appointment with Dr. {self.doctor_assigned} is booked for {self.appointment_date} at {self.appointment_time} ''',
            'subject': 'Test Email'
        }
        rec = mail.create(values)
        rec.send()
        # template_id = self.env.ref('hospital_management_system.action_send_email').id
        # print(template_id)
        # template = self.env['mail.template'].browse(template_id)
        # print(template)
        # template.send_mail(self.id, force_send=True)

    def fetch_appointments(self):
        query = f"""SELECT p.name,a.appointment_date,a.appointment_time FROM hospital_appointment AS a JOIN hospital_patient AS p ON p.id = a.name """
        self.env.cr.execute(query)
        print(self.env.cr.dictfetchall())

    def update_name(self):
        query = f"""UPDATE hospital_patient SET name='Virat Kohli' WHERE name='Virat'"""
        self.env.cr.execute(query)

