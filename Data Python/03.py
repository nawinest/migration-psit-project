""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการต้องการรายได้เพิ่ม และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function3():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[52]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[53], [int(data[54]), int(data[55]), int(data[56]), int(data[57])])
    line_chart.add(data[58], [int(data[59]), int(data[60]), int(data[61]), int(data[62])])
    line_chart.add(data[63], [int(data[64]), int(data[65]), int(data[66]), int(data[67])])
    line_chart.add(data[68], [int(data[69]), int(data[70]), int(data[71]), int(data[72])])
    line_chart.add(data[73], [int(data[74]), int(data[75]), int(data[76]), int(data[77])])
    line_chart.render_to_file('03.svg')
function3()
