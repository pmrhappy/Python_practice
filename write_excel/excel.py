import xlwt
import xlrd

x=1
y=2
z=3

list1=[2.34,4.346,4.234]

book = xlrd.open_workbook("trial.xls")
#book = xlwt.Workbook(encoding="utf-8")

w1 = book.read(0,0)
#sheet1.write(0, 0, "Display")
#sheet1.write(1, 0, "Dominance")
sheet1.write(2, 0, "kkkkkkkkkkk")
book.save("trial.xls")