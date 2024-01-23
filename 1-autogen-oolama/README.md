# AutoGen  + LiteLLM + Mistral running in Google Colab(with oolama + ngrok)
Step 1
Run the Notebook in Colab

[Open In Colab](https://colab.research.google.com/drive/1pF8ZcKv9hHSY0T06Ux9wDlVSr26PeqZ1?usp=sharing)

Step 2:

Install the Lite LLM

Create the Config.Yaml

Update the url of where the llm running in config.yaml

start the litellm with below command
`litellm --config config.yaml`

Open seperate terminal and verify with curl
in windows

curl --location "http://localhost:8000/chat/completions" --header "Content-Type: application/json" --data "{ \"model\": \"gmistral-litellm\", \"messages\": [ { \"role\": \"user\", \"content\": \"what llm are you\" } ] }"

for mac

curl --location "http://localhost:8000/chat/completions" \ --header "Content-Type: application/json" \
--data '{ "model": "gmistral-litellm", "messages": [ { "role": "user", "content": "what llm are you" } ] }'

Step 3:

Install the Autogen

Update the app.py with the model details

Now run the Autogen 

`python app.py`