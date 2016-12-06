""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในหน้าที่การงาน และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function4():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[78]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[79], [int(data[80]), int(data[81]), int(data[82]), int(data[83])])
    line_chart.add(data[84], [int(data[85]), int(data[86]), int(data[87]), int(data[88])])
    line_chart.add(data[89], [int(data[90]), int(data[91]), int(data[92]), int(data[93])])
    line_chart.add(data[94], [int(data[95]), int(data[96]), int(data[97]), int(data[98])])
    line_chart.add(data[99], [int(data[100]), int(data[101]), int(data[102]), int(data[103])])
    line_chart.render_to_file('04.svg')
function4()
