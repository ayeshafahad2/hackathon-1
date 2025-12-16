---
labels:
  - "feature: urdu-translation-agent"
  - "action: task-definition"
---

# Tasks for Urdu Translation Agent

1.  **Analyze existing content:**
    -   Identify all markdown files (`.md`) in the `docs` directory that need to be translated.
    -   Determine the structure of the content to be translated.

2.  **Set up translation environment:**
    -   Research and select a suitable machine translation service or library that supports English to Urdu translation.
    -   Obtain any necessary API keys or credentials and configure them securely.

3.  **Develop the translation script:**
    -   Create a script that can read the content of a markdown file.
    -   Implement the logic to send the text content to the translation service.
    -   Process the translated response and handle any potential errors.

4.  **Integrate and create new files:**
    -   Create a new directory structure for the Urdu localization (e.g., `docs/ur`).
    -   The script should write the translated content into new markdown files, preserving the original file names but placing them in the new localization directory.
    -   Ensure that frontmatter and code blocks are handled correctly and not translated.

5.  **Testing:**
    -   Add a small sample file to test the translation process.
    -   Verify that the output is a valid markdown file with translated content.
    -   Manually review a sample of the translated text for quality.

6.  **Documentation:**
    -   Update the project's documentation to explain how to use the translation agent.
