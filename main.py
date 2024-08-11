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
    st.header('Welcome to Flash-card 🗂️',anchor=False,divider='rainbow')
    st.caption('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat vulputate nisi tincidunt finibus.')
    c1,c2 = st.columns(2)
    c3,c4 = st.columns(2)
    
    with c1.container(border=True,height=200):
        st.image(image='images/flash-card.png',use_column_width='always')
        
    c1.page_link("pages/1_Flash_card.py", label="**Search Flash-Card >>>**", icon="🔎",use_container_width=True)

    with c2.container(border=True,height=200):
        st.image(image='images/add-flash-card.png',use_column_width='always')
    c2.page_link("pages/2_Add_flash_card.py", label="**Create Flash-Card >>>**", icon="✍",use_container_width=True)
        
    with c3.container(border=True,height=200):
        ...
    c3.page_link("pages/3_Statistics.py", label="**Statistics >>>**", icon="📈",use_container_width=True)
        
    with c4.container(border=True,height=200):
        ...
    c4.page_link("pages/Settings.py", label="**Settings >>>**", icon="⚙",use_container_width=True)
    
    
if __name__ == "__main__" :
    main()
    
    
    
    