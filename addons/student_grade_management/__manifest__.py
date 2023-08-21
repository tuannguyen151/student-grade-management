{
    "name": "Quản lý điểm của sinh viên",
    "version": "1.0",
    "author": "Tuan Nguyen - 1041360309",
    "summary": "[HAUI] Quản lý điểm của sinh viên",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_view.xml",
        "views/student_grade_view.xml",
        "views/course_view.xml",
        "report/report_student_template.xml",
    ],
    "installable": True,
}
