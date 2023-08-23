{
    "name": "Quản lý điểm của sinh viên",
    "version": "1.0",
    "author": "Tuan Nguyen - 1041360309",
    "summary": "[HAUI] Quản lý điểm của sinh viên",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_view.xml",
        "views/course_view.xml",
        "views/student_grade_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "student_grade_management/static/src/scss/student_grade_management.scss"
        ]
    },
    "installable": True,
}
