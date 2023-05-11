import obraz

@obraz.template_filter('eleven')
def eleven(content: str, config: str) -> str:
    return content*2