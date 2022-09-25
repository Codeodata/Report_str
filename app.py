from email import header
from streamlit_lottie import st_lottie
from itertools import pairwise
from logging import warning
from tkinter import HORIZONTAL
from turtle import position
import pandas as pd #pip install pandas openpyxl
import streamlit  as st # pip install streamlit
import plotly.express as px #pip install plotly -express
from PIL import Image
from streamlit_option_menu import option_menu
import requests


def load_lottieurl(url:str):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
if "excel_file" not in st.session_state:
        st.session_state["excel_file"]=""

excel_file = st.text_input("Introduzca el archivo que desea visualizar con su extensión .xlsx", st.session_state["excel_file"])
submit = st.button("Submit")

selected = st.sidebar.selectbox('Menu', ['Configuration', 'Cases',
     'Consolidated','Type','Severity','Reason','Status','Product','Information','Interventions'])
selected

if submit:
    st.session_state["excel_file"] = excel_file
    st.write("ingresaste: ", excel_file)

#### Gráfico Configuración
lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_cyvxw69x.json")
st_lottie(
    lottie_hello,
    speed = 1,
    reverse = False,
    loop = True,
    quality= "low",
    height = 300,
    width = 1000,
    key = None,
    )

#### Leyendo Reporte Hoja x Hoja
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
def get_data_from_excel3():
        df_type_num = pd.read_excel(
            excel_file,
            engine="openpyxl",
            sheet_name="Type",
            usecols="A:B",
            header=4,
            nrows=104,
        )
        return df_type_num
def get_data_from_excel4():
        df_severity = pd.read_excel(
            excel_file,
            engine="openpyxl",
            sheet_name="Severity",
            usecols="A:B",
            header=6,
            nrows=3,
        )
        return df_severity
def get_data_from_excel5():
        df_severity2 = pd.read_excel(
            excel_file,
            engine="openpyxl",
            sheet_name="Severity",
            usecols="A:B",
            header=21,
            nrows=3,
        )
        return df_severity2
def get_data_from_excel6():
        df_reason = pd.read_excel(
            excel_file,
            engine="openpyxl",
            sheet_name="Reason",
            usecols="A:B",
            header=4,
            nrows=12,
        )
        return df_reason
def get_data_from_excel7():
        df_reason2 = pd.read_excel(
            excel_file,
            engine="openpyxl",
            sheet_name="Reason",
            usecols="A:B",
            header=25,
            nrows=9,
        )
        return df_reason2
def get_data_from_excel8():
        df_status = pd.read_excel(
            excel_file,
            engine="openpyxl",
            sheet_name="Status",
            usecols="A:B",
            header=4,
            nrows=6,
        )
        return df_status
def get_data_from_excel9():
        df_product = pd.read_excel(
            excel_file,
            engine="openpyxl",
            sheet_name="Product",
            usecols="A:B",
            header=6,
            nrows=6,
        )
        return df_product
def get_data_from_excel10():
        df_information = pd.read_excel(
            excel_file,
            engine="openpyxl",
            sheet_name="Information",
            usecols="A:B",
            header=5,
            nrows=8,
        )
        return df_information
def get_data_from_excel11():
        df_intervention = pd.read_excel(
            excel_file,
            engine="openpyxl",
            sheet_name="Interventions",
            usecols="A:B",
            header=6,
            nrows=4,
        )
        return df_intervention
if selected == "Cases":
    df = get_data_from_excel()
    st.dataframe(df)
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
if selected == "Type":
            df_type_num = get_data_from_excel3()
    ### --- Gráfico Pie Type
            numeros = df_type_num[0:6]
            random_x = numeros['#']
            df_type = df_type_num.loc[:]
            types = df_type['Type'].drop(5,axis=0,inplace=True)
            st.subheader(types)
            names = types
            fig2 = px.pie(values=random_x ,names = names,title='Types Current Month')
            st.plotly_chart(fig2)
            fig2.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))
            )
if selected == "Severity":
            df_severity = get_data_from_excel4()
            df_severity2 = get_data_from_excel5()
                ### --- Gráfico Pie Severity
            numeros2 = df_severity[0:]
            random_x2 = numeros2['#']
            df_severity_names = df_severity.loc[:]
            types = df_severity_names['Severity']
            names = types
            fig3 = px.pie(values=random_x2 ,names = names,title='Severity ALL CASES')
            st.plotly_chart(fig3)
            fig3.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
            )
            ## --- Gráfico Pie Severity2
            numeros2 = df_severity2[0:]
            random_x2 = numeros2['#']
            df_severity_names = df_severity.loc[:]
            df_severity_names.dropna(inplace=True)

            types = df_severity_names['Severity']
            names = types
            fig4 = px.pie(values=random_x2 ,names = names,title='Severity ALL CASES')
            st.plotly_chart(fig4)
            fig4.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
            )
