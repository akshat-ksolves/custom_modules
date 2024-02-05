# from odoo import api, fields, models, SUPERUSER_ID, _
# import psycopg2
#
#
# class ContactInherit(models.Model):
#     _inherit = 'res.partner'
#
#     def test_function(self, keys):
#         connection = psycopg2.connect(database="new_db", user="odoo", host='localhost', password="odoo16",
#                                       port=5432)
#         print("Connection Established !")
#         cr = connection.cursor()
#         str1 = ""
#         length = len(self.ids)
#         count = 0
#         # for rec in self:
#
#         query = f"""INSERT INTO res_partner(name,email,phone) VALUES {str1} """
#         print(query)
#         cr.execute(query)
#         connection.commit()
#         cr.close()
#         connection.close()
#         return True
#
#         # cr = connection.cursor()
#         # connection.commit = True
#         # env = api.Environment(cr, SUPERUSER_ID, {})
#         # env['res.partner'].create(self)
#         # connection.commit()
#         # cr.close()
#         # connection.close()
#
# #
# # count += 1
# # name = rec.name
# # email = rec.email
# # phone = rec.phone
# # if length == count:
# #     str1 += f"('{name}','{email}','{phone}')"
# # else:
# #     str1 += f"('{name}','{email}','{phone}'),"