""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการกลับภูมิลำเนา และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function7():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการกลับภูมิลำเนา และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 0, 274, 0])
    line_chart.add('ภาคกลาง', [10370, 13464, 22257, 5542])
    line_chart.add('ภาคเหนือ', [43324, 48520, 59615, 33980])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [204607, 281300, 205877, 94577])
    line_chart.add('ภาคใต้', [13946, 11070, 28228, 10980])
    line_chart.render_to_file('07.svg')
function7()
