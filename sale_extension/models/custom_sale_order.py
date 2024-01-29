from odoo import api, fields, models

class CustomOrderLine(models.Model):

    _name = 'custom.order.line'
    _description = 'Custom Order Line'

    name = fields.Many2one('product.template', string="Product")
    order_id = fields.Many2one('sale.order', string="Custom Sale Order")
    description = fields.Text(string="Description")
    quantity = fields.Float(string="Quantity")
    unit_price = fields.Float(string="Unit Price")
    taxes = fields.Many2many('account.tax', string="Taxes")
    tax_excl = fields.Char(string="Tax Excl.")

    # def save_data_wiz(self, fields):
    #     res = super(CustomOrderLine, self).default_get(fields)
    #     lst = []
    #     sale_order_data = self.env['sale.order'].browse('active_id')
    #     for i in sale_order_data.wizard_order_line:
    #         line = (0, 0, {
    #             'name': i.name,
    #             'order_id': i.order_id,
    #             'description': i.description,
    #             'quantity': i.quantity,
    #             'unit_price': i.unit_price,
    #             'taxes': i.taxes,
    #             'tax_excl': i.tax_excl
    #         })
    #         lst.append(line)
    #         return line


# res = super(CustomOrderLine, self).default_get(fields)
# active_id = self._context.get('active_id')
# sale_order_data = self.env['sale.order'].browse(active_id)
# lst = []
# for i in sale_order_data.wizard_order_line:
#     line = (0, 0, {
#         'name': i.name,
#         'order_id': i.order_id,
#         'description': i.description,
#         'quantity': i.quantity,
#         'unit_price': i.unit_price,
#         'taxes': i.taxes,
#         'tax_excl': i.tax_excl
#     })
#     lst.append(line)
# res['custom_field'] = lst
# res['wizard_id'] = active_id
# return res
