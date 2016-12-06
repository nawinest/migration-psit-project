""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการต้องการเปลี่ยนงาน และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function2():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[26]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[27], [int(data[28]), int(data[29]), int(data[30]), int(data[31])])
    line_chart.add(data[32], [int(data[33]), int(data[34]), int(data[35]), int(data[36])])
    line_chart.add(data[37], [int(data[38]), int(data[38]), int(data[40]), int(data[41])])
    line_chart.add(data[42], [int(data[43]), int(data[44]), int(data[45]), int(data[46])])
    line_chart.add(data[47], [int(data[48]), int(data[49]), int(data[50]), int(data[51])])
    line_chart.render_to_file('02.svg')
function2()
