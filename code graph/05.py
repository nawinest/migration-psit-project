""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการศึกษาต่อ และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function5():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการศึกษาต่อ และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [4780, 10636, 4000, 13890])
    line_chart.add('ภาคกลาง', [9327, 17487, 9460, 8084])
    line_chart.add('ภาคเหนือ', [11032, 17284, 19477, 8001])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [18514, 38597, 29323, 19633])
    line_chart.add('ภาคใต้', [4772, 5869, 4203, 8986])
    line_chart.render_to_file('05.svg')
function5()
