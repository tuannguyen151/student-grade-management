from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "student"
    _description = "Student"
    _rec_name = "full_name"

    full_name = fields.Char(string="Họ Và Tên", required=True)
    student_code = fields.Char(string="Mã Sinh Viên", required=True)
    birthday = fields.Date(string="Ngày Sinh")
    address = fields.Text(string="Địa chỉ")

    def action_student_form(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "student",
            "res_id": self.id,
            "name": self.full_name,
            "view_mode": "form",
            "views": [(False, "form")],
        }

    @api.constrains("student_code")
    def _check_unique_student_code(self):
        for student in self:
            if self.search_count([("student_code", "=", student.student_code)]) > 1:
                raise ValidationError("Mã sinh viên đã tồn tại")
