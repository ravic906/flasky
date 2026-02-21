from google import genai

client = genai.Client(api_key="AIzaSyAcm_iysylKKzhEo1gTVgXQMxrH7KaSgwk")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Can you read a sql or python file and create documentation?"
)
print(response.text)