import streamlit as st
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType


class WebScraping:
    def __init__(self):
        progressbar = st.progress(0, "Starting...")

        @st.cache_resource
        def get_driver():
            # Deploy
            chromedriver = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install() 
            # Path to your chromedriver.exe (verify your Chrome version)
            #chromedriver = r'C:\_chromedriver\chromedriver.exe' 
            return webdriver.Chrome(
                service=Service(chromedriver), 
                options=options,
            )
            
        progressbar.progress(5, "Configuration...")
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")

        progressbar.progress(10, "Loading Driver...")
        driver = get_driver()

        progressbar.progress(30, "Connecting to Example.com...")
        driver.get("http://example.com")

        title = driver.find_element(By.XPATH, "/html/body/div/h1")
        st.write(title.text)
        
        paragraph = driver.find_element(By.XPATH, "/html/body/div/p[1]")
        st.write(paragraph.text)

        st.write("---")

        st.write("**Page source:**")
        st.code(driver.page_source)

        progressbar.progress(100, "Scraping OK!")


class main():
    def __init__(self):
        st.set_page_config(
            page_title="Web Scraping",
            page_icon="🌐",
            layout="wide",
        )
        st.title("Web Scraping online with Selenium")
        st.write("---")
        
        with st.container():
            if st.button("Start Connect to Example.com"):
                WebScraping()


if __name__ == "__main__":
    main()