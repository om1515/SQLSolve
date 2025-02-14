from google import genai
from google.genai import types

api_key = "AIzaSyAG0o2KrxbXbsdqeyZ5rz9NpWDIRTk8Rtc"

l1 = genai.Client(api_key=api_key)

sys_instruct = """You are a MySQL expert and assistant. Your task is to take a given SQL-related question and generate step-by-step MySQL commands to solve it.

Your response should include:
1. **Understanding the Problem** - Briefly explain the task in simple terms.
2. **Database & Table Creation** - Generate the necessary CREATE TABLE statements with appropriate column types.
3. **Data Insertion** - Generate realistic INSERT INTO statements with suitable sample data.
4. **Query Execution** - Write the required SQL query to achieve the desired result.
5. **Expected Output** - If applicable, describe what the expected result of the query would be.

**Formatting Rules:**
- Write clean and structured MySQL commands.
- Use ````sql` for code blocks.
- Assume relevant column types (e.g., INT for IDs, VARCHAR for names, DATE for dates, etc.).
- Use sample data that best represents the question.
- Ensure commands can be executed sequentially without errors.
- If there are multiple steps to the solution, explain each one clearly.

Your response should be **precise, structured, and fully executable** in a MySQL environment.

"""

conversation_history = []  # To keep track of past interactions

def generate_response(user_prompt):
    conversation_history.append(f"User: {user_prompt}")
    
    # Keep context manageable (limit last 5 exchanges)
    context = "\n".join(conversation_history[-5:])

    l1_response = l1.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=sys_instruct
        ),
        contents=[context]  # Send conversation history as context
    )
    
    response_text = l1_response.text
    print(f"Era: {response_text}")  # Print AI response
    
    conversation_history.append(f"Era: {response_text}")  # Store AI response

while True:
    user_prompt = input("Enter a prompt (or type 'exit' to quit): ")
    if user_prompt.lower() == 'exit':
        break
    generate_response(user_prompt)
