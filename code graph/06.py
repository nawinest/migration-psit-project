""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการย้ายที่อยู่อาศัย และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function6():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการย้ายที่อยู่อาศัย และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 1930, 348, 2192])
    line_chart.add('ภาคกลาง', [20626, 69375, 50325, 44226])
    line_chart.add('ภาคเหนือ', [6499, 18978, 23844, 12126])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [23940, 24502, 37000, 33612])
    line_chart.add('ภาคใต้', [19976, 25831, 11257, 14450])
    line_chart.render_to_file('06.svg')
function6()
