# .\_gml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e72799a1325f9da9ad3fc9c47c29a05da785f284
# Generated 2016-08-21 08:25:54.761000 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://www.multispeak.org/V5.0/gml [xmlns:gml]

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
import _xlink as _ImportedBinding__xlink
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.multispeak.org/V5.0/gml', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xlink = _ImportedBinding__xlink.Namespace
_Namespace_xlink.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://www.multispeak.org/V5.0/gml}AbstractGeometryType with content type EMPTY
class AbstractGeometryType (pyxb.binding.basis.complexTypeDefinition):
    """
        All geometry elements are derived from this abstract supertype; 
        a geometry element may have an identifying attribute (gid). 
        It may be associated with a spatial reference system.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractGeometryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 70, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute gid uses Python identifier gid
    __gid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gid'), 'gid', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_gid', pyxb.binding.datatypes.ID)
    __gid._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 80, 4)
    __gid._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 80, 4)
    
    gid = property(__gid.value, __gid.set, None, None)

    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_srsName', pyxb.binding.datatypes.anyURI)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 81, 4)
    __srsName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 81, 4)
    
    srsName = property(__srsName.value, __srsName.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __gid.name() : __gid,
        __srsName.name() : __srsName
    })
Namespace.addCategoryObject('typeBinding', 'AbstractGeometryType', AbstractGeometryType)


# Complex type {http://www.multispeak.org/V5.0/gml}CoordType with content type ELEMENT_ONLY
class CoordType (pyxb.binding.basis.complexTypeDefinition):
    """
        Represents a coordinate tuple in one, two, or three dimensions.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoordType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 348, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/gml}X uses Python identifier X
    __X = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'X'), 'X', '__httpwww_multispeak_orgV5_0gml_CoordType_httpwww_multispeak_orgV5_0gmlX', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 355, 3), )

    
    X = property(__X.value, __X.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/gml}Y uses Python identifier Y
    __Y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Y'), 'Y', '__httpwww_multispeak_orgV5_0gml_CoordType_httpwww_multispeak_orgV5_0gmlY', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 356, 3), )

    
    Y = property(__Y.value, __Y.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/gml}Z uses Python identifier Z
    __Z = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Z'), 'Z', '__httpwww_multispeak_orgV5_0gml_CoordType_httpwww_multispeak_orgV5_0gmlZ', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 357, 3), )

    
    Z = property(__Z.value, __Z.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/gml}Bulge uses Python identifier Bulge
    __Bulge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Bulge'), 'Bulge', '__httpwww_multispeak_orgV5_0gml_CoordType_httpwww_multispeak_orgV5_0gmlBulge', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 358, 3), )

    
    Bulge = property(__Bulge.value, __Bulge.set, None, 'Bulge is a factor that describes a curved line segment between two points. Bulge=0 is a straight line: Bulge=1 is a curve along the edge of a circle.  A bulge can be associated only with the second point of a line segment.  A negative bulge factor causes the line to bulge to the left as viewed from the first point to the second; a positive bulge causes the line to be curved to the right as viewed from the first point to the left. ')

    _ElementMap.update({
        __X.name() : __X,
        __Y.name() : __Y,
        __Z.name() : __Z,
        __Bulge.name() : __Bulge
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CoordType', CoordType)


# Complex type {http://www.multispeak.org/V5.0/gml}CoordinatesType with content type SIMPLE
class CoordinatesType (pyxb.binding.basis.complexTypeDefinition):
    """
        Coordinates can be included in a single string, but there is no 
        facility for validating string content. The value of the 'cs' attribute 
        is the separator for coordinate values, and the value of the 'ts' 
        attribute gives the tuple separator (a single space by default); the 
        default values may be changed to reflect local usage.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoordinatesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 365, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute decimal uses Python identifier decimal
    __decimal = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decimal'), 'decimal', '__httpwww_multispeak_orgV5_0gml_CoordinatesType_decimal', pyxb.binding.datatypes.string, unicode_default='.')
    __decimal._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 377, 4)
    __decimal._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 377, 4)
    
    decimal = property(__decimal.value, __decimal.set, None, None)

    
    # Attribute cs uses Python identifier cs
    __cs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cs'), 'cs', '__httpwww_multispeak_orgV5_0gml_CoordinatesType_cs', pyxb.binding.datatypes.string, unicode_default=',')
    __cs._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 378, 4)
    __cs._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 378, 4)
    
    cs = property(__cs.value, __cs.set, None, None)

    
    # Attribute ts uses Python identifier ts
    __ts = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ts'), 'ts', '__httpwww_multispeak_orgV5_0gml_CoordinatesType_ts', pyxb.binding.datatypes.string, unicode_default=' ')
    __ts._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 379, 4)
    __ts._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 379, 4)
    
    ts = property(__ts.value, __ts.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __decimal.name() : __decimal,
        __cs.name() : __cs,
        __ts.name() : __ts
    })
Namespace.addCategoryObject('typeBinding', 'CoordinatesType', CoordinatesType)


# Complex type {http://www.multispeak.org/V5.0/gml}AbstractGeometryCollectionBaseType with content type EMPTY
class AbstractGeometryCollectionBaseType (AbstractGeometryType):
    """
        This abstract base type for geometry collections just makes the 
        srsName attribute mandatory.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractGeometryCollectionBaseType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 85, 1)
    _ElementMap = AbstractGeometryType._ElementMap.copy()
    _AttributeMap = AbstractGeometryType._AttributeMap.copy()
    # Base type is AbstractGeometryType
    
    # Attribute gid is restricted from parent
    
    # Attribute gid uses Python identifier gid
    __gid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gid'), 'gid', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_gid', pyxb.binding.datatypes.ID)
    __gid._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 94, 4)
    __gid._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 94, 4)
    
    gid = property(__gid.value, __gid.set, None, None)

    
    # Attribute srsName is restricted from parent
    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_srsName', pyxb.binding.datatypes.anyURI, required=True)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 95, 4)
    __srsName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 95, 4)
    
    srsName = property(__srsName.value, __srsName.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __gid.name() : __gid,
        __srsName.name() : __srsName
    })
