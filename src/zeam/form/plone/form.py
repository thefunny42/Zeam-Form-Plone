
import Acquisition
from Products.statusmessages.interfaces import IStatusMessage

from five import grok
from megrok import pagetemplate as pt
from zeam.form import base
from zeam.form.ztk.actions import EditAction, CancelAction
from zope.i18n.interfaces import IUserPreferredLanguages
from zope.i18n.locales import locales, LoadLocaleError
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('zeam-form-plone')


class PloneFormData(object):

    @property
    def i18nLanguage(self):
        return self.request.get('LANGUAGE', 'en')

    @apply
    def status():
        def get(self):
            return ''
        def set(self, status):
            messager = IStatusMessage(self.request)
            messager.addStatusMessage(status, type="info")
        return property(get, set)


def find_locale(request):
    envadapter = IUserPreferredLanguages(request, None)
    if envadapter is None:
        return None

    langs = envadapter.getPreferredLanguages()
    for httplang in langs:
        parts = (httplang.split('-') + [None, None])[:3]
        try:
            return locales.getLocale(*parts)
        except LoadLocaleError:
            # Just try the next combination
            pass
    else:
        # No combination gave us an existing locale, so use the default,
        # which is guaranteed to exist
        return locales.getLocale(None, None, None)


def decode_to_unicode(string):
    if not isinstance(string, str):
        return string
    try:
        return string.decode('utf-8')
    except UnicodeDecodeError:
        # Log
        return string


def convert_request_form_to_unicode(form):
    for key, value in form.iteritems():
        if isinstance(value, list):
            form[key] = [decode_to_unicode(i) for i in value]
        else:
            form[key] = decode_to_unicode(value)


class PloneForm(PloneFormData, Acquisition.Explicit):
    """Form in Plone.
    """
    grok.baseclass()
    # Inherit from Acquisition for Zope 2.

    def __init__(self, context, request):
        super(PloneForm, self).__init__(context, request)
        self.__name__ = self.__view_name__

    def __call__(self):
        if not hasattr(self.request, 'locale'):
            # This is not pretty, but no choice.
            self.request.locale = find_locale(self.request)
        convert_request_form_to_unicode(self.request.form)
        return super(PloneForm, self).__call__()


class Form(PloneForm, base.Form):
    """Generic Plone Form
    """
    grok.baseclass()
    plonePageBorder = True


class EditForm(Form):
    """Generic Plone Edit Form
    """
    grok.baseclass()
    grok.name('edit')
    grok.require('cmf.ModifyPortalContent')

    label = _(u"Edit")
    ignoreContent = False
    actions = base.Actions(
        EditAction(_(u"Save")),
        CancelAction(_(u"Cancel")))


class FormTemplate(pt.PageTemplate):
    pt.view(Form)
