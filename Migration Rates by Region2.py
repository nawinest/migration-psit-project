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
    pie_chart.title = "อัตราการย้ายถิ่นฐาน"
    pie_chart.add("ทั่วราชอาณาจักร",1.4)
    pie_chart.add("กรุงเทพ",0.7)
    pie_chart.add("กลาง",1.8)
    pie_chart.add("เหนือ",1.4)
    pie_chart.add("ใต้",1.2)
    pie_chart.add("ตะวันออก",1.6)
    pie_chart.render_to_file("Migration Rates by Region2.svg")
function1()
