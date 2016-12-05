""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการขาดคนดูแลและภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function11():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[260]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[261], [int(data[262]), int(data[263]), int(data[264]), int(data[265])])
    line_chart.add(data[266], [int(data[267]), int(data[268]), int(data[269]), int(data[270])])
    line_chart.add(data[271], [int(data[272]), int(data[273]), int(data[274]), int(data[275])])
    line_chart.add(data[276], [int(data[277]), int(data[278]), int(data[279]), int(data[280])])
    line_chart.add(data[281], [int(data[282]), int(data[283]), int(data[284]), int(data[285])])
    line_chart.render_to_file('11.svg')
function11()
