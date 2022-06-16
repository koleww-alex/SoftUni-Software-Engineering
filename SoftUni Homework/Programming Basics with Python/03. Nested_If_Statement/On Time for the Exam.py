exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

total_exam_minutes = (exam_hour * 60) + exam_min
total_arrival_minutes = (arrival_hour * 60) + arrival_min

time_diff = abs(total_exam_minutes - total_arrival_minutes)

if total_arrival_minutes > total_exam_minutes:
    print("Late")
    if time_diff >= 60:
        minutes = total_arrival_minutes - total_exam_minutes
        hours = minutes // 60
        minutes = minutes % 60
        if minutes <= 9:
            print(f"{hours}:{minutes:02d} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
    else:
        minutes = total_arrival_minutes - total_exam_minutes
        print(f"{minutes} minutes after the start")

elif total_arrival_minutes < total_exam_minutes - 30:
    print("Early")
    if time_diff >= 60:
        minutes = total_exam_minutes - total_arrival_minutes
        hours = minutes // 60
        minutes = minutes % 60
        if minutes <= 9:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
    else:
        minutes = total_exam_minutes - total_arrival_minutes
        print(f"{minutes} minutes before the start")

elif total_arrival_minutes == total_exam_minutes:
    print("On time")

else:
    print("On time")
    minutes = total_exam_minutes - total_arrival_minutes
    print(f"{minutes} minutes before the start")
