import pandas as pd #pip install pandas openpyxl
import streamlit  as st # pip install streamlit
from app import excel_file
from app import selected

def consolidated():
    @st.cache(persist=True)         
    def get_data_from_excel():
            df = pd.read_excel(
                excel_file,
                engine="openpyxl",
                sheet_name="Cases",
                usecols="A:N",
                nrows=104,
                header = 0,
            )

            return df
    def get_data_from_excel2():
            df_consolidated = pd.read_excel(
                excel_file,
                engine="openpyxl",
                sheet_name="Consolidated",
                usecols="A:D",
                header=4,
                nrows=104,
            )
            df_consolidated.dropna(inplace=True)
            df_consolidated.drop([6, 6],axis=0,inplace=True)
            return df_consolidated

    if selected == 'Consolidated':
                df_consolidated = get_data_from_excel2()
        ### --- Gráfico barras Consolidated
                fig = px.bar(df_consolidated,
                x=["June", "July", "August"],
                y="Type", title="Type | Months ",
                barmode='group',
                labels={'pop':'Month'},
                template="plotly_white",
                orientation='h',
                #color_discrete_sequence=["#0083B8"] *3,
                )
                fig.update_layout(
                    plot_bgcolor="rgba(0,0,0,0)",
                    xaxis=(dict(showgrid=False))
                )
                st.plotly_chart(fig)