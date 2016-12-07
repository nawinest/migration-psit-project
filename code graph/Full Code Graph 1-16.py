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
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการหางาน และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [31586, 35153, 16495, 27991])
    line_chart.add('ภาคกลาง', [38802, 86029, 85280, 72979])
    line_chart.add('ภาคเหนือ', [5406, 11495, 11907, 5793])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [24406, 18312, 22073, 7093])
    line_chart.add('ภาคใต้', [7838, (11455+10479), 27858, 16041])
    line_chart.render_to_file('01.svg')
function1()
def function2():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการต้องการเปลี่ยนงาน และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [1514, 703, 572, 0])
    line_chart.add('ภาคกลาง', [6716, 16975, 17540, 18179])
    line_chart.add('ภาคเหนือ', [2781, 5551, 6996, 3276])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [8241, 6529, 4586, 11374])
    line_chart.add('ภาคใต้', [3451, 6645, 6593, 3063])
    line_chart.render_to_file('02.svg')
function2()
def function3():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการต้องการรายได้เพิ่ม และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [1146, 3409, 5929, 2528])
    line_chart.add('ภาคกลาง', [4411, 9524, 3286, 7462])
    line_chart.add('ภาคเหนือ', [2326, 5642, 768, 1403])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [5520, 14912, 4245, 5817])
    line_chart.add('ภาคใต้', [2575, 5380, 4907, 1442])
    line_chart.render_to_file('03.svg')
function3()
def function4():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในหน้าที่การงาน และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [10954, 5464, 6067, 11428])
    line_chart.add('ภาคกลาง', [5677, 45170, 35637, 47127])
    line_chart.add('ภาคเหนือ', [(8724+8538), 20841, 11548, 8675])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [21038, 46770, 19152, 23975])
    line_chart.add('ภาคใต้', [7205, 14619, 16400, 19851])
    line_chart.render_to_file('04.svg')
function4()
def function5():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการศึกษาต่อ และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [4780, 10636, 4000, 13890])
    line_chart.add('ภาคกลาง', [9327, 17487, 9460, 8084])
    line_chart.add('ภาคเหนือ', [11032, 17284, 19477, 8001])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [18514, 38597, 29323, 19633])
    line_chart.add('ภาคใต้', [4772, 5869, 4203, 8986])
    line_chart.render_to_file('05.svg')
function5()
def function6():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการย้ายที่อยู่อาศัย และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 1930, 348, 2192])
    line_chart.add('ภาคกลาง', [20626, 69375, 50325, 44226])
    line_chart.add('ภาคเหนือ', [6499, 18978, 23844, 12126])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [23940, 24502, 37000, 33612])
    line_chart.add('ภาคใต้', [19976, 25831, 11257, 14450])
    line_chart.render_to_file('06.svg')
function6()
def function7():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการกลับภูมิลำเนา และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 0, 274, 0])
    line_chart.add('ภาคกลาง', [10370, 13464, 22257, 5542])
    line_chart.add('ภาคเหนือ', [43324, 48520, 59615, 33980])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [204607, 281300, 205877, 94577])
    line_chart.add('ภาคใต้', [13946, 11070, 28228, 10980])
    line_chart.render_to_file('07.svg')
function7()
def function8():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการติดตามคนในครอบครัว และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 10960, 5354, 1777])
    line_chart.add('ภาคกลาง', [46326, 80671, 78125, 53207])
    line_chart.add('ภาคเหนือ', [43324, 52942, 54125, 35979])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [103333, 175577, 71704, 62605])
    line_chart.add('ภาคใต้', [19809, 54292, 44003, 37994])
    line_chart.render_to_file('08.svg')
function8()
def function9():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการทำกิจการครอบครัว และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 0, 0, 0])
    line_chart.add('ภาคกลาง', [2220, 3829, 1470, 3018])
    line_chart.add('ภาคเหนือ', [2227, 1537, 2354, 1618])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [23427, 12898, 11820, 4856])
    line_chart.add('ภาคใต้', [1083, 1526, 1482, 1283])
    line_chart.render_to_file('09.svg')
