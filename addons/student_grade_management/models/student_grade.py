from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentGrade(models.Model):
    _name = "student.grade"
    _description = "Student Grade"
    _rec_name = "student_id"

    _sql_constraints = [
        (
            "check_grade_range",
            "CHECK(grade >= 0 AND grade <= 10)",
            "Điểm phải nằm trong khoảng từ 0 đến 10",
        )
    ]

    student_id = fields.Many2one("student", string="Sinh viên", required=True)
    course_id = fields.Many2one("course", string="Học phần", required=True)
    start_date = fields.Date(string="Ngày bắt đầu", required=True)
    end_date = fields.Date(string="Ngày kết thúc", required=True)
    grade = fields.Float(string="Điểm", required=True)

    @api.constrains("start_date", "end_date", "student_id", "course_id")
    def _check_unique_grade(self):
        for grade in self:
            domain = [
                ("student_id", "=", grade.student_id.id),
                ("course_id", "=", grade.course_id.id),
                ("start_date", "<=", grade.end_date),
                ("end_date", ">=", grade.start_date),
                ("id", "!=", grade.id),
            ]
            if self.search_count(domain) > 0:
                raise ValidationError(
                    "Mỗi sinh viên chỉ được phép có một bản ghi với cùng học phần và cùng khoảng thời gian"
                )
