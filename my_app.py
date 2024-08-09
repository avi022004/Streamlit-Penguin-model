import streamlit as st
st.title("Display Tittle use st.title()")
st.write("Hello World: Getting Bore, Hello Brother!!")
st.write("To write text use st.write()")
st.header("I love Apple :apple: . This was printed by using st.subheader()")
st.write("Once an :apple: keep in a day doctor run away.")
# To create hyperlink
# To create hyperelink
st.markdown("[Streamlit](https://streamlit.io/) this is markdown using st.markdown()")
st.success("success!!. This text was printed using st.success()")
st.info("Information. This text was printed using st.info()")
st.warning("Warning.This text was printed using st.warning()")
st.error("Error. This text was printed using st.error()")
# image import function
st.title("This is image using import st.image")
from PIL import Image

img = Image.open("pexels-cesarperez209-733745.jpg")
st.image(img, width = 300, caption = "This is a image ")

# Video import function()
st.title("This is video import using st.video()")
video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

# This video was imported using link
st.title("This is youtube video importing st.video using link")
st.video("https://www.youtube.com/watch?v=AzblgZNoBWw")

# Audio file importing function
st.title("This is audio track")
audo_file = open("song.mp3","rb")
audio_bytes = audo_file.read()
st.audio(audio_bytes, format = "audio/mp3")

# Making button
if st.button("Play"):
   st.text("Apple is red in color. It is very healdy fruit")
if st.button("Run"):
    st.subheader("Enjoy music !")
    st.video("https://www.youtube.com/watch?v=hOHKltAiKXQ")

if st.checkbox("Box"):
    st.video("https://www.youtube.com/watch?v=YR12Z8f1Dh8")
 
 #09-08-2024  
   
radio_but = st.radio("Select yuor gender", ["Male", "Female"])
if radio_but == "Male":
	st.info("You are Male")
else:
	st.info("You are Female")    


city = st.sidebar.selectbox("Your City", ["Daman", "Diu", "Valsad"])
st.title("Please first select in sidebar")
if city == "Daman":
     st.info("Daman is looking like mine Goa.")
elif city == "Diu":
     st.info("Diu is neighbour city of Daman")
else:
     st.info("Valsad is poulular city")

occupation = st.sidebar.multiselect("Your Occupation", ["Programmer", "Data Scientist", "ITConsultant", "DBA"])

st.title("Input a number using st.number_input")
age = st.number_input("how old are you",1)

st.title("It will use when we need to write long text")
message =st.text_area("About NIELIT","WRITE SOMETHINGS----")
message =st.text_area("Address","WRITE SOMETHINGS----")

select_val = st.slider("Select a Value", 1, 10)
# starting value = 10.0 ending value = 20.0 increment by =0.5
select_val1 = st.slider("Select a Value", 10.0, 20.0,0.5)
if st.button("Balloons"):
	st.balloons()

import pandas as pd 

auto_data= pd.read_csv("auto.csv")
st.dataframe(auto_data.head())
st.table(auto_data.head(10))

st.title("This is Area Chart Apply using st.arae_chart")
st.area_chart(auto_data[["mpg","cylinders"]])
st.area_chart(auto_data[["mpg","cylinders"]].head(20))

st.title("This is Bar Chart Apply using st.bar_chart")
st.bar_chart(auto_data[["mpg","cylinders"]])
st.bar_chart(auto_data[["mpg","cylinders"]].head(20))

st.title("This is Lione Chart Apply using st.line_chart")
st.line_chart(auto_data[["mpg","cylinders"]])
st.line_chart(auto_data[["mpg","cylinders"]].head(20))

import datetime
import time

st.title("That can show today's date")
today = st.date_input("Today's date is",datetime.datetime.now())
st.title("That can show Time")
hour = st.time_input("The time is",datetime.time(12,30))

st.title("Here are some basic code we use by coyping the code")

import streamlit as st

st.code("import pandas as pd")
st.code("print(Welcome to NIELIT Daman)")

julia_code="""
function doit(num::int)
	println(num)
end
"""
st.code(julia_code,language='julia')

import streamlit as st
import pandas as pd
import numpy as np

st.title ("Line Chart")
df=pd.DataFrame(np.random.randn(40,4),
	columns=["C1","C2","C3","C4"])
st.line_chart(df)

st.title("Area")
df=pd.DataFrame(np.random.randn(40,4),
	columns=["C1","C2","C3","C4"])
st.area_chart(df)