function9()
def function10():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการรักษาตัว และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [1522, 0, 0, 0])
    line_chart.add('ภาคกลาง', [461, 492, 1289, 792])
    line_chart.add('ภาคเหนือ', [2528, 321, 2531, 864])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [4360, 14488, 3540, 5216])
    line_chart.add('ภาคใต้', [677, 1261, 529, 147])
    line_chart.render_to_file('10.svg')
function10()
def function11():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการขาดคนดูแลและภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 1543, 1103, 0])
    line_chart.add('ภาคกลาง', [8503, 5189, 6017, 3621])
    line_chart.add('ภาคเหนือ', [6734, 10466, 7904, 6653])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [17908, 15412, 7318, 9975])
    line_chart.add('ภาคใต้', [3232, 2508, 3054, 2778])
    line_chart.render_to_file('11.svg')
function11()
def function12():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลในการเพื่อดูแลคนอื่น และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [0, 1923, 1804, 722])
    line_chart.add('ภาคกลาง', [5833, 2880, 6028, 5237])
    line_chart.add('ภาคเหนือ', [12092, 6602, 9937, 7126])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [23580, 26836, 19357, 10452])
    line_chart.add('ภาคใต้', [1508, 6185, 5238, 689])
    line_chart.render_to_file('12.svg')
function12()
def function13():
    """Show graph that calculated of subject"""
    line_chart = pygal.Line()
    line_chart.title = 'การย้ายถิ่น จำแนกตามเหตุผลอื่นๆ และภาคที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add('กรุงเทพมหานคร', [844, 0, 0, 10604])
    line_chart.add('ภาคกลาง', [4213, 4882, 6064, 6266])
    line_chart.add('ภาคเหนือ', [4935, 453, 3693, 4300])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [29226, 477, 5948, 6804])
    line_chart.add('ภาคใต้', [323, 0, 5955, 3013])
    line_chart.render_to_file('13.svg')
function13()
def function14():
    """Show graph that calculated of subject"""
    line_chart = pygal.Bar()
    line_chart.title = 'จำแนกผู้ย้ายถิ่นที่อยู่ก่อนย้ายและที่อยู่ปัจจุบัน'
    line_chart.x_labels = map(str, ("ใต้", "ตะวันออกเฉียงเหนือ", "เหนือ", "กลาง", "กรุงเทพมหานคร"))
    line_chart.add('มาจากภาคใต้', [0.5, 8.7, 2.5, 4.1, 5.4])
    line_chart.add('มาจากภาคตะวันออกเฉียงเหนือ',  [4.4, 0.5, 13.7, 36.4, 45.5])
    line_chart.add('มาจากภาคเหนือ',      [4.6, 5.7, 0.5, 23.4, 17.5])
    line_chart.add('มาจากภาคกลาง',  [7.1, 40.8, 22.0, 0.5, 38.3])
    line_chart.add('มาจากกรุงเทพมหานคร',  [4.2, 29.5, 8.6, 13.4, 0.5])
    line_chart.render_to_file('14.svg')
function14()
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
def function16():
    """Show graph that calculated of subject"""
    pie_chart = pygal.Pie(print_values=True, value_formatter=lambda x: '{}'.format(x))
    pie_chart.title = 'จำนวนของผู้ย้ายถิ่นจำแนกตามภาคที่อยู่'
    pie_chart.add('ภาคกลาง', 26.55)
    pie_chart.add('กรุงเทพมหานคร', 5.49)
    pie_chart.add('ภาคเหนือ', 15.94)
    pie_chart.add('ภาคตะวันออกเฉียงเหนือ', 40.18)
    pie_chart.add('ภาคใต้', 11.84)
    pie_chart.render_to_file('16.svg')
function16()
