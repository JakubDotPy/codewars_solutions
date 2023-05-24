"""Kata - Evil Autocorrect Prank

completed at: 2019-05-09 09:22:08
by: Jakub Červinka

Your friend won't stop texting his girlfriend.  It's all he does. All day. Seriously.  The texts are so mushy too! The whole situation just makes you feel ill.
Being the wonderful friend that you are, you hatch an evil plot.  While he's sleeping, you take his phone and change the autocorrect options so that every time he types "you" or "u" it gets changed to "your sister."

Write a function called <code>autocorrect</code> that takes a string and replaces all instances of <code>"you"</code> or <code>"u"</code> (not case sensitive) with <code>"your sister"</code> (always lower case).

Return the resulting string.

Here's the slightly tricky part: These are text messages, so there are different forms of "you" and "u".

For the purposes of this kata, here's what you need to support:
<ul>
<li>"youuuuu" with any number of u characters tacked onto the end</li>
<li>"u" at the beginning, middle, or end of a string, but NOT part of a word</li>
<li>"you" but NOT as part of another word like youtube or bayou</li>
</ul>
<p>

"""

def autocorrect(input_string):
    import re
    pattern = r'\b(u|you+)\b'
    replacement = 'your sister'
    return re.sub(pattern, replacement, input_string, flags=re.I)
    
