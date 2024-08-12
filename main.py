import streamlit as st

# -> session state <-
if 'flash_card_data' not in st.session_state : 
    st.session_state.flash_card_data =  [
    {
        'question' : 'What is Wabi-sabi?',
        'answer' : "Wabi-sabi is a Japanese concept that embraces imperfection, \
        transience, and simplicity. It's a philosophy that values the natural \
        world and recognizes that everything is imperfect, impermanent, and incomplete.",
        'tags' : [ '#japanese' , '#philosophy'  ],
        'created_date' : 1722973770000
    },
    {
        'question' : "What is the meaning of 'adios amigos'?",
        'answer' : "Adios amigos is a Spanish phrase that translates to 'good-bye, dear friend'. \
        'Adios' is a Spanish word that means 'farewell' and 'amigos' means 'friends'.",
        'tags' : [ '#spanish' , '#language'  ],
        'created_date' : 1722975923000
    },
    {
        'question': 'What is the speed of light?',
        'answer': "The speed of light in a vacuum is approximately 299,792 kilometers per second \
        (km/s), or about 186,282 miles per second (mi/s). This is considered the ultimate speed \
        limit in the universe according to Einstein's theory of relativity.",
        'tags': ['#physics', '#science'],
        'created_date': 1722978932000
    },
    {
        'question': 'What is the capital of Australia?',
        'answer': "The capital of Australia is Canberra. Contrary to popular belief, Sydney or Melbourne \
        are not the capital cities of Australia, though they are the largest cities.",
        'tags': ['#geography', '#australia'],
        'created_date': 1722980045000
    },
    {
        'question': 'What are Newton’s Three Laws of Motion?',
        'answer': "Newton's First Law states that an object at rest stays at rest and an object in motion \
        stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force. \
        Newton's Second Law states that Force equals mass times acceleration (F=ma). \
        Newton's Third Law states that for every action, there is an equal and opposite reaction.",
        'tags': ['#physics', '#newton'],
        'created_date': 1722981857000
    },
    {
        'question': 'What is the meaning of "carpe diem"?',
        'answer': "'Carpe diem' is a Latin phrase that translates to 'seize the day'. It encourages people \
        to make the most of the present moment without worrying too much about the future.",
        'tags': ['#latin', '#philosophy'],
        'created_date': 1722983248000
    },
    {
        'question': 'What is the difference between a meteor and a meteorite?',
        'answer': "A meteor is the streak of light produced when a meteoroid enters the Earth's atmosphere and burns up. \
        A meteorite is a fragment of a meteoroid that survives its passage through the atmosphere and lands on Earth.",
        'tags': ['#astronomy', '#space'],
        'created_date': 1722984550000
    },
    {
        'question': 'What is the significance of the number "pi" (π)?',
        'answer': "Pi (π) is the ratio of a circle's circumference to its diameter and is approximately equal to 3.14159. \
        It is a crucial constant in mathematics and is used in various formulas involving circles, such as calculating \
        the area or circumference.",
        'tags': ['#mathematics', '#constants'],
        'created_date': 1722985731000
    },
    {
        'question': 'What is the "butterfly effect"?',
        'answer': "The 'butterfly effect' is a concept in chaos theory that suggests small changes in initial conditions \
        can lead to vastly different outcomes. The term is often used to describe how tiny, seemingly insignificant events \
        can have large, unpredictable consequences.",
        'tags': ['#chaos_theory', '#science'],
        'created_date': 1722986842000
    },
    {
        'question': 'What is the main ingredient in guacamole?',
        'answer': "The main ingredient in guacamole is avocado. It is typically mashed and mixed with lime juice, salt, \
        onions, tomatoes, and cilantro to create the classic Mexican dip.",
        'tags': ['#food', '#mexican_cuisine'],
        'created_date': 1722987923000
    }
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

# -> Statistics-page-session.states <-
if 'hashtag_count' not in st.session_state : st.session_state.hashtag_count = ()



# -> Page Config <-
st.set_page_config(
    initial_sidebar_state="collapsed",
)

def main():
    st.header('Welcome to Flash-card 🗂️',anchor=False,divider='rainbow')
    st.caption('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat vulputate nisi tincidunt finibus.')
    c1,c2 = st.columns(2)
    c3,c4 = st.columns(2)
    
    # with c1.container(border=True,height=200):
    c1.image(image='images/flash-card.png',use_column_width='always')
        
    c1.page_link("pages/1_Flash_card.py", label="**Search Flash-Card >>>**", icon="🔎",use_container_width=True)

    # with c2.container(border=True,height=200):
    c2.image(image='images/add-flash-card.png',use_column_width='always')
    c2.page_link("pages/2_Add_flash_card.py", label="**Create Flash-Card >>>**", icon="✍",use_container_width=True)
        
    with c3.container(border=True,height=200):
        ...
    c3.page_link("pages/3_Statistics.py", label="**Statistics >>>**", icon="📈",use_container_width=True)
        
    with c4.container(border=True,height=200):
        ...
    c4.page_link("pages/Settings.py", label="**Settings >>>**", icon="⚙",use_container_width=True)
    
    
if __name__ == "__main__" :
    main()
    
    
    
    