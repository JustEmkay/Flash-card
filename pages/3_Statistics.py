import streamlit as st
from annotated_text import annotated_text
import graphviz

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
        
    # <- Hashtag count->
    st.session_state.hashtag_count = ()
    for i in st.session_state.hash_tags_notchecked + \
    st.session_state.hash_tags_checked:
        count = 0
        for dicts in st.session_state.flash_card_data:
            if i in dicts['tags']:
                count += 1
        st.session_state.hashtag_count = list(st.session_state.hashtag_count)
        st.session_state.hashtag_count.append((i,str(count)))
        st.session_state.hashtag_count = tuple(st.session_state.hashtag_count)
        

    st.subheader('Hashtag count #️⃣',divider=True,anchor=False)
    annotated_text([tags for tags in st.session_state.hashtag_count])

    # Create a graphlib graph object
    graph = graphviz.Digraph()
    graph.edge("run", "intr")
    graph.edge("intr", "runbl")
    graph.edge("runbl", "run")
    graph.edge("run", "kernel")
    graph.edge("kernel", "zombie")
    graph.edge("kernel", "sleep")
    graph.edge("kernel", "runmem")
    graph.edge("sleep", "swap")
    graph.edge("swap", "runswap")
    graph.edge("runswap", "new")
    graph.edge("runswap", "runmem")
    graph.edge("new", "runmem")
    graph.edge("sleep", "runmem")

    st.graphviz_chart(graph)

    
if __name__ == "__main__" :
    main()
    