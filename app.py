import streamlit as st

from prompts import PROMPTS
from openai_service import generate_content


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Writing Assistant",
    page_icon="✍️",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0e1117;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #262730;
    }

    /* Main title */
    .main-title {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        font-size: 20px;
        margin-bottom: 35px;
        color: #dddddd;
    }

    /* Task title */
    .task-title {
        font-size: 32px;
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* Generate button */
    div.stButton > button {
        background-color: #ff4b4b;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 25px;
        font-size: 17px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #ff3333;
        color: white;
    }

    /* Output box */
    .output-box {
        background-color: #262730;
        padding: 25px;
        border-radius: 10px;
        margin-top: 25px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("AI Configuration")

    # Provider
    st.write("AI Provider")

    provider = st.selectbox(
        "AI Provider",
        ["OpenAI"],
        label_visibility="collapsed"
    )


    # Task
    st.write("Task")

    task = st.selectbox(
        "Task",
        [
            "Blog Writing",
            "Email Drafting",
            "Code Explanation",
            "Social Media Post"
        ],
        label_visibility="collapsed"
    )


    # Temperature
    st.write("Temperature")

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.6,
        step=0.1,
        label_visibility="collapsed"
    )

    st.caption(f"Current temperature: {temperature:.1f}")


    # Output format
    st.write("Output Format")

    output_format = st.selectbox(
        "Output Format",
        [
            "Plain Text",
            "Markdown"
        ],
        label_visibility="collapsed"
    )


# --------------------------------------------------
# MAIN CONTENT
# --------------------------------------------------

st.markdown(
    '<div class="main-title">✍️ AI Writing Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Generate blogs, emails, code explanations, and social media posts using AI.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# TASK HEADING
# --------------------------------------------------

st.markdown(
    f'<div class="task-title">{task}</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# INPUT
# --------------------------------------------------

if task == "Blog Writing":

    placeholder = "Example: Benefits of Generative AI in software development"

elif task == "Email Drafting":

    placeholder = "Example: Write an email requesting leave for two days"

elif task == "Code Explanation":

    placeholder = "Paste your Python, Java, JavaScript, or other code here"

else:

    placeholder = "Example: My journey learning Generative AI"


user_input = st.text_area(
    f"Enter your {task.lower()}",
    placeholder=placeholder,
    height=220
)


# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------

generate_button = st.button(
    "🚀 Generate Content",
    use_container_width=False
)


# --------------------------------------------------
# GENERATE CONTENT
# --------------------------------------------------

if generate_button:

    if not user_input.strip():

        st.warning(
            "Please enter some content before generating."
        )

    else:

        # Get selected prompt
        prompt_template = PROMPTS[task]

        # Insert user input
        prompt = prompt_template.format(
            input_text=user_input
        )


        # Add output format instruction
        if output_format == "Markdown":

            prompt += """
            
Format the response using Markdown.
Use headings, bullet points, and emphasis where appropriate.
"""

        else:

            prompt += """
            
Return the response as clean plain text.
"""


        # Temperature instruction
        prompt += f"""

Creativity preference:
{temperature}

Use a writing style appropriate for the selected creativity level.
"""


        # Call OpenAI
        with st.spinner("Generating content..."):

            try:

                result = generate_content(prompt)


                # --------------------------------------------------
                # OUTPUT
                # --------------------------------------------------

                st.markdown(
                    '<div class="output-box">',
                    unsafe_allow_html=True
                )

                st.subheader("Generated Content")

                if output_format == "Markdown":

                    st.markdown(result)

                else:

                    st.text(result)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


            except Exception as e:

                st.error(
                    f"An error occurred: {str(e)}"
                )