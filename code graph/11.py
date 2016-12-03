""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการขาดคนดูแลและภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function11():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการขาดคนดูแลและภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 1543, 1103, 0])
    line_chart.add('ภาคกลาง', [8503, 5189, 6017, 3621])
    line_chart.add('ภาคเหนือ', [6734, 10466, 7904, 6653])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [17908, 15412, 7318, 9975])
    line_chart.add('ภาคใต้', [3232, 2508, 3054, 2778])
    line_chart.render_to_file('11.svg')
function11()
