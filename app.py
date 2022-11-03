"""Main module for the streamlit Paribhasha app"""
import streamlit as st


import tabs.home
import tabs.basicNLP
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
        This app is develop by Mainak. You can contact me at
        [Subhayan](https://github.com/subhayan25).
"""
    )

   #st.sidebar.markdown("[![Github](https://github.com/aryanc55/NLPJenny/blob/master/assests/github.png?raw=true)](https://github/aryanc55)")
    
   

    
if __name__ == "__main__":
    main()
