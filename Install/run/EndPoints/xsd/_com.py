# .\_com.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c15551dcc627c6353a83101da2784af4e2bf30f7
# Generated 2016-08-21 08:25:54.761000 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://www.multispeak.org/V5.0/commonTypes [xmlns:com]

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
import _enum as _ImportedBinding__enum
import _gml as _ImportedBinding__gml

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.multispeak.org/V5.0/commonTypes', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = _ImportedBinding__gml.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.multispeak.org/V5.0/commonTypes}BuildDescriptor
class BuildDescriptor (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The BuildString contains a description of the type of data schema build that is used for thie data in this message.  The options are: PR - Prerelease, RC - Release candidate, Branch - Development branch off of the trunck development, and Release - final release. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildDescriptor')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 196, 1)
    _Documentation = 'The BuildString contains a description of the type of data schema build that is used for thie data in this message.  The options are: PR - Prerelease, RC - Release candidate, Branch - Development branch off of the trunck development, and Release - final release. '
BuildDescriptor._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BuildDescriptor, enum_prefix=None)
BuildDescriptor.Branch = BuildDescriptor._CF_enumeration.addEnumeration(unicode_value='Branch', tag='Branch')
BuildDescriptor.PR = BuildDescriptor._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
BuildDescriptor.RC = BuildDescriptor._CF_enumeration.addEnumeration(unicode_value='RC', tag='RC')
BuildDescriptor.RD = BuildDescriptor._CF_enumeration.addEnumeration(unicode_value='RD', tag='RD')
BuildDescriptor.Release = BuildDescriptor._CF_enumeration.addEnumeration(unicode_value='Release', tag='Release')
BuildDescriptor._InitializeFacetMap(BuildDescriptor._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BuildDescriptor', BuildDescriptor)

# Atomic simple type: {http://www.multispeak.org/V5.0/commonTypes}codedNameType
class codedNameType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'codedNameType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 344, 1)
    _Documentation = None
codedNameType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=codedNameType, enum_prefix=None)
codedNameType.GlobalDomain = codedNameType._CF_enumeration.addEnumeration(unicode_value='GlobalDomain', tag='GlobalDomain')
codedNameType.RegisteredName = codedNameType._CF_enumeration.addEnumeration(unicode_value='RegisteredName', tag='RegisteredName')
codedNameType.SystemName = codedNameType._CF_enumeration.addEnumeration(unicode_value='SystemName', tag='SystemName')
codedNameType.NounType = codedNameType._CF_enumeration.addEnumeration(unicode_value='NounType', tag='NounType')
codedNameType.Other = codedNameType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
codedNameType._InitializeFacetMap(codedNameType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'codedNameType', codedNameType)

# Atomic simple type: {http://www.multispeak.org/V5.0/commonTypes}CSAuthorityNameKind
class CSAuthorityNameKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CSAuthorityNameKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 538, 1)
    _Documentation = None
CSAuthorityNameKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CSAuthorityNameKind, enum_prefix=None)
CSAuthorityNameKind.SPCS = CSAuthorityNameKind._CF_enumeration.addEnumeration(unicode_value='SPCS', tag='SPCS')
CSAuthorityNameKind.EPSG = CSAuthorityNameKind._CF_enumeration.addEnumeration(unicode_value='EPSG', tag='EPSG')
CSAuthorityNameKind.UTM = CSAuthorityNameKind._CF_enumeration.addEnumeration(unicode_value='UTM', tag='UTM')
CSAuthorityNameKind.Other = CSAuthorityNameKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
CSAuthorityNameKind._InitializeFacetMap(CSAuthorityNameKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CSAuthorityNameKind', CSAuthorityNameKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/commonTypes}CSUnitsKind
class CSUnitsKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CSUnitsKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 576, 1)
    _Documentation = None
CSUnitsKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CSUnitsKind, enum_prefix=None)
CSUnitsKind.Feet = CSUnitsKind._CF_enumeration.addEnumeration(unicode_value='Feet', tag='Feet')
CSUnitsKind.Meters = CSUnitsKind._CF_enumeration.addEnumeration(unicode_value='Meters', tag='Meters')
CSUnitsKind.USSurveyFeet = CSUnitsKind._CF_enumeration.addEnumeration(unicode_value='USSurveyFeet', tag='USSurveyFeet')
CSUnitsKind.Other = CSUnitsKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
CSUnitsKind._InitializeFacetMap(CSUnitsKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CSUnitsKind', CSUnitsKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/commonTypes}MessageContext
class MessageContext (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageContext')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 967, 1)
    _Documentation = None
MessageContext._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageContext, enum_prefix=None)
MessageContext.Development = MessageContext._CF_enumeration.addEnumeration(unicode_value='Development', tag='Development')
MessageContext.Production = MessageContext._CF_enumeration.addEnumeration(unicode_value='Production', tag='Production')
MessageContext.Study = MessageContext._CF_enumeration.addEnumeration(unicode_value='Study', tag='Study')
MessageContext.Testing = MessageContext._CF_enumeration.addEnumeration(unicode_value='Testing', tag='Testing')
MessageContext.Training = MessageContext._CF_enumeration.addEnumeration(unicode_value='Training', tag='Training')
MessageContext.Other = MessageContext._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
MessageContext._InitializeFacetMap(MessageContext._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageContext', MessageContext)

# Complex type {http://www.multispeak.org/V5.0/commonTypes}addressItems with content type ELEMENT_ONLY
class addressItems (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}addressItems with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addressItems')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 89, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}addressItem uses Python identifier addressItem
    __addressItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'addressItem'), 'addressItem', '__httpwww_multispeak_orgV5_0commonTypes_addressItems_httpwww_multispeak_orgV5_0commonTypesaddressItem', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 91, 3), )

    
    addressItem = property(__addressItem.value, __addressItem.set, None, None)

    _ElementMap.update({
        __addressItem.name() : __addressItem
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'addressItems', addressItems)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}allocatedLoads with content type ELEMENT_ONLY
class allocatedLoads (pyxb.binding.basis.complexTypeDefinition):
    """An array of allocated loads."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'allocatedLoads')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 129, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}allocatedLoad uses Python identifier allocatedLoad
    __allocatedLoad = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'allocatedLoad'), 'allocatedLoad', '__httpwww_multispeak_orgV5_0commonTypes_allocatedLoads_httpwww_multispeak_orgV5_0commonTypesallocatedLoad', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 134, 3), )

    
    allocatedLoad = property(__allocatedLoad.value, __allocatedLoad.set, None, None)

    _ElementMap.update({
        __allocatedLoad.name() : __allocatedLoad
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'allocatedLoads', allocatedLoads)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}boundingBox with content type ELEMENT_ONLY
class boundingBox (pyxb.binding.basis.complexTypeDefinition):
    """A geographic bounding box defined by two coordinates: (Xmin, Ymin)  and (Xmax, Ymax)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'boundingBox')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 169, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}Xmin uses Python identifier Xmin
    __Xmin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Xmin'), 'Xmin', '__httpwww_multispeak_orgV5_0commonTypes_boundingBox_httpwww_multispeak_orgV5_0commonTypesXmin', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 174, 3), )

    
    Xmin = property(__Xmin.value, __Xmin.set, None, 'The x coordinate of the lower left point of the bounding box.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}Ymin uses Python identifier Ymin
    __Ymin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ymin'), 'Ymin', '__httpwww_multispeak_orgV5_0commonTypes_boundingBox_httpwww_multispeak_orgV5_0commonTypesYmin', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 179, 3), )

    
    Ymin = property(__Ymin.value, __Ymin.set, None, 'The y coordinate of the lower left point of the bounding box.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}Xmax uses Python identifier Xmax
    __Xmax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Xmax'), 'Xmax', '__httpwww_multispeak_orgV5_0commonTypes_boundingBox_httpwww_multispeak_orgV5_0commonTypesXmax', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 184, 3), )

    
    Xmax = property(__Xmax.value, __Xmax.set, None, 'The x coordinate of the upper right point of the bounding box.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}Ymax uses Python identifier Ymax
    __Ymax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ymax'), 'Ymax', '__httpwww_multispeak_orgV5_0commonTypes_boundingBox_httpwww_multispeak_orgV5_0commonTypesYmax', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 189, 3), )

    
    Ymax = property(__Ymax.value, __Ymax.set, None, 'The y coordinate of the upper right point of the bounding box.')

    _ElementMap.update({
        __Xmin.name() : __Xmin,
        __Ymin.name() : __Ymin,
        __Xmax.name() : __Xmax,
        __Ymax.name() : __Ymax
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'boundingBox', boundingBox)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}Caller with content type ELEMENT_ONLY
class Caller (pyxb.binding.basis.complexTypeDefinition):
    """Information to identify the application that sent this message."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Caller')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 228, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}AppName uses Python identifier AppName
    __AppName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AppName'), 'AppName', '__httpwww_multispeak_orgV5_0commonTypes_Caller_httpwww_multispeak_orgV5_0commonTypesAppName', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 233, 3), )

    
    AppName = property(__AppName.value, __AppName.set, None, 'This is the name of the application that sent this message.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}AppVersion uses Python identifier AppVersion
    __AppVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AppVersion'), 'AppVersion', '__httpwww_multispeak_orgV5_0commonTypes_Caller_httpwww_multispeak_orgV5_0commonTypesAppVersion', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 238, 3), )

    
    AppVersion = property(__AppVersion.value, __AppVersion.set, None, 'This is the version of the application that sent this message.  This is NOT the version of MultiSpeak that is used in this message.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}Company uses Python identifier Company
    __Company = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Company'), 'Company', '__httpwww_multispeak_orgV5_0commonTypes_Caller_httpwww_multispeak_orgV5_0commonTypesCompany', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 243, 3), )

    
    Company = property(__Company.value, __Company.set, None, 'This is the name of the company that provides the application that sent this message.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}AuditID uses Python identifier AuditID
    __AuditID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AuditID'), 'AuditID', '__httpwww_multispeak_orgV5_0commonTypes_Caller_httpwww_multispeak_orgV5_0commonTypesAuditID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 248, 3), )

    
    AuditID = property(__AuditID.value, __AuditID.set, None, 'This is the userID of the person who used the system that generated this message.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}AuditPassword uses Python identifier AuditPassword
    __AuditPassword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AuditPassword'), 'AuditPassword', '__httpwww_multispeak_orgV5_0commonTypes_Caller_httpwww_multispeak_orgV5_0commonTypesAuditPassword', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 253, 3), )

    
    AuditPassword = property(__AuditPassword.value, __AuditPassword.set, None, 'This is the password of the person who used the system that generated this message.  It is suggested that this field be used for authorization.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}SystemID uses Python identifier SystemID
    __SystemID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SystemID'), 'SystemID', '__httpwww_multispeak_orgV5_0commonTypes_Caller_httpwww_multispeak_orgV5_0commonTypesSystemID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 258, 3), )

    
    SystemID = property(__SystemID.value, __SystemID.set, None, 'This is the identifier for the system that is sending this message, if needed for authentication.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}Password uses Python identifier Password
    __Password = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Password'), 'Password', '__httpwww_multispeak_orgV5_0commonTypes_Caller_httpwww_multispeak_orgV5_0commonTypesPassword', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 263, 3), )

    
    Password = property(__Password.value, __Password.set, None, 'This is the password for the system that is sending this message if needed for authentication.')

    _ElementMap.update({
        __AppName.name() : __AppName,
        __AppVersion.name() : __AppVersion,
        __Company.name() : __Company,
        __AuditID.name() : __AuditID,
        __AuditPassword.name() : __AuditPassword,
        __SystemID.name() : __SystemID,
        __Password.name() : __Password
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Caller', Caller)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}cimTimePoints with content type ELEMENT_ONLY
class cimTimePoints (pyxb.binding.basis.complexTypeDefinition):
    """This structure is here for future CIM harmonization.  It is not expeted that this schedule structure will be used in MultiSpeak scheduling applications"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cimTimePoints')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 297, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}absoluteTime uses Python identifier absoluteTime
    __absoluteTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'absoluteTime'), 'absoluteTime', '__httpwww_multispeak_orgV5_0commonTypes_cimTimePoints_httpwww_multispeak_orgV5_0commonTypesabsoluteTime', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 302, 3), )

    
    absoluteTime = property(__absoluteTime.value, __absoluteTime.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}relativeTimeInterval uses Python identifier relativeTimeInterval
    __relativeTimeInterval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relativeTimeInterval'), 'relativeTimeInterval', '__httpwww_multispeak_orgV5_0commonTypes_cimTimePoints_httpwww_multispeak_orgV5_0commonTypesrelativeTimeInterval', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 303, 3), )

    
    relativeTimeInterval = property(__relativeTimeInterval.value, __relativeTimeInterval.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}sequenceNumber uses Python identifier sequenceNumber
    __sequenceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sequenceNumber'), 'sequenceNumber', '__httpwww_multispeak_orgV5_0commonTypes_cimTimePoints_httpwww_multispeak_orgV5_0commonTypessequenceNumber', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 304, 3), )

    
    sequenceNumber = property(__sequenceNumber.value, __sequenceNumber.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}window uses Python identifier window
    __window = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'window'), 'window', '__httpwww_multispeak_orgV5_0commonTypes_cimTimePoints_httpwww_multispeak_orgV5_0commonTypeswindow', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 305, 3), )

    
    window = property(__window.value, __window.set, None, None)

    _ElementMap.update({
        __absoluteTime.name() : __absoluteTime,
        __relativeTimeInterval.name() : __relativeTimeInterval,
        __sequenceNumber.name() : __sequenceNumber,
        __window.name() : __window
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'cimTimePoints', cimTimePoints)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}CodedNames with content type ELEMENT_ONLY
class CodedNames (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}CodedNames with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodedNames')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 335, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}codedName uses Python identifier codedName
    __codedName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codedName'), 'codedName', '__httpwww_multispeak_orgV5_0commonTypes_CodedNames_httpwww_multispeak_orgV5_0commonTypescodedName', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 337, 3), )

    
    codedName = property(__codedName.value, __codedName.set, None, 'This is an abbreviation for a part of a fully-qualified object identifier of the form GlobalDomain.RegisteredName.SystemName.nounType.objectGUID')

    _ElementMap.update({
        __codedName.name() : __codedName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CodedNames', CodedNames)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}complexNum with content type ELEMENT_ONLY
class complexNum (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}complexNum with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'complexNum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 401, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}r uses Python identifier r
    __r = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'r'), 'r', '__httpwww_multispeak_orgV5_0commonTypes_complexNum_httpwww_multispeak_orgV5_0commonTypesr', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 403, 3), )

    
    r = property(__r.value, __r.set, None, 'Real portion of the complex number.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__httpwww_multispeak_orgV5_0commonTypes_complexNum_httpwww_multispeak_orgV5_0commonTypesx', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 408, 3), )

    
    x = property(__x.value, __x.set, None, 'Imaginary part of the complex number.')

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_complexNum_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 414, 2)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 414, 2)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        __r.name() : __r,
        __x.name() : __x
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'complexNum', complexNum)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}connectivityModelGroup with content type ELEMENT_ONLY
class connectivityModelGroup (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}connectivityModelGroup with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'connectivityModelGroup')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 446, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}connectivityNodes uses Python identifier connectivityNodes
    __connectivityNodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'connectivityNodes'), 'connectivityNodes', '__httpwww_multispeak_orgV5_0commonTypes_connectivityModelGroup_httpwww_multispeak_orgV5_0commonTypesconnectivityNodes', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 448, 3), )

    
    connectivityNodes = property(__connectivityNodes.value, __connectivityNodes.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}connectivitySections uses Python identifier connectivitySections
    __connectivitySections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'connectivitySections'), 'connectivitySections', '__httpwww_multispeak_orgV5_0commonTypes_connectivityModelGroup_httpwww_multispeak_orgV5_0commonTypesconnectivitySections', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 449, 3), )

    
    connectivitySections = property(__connectivitySections.value, __connectivitySections.set, None, None)

    _ElementMap.update({
        __connectivityNodes.name() : __connectivityNodes,
        __connectivitySections.name() : __connectivitySections
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'connectivityModelGroup', connectivityModelGroup)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}connectivityNodes with content type ELEMENT_ONLY
class connectivityNodes (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}connectivityNodes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'connectivityNodes')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 452, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}node1ID uses Python identifier node1ID
    __node1ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'node1ID'), 'node1ID', '__httpwww_multispeak_orgV5_0commonTypes_connectivityNodes_httpwww_multispeak_orgV5_0commonTypesnode1ID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 454, 3), )

    
    node1ID = property(__node1ID.value, __node1ID.set, None, 'This is the node identifier for this feature in a node-oriented engineering connectivity model.  The connectivityNodeID must be unique. For series-connected devices this is one of the terminal nodes, the upstream node in radial systems.  For shunt-connected devices this is the point of attachment.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}node2ID uses Python identifier node2ID
    __node2ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'node2ID'), 'node2ID', '__httpwww_multispeak_orgV5_0commonTypes_connectivityNodes_httpwww_multispeak_orgV5_0commonTypesnode2ID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 459, 3), )

    
    node2ID = property(__node2ID.value, __node2ID.set, None, 'The connectivityNodeID must be unique if it exists. For series-connected devices this is one of the terminal nodes, the downstream node in a radial system.  For shunt-connected devices this connectivityNodeID refers to neutral, and thus often is not used.')

    _ElementMap.update({
        __node1ID.name() : __node1ID,
        __node2ID.name() : __node2ID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'connectivityNodes', connectivityNodes)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}connectivitySections with content type ELEMENT_ONLY
