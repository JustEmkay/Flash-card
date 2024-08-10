import streamlit as st

# -> Page Config <-
st.set_page_config(
    initial_sidebar_state="collapsed",
)


def main():
    # -> Sidebar for settings <-
    with st.sidebar:
        st.success('Settings selected')
    
    st.header("Settings ⚙",divider='red',anchor=False)
    
if __name__ == "__main__" :
    main()
    