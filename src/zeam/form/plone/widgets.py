
import Acquisition

from five import grok
from zope.interface import Interface
from zeam.form.base.widgets import FieldWidget
from zeam.form.ztk.widgets.text import TextSchemaField


class PloneFieldWidget(FieldWidget, Acquisition.Explicit):
    grok.baseclass()

    @property
    def context(self):
        # Plone Zope 2 template need a context.
        return self.form.context


class PloneWYSIWYGFieldWidget(PloneFieldWidget):
    grok.adapts(TextSchemaField, Interface, Interface)
    grok.name('plone.wysiwyg')
