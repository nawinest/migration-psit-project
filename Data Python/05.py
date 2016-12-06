""" PSIT PROJECT
Subject : 'การย้ายถิ่น จำแนกตามเหตุผลในการศึกษาต่อ และภาคที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function5():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[104]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[105], [int(data[106]), int(data[107]), int(data[108]), int(data[109])])
    line_chart.add(data[110], [int(data[111]), int(data[112]), int(data[113]), int(data[114])])
    line_chart.add(data[115], [int(data[116]), int(data[117]), int(data[118]), int(data[119])])
    line_chart.add(data[120], [int(data[121]), int(data[122]), int(data[123]), int(data[124])])
    line_chart.add(data[125], [int(data[126]), int(data[127]), int(data[128]), int(data[129])])
    line_chart.render_to_file('05.svg')
function5()
