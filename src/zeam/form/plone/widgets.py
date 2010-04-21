
import Acquisition

from five import grok
from zeam.form.base.widgets import FieldWidget
from zeam.form.ztk.widgets.choice import ChoiceSchemaField
from zeam.form.ztk.widgets.collection import (
    CollectionSchemaField, newCollectionWidgetFactory, MultiChoiceFieldWidget)
from zeam.form.ztk.widgets.text import TextSchemaField
from zeam.form.base.interfaces import IWidget
from zeam.form.ztk.interfaces import ICollectionSchemaField
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
    grok.adapts(TextSchemaField, Interface, Interface)
    grok.name('plone.wysiwyg')


grok.global_adapter(
    newCollectionWidgetFactory(mode='plone.multi-select'),
    adapts=(ICollectionSchemaField, Interface, Interface),
    provides=IWidget,
    name='plone.multi-select')


class PloneMultiSelectFieldWidget(MultiChoiceFieldWidget, PloneFieldWidget):
    grok.adapts(CollectionSchemaField, ChoiceSchemaField, Interface, Interface)
    grok.name('plone.multi-select')