Namespace.addCategoryObject('typeBinding', 'AbstractGeometryCollectionBaseType', AbstractGeometryCollectionBaseType)


# Complex type {http://www.multispeak.org/V5.0/gml}GeometryAssociationType with content type ELEMENT_ONLY
class GeometryAssociationType (pyxb.binding.basis.complexTypeDefinition):
    """
        An instance of this type (e.g. a geometryMember) can either 
        enclose or point to a primitive geometry element. When serving 
        as a simple link that references a remote geometry instance, 
        the value of the gml:remoteSchema attribute can be used to 
        locate a schema fragment that constrains the target instance.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeometryAssociationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 112, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.multispeak.org/V5.0/gml}_Geometry uses Python identifier Geometry
    __Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_Geometry'), 'Geometry', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_multispeak_orgV5_0gml_Geometry', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 35, 1), )

    
    Geometry = property(__Geometry.value, __Geometry.set, None, None)

    
    # Attribute {http://www.multispeak.org/V5.0/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'remoteSchema'), 'remoteSchema', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_multispeak_orgV5_0gmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 66, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 126, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 14, 1)
    __href._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 82, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 16, 1)
    __role._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 83, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 17, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 84, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 18, 1)
    __title._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 85, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkshow', _ImportedBinding__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 20, 1)
    __show._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 86, 2)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkactuate', _ImportedBinding__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 47, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 87, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __Geometry.name() : __Geometry
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'GeometryAssociationType', GeometryAssociationType)


# Complex type {http://www.multispeak.org/V5.0/gml}PointType with content type ELEMENT_ONLY
class PointType (AbstractGeometryType):
    """
        A Point is defined by a single coordinate tuple.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 185, 1)
    _ElementMap = AbstractGeometryType._ElementMap.copy()
    _AttributeMap = AbstractGeometryType._AttributeMap.copy()
    # Base type is AbstractGeometryType
    
    # Element {http://www.multispeak.org/V5.0/gml}coord uses Python identifier coord
    __coord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coord'), 'coord', '__httpwww_multispeak_orgV5_0gml_PointType_httpwww_multispeak_orgV5_0gmlcoord', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 55, 1), )

    
    coord = property(__coord.value, __coord.set, None, 'This is one of two optional formats for expressing coordinates in GML.  This option is the one that shall be used for expressing points in MultiSpeak data exchanges.')

    
    # Element {http://www.multispeak.org/V5.0/gml}coordinates uses Python identifier coordinates
    __coordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coordinates'), 'coordinates', '__httpwww_multispeak_orgV5_0gml_PointType_httpwww_multispeak_orgV5_0gmlcoordinates', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 60, 1), )

    
    coordinates = property(__coordinates.value, __coordinates.set, None, 'This is one of two optional formats for expressing coordinates in GML.  This option  shall not be used for expressing points in MultiSpeak data exchanges.')

    
    # Attribute gid inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    
    # Attribute srsName inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    _ElementMap.update({
        __coord.name() : __coord,
        __coordinates.name() : __coordinates
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PointType', PointType)


