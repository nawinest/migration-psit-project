""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการกลับภูมิลำเนา และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function7():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[156]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[157], [int(data[158]), int(data[159]), int(data[160]), int(data[161])])
    line_chart.add(data[162], [int(data[163]), int(data[164]), int(data[165]), int(data[166])])
    line_chart.add(data[167], [int(data[168]), int(data[169]), int(data[170]), int(data[171])])
    line_chart.add(data[172], [int(data[173]), int(data[174]), int(data[175]), int(data[176])])
    line_chart.add(data[177], [int(data[178]), int(data[179]), int(data[180]), int(data[181])])
    line_chart.render_to_file('07.svg')
function7()
