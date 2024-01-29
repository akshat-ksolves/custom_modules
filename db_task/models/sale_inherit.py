# import contextlib
# from odoo import api, fields, models, sql_db, SUPERUSER_ID
#
#
# class SaleOrderInherit(models.Model):
#     _inherit = 'sale.order'
#
#     #
#
#     def create(self, vals):
#         super_call = super(SaleOrderInherit, self).create(vals)
#         new_db = sql_db.db_connect('new_db')
#         with contextlib.closing(new_db.cursor()) as cr:
#             cr._cnx.commit = True
#             env = api.Environment(cr, SUPERUSER_ID, {})
#             lst = list(filter(lambda i: (i[1] != []), vals.items()))
#             # for rec in lst:
#             #     query = """INSERT INTO sale_order ({rec1}) VALUES ({rec2})""".format(rec1=rec[0],rec2=rec[1])
#             # query = f"""INSERT INTO sale_order(partner_id) VALUES('{vals['partner_id']}') """
#             # cr.execute(query)
#             data = cr.dictfetchall()
#             print(data)
#
#         return super_call

#
#
#         # rec_keys = ','.join(vals.keys())
#         # rec_values = ','.join(map(str,vals.values()))
#
#         # cursor = new_db.cursor()
#         # env = api.Environment(cr, SUPERUSER_ID, {})
#         # sale_order = env['sale.order'].create(vals)