# Complex type {http://www.multispeak.org/V5.0/gml}LineStringType with content type ELEMENT_ONLY
class LineStringType (AbstractGeometryType):
    """
        A LineString is defined by two or more coordinate tuples, with 
        linear interpolation between them. 
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineStringType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 202, 1)
    _ElementMap = AbstractGeometryType._ElementMap.copy()
    _AttributeMap = AbstractGeometryType._AttributeMap.copy()
    # Base type is AbstractGeometryType
    
    # Element {http://www.multispeak.org/V5.0/gml}coord uses Python identifier coord
    __coord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coord'), 'coord', '__httpwww_multispeak_orgV5_0gml_LineStringType_httpwww_multispeak_orgV5_0gmlcoord', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 55, 1), )

    
    coord = property(__coord.value, __coord.set, None, 'This is one of two optional formats for expressing coordinates in GML.  This option is the one that shall be used for expressing points in MultiSpeak data exchanges.')

    
    # Element {http://www.multispeak.org/V5.0/gml}coordinates uses Python identifier coordinates
    __coordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coordinates'), 'coordinates', '__httpwww_multispeak_orgV5_0gml_LineStringType_httpwww_multispeak_orgV5_0gmlcoordinates', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 60, 1), )

    
    coordinates = property(__coordinates.value, __coordinates.set, None, 'This is one of two optional formats for expressing coordinates in GML.  This option  shall not be used for expressing points in MultiSpeak data exchanges.')

    
    # Attribute gid inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    
    # Attribute srsName inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    _ElementMap.update({
        __coord.name() : __coord,
        __coordinates.name() : __coordinates
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'LineStringType', LineStringType)


# Complex type {http://www.multispeak.org/V5.0/gml}LinearRingType with content type ELEMENT_ONLY
class LinearRingType (AbstractGeometryType):
    """
        A LinearRing is defined by four or more coordinate tuples, with 
        linear interpolation between them; the first and last coordinates 
        must be coincident.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinearRingType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 220, 1)
    _ElementMap = AbstractGeometryType._ElementMap.copy()
    _AttributeMap = AbstractGeometryType._AttributeMap.copy()
    # Base type is AbstractGeometryType
    
    # Element {http://www.multispeak.org/V5.0/gml}coord uses Python identifier coord
    __coord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coord'), 'coord', '__httpwww_multispeak_orgV5_0gml_LinearRingType_httpwww_multispeak_orgV5_0gmlcoord', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 55, 1), )

    
    coord = property(__coord.value, __coord.set, None, 'This is one of two optional formats for expressing coordinates in GML.  This option is the one that shall be used for expressing points in MultiSpeak data exchanges.')

    
    # Element {http://www.multispeak.org/V5.0/gml}coordinates uses Python identifier coordinates
    __coordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coordinates'), 'coordinates', '__httpwww_multispeak_orgV5_0gml_LinearRingType_httpwww_multispeak_orgV5_0gmlcoordinates', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 60, 1), )

    
    coordinates = property(__coordinates.value, __coordinates.set, None, 'This is one of two optional formats for expressing coordinates in GML.  This option  shall not be used for expressing points in MultiSpeak data exchanges.')

    
    # Attribute gid inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    
    # Attribute srsName inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    _ElementMap.update({
        __coord.name() : __coord,
        __coordinates.name() : __coordinates
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'LinearRingType', LinearRingType)


