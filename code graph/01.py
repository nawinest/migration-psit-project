""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการหางาน และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function1():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการหางาน และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [31586, 35153, 16495, 27991])
    line_chart.add('ภาคกลาง', [38802, 86029, 85280, 72979])
    line_chart.add('ภาคเหนือ', [5406, 11495, 11907, 5793])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [24406, 18312, 22073, 7093])
    line_chart.add('ภาคใต้', [7838, (11455+10479), 27858, 16041])
    line_chart.render_to_file('01.svg')
function1()

