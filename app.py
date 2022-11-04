
import streamlit as st


import tabs.home
import tabs.basicNLP
import tabs.NERT
import tabs.textSummarization


PAGES = {
    "Home": tabs.home,
    "Basic NLP": tabs.basicNLP,
    "Text Summarization": tabs.textSummarization,
    #"Machine Translation": pages.machineTranlation
    #"Caption Generator": pages.captionGenerator
}


def main():
    
    st.sidebar.title("Whatsapp Analyzer")
    
    
    st.sidebar.title("Navigation")
    tabs = st.sidebar.radio("Go to", list(PAGES.keys()))

    #PAGES[page].main()


    with st.spinner(f"Loading {tabs} ..."):
        PAGES[tabs].main()

        
    
    st.sidebar.title("About App")
    
    
    
    
    st.sidebar.title("Contact Developer")
    st.sidebar.info(
        """
        This app is develop by subhayan. You can contact me at
        [Subhayan](https://github.com/subhayan25).
"""
    )

  

    
if __name__ == "__main__":
    main()
