from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, Optional

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a real secret key



class FeedbackForm(FlaskForm):
    # Personal Information
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    # General Experience
    overall_satisfaction = SelectField('Overall Satisfaction (1-10)', choices=[(str(i), str(i)) for i in range(1, 11)], validators=[DataRequired()])
    event_organization = SelectField('Event Organization (1-10)', choices=[(str(i), str(i)) for i in range(1, 11)], validators=[DataRequired()])
    met_expectations = RadioField('Did the hackathon meet your expectations?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])

    # Specific Aspects
    venue_rating = SelectField('Venue and Facilities Rating (1-10)', choices=[(str(i), str(i)) for i in range(1, 11)], validators=[DataRequired()])
    schedule_convenience = RadioField('Was the schedule convenient for you?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    workshops_quality = SelectField('Workshops and Talks Quality (1-10)', choices=[(str(i), str(i)) for i in range(1, 11)], validators=[DataRequired()])
    mentorship_quality = SelectField('Mentorship Quality (1-10)', choices=[(str(i), str(i)) for i in range(1, 11)], validators=[DataRequired()])

    # Team Experience
    team_experience = SelectField('Team Formation and Dynamics (1-10)', choices=[(str(i), str(i)) for i in range(1, 11)], validators=[DataRequired()])
    collaboration_tools_effectiveness = RadioField('Were collaboration tools effective?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])

    # Project and Learning
    project_satisfaction = SelectField('Project Implementation Satisfaction (1-10)', choices=[(str(i), str(i)) for i in range(1, 11)], validators=[DataRequired()])
    learning_experience = RadioField('Did you learn something new?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    challenge_level = SelectField('Challenge Level', choices=[('easy', 'Too Easy'), ('just_right', 'Just Right'), ('difficult', 'Too Difficult')], validators=[DataRequired()])

    # Networking and Community
    networking_opportunities = SelectField('Networking Opportunities (1-10)', choices=[(str(i), str(i)) for i in range(1, 11)], validators=[DataRequired()])
    community_building = RadioField('Did the event help in community building?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])

    # Feedback and Suggestions
    highlights = TextAreaField('Event Highlights', validators=[Optional()])
    areas_for_improvement = TextAreaField('Areas for Improvement', validators=[Optional()])
    additional_comments = TextAreaField('Additional Comments', validators=[Optional()])

    # Personal and Demographic Information
    role = RadioField('Your Role', choices=[('participant', 'Participant'), ('mentor', 'Mentor'), ('organizer', 'Organizer'), ('sponsor', 'Sponsor')], validators=[DataRequired()])
    experience_level = RadioField('Your Experience Level in Hackathons', choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], validators=[DataRequired()])

    # Follow-Up
    future_participation = RadioField('Interested in future events?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    contact_for_future_events = RadioField('Can we contact you for future events?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])

    # Submit Button
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FeedbackForm()
    if form.validate_on_submit():
        # Example: print the data to the console
        print("Name:", form.name.data)
        print("Email:", form.email.data)
        print("Rating:", form.rating.data)
        print("Feedback:", form.feedback.data)
        # Add your logic to handle the form data (e.g., save to database)
        pass
    return render_template('index.html', form=form)

@app.route('/powerbi', methods=['GET'])
def powerbi():
    return render_template('powerbi.html')

if __name__ == '__main__':
    # run flaks app open to the world on port 5000
    app.run(host='0.0.0.0', port=5000)
