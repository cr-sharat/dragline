.. _parser:

=========================
HTML Parser Module
=========================

Basic parser module for parsing :class:`dragline.http.Response`

HtmlParser Function
-------------------

.. autofunction:: dragline.parser.HtmlParser


.. autoclass:: dragline.parser.html.HTMLElement
    :members: extract_text,extract_urls,html_content

    .. function:: cssselect(expr)

        Select elements from this element and its children, using a CSS selector expression. (Note that .xpath(expr) is also available as on all lxml elements.)
