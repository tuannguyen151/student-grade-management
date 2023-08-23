import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "student"
    _description = "Student"
    _rec_name = "code"

    name = fields.Char(string="Họ Và Tên", required=True)
    code = fields.Char(string="Mã Sinh Viên", required=True)
    avatar = fields.Image(string="Ảnh đại diện")
    birthday = fields.Date(string="Ngày Sinh")
    phone = fields.Char(string="Số điện thoại")
    address = fields.Char(string="Địa chỉ")
    student_grade_ids = fields.One2many("student.grade", "student_id", string="Điểm")

    @api.constrains("code")
    def _check_unique_code(self):
        for student in self:
            if self.search_count([("code", "=", student.code)]) > 1:
                raise ValidationError("Mã sinh viên đã tồn tại")

    @api.constrains("phone")
    def _check_valid_phone(self):
        for student in self:
            if student.phone and not re.match(r"^0[1-9][0-9]{8}$", str(student.phone)):
                raise ValidationError("Số điện thoại không hợp lệ")

    def action_generate_student_report(self):
        return self.env.ref(
            "student_grade_management.action_report_student"
        ).report_action(self)
