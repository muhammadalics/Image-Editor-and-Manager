import datetime
import image_query
# from datetime import date

# date1 = datetime.date.fromisoformat('2020-10-01')
# date2 = datetime.date.fromisoformat('2020-10-09')
#
# # datetime.timedelta(date1,date2)
#
# num_days=date2-date1
#
# date_list = [date1.isoformat()]
#
# for day in range(num_days.days):
#     date1 = date1 + datetime.timedelta(days=1)
#     image_query.query(date1.isoformat())
#     date_list.append(date1.isoformat())

start_date = '2006-10-19'
end_date = '2006-12-20'

image_query.query(start_date, end_date)