# `cssminx`

This is a fork of a Python port of the [YUI CSS Compressor][yuicompressor]. Install it:

Use it from the command-line:

    $ cssminx --help
    $ cat file1.css file2.css file3.css | cssminx > output.min.css
    $ cssminx --wrap 1000 < input.css > output.css

Or use it from Python:

    >>> import cssminx
    >>> output = cssminx.cssminx(open('input.css').read())
    >>> print output
