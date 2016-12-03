""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในหน้าที่การงาน และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088
"""
import pygal
def function4():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในหน้าที่การงาน และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [10954, 5464, 6067, 11428])
    line_chart.add('ภาคกลาง', [5677, 45170, 35637, 47127])
    line_chart.add('ภาคเหนือ', [(8724+8538), 20841, 11548, 8675])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [21038, 46770, 19152, 23975])
    line_chart.add('ภาคใต้', [7205, 14619, 16400, 19851])
    line_chart.render_to_file('04.svg')
function4()
