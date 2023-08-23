from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = "course"
    _description = "Course"
    _rec_name = "code"

    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "Tên học phần đã tồn tại"),
        ("unique_code", "UNIQUE(code)", "Mã học phần đã tồn tại"),
        ("positive_credits", "CHECK(credits > 0)", "Số tín chỉ phải lớn hơn 0"),
        ("positive_tuition_fee", "CHECK(tuition_fee > 0)", "Học phí phải lớn hơn 0"),
    ]

    name = fields.Char(string="Tên học phần", required=True)
    code = fields.Char(string="Mã học phần", required=True)
    credits = fields.Integer(string="Số tín chỉ", required=True)
    tuition_fee = fields.Integer(string="Học phí", required=True)
    description = fields.Text(string="Mô tả")
    student_grade_ids = fields.One2many("student.grade", "course_id", string="Điểm")

    def get_low_grades(self, grade_max=5):
        return self.student_grade_ids.filtered(lambda grade: grade.grade < grade_max)

    def get_high_or_equal_grades(self, grade_min=5):
        return self.student_grade_ids.filtered(lambda grade: grade.grade >= grade_min)
