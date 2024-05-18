# Feedback Form Web App

This folder contains a Flask web application for collecting feedback from participants of hackathons. The application includes a feedback form with various fields to gather information about the participant's experience, satisfaction, and suggestions.

## Installation

1. Clone this repository.
2. Install the required dependencies by running `pip install flask flask-wtf`.

## Usage

1. Run the Flask application by executing `python app.py`.
2. Access the feedback form by visiting `http://localhost:5000/` in your web browser.
3. Fill out the form with your feedback and submit it.
4. Optionally, you can explore the PowerBI dashboard by visiting `http://localhost:5000/powerbi`.

## Feedback Form Fields

- Personal Information
- General Experience
- Specific Aspects
- Team Experience
- Project and Learning
- Networking and Community
- Feedback and Suggestions
- Personal and Demographic Information
- Follow-Up

## Form Submission

Upon submitting the form, the data will be printed to the console. You can customize the logic in the `index` function to handle the form data as needed.

## Files

- `app.py`: Contains the Flask application code.
- `index.html`: HTML template for the feedback form.
- `powerbi.html`: HTML template for the PowerBI dashboard.

## Contact

For any issues or questions, please contact yours truly -jasontt33