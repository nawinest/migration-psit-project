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
def function9():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[208]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[209], [int(data[210]), int(data[211]), int(data[212]), int(data[213])])
    line_chart.add(data[214], [int(data[215]), int(data[216]), int(data[217]), int(data[218])])
    line_chart.add(data[219], [int(data[220]), int(data[221]), int(data[222]), int(data[223])])
    line_chart.add(data[224], [int(data[225]), int(data[226]), int(data[227]), int(data[228])])
    line_chart.add(data[229], [int(data[230]), int(data[231]), int(data[232]), int(data[233])])
    line_chart.render_to_file('09.svg')
function9()
def function10():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[234]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[235], [int(data[236]), int(data[237]), int(data[238]), int(data[239])])
    line_chart.add(data[240], [int(data[241]), int(data[242]), int(data[243]), int(data[244])])
    line_chart.add(data[245], [int(data[246]), int(data[247]), int(data[248]), int(data[249])])
    line_chart.add(data[250], [int(data[251]), int(data[252]), int(data[253]), int(data[254])])
    line_chart.add(data[255], [int(data[256]), int(data[257]), int(data[258]), int(data[259])])
    line_chart.render_to_file('10.svg')
function10()
def function11():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[260]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[261], [int(data[262]), int(data[263]), int(data[264]), int(data[265])])
    line_chart.add(data[266], [int(data[267]), int(data[268]), int(data[269]), int(data[270])])
    line_chart.add(data[271], [int(data[272]), int(data[273]), int(data[274]), int(data[275])])
    line_chart.add(data[276], [int(data[277]), int(data[278]), int(data[279]), int(data[280])])
    line_chart.add(data[281], [int(data[282]), int(data[283]), int(data[284]), int(data[285])])
    line_chart.render_to_file('11.svg')
function11()
def function12():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[286]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[287], [int(data[288]), int(data[289]), int(data[290]), int(data[291])])
    line_chart.add(data[292], [int(data[293]), int(data[294]), int(data[295]), int(data[296])])
    line_chart.add(data[297], [int(data[298]), int(data[299]), int(data[300]), int(data[301])])
    line_chart.add(data[302], [int(data[303]), int(data[304]), int(data[305]), int(data[306])])
    line_chart.add(data[307], [int(data[308]), int(data[309]), int(data[310]), int(data[311])])
    line_chart.render_to_file('12.svg')
function12()
def function13():
    """Show graph that calculated of subject"""
    with open('data.txt', 'r') as file:
        read_data = file.read()
    data = read_data.split()
    line_chart = pygal.Line()
    line_chart.title = data[312]
    line_chart.x_labels = map(str, range(2554, 2558))
    line_chart.add(data[313], [int(data[314]), int(data[315]), int(data[316]), int(data[317])])
    line_chart.add(data[318], [int(data[319]), int(data[320]), int(data[321]), int(data[322])])
    line_chart.add(data[323], [int(data[324]), int(data[325]), int(data[326]), int(data[327])])
    line_chart.add(data[328], [int(data[329]), int(data[330]), int(data[331]), int(data[332])])
    line_chart.add(data[333], [int(data[334]), int(data[335]), int(data[336]), int(data[337])])
    line_chart.render_to_file('13.svg')
function13()
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
