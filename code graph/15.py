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
    line_chart = pygal.HorizontalBar(print_values=True, value_formatter=lambda x: '{}'.format(x))
    line_chart.title = 'ร้อยละของผู้ย้ายถิ่น จำแนกตามสาเหตุของการย้ายถิ่่นฐาน'
    line_chart.add('หางานทำ', 15.8)
    line_chart.add('ต้องการเปลี่ยนงาน', 3.8)
    line_chart.add('ต้องการรายได้เพิ่มขึ้น', 2.0)
    line_chart.add('หน้าที่การงาน', 13.7)
    line_chart.add('ศึกษาต่อ', 7.9)
    line_chart.add('ย้ายที่อยู่อาศัย', 10.7)
    line_chart.add('กลับภูมิลำเนา', 3.2)
    line_chart.add('ติดตามคนในครอบครัว', 19.6)
    line_chart.add('ทำกิจกรรมครอบครัว', 14.9)
    line_chart.add('รักษาตัว', 0.9)
    line_chart.add('ขาดคนดูแล', 2.8)
    line_chart.add('เพื่อดูแลคนอื่น', 1.8)
    line_chart.add('อื่นๆ', 2.9)
    line_chart.render_to_file('15.svg')
function15()
