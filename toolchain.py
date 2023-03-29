from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.tools import AIPluginTool
from langchain.callbacks import get_openai_callback
tool = AIPluginTool.from_plugin_url("http://127.0.0.1:8000/.well-known/ai-plugin.json")

llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
tools = load_tools(["requests"] )
tools += [tool]

agent_chain = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
# agent_chain.run("Retrieve my Wealthsimple Trade account status using the API on http://127.0.0.1:8000")

with get_openai_callback() as cb:
	agent_chain.run("Fund my Wealthsimple Trade account with $1 using the API on http://127.0.0.1:8000 and use as action the WSTrade plugin")
	#agent_chain.run("What stock has the highest return in the last 30 days using Wealthsimple Trade API")
