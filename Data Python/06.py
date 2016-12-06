""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการย้ายที่อยู่อาศัย และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function6():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[130]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[131], [int(data[132]), int(data[133]), int(data[134]), int(data[135])])
    line_chart.add(data[136], [int(data[137]), int(data[138]), int(data[139]), int(data[140])])
    line_chart.add(data[141], [int(data[142]), int(data[143]), int(data[144]), int(data[145])])
    line_chart.add(data[146], [int(data[147]), int(data[148]), int(data[149]), int(data[150])])
    line_chart.add(data[151], [int(data[152]), int(data[153]), int(data[154]), int(data[155])])
    line_chart.render_to_file('06.svg')
function6()
