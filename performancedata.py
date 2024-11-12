import pyodbc
import pandas
import warnings
warnings.filterwarnings("ignore")

# 
def extractrecords():
    conn = pyodbc.connect("driver={ODBC Driver 18 for SQL Server};server=192.168.0.178;database=LearnerPerformanceDB;uid=demouser;pwd=roots;TrustServerCertificate=yes")
    performancevalues = pandas.read_sql_query("select * from Student_performance_api", conn)
    performancevalues["Gender"] = performancevalues["Gender"].map({1: "Male", 0: "Female"})
    performancevalues["ParentalEducation"] = performancevalues["ParentalEducation"].map({0: "None", 1: "Poor", 2: "Below Average", 3: "Satisfactory", 4: "Excellent"})
    performancevalues["ParentalSupport"] = performancevalues["ParentalSupport"].map({0: "None", 1: "Poor", 2: "Below Average", 3: "Satisfactory", 4: "Excellent"})
    performancevalues["Sports"] = performancevalues["Sports"].map({1: "Yes", 0: "No"})
    performancevalues["Music"] = performancevalues["Music"].map({1: "Yes", 0: "No"})
    aggregatedperformancevalues = performancevalues.groupby(
        ["Age", "Gender", "ParentalEducation", "ParentalSupport"] 
    ).agg(
        AverageGPA=("GPA", "mean"),
        AverageAbsences=("Absences", "mean"),
        AverageStudyTimeWeekly=("StudyTimeWeekly", "mean")
    ).reset_index()
    return aggregatedperformancevalues
 
records = extractrecords()



