# Import necessary libraries
import streamlit as st
import numpy as np
import pandas as pd

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

# Set up the title and description of the app
st.markdown("""
    <h1 style='text-align: center; font-weight: bold; font-size: 46px;'>
        University Health Center Capacity Expansion Guide
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; font-weight: normal; font-size: 18px;'>
        Complete the questionnaire below, and our algorithm will generate tailored recommendations for expanding your campus health center's capacity, without increasing fixed costs.
    </h1>
""", unsafe_allow_html=True)

st.markdown("<hr style='height:2px; border:none; color:#000000; background-color:#000000;' />", unsafe_allow_html=True)
st.markdown("""
    <h1 style='text-align: center; font-weight: bold; font-size: 20px;'>
        <u>Health Center Current Operations Questionnaire</u>
    </h1>
""", unsafe_allow_html=True)

# OTC Medicine Vending Machine
st.markdown("**<u>Question 1</u>**", unsafe_allow_html=True)
q1 = st.selectbox("Does the pharmacy sell over-the-counter (OTC) products at the on-campus health center?", 
                        options=['Yes', 'No'], index=None)
st.write('')

st.markdown("**<u>Question 2</u>**", unsafe_allow_html=True)
q2 = st.number_input("What percentage of visits to the health center are primarily for obtaining OTC products? (Enter percentage as a decimal)", 
                             min_value=0.0, max_value=1.0, step=.01)
st.write('')

# Nurse-led Appointments
st.markdown("**<u>Question 3</u>**", unsafe_allow_html=True)
q3 = st.number_input("On an average week, what percentage of visits to the health center are for the **Primary Health Services** listed below? (Enter percentage as a decimal)", 
                             min_value=0.0, max_value=1.0, step=.01)
q3_1 = st.selectbox("Who is currently providing **Primary Health Services** at the health center?", 
                            options=['Providers Only', 'Nurses Only', 'Both'], index=None)
q3_2 = st.markdown("""
Primary Healthcare Services:
  - Health assessments (physical exams, health history)
  - Health screenings (vision, hearing, blood pressure, cholesterol, glucose, BMI)""")
st.write('')

st.markdown("**<u>Question 4</u>**", unsafe_allow_html=True)
q4 = st.number_input("On an average week, what percentage of visits to the health center are for the **Sexual and Reproductive Health Services** listed below? (Enter percentage as a decimal)", 
                             min_value=0.0, max_value=1.0, step=.01)
q4_1 = st.selectbox("Who is currently providing **Sexual and Reproductive Health Services** at the health center?", 
                            options=['Providers Only', 'Nurses Only', 'Both'], index=None)
q4_2 = st.markdown("""
Sexual and Reproductive Health Services:
  - Contraceptive counseling and prescriptions
  - STI/STD testing and treatment (chlamydia, gonorrhea, etc.)
  - Pregnancy testing""")
st.write('')

st.markdown("**<u>Question 5</u>**", unsafe_allow_html=True)
q5 = st.number_input("On an average week, what percentage of visits to the health center are for the **Illness Care Services** listed below""? (Enter percentage as a decimal)", 
                             min_value=0.0, max_value=1.0, step=.01)
q5_1 = st.selectbox("Who is currently providing **Illness Care Services** at the health center?", 
                            options=['Providers Only', 'Nurses Only', 'Both'], index=None)
q5_2 = st.markdown("""
Illness Care Services:
  - Treatment for common illnesses (cold, flu, sore throat, minor infections)""")
st.write('')

st.markdown("**<u>Question 6</u>**", unsafe_allow_html=True)
q6 = st.number_input("On an average week, what percentage of visits to the health center are for the **Minor Injury Services** listed below? (Enter percentage as a decimal)", 
                             min_value=0.0, max_value=1.0, step=.01)
q6_1 = st.selectbox("Who is currently providing **Minor Injury Services** at the health center?", 
                            options=['Providers Only', 'Nurses Only', 'Both'], index=None)
q6_2 = st.markdown("""
Minor Injury Services:
  - Wound care (cleaning, dressing minor cuts, scrapes, burns)""")
st.write('')

