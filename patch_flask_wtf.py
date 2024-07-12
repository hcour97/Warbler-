# patch_flask_wtf.py

def apply_patch():
    import flask_wtf.recaptcha.widgets

    # Patch for safe_str_cmp
    import flask_wtf.csrf
    from functools import wraps

    def safe_str_cmp(a, b):
        return a == b

    flask_wtf.csrf.safe_str_cmp = safe_str_cmp

    # Patch for url_encode
    from werkzeug.urls import url_encode as werkzeug_url_encode

    # Define url_encode function
    def url_encode(d, charset='utf-8', encode_keys=False):
        return werkzeug_url_encode(d, charset=charset, encode_keys=encode_keys)

    flask_wtf.recaptcha.widgets.url_encode = url_encode

apply_patch()


