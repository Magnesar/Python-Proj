
def add_time(st,dur,day = ""):
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    fancy_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    tim = st.split()[0]
    tim1_h = int(tim.split(':')[0])
    tim1_m = int(tim.split(':')[1])
    dur_h = int(dur.split(':')[0])
    dur_m = int(dur.split(':')[1])
    if st[-2:] == "PM":
        #print(tim1_h+12)
        tim1_h = tim1_h + 12
    
    nt_h = tim1_h + dur_h
    nt_m = tim1_m + dur_m

    if nt_m>60:
        ex_h = nt_m//60     #excess hours if min>60
        nt_h = nt_h + ex_h
        nt_m = nt_m - ex_h*60
    if nt_m<10:
        nt_m = '0{}'.format(nt_m)
    ex_d = 0

    if nt_h>=24:
        ex_d = nt_h//24
        #print(ex_d)
        nt_h = nt_h - ex_d*24

    
    if nt_h>=12:
        if nt_h == 12: 
            pass
        else:
            nt_h = nt_h - 12
        m = "PM"
    elif nt_h == 0:
        nt_h = 12
        m = "AM"
    else:
        m = "AM"
    
    if not day :
        if ex_d>=0:
            if ex_d ==0:
              new_time = "{}:{} {}".format(nt_h,nt_m,m)
            elif ex_d == 1:
                new_time = "{}:{} {} (next day)".format(nt_h,nt_m,m)
            else:
                new_time = "{}:{} {} ({} days later)".format(nt_h,nt_m,m,ex_d)
    day = day.lower()
    if day in days:
        n = days.index(day)
        if ex_d == 0:
            day = fancy_days[n]
            new_time = "{}:{} {}, {}".format(nt_h,nt_m,m,day)
        elif ex_d == 1:
            n = n + 1
            if n>6:
              n = n - (n//7)*7
            day = fancy_days[n]
            new_time = "{}:{} {}, {} (next day)".format(nt_h,nt_m,m,day)
        else:
            n = n + ex_d
            if n>6:
              n = n - (n//7)*7
            day = fancy_days[n]
            new_time = "{}:{} {}, {} ({} days later)".format(nt_h,nt_m,m,day,ex_d)
    return new_time
        

    

