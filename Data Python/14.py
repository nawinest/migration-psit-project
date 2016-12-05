""" PSIT PROJECT
Subject : 'จำแนกผู้ย้ายถิ่นที่อยู่ก่อนย้ายและที่อยู่ปัจจุบัน'
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import pygal
def function14():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Bar()
    line_chart.title = data[338]
    line_chart.x_labels = map(str, ("ใต้", "ตะวันออกเฉียงเหนือ", "เหนือ", "กลาง", "กรุงเทพมหานคร"))
    line_chart.add(data[339], [float(data[340]), float(data[341]), float(data[342]), float(data[343]), float(data[344])])
    line_chart.add(data[345], [float(data[346]), float(data[347]), float(data[348]), float(data[349]), float(data[350])])
    line_chart.add(data[351], [float(data[352]), float(data[353]), float(data[354]), float(data[355]), float(data[356])])
    line_chart.add(data[357], [float(data[358]), float(data[359]), float(data[360]), float(data[361]), float(data[362])])
    line_chart.add(data[363], [float(data[364]), float(data[365]), float(data[366]), float(data[367]), float(data[368])])
    line_chart.render_to_file('14.svg')
function14()
