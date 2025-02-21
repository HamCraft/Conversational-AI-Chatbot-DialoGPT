
import backend
import streamlit as st
from streamlit_chat import message as st_message

st.title("Conversational-AI Chatbot (DialoGPT)")
st.subheader("By Ahmed Yaqoob Dhedhi")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# # ✅ Wrap title & subtitle inside a container and center-align it properly
# st.markdown(
#     """
#     <style>
#         /* Center Align Title */
#         .title-container {
#             text-align: center;
#         }

#         /* Hover effect for icons */
#         .icon:hover {
#             transform: scale(1.2);
#             transition: transform 0.3s ease-in-out, filter 0.3s ease-in-out;
#             filter: brightness(1.6);
#         }
#     </style>

#     <div class="title-container">
#         <h1>Conversational-AI Chatbot (DialoGPT)</h1>
#         <h5 style='color: blue;'>By Ahmed Yaqoob Dhedhi</h5>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# ✅ Chat Messages - Auto-scroll will now work correctly
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = backend.run(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# # ✅ Place the icons at the bottom to avoid breaking auto-scroll
# st.markdown(
#     """
#     <div style="text-align: center; margin-top: 20px;">
#         <a href="https://github.com/HamCraft" target="_blank">
#             <img class="icon" src="https://cdn-icons-png.flaticon.com/512/733/733609.png" alt="GitHub" width="40" style="margin-right: 10px;">
#         </a>
#         <a href="https://linkedin.com/in/ahmed-yaqoob-dhedhi" target="_blank">
#             <img class="icon" src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="40">
#         </a>
#     </div>
#     """,
#     unsafe_allow_html=True
# )