st.markdown("**<u>Question 7</u>**", unsafe_allow_html=True)
q7 = st.number_input("On an average week, what percentage of visits to the health center are for the **Vaccination Services** listed below? (Enter percentage as a decimal)", 
                             min_value=0.0, max_value=1.0, step=.01)
q7_1 = st.selectbox("Who is currently providing **Vaccination Services** at the health center?", 
                            options=['Providers Only', 'Nurses Only', 'Both'], index=None)
q7_2 = st.markdown("""
Vaccination Services:
  - Flu shots and routine immunizations (MMR, tetanus, etc.)
  - COVID-19 vaccination/booster shots
  - Travel vaccinations for study abroad""")
st.write('')

st.markdown("**<u>Question 8</u>**", unsafe_allow_html=True)
q8 = st.number_input("On an average week, what percentage of visits to the health center are for the **Post-Exposure Services** listed below? (Enter percentage as a decimal)", 
                             min_value=0.0, max_value=1.0, step=.01)
q8_1 = st.selectbox("Who is currently providing **Post-Exposure Services** at the health center?", 
                            options=['Providers Only', 'Nurses Only', 'Both'], index=None)
q8_2 = st.markdown("""
Post-Exposure Services:
  - Emergency contraception (Plan B)
  - HIV Post-Exposure Prophylaxis (PEP)""")
st.write('')

st.markdown("**<u>Question 9</u>**", unsafe_allow_html=True)
q9 = st.number_input("On an average week, what percentage of visits to the health center are for the **Allergy Management Services** listed below? (Enter percentage as a decimal)", 
                             min_value=0.0, max_value=1.0, step=.01)
q9_1 = st.selectbox("Who is currently providing **Allergy Management Services** at the health center?", 
                            options=['Providers Only', 'Nurses Only', 'Both'], index=None)
q9_2 = st.markdown("""
Allergy Management Services:
  - Seasonal allergy care and over-the-counter treatments
  - Allergy shots (immunotherapy)""")
st.write('')

st.markdown("**<u>Question 10</u>**", unsafe_allow_html=True)
q10 = st.number_input("On an average week, what percentage of visits to the health center are for the **Follow-Up Care Services** listed below? (Enter percentage as a decimal)", 
                             min_value=0.0, max_value=1.0, step=.01)
q10_1 = st.selectbox("Who is currently providing **Follow-Up Care Services** at the health center?", 
                             options=['Providers Only', 'Nurses Only', 'Both'], index=None)
q10_2 = st.markdown("""
Follow-Up Care Services:
  - Chronic disease follow-up (asthma, diabetes, hypertension)
  - Post-treatment follow-ups""")
st.write('')

# Pop-up clinic
st.markdown("**<u>Question 11</u>**", unsafe_allow_html=True)
q11 = st.selectbox('Is staff willing to provide care at an on-campus location outside of the health center?', 
                    options= ['Yes', 'No'], index=None)
st.write('')

st.markdown("**<u>Question 12</u>**", unsafe_allow_html=True)
q12 = st.selectbox("Where are **Flu Shots** being provided to students on campus?",
                    options=['Health Center (Appointments/Walk-In)', 'Pop-Up Clinic', 'Hybrid', 'Do Not Provide'], index=None)
st.write('')

st.markdown("**<u>Question 13</u>**", unsafe_allow_html=True)
q13 = st.selectbox("Where are **COVID-19 Vaccination/Booster Shots** being provided to students on campus?",
                    options=['Health Center (Appointments/Walk-In)', 'Pop-Up Clinic', 'Hybrid', 'Do Not Provide'], index=None)
st.write('')

st.markdown("**<u>Question 14</u>**", unsafe_allow_html=True)
q14 = st.selectbox("Where are **Routine Immunizations (MMR, tetanus, etc.)** being provided to students on campus?",
                    options=['Health Center (Appointments/Walk-In)', 'Pop-Up Clinic', 'Hybrid', 'Do Not Provide'], index=None)
st.write('')

st.markdown("**<u>Question 15</u>**", unsafe_allow_html=True)
q15 = st.selectbox("Where are **Seasonal Allergy Management Services** being provided to students on campus?",
                    options=['Health Center (Appointments/Walk-In)', 'Pop-Up Clinic', 'Hybrid', 'Do Not Provide'], index=None)
