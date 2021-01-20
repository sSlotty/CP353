from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class BmiForm(FlaskForm):
    """Contact form."""
    height = NumberField(
        'height',
        [DataRequired()]
    )
    weight = NumberField(
        'weight',
        [
            Email(message=('Not a valid email address.')),
            DataRequired()
        ]
    )
    
    submit = SubmitField('Submit')