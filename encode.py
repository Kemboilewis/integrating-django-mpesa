import base64
import keys



def generate_password(formatted_time):
    data_to_encode = keys.business_shortcode + keys.lipa_na_mpesa_pass_key + formatted_time
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode("utf-8")

    return decoded_password
