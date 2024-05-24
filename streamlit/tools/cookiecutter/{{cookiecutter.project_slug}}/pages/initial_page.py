import common.page_frags as pf
from pages._base_page import BasePageLayout
from pages.pages import app_pages
from common.utils import sidebar_config
from utils.config import settings
import streamlit as st


class LandingPage(BasePageLayout):
    def __init__(self):
        super().__init__()

    def page_content(self):
        st.set_page_config(
            page_icon=settings.app.logo, page_title="Main Page", layout="wide"
        )
        sidebar_config(app_pages())
        st.header("Your new Streamlit app!")
        st.markup("Review the README.md for how to customize it")
        pf.summary()

        # Proof-of-life debug info
        pf.debug_info()


def main():
    page = LandingPage()
    page.page_content()


if __name__ == "__main__":
    main()
