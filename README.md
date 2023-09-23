# finqa_gpt_35_turbo
Example of finetuning gpt 3.5 turbo for financial topics. FinQA dataset was used to prepare financial data.

## Usage
Repo contains 3 files: finqa_gpt_prompt.py, finqa_to_openai.ipynb and openai_train.ipynb

- finqa_to_openai.ipynb is a notebook, which is convering json from finqa dataset into data suitable for openai gpt finetuning
- openai_train.ipynb is a notebook, to finetune gpt 3.5 using data generated in finqa_to_openai
- finqa_gpt_prompt.py is a scipt with simple prompt highlighting best features of finetuned model

  To use notebooks and scripts you have to generate openai api key

## Model and dataset

- FinQA is a large-scale dataset with 2.8k financial reports for 8k Q&A pairs to study numerical reasoning with structured and unstructured evidence. Data is structured in json files,  one for training and another for testing purposes.
- GPT-3.5 models can understand and generate natural language or code. The most capable and cost effective model in the GPT-3.5 family is gpt-3.5-turbo which has been optimized for chat using the Chat completions API but works well for traditional completions tasks as well.

