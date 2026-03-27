import anthropic
from termcolor import colored

# create ClaudeAgent class
class ClaudeAgent:
    def __init__(self):
        self.client = anthropic.Anthropic()

    # func to get user input
    def get_message(self):
        try:
            user_input = input()
            return user_input, bool(user_input)
        except EOFError as e:
            return "", str(e)

    # here we will have a loop that gets a task and keeps running until the task is complete
    def run(self):
        print("Hello! I'm Claude, your AI assistant. How can I help you today?")    
        conversation = []

        while True:
            print(colored('You: ', 'blue'), end='')
            
            user_input, ok = self.get_message()
            if not ok:
                break
            
            # add user input to conversation
            user_msg = {
                "role": "user",
                "content": [{"type": 'text', "text": user_input}]
            }
            conversation.append(user_msg)

            # send the context(conversation history) and the new user message to LLM model, and get the response
            message = self.run_inference(conversation)
            
            # add the response to conversation
            conversation.append({'role': 'assistant', 'content': message.content})

            for content in message.content:
                if content.type == 'text':
                    print(colored("Claude: ", 'yellow'), f" {content.text}")
    
    # call Anthropic model and return model response
    def run_inference(self, conversation):
        return self.client.messages.create(
            model='claude-haiku-4-5', max_tokens=1024, messages=conversation        
        )

def main():
    claude_agent = ClaudeAgent()
    claude_agent.run()

if __name__ == "__main__":
    main()