class connectivitySections (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}connectivitySections with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'connectivitySections')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 466, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}parentSectionIDs uses Python identifier parentSectionIDs
    __parentSectionIDs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parentSectionIDs'), 'parentSectionIDs', '__httpwww_multispeak_orgV5_0commonTypes_connectivitySections_httpwww_multispeak_orgV5_0commonTypesparentSectionIDs', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 468, 3), )

    
    parentSectionIDs = property(__parentSectionIDs.value, __parentSectionIDs.set, None, 'This specifies the upline section(s) in a section-based engineering connectivity model.  Use multiple parentSectionsIDs to model the case in an electrical network model where two or more reduced-phase elements come together to feed a multi-phase element.')

    _ElementMap.update({
        __parentSectionIDs.name() : __parentSectionIDs
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'connectivitySections', connectivitySections)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}contentsItems with content type ELEMENT_ONLY
class contentsItems (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}contentsItems with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contentsItems')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 475, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}contentsItem uses Python identifier contentsItem
    __contentsItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contentsItem'), 'contentsItem', '__httpwww_multispeak_orgV5_0commonTypes_contentsItems_httpwww_multispeak_orgV5_0commonTypescontentsItem', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 477, 3), )

    
    contentsItem = property(__contentsItem.value, __contentsItem.set, None, 'This item is a pointer to the equipment contained in this container. ')

    _ElementMap.update({
        __contentsItem.name() : __contentsItem
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'contentsItems', contentsItems)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}CoordinateSystemInformation with content type ELEMENT_ONLY
class CoordinateSystemInformation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}CoordinateSystemInformation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoordinateSystemInformation')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 484, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}CSUnits uses Python identifier CSUnits
    __CSUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CSUnits'), 'CSUnits', '__httpwww_multispeak_orgV5_0commonTypes_CoordinateSystemInformation_httpwww_multispeak_orgV5_0commonTypesCSUnits', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 486, 3), )

    
    CSUnits = property(__CSUnits.value, __CSUnits.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}CSAuthorities uses Python identifier CSAuthorities
    __CSAuthorities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CSAuthorities'), 'CSAuthorities', '__httpwww_multispeak_orgV5_0commonTypes_CoordinateSystemInformation_httpwww_multispeak_orgV5_0commonTypesCSAuthorities', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 487, 3), )

    
    CSAuthorities = property(__CSAuthorities.value, __CSAuthorities.set, None, 'It is the intention that if there is more than one coordinate system identified here that they SHALL BE multiple identifiers for the same coordinate system.  More than one coordinate system choice Must NOT be implied.')

    _ElementMap.update({
        __CSUnits.name() : __CSUnits,
        __CSAuthorities.name() : __CSAuthorities
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CoordinateSystemInformation', CoordinateSystemInformation)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}CSAuthorities with content type ELEMENT_ONLY
class CSAuthorities (pyxb.binding.basis.complexTypeDefinition):
    """It is the intention that if there is more than one coordinate system identified here that they SHALL BE multiple identifiers for the same coordinate system.  More than one coordinate system choice Must NOT be implied."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CSAuthorities')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 494, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}CSAuthority uses Python identifier CSAuthority
    __CSAuthority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CSAuthority'), 'CSAuthority', '__httpwww_multispeak_orgV5_0commonTypes_CSAuthorities_httpwww_multispeak_orgV5_0commonTypesCSAuthority', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 499, 3), )

    
    CSAuthority = property(__CSAuthority.value, __CSAuthority.set, None, None)

    _ElementMap.update({
        __CSAuthority.name() : __CSAuthority
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CSAuthorities', CSAuthorities)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}CSAuthority with content type ELEMENT_ONLY
class CSAuthority (pyxb.binding.basis.complexTypeDefinition):
    """A naming authority for GIS coordinate systems."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CSAuthority')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 502, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}CSAuthorityName uses Python identifier CSAuthorityName
    __CSAuthorityName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CSAuthorityName'), 'CSAuthorityName', '__httpwww_multispeak_orgV5_0commonTypes_CSAuthority_httpwww_multispeak_orgV5_0commonTypesCSAuthorityName', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 507, 3), )

    
    CSAuthorityName = property(__CSAuthorityName.value, __CSAuthorityName.set, None, 'The string designator for the coordinate system authority.  For example, "SPCS" for the State Plane Coordinate System, "EPSG" for the European Petroleum Survey Group, "UTM" for the Universal Transverse Mercator coordinate system authority.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}CoordinateSystemAuthorityCode uses Python identifier CoordinateSystemAuthorityCode
    __CoordinateSystemAuthorityCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CoordinateSystemAuthorityCode'), 'CoordinateSystemAuthorityCode', '__httpwww_multispeak_orgV5_0commonTypes_CSAuthority_httpwww_multispeak_orgV5_0commonTypesCoordinateSystemAuthorityCode', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 512, 3), )

    
    CoordinateSystemAuthorityCode = property(__CoordinateSystemAuthorityCode.value, __CoordinateSystemAuthorityCode.set, None, 'The string name of the coordinate system authority code.  Examples of coordinate system names are "SPCS:0401", "EPSG:26741", and "UTM:30U".  In these examples "SPCS", "EPSG", and "UTM" are coordinate system authorities and "0401", "26741", and "30U" are coordinate system authority codes.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}Datum uses Python identifier Datum
    __Datum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Datum'), 'Datum', '__httpwww_multispeak_orgV5_0commonTypes_CSAuthority_httpwww_multispeak_orgV5_0commonTypesDatum', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 517, 3), )

    
    Datum = property(__Datum.value, __Datum.set, None, "A datum is a mathematical representation of the shape of the earth's surface.  A complete determination of a geographic coordinate system requires the specification of the CSUnits, Datum, and coordinate system (CSAuthorityName AND CoordinateSystemAuthorityCode).")

    _ElementMap.update({
        __CSAuthorityName.name() : __CSAuthorityName,
        __CoordinateSystemAuthorityCode.name() : __CoordinateSystemAuthorityCode,
        __Datum.name() : __Datum
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CSAuthority', CSAuthority)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}DataSetState with content type ELEMENT_ONLY
class DataSetState (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}DataSetState with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataSetState')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 599, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}PublishDataSetState uses Python identifier PublishDataSetState
    __PublishDataSetState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PublishDataSetState'), 'PublishDataSetState', '__httpwww_multispeak_orgV5_0commonTypes_DataSetState_httpwww_multispeak_orgV5_0commonTypesPublishDataSetState', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 601, 3), )

    
    PublishDataSetState = property(__PublishDataSetState.value, __PublishDataSetState.set, None, 'This option SHALL be used if this message header is for a published data (*Notification) message and it is desired to denote the data set associated with the published information that is being sent in this message.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}RequestDataSetState uses Python identifier RequestDataSetState
    __RequestDataSetState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequestDataSetState'), 'RequestDataSetState', '__httpwww_multispeak_orgV5_0commonTypes_DataSetState_httpwww_multispeak_orgV5_0commonTypesRequestDataSetState', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 606, 3), )

    
    RequestDataSetState = property(__RequestDataSetState.value, __RequestDataSetState.set, None, 'This option SHALL be chosen if this message header is associated with a Get-type request and it is desired to denote the previous data set since which changed data are being requested. ')

    _ElementMap.update({
        __PublishDataSetState.name() : __PublishDataSetState,
        __RequestDataSetState.name() : __RequestDataSetState
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DataSetState', DataSetState)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}eMailAddresses with content type ELEMENT_ONLY
class eMailAddresses (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}eMailAddresses with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'eMailAddresses')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 663, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}eMailAddress uses Python identifier eMailAddress
    __eMailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eMailAddress'), 'eMailAddress', '__httpwww_multispeak_orgV5_0commonTypes_eMailAddresses_httpwww_multispeak_orgV5_0commonTypeseMailAddress', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 665, 3), )

    
    eMailAddress = property(__eMailAddress.value, __eMailAddress.set, None, None)

    _ElementMap.update({
        __eMailAddress.name() : __eMailAddress
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'eMailAddresses', eMailAddresses)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}errorObject with content type ELEMENT_ONLY
class errorObject (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}errorObject with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'errorObject')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 688, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}extensions uses Python identifier extensions
    __extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensions'), 'extensions', '__httpwww_multispeak_orgV5_0commonTypes_errorObject_httpwww_multispeak_orgV5_0commonTypesextensions', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 690, 3), )

    
    extensions = property(__extensions.value, __extensions.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}extensionsList uses Python identifier extensionsList
    __extensionsList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionsList'), 'extensionsList', '__httpwww_multispeak_orgV5_0commonTypes_errorObject_httpwww_multispeak_orgV5_0commonTypesextensionsList', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 691, 3), )

    
    extensionsList = property(__extensionsList.value, __extensionsList.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}errorCode uses Python identifier errorCode
    __errorCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errorCode'), 'errorCode', '__httpwww_multispeak_orgV5_0commonTypes_errorObject_httpwww_multispeak_orgV5_0commonTypeserrorCode', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 692, 3), )

    
    errorCode = property(__errorCode.value, __errorCode.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}eventTime uses Python identifier eventTime
    __eventTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eventTime'), 'eventTime', '__httpwww_multispeak_orgV5_0commonTypes_errorObject_httpwww_multispeak_orgV5_0commonTypeseventTime', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 693, 3), )

    
    eventTime = property(__eventTime.value, __eventTime.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}displayString uses Python identifier displayString
    __displayString = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'displayString'), 'displayString', '__httpwww_multispeak_orgV5_0commonTypes_errorObject_httpwww_multispeak_orgV5_0commonTypesdisplayString', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 694, 3), )

    
    displayString = property(__displayString.value, __displayString.set, None, 'Human readable error message.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}detailedString uses Python identifier detailedString
    __detailedString = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'detailedString'), 'detailedString', '__httpwww_multispeak_orgV5_0commonTypes_errorObject_httpwww_multispeak_orgV5_0commonTypesdetailedString', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 699, 3), )

    
    detailedString = property(__detailedString.value, __detailedString.set, None, None)

    
    # Attribute referenceID uses Python identifier referenceID
    __referenceID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'referenceID'), 'referenceID', '__httpwww_multispeak_orgV5_0commonTypes_errorObject_referenceID', pyxb.binding.datatypes.string)
    __referenceID._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 701, 2)
    __referenceID._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 701, 2)
    
    referenceID = property(__referenceID.value, __referenceID.set, None, 'Identifier for object with error.For objects that inherit from mspObject, this SHALL be an objectGUID, for objects that inherit from mspReferable, this SHALL be a referableID.')

    
    # Attribute nounType uses Python identifier nounType
    __nounType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nounType'), 'nounType', '__httpwww_multispeak_orgV5_0commonTypes_errorObject_nounType', pyxb.binding.datatypes.string)
    __nounType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 706, 2)
    __nounType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 706, 2)
    
    nounType = property(__nounType.value, __nounType.set, None, 'Type of noun for which this error is associated.')

    _ElementMap.update({
        __extensions.name() : __extensions,
        __extensionsList.name() : __extensionsList,
        __errorCode.name() : __errorCode,
        __eventTime.name() : __eventTime,
        __displayString.name() : __displayString,
        __detailedString.name() : __detailedString
    })
    _AttributeMap.update({
        __referenceID.name() : __referenceID,
        __nounType.name() : __nounType
    })
Namespace.addCategoryObject('typeBinding', 'errorObject', errorObject)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}errorObjects with content type ELEMENT_ONLY
class errorObjects (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}errorObjects with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'errorObjects')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 712, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}errorObject uses Python identifier errorObject
    __errorObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errorObject'), 'errorObject', '__httpwww_multispeak_orgV5_0commonTypes_errorObjects_httpwww_multispeak_orgV5_0commonTypeserrorObject', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 714, 3), )

    
    errorObject = property(__errorObject.value, __errorObject.set, None, None)

    _ElementMap.update({
        __errorObject.name() : __errorObject
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'errorObjects', errorObjects)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}extensions with content type ELEMENT_ONLY
class extensions (pyxb.binding.basis.complexTypeDefinition):
    """The extensions container is one way that MultiSpeak objects can be extended using XSD elements."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extensions')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 724, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'extensions', extensions)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}extensionsItem with content type ELEMENT_ONLY
class extensionsItem (pyxb.binding.basis.complexTypeDefinition):
    """This is an optional means to add self-describing extensions to any class that inherits from the mspObject."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extensionsItem')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 736, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}extName uses Python identifier extName
    __extName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extName'), 'extName', '__httpwww_multispeak_orgV5_0commonTypes_extensionsItem_httpwww_multispeak_orgV5_0commonTypesextName', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 741, 3), )

    
    extName = property(__extName.value, __extName.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}extValue uses Python identifier extValue
    __extValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extValue'), 'extValue', '__httpwww_multispeak_orgV5_0commonTypes_extensionsItem_httpwww_multispeak_orgV5_0commonTypesextValue', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 742, 3), )

    
    extValue = property(__extValue.value, __extValue.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}extType uses Python identifier extType
    __extType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extType'), 'extType', '__httpwww_multispeak_orgV5_0commonTypes_extensionsItem_httpwww_multispeak_orgV5_0commonTypesextType', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 743, 3), )

    
    extType = property(__extType.value, __extType.set, None, None)

    _ElementMap.update({
        __extName.name() : __extName,
        __extValue.name() : __extValue,
        __extType.name() : __extType
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'extensionsItem', extensionsItem)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}extensionsList with content type ELEMENT_ONLY
class extensionsList (pyxb.binding.basis.complexTypeDefinition):
    """This is an optional, self-describing means to extend any MultiSpeak object."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extensionsList')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 746, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}extensionsItem uses Python identifier extensionsItem
    __extensionsItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionsItem'), 'extensionsItem', '__httpwww_multispeak_orgV5_0commonTypes_extensionsList_httpwww_multispeak_orgV5_0commonTypesextensionsItem', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 751, 3), )

    
    extensionsItem = property(__extensionsItem.value, __extensionsItem.set, None, None)

    _ElementMap.update({
        __extensionsItem.name() : __extensionsItem
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'extensionsList', extensionsList)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}GMLLines with content type ELEMENT_ONLY
class GMLLines (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}GMLLines with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GMLLines')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 784, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}GMLLine uses Python identifier GMLLine
    __GMLLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GMLLine'), 'GMLLine', '__httpwww_multispeak_orgV5_0commonTypes_GMLLines_httpwww_multispeak_orgV5_0commonTypesGMLLine', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 786, 3), )

    
    GMLLine = property(__GMLLine.value, __GMLLine.set, None, None)

    _ElementMap.update({
        __GMLLine.name() : __GMLLine
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GMLLines', GMLLines)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}GMLPolygons with content type ELEMENT_ONLY
class GMLPolygons (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}GMLPolygons with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GMLPolygons')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 805, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}GMLPolygon uses Python identifier GMLPolygon
    __GMLPolygon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GMLPolygon'), 'GMLPolygon', '__httpwww_multispeak_orgV5_0commonTypes_GMLPolygons_httpwww_multispeak_orgV5_0commonTypesGMLPolygon', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 807, 3), )

    
    GMLPolygon = property(__GMLPolygon.value, __GMLPolygon.set, None, None)

    _ElementMap.update({
        __GMLPolygon.name() : __GMLPolygon
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GMLPolygons', GMLPolygons)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}impedances with content type ELEMENT_ONLY
class impedances (pyxb.binding.basis.complexTypeDefinition):
    """Impedance values are only used in the CPSM profile."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'impedances')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 932, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}r uses Python identifier r
    __r = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'r'), 'r', '__httpwww_multispeak_orgV5_0commonTypes_impedances_httpwww_multispeak_orgV5_0commonTypesr', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 937, 3), )

    
    r = property(__r.value, __r.set, None, 'Positive sequence resistance')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__httpwww_multispeak_orgV5_0commonTypes_impedances_httpwww_multispeak_orgV5_0commonTypesx', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 942, 3), )

    
    x = property(__x.value, __x.set, None, 'Positive sequence reactance.')

    _ElementMap.update({
        __r.name() : __r,
        __x.name() : __x
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'impedances', impedances)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}mspExtensible with content type ELEMENT_ONLY
class mspExtensible (pyxb.binding.basis.complexTypeDefinition):
    """This is an abstract class from which children elements may inherit in order to gain extensibility."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mspExtensible')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1038, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}extensions uses Python identifier extensions
    __extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensions'), 'extensions', '__httpwww_multispeak_orgV5_0commonTypes_mspExtensible_httpwww_multispeak_orgV5_0commonTypesextensions', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3), )

    
    extensions = property(__extensions.value, __extensions.set, None, 'The extensions container is one way that MultiSpeak objects can be extended using XSD elements.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}extensionsList uses Python identifier extensionsList
    __extensionsList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensionsList'), 'extensionsList', '__httpwww_multispeak_orgV5_0commonTypes_mspExtensible_httpwww_multispeak_orgV5_0commonTypesextensionsList', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3), )

    
    extensionsList = property(__extensionsList.value, __extensionsList.set, None, 'This is an optional, self-describing means to extend any MultiSpeak object.')

    _ElementMap.update({
        __extensions.name() : __extensions,
        __extensionsList.name() : __extensionsList
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mspExtensible', mspExtensible)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}multiPartIdentifier with content type ELEMENT_ONLY
class multiPartIdentifier (pyxb.binding.basis.complexTypeDefinition):
    """The multiPartIdentifier is an object identifier that is used when: (i) the noun type is known in advance and hence does not need to be specified in a message payload, (ii) it is not necessary or desirable to use a GUID to point to an object instance, and (iii) at least one and possibly two string names may be used to point to the data instance of interest.  Thus the multiPartIdentifier is a SOFT, NOUN-UNSPECIFIED object identifier."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'multiPartIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1055, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}primaryIdentifier uses Python identifier primaryIdentifier
    __primaryIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'primaryIdentifier'), 'primaryIdentifier', '__httpwww_multispeak_orgV5_0commonTypes_multiPartIdentifier_httpwww_multispeak_orgV5_0commonTypesprimaryIdentifier', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1060, 3), )

    
    primaryIdentifier = property(__primaryIdentifier.value, __primaryIdentifier.set, None, 'Primary human-readable identifier for this instance of the object. ')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}secondaryIdentifier uses Python identifier secondaryIdentifier
    __secondaryIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'secondaryIdentifier'), 'secondaryIdentifier', '__httpwww_multispeak_orgV5_0commonTypes_multiPartIdentifier_httpwww_multispeak_orgV5_0commonTypessecondaryIdentifier', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1065, 3), )

    
    secondaryIdentifier = property(__secondaryIdentifier.value, __secondaryIdentifier.set, None, 'Additional human-readable identifier for this instance of the object. When the secondaryIdentifier is provided, it is expected that the union of the primary and secondary identifiers is necessary to uniquely identify a data instance and both shall be used.')

    _ElementMap.update({
        __primaryIdentifier.name() : __primaryIdentifier,
        __secondaryIdentifier.name() : __secondaryIdentifier
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'multiPartIdentifier', multiPartIdentifier)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}MultiSpeakVersion with content type ELEMENT_ONLY
class MultiSpeakVersion (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}MultiSpeakVersion with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiSpeakVersion')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1072, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}MajorVersion uses Python identifier MajorVersion
    __MajorVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MajorVersion'), 'MajorVersion', '__httpwww_multispeak_orgV5_0commonTypes_MultiSpeakVersion_httpwww_multispeak_orgV5_0commonTypesMajorVersion', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1074, 3), )

    
    MajorVersion = property(__MajorVersion.value, __MajorVersion.set, None, 'The MajorVersion attribute identifies the major version of the data schema used for data in the message.  For instance for Version 5.0.4, the MajorVersion attribute would contain the integer 5.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}MinorVersion uses Python identifier MinorVersion
    __MinorVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MinorVersion'), 'MinorVersion', '__httpwww_multispeak_orgV5_0commonTypes_MultiSpeakVersion_httpwww_multispeak_orgV5_0commonTypesMinorVersion', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1079, 3), )

    
    MinorVersion = property(__MinorVersion.value, __MinorVersion.set, None, 'The MinorVersion attribute identifies the minor version of the data schema used for data in the message. For instance for Version 5.0.4, the MinorVersion attribute would contain the integer 0.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}Build uses Python identifier Build
    __Build = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Build'), 'Build', '__httpwww_multispeak_orgV5_0commonTypes_MultiSpeakVersion_httpwww_multispeak_orgV5_0commonTypesBuild', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1084, 3), )

    
    Build = property(__Build.value, __Build.set, None, 'The Build attribute identifies the build of the data schema used for data in the message. For instance for Version 5.0.4, the Build attribute would contain the integer 4.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}Branch uses Python identifier Branch
    __Branch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Branch'), 'Branch', '__httpwww_multispeak_orgV5_0commonTypes_MultiSpeakVersion_httpwww_multispeak_orgV5_0commonTypesBranch', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1089, 3), )

    
    Branch = property(__Branch.value, __Branch.set, None, 'The Branch attribute identifies the branch number of the data schema used for data in the message. For instance for Version 5.0.4.1, the Branch attribute would contain the integer 1.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}BuildString uses Python identifier BuildString
    __BuildString = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BuildString'), 'BuildString', '__httpwww_multispeak_orgV5_0commonTypes_MultiSpeakVersion_httpwww_multispeak_orgV5_0commonTypesBuildString', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1094, 3), )

    
    BuildString = property(__BuildString.value, __BuildString.set, None, 'The BuildString contains a description of the type of data schema build that is used for the data in this message.  The options are: PR - Prerelease, RC - Release candidate, Branch - Development branch off of the trunk development, RD - Release for Development,  and Release - final release. ')

    _ElementMap.update({
        __MajorVersion.name() : __MajorVersion,
        __MinorVersion.name() : __MinorVersion,
        __Build.name() : __Build,
        __Branch.name() : __Branch,
        __BuildString.name() : __BuildString
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'MultiSpeakVersion', MultiSpeakVersion)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}nounSpecifiedRef with content type ELEMENT_ONLY
class nounSpecifiedRef (pyxb.binding.basis.complexTypeDefinition):
    """The nounSpecifiedRef is used to refer to a data instance when (i) the noun type is not known in advance and hence must be specified in the message payload and (ii) it is desired to use either an objectRef or nounSpecifiedMultiPartIdentifier to refer to the data instance of interest."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nounSpecifiedRef')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1137, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}objectIdentifier uses Python identifier objectIdentifier
    __objectIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectIdentifier'), 'objectIdentifier', '__httpwww_multispeak_orgV5_0commonTypes_nounSpecifiedRef_httpwww_multispeak_orgV5_0commonTypesobjectIdentifier', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1142, 3), )

    
    objectIdentifier = property(__objectIdentifier.value, __objectIdentifier.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}objectRef uses Python identifier objectRef
    __objectRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectRef'), 'objectRef', '__httpwww_multispeak_orgV5_0commonTypes_nounSpecifiedRef_httpwww_multispeak_orgV5_0commonTypesobjectRef', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1143, 3), )

    
    objectRef = property(__objectRef.value, __objectRef.set, None, None)

    _ElementMap.update({
        __objectIdentifier.name() : __objectIdentifier,
        __objectRef.name() : __objectRef
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'nounSpecifiedRef', nounSpecifiedRef)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}nounUnspecifiedRef with content type ELEMENT_ONLY
class nounUnspecifiedRef (pyxb.binding.basis.complexTypeDefinition):
    """The nounUnspecifiedRef is used when it is desirable to refer to an object of known noun type using either an objectID or a multiPartIdentifier. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nounUnspecifiedRef')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1146, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}objectGUID uses Python identifier objectGUID
    __objectGUID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectGUID'), 'objectGUID', '__httpwww_multispeak_orgV5_0commonTypes_nounUnspecifiedRef_httpwww_multispeak_orgV5_0commonTypesobjectGUID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1151, 3), )

    
    objectGUID = property(__objectGUID.value, __objectGUID.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}objectName uses Python identifier objectName
    __objectName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectName'), 'objectName', '__httpwww_multispeak_orgV5_0commonTypes_nounUnspecifiedRef_httpwww_multispeak_orgV5_0commonTypesobjectName', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1152, 3), )

    
    objectName = property(__objectName.value, __objectName.set, None, None)

    _ElementMap.update({
        __objectGUID.name() : __objectGUID,
        __objectName.name() : __objectName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'nounUnspecifiedRef', nounUnspecifiedRef)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}objectID with content type ELEMENT_ONLY
class objectID (pyxb.binding.basis.complexTypeDefinition):
    """An objectID is the primary way to identify an object, using a GUID where the noun type is known in advance.  Since the noun type is known in advance, it does not need to be specified in a message payload.  Thus an objectID is a HARD, NOUN-UNSPECIFIED object identifier."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'objectID')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1155, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}objectGUID uses Python identifier objectGUID
    __objectGUID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectGUID'), 'objectGUID', '__httpwww_multispeak_orgV5_0commonTypes_objectID_httpwww_multispeak_orgV5_0commonTypesobjectGUID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1160, 3), )

    
    objectGUID = property(__objectGUID.value, __objectGUID.set, None, 'This is the objectIdentifier for the data instance of interest.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}primaryIdentifier uses Python identifier primaryIdentifier
    __primaryIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'primaryIdentifier'), 'primaryIdentifier', '__httpwww_multispeak_orgV5_0commonTypes_objectID_httpwww_multispeak_orgV5_0commonTypesprimaryIdentifier', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1165, 3), )

    
    primaryIdentifier = property(__primaryIdentifier.value, __primaryIdentifier.set, None, 'Primary human-readable identifier for this instance of the object. For instance if this object is an instance of an electricMeter, this should be the meterNumber; if this is a customer account, this should be the accountNumber. ')

    _ElementMap.update({
        __objectGUID.name() : __objectGUID,
        __primaryIdentifier.name() : __primaryIdentifier
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'objectID', objectID)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}otherContactInformation with content type ELEMENT_ONLY
class otherContactInformation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}otherContactInformation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'otherContactInformation')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1232, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}otherContactItem uses Python identifier otherContactItem
    __otherContactItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'otherContactItem'), 'otherContactItem', '__httpwww_multispeak_orgV5_0commonTypes_otherContactInformation_httpwww_multispeak_orgV5_0commonTypesotherContactItem', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1234, 3), )

    
    otherContactItem = property(__otherContactItem.value, __otherContactItem.set, None, None)

    _ElementMap.update({
        __otherContactItem.name() : __otherContactItem
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'otherContactInformation', otherContactInformation)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}phoneNumbers with content type ELEMENT_ONLY
class phoneNumbers (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}phoneNumbers with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phoneNumbers')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1277, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}phoneNumber uses Python identifier phoneNumber
    __phoneNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phoneNumber'), 'phoneNumber', '__httpwww_multispeak_orgV5_0commonTypes_phoneNumbers_httpwww_multispeak_orgV5_0commonTypesphoneNumber', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1279, 3), )

    
    phoneNumber = property(__phoneNumber.value, __phoneNumber.set, None, None)

    _ElementMap.update({
        __phoneNumber.name() : __phoneNumber
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'phoneNumbers', phoneNumbers)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}PublishDataSetState with content type ELEMENT_ONLY
class PublishDataSetState (pyxb.binding.basis.complexTypeDefinition):
    """This option SHALL be used if this message header is for a published data (*Notification) message and it is desired to denote the data set associated with the published information that is being sent in this message."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PublishDataSetState')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1293, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}DataSetID uses Python identifier DataSetID
    __DataSetID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetID'), 'DataSetID', '__httpwww_multispeak_orgV5_0commonTypes_PublishDataSetState_httpwww_multispeak_orgV5_0commonTypesDataSetID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1298, 3), )

    
    DataSetID = property(__DataSetID.value, __DataSetID.set, None, 'When it is desired to support data sets, this element SHALL be used to denote the data set for the data included in the message with which this message header is associated.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}PreviousDataSetID uses Python identifier PreviousDataSetID
    __PreviousDataSetID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PreviousDataSetID'), 'PreviousDataSetID', '__httpwww_multispeak_orgV5_0commonTypes_PublishDataSetState_httpwww_multispeak_orgV5_0commonTypesPreviousDataSetID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1303, 3), )

    
    PreviousDataSetID = property(__PreviousDataSetID.value, __PreviousDataSetID.set, None, 'When it is desired to support data sets, this attribute identifies the previously sent block of data by data set identifier.  If the receiver of this message has not received the data set identified in the previous data set ID, it has missed data and it SHALL attempt recovery by calling the appropriate GetModified* service, if any, that has the PreviousDataSetID parameter populated in the message header with the data set identifier of the last data set that it had successfully received. If no GetModified* service is available, or the GetModified service is not supported by the server, then the receiver SHALL return a message with appropriate error information included in the result element.')

    _ElementMap.update({
        __DataSetID.name() : __DataSetID,
        __PreviousDataSetID.name() : __PreviousDataSetID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PublishDataSetState', PublishDataSetState)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}registrationIDs with content type ELEMENT_ONLY
class registrationIDs (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}registrationIDs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'registrationIDs')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1381, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}registrationID uses Python identifier registrationID
    __registrationID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'registrationID'), 'registrationID', '__httpwww_multispeak_orgV5_0commonTypes_registrationIDs_httpwww_multispeak_orgV5_0commonTypesregistrationID', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1383, 3), )

    
    registrationID = property(__registrationID.value, __registrationID.set, None, None)

    _ElementMap.update({
        __registrationID.name() : __registrationID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'registrationIDs', registrationIDs)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}replyCodeIdentifier with content type ELEMENT_ONLY
