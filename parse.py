import openai

def parse_resume_to_json(resume_content):
    prompt = (
        "Take the following resume content and parse it into JSON format. The JSON should include sections like "
        "'Personal Information', 'Education', 'Experience', 'Skills', and 'Projects'. Each section should be structured "
        "with relevant details such as dates, roles, and descriptions.\n\n"
        f"Resume Content:\n{resume_content}"
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )

    return response.choices[0].text.strip()

resume_content = """
[Paste your resume content here]
"""

parsed_resume = parse_resume_to_json(resume_content)
print(parsed_resume)
