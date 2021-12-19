import datetime

def total_time(fast_rut_obj):
    total_secs = sum(x.time_taken for x in fast_rut_obj[1:])
    print('\n\n')
    print(total_secs)
    conversion = datetime.timedelta(seconds=total_secs)
    converted_time = str(conversion)
    print('\n\n__Total Delivery Time__\n', converted_time)