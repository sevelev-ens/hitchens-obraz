import obraz
import hashlib

@obraz.template_filter('sha1')
def sha1(content: str, config: str) -> str:
    return str(hashlib.sha1(content.encode('utf-8')))