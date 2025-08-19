import streamlit as st
import json
import os

# Sample data structure for tools
script_dir = os.path.dirname(os.path.abspath(__file__))  # folder of the .py file
file_path = os.path.join(script_dir, "tools.json")

tools = json.load(open(file_path, "r", encoding="utf-8"))

# Sidebar filters
selected_tags = st.sidebar.multiselect(
    "Filter by tags",
    options={tag for tool in tools for tag in tool["tags"]}
)
geospatial_filter = st.sidebar.selectbox(
    "Geospatial classification",
    options=["All", "Geospatial", "Non-geospatial"]
)
os_filter = st.sidebar.selectbox(
    "Code-base",
    options=["All", "Open-source", "Closed"]
)
# Page title
st.title("Access Tools Dashboard")
# Filter logic
def filter_tools(tools, tags, geospatial, os):
    filtered = []
    for tool in tools:
        if tags and not set(tags).issubset(set(tool["tags"])):
            continue
        if geospatial == "Geospatial" and not tool["geospatial"]:
            continue
        if geospatial == "Non-geospatial" and tool["geospatial"]:
            continue
        if os == "Open-source" and not tool["os"]:
            continue
        if os == "Closed" and tool["os"]:
            continue
        filtered.append(tool)
    return filtered

filtered_tools = filter_tools(tools, selected_tags, geospatial_filter, os_filter)

# Display tools
for tool in filtered_tools:
    st.subheader(tool["name"])
    st.write(", ".join(tool["tags"]))
    #st.write("Geospatial: " + str(tool["geospatial"]))
    preview = tool["description"][:200] + "..." if len(tool["description"]) > 200 else tool["description"]
    if st.button(f"Read more about {tool['name']}"):
        st.write(tool["description"])
        if "website" in tool and tool["website"]:
            st.markdown(f"More information: {tool['website']}")
    else:
        st.write(preview)