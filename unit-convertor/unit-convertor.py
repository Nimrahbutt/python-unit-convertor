import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000
    }

    # Corrected the key formation
    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion  # Fixed the calculation
    else:
        return "Conversion not supported"

st.title("Unit Converter")

# User input
value = st.number_input("Enter the value:")
unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

# Perform conversion on button click
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")
