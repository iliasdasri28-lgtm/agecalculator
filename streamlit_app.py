import streamlit as st

born = st.text_input("what time have you born:\n")
date = st.text_input("what today date:\n")

if st.button("Calculate"):
    try:
        
        daydate,monthdate,yeardate = date.split("/")
        
        today = int(daydate)
        tomonth = int(monthdate)
        toyear = int(yeardate)
        
        born_day,born_month,born_year=born.split("/")
        
        day = int(born_day)
        month = int(born_month)
        year = int(born_year)
        
        if month > tomonth or (month == tomonth and day > today) : 
            ageyear = toyear - year - 1
            
        else:
            ageyear = toyear - year
            
        if day > today :
            agemonth = (tomonth - month - 1)%12
            ageday = (today + 30) - day
            
        else:
            agemonth = (tomonth - month)%12
            ageday = today - day
            
        st.write(f"your age is {ageyear} year and {agemonth} month and {ageday} day")
    except:
          st.error("enter the date as number in that form: xx/yy/zzzz")
