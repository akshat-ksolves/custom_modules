from odoo import api, fields, models


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    task_id = fields.Many2one('project.task', string="Tasks Assigned")

    @api.model
    def create(self, vals):
        if self.date_order.time < fields.datetime.now():
            opportunity = self.env['crm.lead'].create({
                'name': vals.get('name', ''),
                'partner_id': vals.get('partner_id', False),
            })
            vals['opportunity_id'] = opportunity.id
        quotation = super(SaleOrderInherit, self).create(vals)
        return quotation
