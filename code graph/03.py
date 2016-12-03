""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการต้องการรายได้เพิ่ม และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function3():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการต้องการรายได้เพิ่ม และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [1146, 3409, 5929, 2528])
    line_chart.add('ภาคกลาง', [4411, 9524, 3286, 7462])
    line_chart.add('ภาคเหนือ', [2326, 5642, 768, 1403])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [5520, 14912, 4245, 5817])
    line_chart.add('ภาคใต้', [2575, 5380, 4907, 1442])
    line_chart.render_to_file('03.svg')
function3()
