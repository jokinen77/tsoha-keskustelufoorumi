from flask import flash

def validateUpdatePassword(password_new, password_new_re, password_old, password_real):
    result = True

    validateStringLength(password_new, label='Password')

    if password_new != password_new_re:
        result = False
        flash("Passwords must match!")

    if password_old != password_real:
        result = False
        flash("Wrong old password!")

    return result

def validateNewUser(name, username, password, password_re, email, usertype_id):
    result = True

    if not validateStringLength(name, label='Name'):
        result = False
    if not validateStringLength(username, label='Username'):
        result = False
    if not validateStringLength(password, label='Password'):
        result = False
    if password != password_re:
        result = False
        flash("Passwords must match!")
    if not validateEmail(email):
        result = False
    if usertype_id == None:
        flash("Usertype is invalid!")
        result = False

    return result


def validateStringLength(string, label='String', min = 4, max = 255):
    if len(string) < min or len(string) > max:
        flash(label + "'s length must be between " + str(min) + "-" + str(max) + "!")
        return False
    return True

def validateNumberBetween(num, min, max, label = 'Number'):
    if num < min or num > max:
        flash(label + " must be between " + str(min) + "-" + str(max) + "!")
        return False
    return True


def validateEmail(email):
    if "@" not in email or len(email) < 3:
        flash("Invalid email address!")
        return False
    return True
