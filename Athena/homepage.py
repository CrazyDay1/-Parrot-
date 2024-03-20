import streamlit as st
import tempfile
import time 


from agent import agent
from transcribe import transcribe

def responses(prompt, llm_option):
    response = agent(prompt, llm_option)
    
    for word in response.split():
        yield word + " "
        time.sleep(.05)

def main():
    st.title("🏛️ Athena")
    st.write("Eis graphēn phonēs")

    uploaded_file = st.sidebar.file_uploader("Drag and drop your audio file here", type = ["wav", "mp3", "m4a"])

    model_option = st.sidebar.selectbox("☁️ Select Whisper model", ["base", "tiny", "smaller", "medium", "large"])
    llm_option = st.sidebar.selectbox("🤖 Select LLM", ["gemma", "llama2", "mistral"])


    if st.sidebar.button("Transcribe"):
        if uploaded_file is not None:
            st.sidebar.write("Debug Menu:")
            file_details = {"filename": uploaded_file.name, "size": uploaded_file.size, "type": uploaded_file.type}
            
            # Display the file details
            st.sidebar.write("File details:")
            st.sidebar.json(file_details)

            #Get the audio data from the uploaded file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                with st.spinner("🤔 Transcribing audio file..."):
                    result = transcribe(tmp_file.name, model_option)
                audio_data = tmp_file.read()


        else:
            st.error("Please upload an audio file.")

        # Transform into json format
        result_dict = {"transcription": result}

        # Display the transcription results
        st.sidebar.write("Transcription results:")
        try:
            st.sidebar.json(result_dict, expanded=True)
            print(llm_option)
            print(result)
            summary = agent(f"Summarise the the important points for me: {result}", llm_option)
            st.markdown(summary)
        except:
            st.error("Error in transcription.")
            st.write(result)

    # initialise chat history 
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display chat messages from history on app rerun
    for messages in st.session_state.messages:
        with st.chat_message(messages["role"]):
            st.markdown(messages["content"])

    # Get the user's prompt and generate a response from the agent
    prompt = st.chat_input("Speak with Athena")
    
    # Generate response from the agent
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)

        #response = agent(prompt, llm_option)
        with st.chat_message("assistant"):
            # response = st.write_stream(responses(prompt, llm_option))
            response = agent(prompt, llm_option)
            st.markdown(response)

        # Add the prompt and response to the chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": response})
    

if __name__ == "__main__":
    main()
