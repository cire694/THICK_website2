html_content_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>College Essays Brainstorming</title>
    <link rel="stylesheet" href="../css/styles.css">
    <style>
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }}
        .textbox-container {{
            margin-bottom: 15px;
        }}
        .save-button {{
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Brainstorm Prompts</h1>
        <h2><b><i>Remember to save your responses!</i></b></h2>
        {textbox_containers}
        <button class="save-button" id="saveButton">Save</button>
    </div>

    <script>
        document.getElementById('saveButton').addEventListener('click', function() {{
            for (let i = 0; i <= 8; i++) {{
                const textarea = document.getElementById(`prompt${{i}}`);
                localStorage.setItem(`response${{i}}`, textarea.value);
            }}
            alert('Responses saved!');
        }});

        // Load saved responses on page load
        window.addEventListener('load', function() {{
            for (let i = 0; i <= 8; i++) {{
                const savedResponse = localStorage.getItem(`response${{i}}`);
                if (savedResponse) {{
                    document.getElementById(`prompt${{i}}`).value = savedResponse;
                }}
            }}
        }});
    </script>
</body>
</html>
"""

textbox_container_template = """
        <div class="textbox-container">
            <p>{prompt}</p>
            <textarea class="textbox" id="{id}" placeholder="Write your response here"></textarea>
        </div>
"""

question_prompts = [
    "Write a story that reflects you socioeconomically (poverty, immigration). <br>(<i>5 minutes</i>)",
    "Write about a memory growing up. <br>(<i>5 minutes</i>)",
    "List and tell a story about each family member / Write about your family dynamic.",
    "Write about an event that happened in elementary school that shaped you. <br>(<i>5 minutes</i>)",
    "Write about an event that happened in middle school that shaped you. <br>(<i>5 minutes</i>)",
    "Write about an event that happened in high school that shaped you. <br>(<i>5 minutes</i>)",
    "Write about a person who changed your opinion about the world. <br>(<i>5 minutes</i>)", 
    "Write about a hobby you enjoy",
    "What's your biggest regret?"
]

def generate_html_file(prompts, output_file="brainstorm.html"):
    textbox_containers = "".join(
        textbox_container_template.format(prompt=prompt, id=f"prompt{i}") for i, prompt in enumerate(prompts)
    )
    html_content = html_content_template.format(textbox_containers=textbox_containers)
    with open(output_file, "w") as file: 
        file.write(html_content)
    print(f"HTML file '{output_file}' successfully created")

if __name__ == "__main__": 
    generate_html_file(question_prompts)
