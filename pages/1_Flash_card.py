import streamlit as st
import time


# -> Page Config <-
st.set_page_config(
    initial_sidebar_state="collapsed",
)

#<- Search-Question-filter-function ->
def search_filter() -> list:
    if not st.session_state.hash_tags_checked:
        for dicts in st.session_state.flash_card_data:
            if dicts['question'] not in st.session_state.flash_card_questions:
                st.session_state.flash_card_questions.append(dicts['question'])
        return st.session_state.flash_card_questions
    else:
        st.session_state.flash_card_questions=[]
        for dicts in st.session_state.flash_card_data:
            for tag in st.session_state.hash_tags_checked:
                if tag in dicts['tags'] and dicts['question'] not in st.session_state.flash_card_questions:
                    st.session_state.flash_card_questions.append(dicts['question'])
        return st.session_state.flash_card_questions

#<- Answer-Animation ->
def stream_data(data):
    for word in data.split(" "):
        yield word + " "
        time.sleep(0.02)

#<- Update- -> 
def update_fc_questions() -> None:
    st.session_state.flash_card_questions = []
    for dicts in st.session_state.flash_card_data:
        st.session_state.flash_card_questions.appens(dicts['questions'])
    print('\nflash_card_questions session.state updated.\n')

def main():    
    st.header("Search Flash-card 🔎",divider='red',anchor=False)
    search_bar , filter_opt, search_btn = st.columns([3,1,1])
    
    #<- Searchbar ->
    multi = search_bar.multiselect('search bar',options=search_filter(),
                           placeholder="Enter the question?",
                          label_visibility='collapsed')
    if not multi:
            st.session_state.show_cards = False
            
    #<- Filter ->
    with filter_opt.popover("Filter",use_container_width=True):

        #<- Filter.checked ->        
        for tag in st.session_state.hash_tags_checked:
            if not st.checkbox(tag,value=True):
                st.session_state.hash_tags_notchecked.append(tag)
                st.session_state.hash_tags_checked.remove(tag)
                st.rerun()
                
        #<- Filter.notchecked ->
        for tag in st.session_state.hash_tags_notchecked:
            if st.checkbox(tag,value=False):
                st.session_state.hash_tags_checked.append(tag)
                st.session_state.hash_tags_notchecked.remove(tag)
                st.rerun()
   
    #<- Search button ->
    if search_btn.button('Load',type='primary',use_container_width=True):
        if multi:
            st.session_state.show_cards = True
            st.session_state.show_answer = False
            st.session_state.counter = 0

            
        #<- Flash-card Container ->      
    with st.container(border=True,height=450):
        
        #<- Q&A Container ->
        with st.container(border=True,height=350):
            if st.session_state.show_cards:
                if len(multi) > 0:             
                    c_header , c_dlt = st.columns([0.9,0.1])
                    st.divider()
                    #<- question -> 
                    c_header.subheader(multi[st.session_state.counter],anchor=False)
                    #<- delete button ->
                    if c_dlt.button('🗑️',help=":red-background[Delete flash-card 🗑️]",
                                    use_container_width=True):
                        print(f"\n selected flash-card->{multi[st.session_state.counter]} ")
                        try:
                            for index,dicts in enumerate(st.session_state.flash_card_data):
                                if dicts['question'] == multi[st.session_state.counter]:
                                    del st.session_state.flash_card_data[index]
                            update_fc_questions() 
                            st.toast(":green-background[Deleted flash-card successfully]")
                        except Exception as e:
                            st.toast(f":red-background[Error: {e}]")
                
                
                
                
                    if st.session_state.show_answer:
                        for data in st.session_state.flash_card_data:
                            if data['question'] == multi[st.session_state.counter]:
                                st.write_stream(stream_data(data['answer']))
                                    
                    
            else:
                st.caption("press ':green[load]' button to load flash cards")

        #<- Flash-card.button Container[no border] ->
        with st.container():
            btn1,btn2,btn3 = st.columns(3)
            
            #<- Prev-Button ->
            if btn1.button('⏮ prev',use_container_width=True):
                if st.session_state.counter != 0 :
                    st.session_state.counter -= 1
                    st.session_state.show_answer = False
                    st.rerun()
                    
            #<- Show-Button ->        
            if btn2.button('show 📖',use_container_width=True):
                st.session_state.show_answer = True
                st.rerun()
            
            #<- Next-Button ->        
            if btn3.button('next ⏭',use_container_width=True):
                if st.session_state.counter != (len(multi)-1) :
                    st.session_state.counter += 1
                    st.session_state.show_answer = False
                    st.rerun()

        
if __name__ == "__main__" :
    main()
    