st.write('')

# Self-Testing
st.markdown("**<u>Question 16</u>**", unsafe_allow_html=True)
q16 = st.selectbox('How are **STD/STI** testing services being provided to students on campus?', 
                           options=['Health Center (Appointments/Walk-In)', 'Self-Testing', 'Hybrid'], index=None)
q16_1 = st.number_input('On an average week, what percentage of visits to the health center are for **STD/STI** testing services? (Enter percentage as a decimal)', 
                            min_value=0.0, max_value=1.0, step=.01)
st.write('')

st.markdown("**<u>Question 17</u>**", unsafe_allow_html=True)
q17 = st.selectbox('How are **Pregnancy** testing services being provided to students on campus?', 
                           options=['Health Center (Appointments/Walk-In)', 'Self-Testing', 'Hybrid'], index=None)
q17_1 = st.number_input('On an average week, what percentage of visits to the health center are for **Pregnancy** testing services? (Enter percentage as a decimal)', 
                            min_value=0.0, max_value=1.0, step=.01)
st.write('')

st.markdown("**<u>Question 18</u>**", unsafe_allow_html=True)
q18 = st.selectbox('How are **UTI** testing services being provided to students on campus?', 
                           options=['Health Center (Appointments/Walk-In)', 'Self-Testing', 'Hybrid'], index=None)
q18_1 = st.number_input('On an average week, what percentage of visits to the health center are for **UTI** testing services? (Enter percentage as a decimal)', 
                            min_value=0.0, max_value=1.0, step=.01)
st.write('')

st.markdown("**<u>Question 19</u>**", unsafe_allow_html=True)
q19 = st.selectbox('How are **COVID-19 Antigen** testing services being provided to students on campus?', 
                           options=['Health Center (Appointments/Walk-In)', 'Self-Testing', 'Hybrid'], index=None)
q19_1 = st.number_input('On an average week, what percentage of visits to the health center are for **COVID-19 Antigen** testing services? (Enter percentage as a decimal)', 
                            min_value=0.0, max_value=1.0, step=.01)
st.write('')

st.markdown("**<u>Question 20</u>**", unsafe_allow_html=True)
q20 = st.selectbox('How are **Strep Throat** testing services being provided to students on campus?', 
                           options=['Health Center (Appointments/Walk-In)', 'Self-Testing', 'Hybrid'], index=None)
q20_1 = st.number_input('On an average week, what percentage of visits to the health center are for **Strep Throat** testing services? (Enter percentage as a decimal)', 
                            min_value=0.0, max_value=1.0, step=.01)
st.write('')

st.markdown("**<u>Question 21</u>**", unsafe_allow_html=True)
q21 = st.selectbox('How are **Blood Pressure** monitoring services being provided to students on campus?', 
                           options=['Health Center (Appointments/Walk-In)', 'Self-Testing', 'Hybrid'], index=None)
q21_1 = st.number_input('On an average week, what percentage of visits to the health center are for **Blood Pressure** monitoring services? (Enter percentage as a decimal)', 
                            min_value=0.0, max_value=1.0, step=.01)
st.write('')

st.markdown("**<u>Question 22</u>**", unsafe_allow_html=True)
q22 = st.selectbox('How are **Blood Glucose** monitoring services being provided to students on campus?', 
                           options=['Health Center (Appointments/Walk-In)', 'Self-Testing', 'Hybrid'], index=None)
q22_1 = st.number_input('On an average week, what percentage of visits to the health center are for **Blood Glucose** monitoring services? (Enter percentage as a decimal)', 
                            min_value=0.0, max_value=1.0, step=.01)
st.write('')

# Telehealth
st.markdown("**<u>Question 23</u>**", unsafe_allow_html=True)
q23 = st.write('How are the services listed below currently being offered to students?')
q23_1 = st.selectbox('General Health Consultations (ie. routine checkups for minor illnesses or injuries)', 
                            options=['In-Person', 'Teleheath', 'Hybrid'], index=None)
q23_2 = st.selectbox('Prescription Refills', 
                            options=['In-Person', 'Teleheath', 'Hybrid'], index=None)
