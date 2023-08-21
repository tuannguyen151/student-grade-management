from odoo import models, fields


class Student(models.Model):
    _name = "student"
    _description = "Student"

    full_name = fields.Char(string="Full Name", required=True)
