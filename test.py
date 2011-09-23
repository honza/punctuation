string = """
This is a test string. It should cover as many screnations as possible.

If you find a bug, please add an example text here and then make this text
pass.

Test starts bellow:

high-profile high-speed
1900--1910
Nevada--California

We were walking down the street and---bam!

don't can't won't doesn't shouldn't couldn't wouldn't

My mom said: "You cannot smile."
And I replied: "You're wrong."

This is what you call 'closure'.

She said: "This is what you call 'closure'."

Joe's bike. Peter's Dad.
"""

reference = """
This is a test string. It should cover as many screnations as possible.

If you find a bug, please add an example text here and then make this text
pass.

Test starts bellow:

high-profile high-speed
1900&#8211;1910
Nevada&#8211;California

We were walking down the street and&#8212;bam!

don&#8217;t can&#8217;t won&#8217;t doesn&#8217;t shouldn&#8217;t couldn&#8217;t wouldn&#8217;t

My mom said: &#8220;You cannot smile.&#8221;
And I replied: &#8220;You&#8217;re wrong.&#8221;

This is what you call &#8216;closure&#8217;.

She said: &#8220;This is what you call &#8216;closure&#8217;.&#8221;

Joe&#8217;s bike. Peter&#8217;s Dad.
"""

from punctuation import HtmlPunctuationMaker


rendered = HtmlPunctuationMaker(string).html
assert(rendered==reference)
