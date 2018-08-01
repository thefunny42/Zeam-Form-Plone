import os
import Acquisition

from five import grok
from zope.globalrequest import getRequest
from zeam.form.base.widgets import FieldWidget
from zeam.form.ztk.widgets.choice import ChoiceField
import zeam.form.ztk.widgets.collection
from zeam.form.ztk.widgets.collection import (
    CollectionField, newCollectionWidgetFactory,
    MultiChoiceFieldWidget)
from zeam.form.ztk import widgets as zeam_ztk
from zeam.form.ztk.widgets.text import TextField
from zeam.form.base.interfaces import IWidget
from zeam.form.ztk.interfaces import ICollectionField
from zope.interface import Interface
from Products.CMFPlone.resources import add_resource_on_request


zeam_ztk_path = os.path.join(
    os.path.dirname(zeam_ztk.__file__),
    'static')


class ZeamZTKResources(grok.DirectoryResource):
    grok.path(zeam_ztk_path)
    grok.name('zeam_form_ztk_widgets')


class Resources(grok.DirectoryResource):
    grok.path('resources')
    grok.name('zeam_form_plone_resources')


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


# Plone 4 includes the resources by default
# Plone 5 doesn't, so we have to inject them in the request.
# This doesn't alter Plone 4 behavior.

RESOURCES = (
    "resource-zeam_form_plone_resources-widgets-css",
    "resource-zeam_form_ztk_widgets-collection-js",
    "resource-zeam_form_plone_resources-json-template",
    "resource-zeam_form_plone_resources-widgets-js",
)


def resources_include():
    request = getRequest()
    for resource in RESOURCES:
        add_resource_on_request(request, resource)


zeam.form.ztk.widgets.collection.requireCollectionResources = resources_include
