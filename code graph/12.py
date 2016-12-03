""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการเพื่อดูแลคนอื่น และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function12():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการเพื่อดูแลคนอื่น และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 1923, 1804, 722])
    line_chart.add('ภาคกลาง', [5833, 2880, 6028, 5237])
    line_chart.add('ภาคเหนือ', [12092, 6602, 9937, 7126])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [23580, 26836, 19357, 10452])
    line_chart.add('ภาคใต้', [1508, 6185, 5238, 689])
    line_chart.render_to_file('12.svg')
function12()