class replyCodeIdentifier (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}replyCodeIdentifier with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'replyCodeIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1386, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}replyCodeCategory uses Python identifier replyCodeCategory
    __replyCodeCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'replyCodeCategory'), 'replyCodeCategory', '__httpwww_multispeak_orgV5_0commonTypes_replyCodeIdentifier_httpwww_multispeak_orgV5_0commonTypesreplyCodeCategory', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1388, 3), )

    
    replyCodeCategory = property(__replyCodeCategory.value, __replyCodeCategory.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'index'), 'index', '__httpwww_multispeak_orgV5_0commonTypes_replyCodeIdentifier_httpwww_multispeak_orgV5_0commonTypesindex', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1389, 3), )

    
    index = property(__index.value, __index.set, None, None)

    _ElementMap.update({
        __replyCodeCategory.name() : __replyCodeCategory,
        __index.name() : __index
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'replyCodeIdentifier', replyCodeIdentifier)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}RequestDataSetState with content type ELEMENT_ONLY
class RequestDataSetState (pyxb.binding.basis.complexTypeDefinition):
    """This option SHALL be chosen if this message header is associated with a Get-type request and it is desired to denote the previous data set since which changed data are being requested. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestDataSetState')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1392, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}DataSetID uses Python identifier DataSetID
    __DataSetID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetID'), 'DataSetID', '__httpwww_multispeak_orgV5_0commonTypes_RequestDataSetState_httpwww_multispeak_orgV5_0commonTypesDataSetID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1397, 3), )

    
    DataSetID = property(__DataSetID.value, __DataSetID.set, None, 'When necessary, this optional attribute identifies the data sent in this session.  If the DataSetID is included in a GetAll-type method call, then the server shall respond as if it was being asked for a GetModified-type call since that DataSetID, that is to say, it should send only those data instances that have changed since the PreviousDataSetID provided herein.  If the GetAll-type call does not include a DataSetID, or the server does not support data sets, then all instances of the requested object shall be returned.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}PreviousDataSetID uses Python identifier PreviousDataSetID
    __PreviousDataSetID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PreviousDataSetID'), 'PreviousDataSetID', '__httpwww_multispeak_orgV5_0commonTypes_RequestDataSetState_httpwww_multispeak_orgV5_0commonTypesPreviousDataSetID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1402, 3), )

    
    PreviousDataSetID = property(__PreviousDataSetID.value, __PreviousDataSetID.set, None, 'When necessary, this attribute identifies the previously sent block of data by data set identifier.')

    _ElementMap.update({
        __DataSetID.name() : __DataSetID,
        __PreviousDataSetID.name() : __PreviousDataSetID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RequestDataSetState', RequestDataSetState)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}requiredTimePeriod with content type ELEMENT_ONLY
class requiredTimePeriod (pyxb.binding.basis.complexTypeDefinition):
    """A defined time period for which both the start and end times are required."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'requiredTimePeriod')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1414, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startTime'), 'startTime', '__httpwww_multispeak_orgV5_0commonTypes_requiredTimePeriod_httpwww_multispeak_orgV5_0commonTypesstartTime', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1419, 3), )

    
    startTime = property(__startTime.value, __startTime.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}endTime uses Python identifier endTime
    __endTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endTime'), 'endTime', '__httpwww_multispeak_orgV5_0commonTypes_requiredTimePeriod_httpwww_multispeak_orgV5_0commonTypesendTime', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1420, 3), )

    
    endTime = property(__endTime.value, __endTime.set, None, None)

    _ElementMap.update({
        __startTime.name() : __startTime,
        __endTime.name() : __endTime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'requiredTimePeriod', requiredTimePeriod)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}result with content type ELEMENT_ONLY
class result (pyxb.binding.basis.complexTypeDefinition):
    """The result object is used by a Responder to return information to a Requester on the result of processing a prior message.  The result object may also be used as the payload of an asynchronous/unsolicited error message (a SystemStateNotification)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'result')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1461, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}resultIdentifier uses Python identifier resultIdentifier
    __resultIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resultIdentifier'), 'resultIdentifier', '__httpwww_multispeak_orgV5_0commonTypes_result_httpwww_multispeak_orgV5_0commonTypesresultIdentifier', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1466, 3), )

    
    resultIdentifier = property(__resultIdentifier.value, __resultIdentifier.set, None, 'It is suggested that the values of replyCode be chosen from those values included in IEC 61968-9, 2nd Ed., Annex B as extended by Appendix A of "Security in MultiSpeak-Enabled Applications: Requirements".  Values of replyCode SHOULD be of the form [category] "." [index].')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}resultDescription uses Python identifier resultDescription
    __resultDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resultDescription'), 'resultDescription', '__httpwww_multispeak_orgV5_0commonTypes_result_httpwww_multispeak_orgV5_0commonTypesresultDescription', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1471, 3), )

    
    resultDescription = property(__resultDescription.value, __resultDescription.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}level uses Python identifier level
    __level = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'level'), 'level', '__httpwww_multispeak_orgV5_0commonTypes_result_httpwww_multispeak_orgV5_0commonTypeslevel', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1472, 3), )

    
    level = property(__level.value, __level.set, None, 'The level element describes the severity of the error message.  It is suggested that no level element be returned for a fully successful message.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}errorObjects uses Python identifier errorObjects
    __errorObjects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errorObjects'), 'errorObjects', '__httpwww_multispeak_orgV5_0commonTypes_result_httpwww_multispeak_orgV5_0commonTypeserrorObjects', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1477, 3), )

    
    errorObjects = property(__errorObjects.value, __errorObjects.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}dataSetID uses Python identifier dataSetID
    __dataSetID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dataSetID'), 'dataSetID', '__httpwww_multispeak_orgV5_0commonTypes_result_httpwww_multispeak_orgV5_0commonTypesdataSetID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1478, 3), )

    
    dataSetID = property(__dataSetID.value, __dataSetID.set, None, 'If this response header is associated with a GetAll* message, this element SHOULD be populated with the data set identifier by which the server knows the included data so that subsequent GetModified* messages for the same type of data could include a PreviousDataSetID in the request header so that the server could determine which data instances to include in its response (the data instances that had been modified since this base data set).  ')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}lastSent uses Python identifier lastSent
    __lastSent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastSent'), 'lastSent', '__httpwww_multispeak_orgV5_0commonTypes_result_httpwww_multispeak_orgV5_0commonTypeslastSent', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1483, 3), )

    
    lastSent = property(__lastSent.value, __lastSent.set, None, 'Pointer assigned by the server to the last object sent by server when using lastSent and lastReceived to send "chunks" of data.  It is up to the server to generate a pointer that ensures that all data instances are returned, but the pointer does not need to have meaning to the receiver, and it is not required that the pointer match the objectID of the last sent data instance.   Client will return this value in the lastReceived parameter of a web service method to request more data.\n ')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}objectsRemaining uses Python identifier objectsRemaining
    __objectsRemaining = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectsRemaining'), 'objectsRemaining', '__httpwww_multispeak_orgV5_0commonTypes_result_httpwww_multispeak_orgV5_0commonTypesobjectsRemaining', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1489, 3), )

    
    objectsRemaining = property(__objectsRemaining.value, __objectsRemaining.set, None, 'This is an optional attribute that is used to denote the number of objects remaining in a complete data transfer after this set of data is handled.  If this attribute is not included or is set to be 0, all data have been sent at the completion of this data transfer.  If the number of objectsRemaining is known, the value should be entered here.  If the number of remaining data instances is not known, the number should be set to be -1.')

    _ElementMap.update({
        __resultIdentifier.name() : __resultIdentifier,
        __resultDescription.name() : __resultDescription,
        __level.name() : __level,
        __errorObjects.name() : __errorObjects,
        __dataSetID.name() : __dataSetID,
        __lastSent.name() : __lastSent,
        __objectsRemaining.name() : __objectsRemaining
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'result', result)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}servicePointIDs with content type ELEMENT_ONLY
class servicePointIDs (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}servicePointIDs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'servicePointIDs')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1545, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}servicePointID uses Python identifier servicePointID
    __servicePointID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'servicePointID'), 'servicePointID', '__httpwww_multispeak_orgV5_0commonTypes_servicePointIDs_httpwww_multispeak_orgV5_0commonTypesservicePointID', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1547, 3), )

    
    servicePointID = property(__servicePointID.value, __servicePointID.set, None, None)

    _ElementMap.update({
        __servicePointID.name() : __servicePointID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'servicePointIDs', servicePointIDs)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}timePeriod with content type ELEMENT_ONLY
class timePeriod (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}timePeriod with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timePeriod')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1700, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startTime'), 'startTime', '__httpwww_multispeak_orgV5_0commonTypes_timePeriod_httpwww_multispeak_orgV5_0commonTypesstartTime', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1702, 3), )

    
    startTime = property(__startTime.value, __startTime.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}endTime uses Python identifier endTime
    __endTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endTime'), 'endTime', '__httpwww_multispeak_orgV5_0commonTypes_timePeriod_httpwww_multispeak_orgV5_0commonTypesendTime', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1703, 3), )

    
    endTime = property(__endTime.value, __endTime.set, None, None)

    _ElementMap.update({
        __startTime.name() : __startTime,
        __endTime.name() : __endTime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'timePeriod', timePeriod)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}activePower with content type SIMPLE
class activePower (pyxb.binding.basis.complexTypeDefinition):
    """Product of RMS value of the voltage and the RMS value of the in-phase component of the current (Megawatt)."""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activePower')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 12, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_activePower_units', _ImportedBinding__enum.realPowerUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 18, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 18, 4)
    
    units = property(__units.value, __units.set, None, 'Units in which this active power is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'activePower', activePower)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}address with content type ELEMENT_ONLY
class address (mspExtensible):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}address with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'address')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 26, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}address1 uses Python identifier address1
    __address1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address1'), 'address1', '__httpwww_multispeak_orgV5_0commonTypes_address_httpwww_multispeak_orgV5_0commonTypesaddress1', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 30, 5), )

    
    address1 = property(__address1.value, __address1.set, None, 'Address line 1.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}address2 uses Python identifier address2
    __address2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address2'), 'address2', '__httpwww_multispeak_orgV5_0commonTypes_address_httpwww_multispeak_orgV5_0commonTypesaddress2', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 35, 5), )

    
    address2 = property(__address2.value, __address2.set, None, 'Address line 2.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}detailedAddressFields uses Python identifier detailedAddressFields
    __detailedAddressFields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'detailedAddressFields'), 'detailedAddressFields', '__httpwww_multispeak_orgV5_0commonTypes_address_httpwww_multispeak_orgV5_0commonTypesdetailedAddressFields', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 40, 5), )

    
    detailedAddressFields = property(__detailedAddressFields.value, __detailedAddressFields.set, None, 'Detailed information about the components of the composite address lines.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}townCode uses Python identifier townCode
    __townCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'townCode'), 'townCode', '__httpwww_multispeak_orgV5_0commonTypes_address_httpwww_multispeak_orgV5_0commonTypestownCode', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 45, 5), )

    
    townCode = property(__townCode.value, __townCode.set, None, 'Additional information about the city or town, if required.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpwww_multispeak_orgV5_0commonTypes_address_httpwww_multispeak_orgV5_0commonTypescity', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 50, 5), )

    
    city = property(__city.value, __city.set, None, 'Name of the city or municipality.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'state'), 'state', '__httpwww_multispeak_orgV5_0commonTypes_address_httpwww_multispeak_orgV5_0commonTypesstate', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 55, 5), )

    
    state = property(__state.value, __state.set, None, 'The state or province.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), 'postalCode', '__httpwww_multispeak_orgV5_0commonTypes_address_httpwww_multispeak_orgV5_0commonTypespostalCode', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 60, 5), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, 'The postal code.  For instance, in the United States this is the zip code.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'country'), 'country', '__httpwww_multispeak_orgV5_0commonTypes_address_httpwww_multispeak_orgV5_0commonTypescountry', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 65, 5), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    _ElementMap.update({
        __address1.name() : __address1,
        __address2.name() : __address2,
        __detailedAddressFields.name() : __detailedAddressFields,
        __townCode.name() : __townCode,
        __city.name() : __city,
        __state.name() : __state,
        __postalCode.name() : __postalCode,
        __country.name() : __country
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'address', address)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}addressItem with content type ELEMENT_ONLY
class addressItem (mspExtensible):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}addressItem with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addressItem')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 70, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address'), 'address', '__httpwww_multispeak_orgV5_0commonTypes_addressItem_httpwww_multispeak_orgV5_0commonTypesaddress', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 74, 5), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}addressType uses Python identifier addressType
    __addressType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'addressType'), 'addressType', '__httpwww_multispeak_orgV5_0commonTypes_addressItem_httpwww_multispeak_orgV5_0commonTypesaddressType', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 75, 5), )

    
    addressType = property(__addressType.value, __addressType.set, None, 'Type of address. For instance, billing, mailing, service location, etc.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}priorityOrder uses Python identifier priorityOrder
    __priorityOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'priorityOrder'), 'priorityOrder', '__httpwww_multispeak_orgV5_0commonTypes_addressItem_httpwww_multispeak_orgV5_0commonTypespriorityOrder', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 80, 5), )

    
    priorityOrder = property(__priorityOrder.value, __priorityOrder.set, None, 'Order that should be used to contact this person.  First = 1, second = 2, etc.')

    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    _ElementMap.update({
        __address.name() : __address,
        __addressType.name() : __addressType,
        __priorityOrder.name() : __priorityOrder
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'addressItem', addressItem)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}admittance with content type SIMPLE
class admittance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}admittance with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'admittance')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 94, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_admittance_units', _ImportedBinding__enum.sUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 97, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 97, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which this admittance is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'admittance', admittance)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}allocatedLoad with content type ELEMENT_ONLY
class allocatedLoad (mspExtensible):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}allocatedLoad with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'allocatedLoad')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 105, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}phaseCode uses Python identifier phaseCode
    __phaseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phaseCode'), 'phaseCode', '__httpwww_multispeak_orgV5_0commonTypes_allocatedLoad_httpwww_multispeak_orgV5_0commonTypesphaseCode', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 109, 5), )

    
    phaseCode = property(__phaseCode.value, __phaseCode.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}realPower uses Python identifier realPower
    __realPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'realPower'), 'realPower', '__httpwww_multispeak_orgV5_0commonTypes_allocatedLoad_httpwww_multispeak_orgV5_0commonTypesrealPower', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 110, 5), )

    
    realPower = property(__realPower.value, __realPower.set, None, 'Real power load on this section.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}reactivePower uses Python identifier reactivePower
    __reactivePower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reactivePower'), 'reactivePower', '__httpwww_multispeak_orgV5_0commonTypes_allocatedLoad_httpwww_multispeak_orgV5_0commonTypesreactivePower', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 115, 5), )

    
    reactivePower = property(__reactivePower.value, __reactivePower.set, None, 'kVAr load on this section.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}numberOfCustomers uses Python identifier numberOfCustomers
    __numberOfCustomers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'numberOfCustomers'), 'numberOfCustomers', '__httpwww_multispeak_orgV5_0commonTypes_allocatedLoad_httpwww_multispeak_orgV5_0commonTypesnumberOfCustomers', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 120, 5), )

    
    numberOfCustomers = property(__numberOfCustomers.value, __numberOfCustomers.set, None, 'Number of customers allocated to this section.')

    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    _ElementMap.update({
        __phaseCode.name() : __phaseCode,
        __realPower.name() : __realPower,
        __reactivePower.name() : __reactivePower,
        __numberOfCustomers.name() : __numberOfCustomers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'allocatedLoad', allocatedLoad)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}angle with content type SIMPLE
class angle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}angle with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'angle')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 137, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_angle_units', _ImportedBinding__enum.angleUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 140, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 140, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which this angle is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'angle', angle)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}angleInDegrees with content type SIMPLE
class angleInDegrees (pyxb.binding.basis.complexTypeDefinition):
    """Angle measured in degrees."""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'angleInDegrees')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 148, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_angleInDegrees_units', _ImportedBinding__enum.degreeUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 154, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 154, 4)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'angleInDegrees', angleInDegrees)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}apparentPower with content type SIMPLE
class apparentPower (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}apparentPower with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'apparentPower')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 158, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_apparentPower_units', _ImportedBinding__enum.apparentPowerUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 161, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 161, 4)
    
    units = property(__units.value, __units.set, None, 'Units in which this apparent power is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'apparentPower', apparentPower)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}capacitance with content type SIMPLE
class capacitance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}capacitance with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'capacitance')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 270, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_capacitance_units', _ImportedBinding__enum.capacitanceUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 273, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 273, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the capacitance is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'capacitance', capacitance)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}capacitancePerUnitLength with content type SIMPLE
class capacitancePerUnitLength (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}capacitancePerUnitLength with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'capacitancePerUnitLength')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 281, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute capacitanceUnits uses Python identifier capacitanceUnits
    __capacitanceUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'capacitanceUnits'), 'capacitanceUnits', '__httpwww_multispeak_orgV5_0commonTypes_capacitancePerUnitLength_capacitanceUnits', _ImportedBinding__enum.capacitanceUnits)
    __capacitanceUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 284, 4)
    __capacitanceUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 284, 4)
    
    capacitanceUnits = property(__capacitanceUnits.value, __capacitanceUnits.set, None, 'The units in which the capacitance is expressed.')

    
    # Attribute lengthUnits uses Python identifier lengthUnits
    __lengthUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lengthUnits'), 'lengthUnits', '__httpwww_multispeak_orgV5_0commonTypes_capacitancePerUnitLength_lengthUnits', _ImportedBinding__enum.lengthUnits)
    __lengthUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 289, 4)
    __lengthUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 289, 4)
    
    lengthUnits = property(__lengthUnits.value, __lengthUnits.set, None, 'The units used for the reference length.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __capacitanceUnits.name() : __capacitanceUnits,
        __lengthUnits.name() : __lengthUnits
    })
Namespace.addCategoryObject('typeBinding', 'capacitancePerUnitLength', capacitancePerUnitLength)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}codedName with content type ELEMENT_ONLY
class codedName (pyxb.binding.basis.complexTypeDefinition):
    """This is an abbreviation for a part of a fully-qualified object identifier of the form GlobalDomain.RegisteredName.SystemName.nounType.objectGUID"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'codedName')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 308, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}codedValue uses Python identifier codedValue
    __codedValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codedValue'), 'codedValue', '__httpwww_multispeak_orgV5_0commonTypes_codedName_httpwww_multispeak_orgV5_0commonTypescodedValue', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 313, 3), )

    
    codedValue = property(__codedValue.value, __codedValue.set, None, 'This is the shorthand abbreviation for the name part.  For instance, codedValue could equal "1" or "A" for RegisteredName = "ACMEWidgets"')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}namePart uses Python identifier namePart
    __namePart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'namePart'), 'namePart', '__httpwww_multispeak_orgV5_0commonTypes_codedName_httpwww_multispeak_orgV5_0commonTypesnamePart', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 318, 3), )

    
    namePart = property(__namePart.value, __namePart.set, None, 'This is the complete name part.  For instance "ACMEWidgets in the example given in the annotation for the codedValue.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpwww_multispeak_orgV5_0commonTypes_codedName_httpwww_multispeak_orgV5_0commonTypesdescription', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 323, 3), )

    
    description = property(__description.value, __description.set, None, 'This is an optional string description of the name part.')

    
    # Attribute codedNameType uses Python identifier codedNameType
    __codedNameType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'codedNameType'), 'codedNameType', '__httpwww_multispeak_orgV5_0commonTypes_codedName_codedNameType', codedNameType)
    __codedNameType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 329, 2)
    __codedNameType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 329, 2)
    
    codedNameType = property(__codedNameType.value, __codedNameType.set, None, 'The type of name to be encoded, such as RegisteredName, SystemName, etc.')

    _ElementMap.update({
        __codedValue.name() : __codedValue,
        __namePart.name() : __namePart,
        __description.name() : __description
    })
    _AttributeMap.update({
        __codedNameType.name() : __codedNameType
    })
