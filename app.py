import openai
from bottle import route,response, run, template, request
openai.api_key = "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"


@route('/')
def home():
    return '''
        <form action="/chat" method="post">
            Message: <input name="message" type="text" />
            <input value="Chat" type="submit" />
        </form>
    '''

# Define a route for handling chat requests
@route('/chat', method='POST')
def chat():
    # Get the user's message from the request
    message = request.forms.get('message')

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        best_of=4,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the response text from the API response
    response_text = response.choices[0].text.strip()
    response_arr = list(filter(None,[lines for lines in response.choices[0].text.splitlines()]))

    # Return the response to the user
    print(response_arr)
    return '''
        <p>You: {}</p>
        <p>ChatGPT3: {}</p>
        <p><a href="/">Back</a></p>
    '''.format(message, response_text)

# Run the Bottle app
if __name__ == '__main__':
    run(host='localhost', port=8089, debug=True, reloader=True)
