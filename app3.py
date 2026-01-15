import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("خريطة Leafmap تفاعلية في Streamlit")

# إنشاء الخريطة Folium فقط
m = leafmap.Map(center=[40, -100], zoom=4, draw_control=True)

# إضافة Marker تجريبي
m.add_marker(location=[40, -100], popup="Marker تجريبي")

# عرض الخريطة
m.to_streamlit(height=600)
