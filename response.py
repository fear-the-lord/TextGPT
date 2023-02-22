import requests
import openai

def message(username, recruiter_name, company_name, job_role):
        # Define OpenAI API key 
    openai.api_key = "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"

    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = "Ask for a referral for myself {} to a recruiter named {} for the job role {} at {}.".format(username, recruiter_name, job_role, company_name)
    # prompt = "Hello"
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    print(response)
    return response
