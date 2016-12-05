""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการรักษาตัว และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function10():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[234]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[235], [int(data[236]), int(data[237]), int(data[238]), int(data[239])])
    line_chart.add(data[240], [int(data[241]), int(data[242]), int(data[243]), int(data[244])])
    line_chart.add(data[245], [int(data[246]), int(data[247]), int(data[248]), int(data[249])])
    line_chart.add(data[250], [int(data[251]), int(data[252]), int(data[253]), int(data[254])])
    line_chart.add(data[255], [int(data[256]), int(data[257]), int(data[258]), int(data[259])])
    line_chart.render_to_file('10.svg')
function10()
