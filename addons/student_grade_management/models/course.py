from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = "course"
    _description = "Course"

    name = fields.Char(string="Tên học phần", required=True)
    code = fields.Char(string="Mã học phần", required=True)
    description = fields.Text(string="Mô tả")

    @api.constrains("name")
    def _check_unique_name(self):
        for course in self:
            if self.search_count([("name", "=", course.name)]) > 1:
                raise ValidationError("Tên học phần đã tồn tại")

    @api.constrains("code")
    def _check_unique_code(self):
        for course in self:
            if self.search_count([("code", "=", course.code)]) > 1:
                raise ValidationError("Mã học phần đã tồn tại")
