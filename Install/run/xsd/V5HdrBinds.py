# .\V5HdrBinds.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4c1dd66cd60ae440ea010268fe889c54a5ea0bc3
# Generated 2016-08-21 08:25:54.762000 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://www.multispeak.org/V5.0/ws/request

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8c91c870-67b3-11e6-a61b-cf944fb51eae')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _prim as _ImportedBinding__prim
import pyxb.binding.datatypes
import _com as _ImportedBinding__com
import _enum as _ImportedBinding__enum

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.multispeak.org/V5.0/ws/request', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {http://www.multispeak.org/V5.0/ws/request}MultiSpeakRequestMsgHeader with content type ELEMENT_ONLY
class MultiSpeakRequestMsgHeader_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/ws/request}MultiSpeakRequestMsgHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiSpeakRequestMsgHeader')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 20, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/ws/request}MultiSpeakVersion uses Python identifier MultiSpeakVersion
    __MultiSpeakVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MultiSpeakVersion'), 'MultiSpeakVersion', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__httpwww_multispeak_orgV5_0wsrequestMultiSpeakVersion', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 22, 3), )

    
    MultiSpeakVersion = property(__MultiSpeakVersion.value, __MultiSpeakVersion.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/ws/request}Caller uses Python identifier Caller
    __Caller = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Caller'), 'Caller', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__httpwww_multispeak_orgV5_0wsrequestCaller', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 23, 3), )

    
    Caller = property(__Caller.value, __Caller.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/ws/request}CodedNames uses Python identifier CodedNames
    __CodedNames = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CodedNames'), 'CodedNames', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__httpwww_multispeak_orgV5_0wsrequestCodedNames', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 24, 3), )

    
    CodedNames = property(__CodedNames.value, __CodedNames.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/ws/request}CoordinateSystemInformation uses Python identifier CoordinateSystemInformation
    __CoordinateSystemInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CoordinateSystemInformation'), 'CoordinateSystemInformation', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__httpwww_multispeak_orgV5_0wsrequestCoordinateSystemInformation', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 25, 3), )

    
    CoordinateSystemInformation = property(__CoordinateSystemInformation.value, __CoordinateSystemInformation.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/ws/request}DataSetState uses Python identifier DataSetState
    __DataSetState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetState'), 'DataSetState', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__httpwww_multispeak_orgV5_0wsrequestDataSetState', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 26, 3), )

    
    DataSetState = property(__DataSetState.value, __DataSetState.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/ws/request}DoNotReply uses Python identifier DoNotReply
    __DoNotReply = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DoNotReply'), 'DoNotReply', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__httpwww_multispeak_orgV5_0wsrequestDoNotReply', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 27, 3), )

    
    DoNotReply = property(__DoNotReply.value, __DoNotReply.set, None, 'This element has been added so that a subscriber may specify to a publisher that subsequent notification messages should be suppressed for notifications that result solely from handling the payload of this message.  It should be noted that support for this request is optional, but suggested, on all publishers.')

    
    # Attribute DefaultRegisteredName uses Python identifier DefaultRegisteredName
    __DefaultRegisteredName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DefaultRegisteredName'), 'DefaultRegisteredName', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__DefaultRegisteredName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __DefaultRegisteredName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 33, 2)
    __DefaultRegisteredName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 33, 2)
    
    DefaultRegisteredName = property(__DefaultRegisteredName.value, __DefaultRegisteredName.set, None, 'For all objectRefs in this message, this is the default registeredName.  This name is part of an optional dotted-quad notation that may be used when necessary to create unique object identifers.  The fully-qualified name is of the form of RegisteredName.SystemName.NounType.objectGUID.')

    
    # Attribute DefaultSystemName uses Python identifier DefaultSystemName
    __DefaultSystemName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DefaultSystemName'), 'DefaultSystemName', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__DefaultSystemName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __DefaultSystemName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 38, 2)
    __DefaultSystemName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 38, 2)
    
    DefaultSystemName = property(__DefaultSystemName.value, __DefaultSystemName.set, None, 'For all objectRefs in this message, this is the default systemName. This name is part of an optional dotted-quad notation that may be used when necessary to create unique object identifers.  The fully-qualified name is of the form of RegisteredName.SystemName.NounType.objectGUID.')

    
    # Attribute DefaultUtility uses Python identifier DefaultUtility
    __DefaultUtility = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DefaultUtility'), 'DefaultUtility', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__DefaultUtility', pyxb.binding.datatypes.string)
    __DefaultUtility._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 43, 2)
    __DefaultUtility._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 43, 2)
    
    DefaultUtility = property(__DefaultUtility.value, __DefaultUtility.set, None, 'String that is used to identify the default utility that is associated with objects contained in this message.   It may be a text string or a pointer to an organization.  If it is a text string, it is suggested that the string be the Internet domain name for the owner in valid XS:anyURI format.')

    
    # Attribute DefaultCurrencyCode uses Python identifier DefaultCurrencyCode
    __DefaultCurrencyCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DefaultCurrencyCode'), 'DefaultCurrencyCode', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__DefaultCurrencyCode', _ImportedBinding__enum.currencyCode)
    __DefaultCurrencyCode._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 48, 2)
    __DefaultCurrencyCode._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 48, 2)
    
    DefaultCurrencyCode = property(__DefaultCurrencyCode.value, __DefaultCurrencyCode.set, None, 'This is the default currencyCode for money transactions sent in this file.  Values of currencyCode are defined in the MultiSpeak core data schema as enumeration of the currencyCode simple type, beginning in Version 4.0.0, release candidate a. For instance, USD is the currency code for united states dollars.  ')

    
    # Attribute RegistrationID uses Python identifier RegistrationID
    __RegistrationID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RegistrationID'), 'RegistrationID', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__RegistrationID', _ImportedBinding__prim.MultiSpeakGUID)
    __RegistrationID._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 53, 2)
    __RegistrationID._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 53, 2)
    
    RegistrationID = property(__RegistrationID.value, __RegistrationID.set, None, 'This is a unique identifier for a specific registration for service (subscription).')

    
    # Attribute MessageID uses Python identifier MessageID
    __MessageID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MessageID'), 'MessageID', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__MessageID', pyxb.binding.datatypes.string, required=True)
    __MessageID._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 58, 2)
    __MessageID._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 58, 2)
    
    MessageID = property(__MessageID.value, __MessageID.set, None, 'This is a unique identifier for this instance of a message.')

    
    # Attribute TimeStamp uses Python identifier TimeStamp
    __TimeStamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TimeStamp'), 'TimeStamp', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__TimeStamp', pyxb.binding.datatypes.dateTime, required=True)
    __TimeStamp._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 63, 2)
    __TimeStamp._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 63, 2)
    
    TimeStamp = property(__TimeStamp.value, __TimeStamp.set, None, 'The time the message was sent.')

    
    # Attribute MessageCreatedTimeStamp uses Python identifier MessageCreatedTimeStamp
    __MessageCreatedTimeStamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MessageCreatedTimeStamp'), 'MessageCreatedTimeStamp', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__MessageCreatedTimeStamp', pyxb.binding.datatypes.dateTime)
    __MessageCreatedTimeStamp._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 68, 2)
    __MessageCreatedTimeStamp._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 68, 2)
    
    MessageCreatedTimeStamp = property(__MessageCreatedTimeStamp.value, __MessageCreatedTimeStamp.set, None, 'This is the time that the message was originally created.')

    
    # Attribute Context uses Python identifier Context
    __Context = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Context'), 'Context', '__httpwww_multispeak_orgV5_0wsrequest_MultiSpeakRequestMsgHeader__Context', _ImportedBinding__com.MessageContext)
    __Context._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 73, 2)
    __Context._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 73, 2)
    
    Context = property(__Context.value, __Context.set, None, 'If used, this attribute tells the receiver the context in which this message is being sent. It is suggested that the receiver treat any message without a contexxt as a production message.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __MultiSpeakVersion.name() : __MultiSpeakVersion,
        __Caller.name() : __Caller,
        __CodedNames.name() : __CodedNames,
        __CoordinateSystemInformation.name() : __CoordinateSystemInformation,
        __DataSetState.name() : __DataSetState,
        __DoNotReply.name() : __DoNotReply
    })
    _AttributeMap.update({
        __DefaultRegisteredName.name() : __DefaultRegisteredName,
        __DefaultSystemName.name() : __DefaultSystemName,
        __DefaultUtility.name() : __DefaultUtility,
        __DefaultCurrencyCode.name() : __DefaultCurrencyCode,
        __RegistrationID.name() : __RegistrationID,
        __MessageID.name() : __MessageID,
        __TimeStamp.name() : __TimeStamp,
        __MessageCreatedTimeStamp.name() : __MessageCreatedTimeStamp,
        __Context.name() : __Context
    })
