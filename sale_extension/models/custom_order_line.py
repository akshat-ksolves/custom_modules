from odoo import api, fields, models

class SaleOrderExtension(models.Model):
    _inherit = "sale.order"

    custom_field = fields.One2many('custom.order.line','order_id',string="Custom Field")
    # connecting_field = fields.Many2one('custom.order.line')
