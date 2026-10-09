from flask import Flask, render_template, request

app = Flask(__name__)


STUDY_MODES = {
    "coding": {
        "title": "Coding Practice",
        "description": (
            "A practical study session focused on solving, "
            "testing and reviewing code."
        ),
        "steps": [
            "Choose one small programming problem related to the topic.",
            "Write a solution without checking an existing answer first.",
            "Test the solution using at least three different inputs.",
            "Review any errors and improve the implementation.",
            "Write a short note describing what was learned."
        ]
    },

    "reading": {
        "title": "Focused Reading",
        "description": (
            "A structured reading session designed to improve "
            "understanding of technical material."
        ),
        "steps": [
            "Read the selected topic once without taking notes.",
            "Read it again and identify the main concepts.",
            "Record unfamiliar technical terms.",
            "Summarise the main idea using your own words.",
            "Create two questions to review the topic later."
        ]
    },

    "revision": {
        "title": "Revision Session",
        "description": (
            "A recall-based session for reviewing and strengthening "
            "previous learning."
        ),
        "steps": [
            "Write down everything remembered about the topic.",
            "Compare the recalled information with existing notes.",
            "Identify important concepts that were missed.",
            "Review only the areas that require improvement.",
            "Finish by creating three short revision questions."
        ]
    }
}


@app.route("/", methods=["GET", "POST"])
def home():
    subject = ""
    selected_mode = "coding"
    plan = None

    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        selected_mode = request.form.get("mode", "coding")

        if selected_mode not in STUDY_MODES:
            selected_mode = "coding"

        if subject:
            plan = STUDY_MODES[selected_mode]

    return render_template(
        "index.html",
        subject=subject,
        selected_mode=selected_mode,
        modes=STUDY_MODES,
        plan=plan
    )


@app.route("/health")
def health():
    return {
        "application": "StudySprint",
        "service": "task4-3-webapp",
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )