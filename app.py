import streamlit as st
from PIL import Image
import os

# App title
st.set_page_config(page_title="Real-Time Bus Tracking", layout="wide")  # Optional: Wide layout for better UI

# Sidebar with multiple options
option = st.sidebar.selectbox(
    "Choose a Page",
    ["Home", "Sign Up", "Bus Schedule", "Map Location", "Journey"]
)

# Home Page: Display default images from 'image' folder
if option == "Home":
    st.title("Welcome to Your Real-Time Bus Tracking")
    st.subheader("Explore Our Services and Track Your Bus Effortlessly!")

    # Display images from the 'image' folder
    image_folder = "image"  # Folder path
    image_files = os.listdir(image_folder)  # List all files in the folder

    cols = st.columns(2)  # Create 3 columns for displaying images
    for index, image_file in enumerate(image_files):
        if image_file.lower().endswith(('jpg', 'jpeg', 'png')):  # Filter images by extension
            image_path = os.path.join(image_folder, image_file)
            image = Image.open(image_path)
            cols[index % 2].image(image, caption=image_file, use_column_width=True)

# Sign Up Page
elif option == "Sign Up":
    st.header("Sign Up")
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")
    if st.button("Submit"):
        st.success(f"Welcome, {name}! Your account has been created.")

# Bus Schedule Page: Display images from 'bus schedule' folder
elif option == "Bus Schedule":
    st.header("Bus Schedule")
    st.subheader("Check the bus schedule and routes below.")

    schedule = {
        "Route 1": "University -> Tajhat -> Shapla Chattar -> Varisty",
        "Route 2": "University -> Satmatha -> Pressclub -> Varisty",
        "Route 3": "University -> Nisbetganj -> Shapla Chattar -> Varisty",
        "Route 4": "University -> Medical Mor -> T.T.College -> Varisty",
        "Route 5": "University -> Medical Mor -> Hazir Hat -> Varisty"
    }
    for route, time in schedule.items():
        st.write(f"**{route}**: {time}")

    # Display images from 'bus schedule' folder
    schedule_folder = "bus schedule"
    schedule_files = os.listdir(schedule_folder)

    cols = st.columns(2)  # Create 3 columns for the images
    for index, schedule_file in enumerate(schedule_files):
        if schedule_file.lower().endswith(('jpg', 'jpeg', 'png')):
            schedule_path = os.path.join(schedule_folder, schedule_file)
            schedule_image = Image.open(schedule_path)
            cols[index % 2].image(schedule_image, caption=schedule_file, use_column_width=True)

# Map Location Page (Embedding Google Maps)
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

# Journey Page: Select journey locations and show available buses
elif option == "Journey":
    st.header("Plan Your Journey")
    st.subheader("Select Your Journey Location")

    # Dictionary of routes with their stoppages
    routes = {
        "Route 1": ["University", "Tajhat", "Shapla Chattar", "Bikon Mor", "Khamar Mor", "Lalbag", "University"],
        "Route 2": ["University", "Satmatha", "Tajhat", "Pressclub", "University"],
        "Route 3": ["University", "Nisbetganj", "Shapla Chattar", "Shapla Chattar", "Bikon Mor", "Khamar Mor", "Lalbag", "University"],
        "Route 4": ["University", "Medical Mor", "T.T.College", "University"],
        "Route 5": ["University", "Medical Mor", "Hazir Hat", "University"]
    }

    # Dictionary of bus names for each route
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

    # Button to show available buses
    if st.button("Available Bus"):
        if from_stoppage == to_stoppage:
            st.warning("Please select different stoppages.")
        else:
            # Find routes where both stoppages are present
            matching_routes = []
            for route, stops in routes.items():
                if from_stoppage in stops and to_stoppage in stops:
                    matching_routes.append(route)

            # Display matching routes and their available bus names
            if matching_routes:
                st.success(f"Available buses from {from_stoppage} to {to_stoppage}:")
                for route in matching_routes:
                    st.write(f"**{route}**: {' -> '.join(routes[route])}")
                    st.write(f"Available Buses: {', '.join(bus_name[route])}")
            else:
                st.error(f"No available bus route found from {from_stoppage} to {to_stoppage}.")