Namespace.addCategoryObject('typeBinding', 'codedName', codedName)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}complexImpedance with content type ELEMENT_ONLY
class complexImpedance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}complexImpedance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'complexImpedance')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 353, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}r uses Python identifier r
    __r = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'r'), 'r', '__httpwww_multispeak_orgV5_0commonTypes_complexImpedance_httpwww_multispeak_orgV5_0commonTypesr', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 355, 3), )

    
    r = property(__r.value, __r.set, None, 'The resistive portion of impedance.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__httpwww_multispeak_orgV5_0commonTypes_complexImpedance_httpwww_multispeak_orgV5_0commonTypesx', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 360, 3), )

    
    x = property(__x.value, __x.set, None, 'The reactive portion of the impedance')

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_complexImpedance_units', _ImportedBinding__enum.zUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 366, 2)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 366, 2)
    
    units = property(__units.value, __units.set, None, 'The units in which this impedance is expressed.')

    _ElementMap.update({
        __r.name() : __r,
        __x.name() : __x
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'complexImpedance', complexImpedance)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}complexImpedanceWithLeakage with content type ELEMENT_ONLY
class complexImpedanceWithLeakage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}complexImpedanceWithLeakage with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'complexImpedanceWithLeakage')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 372, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}r uses Python identifier r
    __r = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'r'), 'r', '__httpwww_multispeak_orgV5_0commonTypes_complexImpedanceWithLeakage_httpwww_multispeak_orgV5_0commonTypesr', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 374, 3), )

    
    r = property(__r.value, __r.set, None, 'The resistive portion of the impedance.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__httpwww_multispeak_orgV5_0commonTypes_complexImpedanceWithLeakage_httpwww_multispeak_orgV5_0commonTypesx', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 379, 3), )

    
    x = property(__x.value, __x.set, None, 'The reactive portion of the impedance.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}b uses Python identifier b
    __b = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'b'), 'b', '__httpwww_multispeak_orgV5_0commonTypes_complexImpedanceWithLeakage_httpwww_multispeak_orgV5_0commonTypesb', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 384, 3), )

    
    b = property(__b.value, __b.set, None, 'The leakage susceptance.')

    
    # Attribute zUnits uses Python identifier zUnits
    __zUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'zUnits'), 'zUnits', '__httpwww_multispeak_orgV5_0commonTypes_complexImpedanceWithLeakage_zUnits', _ImportedBinding__enum.zUnits)
    __zUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 390, 2)
    __zUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 390, 2)
    
    zUnits = property(__zUnits.value, __zUnits.set, None, 'The units in which this impedance is expressed.')

    
    # Attribute sUnits uses Python identifier sUnits
    __sUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sUnits'), 'sUnits', '__httpwww_multispeak_orgV5_0commonTypes_complexImpedanceWithLeakage_sUnits', _ImportedBinding__enum.sUnits)
    __sUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 395, 2)
    __sUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 395, 2)
    
    sUnits = property(__sUnits.value, __sUnits.set, None, 'Units in which the leakage (susceptance) is expressed.')

    _ElementMap.update({
        __r.name() : __r,
        __x.name() : __x,
        __b.name() : __b
    })
    _AttributeMap.update({
        __zUnits.name() : __zUnits,
        __sUnits.name() : __sUnits
    })
Namespace.addCategoryObject('typeBinding', 'complexImpedanceWithLeakage', complexImpedanceWithLeakage)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}complexVoltage with content type ELEMENT_ONLY
class complexVoltage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}complexVoltage with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'complexVoltage')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 416, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}r uses Python identifier r
    __r = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'r'), 'r', '__httpwww_multispeak_orgV5_0commonTypes_complexVoltage_httpwww_multispeak_orgV5_0commonTypesr', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 418, 3), )

    
    r = property(__r.value, __r.set, None, 'Real component of the voltage.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'x'), 'x', '__httpwww_multispeak_orgV5_0commonTypes_complexVoltage_httpwww_multispeak_orgV5_0commonTypesx', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 423, 3), )

    
    x = property(__x.value, __x.set, None, 'Imaginary component of the voltage.')

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_complexVoltage_units', _ImportedBinding__enum.voltageUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 429, 2)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 429, 2)
    
    units = property(__units.value, __units.set, None, 'Units in which this voltage is expressed.')

    _ElementMap.update({
        __r.name() : __r,
        __x.name() : __x
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'complexVoltage', complexVoltage)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}conductance with content type SIMPLE
class conductance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}conductance with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'conductance')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 435, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_conductance_units', _ImportedBinding__enum.sUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 438, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 438, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which this conductance is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'conductance', conductance)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}CSAuthorityName with content type SIMPLE
class CSAuthorityName (pyxb.binding.basis.complexTypeDefinition):
    """The name of the GIS coordinate system naming authority.  Examples include "SPCS" for U.S. State Plane Coordinate System, "EPSG" for the European Petroleum Survey Group, and "UTM" for the Universal Transverse Mercator."""
    _TypeDefinition = CSAuthorityNameKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CSAuthorityName')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 524, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is CSAuthorityNameKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0commonTypes_CSAuthorityName_otherKind', _ImportedBinding__enum.otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 530, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 530, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'CSAuthorityName', CSAuthorityName)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}CSUnits with content type SIMPLE
class CSUnits (pyxb.binding.basis.complexTypeDefinition):
    """This attribute carries the unit of measure for the defined coordinate system. Possible values are "Feet", "Meters", "USSurveyFeet", and "Other".  If the value "Other" is given, the units MUST be specified using the "otherKind" attribute."""
    _TypeDefinition = CSUnitsKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CSUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 562, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is CSUnitsKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0commonTypes_CSUnits_otherKind', _ImportedBinding__enum.otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 568, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 568, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'CSUnits', CSUnits)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}current with content type SIMPLE
class current (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}current with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'current')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 588, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_current_units', _ImportedBinding__enum.currentUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 591, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 591, 4)
    
    units = property(__units.value, __units.set, None, 'Units in which this current is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'current', current)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}detailedAddressFields with content type ELEMENT_ONLY
class detailedAddressFields (mspExtensible):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}detailedAddressFields with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'detailedAddressFields')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 613, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}streetPrefix uses Python identifier streetPrefix
    __streetPrefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetPrefix'), 'streetPrefix', '__httpwww_multispeak_orgV5_0commonTypes_detailedAddressFields_httpwww_multispeak_orgV5_0commonTypesstreetPrefix', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 617, 5), )

    
    streetPrefix = property(__streetPrefix.value, __streetPrefix.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}streetNumber uses Python identifier streetNumber
    __streetNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetNumber'), 'streetNumber', '__httpwww_multispeak_orgV5_0commonTypes_detailedAddressFields_httpwww_multispeak_orgV5_0commonTypesstreetNumber', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 618, 5), )

    
    streetNumber = property(__streetNumber.value, __streetNumber.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}streetSuffix uses Python identifier streetSuffix
    __streetSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetSuffix'), 'streetSuffix', '__httpwww_multispeak_orgV5_0commonTypes_detailedAddressFields_httpwww_multispeak_orgV5_0commonTypesstreetSuffix', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 619, 5), )

    
    streetSuffix = property(__streetSuffix.value, __streetSuffix.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}streetType uses Python identifier streetType
    __streetType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetType'), 'streetType', '__httpwww_multispeak_orgV5_0commonTypes_detailedAddressFields_httpwww_multispeak_orgV5_0commonTypesstreetType', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 620, 5), )

    
    streetType = property(__streetType.value, __streetType.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}buildingNumber uses Python identifier buildingNumber
    __buildingNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'buildingNumber'), 'buildingNumber', '__httpwww_multispeak_orgV5_0commonTypes_detailedAddressFields_httpwww_multispeak_orgV5_0commonTypesbuildingNumber', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 621, 5), )

    
    buildingNumber = property(__buildingNumber.value, __buildingNumber.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}suiteNumber uses Python identifier suiteNumber
    __suiteNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'suiteNumber'), 'suiteNumber', '__httpwww_multispeak_orgV5_0commonTypes_detailedAddressFields_httpwww_multispeak_orgV5_0commonTypessuiteNumber', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 622, 5), )

    
    suiteNumber = property(__suiteNumber.value, __suiteNumber.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}addressGeneral uses Python identifier addressGeneral
    __addressGeneral = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'addressGeneral'), 'addressGeneral', '__httpwww_multispeak_orgV5_0commonTypes_detailedAddressFields_httpwww_multispeak_orgV5_0commonTypesaddressGeneral', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 623, 5), )

    
    addressGeneral = property(__addressGeneral.value, __addressGeneral.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}postOfficeBox uses Python identifier postOfficeBox
    __postOfficeBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postOfficeBox'), 'postOfficeBox', '__httpwww_multispeak_orgV5_0commonTypes_detailedAddressFields_httpwww_multispeak_orgV5_0commonTypespostOfficeBox', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 624, 5), )

    
    postOfficeBox = property(__postOfficeBox.value, __postOfficeBox.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'region'), 'region', '__httpwww_multispeak_orgV5_0commonTypes_detailedAddressFields_httpwww_multispeak_orgV5_0commonTypesregion', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 625, 5), )

    
    region = property(__region.value, __region.set, None, None)

    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    _ElementMap.update({
        __streetPrefix.name() : __streetPrefix,
        __streetNumber.name() : __streetNumber,
        __streetSuffix.name() : __streetSuffix,
        __streetType.name() : __streetType,
        __buildingNumber.name() : __buildingNumber,
        __suiteNumber.name() : __suiteNumber,
        __addressGeneral.name() : __addressGeneral,
        __postOfficeBox.name() : __postOfficeBox,
        __region.name() : __region
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'detailedAddressFields', detailedAddressFields)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}duration with content type SIMPLE
class duration (pyxb.binding.basis.complexTypeDefinition):
    """Time duration."""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'duration')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 630, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_duration_units', _ImportedBinding__enum.timeUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 636, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 636, 4)
    
    units = property(__units.value, __units.set, None, 'Units of time duration.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'duration', duration)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}eMailAddress with content type ELEMENT_ONLY
class eMailAddress (mspExtensible):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}eMailAddress with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'eMailAddress')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 644, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}eMail uses Python identifier eMail
    __eMail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eMail'), 'eMail', '__httpwww_multispeak_orgV5_0commonTypes_eMailAddress_httpwww_multispeak_orgV5_0commonTypeseMail', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 648, 5), )

    
    eMail = property(__eMail.value, __eMail.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}eMailType uses Python identifier eMailType
    __eMailType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eMailType'), 'eMailType', '__httpwww_multispeak_orgV5_0commonTypes_eMailAddress_httpwww_multispeak_orgV5_0commonTypeseMailType', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 649, 5), )

    
    eMailType = property(__eMailType.value, __eMailType.set, None, 'The type of e-mail address.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}priorityOrder uses Python identifier priorityOrder
    __priorityOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'priorityOrder'), 'priorityOrder', '__httpwww_multispeak_orgV5_0commonTypes_eMailAddress_httpwww_multispeak_orgV5_0commonTypespriorityOrder', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 654, 5), )

    
    priorityOrder = property(__priorityOrder.value, __priorityOrder.set, None, 'Order in which these e-mail addresses should be used to contact this person.')

    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    _ElementMap.update({
        __eMail.name() : __eMail,
        __eMailType.name() : __eMailType,
        __priorityOrder.name() : __priorityOrder
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'eMailAddress', eMailAddress)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}equipmentCatalogRef with content type SIMPLE
class equipmentCatalogRef (pyxb.binding.basis.complexTypeDefinition):
    """This is a reference to an engineering equipment catalog entry."""
    _TypeDefinition = _ImportedBinding__prim.MultiSpeakGUID
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equipmentCatalogRef')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 668, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.MultiSpeakGUID
    
    # Attribute equipmentType uses Python identifier equipmentType
    __equipmentType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'equipmentType'), 'equipmentType', '__httpwww_multispeak_orgV5_0commonTypes_equipmentCatalogRef_equipmentType', _ImportedBinding__enum.equipmentTypeKind, required=True)
    __equipmentType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 674, 4)
    __equipmentType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 674, 4)
    
    equipmentType = property(__equipmentType.value, __equipmentType.set, None, 'This is the type of the engineering catalog entry.')

    
    # Attribute entryName uses Python identifier entryName
    __entryName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'entryName'), 'entryName', '__httpwww_multispeak_orgV5_0commonTypes_equipmentCatalogRef_entryName', pyxb.binding.datatypes.string)
    __entryName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 679, 4)
    __entryName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 679, 4)
    
    entryName = property(__entryName.value, __entryName.set, None, 'This is the human-readable name for the specific type of equipment defined by this catalog entry.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __equipmentType.name() : __equipmentType,
        __entryName.name() : __entryName
    })
