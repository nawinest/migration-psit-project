""" PSIT PROJECT
Subject : Migration of population
made by :
          1. นายกิตติบุญ สัตบุษ    59070016
          2. นายจิรายุส  ไพรวรรณ 59070026
          3. นายธนวรรษ ประดับราช 59070069
          4. นายนาวิน   พูลสวัสดิ์  59070088"""
import os
import uuid
import pygal
from pygal import *
def function1():
    """Get the information to plot a graph Migration Rates by Region"""
    pie_chart = Pie()
    pie_chart.title = "อัตราการย้ายถิ่นฐาน จำแนกการศึกษา"
    pie_chart.add("ไม่มีกรศึกษา",2.6)
    pie_chart.add("ต่ำกว่า ประถมศึกษา",0.5)
    pie_chart.add("ประถมศึกษา",1.3)
    pie_chart.add("มัธยมศึกษาตอนต้น",1.9)
    pie_chart.add("มัธยมศึกษาตอนปลาย",2.3)
    pie_chart.add("อุดมศึกษา",1.7)
    pie_chart.render_to_file("Migration Rates by Region4.svg")
function1()
