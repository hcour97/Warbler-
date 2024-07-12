import werkzeug
from werkzeug.security import safe_str_cmp

# Patch flask_wtf to not use safe_str_cmp
def apply_patch():
    import flask_wtf.csrf
    def safe_str_cmp(a, b):
        if len(a) != len(b):
            return False
        result = 0
        for x, y in zip(a, b):
            result |= ord(x) ^ ord(y)
        return result == 0

    flask_wtf.csrf.safe_str_cmp = safe_str_cmp

apply_patch()
