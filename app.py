import streamlit as st

import time

from prompt_template import features , user_stories , backlog , api_specification , data_model, wireframes ,technical_architecture

from langchain_openai import OpenAI, ChatOpenAI,AzureChatOpenAI

from langchain.prompts import PromptTemplate

from dotenv import load_dotenv

import json 





load_dotenv()



# azure_auth = AzureAuthenticator()

# azure_auth.set_environment_variables()



# llm = AzureChatOpenAI( model="ptc-chat-gpt-35-1106",

            # azure_endpoint="https://dp-ptc-dev-oai-gpt4.openai.azure.com/",

            # api_version="2024-02-15-preview",)


llm = ChatOpenAI(model="gpt-4o-mini")


# Load and display the logo at the top of the app

st.image("logo.png", width=200)  # Adjust width as needed



# Define the names of the tabs in order

tabs = ["Customer Idea/RFP", "Features", "User Stories", "Backlog", 

        "API Specifications", "Technical Architectures", "Wireframes", "Data Model"]




variables={

    "Features": "client_idea",

    "User Stories": "features",

    "Backlog": "user_stories",

    "API Specifications": "backlog",

    "Technical Architectures": "backlog",

    "Wireframes": "backlog",

    "Data Model": "backlog"

    }



refers={ 

    "Features": "customer_input",

    "User Stories": "Features_output",

    "Backlog": "User Stories_output",

    "API Specifications": "Backlog_output",

    "Technical Architectures": "Backlog_output",

    "Wireframes": "Backlog_output",

    "Data Model": "Backlog_output"

        }

prompts={

    "Features": features,

    "User Stories": user_stories,

    "Backlog": backlog,

    "API Specifications": backlog,

    "Technical Architectures": backlog,

    "Wireframes": backlog,

    "Data Model": backlog

    }



# Initialize session state for active tab and customer input

if "active_tab" not in st.session_state:

    st.session_state["active_tab"] = "Customer Idea/RFP"



for item in refers.values():

    if item not in st.session_state:

        st.session_state[item]=""


# Set a flag for each tab to track whether it's processed
if "processed_tabs" not in st.session_state:
    st.session_state["processed_tabs"] = {tab: False for tab in tabs}
# if "customer_input" not in st.session_state:

#     st.session_state["customer_input"] = ""



# Function to navigate to the next tab

def next_tab():

    current_index = tabs.index(st.session_state["active_tab"])

    next_index = (current_index + 1) % len(tabs)  # Cycle back to the first tab after the last

    st.session_state["active_tab"] = tabs[next_index]



# Function to create streaming text effect

def stream_text(text):

        text_display = st.empty()  # Create an empty element for the text

        for i in range(1, len(text) + 1):

            text_display.markdown(text[:i])

            time.sleep(0.01)





# Function to download the current tab content as JSON

def download_json(tab_name, tab_content):

    json_content = json.dumps({tab_name: tab_content})

    st.download_button(

        label=f"Download {tab_name} in JSON format",

        data=json_content,

        file_name=f"{tab_name}.json",

        mime="application/json"

    )

    

def call_llm(tab_name):

    variable=variables[tab_name]

    prompt=PromptTemplate(

                input_variables=[variable],

                template=prompts[tab_name]

            )

    chain=prompt | llm

    output_content=chain.invoke({variable:st.session_state[refers[tab_name]]}).content

    output_name=tab_name+"_output"

    st.session_state[output_name]=output_content

    return output_content

    

    

# Function to create layout for each tab

def create_tab_content(tab_name):

    st.header(f"{tab_name} Section")

    # Button label and navigation

    current_index = tabs.index(tab_name)
    next_tab_name = tabs[(current_index + 1) % len(tabs)]
    
    # Input for Customer Idea/RFP
    if tab_name == "Customer Idea/RFP":
        st.session_state["customer_input"] = st.text_area(
            "Input your Customer Idea/RFP", 
            value=st.session_state["customer_input"], 
            placeholder="Enter details here...", 
            height=200
        )
    else:
        # Check if content has been generated for the tab
        output_name = tab_name + "_output"
        if not st.session_state["processed_tabs"][tab_name]:
            output = call_llm(tab_name)
            stream_text(output)
            download_json(tab_name, output)
        else:
            # Display previously generated content
            stream_text(st.session_state[output_name])
            download_json(tab_name, st.session_state[output_name])

    # Navigation button
    if st.button(f"Go to {next_tab_name}"):
        next_tab()

# Render the active tab content
create_tab_content(st.session_state["active_tab"])