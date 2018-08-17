import pandas as pd
import numpy as np

school_file = "Resources/schools_complete.csv"
student_file = "Resources/students_complete.csv"

school_data = pd.read_csv(school_file)
student_data = pd.read_csv(student_file)

school_student_data = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

#District Summary Calculations
total_schools = school_student_data["school_name"].nunique()
total_students = school_student_data["Student ID"].nunique()
total_budget = (school_student_data["budget"].unique()).sum()

avg_math_score = school_student_data["math_score"].mean()
avg_reading_score = school_student_data["reading_score"].mean()
overall_pass_rate = (avg_math_score + avg_reading_score)/2

pass_math =(school_student_data["math_score"]>=70).value_counts()
pass_math_percent = (pass_math[True]/total_students)*100

pass_read =(school_student_data["reading_score"]>=70).value_counts()
pass_read_percent = (pass_read[True]/total_students)*100

district_summary = pd.DataFrame({"Total Schools":[total_schools], "Total Students":[total_students], "Total Budget":[total_budget], 
                              "Average Math Score":[avg_math_score], "Average Reading Score":[avg_reading_score],
                              "Percent Pass Math":[pass_math_percent], "Percent Pass Reading":[pass_read_percent], "Overall Passing Rate":[overall_pass_rate]})
district_summary

#School Summary
school_group = school_data.groupby(["school_name", "type"])
school_student_group =school_student_data.groupby(["school_name", "type"])

students_per_school = school_student_group["Student ID"].nunique()
budget_per_school = school_group["budget"].sum()
budget_per_student = budget_per_school/students_per_school
avg_math_per_school = school_student_group["math_score"].mean()
avg_read_per_school = school_student_group["reading_score"].mean()
pass_math_per_school = school_student_data[school_student_data["math_score"]>=70].groupby("school_name")["math_score"].count()
math_percent_per_school = (pass_math_per_school/students_per_school)*100
pass_read_per_school = school_student_data[school_student_data["reading_score"]>=70].groupby("school_name")["reading_score"].count()
read_percent_per_school = (pass_read_per_school/students_per_school)*100
overall_pass_per_school = (math_percent_per_school + read_percent_per_school)/2

school_summary = pd.DataFrame({"Total Students":students_per_school,
                               "Total School Budget":budget_per_school,
                               "Per Student Budget":budget_per_student,
                               "Average Math Score":avg_math_per_school,
                               "Average Reading Score":avg_read_per_school,
                               "% Pass Math":math_percent_per_school,
                               "% Pass Reading":read_percent_per_school,
                               "Overall Passing Rate":overall_pass_per_school
                             })
school_summary

#Top 5 Performing Schools
top_performing_schools = school_summary.sort_values("Overall Passing Rate", ascending = False).head(5)
top_performing_schools

#Lowest 5 Performing Schools
lowest_performing_schools = school_summary.sort_values("Overall Passing Rate", ascending = True).head(5)
lowest_performing_schools

#Average Math Scores by Grade by School
math_9 = student_data[student_data["grade"]=="9th"].groupby("school_name")["math_score"].mean()
math_10 = student_data[student_data["grade"]=="10th"].groupby("school_name")["math_score"].mean()
math_11 = student_data[student_data["grade"]=="11th"].groupby("school_name")["math_score"].mean()
math_12 = student_data[student_data["grade"]=="12th"].groupby("school_name")["math_score"].mean()

gradelevel_math = pd.DataFrame({"9th":math_9,
                                "10th":math_10,
                                "11th":math_11,
                                "12th":math_12
                               })

gradelevel_math

#Average Reading Scores by Grade by School
read_9 = student_data[student_data["grade"]=="9th"].groupby("school_name")["reading_score"].mean()
read_10 = student_data[student_data["grade"]=="10th"].groupby("school_name")["reading_score"].mean()
read_11 = student_data[student_data["grade"]=="11th"].groupby("school_name")["reading_score"].mean()
read_12 = student_data[student_data["grade"]=="12th"].groupby("school_name")["reading_score"].mean()

gradelevel_read = pd.DataFrame({"9th":read_9,
                                "10th":read_10,
                                "11th":read_11,
                                "12th":read_12
                               })

gradelevel_read

#Scores by School Spending
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]

school_summary2 = school_summary.loc[:,"Per Student Budget":"Overall Passing Rate"]
school_summary2["Spending Ranges (Per Student)"]=pd.cut(school_summary2["Per Student Budget"], spending_bins, labels = group_names)
school_summary2 = school_summary2.groupby("Spending Ranges (Per Student)")
school_summary2.mean()

#Scores by School Size
size_bins = [0, 1000, 2000, 5000]
group_names2 = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

school_summary3 = school_summary.iloc[:,0:8]
school_summary3["School Size"]=pd.cut(school_summary3["Total Students"], size_bins, labels = group_names2)
school_summary3 = school_summary3.groupby("School Size")
school_summary3.mean()

school_summary4=school_summary.loc[:, "Average Math Score":"Overall Passing Rate"].groupby("type").mean()
school_summary4

