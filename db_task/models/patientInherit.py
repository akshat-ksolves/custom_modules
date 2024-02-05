from odoo import api, fields, models, SUPERUSER_ID
import psycopg2
import pyodbc


class PatientInherit(models.Model):
    _inherit = "hospital.patient"


    # CREATE DATA using PSYCOPG2
    def create(self, vals):
        super_call = super(PatientInherit, self).create(vals)
        connection = psycopg2.connect(database="new_db", user="odoo", host='localhost', password="odoo16", port=5432)

        print("Connection Established !")
        # connection.autocommit = True
        cr = connection.cursor()
        # lst = list(filter(lambda i: (i[1] != []), vals.items()))
        # for rec in lst:
        #     query = """INSERT INTO hospital_patient ({rec1}) VALUES ({rec2})""".format(rec1=rec[0], rec2=rec[1])
        query = f"""INSERT INTO hospital_patient (patient_name, age, notes) VALUES ('{vals['patient_name']}', '{vals['age']}','{vals['notes']}')"""
        cr.execute(query)
        connection.commit()
        cr.close()
        connection.close()
        return super_call

    # DELETE DATA using PSYCOPG2
    @api.model
    def delete_records(self, vals):
        connection = psycopg2.connect(database="new_db", user="odoo", host='localhost', password="odoo16", port=5432)
        print("Connection Established !")
        # connection.autocommit = True
        cr = connection.cursor()
        query = f"""DELETE FROM hospital_patient WHERE patient_name={vals['patient_name']}"""
        cr.execute(query)
        connection.commit()
        cr.close()
        connection.close()

    # SELECT DATA using PSYCOPG2
    def select_records(self, vals):

        connection = psycopg2.connect(database="new_db", user="odoo", host='localhost', password="odoo16", port=5432)
        print("Connection Established !")
        cr = connection.cursor()
        query = f"""SELECT * FROM hospital_patient"""
        cr.execute(query)
        connection.commit()
        data = cr.fetchall()
        print(data)
        cr.close()
        connection.close()


    # SELECT DATA using PYODBC Method
    # def select_records(self):
    #     user = "odoo"
    #     password = "odoo16"
    #     database = "new_db"
    #     host = "localhost"
    #
    #     connection_string = f"DRIVER={{PostgreSQL ANSI}};SERVER={host};DATABASE={database};UID={user};PWD={password}"
    #     conn = pyodbc.connect(connection_string)
    #     cursor = conn.cursor()
    #     cursor.execute('SELECT * FROM hospital_patient')
    #     rows = cursor.fetchall()
    #     for row in rows:
    #         print(row)
    #     cursor.close()
    #     conn.close()
