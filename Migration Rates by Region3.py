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
    pie_chart.title = "อัตราการย้ายถิ่นฐาน จำแนกตามอายุ"
    pie_chart.add("60 ขึ้นไป",0.2)
    pie_chart.add("35-59",0.9)
    pie_chart.add("25-34",2.7)
    pie_chart.add("15-24",3.2)
    pie_chart.add("0-14",1.0)
    pie_chart.render_to_file("Migration Rates by Region3.svg")
function1()
