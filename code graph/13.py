""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลอื่นๆ และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function13():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลอื่นๆ และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [844, 0, 0, 10604])
    line_chart.add('ภาคกลาง', [4213, 4882, 6064, 6266])
    line_chart.add('ภาคเหนือ', [4935, 453, 3693, 4300])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [29226, 477, 5948, 6804])
    line_chart.add('ภาคใต้', [323, 0, 5955, 3013])
    line_chart.render_to_file('13.svg')
function13()
