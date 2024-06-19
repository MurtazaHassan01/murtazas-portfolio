import streamlit as st


# st.set_page_config(layout="wide")
# st.markdown("""<style>.main {max-width: 1200px;margin: 0 auto;}
#     </style>""",unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader(" ")
    st.subheader(" ")
    st.subheader("Hi :wave:")
    st.title("I am Murtaza Hassan ")

with col2:
    st.image("images/murtaza.png")

st.write("")  # Add a single line of space
st.write("")  # Add a single line of space

st.title("About Me")
st.write("Iam an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics. I run one of the largest YouTube channels in the field of Computer Vision, educating over 3 Million developers, hobbyists and students. I obtained my Bachelor’s degree in Mechatronics and later specialized in the field of Robotics from Bristol University (UK). He is also a serial entrepreneur having launched several successful ventures including CVZone, which is a one stop solution for learning and building vision projects. Prior to starting his entrepreneurial career, Murtaza worked as a university lecturer and a design engineer, evaluating and developing rapid prototypes of US patents.")
st.write("")  # Add a single line of space
st.write("")  # Add a single line of space
st.write("")  # Add a single line of space
st.write("")  # Add a single line of space




col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.markdown("- Largest Computer Vision Channel")
    st.markdown("- 400k+ Subscribers")
    st.markdown("- Over 150 Free Tutorials")
    st.markdown("- 15 Million+ Views")
    st.markdown("- 1.5 Million Hours+ Watch time")


with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")

st.write("")  # Add a single line of space
st.write("")  # Add a single line of space


st.title("My Setup")
st.image("images/setup.jpg")




st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 90)
st.slider("Robotics", 0, 100, 85)

st.write("")  # Add a single line of space
st.write("")  # Add a single line of space




st.title("Gallery")
image_paths = []
for i in range(9):
    image_paths.append(f"images/g{i+1}.jpg" )

# Create a 3x3 grid for the image gallery
col1, col2, col3 = st.columns(3)

with col1:
    st.image(image_paths[0])
    st.image(image_paths[1])
    st.image(image_paths[2])

with col2:
    st.image(image_paths[3])
    st.image(image_paths[4])
    st.image(image_paths[5])

with col3:
    st.image(image_paths[6])
    st.image(image_paths[7])
    st.image(image_paths[8])

st.write("")  # Add a single line of space
st.write("")  # Add a single line of space


st.write("CONTACT")
st.title("For any inquiries please email")
st.subheader("contact@murtazahassan.com")
