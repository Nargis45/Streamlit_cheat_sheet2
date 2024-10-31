import streamlit as st

st.set_page_config(layout="wide")

st.title("All about Streamlit :coffee: ")
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #ffefba, #ffffff);
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#tabs
listTabs = ["Cheat Sheet", "Designs"]
tab1, tab2= st.tabs(listTabs)

with tab1:
    col1, col2, col3= st.columns([4,5,4])
    with col1:
        st.write('Install and Import')
        st.code("""$ pip install streamlit
import streamlit as st""")
        st.write('Run streamlit file')
        st.code("""streamlit run filename.py""")

        st.write('Learn about streamlit basic functions:')
        with st.expander("Text Elements"):
            st.help(st.title)
            st.help(st.header)
            st.help(st.subheader)
            st.help(st.text)
            st.help(st.write)
            st.help(st.markdown)
            st.help(st.caption)
            st.help(st.latex)
            st.help(st.code)
            st.help(st.echo)

        with st.expander("Status Elements"):
            st.help(st.success)
            st.help(st.info)
            st.help(st.warning)
            st.help(st.error)
            st.help(st.balloons)
            st.help(st.snow)
            st.help(st.progress)
            st.help(st.toast) 
            st.help(st.spinner)
            st.help(st.exception)
            st.help(st.status)
            st.help(st.divider)

        with st.expander("Control Flow"):
            st.help(st.stop)

        with st.expander("Input Widgets"):
            st.help(st.button)
            st.help(st.download_button)
            st.help(st.checkbox)
            st.help(st.radio)
            st.help(st.selectbox)
            st.help(st.multiselect)
            st.help(st.slider)
            st.help(st.select_slider)
            st.help(st.color_picker)
            st.help(st.toggle)
            st.help(st.camera_input)
            st.help(st.image)
            st.help(st.link_button)
            st.help(st.text_input)
            st.help(st.number_input)
            st.help(st.text_area)
            st.help(st.date_input)
            st.help(st.time_input)
            st.help(st.file_uploader)

        with st.expander("Layouts and Containers"):
            st.help(st.container)
            st.help(st.columns)
            st.help(st.expander)
            st.help(st.popover)
            st.help(st.tabs)
            st.help(st.form)

        with st.expander("Media Elements"):
            st.help(st.image)
            st.help(st.audio)
            st.help(st.video)
            
        with st.expander("Session Elements"):
            st.help(st.session_state)
            
        with st.expander("Data Display Elements"):
            st.help(st.dataframe)
            st.help(st.data_editor)
            st.help(st.table)
            st.help(st.json)
            st.help(st.metric)
            
        with st.expander("Charts Elements"):
            st.help(st.line_chart)
            st.help(st.area_chart)
            st.help(st.bar_chart)
            st.help(st.altair_chart)
            st.help(st.pyplot)
            st.help(st.plotly_chart)
            st.help(st.bokeh_chart)
            st.help(st.pydeck_chart)
            st.help(st.map)
        
        with st.expander("Caching"):
            st.help(st.cache_data)
            st.help(st.cache_resource)

        with st.expander("Database Connection"):
            st.help(st.cache_data)
