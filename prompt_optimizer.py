# AI Prompt Optimizer Tool
# Created by M. Danush Kumar
# Helps improve prompts for better AI responses

def optimize_prompt(user_prompt):
    print("\n=== AI Prompt Optimizer ===\n")
    print(f"Original Prompt:\n{user_prompt}\n")
    
    # Improved prompt with best practices
    improved = f"""You are a highly intelligent, truthful, and helpful AI assistant.
    
User request: {user_prompt}

Please provide a clear, detailed, accurate, and well-structured response.
Use step-by-step reasoning when appropriate.
Be honest if you are unsure about something.
"""
    
    print(f"Optimized Prompt:\n{improved}")
    print("\nThis optimized prompt will usually give much better results from Grok or any other AI!")

# Main program
if _name_ == "_main_":
    print("Welcome to AI Prompt Optimizer!")
    print("Type your prompt below and I will improve it for you.\n")
    
    user_input = input("Enter your prompt: ")
    optimize_prompt(user_input)
