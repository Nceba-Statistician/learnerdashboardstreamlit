import streamlit
import altair 
from plotly import express
from performancedata import records
# streamlit.set_page_config(
    # page_title="learner perfomance", layout="wide", initial_sidebar_state="expanded"
# )
streamlit.header("Dashboard")

def createsidebar(records):
    altair.themes.enable("dark")
    with streamlit.sidebar:
        streamlit.title("Learner Variable Filter")
        Gender_list = list(records.Gender.unique())[::-1]
        ParentalEducation_list = list(records.ParentalEducation.unique())
        ParentalSupport_list = list(records.ParentalSupport.unique())

        select_Gender = streamlit.selectbox("Select a age", Gender_list, index=len(Gender_list)-1)
        select_ParentalEducation = streamlit.selectbox("Select a ParentalEducation", ParentalEducation_list, index=len(ParentalEducation_list)-1)
        select_ParentalSupport = streamlit.selectbox("Select a ParentalSupport", ParentalSupport_list, index=len(ParentalSupport_list)-1)

        # Filter records based on selections

        filtered_records = records[
            (records.Gender == select_Gender) &
            (records.ParentalEducation == select_ParentalEducation) &
            (records.ParentalSupport == select_ParentalSupport)
        ]
        
        return filtered_records
    
filtered_records = createsidebar(records)

def filtering(filtered_records):
    streamlit.write("Overview")
    streamlit.write(filtered_records.reset_index(drop = True))
filtering(filtered_records) 
   
# age_average_gpa.rename(columns={"Age": "AgeGroup", "AverageGPA": "AverageGPA"}, inplace=True)

# Plot with Plotly
def plotly_chart(data):
    fig = express.bar(data, x = data.Age, y = data.AverageGPA, color = data.AverageGPA, text=data.AverageGPA)
    fig.update_layout(title = "Average GPA by Age", width=1000, height=300)
    fig.update_traces(textposition='inside', texttemplate='%{text:.2f}') 
    streamlit.plotly_chart(fig)

plotly_chart(filtered_records)