Namespace.addCategoryObject('typeBinding', 'equipmentCatalogRef', equipmentCatalogRef)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}exponent with content type SIMPLE
class exponent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}exponent with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'exponent')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 717, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_exponent_units', pyxb.binding.datatypes.string, fixed=True, unicode_default='Exponent')
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 720, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 720, 4)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'exponent', exponent)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}extValue with content type SIMPLE
class extValue (pyxb.binding.basis.complexTypeDefinition):
    """This is the value of the extensionsItem.  The units of this extensionsItem are included in the Units attrbute on extValue."""
    _TypeDefinition = _ImportedBinding__prim.stringType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extValue')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 754, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.stringType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_extValue_units', _ImportedBinding__enum.uomKind)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 760, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 760, 4)
    
    units = property(__units.value, __units.set, None, 'If used, this attribute carries the units in which the extValue is expressed. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'extValue', extValue)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}frequency with content type SIMPLE
class frequency (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}frequency with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'frequency')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 768, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_frequency_units', _ImportedBinding__enum.frequencyUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 771, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 771, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the frequency is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'frequency', frequency)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}GPSLocation with content type ELEMENT_ONLY
class GPSLocation (mspExtensible):
    """A geographical location as expressed in a geographic coordinate system. The GPSLocation SHALL be expressed using the WGS84 datum. This object SHOULD be used for expressing all types of GPS data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GPSLocation')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 810, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}latitude uses Python identifier latitude
    __latitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'latitude'), 'latitude', '__httpwww_multispeak_orgV5_0commonTypes_GPSLocation_httpwww_multispeak_orgV5_0commonTypeslatitude', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 817, 5), )

    
    latitude = property(__latitude.value, __latitude.set, None, 'The latitude portion of a geographical location.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'longitude'), 'longitude', '__httpwww_multispeak_orgV5_0commonTypes_GPSLocation_httpwww_multispeak_orgV5_0commonTypeslongitude', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 822, 5), )

    
    longitude = property(__longitude.value, __longitude.set, None, 'The longitude portion of a geographical location.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}altitude uses Python identifier altitude
    __altitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'altitude'), 'altitude', '__httpwww_multispeak_orgV5_0commonTypes_GPSLocation_httpwww_multispeak_orgV5_0commonTypesaltitude', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 827, 5), )

    
    altitude = property(__altitude.value, __altitude.set, None, 'The altitude above mean sea level for this geographical location, assuming the use of the WGS84 datum.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}GPSMetadata uses Python identifier GPSMetadata
    __GPSMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GPSMetadata'), 'GPSMetadata', '__httpwww_multispeak_orgV5_0commonTypes_GPSLocation_httpwww_multispeak_orgV5_0commonTypesGPSMetadata', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 832, 5), )

    
    GPSMetadata = property(__GPSMetadata.value, __GPSMetadata.set, None, 'If it is desirable to send metadata about how this GPSLocation was collected, that data is documented in this element.')

    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Attribute GPSValidity uses Python identifier GPSValidity
    __GPSValidity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GPSValidity'), 'GPSValidity', '__httpwww_multispeak_orgV5_0commonTypes_GPSLocation_GPSValidity', pyxb.binding.datatypes.boolean)
    __GPSValidity._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 838, 4)
    __GPSValidity._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 838, 4)
    
    GPSValidity = property(__GPSValidity.value, __GPSValidity.set, None, 'Validity of GPS location; false = invalid, true = valid.')

    _ElementMap.update({
        __latitude.name() : __latitude,
        __longitude.name() : __longitude,
        __altitude.name() : __altitude,
        __GPSMetadata.name() : __GPSMetadata
    })
    _AttributeMap.update({
        __GPSValidity.name() : __GPSValidity
    })
Namespace.addCategoryObject('typeBinding', 'GPSLocation', GPSLocation)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}GPSMetadata with content type ELEMENT_ONLY
class GPSMetadata (mspExtensible):
    """If it is desirable to send metadata about how this GPSLocation was collected, that data is documented in this element."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GPSMetadata')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 846, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}easting uses Python identifier easting
    __easting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'easting'), 'easting', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypeseasting', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 853, 5), )

    
    easting = property(__easting.value, __easting.set, None, 'Easting for coordinate zone.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}northing uses Python identifier northing
    __northing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'northing'), 'northing', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypesnorthing', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 858, 5), )

    
    northing = property(__northing.value, __northing.set, None, 'Northing for coordinate zone.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypessource', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 863, 5), )

    
    source = property(__source.value, __source.set, None, 'Source of data.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'number'), 'number', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypesnumber', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 868, 5), )

    
    number = property(__number.value, __number.set, None, 'Number of readings that were averaged during the collection of this location.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}isRealTimeDiffCorrection uses Python identifier isRealTimeDiffCorrection
    __isRealTimeDiffCorrection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isRealTimeDiffCorrection'), 'isRealTimeDiffCorrection', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypesisRealTimeDiffCorrection', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 873, 5), )

    
    isRealTimeDiffCorrection = property(__isRealTimeDiffCorrection.value, __isRealTimeDiffCorrection.set, None, 'Has this point been differentially corrected in real time?')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}hdop uses Python identifier hdop
    __hdop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hdop'), 'hdop', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypeshdop', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 878, 5), )

    
    hdop = property(__hdop.value, __hdop.set, None, 'Horizontal dilution of precision.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}vdop uses Python identifier vdop
    __vdop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vdop'), 'vdop', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypesvdop', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 883, 5), )

    
    vdop = property(__vdop.value, __vdop.set, None, 'Vertical dilution of precision.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}diffID uses Python identifier diffID
    __diffID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'diffID'), 'diffID', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypesdiffID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 888, 5), )

    
    diffID = property(__diffID.value, __diffID.set, None, 'The identifier for the source of differential correction signal.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}collected uses Python identifier collected
    __collected = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collected'), 'collected', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypescollected', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 893, 5), )

    
    collected = property(__collected.value, __collected.set, None, 'The date and time that this location was taken.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}numSat uses Python identifier numSat
    __numSat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'numSat'), 'numSat', '__httpwww_multispeak_orgV5_0commonTypes_GPSMetadata_httpwww_multispeak_orgV5_0commonTypesnumSat', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 898, 5), )

    
    numSat = property(__numSat.value, __numSat.set, None, 'Number of satellites visible when this location was taken.')

    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    _ElementMap.update({
        __easting.name() : __easting,
        __northing.name() : __northing,
        __source.name() : __source,
        __number.name() : __number,
        __isRealTimeDiffCorrection.name() : __isRealTimeDiffCorrection,
        __hdop.name() : __hdop,
        __vdop.name() : __vdop,
        __diffID.name() : __diffID,
        __collected.name() : __collected,
        __numSat.name() : __numSat
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GPSMetadata', GPSMetadata)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}height with content type SIMPLE
class height (pyxb.binding.basis.complexTypeDefinition):
    """Value of height expressed in units carried in lengthUnits."""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'height')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 907, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_height_units', _ImportedBinding__enum.lengthUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 913, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 913, 4)
    
    units = property(__units.value, __units.set, None, 'Units of height.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'height', height)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}impedance with content type SIMPLE
class impedance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}impedance with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'impedance')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 921, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_impedance_units', _ImportedBinding__enum.zUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 924, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 924, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the impedance is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'impedance', impedance)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}length with content type SIMPLE
class length (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}length with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'length')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 949, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_length_units', _ImportedBinding__enum.lengthUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 952, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 952, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the length is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'length', length)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}lengthUnitValue with content type SIMPLE
class lengthUnitValue (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}lengthUnitValue with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.doubleType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthUnitValue')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 960, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.doubleType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_lengthUnitValue_units', _ImportedBinding__enum.lengthUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 963, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 963, 4)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'lengthUnitValue', lengthUnitValue)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}meterID with content type SIMPLE
class meterID (pyxb.binding.basis.complexTypeDefinition):
    """This is the identifier for a meter.  The body of the meterID SHALL carry the GUID identifier for the meter.  Additional information, such as the meterName (the primaryIdentifier for a meter instance) or the serviceType MAY also be specified. Note that the meter might be of different service types (for example: electric, gas, propane, water, etc.). """
    _TypeDefinition = _ImportedBinding__prim.MultiSpeakGUID
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'meterID')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 977, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.MultiSpeakGUID
    
    # Attribute meterName uses Python identifier meterName
    __meterName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'meterName'), 'meterName', '__httpwww_multispeak_orgV5_0commonTypes_meterID_meterName', pyxb.binding.datatypes.string)
    __meterName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 983, 4)
    __meterName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 983, 4)
    
    meterName = property(__meterName.value, __meterName.set, None, 'Meter name.  This is a utility-assigned, human readable identifier This identifier SHALL be used in the primaryIdentifier field for any meter.  This value was called meterNo in both Version 3.0 and 4.1.')

    
    # Attribute serviceType uses Python identifier serviceType
    __serviceType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'serviceType'), 'serviceType', '__httpwww_multispeak_orgV5_0commonTypes_meterID_serviceType', _ImportedBinding__enum.serviceKind)
    __serviceType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 988, 4)
    __serviceType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 988, 4)
    
    serviceType = property(__serviceType.value, __serviceType.set, None, 'This identifies the type of service this meter records.  For instance for an electricMeter, the serviceType would be "Electric".  ')

    
    # Attribute otherServiceType uses Python identifier otherServiceType
    __otherServiceType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherServiceType'), 'otherServiceType', '__httpwww_multispeak_orgV5_0commonTypes_meterID_otherServiceType', pyxb.binding.datatypes.string)
    __otherServiceType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 993, 4)
    __otherServiceType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 993, 4)
    
    otherServiceType = property(__otherServiceType.value, __otherServiceType.set, None, 'If no acceptable hard enumeration value is available for serviceType, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    
    # Attribute communicationAddress uses Python identifier communicationAddress
    __communicationAddress = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'communicationAddress'), 'communicationAddress', '__httpwww_multispeak_orgV5_0commonTypes_meterID_communicationAddress', pyxb.binding.datatypes.string)
    __communicationAddress._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 998, 4)
    __communicationAddress._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 998, 4)
    
    communicationAddress = property(__communicationAddress.value, __communicationAddress.set, None, 'This attribute carries the unique address for the communications module (transponder) associated with the meter, if any.')

    
    # Attribute communicationsPort uses Python identifier communicationsPort
    __communicationsPort = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'communicationsPort'), 'communicationsPort', '__httpwww_multispeak_orgV5_0commonTypes_meterID_communicationsPort', pyxb.binding.datatypes.string)
    __communicationsPort._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1003, 4)
    __communicationsPort._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1003, 4)
    
    communicationsPort = property(__communicationsPort.value, __communicationsPort.set, None, 'This is the port identifier on the communications module (transponder) if necessary to communicate with this meter. This attribute is used when multiple meters are addressed using a single communication device (module). This identifier allows the CIS (or other inventory management) system to identify to the AMI system what port a meter is connected to on AMI devices that support multiple meters connected to a single AMI device.')

    
    # Attribute utility uses Python identifier utility
    __utility = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'utility'), 'utility', '__httpwww_multispeak_orgV5_0commonTypes_meterID_utility', pyxb.binding.datatypes.string)
    __utility._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1008, 4)
    __utility._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1008, 4)
    
    utility = property(__utility.value, __utility.set, None, 'A string identifier for the owner (typically a utility) of the meter identified by this meterID.  It may be a text string or a pointer to an organization.  If it is a text string, it is suggested that the string be the Internet domain name for the owner in valid XS:anyURI format.')

    
    # Attribute registeredName uses Python identifier registeredName
    __registeredName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'registeredName'), 'registeredName', '__httpwww_multispeak_orgV5_0commonTypes_meterID_registeredName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __registeredName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1013, 4)
    __registeredName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1013, 4)
    
    registeredName = property(__registeredName.value, __registeredName.set, None, 'This is the registeredName part of the fully-qualified object name of the format GlobalDomain.RegisteredName.SystemName.Noun.objectGUID.')

    
    # Attribute systemName uses Python identifier systemName
    __systemName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'systemName'), 'systemName', '__httpwww_multispeak_orgV5_0commonTypes_meterID_systemName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __systemName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1018, 4)
    __systemName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1018, 4)
    
    systemName = property(__systemName.value, __systemName.set, None, 'This is the systemName part of the fully-qualified object name of the format GlobalDomain.RegisteredName.SystemName.Noun.objectGUID.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __meterName.name() : __meterName,
        __serviceType.name() : __serviceType,
        __otherServiceType.name() : __otherServiceType,
        __communicationAddress.name() : __communicationAddress,
        __communicationsPort.name() : __communicationsPort,
        __utility.name() : __utility,
        __registeredName.name() : __registeredName,
        __systemName.name() : __systemName
    })
Namespace.addCategoryObject('typeBinding', 'meterID', meterID)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}money with content type SIMPLE
class money (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}money with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'money')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1027, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute currencyCode uses Python identifier currencyCode
    __currencyCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'currencyCode'), 'currencyCode', '__httpwww_multispeak_orgV5_0commonTypes_money_currencyCode', _ImportedBinding__enum.currencyCode)
    __currencyCode._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1030, 4)
    __currencyCode._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1030, 4)
    
    currencyCode = property(__currencyCode.value, __currencyCode.set, None, 'Three letter currency code as standardized in ISO4217-2001. Typically is the two letter Internet domain code for the country followed by a one letter designator for the currency; for instance the USA dollar is USD.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __currencyCode.name() : __currencyCode
    })
Namespace.addCategoryObject('typeBinding', 'money', money)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}nodeIdentifier with content type SIMPLE
class nodeIdentifier (pyxb.binding.basis.complexTypeDefinition):
    """This class identifies a node in a connectivity model."""
    _TypeDefinition = _ImportedBinding__prim.MultiSpeakGUID
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nodeIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1109, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.MultiSpeakGUID
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_multispeak_orgV5_0commonTypes_nodeIdentifier_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1115, 4)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1115, 4)
    
    name = property(__name.value, __name.set, None, 'Name for engineering node.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'nodeIdentifier', nodeIdentifier)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}nounSpecifiedMultiPartIdentifier with content type ELEMENT_ONLY
class nounSpecifiedMultiPartIdentifier (multiPartIdentifier):
    """The nounSpecifiedMultiPartIdentifier is used to identify an object when (i) the noun type is not known in advance and hence the noun type must be specified in the message payload, (iii) it is not necessary or desirable to use a GUID to refer to the data instance, and (iii) one or more string identifiers are needed to uniquely specify the desired data instance."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nounSpecifiedMultiPartIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1123, 1)
    _ElementMap = multiPartIdentifier._ElementMap.copy()
    _AttributeMap = multiPartIdentifier._AttributeMap.copy()
    # Base type is multiPartIdentifier
    
    # Element primaryIdentifier ({http://www.multispeak.org/V5.0/commonTypes}primaryIdentifier) inherited from {http://www.multispeak.org/V5.0/commonTypes}multiPartIdentifier
    
    # Element secondaryIdentifier ({http://www.multispeak.org/V5.0/commonTypes}secondaryIdentifier) inherited from {http://www.multispeak.org/V5.0/commonTypes}multiPartIdentifier
    
    # Attribute identifierKind uses Python identifier identifierKind
    __identifierKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'identifierKind'), 'identifierKind', '__httpwww_multispeak_orgV5_0commonTypes_nounSpecifiedMultiPartIdentifier_identifierKind', pyxb.binding.datatypes.string, required=True)
    __identifierKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1129, 4)
    __identifierKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1129, 4)
    
    identifierKind = property(__identifierKind.value, __identifierKind.set, None, 'Type of identifier to follow.  Potential examples of this identifier are:"Work order", "Service order", "Outage ticket", "Other" and "Unknown".')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __identifierKind.name() : __identifierKind
    })
Namespace.addCategoryObject('typeBinding', 'nounSpecifiedMultiPartIdentifier', nounSpecifiedMultiPartIdentifier)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}objectRef with content type SIMPLE
class objectRef (pyxb.binding.basis.complexTypeDefinition):
    """This is a reference to any type of object.  An objectRef is used as an objectIdentifier when the noun type is not necessarily known in advance and hence must be specified in the message payload.   An objectRef is a HARD, NOUN-SPECIFIED object identifier."""
    _TypeDefinition = _ImportedBinding__prim.MultiSpeakGUID
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'objectRef')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1172, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.MultiSpeakGUID
    
    # Attribute primaryIdentifierValue uses Python identifier primaryIdentifierValue
    __primaryIdentifierValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'primaryIdentifierValue'), 'primaryIdentifierValue', '__httpwww_multispeak_orgV5_0commonTypes_objectRef_primaryIdentifierValue', pyxb.binding.datatypes.string)
    __primaryIdentifierValue._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1178, 4)
    __primaryIdentifierValue._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1178, 4)
    
    primaryIdentifierValue = property(__primaryIdentifierValue.value, __primaryIdentifierValue.set, None, 'Primary human-readable identifier for this instance of the object. ')

    
    # Attribute secondaryIdentifierValue uses Python identifier secondaryIdentifierValue
    __secondaryIdentifierValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'secondaryIdentifierValue'), 'secondaryIdentifierValue', '__httpwww_multispeak_orgV5_0commonTypes_objectRef_secondaryIdentifierValue', pyxb.binding.datatypes.string)
    __secondaryIdentifierValue._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1183, 4)
    __secondaryIdentifierValue._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1183, 4)
    
    secondaryIdentifierValue = property(__secondaryIdentifierValue.value, __secondaryIdentifierValue.set, None, 'Additional human-readable identifier for this instance of the object. When the secondaryIdentifier is provided, it is expected that the union of the primary and secondary identifiers is necessary to uniquely identify a data instance and both shall be used.')

    
    # Attribute noun uses Python identifier noun
    __noun = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'noun'), 'noun', '__httpwww_multispeak_orgV5_0commonTypes_objectRef_noun', pyxb.binding.datatypes.QName, required=True)
    __noun._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1188, 4)
    __noun._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1188, 4)
    
    noun = property(__noun.value, __noun.set, None, 'The noun is the name of the object type that includes this instance.  For example, if instance is described by the MultiSpeak "substation" object then this field will contain "substation".')

    
    # Attribute utility uses Python identifier utility
    __utility = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'utility'), 'utility', '__httpwww_multispeak_orgV5_0commonTypes_objectRef_utility', pyxb.binding.datatypes.string)
    __utility._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1193, 4)
    __utility._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1193, 4)
    
    utility = property(__utility.value, __utility.set, None, 'String that is used to identify the utility associated with this item. It may be a text string or a pointer to an organization.  If it is a text string, it is suggested that the string be the Internet domain name for the owner in valid XS:anyURI format.')

    
    # Attribute registeredName uses Python identifier registeredName
    __registeredName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'registeredName'), 'registeredName', '__httpwww_multispeak_orgV5_0commonTypes_objectRef_registeredName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __registeredName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1198, 4)
    __registeredName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1198, 4)
    
    registeredName = property(__registeredName.value, __registeredName.set, None, 'This is the registeredName part of the fully-qualified object name of the format GlobalDomain.RegisteredName.SystemName.Noun.objectGUID.')

    
    # Attribute systemName uses Python identifier systemName
    __systemName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'systemName'), 'systemName', '__httpwww_multispeak_orgV5_0commonTypes_objectRef_systemName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __systemName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1203, 4)
    __systemName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1203, 4)
    
    systemName = property(__systemName.value, __systemName.set, None, 'This is the systemName part of the fully-qualified object name of the format GlobalDomain.RegisteredName.SystemName.Noun.objectGUID.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __primaryIdentifierValue.name() : __primaryIdentifierValue,
        __secondaryIdentifierValue.name() : __secondaryIdentifierValue,
        __noun.name() : __noun,
        __utility.name() : __utility,
        __registeredName.name() : __registeredName,
        __systemName.name() : __systemName
    })
Namespace.addCategoryObject('typeBinding', 'objectRef', objectRef)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}odometer with content type SIMPLE
class odometer (pyxb.binding.basis.complexTypeDefinition):
    """Odometer reading."""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'odometer')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1212, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute odometerReadingType uses Python identifier odometerReadingType
    __odometerReadingType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'odometerReadingType'), 'odometerReadingType', '__httpwww_multispeak_orgV5_0commonTypes_odometer_odometerReadingType', _ImportedBinding__enum.odometerReadingType)
    __odometerReadingType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1218, 4)
    __odometerReadingType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1218, 4)
    
    odometerReadingType = property(__odometerReadingType.value, __odometerReadingType.set, None, None)

    
    # Attribute otherOdometerReadingType uses Python identifier otherOdometerReadingType
    __otherOdometerReadingType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherOdometerReadingType'), 'otherOdometerReadingType', '__httpwww_multispeak_orgV5_0commonTypes_odometer_otherOdometerReadingType', pyxb.binding.datatypes.string)
    __otherOdometerReadingType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1219, 4)
    __otherOdometerReadingType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1219, 4)
    
    otherOdometerReadingType = property(__otherOdometerReadingType.value, __otherOdometerReadingType.set, None, 'If the enumeration value chose in the odometerReadingType is "Other" the actual value should be specified here.')

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_odometer_units', _ImportedBinding__enum.lengthUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1224, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1224, 4)
    
    units = property(__units.value, __units.set, None, 'Units that the odometer reading is expressed in.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __odometerReadingType.name() : __odometerReadingType,
        __otherOdometerReadingType.name() : __otherOdometerReadingType,
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'odometer', odometer)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}otherContactItem with content type ELEMENT_ONLY
class otherContactItem (mspExtensible):
    """This is an element to carry other miscellaneous contact information, such as web site address, truck radio number, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'otherContactItem')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1237, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}details uses Python identifier details
    __details = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'details'), 'details', '__httpwww_multispeak_orgV5_0commonTypes_otherContactItem_httpwww_multispeak_orgV5_0commonTypesdetails', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1244, 5), )

    
    details = property(__details.value, __details.set, None, 'This element carries the miscellaneous contact information.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}infoType uses Python identifier infoType
    __infoType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infoType'), 'infoType', '__httpwww_multispeak_orgV5_0commonTypes_otherContactItem_httpwww_multispeak_orgV5_0commonTypesinfoType', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1249, 5), )

    
    infoType = property(__infoType.value, __infoType.set, None, 'This element is used to describe the type of information stored in the "details" element.  Examples might be: IP address, truck number, radio number.')

    _ElementMap.update({
        __details.name() : __details,
        __infoType.name() : __infoType
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'otherContactItem', otherContactItem)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}phoneNumber with content type ELEMENT_ONLY
class phoneNumber (mspExtensible):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}phoneNumber with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phoneNumber')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1258, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phone'), 'phone', '__httpwww_multispeak_orgV5_0commonTypes_phoneNumber_httpwww_multispeak_orgV5_0commonTypesphone', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1262, 5), )

    
    phone = property(__phone.value, __phone.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}phoneType uses Python identifier phoneType
    __phoneType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phoneType'), 'phoneType', '__httpwww_multispeak_orgV5_0commonTypes_phoneNumber_httpwww_multispeak_orgV5_0commonTypesphoneType', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1263, 5), )

    
    phoneType = property(__phoneType.value, __phoneType.set, None, 'The type of phone number.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}priorityOrder uses Python identifier priorityOrder
    __priorityOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'priorityOrder'), 'priorityOrder', '__httpwww_multispeak_orgV5_0commonTypes_phoneNumber_httpwww_multispeak_orgV5_0commonTypespriorityOrder', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1268, 5), )

    
    priorityOrder = property(__priorityOrder.value, __priorityOrder.set, None, 'Order in which these phone numbers should be used to contact this person.')

    _ElementMap.update({
        __phone.name() : __phone,
        __phoneType.name() : __phoneType,
        __priorityOrder.name() : __priorityOrder
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'phoneNumber', phoneNumber)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}pressure with content type SIMPLE
class pressure (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}pressure with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pressure')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1282, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_pressure_units', _ImportedBinding__enum.pressureUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1285, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1285, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the pressure is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'pressure', pressure)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}reactance with content type SIMPLE
class reactance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}reactance with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reactance')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1310, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_reactance_units', _ImportedBinding__enum.zUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1313, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1313, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which this reactance is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'reactance', reactance)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}reactancePerUnitLength with content type SIMPLE
class reactancePerUnitLength (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}reactancePerUnitLength with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reactancePerUnitLength')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1321, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute reactanceUnits uses Python identifier reactanceUnits
    __reactanceUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reactanceUnits'), 'reactanceUnits', '__httpwww_multispeak_orgV5_0commonTypes_reactancePerUnitLength_reactanceUnits', _ImportedBinding__enum.zUnits)
    __reactanceUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1324, 4)
    __reactanceUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1324, 4)
    
    reactanceUnits = property(__reactanceUnits.value, __reactanceUnits.set, None, 'The units in wich the reactance is expressed.')

    
    # Attribute lengthUnits uses Python identifier lengthUnits
    __lengthUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lengthUnits'), 'lengthUnits', '__httpwww_multispeak_orgV5_0commonTypes_reactancePerUnitLength_lengthUnits', _ImportedBinding__enum.lengthUnits)
    __lengthUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1329, 4)
    __lengthUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1329, 4)
    
    lengthUnits = property(__lengthUnits.value, __lengthUnits.set, None, 'The units in which the reference length is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reactanceUnits.name() : __reactanceUnits,
        __lengthUnits.name() : __lengthUnits
    })