# Complex type {http://www.multispeak.org/V5.0/gml}BoxType with content type ELEMENT_ONLY
class BoxType (AbstractGeometryType):
    """
        The Box structure defines an extent using a pair of coordinate tuples.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoxType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 239, 1)
    _ElementMap = AbstractGeometryType._ElementMap.copy()
    _AttributeMap = AbstractGeometryType._AttributeMap.copy()
    # Base type is AbstractGeometryType
    
    # Element {http://www.multispeak.org/V5.0/gml}coord uses Python identifier coord
    __coord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coord'), 'coord', '__httpwww_multispeak_orgV5_0gml_BoxType_httpwww_multispeak_orgV5_0gmlcoord', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 55, 1), )

    
    coord = property(__coord.value, __coord.set, None, 'This is one of two optional formats for expressing coordinates in GML.  This option is the one that shall be used for expressing points in MultiSpeak data exchanges.')

    
    # Element {http://www.multispeak.org/V5.0/gml}coordinates uses Python identifier coordinates
    __coordinates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coordinates'), 'coordinates', '__httpwww_multispeak_orgV5_0gml_BoxType_httpwww_multispeak_orgV5_0gmlcoordinates', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 60, 1), )

    
    coordinates = property(__coordinates.value, __coordinates.set, None, 'This is one of two optional formats for expressing coordinates in GML.  This option  shall not be used for expressing points in MultiSpeak data exchanges.')

    
    # Attribute gid inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    
    # Attribute srsName inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    _ElementMap.update({
        __coord.name() : __coord,
        __coordinates.name() : __coordinates
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BoxType', BoxType)


# Complex type {http://www.multispeak.org/V5.0/gml}PolygonType with content type ELEMENT_ONLY
class PolygonType (AbstractGeometryType):
    """
        A Polygon is defined by an outer boundary and zero or more inner 
        boundaries which are in turn defined by LinearRings.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PolygonType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 256, 1)
    _ElementMap = AbstractGeometryType._ElementMap.copy()
    _AttributeMap = AbstractGeometryType._AttributeMap.copy()
    # Base type is AbstractGeometryType
    
    # Element {http://www.multispeak.org/V5.0/gml}outerBoundaryIs uses Python identifier outerBoundaryIs
    __outerBoundaryIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outerBoundaryIs'), 'outerBoundaryIs', '__httpwww_multispeak_orgV5_0gml_PolygonType_httpwww_multispeak_orgV5_0gmlouterBoundaryIs', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 41, 1), )

    
    outerBoundaryIs = property(__outerBoundaryIs.value, __outerBoundaryIs.set, None, None)

    
    # Element {http://www.multispeak.org/V5.0/gml}innerBoundaryIs uses Python identifier innerBoundaryIs
    __innerBoundaryIs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'innerBoundaryIs'), 'innerBoundaryIs', '__httpwww_multispeak_orgV5_0gml_PolygonType_httpwww_multispeak_orgV5_0gmlinnerBoundaryIs', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 42, 1), )

    
    innerBoundaryIs = property(__innerBoundaryIs.value, __innerBoundaryIs.set, None, None)

    
    # Attribute gid inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    
    # Attribute srsName inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryType
    _ElementMap.update({
        __outerBoundaryIs.name() : __outerBoundaryIs,
        __innerBoundaryIs.name() : __innerBoundaryIs
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PolygonType', PolygonType)


# Complex type {http://www.multispeak.org/V5.0/gml}PointMemberType with content type ELEMENT_ONLY
class PointMemberType (GeometryAssociationType):
    """Restricts the geometry member to being a Point instance."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PointMemberType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 129, 1)
    _ElementMap = GeometryAssociationType._ElementMap.copy()
    _AttributeMap = GeometryAssociationType._AttributeMap.copy()
    # Base type is GeometryAssociationType
    
    # Element {http://www.multispeak.org/V5.0/gml}Point uses Python identifier Point
    __Point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Point'), 'Point', '__httpwww_multispeak_orgV5_0gml_PointMemberType_httpwww_multispeak_orgV5_0gmlPoint', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 44, 1), )

    
    Point = property(__Point.value, __Point.set, None, None)

    
    # Attribute remoteSchema is restricted from parent
    
    # Attribute {http://www.multispeak.org/V5.0/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'remoteSchema'), 'remoteSchema', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_multispeak_orgV5_0gmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 66, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 110, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, None)

    
    # Attribute href is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 14, 1)
    __href._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 82, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute role is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 16, 1)
    __role._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 83, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute arcrole is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 17, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 84, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute title is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 18, 1)
    __title._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 85, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute show is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkshow', _ImportedBinding__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 20, 1)
    __show._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 86, 2)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute actuate is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkactuate', _ImportedBinding__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 47, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 87, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    
    # Attribute type is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __Point.name() : __Point
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'PointMemberType', PointMemberType)


# Complex type {http://www.multispeak.org/V5.0/gml}LineStringMemberType with content type ELEMENT_ONLY
class LineStringMemberType (GeometryAssociationType):
    """Restricts the geometry member to being a LineString instance."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LineStringMemberType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 142, 1)
    _ElementMap = GeometryAssociationType._ElementMap.copy()
    _AttributeMap = GeometryAssociationType._AttributeMap.copy()
    # Base type is GeometryAssociationType
    
    # Element {http://www.multispeak.org/V5.0/gml}LineString uses Python identifier LineString
    __LineString = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LineString'), 'LineString', '__httpwww_multispeak_orgV5_0gml_LineStringMemberType_httpwww_multispeak_orgV5_0gmlLineString', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 45, 1), )

    
    LineString = property(__LineString.value, __LineString.set, None, None)

    
    # Attribute remoteSchema is restricted from parent
    
    # Attribute {http://www.multispeak.org/V5.0/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'remoteSchema'), 'remoteSchema', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_multispeak_orgV5_0gmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 66, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 110, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, None)

    
    # Attribute href is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 14, 1)
    __href._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 82, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute role is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 16, 1)
    __role._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 83, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute arcrole is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 17, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 84, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute title is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 18, 1)
    __title._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 85, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute show is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkshow', _ImportedBinding__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 20, 1)
    __show._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 86, 2)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute actuate is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkactuate', _ImportedBinding__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 47, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 87, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    
    # Attribute type is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __LineString.name() : __LineString
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'LineStringMemberType', LineStringMemberType)


