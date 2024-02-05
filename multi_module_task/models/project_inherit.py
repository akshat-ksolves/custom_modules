from odoo import api, fields, models


class ProjectInherit(models.Model):
    _inherit = 'project.task'

    sale_order_ids = fields.One2many('sale.order', 'task_id', string="Sale Orders ")

    def get_saleOrders(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Orders',
            'target': 'new',
            'view_mode': 'tree',
            'res_model': 'sale.order',
            'domain': [('task_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def open_wizard_sale_order(self):
        record = self.env['sale.order'].search([('task_id', '=', self.id)])
        sum_total = 0
        for rec in record:
            sum_total += rec.amount_total
        wizard = self.env['sale.order.wizard'].create(
            {
                'wizard_id': self.id,
                'sale_order_detail_ids': record.ids,
                'total_sales_order': sum_total,
            }
        )
        return {
            'name': 'Sale Order Wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'sale.order.wizard',
            'res_id': wizard.id,
            'target': 'new',
        }
