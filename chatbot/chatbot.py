from probability import get_response

while True:
    if input('You: ').strip() == 'exit':
        break
    print('Bot: '+ get_response(input('You: ')))