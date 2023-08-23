import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "student"
    _description = "Student"

    name = fields.Char(string="Họ Và Tên", required=True)
    code = fields.Char(string="Mã Sinh Viên", required=True)
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
            clean_phone = re.sub(r"\D", "", student.phone)

            if not re.match(r"^0[1-9][0-9]{8}$", clean_phone):
                raise ValidationError("Số điện thoại không hợp lệ")
