import autogen 

#config_list = [{'api_key': 'sk-xxxxx', 'model': 'gpt-4'}]
config_list = [{'base_url': 'http://localhost:8000', 'model': 'gmistral-litellm'}]


llm_config = {
    "timeout": 800,
    "config_list": config_list
}

assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    code_execution_config = {
        "work_dir":"coding_mistral",
    }
)

user_proxy.initiate_chat(assistant,message="Create a python program to check if given text is palindrom and save it in a file")