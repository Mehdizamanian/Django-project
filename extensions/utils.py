from . import jalali

def persian_number_coverter(mystr):
    numbers={
        "1":"۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for e , p in numbers.items():
        mystr=mystr.replace(e, p )
        return mystr

def jconverter (time):

    time_to_str ="{},{},{}".format(time.year , time.month , time.day)
    time_to_touple = jalali.Gregorian(time_to_str).persian_tuple()
    output = "{}/{}/{} | ساعت {}:{} " .format(
    time_to_touple[0],
    time_to_touple[1],
    time_to_touple[2],
    time.hour,
    time.minute,
                )
    return persian_number_coverter(output)














# from . import jalali
#
# def jconverter (time):
#
#     jmonths=["فروردین",  "اردیبهشت", "خرداد", "تیر","مرداد", "شهریور","مهر","ابان","اذر","دی", "بهمن","اسفند",]
#
#     time_to_st="{},{},{}".format(time.year,time.month,time.day)
#     time_to_touple = jalali.Gregorian(time_to_st).persian_tuple()
#
#     time_to_list=list(time_to_touple)
#     for index, month in enumerate(jmonths):
#         if time_to_list[1] == index+1:
#             time_to_list[1] = month
#             break
#
#     output = ",{}{}{}| ساعت ,{}:{} " .format(
#         time_to_list[0],
#         time_to_list[1],
#         time_to_list[2],
#         time.hour,
#         time.minute,
#     )
#     return output
#
