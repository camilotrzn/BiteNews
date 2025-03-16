from openai import OpenAI

class summarizer:

    def __init__(self):
        pass
    
    def get_summary(self,content):

        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
        )

        completion = client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-r1:free",
        messages=[
            {
            "role": "user",
            "content": f"Summarize this: {content}"
            }
        ]
        )

        return completion.choices[0].message.content 

if __name__ == "__main__":

    word = "Python is a programming language that is interpreted, object-oriented, and considered to be high-level too. What is Python? Python is one of the easiest yet most useful programming languages which is widely used in the software industry. People use Python for Competitive Programming, Web Development, and creating software. Due to its easiest syntax, it is recommended for beginners who are new to the software engineering field. Its demand is growing at a very rapid pace due to its vast use cases in Modern Technological fields like Data Science, Machine learning, and Automation Tasks. For many years now, it has been ranked among the top Programming languages."

    dp_r1 = summarizer()

    response = dp_r1.get_summary(content = word)

    print(response)



