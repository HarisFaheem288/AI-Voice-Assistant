import ollama

def generate_response(user_text: str):

    response = ollama.chat(
        model='llama3',
        messages=[
            {
                'role': 'user',
                'content': user_text
            }
        ]
    )

    return response['message']['content']