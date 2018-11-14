# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 00:59:36 2018

@author: AMARESH
"""

import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope= ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials= ServiceAccountCredentials.from_json_keyfile_name('SpreadSheetExample-7141178631f1.json',scope)

gc = gspread.authorize(credentials)

wks = gc.open('SpreadsheetApi').sheet1

print(wks.get_all_records())

#Adding new rows
wks.append_row(["This is 1st col","This is 2nd Col"])

print(wks.get_all_records())

wks.delete_row(2)

print(wks.get_all_records())

wks.acell()

wks.findall()
wks.update_cell()

#For finding and replacing values:
for cell in wks.findall('data'):
    cell.value = 'new data'