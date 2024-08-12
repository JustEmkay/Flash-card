import streamlit as st

# -> Page Config <-
st.set_page_config(
    initial_sidebar_state="collapsed",
)


def main():
    st.header("Statistics 📈",divider='red',anchor=False)
    
    # <- Activate-tracking ->
    with st.container(border=True):
        c1,actv_btn = st.columns([3,1],vertical_alignment='center')
        c1.info('Start tracking your studies')
        actv_btn.button('activate',type='primary',use_container_width=True)
        
    # <- S ->
    for i in st.session_state.hash_tags_notchecked + \
    st.session_state.hash_tags_checked:
        count = 0
        for dicts in st.session_state.flash_card_data:
            if i in dicts['tags']:
                count += 1
        st.write(f'{i} -> {count}')
    
    
if __name__ == "__main__" :
    main()
    