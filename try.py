from openai import OpenAI

client = OpenAI(
    # api_key=os.environ[
    #     "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"
    # ],  # this is also the default, it can be omitted
    api_key="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"
)
job_qualifications = "python django developer"
job_title = "junior backend dev"
json_format = """
                    {
                    "job_title": "",
                    "job_qualifications": "",
                    "candidate1": {
                        "name":"",
                        "strengths": [],
                        "weaknesses": [],
                        "qualification_percentage": ""
                    },
                    "summary": ""
                    }
                """
candidate1 = """
PEÑA, GEORGE VINCENT B.
Tibungco, Davao City. 8000
09762031466 PROFILE
I'm an Enthusiastic, reliable, and innovative. I understand programming well, can make algorithms to solve problems, and have a genuine passion for coding. Email: gvbpena@gmail.com Portfolio: gvbpena.vercel.app TECHNICAL PROFICIENCY Web Development: HTML/CSS, Bootstrap, jQuery, React.js, Django Programing Languages: Python, JavaScript, PHP, Java, C/C++, Dart. Database: MySQL, Firebase Tools: VS Code, XAMPP, Git, Github Additional Skills: English Communication, Basic Computer Skills EXPERIENCES Jairosoft Inc, Davao City 8000. July to August 2023 INTERNSHIP I have acquired valuable skills in this internship, including Python/Django, backend development, API and AI integration, and REST APIs. The hands-on experience has been valuable for my tech journey. University of Mindanao, Davao City 8000. August 2020 to Present BS IN COMPUTER SCIENCE Earned college units in Software Engineering, Data Structures, Database Management, Robotics, and Web/Mobile Programming, gaining valuable knowledge and skills. CERTIFICATES Information Technology Specialist (Java) | Certiport – A Pearson VUE Business | June 13, 2023 Information Technology Specialist (HTML/CSS) | Certiport – A Pearson VUE Business | June 15, 2023 University of Mindanao’s Dean's Lister | S.Y 2021 – 2022 University of Mindanao’s Dean's Lister | S.Y 2020 – 2021 Certificate of Completion at Jairosoft Inc | Internship
"""


chatgpt_prompt = f"""
        Instructions:
        1. You are a very strict and meticulous human resource manager that oversee the recruitment process and thoroughly and strictly selects the job applicants who best fit the organization's requirements.
        ----------------------------------
        2. This is the resume of an applicant applying for the position of {job_title}: "{candidate1}"
        ----------------------------------
        3. Please analyze the applicant's resume 10 times, and determine how well their skills and experience match the given job qualifications below:
        {job_qualifications}
        ----------------------------------
        4. The JSON format provided below includes fields for a job title, job qualifications, a applicant's information, and a summary of the analysis:
        {json_format}
        ----------------------------------
        5. Replace the empty strings under the "job_title", "job_qualifications", and "candidate1" sections with relevant information from the job qualifications and a job applicant's resume, respectively.
        ----------------------------------
        6. For the "candidate1" section, you are required to analyze the applicant's skills and experience based on their resume, and determine their strengths and weaknesses as compared to the job qualifications.
            "name": The applicant's name.
            "strengths": A list of the applicant's strengths that align with the job qualifications make the explanation long .
            "weaknesses": A list of areas where the applicant's skills and experience may not fully match the job requirements, a list of lacking skills, or a list of lacking experience in specific areas of expertise make the explanation long .
            "qualification_percentage": A rating representing how well the applicant's skills and experience match the provided job requirements.
                Give a "Very Low" rating if the applicant's skills and experience matches only 0% to 20% of the provided job requirements and the position of {job_title}.
                Give a "Low" rating if the applicant's skills and experience matches only 21% to 39% of the provided job requirements and the position of {job_title}.
                Give an "Average" rating if the applicant's skills and experience matches only 40% to 60% of the provided job requirements and the position of {job_title}.
                Give a "High" rating if the applicant's skills and experience matches 61% to 79% of the provided job requirements and the position of {job_title}.
                Give a "Very High" rating if the applicant's skills and experience matches 80% to 100% of the provided job requirements and the position of {job_title}.
        ----------------------------------
        7. Use the provided format to summarize the analysis results in the "summary" section. This summary should highlight the applicant's suitability for the job based on their skills, experience, strengths, and areas for improvement. This should be 280 characters (Ensure that the summary provides constructive criticism of the candidate's resume to evaluate its suitability highlight whats lacking in the resume refering to the {job_title}).
        ----------------------------------
        8. After completing the JSON format, you can create a sample job listing and applicant's qualifications to populate the fields. Use your creativity to come up with realistic data for the analysis.
        ----------------------------------
        9. Make sure to complete the JSON format and leave nothing unanswered.
        """
response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": "You are a very strict and meticulous human resource manager that oversee the recruitment process and thoroughly and strictly selects the job applicants who best fit the organization's requirements.",
        },
        {"role": "user", "content": chatgpt_prompt},
    ],
)
print(response.choices[0].message.content)
