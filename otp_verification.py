import random

otp_data = {}

def generate_otp():
    otp = random.randint(100000, 999999)
    return str(otp)

def send_email(email, otp):
    otp_data[email] = otp

def verify_otp(email, user_otp):
    otp = otp_data.get(email)
    if otp and otp == user_otp:
        del otp_data[email]
        return True
    return False

def otp_verification():
    email = input("Enter your email address: ")

    otp = generate_otp()
    send_email(email, otp)
    print("OTP sent to your email.")
    print("OTP:", otp)  # Display the OTP in the console

    user_otp = input("Enter the OTP received: ")

    if verify_otp(email, user_otp):
        print("OTP verification successful.")
    else:
        print("OTP verification failed.")

otp_verification()
