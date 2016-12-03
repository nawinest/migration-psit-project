""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการติดตามคนในครอบครัว และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function8():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการติดตามคนในครอบครัว และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 10960, 5354, 1777])
    line_chart.add('ภาคกลาง', [46326, 80671, 78125, 53207])
    line_chart.add('ภาคเหนือ', [43324, 52942, 54125, 35979])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [103333, 175577, 71704, 62605])
    line_chart.add('ภาคใต้', [19809, 54292, 44003, 37994])
    line_chart.render_to_file('08.svg')
function8()
