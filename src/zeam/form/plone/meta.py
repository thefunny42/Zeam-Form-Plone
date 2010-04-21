
from five.grok.meta import ViewSecurityGrokker
from zeam.form.plone import form
import martian


class FormSecurityGrokker(ViewSecurityGrokker):
    """We want to set Zope 2 security on Forms
    """
    martian.component(form.PloneForm)
