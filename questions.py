import xlrd
import numpy as np
import pandas as pd
import researchpy as rp
from scipy import stats


loc = "responses.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

columns_responder_info = [1, 2, 3]
column_response = 14
for actual_responder_info_column in columns_responder_info:
  data1 = []
  data2 = []
  for row in range(1, 213):
    responder_info = sheet.cell_value(row, actual_responder_info_column)
    if actual_responder_info_column == 2:
      if responder_info <= 21:
        responder_info = '18-21'
      elif responder_info <= 24:
        responder_info = '22-24'
      elif responder_info <= 28:
        responder_info = '25-28'
      elif responder_info <= 33:
        responder_info = '28-33'
      else:
        responder_info = '32-40'
    if actual_responder_info_column == 3:
      if responder_info in ("SŠ s maturitou", "ZŠ"):
        responder_info = "ZŠ/SŠ"
    response = sheet.cell_value(row, column_response)
    append_data = True
    if column_response == 4:
      if 'ano' in response.lower():
        response = 'ano'
      elif 'ne' in response.lower():
        response = 'ne'
    if column_response == 5:
      if response in ("Ne, nesnažím se", "Nevím"):
        append_data = False
    if column_response == 6:
      if response in ("Ne, nerecyklujeme", "Nevím"):
        append_data = False
    if column_response == 13:
      if response == "Nevím":
        append_data = False
    if append_data:
      data1.append(responder_info)
      data2.append(response)
  df = pd.DataFrame(list(zip(data1, data2)), columns =['ResponderInfo', 'Response'])
  crosstab = pd.crosstab(df['ResponderInfo'], df['Response'])
  print(crosstab)
  results = stats.chi2_contingency(crosstab)
  print(results)