import streamlit as st
import re
from annotated_text import annotated_text
from datetime import datetime



# -> session state <-
if 'tag_list' not in st.session_state: st.session_state.tag_list=None

# -> Page Config <-
st.set_page_config(
    initial_sidebar_state="collapsed",
        page_title='Add Flash-Card',
)

# -> Functions <-
def tags_to_list(text):
    # function to filter hashtags
    print("\nfn-> tags_to_list")
    print("input: ",text)
    
    text = text.split()
    print("text to unf-list: ",text)
    flist = [tag.lower() for tag in text if re.search("#",tag)]
    print("text to f-list: ",flist)
    st.session_state.tag_list=flist


# -> Dialogue box <-
@st.dialog("Flash-Card")
def show_flash_card(question,answer,tags):
    with st.container(border=True):
        st.subheader(question,anchor=False,divider=True)
        st.write(answer)
    with st.container(border=True):
        annotated_text("tags: ",[(tags,"","green") for tags in st.session_state.tag_list])
    if st.button("Create card",use_container_width=True,type='primary'):
        try:
            st.session_state.flash_card_data.append(
                {
                'question' : question,
                'answer' : answer,
                'tags' : tags,
                'created_date' : datetime.now().timestamp()
                }
            )
            st.toast(':green[Added to Successful!!]')
            
            for tag in tags:
                if tag not in st.session_state.hash_tags_notchecked:
                    st.session_state.hash_tags_notchecked.append(tag)

            st.toast(':green[Updated #hashtags]',icon="#️⃣")
            
        except:
            st.toast("Error appending!!")



def main():    
    # -> Sidebar for add_flash-card <-
    with st.sidebar:
        st.success('Add flash-card selected')
    
    st.header("Add Flash Card",divider='blue',anchor=False)
    
    # -> add card Form <-
    question : str = st.text_input("Enter question:") 
    answer = st.text_area("Enter answer for above question:")    
    
    
    hash_tags = st.text_input("Enter tags related to above questions",
                placeholder="Enter tags related to above questions",
                help='use white space to input different tags',
                label_visibility='collapsed',
                )
    if hash_tags:
        tags_to_list(hash_tags)
    else:
        st.session_state.tag_list=[]
    
    with st.expander(':red[Hashtags Stored (***Suggetions***)]',expanded=False):
        if st.session_state.hash_tags_notchecked + st.session_state.hash_tags_checked:
            annotated_text([(tags,"","#de554b") \
                for tags in st.session_state.hash_tags_notchecked + st.session_state.hash_tags_checked])
        else:
            st.info('Hashtags not found.')
    annotated_text("#tags: ",[(tags,"","green") for tags in st.session_state.tag_list])
    
    if question and answer and st.session_state.tag_list:
        btn_actv = False
        btn_help=':green[Press to perview flash card.]'
    else:
        btn_actv = True
        btn_help=':red[Check all inputs]'
                
    if st.button("Card Preview",use_container_width=True,
                 type='primary',disabled=btn_actv,help=btn_help):
            show_flash_card(question,answer,st.session_state.tag_list)




    
# <<<< MAIN >>>> 
if __name__ == "__main__" :
    main()
    