# Complex type {http://www.multispeak.org/V5.0/gml}PolygonMemberType with content type ELEMENT_ONLY
class PolygonMemberType (GeometryAssociationType):
    """Restricts the geometry member to being a Polygon instance."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PolygonMemberType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 155, 1)
    _ElementMap = GeometryAssociationType._ElementMap.copy()
    _AttributeMap = GeometryAssociationType._AttributeMap.copy()
    # Base type is GeometryAssociationType
    
    # Element {http://www.multispeak.org/V5.0/gml}Polygon uses Python identifier Polygon
    __Polygon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Polygon'), 'Polygon', '__httpwww_multispeak_orgV5_0gml_PolygonMemberType_httpwww_multispeak_orgV5_0gmlPolygon', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 47, 1), )

    
    Polygon = property(__Polygon.value, __Polygon.set, None, None)

    
    # Attribute remoteSchema is restricted from parent
    
    # Attribute {http://www.multispeak.org/V5.0/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'remoteSchema'), 'remoteSchema', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_multispeak_orgV5_0gmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 66, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 110, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, None)

    
    # Attribute href is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 14, 1)
    __href._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 82, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute role is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 16, 1)
    __role._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 83, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute arcrole is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 17, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 84, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute title is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 18, 1)
    __title._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 85, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute show is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkshow', _ImportedBinding__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 20, 1)
    __show._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 86, 2)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute actuate is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkactuate', _ImportedBinding__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 47, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 87, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    
    # Attribute type is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __Polygon.name() : __Polygon
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'PolygonMemberType', PolygonMemberType)


# Complex type {http://www.multispeak.org/V5.0/gml}LinearRingMemberType with content type ELEMENT_ONLY
class LinearRingMemberType (GeometryAssociationType):
    """Restricts the outer or inner boundary of a polygon instance 
			to being a LinearRing."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinearRingMemberType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 168, 1)
    _ElementMap = GeometryAssociationType._ElementMap.copy()
    _AttributeMap = GeometryAssociationType._AttributeMap.copy()
    # Base type is GeometryAssociationType
    
    # Element {http://www.multispeak.org/V5.0/gml}LinearRing uses Python identifier LinearRing
    __LinearRing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LinearRing'), 'LinearRing', '__httpwww_multispeak_orgV5_0gml_LinearRingMemberType_httpwww_multispeak_orgV5_0gmlLinearRing', False, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 46, 1), )

    
    LinearRing = property(__LinearRing.value, __LinearRing.set, None, None)

    
    # Attribute remoteSchema is restricted from parent
    
    # Attribute {http://www.multispeak.org/V5.0/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'remoteSchema'), 'remoteSchema', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_multispeak_orgV5_0gmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 66, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 110, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, None)

    
    # Attribute href is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 14, 1)
    __href._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 82, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute role is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkrole', pyxb.binding.datatypes.anyURI)
    __role._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 16, 1)
    __role._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 83, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute arcrole is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkarcrole', pyxb.binding.datatypes.anyURI)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 17, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 84, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute title is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 18, 1)
    __title._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 85, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute show is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkshow', _ImportedBinding__xlink.STD_ANON)
    __show._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 20, 1)
    __show._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 86, 2)
    
    show = property(__show.value, __show.set, None, "\n        The 'show' attribute is used to communicate the desired presentation \n        of the ending resource on traversal from the starting resource; it's \n        value should be treated as follows: \n        new - load ending resource in a new window, frame, pane, or other \n              presentation context\n        replace - load the resource in the same window, frame, pane, or \n                  other presentation context\n        embed - load ending resource in place of the presentation of the \n                starting resource\n        other - behavior is unconstrained; examine other markup in the \n                link for hints \n        none - behavior is unconstrained \n      ")

    
    # Attribute actuate is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinkactuate', _ImportedBinding__xlink.STD_ANON_)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 47, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 87, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, "\n        The 'actuate' attribute is used to communicate the desired timing \n        of traversal from the starting resource to the ending resource; \n        it's value should be treated as follows:\n        onLoad - traverse to the ending resource immediately on loading \n                 the starting resource \n        onRequest - traverse from the starting resource to the ending \n                    resource only on a post-loading event triggered for \n                    this purpose \n        other - behavior is unconstrained; examine other markup in link \n                for hints \n        none - behavior is unconstrained\n      ")

    
    # Attribute type is restricted from parent
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_multispeak_orgV5_0gml_GeometryAssociationType_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.string, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\xlinks.xsd', 81, 2)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __LinearRing.name() : __LinearRing
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'LinearRingMemberType', LinearRingMemberType)


