""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการทำกิจการครอบครัว และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function9():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการทำกิจการครอบครัว และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 0, 0, 0])
    line_chart.add('ภาคกลาง', [2220, 3829, 1470, 3018])
    line_chart.add('ภาคเหนือ', [2227, 1537, 2354, 1618])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [23427, 12898, 11820, 4856])
    line_chart.add('ภาคใต้', [1083, 1526, 1482, 1283])
    line_chart.render_to_file('09.svg')
function9()
