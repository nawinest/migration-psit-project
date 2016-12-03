""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการต้องการเปลี่ยนงาน และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function2():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการต้องการเปลี่ยนงาน และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [1514, 703, 572, 0])
    line_chart.add('ภาคกลาง', [6716, 16975, 17540, 18179])
    line_chart.add('ภาคเหนือ', [2781, 5551, 6996, 3276])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [8241, 6529, 4586, 11374])
    line_chart.add('ภาคใต้', [3451, 6645, 6593, 3063])
    line_chart.render_to_file('02.svg')
function2()
