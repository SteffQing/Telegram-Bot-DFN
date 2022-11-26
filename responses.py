
def responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("contract?", "address?", "contract", "address"):
        return """
Marketplace Contract address is at 0xa3c32c5f83d1669038baada2b17db84c7bb15cef
Qatar event Contract address is at 0x962a4663818a7E3f0d44Fc62354ee54739A9B702
        """
    if user_message in ("website link?", "website", "link", "website link"):
        return  """
Website link is at https://distant.finance
Marketplace beta is available at https://mart.distant.finance
Qatar event is available at https://qatar.distant.finance
        """
    if user_message in ("socials?", "twitter?", "socials", "twitter"):
        return "Twitter -> twitter.com/distant_finance"
    if user_message in ("medium?", "medium", "blog?"):
        return "Medium -> medium.com/@distant_finance"