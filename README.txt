===============
zeam.form.plone
===============

``zeam.form.plone`` provides support for `zeam.form.base`_ into Plone
3.x:

- make forms and security work in Zope 2,

- default form template using Plone macros,

- provide a simple simple edit form,

- use Plone status message system to report status,

- provides extra widgets, like a WYSIWYG text widget.


Example
=======

Let's define a simple example::

   from zeam.form.plone import EditForm
   from zeam.form.base import Fields

   class EditPeople(EditForm):
       label = u"Edit people"
       fields = Fields(IPeople)
       fields['summary'].mode = 'plone.wysiwyg'

If you install the extension *Zeam Form* you will get nicer CSS and
extra JS for the widgets.

For more information information, please refer to `zeam.form.base`_
and to the Grok documentation.

.. _zeam.form.base: http://pypi.python.org/pypi/zeam.form.base

