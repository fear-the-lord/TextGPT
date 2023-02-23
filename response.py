import requests
import openai

def message(username, recruiter_name, company_name, job_role):
        # Define OpenAI API key 
    # openai.api_key = "api-key"

    # # Set up the model and prompt
    # model_engine = "text-davinci-003"
    # prompt = "Ask for a referral for myself {} to a recruiter named {} for the job role {} at {}.".format(username, recruiter_name, job_role, company_name)
    # # prompt = "Hello"
    # # Generate a response
    # completion = openai.Completion.create(
    #     engine=model_engine,
    #     prompt=prompt,
    #     max_tokens=2048,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )

    # response = completion.choices[0].text
    # Use dummy text while testing
    response = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec mi nisi, egestas at felis ac, pellentesque molestie mauris. Vivamus tempor justo vel nunc ornare ornare. Nulla eu fermentum risus, vitae porttitor elit. Duis urna sem, interdum id laoreet non, aliquam nec velit. Duis venenatis ut libero quis tempus. Duis volutpat pretium consectetur. Etiam pharetra massa nec ipsum blandit blandit. Vestibulum in vehicula justo. Maecenas feugiat tempus est, eget rutrum eros ornare ac. Aenean sit amet semper lectus. Praesent mollis sapien eget risus suscipit commodo. Vivamus vitae nulla quis augue convallis dapibus. Quisque varius luctus neque, vel consequat velit pellentesque sed. Cras vitae nibh suscipit, lobortis tortor euismod, mollis tortor. Maecenas vel velit eget libero sollicitudin gravida ut eu ante. Vivamus consequat in ligula quis efficitur. Maecenas porta nulla ac mauris lacinia, vitae auctor mauris semper. Morbi egestas elit et gravida porttitor. Nam sollicitudin neque interdum mauris accumsan efficitur. Nulla aliquam, nunc eget fermentum eleifend, eros lacus mattis lacus, id ullamcorper metus augue in diam. Integer tempus ante iaculis dui vulputate auctor. Vivamus vel odio non leo porta porttitor. Aliquam a quam tortor. Ut mi mauris, gravida id nulla et, facilisis accumsan lorem. Nam et orci iaculis, elementum lorem quis, faucibus enim. Duis pulvinar eget orci a euismod. Suspendisse in nibh odio. Phasellus nec arcu vel nisl pretium feugiat."
    print(response)
    return response