Namespace.addCategoryObject('typeBinding', 'reactancePerUnitLength', reactancePerUnitLength)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}reactiveEnergy with content type SIMPLE
class reactiveEnergy (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}reactiveEnergy with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reactiveEnergy')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1337, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_reactiveEnergy_units', _ImportedBinding__enum.reactiveEnergyUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1340, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1340, 4)
    
    units = property(__units.value, __units.set, None, 'Units in which this reactive energy is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'reactiveEnergy', reactiveEnergy)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}reactivePower with content type SIMPLE
class reactivePower (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}reactivePower with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reactivePower')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1348, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_reactivePower_units', _ImportedBinding__enum.reactivePowerUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1351, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1351, 4)
    
    units = property(__units.value, __units.set, None, 'Units in which this reactive power is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'reactivePower', reactivePower)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}realEnergy with content type SIMPLE
class realEnergy (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}realEnergy with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'realEnergy')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1359, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_realEnergy_units', _ImportedBinding__enum.realEnergyUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1362, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1362, 4)
    
    units = property(__units.value, __units.set, None, 'Units in which this real energy is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'realEnergy', realEnergy)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}realPower with content type SIMPLE
class realPower (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}realPower with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'realPower')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1370, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_realPower_units', _ImportedBinding__enum.realPowerUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1373, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1373, 4)
    
    units = property(__units.value, __units.set, None, 'Units in which this real power is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'realPower', realPower)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}requestedCoordinateSystem with content type ELEMENT_ONLY
class requestedCoordinateSystem (CoordinateSystemInformation):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}requestedCoordinateSystem with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'requestedCoordinateSystem')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1409, 1)
    _ElementMap = CoordinateSystemInformation._ElementMap.copy()
    _AttributeMap = CoordinateSystemInformation._AttributeMap.copy()
    # Base type is CoordinateSystemInformation
    
    # Element CSUnits ({http://www.multispeak.org/V5.0/commonTypes}CSUnits) inherited from {http://www.multispeak.org/V5.0/commonTypes}CoordinateSystemInformation
    
    # Element CSAuthorities ({http://www.multispeak.org/V5.0/commonTypes}CSAuthorities) inherited from {http://www.multispeak.org/V5.0/commonTypes}CoordinateSystemInformation
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'requestedCoordinateSystem', requestedCoordinateSystem)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}resistance with content type SIMPLE
class resistance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}resistance with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resistance')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1423, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_resistance_units', _ImportedBinding__enum.zUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1426, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1426, 4)
    
    units = property(__units.value, __units.set, None, 'Units in which this resistance is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'resistance', resistance)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}resistancePerUnitLength with content type SIMPLE
class resistancePerUnitLength (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}resistancePerUnitLength with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resistancePerUnitLength')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1434, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute resistanceUnits uses Python identifier resistanceUnits
    __resistanceUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'resistanceUnits'), 'resistanceUnits', '__httpwww_multispeak_orgV5_0commonTypes_resistancePerUnitLength_resistanceUnits', _ImportedBinding__enum.zUnits)
    __resistanceUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1437, 4)
    __resistanceUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1437, 4)
    
    resistanceUnits = property(__resistanceUnits.value, __resistanceUnits.set, None, 'Units in which this resistance is measured.')

    
    # Attribute lengthUnits uses Python identifier lengthUnits
    __lengthUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lengthUnits'), 'lengthUnits', '__httpwww_multispeak_orgV5_0commonTypes_resistancePerUnitLength_lengthUnits', _ImportedBinding__enum.lengthUnits)
    __lengthUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1442, 4)
    __lengthUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1442, 4)
    
    lengthUnits = property(__lengthUnits.value, __lengthUnits.set, None, 'Units for the reference length.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __resistanceUnits.name() : __resistanceUnits,
        __lengthUnits.name() : __lengthUnits
    })
Namespace.addCategoryObject('typeBinding', 'resistancePerUnitLength', resistancePerUnitLength)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}resistivity with content type SIMPLE
class resistivity (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}resistivity with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resistivity')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1450, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_resistivity_units', _ImportedBinding__enum.resistivityUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1453, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1453, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the resistivity is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'resistivity', resistivity)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}seconds with content type SIMPLE
class seconds (pyxb.binding.basis.complexTypeDefinition):
    """Time expressed in seconds"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'seconds')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1496, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_seconds_units', pyxb.binding.datatypes.string, fixed=True, unicode_default='Seconds')
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1502, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1502, 4)
    
    units = property(__units.value, __units.set, None, '"Seconds"')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'seconds', seconds)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}servicePointID with content type SIMPLE
class servicePointID (pyxb.binding.basis.complexTypeDefinition):
    """This is a reference for a customer service point.  A service point is located at a customer service location and applies to a specific service type (electric, gas, water, etc.).  Service points may be of different classes, for instance electricServicePoint, waterServicePoint, gasServicePoint, etc.).  Hence to completely identify a service point, it is necessary to know the type of service and the objectID of that type of service point. The servicePointID should include the concatenated string consisting of serviceType.objectID."""
    _TypeDefinition = _ImportedBinding__prim.MultiSpeakGUID
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'servicePointID')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1510, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.MultiSpeakGUID
    
    # Attribute serviceType uses Python identifier serviceType
    __serviceType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'serviceType'), 'serviceType', '__httpwww_multispeak_orgV5_0commonTypes_servicePointID_serviceType', _ImportedBinding__enum.serviceKind)
    __serviceType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1516, 4)
    __serviceType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1516, 4)
    
    serviceType = property(__serviceType.value, __serviceType.set, None, 'Service type is an enumeration that describes the class of utility service (electric, gas, water, etc.).')

    
    # Attribute otherServiceType uses Python identifier otherServiceType
    __otherServiceType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherServiceType'), 'otherServiceType', '__httpwww_multispeak_orgV5_0commonTypes_servicePointID_otherServiceType', pyxb.binding.datatypes.string)
    __otherServiceType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1521, 4)
    __otherServiceType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1521, 4)
    
    otherServiceType = property(__otherServiceType.value, __otherServiceType.set, None, 'If no acceptable hard enumeration value is available for serviceType, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    
    # Attribute utility uses Python identifier utility
    __utility = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'utility'), 'utility', '__httpwww_multispeak_orgV5_0commonTypes_servicePointID_utility', pyxb.binding.datatypes.string)
    __utility._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1526, 4)
    __utility._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1526, 4)
    
    utility = property(__utility.value, __utility.set, None, 'String that is used to identify the owner of this item.  It may be a text string or a pointer to an organization.  If it is a text string, it is suggested that the string be the Internet domain name for the owner in valid XS:anyURI format. ')

    
    # Attribute registeredName uses Python identifier registeredName
    __registeredName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'registeredName'), 'registeredName', '__httpwww_multispeak_orgV5_0commonTypes_servicePointID_registeredName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __registeredName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1531, 4)
    __registeredName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1531, 4)
    
    registeredName = property(__registeredName.value, __registeredName.set, None, 'This is the registeredName part of the fully-qualified object name of the format GlobalDomain.RegisteredName.SystemName.Noun.objectGUID.')

    
    # Attribute systemName uses Python identifier systemName
    __systemName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'systemName'), 'systemName', '__httpwww_multispeak_orgV5_0commonTypes_servicePointID_systemName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __systemName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1536, 4)
    __systemName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1536, 4)
    
    systemName = property(__systemName.value, __systemName.set, None, 'This is the systemName part of the fully-qualified object name of the format GlobalDomain.RegisteredName.SystemName.Noun.objectGUID.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __serviceType.name() : __serviceType,
        __otherServiceType.name() : __otherServiceType,
        __utility.name() : __utility,
        __registeredName.name() : __registeredName,
        __systemName.name() : __systemName
    })
Namespace.addCategoryObject('typeBinding', 'servicePointID', servicePointID)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}singleIdentifier with content type SIMPLE
class singleIdentifier (pyxb.binding.basis.complexTypeDefinition):
    """This is a class of string identifer.  The identifier value for a data instance goes in the element that inherits from this complexType.  The identifierName is the commonly used human-readable identifier name assigned by the sysem of record for this type of object and the identifierLabel is the string value that would be displayed to a user to describe the context of this identifier type.  For instance, for a customer account object, the system of record might consider the accountNumber to be the primary human-readable identifier.  Also, in previous versions, MultiSpeak included methods such as GetAllMetersByAccountNumber, which implies that this is expected to be a unique identifier.  Thus the identifierName would be "accountNumber" and the identifierLabel might be "Account Number".  """
    _TypeDefinition = _ImportedBinding__prim.stringType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'singleIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1550, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.stringType
    
    # Attribute identifierName uses Python identifier identifierName
    __identifierName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'identifierName'), 'identifierName', '__httpwww_multispeak_orgV5_0commonTypes_singleIdentifier_identifierName', pyxb.binding.datatypes.string, required=True)
    __identifierName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1556, 4)
    __identifierName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1556, 4)
    
    identifierName = property(__identifierName.value, __identifierName.set, None, 'This is the name of the human-readable identifier by which the system of record knows an instance of this object.  For instance, for a customer account object, the system of record might consider the accountNumber to be the primary human-readable identifier.  Also, in previous versions, MultiSpeak included methods such as GetMetersByAccountNumber, which implies that this human-readable identifier was expected to be a unique value.  Thus the identifierName for the account object would be "accountNumber".   If this identifierName is not applicable to a specific data instance than fill this field with "NA".')

    
    # Attribute identifierLabel uses Python identifier identifierLabel
    __identifierLabel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'identifierLabel'), 'identifierLabel', '__httpwww_multispeak_orgV5_0commonTypes_singleIdentifier_identifierLabel', pyxb.binding.datatypes.string)
    __identifierLabel._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1561, 4)
    __identifierLabel._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1561, 4)
    
    identifierLabel = property(__identifierLabel.value, __identifierLabel.set, None, 'If desired, this string will be displayed to the user as a reference for this identifier. For instance, for a meter, the identifierLabel for the primaryIdentifer might be "Meter Number".  For a workOrder, the identifierLabel for the secondaryIdentifier might be "Job Number".')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __identifierName.name() : __identifierName,
        __identifierLabel.name() : __identifierLabel
    })
Namespace.addCategoryObject('typeBinding', 'singleIdentifier', singleIdentifier)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}speed with content type SIMPLE
class speed (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}speed with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'speed')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1569, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_speed_units', _ImportedBinding__enum.speedUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1572, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1572, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the speed is measured.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'speed', speed)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}substationRef with content type SIMPLE
class substationRef (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}substationRef with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.MultiSpeakGUID
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'substationRef')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1580, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.MultiSpeakGUID
    
    # Attribute substationCode uses Python identifier substationCode
    __substationCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'substationCode'), 'substationCode', '__httpwww_multispeak_orgV5_0commonTypes_substationRef_substationCode', pyxb.binding.datatypes.string)
    __substationCode._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1583, 4)
    __substationCode._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1583, 4)
    
    substationCode = property(__substationCode.value, __substationCode.set, None, 'A alphanumeric code that refers to this substation.')

    
    # Attribute substationName uses Python identifier substationName
    __substationName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'substationName'), 'substationName', '__httpwww_multispeak_orgV5_0commonTypes_substationRef_substationName', pyxb.binding.datatypes.string, required=True)
    __substationName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1588, 4)
    __substationName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1588, 4)
    
    substationName = property(__substationName.value, __substationName.set, None, 'This is the utility-defined, human-friendly name for this substation.')

    
    # Attribute utility uses Python identifier utility
    __utility = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'utility'), 'utility', '__httpwww_multispeak_orgV5_0commonTypes_substationRef_utility', pyxb.binding.datatypes.string)
    __utility._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1593, 4)
    __utility._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1593, 4)
    
    utility = property(__utility.value, __utility.set, None, 'This is a string identifier for the utility to which this substation pertains.')

    
    # Attribute registeredName uses Python identifier registeredName
    __registeredName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'registeredName'), 'registeredName', '__httpwww_multispeak_orgV5_0commonTypes_substationRef_registeredName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __registeredName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1598, 4)
    __registeredName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1598, 4)
    
    registeredName = property(__registeredName.value, __registeredName.set, None, 'This is the registeredName part of the fully-qualified object name of the format: GlobalDomain.RegisteredName.SystemName.Noun.objectGUID.')

    
    # Attribute systemName uses Python identifier systemName
    __systemName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'systemName'), 'systemName', '__httpwww_multispeak_orgV5_0commonTypes_substationRef_systemName', _ImportedBinding__prim.alphaNumericRestrictedString)
    __systemName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1603, 4)
    __systemName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1603, 4)
    
    systemName = property(__systemName.value, __systemName.set, None, 'This is the registeredName part of the fully-qualified object name of the format: GlobalDomain.RegisteredName.SystemName.Noun.objectGUID.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __substationCode.name() : __substationCode,
        __substationName.name() : __substationName,
        __utility.name() : __utility,
        __registeredName.name() : __registeredName,
        __systemName.name() : __systemName
    })
Namespace.addCategoryObject('typeBinding', 'substationRef', substationRef)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}susceptance with content type SIMPLE
class susceptance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}susceptance with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'susceptance')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1612, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_susceptance_units', _ImportedBinding__enum.sUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1615, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1615, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which this suseptance is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'susceptance', susceptance)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}telephoneNumber with content type ELEMENT_ONLY
class telephoneNumber (mspExtensible):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}telephoneNumber with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'telephoneNumber')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1623, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}areaCode uses Python identifier areaCode
    __areaCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'areaCode'), 'areaCode', '__httpwww_multispeak_orgV5_0commonTypes_telephoneNumber_httpwww_multispeak_orgV5_0commonTypesareaCode', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1627, 5), )

    
    areaCode = property(__areaCode.value, __areaCode.set, None, 'Area or region code.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}cityCode uses Python identifier cityCode
    __cityCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cityCode'), 'cityCode', '__httpwww_multispeak_orgV5_0commonTypes_telephoneNumber_httpwww_multispeak_orgV5_0commonTypescityCode', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1632, 5), )

    
    cityCode = property(__cityCode.value, __cityCode.set, None, 'City code for telephone number, if applicable.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httpwww_multispeak_orgV5_0commonTypes_telephoneNumber_httpwww_multispeak_orgV5_0commonTypescountryCode', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1637, 5), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, 'Country code for telephone number, if applicable.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}localNumber uses Python identifier localNumber
    __localNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'localNumber'), 'localNumber', '__httpwww_multispeak_orgV5_0commonTypes_telephoneNumber_httpwww_multispeak_orgV5_0commonTypeslocalNumber', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1642, 5), )

    
    localNumber = property(__localNumber.value, __localNumber.set, None, 'The primary portion of a telephone number as dialed in a local calling area.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}extension uses Python identifier extension
    __extension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extension'), 'extension', '__httpwww_multispeak_orgV5_0commonTypes_telephoneNumber_httpwww_multispeak_orgV5_0commonTypesextension', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1647, 5), )

    
    extension = property(__extension.value, __extension.set, None, 'Extension for telephone number if required.')

    _ElementMap.update({
        __areaCode.name() : __areaCode,
        __cityCode.name() : __cityCode,
        __countryCode.name() : __countryCode,
        __localNumber.name() : __localNumber,
        __extension.name() : __extension
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'telephoneNumber', telephoneNumber)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}temperature with content type SIMPLE
class temperature (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}temperature with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'temperature')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1656, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_temperature_units', _ImportedBinding__enum.temperatureUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1659, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1659, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the temperature is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'temperature', temperature)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}thermalCoefficientOfResistance with content type SIMPLE
class thermalCoefficientOfResistance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}thermalCoefficientOfResistance with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermalCoefficientOfResistance')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1667, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_thermalCoefficientOfResistance_units', _ImportedBinding__enum.thermalCoefficientOfResistanceUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1670, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1670, 4)
    
    units = property(__units.value, __units.set, None, 'Units of temperature coefficient.  It is suggested that temperatures are expressed in degrees C and that the coefficient is expressed in reciprocal degrees C.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'thermalCoefficientOfResistance', thermalCoefficientOfResistance)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}thickness with content type SIMPLE
class thickness (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}thickness with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thickness')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1678, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_thickness_units', _ImportedBinding__enum.thicknessUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1681, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1681, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the thickness is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'thickness', thickness)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}time with content type SIMPLE
class time (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}time with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'time')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1689, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_time_units', _ImportedBinding__enum.timeUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1692, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1692, 4)
    
    units = property(__units.value, __units.set, None, 'Units of time')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'time', time)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}timeZone with content type SIMPLE
class timeZone (pyxb.binding.basis.complexTypeDefinition):
    """This is the time zone for this location.  The time zone designator goes in the element, the attributes optioanlly give additional information about this time zone.  For instance the time zine for Denver, Colorado, USA is MT (Mountain Time).  Daylight savings time is enabled in Denver, so DSTEnabled = 1 or true.  The MT time zone is UTC - 7.00 hours when DST is not in effect, so the UTCOffest would be "-7.00".  On the other hand, Phoenix is also in the Moutain Time zone, but DST is not employed in Arizona.  For the case of Phoenix, all of the settings would be the same as for Denver, except that DSTEnabled would be false.  The standard civilian time zones (e.g., AT,ET,CT, MT, PT, and AKT for North America) are included for all global locations as are the military time zone designations (e.g. Z, A, B...). """
    _TypeDefinition = _ImportedBinding__prim.stringType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeZone')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1706, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.stringType
    
    # Attribute DSTEnabled uses Python identifier DSTEnabled
    __DSTEnabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DSTEnabled'), 'DSTEnabled', '__httpwww_multispeak_orgV5_0commonTypes_timeZone_DSTEnabled', pyxb.binding.datatypes.boolean)
    __DSTEnabled._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1712, 4)
    __DSTEnabled._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1712, 4)
    
    DSTEnabled = property(__DSTEnabled.value, __DSTEnabled.set, None, 'This attribute determines if daylight savings time is enabled at this location.  If DSTEnabled is false then DST offsets are not used at this location.  Standard date ranges for DST effectiveness and DST offsets are assumed for this location.')

    
    # Attribute UTCOffset uses Python identifier UTCOffset
    __UTCOffset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UTCOffset'), 'UTCOffset', '__httpwww_multispeak_orgV5_0commonTypes_timeZone_UTCOffset', pyxb.binding.datatypes.decimal, required=True)
    __UTCOffset._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1717, 4)
    __UTCOffset._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1717, 4)
    
    UTCOffset = property(__UTCOffset.value, __UTCOffset.set, None, 'This is the offset in decimal hours from Universal Coordinated Time (UTC) for this timezone when daylight savings time is not in effect.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_multispeak_orgV5_0commonTypes_timeZone_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1722, 4)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1722, 4)
    
    name = property(__name.value, __name.set, None, 'Display name for this time zone.')

    
    # Attribute comment uses Python identifier comment
    __comment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'comment'), 'comment', '__httpwww_multispeak_orgV5_0commonTypes_timeZone_comment', pyxb.binding.datatypes.string)
    __comment._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1727, 4)
    __comment._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1727, 4)
    
    comment = property(__comment.value, __comment.set, None, 'Additional information about this time zone.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __DSTEnabled.name() : __DSTEnabled,
        __UTCOffset.name() : __UTCOffset,
        __name.name() : __name,
        __comment.name() : __comment
    })
Namespace.addCategoryObject('typeBinding', 'timeZone', timeZone)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}utilityInfo with content type ELEMENT_ONLY
class utilityInfo (mspExtensible):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}utilityInfo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'utilityInfo')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1735, 1)
    _ElementMap = mspExtensible._ElementMap.copy()
    _AttributeMap = mspExtensible._AttributeMap.copy()
    # Base type is mspExtensible
    
    # Element extensions ({http://www.multispeak.org/V5.0/commonTypes}extensions) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element extensionsList ({http://www.multispeak.org/V5.0/commonTypes}extensionsList) inherited from {http://www.multispeak.org/V5.0/commonTypes}mspExtensible
    
    # Element {http://www.multispeak.org/V5.0/commonTypes}owner uses Python identifier owner
    __owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'owner'), 'owner', '__httpwww_multispeak_orgV5_0commonTypes_utilityInfo_httpwww_multispeak_orgV5_0commonTypesowner', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1739, 5), )

    
    owner = property(__owner.value, __owner.set, None, 'This is the owner of the physical device.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}serviceLocationID uses Python identifier serviceLocationID
    __serviceLocationID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceLocationID'), 'serviceLocationID', '__httpwww_multispeak_orgV5_0commonTypes_utilityInfo_httpwww_multispeak_orgV5_0commonTypesserviceLocationID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1744, 5), )

    
    serviceLocationID = property(__serviceLocationID.value, __serviceLocationID.set, None, 'This is the objectID of the service location at which this device is installed.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}servicePointID uses Python identifier servicePointID
    __servicePointID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'servicePointID'), 'servicePointID', '__httpwww_multispeak_orgV5_0commonTypes_utilityInfo_httpwww_multispeak_orgV5_0commonTypesservicePointID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1749, 5), )

    
    servicePointID = property(__servicePointID.value, __servicePointID.set, None, 'This is a pointer to the service point at which this meter is installed')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}accountID uses Python identifier accountID
    __accountID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accountID'), 'accountID', '__httpwww_multispeak_orgV5_0commonTypes_utilityInfo_httpwww_multispeak_orgV5_0commonTypesaccountID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1754, 5), )

    
    accountID = property(__accountID.value, __accountID.set, None, 'This is a pointer to the customer account for this serviceLocation. This SHALL be the objectID of the associated account object.  If the acountNumber is different than the objectGUID for this data instance of account, then the accountNumber may be carried in the accountID.primaryIdentifier element.')

    
    # Element {http://www.multispeak.org/V5.0/commonTypes}customerID uses Python identifier customerID
    __customerID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerID'), 'customerID', '__httpwww_multispeak_orgV5_0commonTypes_utilityInfo_httpwww_multispeak_orgV5_0commonTypescustomerID', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1759, 5), )

    
    customerID = property(__customerID.value, __customerID.set, None, 'This is the objectID of the customer with which this device is associated.')

    _ElementMap.update({
        __owner.name() : __owner,
        __serviceLocationID.name() : __serviceLocationID,
        __servicePointID.name() : __servicePointID,
        __accountID.name() : __accountID,
        __customerID.name() : __customerID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'utilityInfo', utilityInfo)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}voltage with content type SIMPLE
class voltage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}voltage with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'voltage')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1768, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_voltage_units', _ImportedBinding__enum.voltageUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1771, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1771, 4)
    
    units = property(__units.value, __units.set, None, 'Units of voltage')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'voltage', voltage)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}weight with content type SIMPLE
class weight (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}weight with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'weight')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1779, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__httpwww_multispeak_orgV5_0commonTypes_weight_units', _ImportedBinding__enum.weightUnits)
    __units._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1782, 4)
    __units._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1782, 4)
    
    units = property(__units.value, __units.set, None, 'The units in which the weight is expressed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })
Namespace.addCategoryObject('typeBinding', 'weight', weight)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}weightPerLength with content type SIMPLE
class weightPerLength (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}weightPerLength with content type SIMPLE"""
    _TypeDefinition = _ImportedBinding__prim.floatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'weightPerLength')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1790, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__prim.floatType
    
    # Attribute weightUnits uses Python identifier weightUnits
    __weightUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'weightUnits'), 'weightUnits', '__httpwww_multispeak_orgV5_0commonTypes_weightPerLength_weightUnits', _ImportedBinding__enum.weightUnits)
    __weightUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1793, 4)
    __weightUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1793, 4)
    
    weightUnits = property(__weightUnits.value, __weightUnits.set, None, 'The units in which the weight is expressed.')

    
    # Attribute lengthUnits uses Python identifier lengthUnits
    __lengthUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lengthUnits'), 'lengthUnits', '__httpwww_multispeak_orgV5_0commonTypes_weightPerLength_lengthUnits', _ImportedBinding__enum.lengthUnits)
    __lengthUnits._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1798, 4)
    __lengthUnits._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1798, 4)
    
    lengthUnits = property(__lengthUnits.value, __lengthUnits.set, None, 'The units used to express the reference length.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __weightUnits.name() : __weightUnits,
        __lengthUnits.name() : __lengthUnits
    })