q23_3 = st.selectbox('Follow-Up Care', 
                            options=['In-Person', 'Teleheath', 'Hybrid'], index=None)
submit_button = st.button('Submit Form Data')



if submit_button == True:
    result = []
    
    if q1 == "Yes" and q2 >= 0.1:
        result.append("OTC Medicine Vending Machines")

    if q3 >= 0.2 and q3_1 == ('Providers Only' or 'Both'):
        result.append("Nurse-led Appointments for Primary Health Services")

    if q4 >= 0.2 and q4_1 == ('Providers Only' or 'Both'):
        result.append("Nurse-led Appointments for Sexual and Reproductive Health Servicess")

    if q5 >= 0.2 and q5_1 == ('Providers Only' or 'Both'):
        result.append("Nurse-led Appointments for Illness Care Services")

    if q6 >= 0.2 and q6_1 == ('Providers Only' or 'Both'):
        result.append("Nurse-led Appointments for Minor Injury Services")

    if q7 >= 0.2 and q7_1 == ('Providers Only' or 'Both'):
        result.append("Nurse-led Appointments for Vaccination Services")

    if q8 >= 0.2 and q8_1 == ('Providers Only' or 'Both'):
        result.append("Nurse-led Appointments for Post-Exposure Services")

    if q9 >= 0.2 and q9_1 == ('Providers Only' or 'Both'):
        result.append("Nurse-led Appointments for Allergy Management Services")

    if q10 >= 0.2 and q10_1 == ('Providers Only' or 'Both'):
        result.append("Nurse-led Appointments for Follow-Up Care Services")
 
    if q11 == "Yes":
        if q7 >= .1 and q12 == 'Health Center (Appointments/Walk-In)':
            result.append("Flu Shot Pop-Up Clinics")

        if q7>= .1 and q13 == 'Health Center (Appointments/Walk-In)':
            result.append("COVID-19 Vaccination/Booster Shot Pop-Up Clinics")

        if q7 >= .1 and q14 == 'Health Center (Appointments/Walk-In)':
            result.append("Routine Immunization (MMR, tetanus, etc.) Pop-Up Clinics")

        if q9 >= .1 and q15 == 'Health Center (Appointments/Walk-In)':
            result.append("Seasonal Allergy Management Pop-Up Clinics")
            
    if q16 == ('Health Center (Appointments/Walk-In)') and q16_1 >= 0.1:
        result.append("Self-Testing for STD/STI")

    if q17 == ('Health Center (Appointments/Walk-In)') and q17_1 >= 0.1:
        result.append("Self-Testing for Pregnancy")
      
    if q18 == ('Health Center (Appointments/Walk-In)') and q18_1 >= 0.1:
        result.append("Self-Testing for UTI")
    
    if q19 == ('Health Center (Appointments/Walk-In)') and q19_1 >= 0.1:
        result.append("Self-Testing for COVID-19 Antigen")

    if q20 == ('Health Center (Appointments/Walk-In)') and q20_1 >= 0.1:
        result.append("Self-Testing for Strep Throat")

    if q21 == ('Health Center (Appointments/Walk-In)') and q21_1 >= 0.1:
        result.append("Self-Testing for Blood Pressure Monitors")

    if q22 == ('Health Center (Appointments/Walk-In)') and q22_1 >= 0.1:
        result.append("Self-Testing for Blood Glucose Monitors")

    if q23_1 == ("In-Person"):
        result.append("Telehealth Appointments for General Health Consultations")

    if q23_2 == ("In-Person"):
        result.append("Telehealth Appointments for Prescription Refills")

    if q23_3 == ("In-Person"):
        result.append("Telehealth Appointments for Follow-up Care")

    st.sidebar.success("✅ Data submitted successfully!")

    # Display the result
    if result:
        st.sidebar.header("Recommended Services:")
        numbered_list = '\n'.join([f"{i+1}. {item}" for i, item in enumerate(result)])
        st.sidebar.write(numbered_list)
    else:
        st.sidebar.write("No recommended services for increasing the capacity of your campus health center.")
else: 
    st.sidebar.warning('⚠️ Please fill out the form to provide recommendations.')
