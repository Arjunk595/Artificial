import random 
 
# define the possible user inputs and corresponding chatbot responses 
responses = { 
    "hi": ["Hello!", "Hi there!", "Hi, how can I help you?"], 
    "hello": ["Hello there!", "Hi! How can I assist you today?"], 
    "how are you": ["I'm doing well, thank you. How about you?",  
                   "I'm great, thanks for asking! How can I assist you?"], 
    "what's your name": ["My name is Chatbot. How may I assist you?",  
                        "I'm Chatbot. How can I help you today?"], 
    "goodbye": ["Goodbye!", "Have a great day!"], 
    "default": ["Sorry, I didn't understand your question. Can you please rephrase?",  
               "I'm not sure what you mean. Can you please clarify?"], 
} 
 
# define a function to generate a chatbot response based on user input 
def generate_response(user_input): 
    # convert user input to lowercase for easy matching 
    user_input = user_input.lower() 
    # find a response for the user input, or use a default response if not found 
    chatbot_response = responses.get(user_input, responses["default"]) 
    # randomly select a response from the possible options 
    return random.choice(chatbot_response) 
 
# main program loop 
while True: 
    # get user input 
    user_input = input("You: ") 
# generate chatbot response based on user input 
    chatbot_response = generate_response(user_input) 
# print chatbot response 
    print("Chatbot:", chatbot_response) 
# exit loop if user says goodbye 
    if user_input.lower() == "goodbye": 
        break 