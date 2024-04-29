import streamlit as st
import pandas as pd

class Charts:
    def __init__(self):
        df = pd.read_excel("files/clientes_exemplo.xlsx")

        df_regimes = df['REGIME'].value_counts().reset_index().rename(columns={'REGIME': 'Regime', 'count': 'Quantidade'})
        df_regimes.index = range(1, len(df_regimes) + 1)

        tab1, tab2 = st.tabs(["📈 Chart", "🎲 Data"])
        tab1.bar_chart(df_regimes, x='Regime', y='Quantidade', use_container_width=True)
        tab2.write(df_regimes)
    


class main():
    def __init__(self):
        st.set_page_config(
            page_title="Charts",
            page_icon="🌐",
            layout="wide",            
        )
        st.title("Charts")
        st.write("---")
        

        with st.container():
            st.subheader("Type of Regime")
        
            Charts()

            st.write("---")


if __name__ == "__main__":
    main()