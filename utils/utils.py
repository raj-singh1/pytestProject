# CONSTANTS
import inspect

url = "https://www.flipkart.com/"
email = "8097881727"
password = "Quark@123"


def whoami():
    return inspect.stack()[1][3]
