from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CheckAppointmentWizard(models.TransientModel):
    _name = 'check.appointment.wizard'
    _description = 'Description for Check appointment'

    name = fields.Many2one('hospital.doctor', string="Doctor's Name", required=True)
    patient_name = fields.Many2one('hospital.patient', string="Patient Name")
    appointment_date = fields.Date(string="Appointment Date", required=True)
    appointment_time = fields.Selection(
        [('slot1', '10 - 11'), ('slot2', '11 - 12'), ('slot3', '1 - 2'), ('slot4', '2 - 3'), ('slot5', '3 - 4'),
         ('slot6', '4 - 5'), ('slot7', '5 - 6'), ('slot8', '6 - 7'), ('slot9', '7 - 8'), ('slot10', '8 - 9')],
        required=True)

    @api.constrains('appointment_time')
    def check_slot(self):
        for record in self:
            rec = self.env['hospital.appointment'].search(
                [('doctor_assigned', '=', record.name.id), ('appointment_date', '=', record.appointment_date),
                 ('appointment_time', '=', record.appointment_time), ('id', '!=', record.id)])

            if rec:
                raise ValidationError("Slot already Booked !")

            elif record.appointment_date < fields.Date.today():
                raise ValidationError("Cannot Book Slot for previous date")

            else:
                vals = {
                    'doctor_assigned': record.name.id,
                    'name': record.patient_name.id,
                    'appointment_date': record.appointment_date,
                    'appointment_time': record.appointment_time
                }
            self.env['hospital.appointment'].create(vals)
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'type': 'success',
                    'message': "New Appointment Booked since this slot was empty",
                    'next': {'type': 'ir.actions.act_window_close'},
                }
            }
