from odoo import api, fields, models


class DataDisplayWizard(models.TransientModel):
    _name = 'data.display.wizard'

    wizard_id = fields.Many2one('sale.order', string="Product ID")
    wizard_order_line = fields.One2many('custom.order.line.wiz', 'connecting_field')

    def save_data(self):
        sale_id = self.wizard_id
        # self.env['custom.order.line'].unlink()
        lst = []
        for rec in self.wizard_order_line:
            # if rec.name.exists():
            #     continue
            # else:
            # record = self.env['custom.order.line.wiz'].browse(
            #     [('custom_field.name.id', '=', rec.name.id)])
            # if record.exists():
            #     continue
            # else:
            new_field = self.env['custom.order.line'](0, 0,{
                'name': rec.name.id,
                'order_id': rec.order_id,
                'description': rec.description,
                'quantity': rec.quantity,
                'unit_price': rec.unit_price,
                'taxes': rec.taxes,
                'tax_excl': rec.tax_excl
            })
            lst.append(new_field.id)
        sale_id.custom_field.write([(6, 0, lst.ids)])

    @api.model
    def default_get(self, fields):
        res = super(DataDisplayWizard, self).default_get(fields)
        active_id = self._context.get('active_id')
        sale_order_data = self.env['sale.order'].browse(active_id)
        lst = []
        for i in sale_order_data.custom_field:
            line = (0, 0, {
                'name': i.name,
                'order_id': i.order_id,
                'description': i.description,
                'quantity': i.quantity,
                'unit_price': i.unit_price,
                'taxes': i.taxes,
                'tax_excl': i.tax_excl
            })
            lst.append(line)
        res['wizard_order_line'] = lst
        res['wizard_id'] = active_id
        return res


class CustomOrderLineWizard(models.TransientModel):
    _name = 'custom.order.line.wiz'

    name = fields.Many2one('product.template', string="Product")
    order_id = fields.Many2one('custom.order.line', string="Custom Sale Order")
    description = fields.Text(string="Description")
    quantity = fields.Float(string="Quantity")
    unit_price = fields.Float(string="Unit Price")
    taxes = fields.Many2many('account.tax', string="Taxes")
    tax_excl = fields.Char(string="Tax Excl.")
    connecting_field = fields.Many2one('data.display.wizard', string="Dummy Field")