Namespace.addCategoryObject('typeBinding', 'weightPerLength', weightPerLength)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}GMLLine with content type ELEMENT_ONLY
class GMLLine (_ImportedBinding__gml.LineStringType):
    """Complex type {http://www.multispeak.org/V5.0/commonTypes}GMLLine with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GMLLine')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 779, 1)
    _ElementMap = _ImportedBinding__gml.LineStringType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__gml.LineStringType._AttributeMap.copy()
    # Base type is _ImportedBinding__gml.LineStringType
    
    # Element coord ({http://www.multispeak.org/V5.0/gml}coord) inherited from {http://www.multispeak.org/V5.0/gml}LineStringType
    
    # Element coordinates ({http://www.multispeak.org/V5.0/gml}coordinates) inherited from {http://www.multispeak.org/V5.0/gml}LineStringType
    
    # Attribute gid inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    
    # Attribute srsName inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GMLLine', GMLLine)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}GMLLocation with content type ELEMENT_ONLY
class GMLLocation (_ImportedBinding__gml.PointType):
    """This is a geographical x,y, (z) location, referenced to a specific geographical coordinate system and datum."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GMLLocation')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 789, 1)
    _ElementMap = _ImportedBinding__gml.PointType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__gml.PointType._AttributeMap.copy()
    # Base type is _ImportedBinding__gml.PointType
    
    # Element coord ({http://www.multispeak.org/V5.0/gml}coord) inherited from {http://www.multispeak.org/V5.0/gml}PointType
    
    # Element coordinates ({http://www.multispeak.org/V5.0/gml}coordinates) inherited from {http://www.multispeak.org/V5.0/gml}PointType
    
    # Attribute gid inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    
    # Attribute srsName inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GMLLocation', GMLLocation)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}GMLPolygon with content type ELEMENT_ONLY
