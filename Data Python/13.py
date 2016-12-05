""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลอื่นๆ และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function13():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[312]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[313], [int(data[314]), int(data[315]), int(data[316]), int(data[317])])
    line_chart.add(data[318], [int(data[319]), int(data[320]), int(data[321]), int(data[322])])
    line_chart.add(data[323], [int(data[324]), int(data[325]), int(data[326]), int(data[327])])
    line_chart.add(data[328], [int(data[329]), int(data[330]), int(data[331]), int(data[332])])
    line_chart.add(data[333], [int(data[334]), int(data[335]), int(data[336]), int(data[337])])
    line_chart.render_to_file('13.svg')
function13()
