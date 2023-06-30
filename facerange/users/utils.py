import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from facerange import mail


def save_picture(form_picture):
    # Creates a random title for the uploaded image.
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics/', picture_fn)
    # Re-sizes the uploaded image to 125 x 125 pixels
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    # Saves the picture
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset', sender='noreply@facerange.com', recipients=[user.email])
    msg.body = f'''Please click on the following link to reset your password:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request, please disregard this email and no changes will be made. 
'''
    mail.send(msg)