class GMLPolygon (_ImportedBinding__gml.PolygonType):
    """This is a polygon geometry that is built using GML classes. Note that the lines that make up a polygon should be closed.  If the line is intended to be a closed line, then the first and last coordiantes must be identical.  If the first and last coordinates are not identical, then the line is assumed not to be closed."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GMLPolygon')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 797, 1)
    _ElementMap = _ImportedBinding__gml.PolygonType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__gml.PolygonType._AttributeMap.copy()
    # Base type is _ImportedBinding__gml.PolygonType
    
    # Element outerBoundaryIs ({http://www.multispeak.org/V5.0/gml}outerBoundaryIs) inherited from {http://www.multispeak.org/V5.0/gml}PolygonType
    
    # Element innerBoundaryIs ({http://www.multispeak.org/V5.0/gml}innerBoundaryIs) inherited from {http://www.multispeak.org/V5.0/gml}PolygonType
    
    # Attribute gid inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    
    # Attribute srsName inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GMLPolygon', GMLPolygon)


# Complex type {http://www.multispeak.org/V5.0/commonTypes}networkModelRef with content type SIMPLE
class networkModelRef (objectRef):
    """Reference to an instance of an object. When used to describe an engineering line section, this object must contain a section name and may also contain a noun/objectID pair that will uniquely identify the MultiSpeak noun (element) and instance of that noun that is contained in the named section.  In Versions 3.0 and 4.1 this was called eaLoc."""
    _TypeDefinition = _ImportedBinding__prim.MultiSpeakGUID
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'networkModelRef')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1101, 1)
    _ElementMap = objectRef._ElementMap.copy()
    _AttributeMap = objectRef._AttributeMap.copy()
    # Base type is objectRef
    
    # Attribute primaryIdentifierValue inherited from {http://www.multispeak.org/V5.0/commonTypes}objectRef
    
    # Attribute secondaryIdentifierValue inherited from {http://www.multispeak.org/V5.0/commonTypes}objectRef
    
    # Attribute noun inherited from {http://www.multispeak.org/V5.0/commonTypes}objectRef
    
    # Attribute utility inherited from {http://www.multispeak.org/V5.0/commonTypes}objectRef
    
    # Attribute registeredName inherited from {http://www.multispeak.org/V5.0/commonTypes}objectRef
    
    # Attribute systemName inherited from {http://www.multispeak.org/V5.0/commonTypes}objectRef
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'networkModelRef', networkModelRef)




addressItems._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addressItem'), addressItem, scope=addressItems, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 91, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(addressItems._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'addressItem')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 91, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
addressItems._Automaton = _BuildAutomaton()




allocatedLoads._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'allocatedLoad'), allocatedLoad, scope=allocatedLoads, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 134, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(allocatedLoads._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'allocatedLoad')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 134, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
allocatedLoads._Automaton = _BuildAutomaton_()




boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Xmin'), pyxb.binding.datatypes.double, scope=boundingBox, documentation='The x coordinate of the lower left point of the bounding box.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 174, 3)))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ymin'), pyxb.binding.datatypes.double, scope=boundingBox, documentation='The y coordinate of the lower left point of the bounding box.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 179, 3)))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Xmax'), pyxb.binding.datatypes.double, scope=boundingBox, documentation='The x coordinate of the upper right point of the bounding box.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 184, 3)))

boundingBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ymax'), pyxb.binding.datatypes.double, scope=boundingBox, documentation='The y coordinate of the upper right point of the bounding box.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 189, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Xmin')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 174, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ymin')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 179, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Xmax')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 184, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(boundingBox._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ymax')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 189, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
boundingBox._Automaton = _BuildAutomaton_2()




Caller._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AppName'), pyxb.binding.datatypes.string, scope=Caller, documentation='This is the name of the application that sent this message.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 233, 3)))

Caller._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AppVersion'), pyxb.binding.datatypes.string, scope=Caller, documentation='This is the version of the application that sent this message.  This is NOT the version of MultiSpeak that is used in this message.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 238, 3)))

Caller._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Company'), pyxb.binding.datatypes.string, scope=Caller, documentation='This is the name of the company that provides the application that sent this message.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 243, 3)))

Caller._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AuditID'), pyxb.binding.datatypes.string, scope=Caller, documentation='This is the userID of the person who used the system that generated this message.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 248, 3)))

Caller._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AuditPassword'), pyxb.binding.datatypes.string, scope=Caller, documentation='This is the password of the person who used the system that generated this message.  It is suggested that this field be used for authorization.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 253, 3)))

Caller._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SystemID'), pyxb.binding.datatypes.string, scope=Caller, documentation='This is the identifier for the system that is sending this message, if needed for authentication.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 258, 3)))

Caller._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Password'), pyxb.binding.datatypes.string, scope=Caller, documentation='This is the password for the system that is sending this message if needed for authentication.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 263, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 238, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 248, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 253, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 258, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 263, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Caller._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AppName')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 233, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Caller._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AppVersion')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 238, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Caller._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Company')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 243, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Caller._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AuditID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 248, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Caller._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AuditPassword')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 253, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Caller._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SystemID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 258, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Caller._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Password')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 263, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Caller._Automaton = _BuildAutomaton_3()




cimTimePoints._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'absoluteTime'), _ImportedBinding__prim.mspDateTime, scope=cimTimePoints, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 302, 3)))

cimTimePoints._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relativeTimeInterval'), duration, scope=cimTimePoints, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 303, 3)))

cimTimePoints._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sequenceNumber'), pyxb.binding.datatypes.integer, scope=cimTimePoints, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 304, 3)))

cimTimePoints._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'window'), timePeriod, scope=cimTimePoints, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 305, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 302, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 303, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 304, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 305, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cimTimePoints._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'absoluteTime')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 302, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cimTimePoints._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relativeTimeInterval')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 303, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cimTimePoints._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sequenceNumber')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 304, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cimTimePoints._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'window')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 305, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cimTimePoints._Automaton = _BuildAutomaton_4()




CodedNames._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codedName'), codedName, scope=CodedNames, documentation='This is an abbreviation for a part of a fully-qualified object identifier of the form GlobalDomain.RegisteredName.SystemName.nounType.objectGUID', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 337, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CodedNames._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codedName')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 337, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CodedNames._Automaton = _BuildAutomaton_5()




complexNum._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'r'), pyxb.binding.datatypes.float, scope=complexNum, documentation='Real portion of the complex number.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 403, 3)))

complexNum._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), pyxb.binding.datatypes.float, scope=complexNum, documentation='Imaginary part of the complex number.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 408, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 403, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 408, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(complexNum._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'r')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 403, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(complexNum._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 408, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
complexNum._Automaton = _BuildAutomaton_6()




connectivityModelGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'connectivityNodes'), connectivityNodes, scope=connectivityModelGroup, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 448, 3)))

connectivityModelGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'connectivitySections'), connectivitySections, scope=connectivityModelGroup, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 449, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(connectivityModelGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'connectivityNodes')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 448, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(connectivityModelGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'connectivitySections')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 449, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
connectivityModelGroup._Automaton = _BuildAutomaton_7()




connectivityNodes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'node1ID'), nodeIdentifier, scope=connectivityNodes, documentation='This is the node identifier for this feature in a node-oriented engineering connectivity model.  The connectivityNodeID must be unique. For series-connected devices this is one of the terminal nodes, the upstream node in radial systems.  For shunt-connected devices this is the point of attachment.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 454, 3)))

connectivityNodes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'node2ID'), nodeIdentifier, scope=connectivityNodes, documentation='The connectivityNodeID must be unique if it exists. For series-connected devices this is one of the terminal nodes, the downstream node in a radial system.  For shunt-connected devices this connectivityNodeID refers to neutral, and thus often is not used.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 459, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(connectivityNodes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'node1ID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 454, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(connectivityNodes._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'node2ID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 459, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
connectivityNodes._Automaton = _BuildAutomaton_8()




connectivitySections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parentSectionIDs'), networkModelRef, scope=connectivitySections, documentation='This specifies the upline section(s) in a section-based engineering connectivity model.  Use multiple parentSectionsIDs to model the case in an electrical network model where two or more reduced-phase elements come together to feed a multi-phase element.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 468, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=3, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 468, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(connectivitySections._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parentSectionIDs')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 468, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
connectivitySections._Automaton = _BuildAutomaton_9()




contentsItems._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contentsItem'), objectRef, scope=contentsItems, documentation='This item is a pointer to the equipment contained in this container. ', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 477, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(contentsItems._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contentsItem')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 477, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
contentsItems._Automaton = _BuildAutomaton_10()




CoordinateSystemInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CSUnits'), CSUnits, scope=CoordinateSystemInformation, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 486, 3)))

CoordinateSystemInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CSAuthorities'), CSAuthorities, scope=CoordinateSystemInformation, documentation='It is the intention that if there is more than one coordinate system identified here that they SHALL BE multiple identifiers for the same coordinate system.  More than one coordinate system choice Must NOT be implied.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 487, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CSUnits')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 486, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CoordinateSystemInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CSAuthorities')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 487, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CoordinateSystemInformation._Automaton = _BuildAutomaton_11()




CSAuthorities._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CSAuthority'), CSAuthority, scope=CSAuthorities, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 499, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CSAuthorities._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CSAuthority')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 499, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CSAuthorities._Automaton = _BuildAutomaton_12()




CSAuthority._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CSAuthorityName'), CSAuthorityName, scope=CSAuthority, documentation='The string designator for the coordinate system authority.  For example, "SPCS" for the State Plane Coordinate System, "EPSG" for the European Petroleum Survey Group, "UTM" for the Universal Transverse Mercator coordinate system authority.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 507, 3)))

CSAuthority._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoordinateSystemAuthorityCode'), pyxb.binding.datatypes.string, scope=CSAuthority, documentation='The string name of the coordinate system authority code.  Examples of coordinate system names are "SPCS:0401", "EPSG:26741", and "UTM:30U".  In these examples "SPCS", "EPSG", and "UTM" are coordinate system authorities and "0401", "26741", and "30U" are coordinate system authority codes.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 512, 3)))

CSAuthority._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Datum'), pyxb.binding.datatypes.string, scope=CSAuthority, documentation="A datum is a mathematical representation of the shape of the earth's surface.  A complete determination of a geographic coordinate system requires the specification of the CSUnits, Datum, and coordinate system (CSAuthorityName AND CoordinateSystemAuthorityCode).", location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 517, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CSAuthority._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CSAuthorityName')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 507, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CSAuthority._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CoordinateSystemAuthorityCode')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 512, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CSAuthority._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Datum')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 517, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CSAuthority._Automaton = _BuildAutomaton_13()




DataSetState._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PublishDataSetState'), PublishDataSetState, scope=DataSetState, documentation='This option SHALL be used if this message header is for a published data (*Notification) message and it is desired to denote the data set associated with the published information that is being sent in this message.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 601, 3)))

DataSetState._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequestDataSetState'), RequestDataSetState, scope=DataSetState, documentation='This option SHALL be chosen if this message header is associated with a Get-type request and it is desired to denote the previous data set since which changed data are being requested. ', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 606, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataSetState._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PublishDataSetState')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 601, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataSetState._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequestDataSetState')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 606, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DataSetState._Automaton = _BuildAutomaton_14()




eMailAddresses._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eMailAddress'), eMailAddress, scope=eMailAddresses, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 665, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(eMailAddresses._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eMailAddress')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 665, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
eMailAddresses._Automaton = _BuildAutomaton_15()




errorObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensions'), extensions, scope=errorObject, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 690, 3)))

errorObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionsList'), extensionsList, scope=errorObject, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 691, 3)))

errorObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorCode'), replyCodeIdentifier, scope=errorObject, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 692, 3)))

errorObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eventTime'), _ImportedBinding__prim.mspDateTime, scope=errorObject, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 693, 3)))

errorObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'displayString'), pyxb.binding.datatypes.string, scope=errorObject, documentation='Human readable error message.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 694, 3)))

errorObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'detailedString'), pyxb.binding.datatypes.string, scope=errorObject, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 699, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 690, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 691, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 692, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 694, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 699, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(errorObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 690, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(errorObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 691, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(errorObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorCode')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 692, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(errorObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eventTime')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 693, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(errorObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'displayString')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 694, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(errorObject._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'detailedString')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 699, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
errorObject._Automaton = _BuildAutomaton_16()




errorObjects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorObject'), errorObject, scope=errorObjects, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 714, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(errorObjects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorObject')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 714, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
errorObjects._Automaton = _BuildAutomaton_17()




def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 728, 2))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 729, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 729, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
extensions._Automaton = _BuildAutomaton_18()




extensionsItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extName'), pyxb.binding.datatypes.string, scope=extensionsItem, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 741, 3)))

extensionsItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extValue'), extValue, scope=extensionsItem, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 742, 3)))

extensionsItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extType'), _ImportedBinding__enum.extType, scope=extensionsItem, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 743, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 743, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(extensionsItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extName')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 741, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(extensionsItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extValue')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 742, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extensionsItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extType')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 743, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
extensionsItem._Automaton = _BuildAutomaton_19()




extensionsList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionsItem'), extensionsItem, scope=extensionsList, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 751, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(extensionsList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsItem')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 751, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
extensionsList._Automaton = _BuildAutomaton_20()




GMLLines._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GMLLine'), GMLLine, scope=GMLLines, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 786, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GMLLines._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GMLLine')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 786, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GMLLines._Automaton = _BuildAutomaton_21()




GMLPolygons._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GMLPolygon'), GMLPolygon, scope=GMLPolygons, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 807, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GMLPolygons._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GMLPolygon')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 807, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GMLPolygons._Automaton = _BuildAutomaton_22()




impedances._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'r'), resistance, scope=impedances, documentation='Positive sequence resistance', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 937, 3)))

impedances._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), reactance, scope=impedances, documentation='Positive sequence reactance.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 942, 3)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 937, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 942, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(impedances._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'r')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 937, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(impedances._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 942, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
impedances._Automaton = _BuildAutomaton_23()




mspExtensible._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensions'), extensions, scope=mspExtensible, documentation='The extensions container is one way that MultiSpeak objects can be extended using XSD elements.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3)))

mspExtensible._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensionsList'), extensionsList, scope=mspExtensible, documentation='This is an optional, self-describing means to extend any MultiSpeak object.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mspExtensible._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mspExtensible._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mspExtensible._Automaton = _BuildAutomaton_24()




multiPartIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'primaryIdentifier'), singleIdentifier, scope=multiPartIdentifier, documentation='Primary human-readable identifier for this instance of the object. ', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1060, 3)))

multiPartIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'secondaryIdentifier'), singleIdentifier, scope=multiPartIdentifier, documentation='Additional human-readable identifier for this instance of the object. When the secondaryIdentifier is provided, it is expected that the union of the primary and secondary identifiers is necessary to uniquely identify a data instance and both shall be used.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1065, 3)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1065, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(multiPartIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'primaryIdentifier')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1060, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(multiPartIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'secondaryIdentifier')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1065, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
multiPartIdentifier._Automaton = _BuildAutomaton_25()




MultiSpeakVersion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MajorVersion'), pyxb.binding.datatypes.integer, scope=MultiSpeakVersion, documentation='The MajorVersion attribute identifies the major version of the data schema used for data in the message.  For instance for Version 5.0.4, the MajorVersion attribute would contain the integer 5.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1074, 3)))

MultiSpeakVersion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinorVersion'), pyxb.binding.datatypes.integer, scope=MultiSpeakVersion, documentation='The MinorVersion attribute identifies the minor version of the data schema used for data in the message. For instance for Version 5.0.4, the MinorVersion attribute would contain the integer 0.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1079, 3)))

MultiSpeakVersion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Build'), pyxb.binding.datatypes.integer, scope=MultiSpeakVersion, documentation='The Build attribute identifies the build of the data schema used for data in the message. For instance for Version 5.0.4, the Build attribute would contain the integer 4.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1084, 3)))

MultiSpeakVersion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Branch'), pyxb.binding.datatypes.integer, scope=MultiSpeakVersion, documentation='The Branch attribute identifies the branch number of the data schema used for data in the message. For instance for Version 5.0.4.1, the Branch attribute would contain the integer 1.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1089, 3)))

MultiSpeakVersion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildString'), BuildDescriptor, scope=MultiSpeakVersion, documentation='The BuildString contains a description of the type of data schema build that is used for the data in this message.  The options are: PR - Prerelease, RC - Release candidate, Branch - Development branch off of the trunk development, RD - Release for Development,  and Release - final release. ', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1094, 3)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1089, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1094, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MultiSpeakVersion._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MajorVersion')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1074, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MultiSpeakVersion._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MinorVersion')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1079, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MultiSpeakVersion._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Build')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1084, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MultiSpeakVersion._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Branch')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1089, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MultiSpeakVersion._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BuildString')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1094, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MultiSpeakVersion._Automaton = _BuildAutomaton_26()




nounSpecifiedRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectIdentifier'), nounSpecifiedMultiPartIdentifier, scope=nounSpecifiedRef, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1142, 3)))

nounSpecifiedRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectRef'), objectRef, scope=nounSpecifiedRef, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1143, 3)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nounSpecifiedRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectIdentifier')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1142, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nounSpecifiedRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectRef')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1143, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
nounSpecifiedRef._Automaton = _BuildAutomaton_27()




nounUnspecifiedRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectGUID'), _ImportedBinding__prim.MultiSpeakGUID, scope=nounUnspecifiedRef, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1151, 3)))

nounUnspecifiedRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectName'), multiPartIdentifier, scope=nounUnspecifiedRef, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1152, 3)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nounUnspecifiedRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectGUID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1151, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nounUnspecifiedRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectName')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1152, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
nounUnspecifiedRef._Automaton = _BuildAutomaton_28()




objectID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectGUID'), _ImportedBinding__prim.MultiSpeakGUID, scope=objectID, documentation='This is the objectIdentifier for the data instance of interest.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1160, 3)))

objectID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'primaryIdentifier'), singleIdentifier, scope=objectID, documentation='Primary human-readable identifier for this instance of the object. For instance if this object is an instance of an electricMeter, this should be the meterNumber; if this is a customer account, this should be the accountNumber. ', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1165, 3)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1165, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(objectID._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectGUID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1160, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(objectID._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'primaryIdentifier')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1165, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
objectID._Automaton = _BuildAutomaton_29()




otherContactInformation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'otherContactItem'), otherContactItem, scope=otherContactInformation, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1234, 3)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(otherContactInformation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'otherContactItem')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1234, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
otherContactInformation._Automaton = _BuildAutomaton_30()




phoneNumbers._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phoneNumber'), phoneNumber, scope=phoneNumbers, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1279, 3)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1278, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(phoneNumbers._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phoneNumber')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1279, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
phoneNumbers._Automaton = _BuildAutomaton_31()




PublishDataSetState._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetID'), pyxb.binding.datatypes.string, scope=PublishDataSetState, documentation='When it is desired to support data sets, this element SHALL be used to denote the data set for the data included in the message with which this message header is associated.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1298, 3)))

PublishDataSetState._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PreviousDataSetID'), pyxb.binding.datatypes.string, scope=PublishDataSetState, documentation='When it is desired to support data sets, this attribute identifies the previously sent block of data by data set identifier.  If the receiver of this message has not received the data set identified in the previous data set ID, it has missed data and it SHALL attempt recovery by calling the appropriate GetModified* service, if any, that has the PreviousDataSetID parameter populated in the message header with the data set identifier of the last data set that it had successfully received. If no GetModified* service is available, or the GetModified service is not supported by the server, then the receiver SHALL return a message with appropriate error information included in the result element.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1303, 3)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PublishDataSetState._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1298, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PublishDataSetState._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PreviousDataSetID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1303, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PublishDataSetState._Automaton = _BuildAutomaton_32()




registrationIDs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'registrationID'), _ImportedBinding__prim.MultiSpeakGUID, scope=registrationIDs, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1383, 3)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(registrationIDs._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'registrationID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1383, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
registrationIDs._Automaton = _BuildAutomaton_33()




replyCodeIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'replyCodeCategory'), _ImportedBinding__enum.replyCodeCategory, scope=replyCodeIdentifier, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1388, 3)))

replyCodeIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'index'), pyxb.binding.datatypes.string, scope=replyCodeIdentifier, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1389, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(replyCodeIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'replyCodeCategory')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1388, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(replyCodeIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'index')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1389, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
replyCodeIdentifier._Automaton = _BuildAutomaton_34()




RequestDataSetState._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetID'), pyxb.binding.datatypes.string, scope=RequestDataSetState, documentation='When necessary, this optional attribute identifies the data sent in this session.  If the DataSetID is included in a GetAll-type method call, then the server shall respond as if it was being asked for a GetModified-type call since that DataSetID, that is to say, it should send only those data instances that have changed since the PreviousDataSetID provided herein.  If the GetAll-type call does not include a DataSetID, or the server does not support data sets, then all instances of the requested object shall be returned.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1397, 3)))

RequestDataSetState._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PreviousDataSetID'), pyxb.binding.datatypes.string, scope=RequestDataSetState, documentation='When necessary, this attribute identifies the previously sent block of data by data set identifier.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1402, 3)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1397, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestDataSetState._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1397, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RequestDataSetState._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PreviousDataSetID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1402, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RequestDataSetState._Automaton = _BuildAutomaton_35()




requiredTimePeriod._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startTime'), _ImportedBinding__prim.mspDateTime, scope=requiredTimePeriod, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1419, 3)))

requiredTimePeriod._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endTime'), _ImportedBinding__prim.mspDateTime, scope=requiredTimePeriod, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1420, 3)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(requiredTimePeriod._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startTime')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1419, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(requiredTimePeriod._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endTime')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1420, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
requiredTimePeriod._Automaton = _BuildAutomaton_36()




result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resultIdentifier'), replyCodeIdentifier, scope=result, documentation='It is suggested that the values of replyCode be chosen from those values included in IEC 61968-9, 2nd Ed., Annex B as extended by Appendix A of "Security in MultiSpeak-Enabled Applications: Requirements".  Values of replyCode SHOULD be of the form [category] "." [index].', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1466, 3)))

result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resultDescription'), pyxb.binding.datatypes.string, scope=result, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1471, 3)))

result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'level'), _ImportedBinding__enum.messageResultLevel, scope=result, documentation='The level element describes the severity of the error message.  It is suggested that no level element be returned for a fully successful message.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1472, 3)))

result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorObjects'), errorObjects, scope=result, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1477, 3)))

result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dataSetID'), pyxb.binding.datatypes.string, scope=result, documentation='If this response header is associated with a GetAll* message, this element SHOULD be populated with the data set identifier by which the server knows the included data so that subsequent GetModified* messages for the same type of data could include a PreviousDataSetID in the request header so that the server could determine which data instances to include in its response (the data instances that had been modified since this base data set).  ', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1478, 3)))

result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastSent'), pyxb.binding.datatypes.string, scope=result, documentation='Pointer assigned by the server to the last object sent by server when using lastSent and lastReceived to send "chunks" of data.  It is up to the server to generate a pointer that ensures that all data instances are returned, but the pointer does not need to have meaning to the receiver, and it is not required that the pointer match the objectID of the last sent data instance.   Client will return this value in the lastReceived parameter of a web service method to request more data.\n ', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1483, 3)))

result._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectsRemaining'), _ImportedBinding__prim.objectsRemaining, scope=result, documentation='This is an optional attribute that is used to denote the number of objects remaining in a complete data transfer after this set of data is handled.  If this attribute is not included or is set to be 0, all data have been sent at the completion of this data transfer.  If the number of objectsRemaining is known, the value should be entered here.  If the number of remaining data instances is not known, the number should be set to be -1.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1489, 3)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1471, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1472, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1477, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1478, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1483, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1489, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resultIdentifier')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1466, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resultDescription')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1471, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'level')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1472, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorObjects')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1477, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dataSetID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1478, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastSent')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1483, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(result._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectsRemaining')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1489, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
result._Automaton = _BuildAutomaton_37()




servicePointIDs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'servicePointID'), servicePointID, scope=servicePointIDs, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1547, 3)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(servicePointIDs._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'servicePointID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1547, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
servicePointIDs._Automaton = _BuildAutomaton_38()




timePeriod._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startTime'), _ImportedBinding__prim.mspDateTime, scope=timePeriod, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1702, 3)))

timePeriod._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endTime'), _ImportedBinding__prim.mspDateTime, scope=timePeriod, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1703, 3)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1702, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1703, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(timePeriod._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startTime')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1702, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(timePeriod._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endTime')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1703, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
timePeriod._Automaton = _BuildAutomaton_39()




address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address1'), pyxb.binding.datatypes.string, scope=address, documentation='Address line 1.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 30, 5)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address2'), pyxb.binding.datatypes.string, scope=address, documentation='Address line 2.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 35, 5)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'detailedAddressFields'), detailedAddressFields, scope=address, documentation='Detailed information about the components of the composite address lines.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 40, 5)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'townCode'), pyxb.binding.datatypes.string, scope=address, documentation='Additional information about the city or town, if required.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 45, 5)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string, scope=address, documentation='Name of the city or municipality.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 50, 5)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'state'), pyxb.binding.datatypes.string, scope=address, documentation='The state or province.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 55, 5)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), pyxb.binding.datatypes.string, scope=address, documentation='The postal code.  For instance, in the United States this is the zip code.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 60, 5)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'country'), pyxb.binding.datatypes.string, scope=address, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 65, 5)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 30, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 35, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 40, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 45, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 50, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 55, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 60, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 65, 5))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address1')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 30, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address2')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 35, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'detailedAddressFields')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 40, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'townCode')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 45, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 50, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'state')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 55, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postalCode')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 60, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 65, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
address._Automaton = _BuildAutomaton_40()




addressItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), address, scope=addressItem, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 74, 5)))

addressItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addressType'), _ImportedBinding__enum.addressType, scope=addressItem, documentation='Type of address. For instance, billing, mailing, service location, etc.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 75, 5)))

addressItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'priorityOrder'), pyxb.binding.datatypes.integer, scope=addressItem, documentation='Order that should be used to contact this person.  First = 1, second = 2, etc.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 80, 5)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 75, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 80, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(addressItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 74, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(addressItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'addressType')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 75, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(addressItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'priorityOrder')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 80, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
addressItem._Automaton = _BuildAutomaton_41()




allocatedLoad._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phaseCode'), _ImportedBinding__enum.phaseCode, scope=allocatedLoad, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 109, 5)))

allocatedLoad._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'realPower'), realPower, scope=allocatedLoad, documentation='Real power load on this section.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 110, 5)))

allocatedLoad._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reactivePower'), reactivePower, scope=allocatedLoad, documentation='kVAr load on this section.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 115, 5)))

allocatedLoad._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numberOfCustomers'), pyxb.binding.datatypes.integer, scope=allocatedLoad, documentation='Number of customers allocated to this section.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 120, 5)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 109, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 110, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 115, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 120, 5))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(allocatedLoad._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(allocatedLoad._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(allocatedLoad._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phaseCode')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 109, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(allocatedLoad._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'realPower')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 110, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(allocatedLoad._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reactivePower')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 115, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(allocatedLoad._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'numberOfCustomers')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 120, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
allocatedLoad._Automaton = _BuildAutomaton_42()




codedName._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codedValue'), _ImportedBinding__prim.alphaNumericRestrictedString, scope=codedName, documentation='This is the shorthand abbreviation for the name part.  For instance, codedValue could equal "1" or "A" for RegisteredName = "ACMEWidgets"', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 313, 3)))

codedName._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'namePart'), _ImportedBinding__prim.alphaNumericRestrictedString, scope=codedName, documentation='This is the complete name part.  For instance "ACMEWidgets in the example given in the annotation for the codedValue.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 318, 3)))

codedName._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=codedName, documentation='This is an optional string description of the name part.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 323, 3)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 323, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(codedName._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codedValue')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 313, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(codedName._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'namePart')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 318, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(codedName._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 323, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
codedName._Automaton = _BuildAutomaton_43()




complexImpedance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'r'), pyxb.binding.datatypes.float, scope=complexImpedance, documentation='The resistive portion of impedance.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 355, 3)))

complexImpedance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), pyxb.binding.datatypes.float, scope=complexImpedance, documentation='The reactive portion of the impedance', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 360, 3)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 355, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 360, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(complexImpedance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'r')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 355, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(complexImpedance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 360, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
complexImpedance._Automaton = _BuildAutomaton_44()




complexImpedanceWithLeakage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'r'), pyxb.binding.datatypes.float, scope=complexImpedanceWithLeakage, documentation='The resistive portion of the impedance.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 374, 3)))

complexImpedanceWithLeakage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), pyxb.binding.datatypes.float, scope=complexImpedanceWithLeakage, documentation='The reactive portion of the impedance.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 379, 3)))

complexImpedanceWithLeakage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'b'), pyxb.binding.datatypes.float, scope=complexImpedanceWithLeakage, documentation='The leakage susceptance.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 384, 3)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 374, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 379, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 384, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(complexImpedanceWithLeakage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'r')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 374, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(complexImpedanceWithLeakage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 379, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(complexImpedanceWithLeakage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'b')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 384, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
complexImpedanceWithLeakage._Automaton = _BuildAutomaton_45()




complexVoltage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'r'), pyxb.binding.datatypes.float, scope=complexVoltage, documentation='Real component of the voltage.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 418, 3)))

complexVoltage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x'), pyxb.binding.datatypes.float, scope=complexVoltage, documentation='Imaginary component of the voltage.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 423, 3)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 418, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 423, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(complexVoltage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'r')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 418, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(complexVoltage._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'x')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 423, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
complexVoltage._Automaton = _BuildAutomaton_46()




detailedAddressFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetPrefix'), pyxb.binding.datatypes.string, scope=detailedAddressFields, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 617, 5)))

detailedAddressFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetNumber'), pyxb.binding.datatypes.string, scope=detailedAddressFields, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 618, 5)))

detailedAddressFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetSuffix'), pyxb.binding.datatypes.string, scope=detailedAddressFields, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 619, 5)))

detailedAddressFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetType'), pyxb.binding.datatypes.string, scope=detailedAddressFields, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 620, 5)))

detailedAddressFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'buildingNumber'), pyxb.binding.datatypes.string, scope=detailedAddressFields, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 621, 5)))

detailedAddressFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'suiteNumber'), pyxb.binding.datatypes.string, scope=detailedAddressFields, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 622, 5)))

detailedAddressFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addressGeneral'), pyxb.binding.datatypes.string, scope=detailedAddressFields, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 623, 5)))

detailedAddressFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postOfficeBox'), pyxb.binding.datatypes.string, scope=detailedAddressFields, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 624, 5)))

detailedAddressFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'region'), pyxb.binding.datatypes.string, scope=detailedAddressFields, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 625, 5)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 617, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 618, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 619, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 620, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 621, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 622, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 623, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 624, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 625, 5))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetPrefix')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 617, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetNumber')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 618, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetSuffix')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 619, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetType')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 620, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'buildingNumber')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 621, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'suiteNumber')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 622, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'addressGeneral')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 623, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postOfficeBox')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 624, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(detailedAddressFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 625, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
detailedAddressFields._Automaton = _BuildAutomaton_47()




eMailAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eMail'), pyxb.binding.datatypes.string, scope=eMailAddress, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 648, 5)))

eMailAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eMailType'), _ImportedBinding__enum.eMailType, scope=eMailAddress, documentation='The type of e-mail address.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 649, 5)))

eMailAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'priorityOrder'), pyxb.binding.datatypes.integer, scope=eMailAddress, documentation='Order in which these e-mail addresses should be used to contact this person.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 654, 5)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 649, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 654, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(eMailAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(eMailAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(eMailAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eMail')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 648, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(eMailAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eMailType')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 649, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(eMailAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'priorityOrder')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 654, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
eMailAddress._Automaton = _BuildAutomaton_48()




GPSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'latitude'), pyxb.binding.datatypes.double, scope=GPSLocation, documentation='The latitude portion of a geographical location.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 817, 5)))

GPSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'longitude'), pyxb.binding.datatypes.double, scope=GPSLocation, documentation='The longitude portion of a geographical location.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 822, 5)))

GPSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'altitude'), pyxb.binding.datatypes.double, scope=GPSLocation, documentation='The altitude above mean sea level for this geographical location, assuming the use of the WGS84 datum.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 827, 5)))

GPSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GPSMetadata'), GPSMetadata, scope=GPSLocation, documentation='If it is desirable to send metadata about how this GPSLocation was collected, that data is documented in this element.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 832, 5)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 827, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 832, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GPSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GPSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GPSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'latitude')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 817, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GPSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'longitude')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 822, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GPSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'altitude')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 827, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GPSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GPSMetadata')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 832, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
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
GPSLocation._Automaton = _BuildAutomaton_49()




GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'easting'), pyxb.binding.datatypes.double, scope=GPSMetadata, documentation='Easting for coordinate zone.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 853, 5)))

GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'northing'), pyxb.binding.datatypes.double, scope=GPSMetadata, documentation='Northing for coordinate zone.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 858, 5)))

GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), pyxb.binding.datatypes.string, scope=GPSMetadata, documentation='Source of data.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 863, 5)))

GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'number'), pyxb.binding.datatypes.long, scope=GPSMetadata, documentation='Number of readings that were averaged during the collection of this location.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 868, 5)))

GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isRealTimeDiffCorrection'), pyxb.binding.datatypes.boolean, scope=GPSMetadata, documentation='Has this point been differentially corrected in real time?', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 873, 5)))

GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hdop'), pyxb.binding.datatypes.float, scope=GPSMetadata, documentation='Horizontal dilution of precision.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 878, 5)))

GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vdop'), pyxb.binding.datatypes.float, scope=GPSMetadata, documentation='Vertical dilution of precision.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 883, 5)))

GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'diffID'), pyxb.binding.datatypes.string, scope=GPSMetadata, documentation='The identifier for the source of differential correction signal.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 888, 5)))

GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collected'), pyxb.binding.datatypes.dateTime, scope=GPSMetadata, documentation='The date and time that this location was taken.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 893, 5)))

GPSMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numSat'), pyxb.binding.datatypes.long, scope=GPSMetadata, documentation='Number of satellites visible when this location was taken.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 898, 5)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 853, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 858, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 863, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 868, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 873, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 878, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 883, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 888, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 893, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 898, 5))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'easting')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 853, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'northing')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 858, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 863, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'number')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 868, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isRealTimeDiffCorrection')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 873, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hdop')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 878, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vdop')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 883, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'diffID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 888, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collected')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 893, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(GPSMetadata._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'numSat')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 898, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GPSMetadata._Automaton = _BuildAutomaton_50()




def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1065, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nounSpecifiedMultiPartIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'primaryIdentifier')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1060, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(nounSpecifiedMultiPartIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'secondaryIdentifier')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1065, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
nounSpecifiedMultiPartIdentifier._Automaton = _BuildAutomaton_51()




otherContactItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'details'), pyxb.binding.datatypes.string, scope=otherContactItem, documentation='This element carries the miscellaneous contact information.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1244, 5)))

otherContactItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infoType'), pyxb.binding.datatypes.string, scope=otherContactItem, documentation='This element is used to describe the type of information stored in the "details" element.  Examples might be: IP address, truck number, radio number.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1249, 5)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1249, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(otherContactItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(otherContactItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(otherContactItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'details')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1244, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(otherContactItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infoType')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1249, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
otherContactItem._Automaton = _BuildAutomaton_52()




phoneNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phone'), telephoneNumber, scope=phoneNumber, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1262, 5)))

phoneNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phoneType'), _ImportedBinding__enum.phoneType, scope=phoneNumber, documentation='The type of phone number.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1263, 5)))

phoneNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'priorityOrder'), pyxb.binding.datatypes.integer, scope=phoneNumber, documentation='Order in which these phone numbers should be used to contact this person.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1268, 5)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1263, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1268, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(phoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(phoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(phoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phone')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1262, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(phoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phoneType')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1263, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(phoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'priorityOrder')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1268, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
phoneNumber._Automaton = _BuildAutomaton_53()




def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(requestedCoordinateSystem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CSUnits')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 486, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(requestedCoordinateSystem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CSAuthorities')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 487, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
requestedCoordinateSystem._Automaton = _BuildAutomaton_54()




telephoneNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'areaCode'), pyxb.binding.datatypes.string, scope=telephoneNumber, documentation='Area or region code.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1627, 5)))

telephoneNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cityCode'), pyxb.binding.datatypes.string, scope=telephoneNumber, documentation='City code for telephone number, if applicable.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1632, 5)))

telephoneNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), pyxb.binding.datatypes.string, scope=telephoneNumber, documentation='Country code for telephone number, if applicable.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1637, 5)))

telephoneNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'localNumber'), pyxb.binding.datatypes.string, scope=telephoneNumber, documentation='The primary portion of a telephone number as dialed in a local calling area.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1642, 5)))

telephoneNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extension'), pyxb.binding.datatypes.string, scope=telephoneNumber, documentation='Extension for telephone number if required.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1647, 5)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1627, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1632, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1637, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1642, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1647, 5))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(telephoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(telephoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(telephoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'areaCode')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1627, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(telephoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cityCode')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1632, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(telephoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1637, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(telephoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'localNumber')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1642, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(telephoneNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extension')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1647, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
telephoneNumber._Automaton = _BuildAutomaton_55()




utilityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'owner'), pyxb.binding.datatypes.string, scope=utilityInfo, documentation='This is the owner of the physical device.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1739, 5)))

utilityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceLocationID'), objectID, scope=utilityInfo, documentation='This is the objectID of the service location at which this device is installed.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1744, 5)))

utilityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'servicePointID'), servicePointID, scope=utilityInfo, documentation='This is a pointer to the service point at which this meter is installed', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1749, 5)))

utilityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accountID'), objectID, scope=utilityInfo, documentation='This is a pointer to the customer account for this serviceLocation. This SHALL be the objectID of the associated account object.  If the acountNumber is different than the objectGUID for this data instance of account, then the accountNumber may be carried in the accountID.primaryIdentifier element.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1754, 5)))

utilityInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerID'), objectID, scope=utilityInfo, documentation='This is the objectID of the customer with which this device is associated.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1759, 5)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1739, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1744, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1749, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1754, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1759, 5))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(utilityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1043, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(utilityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensionsList')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1048, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(utilityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'owner')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1739, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(utilityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceLocationID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1744, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(utilityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'servicePointID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1749, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(utilityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accountID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1754, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(utilityInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerID')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspCommonTypes.xsd', 1759, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
utilityInfo._Automaton = _BuildAutomaton_56()




def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 213, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GMLLine._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'coord')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 213, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GMLLine._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'coordinates')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 214, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GMLLine._Automaton = _BuildAutomaton_57()




def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GMLLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'coord')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 195, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GMLLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'coordinates')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 196, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GMLLocation._Automaton = _BuildAutomaton_58()




def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 267, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GMLPolygon._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'outerBoundaryIs')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 266, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GMLPolygon._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'innerBoundaryIs')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 267, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GMLPolygon._Automaton = _BuildAutomaton_59()

