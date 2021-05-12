# .\_prim.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:70fb7217d1b6af0e48587d7cbb8fbc59d60db316
# Generated 2016-08-21 08:25:54.759000 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://www.multispeak.org/V5.0/primitives [xmlns:prim]

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
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.multispeak.org/V5.0/primitives', create_if_missing=True)
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


# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}alphaNumericRestrictedString
class alphaNumericRestrictedString (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'alphaNumericRestrictedString')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 10, 1)
    _Documentation = None
alphaNumericRestrictedString._CF_pattern = pyxb.binding.facets.CF_pattern()
alphaNumericRestrictedString._CF_pattern.addPattern(pattern='[A-Za-z0-9]*')
alphaNumericRestrictedString._InitializeFacetMap(alphaNumericRestrictedString._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'alphaNumericRestrictedString', alphaNumericRestrictedString)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}delimiter
class delimiter (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'delimiter')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 15, 1)
    _Documentation = None
delimiter._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
delimiter._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
delimiter._InitializeFacetMap(delimiter._CF_maxLength,
   delimiter._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'delimiter', delimiter)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}domainName
class domainName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'domainName')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 21, 1)
    _Documentation = None
domainName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'domainName', domainName)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}doubleType
class doubleType (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'doubleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 24, 1)
    _Documentation = None
doubleType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'doubleType', doubleType)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}floatType
class floatType (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'floatType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 33, 1)
    _Documentation = None
floatType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'floatType', floatType)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}integerType
class integerType (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 36, 1)
    _Documentation = None
integerType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'integerType', integerType)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}mspDateTime
class mspDateTime (pyxb.binding.datatypes.dateTime):

    """ISO 8601 date time.  All dateTime fields will be formatted with UTC offsets.  The use of "Z" is acceptable to denote UTC or "Zulu" time.all dates will be formatted as:

2005-06-15T11:30:22.56-07:00  

where the date is in YYYY-MM-DD format and the time is in military time, beginning after the date-time separator “T”, in hh:mm:ss.ss format, followed by the time zone offset.  The use of fractional seconds is optional and any level of decimal precision in seconds is supported.  The time zone offset is shown as hh:mm offset from GMT, with either a positive offset (east of the prime meridian) or negative offset (west of the prime meridian).  """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mspDateTime')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 39, 1)
    _Documentation = 'ISO 8601 date time.  All dateTime fields will be formatted with UTC offsets.  The use of "Z" is acceptable to denote UTC or "Zulu" time.all dates will be formatted as:\n\n2005-06-15T11:30:22.56-07:00  \n\nwhere the date is in YYYY-MM-DD format and the time is in military time, beginning after the date-time separator \u201cT\u201d, in hh:mm:ss.ss format, followed by the time zone offset.  The use of fractional seconds is optional and any level of decimal precision in seconds is supported.  The time zone offset is shown as hh:mm offset from GMT, with either a positive offset (east of the prime meridian) or negative offset (west of the prime meridian).  '
mspDateTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'mspDateTime', mspDateTime)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}MultiSpeakGUID
class MultiSpeakGUID (pyxb.binding.datatypes.string):

    """This is intended to be a universally unique identifier (UUID) for an instance of an object.  It is intended that this identifier is compliant with the IETF RFC 4122 ("A Universally Unique IDentifier URN Namespace") definition of a UUID. Furthermore, the pattern used to restrict the xs:string should support any of the RFC 4122 UUID variants, including the Microsoft Globally Unique Identifier (GUID) variant of the UUID, without being restricted to supporting ONLY the Microsoft GUID definition."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiSpeakGUID')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 49, 1)
    _Documentation = 'This is intended to be a universally unique identifier (UUID) for an instance of an object.  It is intended that this identifier is compliant with the IETF RFC 4122 ("A Universally Unique IDentifier URN Namespace") definition of a UUID. Furthermore, the pattern used to restrict the xs:string should support any of the RFC 4122 UUID variants, including the Microsoft Globally Unique Identifier (GUID) variant of the UUID, without being restricted to supporting ONLY the Microsoft GUID definition.'
MultiSpeakGUID._CF_pattern = pyxb.binding.facets.CF_pattern()
MultiSpeakGUID._CF_pattern.addPattern(pattern='[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
MultiSpeakGUID._InitializeFacetMap(MultiSpeakGUID._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MultiSpeakGUID', MultiSpeakGUID)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}objectsRemaining
class objectsRemaining (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'objectsRemaining')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 57, 1)
    _Documentation = None
objectsRemaining._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=objectsRemaining, value=pyxb.binding.datatypes.integer(-1))
objectsRemaining._InitializeFacetMap(objectsRemaining._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'objectsRemaining', objectsRemaining)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}percent
class percent (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'percent')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 62, 1)
    _Documentation = None
percent._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'percent', percent)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}stringType
class stringType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stringType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 65, 1)
    _Documentation = None
stringType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stringType', stringType)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}trueBoolean
class trueBoolean (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'trueBoolean')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 68, 1)
    _Documentation = None
trueBoolean._CF_pattern = pyxb.binding.facets.CF_pattern()
trueBoolean._CF_pattern.addPattern(pattern='(true|1)')
trueBoolean._InitializeFacetMap(trueBoolean._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'trueBoolean', trueBoolean)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}valueFloat
class valueFloat (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'valueFloat')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 73, 1)
    _Documentation = None
valueFloat._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'valueFloat', valueFloat)

# Atomic simple type: {http://www.multispeak.org/V5.0/primitives}expirationTime
class expirationTime (mspDateTime):

    """A point in time after which a request expires."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'expirationTime')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspPrimitives.xsd', 27, 1)
    _Documentation = 'A point in time after which a request expires.'
expirationTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'expirationTime', expirationTime)
