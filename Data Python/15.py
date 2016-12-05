""" PSIT PROJECT
Subject : 'ร้อยละของผู้ย้ายถิ่น จำแนกตามสาเหตุของการย้ายถิ่่นฐาน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function15():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.HorizontalBar(print_values=True, value_formatter=lambda x: '{}'.format(x))
    line_chart.title = data[369]
    line_chart.add(data[384], float(data[385]))
    line_chart.add(data[370], float(data[371]))
    line_chart.add(data[386], float(data[387]))
    line_chart.add(data[376], float(data[377]))
    line_chart.add(data[380], float(data[381]))
    line_chart.add(data[378], float(data[379]))
    line_chart.add(data[372], float(data[373]))
    line_chart.add(data[382], float(data[383]))
    line_chart.add(data[394], float(data[395]))
    line_chart.add(data[390], float(data[391]))
    line_chart.add(data[374], float(data[375]))
    line_chart.add(data[392], float(data[393]))
    line_chart.add(data[388], float(data[389]))
    line_chart.render_to_file('15.svg')
function15()