# Complex type {http://www.multispeak.org/V5.0/gml}GeometryCollectionType with content type ELEMENT_ONLY
class GeometryCollectionType (AbstractGeometryCollectionBaseType):
    """
        A geometry collection must include one or more geometries, referenced 
        through geometryMember elements. User-defined geometry collections 
        that accept GML geometry classes as members must instantiate--or 
        derive from--this type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeometryCollectionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 275, 1)
    _ElementMap = AbstractGeometryCollectionBaseType._ElementMap.copy()
    _AttributeMap = AbstractGeometryCollectionBaseType._AttributeMap.copy()
    # Base type is AbstractGeometryCollectionBaseType
    
    # Element {http://www.multispeak.org/V5.0/gml}geometryMember uses Python identifier geometryMember
    __geometryMember = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geometryMember'), 'geometryMember', '__httpwww_multispeak_orgV5_0gml_GeometryCollectionType_httpwww_multispeak_orgV5_0gmlgeometryMember', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 37, 1), )

    
    geometryMember = property(__geometryMember.value, __geometryMember.set, None, None)

    
    # Attribute gid_ inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryCollectionBaseType
    
    # Attribute srsName_ inherited from {http://www.multispeak.org/V5.0/gml}AbstractGeometryCollectionBaseType
    _ElementMap.update({
        __geometryMember.name() : __geometryMember
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GeometryCollectionType', GeometryCollectionType)


# Complex type {http://www.multispeak.org/V5.0/gml}MultiPointType with content type ELEMENT_ONLY
class MultiPointType (GeometryCollectionType):
    """
        A MultiPoint is defined by one or more Points, referenced through 
        pointMember elements.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiPointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 292, 1)
    _ElementMap = GeometryCollectionType._ElementMap.copy()
    _AttributeMap = GeometryCollectionType._AttributeMap.copy()
    # Base type is GeometryCollectionType
    
    # Element {http://www.multispeak.org/V5.0/gml}pointMember uses Python identifier pointMember
    __pointMember = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pointMember'), 'pointMember', '__httpwww_multispeak_orgV5_0gml_MultiPointType_httpwww_multispeak_orgV5_0gmlpointMember', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 38, 1), )

    
    pointMember = property(__pointMember.value, __pointMember.set, None, None)

    
    # Attribute gid is restricted from parent
    
    # Attribute gid uses Python identifier gid
    __gid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gid'), 'gid', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_gid', pyxb.binding.datatypes.ID)
    __gid._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 304, 4)
    __gid._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 304, 4)
    
    gid = property(__gid.value, __gid.set, None, None)

    
    # Attribute srsName is restricted from parent
    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_srsName', pyxb.binding.datatypes.anyURI, required=True)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 305, 4)
    __srsName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 305, 4)
    
    srsName = property(__srsName.value, __srsName.set, None, None)

    _ElementMap.update({
        __pointMember.name() : __pointMember
    })
    _AttributeMap.update({
        __gid.name() : __gid,
        __srsName.name() : __srsName
    })
Namespace.addCategoryObject('typeBinding', 'MultiPointType', MultiPointType)


# Complex type {http://www.multispeak.org/V5.0/gml}MultiLineStringType with content type ELEMENT_ONLY
class MultiLineStringType (GeometryCollectionType):
    """
        A MultiLineString is defined by one or more LineStrings, referenced 
        through lineStringMember elements.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiLineStringType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 309, 1)
    _ElementMap = GeometryCollectionType._ElementMap.copy()
    _AttributeMap = GeometryCollectionType._AttributeMap.copy()
    # Base type is GeometryCollectionType
    
    # Element {http://www.multispeak.org/V5.0/gml}lineStringMember uses Python identifier lineStringMember
    __lineStringMember = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lineStringMember'), 'lineStringMember', '__httpwww_multispeak_orgV5_0gml_MultiLineStringType_httpwww_multispeak_orgV5_0gmllineStringMember', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 39, 1), )

    
    lineStringMember = property(__lineStringMember.value, __lineStringMember.set, None, None)

    
    # Attribute gid is restricted from parent
    
    # Attribute gid uses Python identifier gid
    __gid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gid'), 'gid', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_gid', pyxb.binding.datatypes.ID)
    __gid._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 321, 4)
    __gid._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 321, 4)
    
    gid = property(__gid.value, __gid.set, None, None)

    
    # Attribute srsName is restricted from parent
    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_srsName', pyxb.binding.datatypes.anyURI, required=True)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 322, 4)
    __srsName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 322, 4)
    
    srsName = property(__srsName.value, __srsName.set, None, None)

    _ElementMap.update({
        __lineStringMember.name() : __lineStringMember
    })
    _AttributeMap.update({
        __gid.name() : __gid,
        __srsName.name() : __srsName
    })
Namespace.addCategoryObject('typeBinding', 'MultiLineStringType', MultiLineStringType)


# Complex type {http://www.multispeak.org/V5.0/gml}MultiPolygonType with content type ELEMENT_ONLY
class MultiPolygonType (GeometryCollectionType):
    """
        A MultiPolygon is defined by one or more Polygons, referenced through 
        polygonMember elements. 
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiPolygonType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 326, 1)
    _ElementMap = GeometryCollectionType._ElementMap.copy()
    _AttributeMap = GeometryCollectionType._AttributeMap.copy()
    # Base type is GeometryCollectionType
    
    # Element {http://www.multispeak.org/V5.0/gml}polygonMember uses Python identifier polygonMember
    __polygonMember = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'polygonMember'), 'polygonMember', '__httpwww_multispeak_orgV5_0gml_MultiPolygonType_httpwww_multispeak_orgV5_0gmlpolygonMember', True, pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 40, 1), )

    
    polygonMember = property(__polygonMember.value, __polygonMember.set, None, None)

    
    # Attribute gid is restricted from parent
    
    # Attribute gid uses Python identifier gid
    __gid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'gid'), 'gid', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_gid', pyxb.binding.datatypes.ID)
    __gid._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 338, 4)
    __gid._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 338, 4)
    
    gid = property(__gid.value, __gid.set, None, None)

    
    # Attribute srsName is restricted from parent
    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__httpwww_multispeak_orgV5_0gml_AbstractGeometryType_srsName', pyxb.binding.datatypes.anyURI, required=True)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 339, 4)
    __srsName._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 339, 4)
    
    srsName = property(__srsName.value, __srsName.set, None, None)

    _ElementMap.update({
        __polygonMember.name() : __polygonMember
    })
    _AttributeMap.update({
        __gid.name() : __gid,
        __srsName.name() : __srsName
    })
