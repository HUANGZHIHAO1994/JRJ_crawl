import calendar
from calendar import TextCalendar
import time


# print(calendar.month(2018, 11))


class CalStr(TextCalendar):
    def __init__(self, start_year, start_month, end_year, end_month):
        super(CalStr, self).__init__()
        self.start_year = start_year
        self.start_month = start_month
        self.end_year = end_year
        self.end_month = end_month

    def calendarlist(self):
        cal_list = []
        if self.end_year == self.start_year:
            if self.start_month != self.end_month:
                for year in range(self.start_year, self.end_year + 1):
                    for month in range(self.start_month, self.end_month):
                        year_month = time.strftime("%Y%m", time.strptime("{}-{}".format(year, month), "%Y-%m"))
                        all_days = eval(calendar.month(year, month).split()[-1])
                        for day in range(1, all_days + 1):
                            list_tmp = []
                            list_tmp.append(year_month)
                            year_month_day = time.strftime("%Y%m%d",
                                                           time.strptime("{}-{}-{}".format(year, month, day),
                                                                         "%Y-%m-%d"))
                            list_tmp.append(year_month_day)
                            cal_list.append(list_tmp)
            else:
                for year in range(self.start_year, self.end_year + 1):
                    for month in range(self.start_month, self.end_month + 1):
                        year_month = time.strftime("%Y%m", time.strptime("{}-{}".format(year, month), "%Y-%m"))
                        all_days = eval(calendar.month(year, month).split()[-1])
                        for day in range(1, all_days + 1):
                            list_tmp = []
                            list_tmp.append(year_month)
                            year_month_day = time.strftime("%Y%m%d",
                                                           time.strptime("{}-{}-{}".format(year, month, day),
                                                                         "%Y-%m-%d"))
                            list_tmp.append(year_month_day)
                            cal_list.append(list_tmp)

        if self.end_year - self.start_year == 1:
            # start year
            for year in range(self.start_year, self.start_year + 1):
                for month in range(self.start_month, 13):
                    year_month = time.strftime("%Y%m", time.strptime("{}-{}".format(year, month), "%Y-%m"))
                    all_days = eval(calendar.month(year, month).split()[-1])
                    for day in range(1, all_days + 1):
                        list_tmp = []
                        list_tmp.append(year_month)
                        year_month_day = time.strftime("%Y%m%d",
                                                       time.strptime("{}-{}-{}".format(year, month, day), "%Y-%m-%d"))
                        list_tmp.append(year_month_day)
                        cal_list.append(list_tmp)
            # end year
            for year in range(self.end_year, self.end_year + 1):
                for month in range(self.start_month, 13):
                    year_month = time.strftime("%Y%m", time.strptime("{}-{}".format(year, month), "%Y-%m"))
                    all_days = eval(calendar.month(year, month).split()[-1])
                    for day in range(1, all_days + 1):
                        list_tmp = []
                        list_tmp.append(year_month)
                        year_month_day = time.strftime("%Y%m%d",
                                                       time.strptime("{}-{}-{}".format(year, month, day), "%Y-%m-%d"))
                        list_tmp.append(year_month_day)
                        cal_list.append(list_tmp)

        if self.end_year - self.start_year >= 2:
            # start year
            for year in range(self.start_year, self.start_year + 1):
                for month in range(self.start_month, 13):
                    year_month = time.strftime("%Y%m", time.strptime("{}-{}".format(year, month), "%Y-%m"))
                    all_days = eval(calendar.month(year, month).split()[-1])
                    for day in range(1, all_days + 1):
                        list_tmp = []
                        list_tmp.append(year_month)
                        year_month_day = time.strftime("%Y%m%d",
                                                       time.strptime("{}-{}-{}".format(year, month, day), "%Y-%m-%d"))
                        list_tmp.append(year_month_day)
                        cal_list.append(list_tmp)
            # end year
            for year in range(self.end_year, self.end_year + 1):
                for month in range(self.start_month, 13):
                    year_month = time.strftime("%Y%m", time.strptime("{}-{}".format(year, month), "%Y-%m"))
                    all_days = eval(calendar.month(year, month).split()[-1])
                    for day in range(1, all_days + 1):
                        list_tmp = []
                        list_tmp.append(year_month)
                        year_month_day = time.strftime("%Y%m%d",
                                                       time.strptime("{}-{}-{}".format(year, month, day), "%Y-%m-%d"))
                        list_tmp.append(year_month_day)
                        cal_list.append(list_tmp)
            # other years
            for year in range(self.start_year + 1, self.end_year):
                for month in range(1, 13):
                    year_month = time.strftime("%Y%m", time.strptime("{}-{}".format(year, month), "%Y-%m"))
                    all_days = eval(calendar.month(year, month).split()[-1])
                    for day in range(1, all_days + 1):
                        list_tmp = []
                        list_tmp.append(year_month)
                        year_month_day = time.strftime("%Y%m%d",
                                                       time.strptime("{}-{}-{}".format(year, month, day), "%Y-%m-%d"))
                        list_tmp.append(year_month_day)
                        cal_list.append(list_tmp)
        return cal_list


if __name__ == '__main__':
    c = CalStr(2017, 2, 2020, 3)
    print(c.calendarlist())
