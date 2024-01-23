import autogen 

config_list = [{'api_key': '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', 'model': 'gpt-4'}]


llm_config = {
    "config_list": config_list
}

assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    code_execution_config = {
        "work_dir":"coding_openai",
    }
)

user_proxy.initiate_chat(assistant,message="Create a python program to check if given text is palindrom and save it in a file")