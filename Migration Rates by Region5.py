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
    pie_chart.title = "อัตราการย้ายถิ่นฐาน ตามสถานภาพสมรส"
    pie_chart.add("สมรส",56.5)
    pie_chart.add("ม่าย",2.7)
    pie_chart.add("หย่า",1.9)
    pie_chart.add("แยกกันอยู่",2.3)
    pie_chart.add("เคยสมรสแต่ไมม่ทราบสถานภาพ",0.1)
    pie_chart.add("โสด",36.5)
    pie_chart.render_to_file("Migration Rates by Region5.svg")
function1()
