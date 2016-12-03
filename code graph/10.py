""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการรักษาตัว และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function10():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการรักษาตัว และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [1522, 0, 0, 0])
    line_chart.add('ภาคกลาง', [461, 492, 1289, 792])
    line_chart.add('ภาคเหนือ', [2528, 321, 2531, 864])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [4360, 14488, 3540, 5216])
    line_chart.add('ภาคใต้', [677, 1261, 529, 147])
    line_chart.render_to_file('10.svg')
function10()
