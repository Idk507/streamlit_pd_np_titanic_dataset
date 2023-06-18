import streamlit as st
import pandas as pd
import plotly.express as px
import time

# session_state variable 
if "showData" not in st.session_state:
    st.session_state['showData'] = False 

if "bgchange" not in st.session_state:
    st.session_state['bgchange'] = False 


filename = "./Titanic-Dataset.csv"


# Content Render funciton
def embarkcontent():
    if st.session_state['showData']  :
        st.divider()  # 👈 Draws a horizontal rule
        st.title("Embarked")
        embarkedChart(getData())

def sexColumncontent():
    if st.session_state['showData'] :
        st.divider()  # 👈 Draws a horizontal rule
        st.title("Sex")
        sexChart(getData())

def rendershowData():
    if st.session_state['showData'] :
        st.subheader('Data')
        st.write(getData().head(10)) 





@st.cache_resource
def getData(file= filename):
    data = pd.read_csv(file)
    return data 



@st.cache_resource
def embarkedChart(data):
    # # 
    data_c = data.copy()  
    # print(data_c.head(10))
    df = data_c['Embarked'].value_counts().to_frame(name='Count').reset_index()  
    # print(df,type(df))
    fig = px.pie(df,values='Count',names="Embarked")
    st.plotly_chart(fig) 


@st.cache_resource
def sexChart(data):
    data_c = data.copy() 
    df = data_c['Sex'].value_counts().to_frame(name='Count').reset_index()
    # print(df)
    fig = px.bar(df,x ='Sex',y = 'Count',color ='Sex')
    st.plotly_chart(fig) 




# url = "https://images.unsplash.com/photo-1501426026826-31c667bdf23d"
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url({});
background-size: 100%;
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;

}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""


# # st.set_page_config(page_title="Titanic") 



   
 

# heading container
with st.container():
    col1, col2 = st.columns([9, 3])
    with col1:
        st.title("Titanic Data set") 
        # st.write(st.session_state['showData'])
        # st.write(st.session_state['bgchange'])
    with col2 :
        imageurl = st.text_input('Change background image',placeholder="url for image") 
        if len(imageurl)>0:
            with st.spinner(text='In progress'):
                st.session_state['bgchange'] = True
                time.sleep(1)
                st.markdown(page_bg_img.format(imageurl), unsafe_allow_html=True)
                # st.success('Done')  
        else:
            # e = RuntimeError('enter correct url')
            # st.exception(e)
            pass 
            # st.session_state['showData'] = st.session_state['showData']
   



### first conatainer s
with st.container():
    # to show dataset
   
    button_show_data = st.button(label="Show data")
    if button_show_data:
        with st.spinner(text='In progress'):
            st.session_state['showData'] = not  st.session_state['showData']
            time.sleep(1)
            rendershowData()  
    else:
        st.session_state['showData'] = st.session_state['showData']   
    # #     st.write("To generate data click on showdata ")
    


 

# Embark Column content 
with st.container():
    embarkcontent()
   
    
# Sex Column content   
with st.container():
    sexColumncontent()
   




