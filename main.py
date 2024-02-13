import streamlit as st

st.title('CHATBOT')

prompt = st.chat_input("What's on your mind?")

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	user_input = st.chat_message(message['role'])
	user_input.write(message['content'])

st.chat_message("user").write(prompt)

if prompt and prompt != '':
	st.session_state.messages.append({'role': 'user', 'content': prompt})

if prompt == 'Hello':
	st.chat_message("assistant").write("How are you?")
	st.session_state.messages.append({'role': 'assistant', 'content': 'How are you?'})
elif prompt == 'Who are you?':
	st.chat_message('assistant').write('I am your assistant')
	st.session_state.messages.append({'role': 'assistant', 'content': 'I am your assistant'})
elif prompt == 'Hi':
	st.chat_message('assistant').write('Hello!')
	st.session_state.messages.append({'role': 'assistant', 'content': 'Hello!'})
elif prompt == 'ano ginagawa mo?':
	st.chat_message('assistant').write('eto nagcocode')
	st.session_state.messages.append({'role': 'assistant', 'content': 'eto nagcocode'})
elif prompt == '':
	st.chat_message('assistant').write('Hello!')
	st.session_state.messages.append({'role': 'assistant', 'content': 'Hello!'})
elif prompt == 'Hi':
	st.chat_message('assistant').write('Hello!')
	st.session_state.messages.append({'role': 'assistant', 'content': 'Hello!'})