Namespace.addCategoryObject('typeBinding', 'MultiSpeakRequestMsgHeader', MultiSpeakRequestMsgHeader_)


MultiSpeakRequestMsgHeader = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultiSpeakRequestMsgHeader'), MultiSpeakRequestMsgHeader_, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 19, 1))
Namespace.addCategoryObject('elementBinding', MultiSpeakRequestMsgHeader.name().localName(), MultiSpeakRequestMsgHeader)



MultiSpeakRequestMsgHeader_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultiSpeakVersion'), _ImportedBinding__com.MultiSpeakVersion, scope=MultiSpeakRequestMsgHeader_, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 22, 3)))

MultiSpeakRequestMsgHeader_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Caller'), _ImportedBinding__com.Caller, scope=MultiSpeakRequestMsgHeader_, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 23, 3)))

MultiSpeakRequestMsgHeader_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CodedNames'), _ImportedBinding__com.CodedNames, scope=MultiSpeakRequestMsgHeader_, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 24, 3)))

MultiSpeakRequestMsgHeader_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoordinateSystemInformation'), _ImportedBinding__com.CoordinateSystemInformation, scope=MultiSpeakRequestMsgHeader_, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 25, 3)))

MultiSpeakRequestMsgHeader_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetState'), _ImportedBinding__com.DataSetState, scope=MultiSpeakRequestMsgHeader_, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 26, 3)))

MultiSpeakRequestMsgHeader_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DoNotReply'), _ImportedBinding__com.registrationIDs, scope=MultiSpeakRequestMsgHeader_, documentation='This element has been added so that a subscriber may specify to a publisher that subsequent notification messages should be suppressed for notifications that result solely from handling the payload of this message.  It should be noted that support for this request is optional, but suggested, on all publishers.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 27, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 24, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 25, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 26, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 27, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MultiSpeakRequestMsgHeader_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MultiSpeakVersion')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 22, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MultiSpeakRequestMsgHeader_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Caller')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 23, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MultiSpeakRequestMsgHeader_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CodedNames')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 24, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MultiSpeakRequestMsgHeader_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CoordinateSystemInformation')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 25, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MultiSpeakRequestMsgHeader_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetState')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 26, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MultiSpeakRequestMsgHeader_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DoNotReply')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\MultiSpeakWebServicesRequestMsgHeader.xsd', 27, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MultiSpeakRequestMsgHeader_._Automaton = _BuildAutomaton()

