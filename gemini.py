from google import genai

client = 

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Can you read a sql or python file and create documentation?"
)

print(response.text)
