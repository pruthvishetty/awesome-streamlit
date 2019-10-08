import streamlit as st
import pages.awesome_streamlit_vision
import pages.awesome_streamlit_resources
import importlib


def write():
    st.write(
        """
[Streamlit](https://streamlit.io/) is [announced](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace) as being **The fastest way to build custom Machine Learning tools** but I believe it has the potential to become much more awesome than that.

I believe Streamlit has the **potential to become the Iphone of Data Science, Technical Writing, Micro Apps, Code, Python and more**.

The purpose of this application is to

- Share list of awesome Streamlit resources.
- Share a vision on how awesome Streamlit can be.
- Provide awesome Streamlit examples.

You navigate to the material and examples using the sidebar on the left.
"""
    )
    st.write(
        """[![Streamlit Video](https://miro.medium.com/max/700/1*p3XPm-x0TUIuMmQQa4mjHQ.gif)](https://miro.medium.com/max/700/1*p3XPm-x0TUIuMmQQa4mjHQ.gif)"""
    )
