import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height_ft, height_in):
    # Convert height to meters (1 foot = 0.3048 meters, 1 inch = 0.0254 meters)
    height_m = (height_ft * 0.3048) + (height_in * 0.0254)
    bmi = weight / (height_m ** 2)
    return bmi

# Streamlit app UI
def main():
    st.title("BMI Calculator")

    # Input fields for weight and height
    weight = st.number_input("Enter your weight in kg:", min_value=1.0, value=60.0)
    height_ft = st.number_input("Enter your height (feet):", min_value=1, value=5)
    height_in = st.number_input("Enter your height (inches):", min_value=0, value=8)

    # BMI Calculation button
    if st.button("Calculate BMI"):
        # Validate inputs
        if weight <= 0 or height_ft < 0 or height_in < 0:
            st.error("Please enter valid positive values for weight and height.")
        else:
            # Calculate and display BMI
            bmi = calculate_bmi(weight, height_ft, height_in)
            st.write(f"Your BMI is: {bmi:.2f}")

            # Provide health category based on BMI value
            if bmi < 18.5:
                st.write("You are Underweight.")
            elif 18.5 <= bmi < 24.9:
                st.write("You have a Normal weight.")
            elif 25 <= bmi < 29.9:
                st.write("You are Overweight.")
            else:
                st.write("You are Obese.")

if __name__ == "__main__":
    main()