if selected == "Reason":
            df_reason = get_data_from_excel6()
            df_reason2 = get_data_from_excel7()
            ### --- Gráfico Pie Reason
            numeros2 = df_reason[0:]
            random_x2 = numeros2['#']
            df_severity_names = df_reason.loc[:]
            types = df_severity_names['Reason']
            names = types
            fig5 = px.pie(values=random_x2 ,height = 800,names = names,title='REASON ALL CASES')
            st.plotly_chart(fig5)
            ### --- Gráfico Pie Reason 2
            numeros2 = df_reason2[0:]
            random_x2 = numeros2['#']
            df_severity_names = df_reason2.loc[:]
            types = df_reason['Reason']  
            names = types
            fig6 = px.pie(values=random_x2 ,height = 500,names = names,title='INCIDENT CASES')
            st.plotly_chart(fig6)
if selected == "Status":

            df_status = get_data_from_excel8()

            ### --- Gráfico Pie Statuss
            numeros2 = df_status[0:]
            random_x2 = numeros2['#']
            df_severity_names = df_status.loc[:]
            types = df_severity_names['Status']
            names = types
            fig7 = px.pie(values=random_x2 ,height = 500,names = names,title='STATUS CASES')
            st.plotly_chart(fig7)
if selected == "Product":
            df_product = get_data_from_excel9()
    ### --- Gráfico Pie Product
            numeros2 = df_product[0:]
            random_x2 = numeros2['#']
            df_severity_names = df_product.loc[:]
            types = df_severity_names['Product']
            names = types
            fig8 = px.pie(values=random_x2 ,height = 500,names = names,title='STATUS CASES')
            st.plotly_chart(fig8)
if selected == "Information":

### --- Gráfico Bar Information
            df_information = get_data_from_excel10()
            fig9 = px.bar(df_information,
                        x="Hours",
                        y="Month", title="INFORMATION (Type | Hours) ",
                        barmode='group',
                        labels={'pop':'Hours'},
                        template="plotly_white",
                        orientation='h',
                        )
            fig9.update_layout(
                #plot_bgcolor="rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False))
            )
            st.plotly_chart(fig9)
            st.subheader("Total de horas en el año")
            total_hours = df_information['Hours'].sum()
            st.subheader(total_hours)
            df_information = get_data_from_excel10()
if selected == "Interventions": 
            df_intervention = get_data_from_excel11()
            ### --- Gráfico Pie Interventions
            numeros2 = df_intervention[0:]
            random_x2 = numeros2['#']
            df_severity_names = df_intervention.loc[:]
            types = df_severity_names['Activity Type']
            names = types
            fig10 = px.pie(values=random_x2 ,height = 500,names = names,title='ACTIVITY TYPE')
            st.plotly_chart(fig10)

            st.subheader("TOTAL")
            st.subheader(df_intervention['#'].sum())
            #---- HIDE STREAMLIT STYLE ----
            hide_st_style = """
                        <style>
                        #MainMenu {visibility: hidden;}

                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                        </style>
                        """
            st.markdown(hide_st_style, unsafe_allow_html=True)


# # ### SIDEBARS
# #     # ---- TYPE ----
# # st.sidebar.header("Please Filter Here:")
# # type = st.sidebar.multiselect(
# #     "TYPE:",
# #     options=df["TYPE"].unique(),
# #     default=df["TYPE"].unique()
# # )
# # ---- SITE ----
# site = st.sidebar.multiselect(
#     "SITE:",
#     options=df["SITE"].unique(),
#     default=df["SITE"].unique()
# )
# # ---- STATUS ----
# status = st.sidebar.multiselect(
#     "STATUS:",
#     options=df["STATUS"].unique(),
#     default=df["STATUS"].unique()
# )
# # ---- PRODUCT ----
# product = st.sidebar.multiselect(
#     "PRODUCT:",
#     options=df["PRODUCT"].unique(),
#     default=df["PRODUCT"].unique()
# )
# df_selection = df.query(
#     "TYPE == @type & SITE ==@site & STATUS == @status & PRODUCT == @product"
# )

# TYPES BY MONHT LINE [#]

