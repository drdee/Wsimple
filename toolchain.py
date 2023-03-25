from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.tools import AIPluginTool
tool = AIPluginTool.from_plugin_url("http://127.0.0.1:8000/.well-known/ai-plugin.json")

llm = ChatOpenAI(temperature=0)
tools = load_tools(["requests"] )
tools += [tool]

agent_chain = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
# agent_chain.run("Retrieve my Wealthsimple Trade account status")
agent_chain.run("Fund my Wealthsimple Trade account with $1")

