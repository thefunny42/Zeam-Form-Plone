
import Acquisition

from five import grok
from zeam.form.base.widgets import FieldWidget
from zeam.form.ztk.widgets.choice import ChoiceField
from zeam.form.ztk.widgets.collection import (
    CollectionField, newCollectionWidgetFactory, MultiChoiceFieldWidget)
from zeam.form.ztk.widgets.text import TextField
from zeam.form.base.interfaces import IWidget
from zeam.form.ztk.interfaces import ICollectionField
from zope.interface import Interface


class Resources(grok.DirectoryResource):
    grok.path('resources')
    grok.name('zeam.form.plone.resources')


class PloneFieldWidget(FieldWidget, Acquisition.Explicit):
    grok.baseclass()

    @property
    def context(self):
        # Plone Zope 2 template need a context.
        return self.form.context


class PloneWYSIWYGFieldWidget(PloneFieldWidget):
    grok.adapts(TextField, Interface, Interface)
    grok.name('plone.wysiwyg')


grok.global_adapter(
    newCollectionWidgetFactory(mode='plone.multi-select'),
    adapts=(ICollectionField, Interface, Interface),
    provides=IWidget,
    name='plone.multi-select')


class PloneMultiSelectFieldWidget(MultiChoiceFieldWidget, PloneFieldWidget):
    grok.adapts(CollectionField, ChoiceField, Interface, Interface)
    grok.name('plone.multi-select')
