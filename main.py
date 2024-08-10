import streamlit as st

# -> session state <-
if 'flash_card_data' not in st.session_state : 
    st.session_state.flash_card_data = [{
        'question' : 'What is Wabi-sabi?',
        'answer' : "Wabi-sabi is a Japanese concept that embraces imperfection, \
        transience, and simplicity. It's a philosophy that values the natural \
        world and recognizes that everything is imperfect, impermanent, and incomplete.",
        'tags' : [ '#japanese' , '#philosophy'  ],
        'created_date' : 1722973770000
    },
    {
        'question' : "what is the meaning of 'adios amigos' ? ",
        'answer' : "Adios amigos is a Spanish phrase that translates to 'good-bye,dear friend'.\
            'Adios' is a Spanish word means 'farewell' and 'amigos' means 'friend'.",
        'tags' : [ '#Spanish' , '#language'  ],
        'created_date' : 1722975923000
    },
                                        ] 

if 'flash_card_questions' not in st.session_state:
    st.session_state.flash_card_questions = []

if 'flash_card_filtered' not in st.session_state:
    st.session_state.flash_card_filtered = []
    
if 'hash_tags_notchecked' not in st.session_state : 
    st.session_state.hash_tags_notchecked=[]
    for dict in st.session_state.flash_card_data:
        for tag in dict['tags']:
            if tag not in st.session_state.hash_tags_notchecked:
                st.session_state.hash_tags_notchecked.append(tag)

if 'hash_tags_checked' not in st.session_state :
    st.session_state.hash_tags_checked=[]
    
if 'counter' not in st.session_state : st.session_state.counter = 0
    
if 'show_cards' not in st.session_state : st.session_state.show_cards = False
if 'show_answer' not in st.session_state : st.session_state.show_answer = False



# -> Page Config <-
st.set_page_config(
    initial_sidebar_state="collapsed",
)


def main():
    # -> Sidebar for main-page <-
    # with st.sidebar:
    # st.session_state.flash_card_data
    st.header('Welcome to Flash card',divider='green')
    # st.caption("dadadajwdbnawjmnd")
    
    c1,c2,c3 = st.columns(3)
    
    with c1.container(border=True):
        st.metric(label="Cards", value=len(st.session_state.flash_card_data))
    with c2.container(border=True):
        ...
    with c3.container(border=True):
        ...
    st.divider()
    
if __name__ == "__main__" :
    main()
    
    
    
    