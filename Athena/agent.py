from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import (
    ChatMessagePromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate
)

def agent(prompt, model):
    llm = Ollama(model=model,
                    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
                    )
    
    return llm.invoke(prompt)
