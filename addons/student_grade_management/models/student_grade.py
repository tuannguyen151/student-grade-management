from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentGrade(models.Model):
    _name = "student.grade"
    _description = "Student Grade"
    _rec_name = "student_id"

    student_id = fields.Many2one("student", string="Học sinh", required=True)
    course_id = fields.Many2one("course", string="Học phần", required=True)
    grade = fields.Float(string="Điểm", required=True)

    @api.constrains("grade")
    def _check_valid_grade(self):
        for record in self:
            if not 0 <= record.grade <= 10:
                raise ValidationError("Điểm phải nằm trong khoảng từ 0 đến 10")

    @api.constrains("student_id", "course_id")
    def _check_unique_student_course(self):
        for record in self:
            domain = [
                ("student_id", "=", record.student_id.id),
                ("course_id", "=", record.course_id.id),
            ]
            if self.search_count(domain) > 1:
                raise ValidationError(
                    "Mỗi học sinh chỉ được phép có một bản ghi với cùng học phần."
                )
