Punctuation
===========

`punctuation` is a Python utility that converts common punctuation markers in a
string of text into proper HTML entities.



    Source     HTML entity            Description
    ----------------------------------------------------------------------
    ---        &#8212;                 em dash
    --         &#8211;                 en dash
    "" ... ""  &#8220; and &#8221;     opening and closing double quotes
    ' ... '    &#8216; and &#8217;     opening and closing single quotes
    '          &#8217;                 apostrophe


Installation
------------

Install with pip:

    $ pip install punctuation

Or, the latest from Github:

    $ pip install -e git+git://github.com/honza/punctuation.git#egg=punctuation


Usage
-----

Command line utility:


    $ punctuation path/to/file.html

Or, API:

    from punctuation import HtmlPunctuationMaker

    string = "This is a test---that's right"
    html = HtmlPunctuationMaker(string).html
    print html
    >>>
    "This is a test&#8212;that&#8217;s right"


Credits
-------

The recommendations and entity characters come from the excellent [The Trouble
With EM & EN (and Other Shady Characters)][1] article.

License
-------

BSD, short and sweet.


[1]: http://www.alistapart.com/articles/emen/
