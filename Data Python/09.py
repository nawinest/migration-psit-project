""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการทำกิจการครอบครัว และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function9():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[208]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[209], [int(data[210]), int(data[211]), int(data[212]), int(data[213])])
    line_chart.add(data[214], [int(data[215]), int(data[216]), int(data[217]), int(data[218])])
    line_chart.add(data[219], [int(data[220]), int(data[221]), int(data[222]), int(data[223])])
    line_chart.add(data[224], [int(data[225]), int(data[226]), int(data[227]), int(data[228])])
    line_chart.add(data[229], [int(data[230]), int(data[231]), int(data[232]), int(data[233])])
    line_chart.render_to_file('09.svg')
function9()
