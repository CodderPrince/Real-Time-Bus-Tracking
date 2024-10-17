import streamlit as st
from PIL import Image
import os

# App title and layout
st.set_page_config(page_title="Real-Time Bus Tracking", layout="wide")

# Sidebar with radio buttons to navigate between pages
option = st.sidebar.radio(
    "Choose a Page",
    ["Home", "Sign Up", "Bus Schedule", "Map Location", "Journey"]
)

# ===========================
# Home Page: Display images from 'image' folder
# ===========================
if option == "Home":
    st.title("Welcome to Your Real-Time Bus Tracking")
    st.subheader("Explore Our Services and Track Your Bus Effortlessly!")

    # Custom order of images for the Home page
    home_image_order = [
        "1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"
    ]

    # Folder path where home images are stored
    image_folder = "image"

    # Display home images in the specified order
    cols = st.columns(3)  # Create 3 columns
    for index, image_file in enumerate(home_image_order):
        image_path = os.path.join(image_folder, image_file)

        # Check if the file exists to avoid errors
        if os.path.isfile(image_path):
            image = Image.open(image_path)
            cols[index % 3].image(image, caption=image_file, use_column_width=True)
        else:
            st.warning(f"Image '{image_file}' not found in the 'image' folder.")

# ===========================
# Sign Up Page
# ===========================
elif option == "Sign Up":
    st.header("Sign Up")
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")
    if st.button("Submit"):
        st.success(f"Welcome, {name}! Your account has been created.")

# ===========================
# Bus Schedule Page: Display images from 'bus schedule' folder
# ===========================
elif option == "Bus Schedule":
    st.header("Bus Schedule")
    st.subheader("Check the bus schedule and routes below.")

    # Display route details
    schedule = {
        "Route 1": "University -> Tajhat -> Shapla Chattar -> University",
        "Route 2": "University -> Satmatha -> Pressclub -> University",
        "Route 3": "University -> Nisbetganj -> Shapla Chattar -> University",
        "Route 4": "University -> Medical Mor -> T.T.College -> University",
        "Route 5": "University -> Medical Mor -> Hazir Hat -> University"
    }
    for route, time in schedule.items():
        st.write(f"**{route}**: {time}")

    # Custom order of images for Bus Schedule
    schedule_image_order = [
        "1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg"
    ]

    # Folder path for bus schedule images
    schedule_folder = "bus schedule"

    # Display bus schedule images in the specified order
    cols = st.columns(2)  # Create 2 columns
    for index, image_file in enumerate(schedule_image_order):
        image_path = os.path.join(schedule_folder, image_file)

        # Check if the file exists to avoid errors
        if os.path.isfile(image_path):
            image = Image.open(image_path)
            cols[index % 2].image(image, caption=image_file, use_column_width=True)
        else:
            st.warning(f"Image '{image_file}' not found in the 'bus schedule' folder.")

# ===========================
# Map Location Page (Google Maps embed)
# ===========================
elif option == "Map Location":
    st.header("Map Location")

    # Embed Google Maps iframe
    st.markdown(
        """
        <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.835434509399!2d144.95373631531588!3d-37.81627997975154!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad642af0f11fd81%3A0xf5777df9f28210a!2sFederation%20Square!5e0!3m2!1sen!2sau!4v1617719961120!5m2!1sen!2sau"
            width="100%" 
            height="500" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy">
        </iframe>
        """,
        unsafe_allow_html=True
    )

# ===========================
# Journey Page: Select journey locations and show available buses
# ===========================
elif option == "Journey":
    st.header("Plan Your Journey")
    st.subheader("Select Your Journey Location")

    # Define routes and available buses
    routes = {
        "Route 1": ["University", "Tajhat", "Shapla Chattar", "Bikon Mor", "Khamar Mor", "Lalbag", "University"],
        "Route 2": ["University", "Satmatha", "Tajhat", "Pressclub", "University"],
        "Route 3": ["University", "Nisbetganj", "Shapla Chattar", "Bikon Mor", "Khamar Mor", "Lalbag", "University"],
        "Route 4": ["University", "Medical Mor", "T.T.College", "University"],
        "Route 5": ["University", "Medical Mor", "Hazir Hat", "University"]
    }

    bus_name = {
        "Route 1": ["Shamasundari", "Jaleswari", "Padmaraga"],
        "Route 2": ["Teesta", "Shatranji", "Charyapad"],
        "Route 3": ["Ekuse", "Shamasundari", "Shatranji"],
        "Route 4": ["Jaleswari", "Charyapad", "Padmaraga"],
        "Route 5": ["Ekuse", "Shatranji", "Jaleswari"]
    }

    # Input fields for From and To stoppage
    from_stoppage = st.selectbox(
        "From Stoppage",
        ["University", "Tajhat", "Lalbag", "Khamar Mor", "Bikon Mor", "Shapla Chattar",
         "Pressclub", "Satmatha", "Hazir Hat", "T.T.College", "Medical Mor"]
    )
    to_stoppage = st.selectbox(
        "To Stoppage",
        ["University", "Tajhat", "Lalbag", "Khamar Mor", "Bikon Mor", "Shapla Chattar",
         "Pressclub", "Satmatha", "Hazir Hat", "T.T.College", "Medical Mor"]
    )

    # Show available buses on button click
    if st.button("Available Bus"):
        if from_stoppage == to_stoppage:
            st.warning("Please select different stoppages.")
        else:
            matching_routes = [
                route for route, stops in routes.items()
                if from_stoppage in stops and to_stoppage in stops
            ]

            if matching_routes:
                st.success(f"Available buses from {from_stoppage} to {to_stoppage}:")
                for route in matching_routes:
                    st.write(f"**{route}**: {' -> '.join(routes[route])}")
                    st.write(f"Available Buses: {', '.join(bus_name[route])}")
            else:
                st.error(f"No available bus route found from {from_stoppage} to {to_stoppage}.")
