import re


class HtmlPunctuationMaker(object):
    """
    Replace common punctuation marks with proper HTML representations.
    ---        &#8212; em dash
    --         &#8211; en dash
    "" ... ""  &#8220; &#8221; opening and closing double quotes
    ' ... '    &#8216; &#8217; opening and closing single quotes
    '          &#8217; apostrophe
    """
    def __init__(self, html):
        html = html.replace('---', '&#8212;')
        html = html.replace('--', '&#8211;')

        # Possessive 's
        regex = re.compile(r"[a-zA-Z0-9]'s")
        matches = regex.findall(html)
        for c in matches:
            cc = c.replace("'", '&#8217;')
            html = html.replace(c, cc)

        # apostrophe stuff
        cont = [
            "ren't", "an't", "ouldn't", "idn't", "oesn't", "on't", "adn't",
            "asn't", "aven't", "e'd", "e'll", "e's", "'d", "'ll", "'m", "'ve",
            "sn't", "et's", "ightn't", "ustn't", "han't", "he'd", "he'll",
            "he's", "houldn't", "hat's", "here's", "hey'd", "hey'll", "hey're",
            "hey've", "e're", "e've", "eren't", "hat'll", "hat're", "hat've",
            "ho's", "ho'll", "ho're", "ho've", "ou'd", "ou'll", "ou're",
            "ou've"
        ]

        for c in cont:
            cc = c.replace("'", '&#8217;')
            html = html.replace(c, cc)

        # double quotes
        regex = re.compile(r"\"[\w\d\s\,\;\.\'\*\&\!\@\#\$\%\^\(\)\-\+\=\?]+\"")
        matches = regex.findall(html)

        for g in matches:
            gg = g.replace('"', '&#8220;', 1)
            gg = gg.replace('"', '&#8221;')
            html = html.replace(g, gg)

        # single quotes
        regex = re.compile(r'\'[\w\d\s\,\;\.\*\&\!\@\#\$\%\^\(\)\-\+\=\?]+\'')
        matches = regex.findall(html)

        for g in matches:
            gg = g.replace("'", '&#8216;', 1)
            gg = gg.replace("'", '&#8217;')
            html = html.replace(g, gg)

        self.html = html
