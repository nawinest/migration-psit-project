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
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[182]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[183], [int(data[184]), int(data[185]), int(data[186]), int(data[187])])
    line_chart.add(data[188], [int(data[189]), int(data[190]), int(data[191]), int(data[192])])
    line_chart.add(data[193], [int(data[194]), int(data[195]), int(data[196]), int(data[197])])
    line_chart.add(data[198], [int(data[199]), int(data[200]), int(data[201]), int(data[202])])
    line_chart.add(data[203], [int(data[204]), int(data[205]), int(data[206]), int(data[207])])
    line_chart.render_to_file('08.svg')
function8()
