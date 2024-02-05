from odoo import api, fields, models

class CrmInherit(models.Model):

    _inherit = 'crm.lead'

    def display_cancelled_sale_orders(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cancelled Sale Orders',
            'target': 'new',
            'view_mode': 'tree',
            'res_model': 'sale.order',
            'domain': [('state', '=', 'cancel')],
            'context': "{'create': False}"
        }