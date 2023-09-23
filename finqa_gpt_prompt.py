import openai
import os
import traceback

# Set the OpenAI API key
openai.api_key = ""

# Set the engine name
engine_name = "ft:gpt-3.5-turbo-0613:personal:finqa:81fRFXj0"


def get_user_input():
    try:
        options = [
            "Financial question answering assistant",
            "Investing advisor",
            "Other"
        ]
        print("Please choose an option:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = int(input("Enter the option number: "))
        while choice not in range(1, len(options) + 1):
            choice = int(
                input("Invalid choice. Enter a valid option number: "))

        if choice == 1:
            desired_prompt = input("Enter the prompt: ")

            context="Financial question answering assistant"
            additional_info = input("Any additional information or context? ")
            user_message = desired_prompt + ". " + additional_info + "."

        elif choice == 2:
            desired_prompt = input("Enter the prompt: ")

            context="Investing advisor"
            additional_info = input("Any additional information or context? ")
            user_message = desired_prompt + ". " + additional_info + "."


        elif choice == 3:
            context = input("Enter a Topic: ")

            desired_prompt = input("Enter the prompt: ")

            additional_info = input("Any additional information or context? ")
            user_message = desired_prompt + ". " + additional_info + "."

            

        # Define the initial role and message for the conversation
        conversation=[{"role": "system", "content": context}]
        conversation.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model=engine_name,
            messages=conversation,
            temperature=0.8,
            max_tokens=250,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response.choices[0].message.content)


        # Add the AI-generated response to the conversation
        ai_response = response.choices[0].message.content
        conversation.append({"role": "system", "content": context})

        conversation.append(
            {"role": 'assistant', "content": ai_response})
        
        while True:
            desired_prompt = input("\nTo exit, type 'exit' \n Next question: ")
            if desired_prompt == "exit":    
                break
            conversation.append({"role": "system", "content": context})
            conversation.append({"role": "user", "content": desired_prompt})
            response = openai.ChatCompletion.create(
            model=engine_name,
            messages=conversation,
            temperature=0.8,
            max_tokens=250,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
            print("\n"+response.choices[0].message.content)

            ai_response = response.choices[0].message.content
            conversation.append({"role": "system", "content": context})

            conversation.append(
                {"role": 'assistant', "content": ai_response})
            



    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()


# Call the get_user_input function
get_user_input()
