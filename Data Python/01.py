""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการหางาน และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function1():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[0]
    line_chart.add(data[1], [int(data[2]), int(data[3]), int(data[4]), int(data[5])])
    line_chart.add(data[6], [int(data[7]), int(data[8]), int(data[9]), int(data[10])])
    line_chart.add(data[11], [int(data[12]), int(data[13]), int(data[14]), int(data[15])])
    line_chart.add(data[16], [int(data[17]), int(data[18]), int(data[19]), int(data[20])])
    line_chart.add(data[21], [int(data[22]), int(data[23]), int(data[24]), int(data[25])])
    line_chart.render_to_file('01.svg')
    line_chart.x_labels = map(str, range(2554, 2558))
function1()

