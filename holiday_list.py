# -*- coding: utf-8 -*- 
import datetime
import jholiday
import sys
# ---------------------------------------------------------------------------
# 目的：特定の日付から今日までの中で、土日祝日を含む休日が何日でいつなのか調べる（リスト作成）
# ---------------------------------------------------------------------------

def holiday_list(y,m,d):
	# 今日
	today = datetime.date.today()
	# 開始日
	start_date = datetime.date(y,m,d)
	
	# 日数の計算
	date_count = today - start_date
	
	# 休日判別処理
	li = []
	day = start_date
	count_holiday = 0
	count_sun_stu = 0
	while today > day:
		date_y = int(day.strftime('%Y'))
		date_m = int(day.strftime('%m'))
		date_d = int(day.strftime('%d'))
		date_str = day.strftime('%Y%m%d')
		# print jholiday.holiday_name(date_y,date_m,date_d)
		if jholiday.holiday_name(date_y,date_m,date_d):
			li.append(date_str)
			count_holiday += 1
		elif day.weekday() == 5 and 6:
			li.append(date_str)
			count_sun_stu += 1
		day = day + datetime.timedelta(1)
	
	#print li
	print ("day: %s" % date_count)
	print ("holiday: %s" % count_holiday)
	print ("sun_stu: %s" % count_sun_stu)
	
	return li

# 休日のリスト出力
print (holiday_list(2007,1,1))