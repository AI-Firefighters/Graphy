from langchain_community.tools import DuckDuckGoSearchResults, DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

wrapper = DuckDuckGoSearchAPIWrapper(region="wt-wt", time="d", max_results=5)

search = DuckDuckGoSearchResults(api_wrapper=wrapper)

tools = [search]