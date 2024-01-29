from odoo import api, fields, models, _


class InheritSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hide_records = fields.Boolean(string="Hide Records", store=True)


    def set_values(self):
        super(InheritSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('xyz', self.hide_records)

    @api.model
    def get_values(self):
        res = super(InheritSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            hide_records=params.get_param('xyz'))
        return res