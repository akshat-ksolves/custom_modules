from odoo import api, fields, models


class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'

    wizard_id = fields.Many2one('project.task', string="Task ID", readonly=True,
                                default=lambda self: self.env.context.get('active_id'))
    sale_order_detail_ids = fields.Many2many('sale.order', string="Sale Order Details")
    total_sales_order = fields.Float(string="Total Sales:",readonly=True)

    def save_wiz_data(self):
        for rec in self.sale_order_detail_ids:
            rec.task_id = self.wizard_id

