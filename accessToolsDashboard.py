import streamlit as st

# Sample data structure for tools
tools = [
    {
        "name": "OnSSET (Open Source Spatial Electrification Tool)",
        "description": "OnSSET is an open-source geospatial modeling tool designed to support long-term electricity planning, particularly for rural electrification in developing countries. It uses spatial data such as population distribution, energy demand, existing infrastructure, renewable energy resources, and technology costs to identify least-cost electrification pathways. By comparing grid extension, mini-grid, and standalone system options, OnSSET helps policymakers, planners, and researchers evaluate electrification strategies and investment priorities at national or regional scales.",
        "tags": ["geospatial electrification"],
        "geospatial": True,
        "os": True
    }
    ,
    {
        "name": "REM (Reference Electrification Model)",
        "description": "REM is a geospatially driven, open-source modeling tool developed by MIT and collaborators to support electrification planning. It optimizes least-cost electricity access strategies by analyzing grid extension, mini-grid, and off-grid solutions. REM integrates population data, demand forecasts, costs, and geographic information to design detailed electrification plans, often at village or household level, making it suitable for policymakers, utilities, and NGOs focused on expanding energy access.",
        "tags": ["geospatial electrification"],
        "geospatial": True,
        "os": False

    }
    ,
    {
        "name": "HOMER (Hybrid Optimization of Multiple Energy Resources)",
        "description": "HOMER is a widely used commercial software for designing and optimizing hybrid renewable energy systems. It allows users to simulate different combinations of energy resources—such as solar, wind, diesel, hydro, and storage—and evaluate them based on cost, reliability, and technical feasibility. HOMER is particularly useful for microgrid design, rural electrification, and distributed energy projects, helping developers, engineers, and policymakers identify least-cost and sustainable energy solutions.",
        "tags": ["mini-grid optimization"],
        "geospatial": False,
        "os": False
    }
    ,
    {
        "name": "MicroGridsPy",
        "description": "MicroGridsPy is an open-source Python-based simulation and optimization tool designed for microgrid planning and analysis. It enables users to model hybrid energy systems, evaluate technical performance, and optimize investment decisions. The tool supports multi-year simulations, integration of renewable resources, storage technologies, and demand-side management. Its flexibility and open-source nature make it suitable for researchers, developers, and decision-makers working on energy access and decentralized energy systems.",
        "tags": ["mini-grid optimization"],
        "geospatial": False,
        "os": True
    }
    ,
    {
        "name": "Odyssey",
        "description": "Odyssey is a cloud-based platform designed to support the development, financing, and management of mini-grid and decentralized energy projects. It provides tools for data management, financial modeling, performance monitoring, and portfolio management, enabling project developers, financiers, and governments to scale up energy access initiatives. By standardizing project data and processes, Odyssey facilitates investment flows into distributed energy systems, particularly in emerging markets.",
        "tags": ["platform", "monitoring"],
        "geospatial": False,
        "os": False
    }


]

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
    else:
        st.write(preview)