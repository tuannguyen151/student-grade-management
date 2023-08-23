from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentGrade(models.Model):
    _name = "student.grade"
    _description = "Student Grade"
    _rec_name = "student_id"

    _sql_constraints = [
        (
            "unique_student_course",
            "UNIQUE(student_id, course_id)",
            "Mỗi sinh viên chỉ được phép có một bản ghi với cùng học phần",
        ),
        (
            "check_grade_range",
            "CHECK(grade >= 0 AND grade <= 10)",
            "Điểm phải nằm trong khoảng từ 0 đến 10",
        ),
        (
            "check_start_end_dates",
            "CHECK(start_date <= end_date)",
            "Ngày bắt đầu phải nhỏ hơn hoặc bằng ngày kết thúc",
        ),
    ]

    student_id = fields.Many2one("student", string="Mã sinh viên", required=True)
    course_id = fields.Many2one("course", string="Mã học phần", required=True)
    start_date = fields.Date(string="Ngày bắt đầu")
    end_date = fields.Date(string="Ngày kết thúc")
    grade = fields.Float(string="Điểm", required=True)
