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
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[0]
    line_chart.add(data[1], [int(data[2]), int(data[3]), int(data[4]), int(data[5])])
    line_chart.add(data[6], [int(data[7]), int(data[8]), int(data[9]), int(data[10])])
    line_chart.add(data[11], [int(data[12]), int(data[13]), int(data[14]), int(data[15])])
    line_chart.add(data[16], [int(data[17]), int(data[18]), int(data[19]), int(data[20])])
    line_chart.add(data[21], [int(data[22]), int(data[23]), int(data[24]), int(data[25])])
    line_chart.render_to_file('01.svg')
    line_chart.x_labels = map(str, range(2554, 2558))
function1()
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
def function6():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[130]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[131], [int(data[132]), int(data[133]), int(data[134]), int(data[135])])
    line_chart.add(data[136], [int(data[137]), int(data[138]), int(data[139]), int(data[140])])
    line_chart.add(data[141], [int(data[142]), int(data[143]), int(data[144]), int(data[145])])
    line_chart.add(data[146], [int(data[147]), int(data[148]), int(data[149]), int(data[150])])
    line_chart.add(data[151], [int(data[152]), int(data[153]), int(data[154]), int(data[155])])
    line_chart.render_to_file('06.svg')
function6()
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
def function8():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[182]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[183], [int(data[184]), int(data[185]), int(data[186]), int(data[187])])
    line_chart.add(data[188], [int(data[189]), int(data[190]), int(data[191]), int(data[192])])
    line_chart.add(data[193], [int(data[194]), int(data[195]), int(data[196]), int(data[197])])
    line_chart.add(data[198], [int(data[199]), int(data[200]), int(data[201]), int(data[202])])
    line_chart.add(data[203], [int(data[204]), int(data[205]), int(data[206]), int(data[207])])
    line_chart.render_to_file('08.svg')
function8()