Namespace.addCategoryObject('typeBinding', 'MultiPolygonType', MultiPolygonType)


Geometry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Geometry'), AbstractGeometryType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 35, 1))
Namespace.addCategoryObject('elementBinding', Geometry.name().localName(), Geometry)

coord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coord'), CoordType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option is the one that shall be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 55, 1))
Namespace.addCategoryObject('elementBinding', coord.name().localName(), coord)

coordinates = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coordinates'), CoordinatesType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option  shall not be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 60, 1))
Namespace.addCategoryObject('elementBinding', coordinates.name().localName(), coordinates)

geometryMember = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geometryMember'), GeometryAssociationType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 37, 1))
Namespace.addCategoryObject('elementBinding', geometryMember.name().localName(), geometryMember)

outerBoundaryIs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outerBoundaryIs'), LinearRingType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 41, 1))
Namespace.addCategoryObject('elementBinding', outerBoundaryIs.name().localName(), outerBoundaryIs)

innerBoundaryIs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'innerBoundaryIs'), LinearRingType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', innerBoundaryIs.name().localName(), innerBoundaryIs)

Point = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Point'), PointType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 44, 1))
Namespace.addCategoryObject('elementBinding', Point.name().localName(), Point)

LineString = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LineString'), LineStringType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 45, 1))
Namespace.addCategoryObject('elementBinding', LineString.name().localName(), LineString)

LinearRing = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LinearRing'), LinearRingType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 46, 1))
Namespace.addCategoryObject('elementBinding', LinearRing.name().localName(), LinearRing)

Polygon = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Polygon'), PolygonType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 47, 1))
Namespace.addCategoryObject('elementBinding', Polygon.name().localName(), Polygon)

Box = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Box'), BoxType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 48, 1))
Namespace.addCategoryObject('elementBinding', Box.name().localName(), Box)

GeometryCollection = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GeometryCollection'), GeometryCollectionType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', GeometryCollection.name().localName(), GeometryCollection)

pointMember = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pointMember'), PointMemberType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 38, 1))
Namespace.addCategoryObject('elementBinding', pointMember.name().localName(), pointMember)

lineStringMember = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineStringMember'), LineStringMemberType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 39, 1))
Namespace.addCategoryObject('elementBinding', lineStringMember.name().localName(), lineStringMember)

polygonMember = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'polygonMember'), PolygonMemberType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 40, 1))
Namespace.addCategoryObject('elementBinding', polygonMember.name().localName(), polygonMember)

MultiGeometry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultiGeometry'), GeometryCollectionType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 50, 1))
Namespace.addCategoryObject('elementBinding', MultiGeometry.name().localName(), MultiGeometry)

MultiPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultiPoint'), MultiPointType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 51, 1))
Namespace.addCategoryObject('elementBinding', MultiPoint.name().localName(), MultiPoint)

MultiLineString = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultiLineString'), MultiLineStringType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 52, 1))
Namespace.addCategoryObject('elementBinding', MultiLineString.name().localName(), MultiLineString)

MultiPolygon = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultiPolygon'), MultiPolygonType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 53, 1))
Namespace.addCategoryObject('elementBinding', MultiPolygon.name().localName(), MultiPolygon)



CoordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'X'), pyxb.binding.datatypes.decimal, scope=CoordType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 355, 3)))

CoordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Y'), pyxb.binding.datatypes.decimal, scope=CoordType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 356, 3)))

CoordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Z'), pyxb.binding.datatypes.decimal, scope=CoordType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 357, 3)))

CoordType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Bulge'), pyxb.binding.datatypes.float, scope=CoordType, documentation='Bulge is a factor that describes a curved line segment between two points. Bulge=0 is a straight line: Bulge=1 is a curve along the edge of a circle.  A bulge can be associated only with the second point of a line segment.  A negative bulge factor causes the line to bulge to the left as viewed from the first point to the second; a positive bulge causes the line to be curved to the right as viewed from the first point to the left. ', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 358, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 356, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 357, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 358, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CoordType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'X')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 355, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CoordType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Y')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 356, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CoordType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Z')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 357, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CoordType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Bulge')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 358, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CoordType._Automaton = _BuildAutomaton()




GeometryAssociationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Geometry'), AbstractGeometryType, abstract=pyxb.binding.datatypes.boolean(1), scope=GeometryAssociationType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 35, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 122, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeometryAssociationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_Geometry')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 123, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GeometryAssociationType._Automaton = _BuildAutomaton_()




PointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coord'), CoordType, scope=PointType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option is the one that shall be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 55, 1)))

PointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coordinates'), CoordinatesType, scope=PointType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option  shall not be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 60, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coord')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 195, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coordinates')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 196, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PointType._Automaton = _BuildAutomaton_2()




LineStringType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coord'), CoordType, scope=LineStringType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option is the one that shall be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 55, 1)))

LineStringType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coordinates'), CoordinatesType, scope=LineStringType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option  shall not be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 60, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 213, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LineStringType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coord')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 213, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LineStringType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coordinates')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 214, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LineStringType._Automaton = _BuildAutomaton_3()




LinearRingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coord'), CoordType, scope=LinearRingType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option is the one that shall be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 55, 1)))

LinearRingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coordinates'), CoordinatesType, scope=LinearRingType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option  shall not be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 60, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=4, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 232, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LinearRingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coord')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 232, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LinearRingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coordinates')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 233, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LinearRingType._Automaton = _BuildAutomaton_4()




BoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coord'), CoordType, scope=BoxType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option is the one that shall be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 55, 1)))

BoxType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coordinates'), CoordinatesType, scope=BoxType, documentation='This is one of two optional formats for expressing coordinates in GML.  This option  shall not be used for expressing points in MultiSpeak data exchanges.', location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 60, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=2, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 249, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coord')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 249, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BoxType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coordinates')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 250, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BoxType._Automaton = _BuildAutomaton_5()




PolygonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outerBoundaryIs'), LinearRingType, scope=PolygonType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 41, 1)))

PolygonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'innerBoundaryIs'), LinearRingType, scope=PolygonType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 42, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 267, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PolygonType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outerBoundaryIs')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 266, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PolygonType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'innerBoundaryIs')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 267, 5))
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
PolygonType._Automaton = _BuildAutomaton_6()




PointMemberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Point'), PointType, scope=PointMemberType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 44, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 135, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PointMemberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Point')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 136, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PointMemberType._Automaton = _BuildAutomaton_7()




LineStringMemberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LineString'), LineStringType, scope=LineStringMemberType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 45, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 148, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LineStringMemberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LineString')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 149, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LineStringMemberType._Automaton = _BuildAutomaton_8()




PolygonMemberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Polygon'), PolygonType, scope=PolygonMemberType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 47, 1)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 161, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PolygonMemberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Polygon')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 162, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PolygonMemberType._Automaton = _BuildAutomaton_9()




LinearRingMemberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LinearRing'), LinearRingType, scope=LinearRingMemberType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 46, 1)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 175, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LinearRingMemberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LinearRing')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 176, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LinearRingMemberType._Automaton = _BuildAutomaton_10()




GeometryCollectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geometryMember'), GeometryAssociationType, scope=GeometryCollectionType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 37, 1)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeometryCollectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geometryMember')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 287, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeometryCollectionType._Automaton = _BuildAutomaton_11()




MultiPointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pointMember'), PointMemberType, scope=MultiPointType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 38, 1)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MultiPointType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pointMember')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 302, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MultiPointType._Automaton = _BuildAutomaton_12()




MultiLineStringType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineStringMember'), LineStringMemberType, scope=MultiLineStringType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 39, 1)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MultiLineStringType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lineStringMember')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 319, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MultiLineStringType._Automaton = _BuildAutomaton_13()




MultiPolygonType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'polygonMember'), PolygonMemberType, scope=MultiPolygonType, location=pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 40, 1)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MultiPolygonType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'polygonMember')), pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspGeometry.xsd', 336, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MultiPolygonType._Automaton = _BuildAutomaton_14()


Point._setSubstitutionGroup(Geometry)

LineString._setSubstitutionGroup(Geometry)

LinearRing._setSubstitutionGroup(Geometry)

Polygon._setSubstitutionGroup(Geometry)

GeometryCollection._setSubstitutionGroup(Geometry)

pointMember._setSubstitutionGroup(geometryMember)

lineStringMember._setSubstitutionGroup(geometryMember)

polygonMember._setSubstitutionGroup(geometryMember)

MultiGeometry._setSubstitutionGroup(Geometry)

MultiPoint._setSubstitutionGroup(Geometry)

MultiLineString._setSubstitutionGroup(Geometry)

MultiPolygon._setSubstitutionGroup(Geometry)
