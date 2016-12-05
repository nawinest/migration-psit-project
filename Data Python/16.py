""" PSIT PROJECT
Subject : 'จำนวนของผู้ย้ายถิ่นจำแนกตามภาคที่อยู่'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function16():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    pie_chart = pygal.Pie(print_values=True, value_formatter=lambda x: '{}'.format(x))
    pie_chart.title = data[396]
    pie_chart.add(data[397], float(data[398]))
    pie_chart.add(data[399], float(data[400]))
    pie_chart.add(data[401], float(data[402]))
    pie_chart.add(data[403], float(data[404]))
    pie_chart.add(data[405], float(data[406]))
    pie_chart.render_to_file('16.svg')
function16()
