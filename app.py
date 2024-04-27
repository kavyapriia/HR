import streamlit as st
import pandas as pd
import csv

# Function to get user input and append to CSV
def get_user_input():
    with open("employees.csv", "a", newline="") as csvfile:
        fieldnames = ['name', 'age', 'dob', 'mobile', 'email', 'address', 'school', 'sscmarks', 'hscmarks',
                      'degree', 'college', 'cgpa', 'achievements', 'jobtitles', 'yearsofexp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        name = st.text_input("Enter your name:")
        dob = st.text_input("Enter your date of birth in the form DD/MM/YYYY:")
        mobile = st.text_input("Enter your mobile number:")
        email = st.text_input("Enter your email:")
        address = st.text_input("Enter your address:")
        school = st.text_input("Enter your school name:")
        sscmarks = st.text_input("Enter your 10th marks:")
        hscmarks = st.text_input("Enter your 12th marks:")
        degree = st.text_input("Enter your degree:")
        college = st.text_input("Enter your University or College:")
        cgpa = st.text_input("Enter your CGPA:")
        achievements = st.text_input("Enter your other Certifications and Academic achievements:")
        jobtitles = st.text_input("Enter the job titles you have experience in:")
        yearsofexp = st.text_input("Enter your years of experience:")


        submit=st.button("submit")
        st.write(submit)
        if submit is True:
          writer.writerow({"name": name, "dob": dob, "mobile": mobile, "email": email, "address": address,
                  "school": school, "sscmarks": sscmarks, "hscmarks": hscmarks, "degree": degree,
                  "college": college, "cgpa": cgpa, "achievements": achievements, "jobtitles": jobtitles,
                  "yearsofexp": yearsofexp})
          st.write("you application is successful")


# Function to display HR view
def display_hr_view():
    st.subheader("HR View")
    path = "employees.csv"
    df = pd.read_csv(path)
    st.write(df.head(10))

# Main function to run the Streamlit app
def main():
    st.title("Employee Management System")
    menu = ["Apply", "HR View"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Apply":
        get_user_input()
    elif choice == "HR View":
        display_hr_view()

if __name__ == "__main__":
    main()
