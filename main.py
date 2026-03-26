import anthropic


# create ClaudeAgent class
class ClaudeAgent:
    def __init__(self):
        self.client = anthropic.Anthropic()

    # func to get user input
    def get_message(self):
        user_input = input()
        return user_input, bool(user_input)

    def run(self):
        pass    

def main():
    claude_agent = ClaudeAgent()
    claude_agent.run()

if __name__ == "__main__":
    main()
