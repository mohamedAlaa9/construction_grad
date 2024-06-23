import streamlit as st

st.set_page_config(
    page_title="Construction Graduation Project",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)

st.markdown(
    """
    <div style='text-align: center;'>
        <h1>Construction Graduation Project</h1>
    </div>
    """,
    unsafe_allow_html=True
)


sustainable_credits = [
    ("Construction activity pollution prevention", 0, True, 15000),
    ("Site assessment", 1, False, 20000),
    ("Protect or restore habitat", 2, False, 32950),
    ("Open space", 1, False, 0),
    ("Rainwater management", 3, False, 0),
    ("Heat island reduction", 1, False, 17000),
]

location_credits =[
    ("Bicycle Facilities", 1, False, 3500),
    ("Reduced Parking Footprint", 1, False, 0),
    ("Electric vehicles", 1, False, 28500),
    ("Surrounding Density and Diverse Uses", 4, False, 0),
    ("Sensitive Land Protection", 1, False, 0),
    ("Access to Quality Transit", 5, False, 0),
    ("High Priority Site and Equitable Development", 1, False, 10000),
]

water_credits = [
    ("Outdoor water use reduction", 0, True, 10000),
    ("Indoor water use reduction", 0, True, 26270),
    ("Building-level water metering", 0, True, 0),
    ("Outdoor water use reduction_2", 1, False, 3000),
    ("Indoor water use reduction_2", 4, False, 0),
    ("Water metering", 1, False, 2000)
]

energy_credits = [
    ("Fundamental commissioning and verification", 0, True, 30000),
    ("Minimum energy performance", 0, True, 0),
    ("Building-level energy metering", 0, True, 0),
    ("Fundamental refrigerant management", 0, True, 0),
    ("Enhanced commissioning", 6, False, 30000),
    ("Optimize energy performance", 13, False, 10500),
    ("Advanced energy metering", 1, False, 24000),
    ("Renewable energy", 5, False, 41800),
]

material_credits = [
    ("Storage and collection of recyclables", 0, True, 2800),
    ("Building life-cycle impact reduction", 3, False, 200000),
    ("Construction and demolition waste management", 2, False, 0)
]

indoor_credits = [
    ("Minimum IAQ performance", 0, True, 0),
    ("Environmental tobacco smoke control", 0, True, 1500),
    ("Enhanced IAQ strategies", 1, False, 8100),
    ("Low-emitting materials", 1, False, 0),
    ("Construction IAQ management plan", 1, False, 15000),
    ("Thermal comfort", 1, False, 0),
    ("Interior lighting", 1, False, 7500),
    ("Daylight", 3, False, 10000),
]

innovation_credits = [
    ("Innovation", 0, False, 0),
    ("LEED Accredited Professional", 1, False, 0)
]

regional_credits = [
    ("Regional Priority", 4, False, 0)
]

def display_credits(title, credits, parent_checkbox=None):
    with st.expander(title):
        total_points = 0
        total_money = 0
        all_selected = False

        if parent_checkbox:
            col_1, col_2 = st.columns([4, 1])
            with col_1:
                st.write(f"{parent_checkbox[0]}")
            with col_2:
                parent_checked = st.checkbox('', value=parent_checkbox[2], key=parent_checkbox[0], disabled=parent_checkbox[2])
                all_selected = parent_checked
                if all_selected:
                    total_points += parent_checkbox[1]
                    total_money += parent_checkbox[3]
                    
        for text, points, required, money in credits:
            col_1, col_2, col_3, col_4 = st.columns([3, 2, 1, 1])
            with col_1:
                st.write(f"{text} {'(Required)' if required else ''}")
            with col_2:
                selected = st.checkbox("", value=required or all_selected, key=text)
                if selected:
                    total_points += points
                    total_money += money    
            with col_3:
                st.write(f"Points: {points}")
            with col_4:
                st.write(f"Money: ${money}")

        st.write(f"**Total Points for {title}: {total_points}**")
        st.write(f"**Total Money for {title}: ${total_money}**")
        return total_points, total_money

# Track total points and money across all categories
total_points = 0
total_money = 0

# Create columns with increased spacing and no margin for the first and last columns
col1, spacer1, col2, spacer2, col3 = st.columns([4, 1, 4, 1, 4])

with col1:
    points, money = display_credits("Location & Transportation", location_credits)
    total_points += points
    total_money += money

with col2:
    points, money = display_credits("Sustainable Sites", sustainable_credits)
    total_points += points
    total_money += money

with col3:
    points, money = display_credits("Water Efficiency", water_credits)
    total_points += points
    total_money += money

# Create columns with increased spacing and no margin for the first and last columns
col1, spacer1, col2, spacer2, col3 = st.columns([4, 1, 4, 1, 4])

with col1:
    points, money = display_credits("Energy & Atmosphere", energy_credits)
    total_points += points
    total_money += money

with col2:
    points, money = display_credits("Material & Resources", material_credits)
    total_points += points
    total_money += money

with col3:
    points, money = display_credits("Indoor Environmental Quality", indoor_credits)
    total_points += points
    total_money += money

col1, spacer1, col2, spacer2, col3 = st.columns([4, 1, 4, 1, 4])

with col1:
    points, money = display_credits("Innovation", innovation_credits)
    total_points += points
    total_money += money

with col2:
    points, money = display_credits("Regional Priority", regional_credits)
    total_points += points
    total_money += money

# Display total points and money at the bottom of the last column using st.markdown
with col3:
    st.markdown(
        f"""
        <div style="margin-top: 10px;">
            <p><strong>Total Points Achieved: {total_points}</strong></p>
            <p><strong>Total Money: {total_money} EGP</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if total_points >= 40 and total_points <= 49:
        st.image("certified.jpeg")
    elif total_points >= 50 and total_points <= 59:
        st.image("silver.jpeg")
    elif total_points >= 60 and total_points <= 79:
        st.image("gold.jpeg")
    elif total_points >= 80:
        st.image("platinum.jpeg")
    else:
        st.write("No certificate earned yet.")





