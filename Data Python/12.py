""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการเพื่อดูแลคนอื่น และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function12():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[286]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[287], [int(data[288]), int(data[289]), int(data[290]), int(data[291])])
    line_chart.add(data[292], [int(data[293]), int(data[294]), int(data[295]), int(data[296])])
    line_chart.add(data[297], [int(data[298]), int(data[299]), int(data[300]), int(data[301])])
    line_chart.add(data[302], [int(data[303]), int(data[304]), int(data[305]), int(data[306])])
    line_chart.add(data[307], [int(data[308]), int(data[309]), int(data[310]), int(data[311])])
    line_chart.render_to_file('12.svg')
function12()
