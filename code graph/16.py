""" PSIT PROJECT
Subject : 'จำนวนของผู้ย้ายถิ่นจำแนกตามภาคที่อยู่'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function16():
    """Show graph that calculated of subject"""
    pie_chart = pygal.Pie(print_values=True, value_formatter=lambda x: '{}'.format(x))
    pie_chart.title = 'จำนวนของผู้ย้ายถิ่นจำแนกตามภาคที่อยู่'
    pie_chart.add('ภาคกลาง', 26.55)
    pie_chart.add('กรุงเทพมหานคร', 5.49)
    pie_chart.add('ภาคเหนือ', 15.94)
    pie_chart.add('ภาคตะวันออกเฉียงเหนือ', 40.18)
    pie_chart.add('ภาคใต้', 11.84)
    pie_chart.render_to_file('16.svg')
function16()
