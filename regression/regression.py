import numpy as np
import statsmodels.api as sm
from openpyxl import load_workbook

yCol = 6
xCol = 2
coefAlpha = 0.05
x0 = 40
predAlpha = 0.05

wb = load_workbook(filename = 'data.xlsx')
ws = wb.active

x = []
y = []
for row in range(1, 26):
    cell = ws.cell(column=yCol, row=row).value
    y.append(ws.cell(column=yCol, row=row).value)
    x.append(ws.cell(column=xCol, row=row).value)
x = sm.add_constant(x)

mod = sm.OLS(y, x)
res = mod.fit()
print(f"Parameters are: b0 = {round(res.params[0], 4)}, b1 = {round(res.params[1], 4)}")
print(f"R2 = {round(res.rsquared, 4)}")
confIntervals = res.conf_int(alpha=coefAlpha)
print(f"Conf Intervals ({(1 - coefAlpha) * 100 } %), Beta0: < {round(confIntervals[0][0], 4)}, {round(confIntervals[0][1], 4)} >, Beta1: < {round(confIntervals[1][0], 4)}, {round(confIntervals[1][1], 4)} >")

predAvarege = res.get_prediction(exog=[1, x0]).conf_int(alpha=predAlpha)
print(f"Average Conf Intervals for x = {x0} ({(1 - predAlpha) * 100 } %): < {round(predAvarege[0][0], 4)}, {round(predAvarege[0][1], 4)} > ")
predObserved = res.get_prediction(exog=[1, x0]).conf_int(obs=True, alpha=predAlpha)
print(f"Observed Conf Intervals for x = {x0} ({(1 - predAlpha) * 100 } %): < {round(predObserved[0][0], 4)}, {round(predObserved[0][1], 4)} > ")