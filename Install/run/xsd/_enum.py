# .\_enum.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e7836dd1452a18ec3d907fc9198a72618df4cf81
# Generated 2016-08-21 08:25:54.759000 by PyXB version 1.2.4 using Python 2.7.11.final.0
# Namespace http://www.multispeak.org/V5.0/enumerations [xmlns:enum]

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.multispeak.org/V5.0/enumerations', create_if_missing=True)
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


# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}accountability
class accountability (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accountability')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 9, 1)
    _Documentation = None
accountability._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=accountability, enum_prefix=None)
accountability.Q1 = accountability._CF_enumeration.addEnumeration(unicode_value='Q1', tag='Q1')
accountability.Q2 = accountability._CF_enumeration.addEnumeration(unicode_value='Q2', tag='Q2')
accountability.Q3 = accountability._CF_enumeration.addEnumeration(unicode_value='Q3', tag='Q3')
accountability.Q4 = accountability._CF_enumeration.addEnumeration(unicode_value='Q4', tag='Q4')
accountability.Q1_2 = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-2', tag='Q1_2')
accountability.Q1_3 = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-3', tag='Q1_3')
accountability.Q1_4 = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-4', tag='Q1_4')
accountability.Q2_3 = accountability._CF_enumeration.addEnumeration(unicode_value='Q2-3', tag='Q2_3')
accountability.Q2_4 = accountability._CF_enumeration.addEnumeration(unicode_value='Q2-4', tag='Q2_4')
accountability.Q3_4 = accountability._CF_enumeration.addEnumeration(unicode_value='Q3-4', tag='Q3_4')
accountability.Q1_2_3 = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-2-3', tag='Q1_2_3')
accountability.Q1_2_4 = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-2-4', tag='Q1_2_4')
accountability.Q1_3_4 = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-3-4', tag='Q1_3_4')
accountability.Q2_3_4 = accountability._CF_enumeration.addEnumeration(unicode_value='Q2-3-4', tag='Q2_3_4')
accountability.Q1_2_3_4 = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-2-3-4', tag='Q1_2_3_4')
accountability.Q1_2_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-2-netFlow', tag='Q1_2_netFlow')
accountability.Q1_3_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-3-netFlow', tag='Q1_3_netFlow')
accountability.Q1_4_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-4-netFlow', tag='Q1_4_netFlow')
accountability.Q2_3_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q2-3-netFlow', tag='Q2_3_netFlow')
accountability.Q2_4_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q2-4-netFlow', tag='Q2_4_netFlow')
accountability.Q3_4_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q3-4-netFlow', tag='Q3_4_netFlow')
accountability.Q1_2_3_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-2-3-netFlow', tag='Q1_2_3_netFlow')
accountability.Q1_2_4_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-2-4-netFlow', tag='Q1_2_4_netFlow')
accountability.Q1_3_4_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-3-4-netFlow', tag='Q1_3_4_netFlow')
accountability.Q2_3_4_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q2-3-4-netFlow', tag='Q2_3_4_netFlow')
accountability.Q1_2_3_4_netFlow = accountability._CF_enumeration.addEnumeration(unicode_value='Q1-2-3-4-netFlow', tag='Q1_2_3_4_netFlow')
accountability._InitializeFacetMap(accountability._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'accountability', accountability)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}accountStatusKind
class accountStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accountStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 53, 1)
    _Documentation = None
accountStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=accountStatusKind, enum_prefix=None)
accountStatusKind.Unknown = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
accountStatusKind.Active = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
accountStatusKind.ActiveNotBilled = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='ActiveNotBilled', tag='ActiveNotBilled')
accountStatusKind.Inactive = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='Inactive', tag='Inactive')
accountStatusKind.NonPay = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='NonPay', tag='NonPay')
accountStatusKind.NotFinal = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='NotFinal', tag='NotFinal')
accountStatusKind.PendingConnect = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='PendingConnect', tag='PendingConnect')
accountStatusKind.PendingConnectNonPay = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='PendingConnectNonPay', tag='PendingConnectNonPay')
accountStatusKind.PendingDisconnect = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='PendingDisconnect', tag='PendingDisconnect')
accountStatusKind.PendingDisconnectNonPay = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='PendingDisconnectNonPay', tag='PendingDisconnectNonPay')
accountStatusKind.Other = accountStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
accountStatusKind._InitializeFacetMap(accountStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'accountStatusKind', accountStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}action
class action (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'action')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 104, 1)
    _Documentation = None
action._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=action, enum_prefix=None)
action.New = action._CF_enumeration.addEnumeration(unicode_value='New', tag='New')
action.Change = action._CF_enumeration.addEnumeration(unicode_value='Change', tag='Change')
action.Delete = action._CF_enumeration.addEnumeration(unicode_value='Delete', tag='Delete')
action.Replace = action._CF_enumeration.addEnumeration(unicode_value='Replace', tag='Replace')
action.Link = action._CF_enumeration.addEnumeration(unicode_value='Link', tag='Link')
action.Unlink = action._CF_enumeration.addEnumeration(unicode_value='Unlink', tag='Unlink')
action._InitializeFacetMap(action._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'action', action)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}actionCodeKind
class actionCodeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Action to be taken on this work order."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actionCodeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 125, 1)
    _Documentation = 'Action to be taken on this work order.'
actionCodeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=actionCodeKind, enum_prefix=None)
actionCodeKind.Unknown = actionCodeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
actionCodeKind.Estimate = actionCodeKind._CF_enumeration.addEnumeration(unicode_value='Estimate', tag='Estimate')
actionCodeKind.CPROnly = actionCodeKind._CF_enumeration.addEnumeration(unicode_value='CPROnly', tag='CPROnly')
actionCodeKind.MaterialOnly = actionCodeKind._CF_enumeration.addEnumeration(unicode_value='MaterialOnly', tag='MaterialOnly')
actionCodeKind.CPRAndMaterial = actionCodeKind._CF_enumeration.addEnumeration(unicode_value='CPRAndMaterial', tag='CPRAndMaterial')
actionCodeKind.Other = actionCodeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
actionCodeKind._InitializeFacetMap(actionCodeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'actionCodeKind', actionCodeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}actionFlag
class actionFlag (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actionFlag')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 138, 1)
    _Documentation = None
actionFlag._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=actionFlag, enum_prefix=None)
actionFlag.Unknown = actionFlag._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
actionFlag.Enable = actionFlag._CF_enumeration.addEnumeration(unicode_value='Enable', tag='Enable')
actionFlag.Disable = actionFlag._CF_enumeration.addEnumeration(unicode_value='Disable', tag='Disable')
actionFlag.Other = actionFlag._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
actionFlag._InitializeFacetMap(actionFlag._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'actionFlag', actionFlag)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}actionTakenKind
class actionTakenKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actionTakenKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 162, 1)
    _Documentation = None
actionTakenKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=actionTakenKind, enum_prefix=None)
actionTakenKind.Unknown = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
actionTakenKind.Received = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Received', tag='Received')
actionTakenKind.PlacedIntoInventory = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='PlacedIntoInventory', tag='PlacedIntoInventory')
actionTakenKind.CheckedOut = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='CheckedOut', tag='CheckedOut')
actionTakenKind.Installed = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Installed', tag='Installed')
actionTakenKind.PlacedIntoService = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='PlacedIntoService', tag='PlacedIntoService')
actionTakenKind.Connected = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Connected', tag='Connected')
actionTakenKind.Disconnected = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Disconnected', tag='Disconnected')
actionTakenKind.Removed = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Removed', tag='Removed')
actionTakenKind.Inspected = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Inspected', tag='Inspected')
actionTakenKind.Tested = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Tested', tag='Tested')
actionTakenKind.Repaired = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Repaired', tag='Repaired')
actionTakenKind.Adjusted = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Adjusted', tag='Adjusted')
actionTakenKind.Calibrated = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Calibrated', tag='Calibrated')
actionTakenKind.Checked = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Checked', tag='Checked')
actionTakenKind.Treated = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Treated', tag='Treated')
actionTakenKind.ReturnedToInventory = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='ReturnedToInventory', tag='ReturnedToInventory')
actionTakenKind.Retired = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Retired', tag='Retired')
actionTakenKind.Destroyed = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Destroyed', tag='Destroyed')
actionTakenKind.Replaced = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Replaced', tag='Replaced')
actionTakenKind.Read = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Read', tag='Read')
actionTakenKind.Other = actionTakenKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
actionTakenKind._InitializeFacetMap(actionTakenKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'actionTakenKind', actionTakenKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}addressKind
class addressKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addressKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 188, 1)
    _Documentation = None
addressKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=addressKind, enum_prefix=None)
addressKind.Unknown = addressKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
addressKind.Billing = addressKind._CF_enumeration.addEnumeration(unicode_value='Billing', tag='Billing')
addressKind.Service = addressKind._CF_enumeration.addEnumeration(unicode_value='Service', tag='Service')
addressKind.Mailing = addressKind._CF_enumeration.addEnumeration(unicode_value='Mailing', tag='Mailing')
addressKind.Agent = addressKind._CF_enumeration.addEnumeration(unicode_value='Agent', tag='Agent')
addressKind.Headquarters = addressKind._CF_enumeration.addEnumeration(unicode_value='Headquarters', tag='Headquarters')
addressKind.Landlord = addressKind._CF_enumeration.addEnumeration(unicode_value='Landlord', tag='Landlord')
addressKind.Other = addressKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
addressKind._InitializeFacetMap(addressKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'addressKind', addressKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}allowableTransactionKind
class allowableTransactionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Allowable types of electronic payments. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'allowableTransactionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 214, 1)
    _Documentation = 'Allowable types of electronic payments. '
allowableTransactionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=allowableTransactionKind, enum_prefix=None)
allowableTransactionKind.ACHPayment = allowableTransactionKind._CF_enumeration.addEnumeration(unicode_value='ACHPayment', tag='ACHPayment')
allowableTransactionKind.CashPayment = allowableTransactionKind._CF_enumeration.addEnumeration(unicode_value='CashPayment', tag='CashPayment')
allowableTransactionKind.CreditCardPayment = allowableTransactionKind._CF_enumeration.addEnumeration(unicode_value='CreditCardPayment', tag='CreditCardPayment')
allowableTransactionKind.ECheckPayment = allowableTransactionKind._CF_enumeration.addEnumeration(unicode_value='ECheckPayment', tag='ECheckPayment')
allowableTransactionKind.SendToOperator = allowableTransactionKind._CF_enumeration.addEnumeration(unicode_value='SendToOperator', tag='SendToOperator')
allowableTransactionKind.Other = allowableTransactionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
allowableTransactionKind._InitializeFacetMap(allowableTransactionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'allowableTransactionKind', allowableTransactionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}analogConditionKind
class analogConditionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Range of analog value(see enumeration)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'analogConditionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 249, 1)
    _Documentation = 'Range of analog value(see enumeration).'
analogConditionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=analogConditionKind, enum_prefix=None)
analogConditionKind.L4 = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='L4', tag='L4')
analogConditionKind.L3 = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='L3', tag='L3')
analogConditionKind.L2 = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='L2', tag='L2')
analogConditionKind.L1 = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='L1', tag='L1')
analogConditionKind.Normal = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
analogConditionKind.H1 = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='H1', tag='H1')
analogConditionKind.H2 = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='H2', tag='H2')
analogConditionKind.H3 = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='H3', tag='H3')
analogConditionKind.H4 = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='H4', tag='H4')
analogConditionKind.Other = analogConditionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
analogConditionKind._InitializeFacetMap(analogConditionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'analogConditionKind', analogConditionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}angleUnits
class angleUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'angleUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 266, 1)
    _Documentation = None
angleUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=angleUnits, enum_prefix=None)
angleUnits.Unknown = angleUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
angleUnits.Degrees = angleUnits._CF_enumeration.addEnumeration(unicode_value='Degrees', tag='Degrees')
angleUnits.Minutes = angleUnits._CF_enumeration.addEnumeration(unicode_value='Minutes', tag='Minutes')
angleUnits.Seconds = angleUnits._CF_enumeration.addEnumeration(unicode_value='Seconds', tag='Seconds')
angleUnits.Radians = angleUnits._CF_enumeration.addEnumeration(unicode_value='Radians', tag='Radians')
angleUnits.Other = angleUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
angleUnits._InitializeFacetMap(angleUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'angleUnits', angleUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}apparentPowerUnits
class apparentPowerUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'apparentPowerUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 276, 1)
    _Documentation = None
apparentPowerUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=apparentPowerUnits, enum_prefix=None)
apparentPowerUnits.Unknown = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
apparentPowerUnits.VA = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
apparentPowerUnits.kVA = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='kVA', tag='kVA')
apparentPowerUnits.MVA = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='MVA', tag='MVA')
apparentPowerUnits.GVA = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='GVA', tag='GVA')
apparentPowerUnits.mVA = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='mVA', tag='mVA')
apparentPowerUnits.microVA = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='microVA', tag='microVA')
apparentPowerUnits.PerUnit = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='PerUnit', tag='PerUnit')
apparentPowerUnits.Percent = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='Percent', tag='Percent')
apparentPowerUnits.Other = apparentPowerUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
apparentPowerUnits._InitializeFacetMap(apparentPowerUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'apparentPowerUnits', apparentPowerUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}assetReturnType
class assetReturnType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This simpleType provides the ability to specify the form of asset information that is to be returned in response to a GetAssetsByXXX request method that is submitted to the AM endpoint."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'assetReturnType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 290, 1)
    _Documentation = 'This simpleType provides the ability to specify the form of asset information that is to be returned in response to a GetAssetsByXXX request method that is submitted to the AM endpoint.'
assetReturnType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=assetReturnType, enum_prefix=None)
assetReturnType.Concrete = assetReturnType._CF_enumeration.addEnumeration(unicode_value='Concrete', tag='Concrete')
assetReturnType.Generic = assetReturnType._CF_enumeration.addEnumeration(unicode_value='Generic', tag='Generic')
assetReturnType._InitializeFacetMap(assetReturnType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'assetReturnType', assetReturnType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}assetStatusKind
class assetStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'assetStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 321, 1)
    _Documentation = None
assetStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=assetStatusKind, enum_prefix=None)
assetStatusKind.Unknown = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
assetStatusKind.Quarantined = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='Quarantined', tag='Quarantined')
assetStatusKind.InInventory = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='InInventory', tag='InInventory')
assetStatusKind.CheckedOut = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='CheckedOut', tag='CheckedOut')
assetStatusKind.Installed = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='Installed', tag='Installed')
assetStatusKind.InService = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='InService', tag='InService')
assetStatusKind.OutOfService = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='OutOfService', tag='OutOfService')
assetStatusKind.Retired = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='Retired', tag='Retired')
assetStatusKind.Destroyed = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='Destroyed', tag='Destroyed')
assetStatusKind.Other = assetStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
assetStatusKind._InitializeFacetMap(assetStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'assetStatusKind', assetStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}assignmentStatusKind
class assignmentStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Changed status of this assignment.  """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'assignmentStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 378, 1)
    _Documentation = 'Changed status of this assignment.  '
assignmentStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=assignmentStatusKind, enum_prefix=None)
assignmentStatusKind.Other = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
assignmentStatusKind.Issued = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Issued', tag='Issued')
assignmentStatusKind.ReceivedAssignment = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='ReceivedAssignment', tag='ReceivedAssignment')
assignmentStatusKind.Delivered = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Delivered', tag='Delivered')
assignmentStatusKind.Accepted = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Accepted', tag='Accepted')
assignmentStatusKind.Rejected = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Rejected', tag='Rejected')
assignmentStatusKind.Queued = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Queued', tag='Queued')
assignmentStatusKind.TimedOut = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='TimedOut', tag='TimedOut')
assignmentStatusKind.PartiallyCompleted = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='PartiallyCompleted', tag='PartiallyCompleted')
assignmentStatusKind.Completed = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Completed', tag='Completed')
assignmentStatusKind.OnHold = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='OnHold', tag='OnHold')
assignmentStatusKind.Returned = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Returned', tag='Returned')
assignmentStatusKind.Unknown = assignmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
assignmentStatusKind._InitializeFacetMap(assignmentStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'assignmentStatusKind', assignmentStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}associatedDateKind
class associatedDateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'associatedDateKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 398, 1)
    _Documentation = None
associatedDateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=associatedDateKind, enum_prefix=None)
associatedDateKind.Unknown = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
associatedDateKind.ManufacturedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='ManufacturedDate', tag='ManufacturedDate')
associatedDateKind.EnteredInventoryDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='EnteredInventoryDate', tag='EnteredInventoryDate')
associatedDateKind.LeftInventoryDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='LeftInventoryDate', tag='LeftInventoryDate')
associatedDateKind.InstalledDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='InstalledDate', tag='InstalledDate')
associatedDateKind.PlacedIntoServiceDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='PlacedIntoServiceDate', tag='PlacedIntoServiceDate')
associatedDateKind.ConnectedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='ConnectedDate', tag='ConnectedDate')
associatedDateKind.DisconnectedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='DisconnectedDate', tag='DisconnectedDate')
associatedDateKind.RemovedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='RemovedDate', tag='RemovedDate')
associatedDateKind.InspectedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='InspectedDate', tag='InspectedDate')
associatedDateKind.TestedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='TestedDate', tag='TestedDate')
associatedDateKind.RepairedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='RepairedDate', tag='RepairedDate')
associatedDateKind.AdjustedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='AdjustedDate', tag='AdjustedDate')
associatedDateKind.CalibratedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='CalibratedDate', tag='CalibratedDate')
associatedDateKind.CheckedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='CheckedDate', tag='CheckedDate')
associatedDateKind.TreatedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='TreatedDate', tag='TreatedDate')
associatedDateKind.ReturnedToInventoryDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='ReturnedToInventoryDate', tag='ReturnedToInventoryDate')
associatedDateKind.RetiredDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='RetiredDate', tag='RetiredDate')
associatedDateKind.DestroyedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='DestroyedDate', tag='DestroyedDate')
associatedDateKind.ReplacedDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='ReplacedDate', tag='ReplacedDate')
associatedDateKind.ReadDate = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='ReadDate', tag='ReadDate')
associatedDateKind.Other = associatedDateKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
associatedDateKind._InitializeFacetMap(associatedDateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'associatedDateKind', associatedDateKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}authorizatonTypeKind
class authorizatonTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'authorizatonTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 460, 1)
    _Documentation = None
authorizatonTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=authorizatonTypeKind, enum_prefix=None)
authorizatonTypeKind.RequestedBy = authorizatonTypeKind._CF_enumeration.addEnumeration(unicode_value='RequestedBy', tag='RequestedBy')
authorizatonTypeKind.CreatedBy = authorizatonTypeKind._CF_enumeration.addEnumeration(unicode_value='CreatedBy', tag='CreatedBy')
authorizatonTypeKind.CheckedBy = authorizatonTypeKind._CF_enumeration.addEnumeration(unicode_value='CheckedBy', tag='CheckedBy')
authorizatonTypeKind.ModifiedBy = authorizatonTypeKind._CF_enumeration.addEnumeration(unicode_value='ModifiedBy', tag='ModifiedBy')
authorizatonTypeKind.ReleasedBy = authorizatonTypeKind._CF_enumeration.addEnumeration(unicode_value='ReleasedBy', tag='ReleasedBy')
authorizatonTypeKind.Other = authorizatonTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
authorizatonTypeKind._InitializeFacetMap(authorizatonTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'authorizatonTypeKind', authorizatonTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}balanceKind
class balanceKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'balanceKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 470, 1)
    _Documentation = None
balanceKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=balanceKind, enum_prefix=None)
balanceKind.PriorityBalance = balanceKind._CF_enumeration.addEnumeration(unicode_value='PriorityBalance', tag='PriorityBalance')
balanceKind.TotalBalance = balanceKind._CF_enumeration.addEnumeration(unicode_value='TotalBalance', tag='TotalBalance')
balanceKind.ArrearsBalance = balanceKind._CF_enumeration.addEnumeration(unicode_value='ArrearsBalance', tag='ArrearsBalance')
balanceKind.PrepaidBalance = balanceKind._CF_enumeration.addEnumeration(unicode_value='PrepaidBalance', tag='PrepaidBalance')
balanceKind.Other = balanceKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
balanceKind._InitializeFacetMap(balanceKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'balanceKind', balanceKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}baseType
class baseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of mounting for the meter.  See enumeration list."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'baseType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 490, 1)
    _Documentation = 'Type of mounting for the meter.  See enumeration list.'
baseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=baseType, enum_prefix=None)
baseType.BaseType1 = baseType._CF_enumeration.addEnumeration(unicode_value='BaseType1', tag='BaseType1')
baseType.SBase = baseType._CF_enumeration.addEnumeration(unicode_value='SBase', tag='SBase')
baseType.ABase = baseType._CF_enumeration.addEnumeration(unicode_value='ABase', tag='ABase')
baseType.BBase = baseType._CF_enumeration.addEnumeration(unicode_value='BBase', tag='BBase')
baseType.KBase = baseType._CF_enumeration.addEnumeration(unicode_value='KBase', tag='KBase')
baseType.PBase = baseType._CF_enumeration.addEnumeration(unicode_value='PBase', tag='PBase')
baseType.IECBottomConnected = baseType._CF_enumeration.addEnumeration(unicode_value='IECBottomConnected', tag='IECBottomConnected')
baseType.Switchboard = baseType._CF_enumeration.addEnumeration(unicode_value='Switchboard', tag='Switchboard')
baseType.Rackmount = baseType._CF_enumeration.addEnumeration(unicode_value='Rackmount', tag='Rackmount')
baseType.Other = baseType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
baseType._InitializeFacetMap(baseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'baseType', baseType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}billingItemsKind
class billingItemsKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Class of billing terms."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'billingItemsKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 507, 1)
    _Documentation = 'Class of billing terms.'
billingItemsKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=billingItemsKind, enum_prefix=None)
billingItemsKind.Unknown = billingItemsKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
billingItemsKind.Cycle = billingItemsKind._CF_enumeration.addEnumeration(unicode_value='Cycle', tag='Cycle')
billingItemsKind.BudgetBilled = billingItemsKind._CF_enumeration.addEnumeration(unicode_value='BudgetBilled', tag='BudgetBilled')
billingItemsKind.AnnualOrSeasonal = billingItemsKind._CF_enumeration.addEnumeration(unicode_value='AnnualOrSeasonal', tag='AnnualOrSeasonal')
billingItemsKind.PrePaid = billingItemsKind._CF_enumeration.addEnumeration(unicode_value='PrePaid', tag='PrePaid')
billingItemsKind.Other = billingItemsKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
billingItemsKind._InitializeFacetMap(billingItemsKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'billingItemsKind', billingItemsKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}billingTermsKind
class billingTermsKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'billingTermsKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 545, 1)
    _Documentation = None
billingTermsKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=billingTermsKind, enum_prefix=None)
billingTermsKind.Cycle = billingTermsKind._CF_enumeration.addEnumeration(unicode_value='Cycle', tag='Cycle')
billingTermsKind.Budget = billingTermsKind._CF_enumeration.addEnumeration(unicode_value='Budget', tag='Budget')
billingTermsKind.Prepay = billingTermsKind._CF_enumeration.addEnumeration(unicode_value='Prepay', tag='Prepay')
billingTermsKind.Other = billingTermsKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
billingTermsKind._InitializeFacetMap(billingTermsKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'billingTermsKind', billingTermsKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}binaryType
class binaryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of binary content in this file."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'binaryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 553, 1)
    _Documentation = 'Type of binary content in this file.'
binaryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=binaryType, enum_prefix=None)
binaryType.Text = binaryType._CF_enumeration.addEnumeration(unicode_value='Text', tag='Text')
binaryType.Image = binaryType._CF_enumeration.addEnumeration(unicode_value='Image', tag='Image')
binaryType.Audio = binaryType._CF_enumeration.addEnumeration(unicode_value='Audio', tag='Audio')
binaryType.Video = binaryType._CF_enumeration.addEnumeration(unicode_value='Video', tag='Video')
binaryType.Application = binaryType._CF_enumeration.addEnumeration(unicode_value='Application', tag='Application')
binaryType._InitializeFacetMap(binaryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'binaryType', binaryType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}calculationMethodKind
class calculationMethodKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This element describes whether the variant was chosen by the user or automatically chosen by the software."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'calculationMethodKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 579, 1)
    _Documentation = 'This element describes whether the variant was chosen by the user or automatically chosen by the software.'
calculationMethodKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=calculationMethodKind, enum_prefix=None)
calculationMethodKind.Unknown = calculationMethodKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
calculationMethodKind.Automatic = calculationMethodKind._CF_enumeration.addEnumeration(unicode_value='Automatic', tag='Automatic')
calculationMethodKind.Manual = calculationMethodKind._CF_enumeration.addEnumeration(unicode_value='Manual', tag='Manual')
calculationMethodKind.Other = calculationMethodKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
calculationMethodKind._InitializeFacetMap(calculationMethodKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'calculationMethodKind', calculationMethodKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}callBackTypeKind
class callBackTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'callBackTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 609, 1)
    _Documentation = None
callBackTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=callBackTypeKind, enum_prefix=None)
callBackTypeKind.Unknown = callBackTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
callBackTypeKind.IVR = callBackTypeKind._CF_enumeration.addEnumeration(unicode_value='IVR', tag='IVR')
callBackTypeKind.Manual = callBackTypeKind._CF_enumeration.addEnumeration(unicode_value='Manual', tag='Manual')
callBackTypeKind.Other = callBackTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
callBackTypeKind._InitializeFacetMap(callBackTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'callBackTypeKind', callBackTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}callType
class callType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'callType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 617, 1)
    _Documentation = None
callType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=callType, enum_prefix=None)
callType.Unknown = callType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
callType.Call = callType._CF_enumeration.addEnumeration(unicode_value='Call', tag='Call')
callType.CustomerServiceRep = callType._CF_enumeration.addEnumeration(unicode_value='CustomerServiceRep', tag='CustomerServiceRep')
callType.InboundTelephoneDevice = callType._CF_enumeration.addEnumeration(unicode_value='InboundTelephoneDevice', tag='InboundTelephoneDevice')
callType.Manual = callType._CF_enumeration.addEnumeration(unicode_value='Manual', tag='Manual')
callType.IVR = callType._CF_enumeration.addEnumeration(unicode_value='IVR', tag='IVR')
callType.Sensor = callType._CF_enumeration.addEnumeration(unicode_value='Sensor', tag='Sensor')
callType.Other = callType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
callType._InitializeFacetMap(callType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'callType', callType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}capacitanceUnits
class capacitanceUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'capacitanceUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 629, 1)
    _Documentation = None
capacitanceUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=capacitanceUnits, enum_prefix=None)
capacitanceUnits.Unknown = capacitanceUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
capacitanceUnits.F = capacitanceUnits._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
capacitanceUnits.mF = capacitanceUnits._CF_enumeration.addEnumeration(unicode_value='mF', tag='mF')
capacitanceUnits.microF = capacitanceUnits._CF_enumeration.addEnumeration(unicode_value='microF', tag='microF')
capacitanceUnits.Other = capacitanceUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
capacitanceUnits._InitializeFacetMap(capacitanceUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'capacitanceUnits', capacitanceUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}capacitorConnectionCode
class capacitorConnectionCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This enumeration outlines the possible connections for a capacitor bank."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'capacitorConnectionCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 638, 1)
    _Documentation = 'This enumeration outlines the possible connections for a capacitor bank.'
capacitorConnectionCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=capacitorConnectionCode, enum_prefix=None)
capacitorConnectionCode.ShuntWye = capacitorConnectionCode._CF_enumeration.addEnumeration(unicode_value='ShuntWye', tag='ShuntWye')
capacitorConnectionCode.ShuntUngroundedWye = capacitorConnectionCode._CF_enumeration.addEnumeration(unicode_value='ShuntUngroundedWye', tag='ShuntUngroundedWye')
capacitorConnectionCode.ShuntDelta = capacitorConnectionCode._CF_enumeration.addEnumeration(unicode_value='ShuntDelta', tag='ShuntDelta')
capacitorConnectionCode.ShuntSameAsParent = capacitorConnectionCode._CF_enumeration.addEnumeration(unicode_value='ShuntSameAsParent', tag='ShuntSameAsParent')
capacitorConnectionCode.Series = capacitorConnectionCode._CF_enumeration.addEnumeration(unicode_value='Series', tag='Series')
capacitorConnectionCode.Other = capacitorConnectionCode._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
capacitorConnectionCode._InitializeFacetMap(capacitorConnectionCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'capacitorConnectionCode', capacitorConnectionCode)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}capacitorSwitchStatusKind
class capacitorSwitchStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'capacitorSwitchStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 662, 1)
    _Documentation = None
capacitorSwitchStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=capacitorSwitchStatusKind, enum_prefix=None)
capacitorSwitchStatusKind.Unknown = capacitorSwitchStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
capacitorSwitchStatusKind.Connected = capacitorSwitchStatusKind._CF_enumeration.addEnumeration(unicode_value='Connected', tag='Connected')
capacitorSwitchStatusKind.Disconnected = capacitorSwitchStatusKind._CF_enumeration.addEnumeration(unicode_value='Disconnected', tag='Disconnected')
capacitorSwitchStatusKind.Failed = capacitorSwitchStatusKind._CF_enumeration.addEnumeration(unicode_value='Failed', tag='Failed')
capacitorSwitchStatusKind.InTransition = capacitorSwitchStatusKind._CF_enumeration.addEnumeration(unicode_value='InTransition', tag='InTransition')
capacitorSwitchStatusKind.Other = capacitorSwitchStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
capacitorSwitchStatusKind._InitializeFacetMap(capacitorSwitchStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'capacitorSwitchStatusKind', capacitorSwitchStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}cardinalHeadingKind
class cardinalHeadingKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cardinalHeadingKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 672, 1)
    _Documentation = None
cardinalHeadingKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=cardinalHeadingKind, enum_prefix=None)
cardinalHeadingKind.Unknown = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
cardinalHeadingKind.N = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
cardinalHeadingKind.NNE = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='NNE', tag='NNE')
cardinalHeadingKind.NE = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='NE', tag='NE')
cardinalHeadingKind.ENE = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='ENE', tag='ENE')
cardinalHeadingKind.E = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
cardinalHeadingKind.ESE = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='ESE', tag='ESE')
cardinalHeadingKind.SE = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='SE', tag='SE')
cardinalHeadingKind.SSE = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='SSE', tag='SSE')
cardinalHeadingKind.S = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
cardinalHeadingKind.SSW = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='SSW', tag='SSW')
cardinalHeadingKind.SW = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='SW', tag='SW')
cardinalHeadingKind.WSW = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='WSW', tag='WSW')
cardinalHeadingKind.W = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
cardinalHeadingKind.WNW = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='WNW', tag='WNW')
cardinalHeadingKind.NW = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='NW', tag='NW')
cardinalHeadingKind.NNW = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='NNW', tag='NNW')
cardinalHeadingKind.Other = cardinalHeadingKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
cardinalHeadingKind._InitializeFacetMap(cardinalHeadingKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'cardinalHeadingKind', cardinalHeadingKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}CDReasonCodeKind
class CDReasonCodeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CDReasonCodeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 788, 1)
    _Documentation = None
CDReasonCodeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CDReasonCodeKind, enum_prefix=None)
CDReasonCodeKind.Unknown = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
CDReasonCodeKind.PPMBalanceNegative = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='PPMBalanceNegative', tag='PPMBalanceNegative')
CDReasonCodeKind.PPMBalancePositive = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='PPMBalancePositive', tag='PPMBalancePositive')
CDReasonCodeKind.NonPayment = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='NonPayment', tag='NonPayment')
CDReasonCodeKind.ServiceInactive = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='ServiceInactive', tag='ServiceInactive')
CDReasonCodeKind.PaymentAgreement = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='PaymentAgreement', tag='PaymentAgreement')
CDReasonCodeKind.PaymentReceived = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='PaymentReceived', tag='PaymentReceived')
CDReasonCodeKind.NewCustomer = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='NewCustomer', tag='NewCustomer')
CDReasonCodeKind.ServiceRestored = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='ServiceRestored', tag='ServiceRestored')
CDReasonCodeKind.ServiceReconnected = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='ServiceReconnected', tag='ServiceReconnected')
CDReasonCodeKind.Other = CDReasonCodeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
CDReasonCodeKind._InitializeFacetMap(CDReasonCodeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CDReasonCodeKind', CDReasonCodeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}clockPosition
class clockPosition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This is the phase shift for this winding from the primary winding expressed in clock position nomenclature, where lagging phase shifts are expressed as positive clockwise positions.  Each 30 degrees of phase shift corresponds to one hour of clock position.  For instance a delta-wye transformer with delta-connected high side and wye-connected low side that has a 30 degree phase shift between the high side and the low side (low side lagging by 30 degrees) would have a clock position of 1."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'clockPosition')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 803, 1)
    _Documentation = 'This is the phase shift for this winding from the primary winding expressed in clock position nomenclature, where lagging phase shifts are expressed as positive clockwise positions.  Each 30 degrees of phase shift corresponds to one hour of clock position.  For instance a delta-wye transformer with delta-connected high side and wye-connected low side that has a 30 degree phase shift between the high side and the low side (low side lagging by 30 degrees) would have a clock position of 1.'
clockPosition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=clockPosition, enum_prefix=None)
clockPosition.n0 = clockPosition._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
clockPosition.n1 = clockPosition._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
clockPosition.n2 = clockPosition._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
clockPosition.n3 = clockPosition._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
clockPosition.n4 = clockPosition._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
clockPosition.n5 = clockPosition._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
clockPosition.n6 = clockPosition._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
clockPosition.n7 = clockPosition._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
clockPosition.n8 = clockPosition._CF_enumeration.addEnumeration(unicode_value='8', tag='n8')
clockPosition.n9 = clockPosition._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
clockPosition.n10 = clockPosition._CF_enumeration.addEnumeration(unicode_value='10', tag='n10')
clockPosition.n11 = clockPosition._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
clockPosition._InitializeFacetMap(clockPosition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'clockPosition', clockPosition)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}conduitMaterialKind
class conduitMaterialKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'conduitMaterialKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 833, 1)
    _Documentation = None
conduitMaterialKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=conduitMaterialKind, enum_prefix=None)
conduitMaterialKind.Unknown = conduitMaterialKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
conduitMaterialKind.PVC = conduitMaterialKind._CF_enumeration.addEnumeration(unicode_value='PVC', tag='PVC')
conduitMaterialKind.PE = conduitMaterialKind._CF_enumeration.addEnumeration(unicode_value='PE', tag='PE')
conduitMaterialKind.Fiber = conduitMaterialKind._CF_enumeration.addEnumeration(unicode_value='Fiber', tag='Fiber')
conduitMaterialKind.Transite = conduitMaterialKind._CF_enumeration.addEnumeration(unicode_value='Transite', tag='Transite')
conduitMaterialKind.Steel = conduitMaterialKind._CF_enumeration.addEnumeration(unicode_value='Steel', tag='Steel')
conduitMaterialKind.Other = conduitMaterialKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
conduitMaterialKind._InitializeFacetMap(conduitMaterialKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'conduitMaterialKind', conduitMaterialKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}connectivityModelKind
class connectivityModelKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This attribute, if used, specifies whether the connectivity model included uses nodal or sectional references."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'connectivityModelKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 844, 1)
    _Documentation = 'This attribute, if used, specifies whether the connectivity model included uses nodal or sectional references.'
connectivityModelKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=connectivityModelKind, enum_prefix=None)
connectivityModelKind.Nodal = connectivityModelKind._CF_enumeration.addEnumeration(unicode_value='Nodal', tag='Nodal')
connectivityModelKind.Sectional = connectivityModelKind._CF_enumeration.addEnumeration(unicode_value='Sectional', tag='Sectional')
connectivityModelKind._InitializeFacetMap(connectivityModelKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'connectivityModelKind', connectivityModelKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}connectivityStatusKind
class connectivityStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'connectivityStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 867, 1)
    _Documentation = None
connectivityStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=connectivityStatusKind, enum_prefix=None)
connectivityStatusKind.Unknown = connectivityStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
connectivityStatusKind.Connected = connectivityStatusKind._CF_enumeration.addEnumeration(unicode_value='Connected', tag='Connected')
connectivityStatusKind.Disconnected = connectivityStatusKind._CF_enumeration.addEnumeration(unicode_value='Disconnected', tag='Disconnected')
connectivityStatusKind.Other = connectivityStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
connectivityStatusKind._InitializeFacetMap(connectivityStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'connectivityStatusKind', connectivityStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}connectorStatus
class connectorStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'connectorStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 875, 1)
    _Documentation = None
connectorStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=connectorStatus, enum_prefix=None)
connectorStatus.Unknown = connectorStatus._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
connectorStatus.OutOfService = connectorStatus._CF_enumeration.addEnumeration(unicode_value='OutOfService', tag='OutOfService')
connectorStatus.Wired = connectorStatus._CF_enumeration.addEnumeration(unicode_value='Wired', tag='Wired')
connectorStatus.Other = connectorStatus._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
connectorStatus._InitializeFacetMap(connectorStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'connectorStatus', connectorStatus)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}constructionGradeKind
class constructionGradeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'constructionGradeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 894, 1)
    _Documentation = None
constructionGradeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=constructionGradeKind, enum_prefix=None)
constructionGradeKind.Unknown = constructionGradeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
constructionGradeKind.GradeB = constructionGradeKind._CF_enumeration.addEnumeration(unicode_value='GradeB', tag='GradeB')
constructionGradeKind.GradeC = constructionGradeKind._CF_enumeration.addEnumeration(unicode_value='GradeC', tag='GradeC')
constructionGradeKind.GradeN = constructionGradeKind._CF_enumeration.addEnumeration(unicode_value='GradeN', tag='GradeN')
constructionGradeKind.Other = constructionGradeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
constructionGradeKind._InitializeFacetMap(constructionGradeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'constructionGradeKind', constructionGradeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}constructionLevelKind
class constructionLevelKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This is the level at which this line is constructed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'constructionLevelKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 917, 1)
    _Documentation = 'This is the level at which this line is constructed.'
constructionLevelKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=constructionLevelKind, enum_prefix=None)
constructionLevelKind.Unknown = constructionLevelKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
constructionLevelKind.Overhead = constructionLevelKind._CF_enumeration.addEnumeration(unicode_value='Overhead', tag='Overhead')
constructionLevelKind.Underbuild = constructionLevelKind._CF_enumeration.addEnumeration(unicode_value='Underbuild', tag='Underbuild')
constructionLevelKind.Underground = constructionLevelKind._CF_enumeration.addEnumeration(unicode_value='Underground', tag='Underground')
constructionLevelKind.Other = constructionLevelKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
constructionLevelKind._InitializeFacetMap(constructionLevelKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'constructionLevelKind', constructionLevelKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}constructionReferenceKind
class constructionReferenceKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This enumeration gives context to a constructionItem as part of an ACLineSegment."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'constructionReferenceKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 929, 1)
    _Documentation = 'This enumeration gives context to a constructionItem as part of an ACLineSegment.'
constructionReferenceKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=constructionReferenceKind, enum_prefix=None)
constructionReferenceKind.Unknown = constructionReferenceKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
constructionReferenceKind.BackSpan = constructionReferenceKind._CF_enumeration.addEnumeration(unicode_value='BackSpan', tag='BackSpan')
constructionReferenceKind.HeadSpan = constructionReferenceKind._CF_enumeration.addEnumeration(unicode_value='HeadSpan', tag='HeadSpan')
constructionReferenceKind.Conduit = constructionReferenceKind._CF_enumeration.addEnumeration(unicode_value='Conduit', tag='Conduit')
constructionReferenceKind.Other = constructionReferenceKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
constructionReferenceKind._InitializeFacetMap(constructionReferenceKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'constructionReferenceKind', constructionReferenceKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}constTypeKind
class constTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Construction type code for construction at this location. This field is used to specify whether the units applied to this station use the hot labor estimates or the cold labor estimates.  Suggested enumerations are (Hot and Cold)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'constTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 969, 1)
    _Documentation = 'Construction type code for construction at this location. This field is used to specify whether the units applied to this station use the hot labor estimates or the cold labor estimates.  Suggested enumerations are (Hot and Cold).'
constTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=constTypeKind, enum_prefix=None)
constTypeKind.Unknown = constTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
constTypeKind.Hot = constTypeKind._CF_enumeration.addEnumeration(unicode_value='Hot', tag='Hot')
constTypeKind.Cold = constTypeKind._CF_enumeration.addEnumeration(unicode_value='Cold', tag='Cold')
constTypeKind.Other = constTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
constTypeKind._InitializeFacetMap(constTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'constTypeKind', constTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}contactRequestStatusKind
class contactRequestStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contactRequestStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 991, 1)
    _Documentation = None
contactRequestStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=contactRequestStatusKind, enum_prefix=None)
contactRequestStatusKind.Unknown = contactRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
contactRequestStatusKind.Successful = contactRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='Successful', tag='Successful')
contactRequestStatusKind.Undialable = contactRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='Undialable', tag='Undialable')
contactRequestStatusKind.MaxDial = contactRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='MaxDial', tag='MaxDial')
contactRequestStatusKind.NoResponse = contactRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='NoResponse', tag='NoResponse')
contactRequestStatusKind.Other = contactRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
contactRequestStatusKind._InitializeFacetMap(contactRequestStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'contactRequestStatusKind', contactRequestStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}contentEncodingKind
class contentEncodingKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contentEncodingKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1001, 1)
    _Documentation = None
contentEncodingKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=contentEncodingKind, enum_prefix=None)
contentEncodingKind.gzip = contentEncodingKind._CF_enumeration.addEnumeration(unicode_value='gzip', tag='gzip')
contentEncodingKind.compress = contentEncodingKind._CF_enumeration.addEnumeration(unicode_value='compress', tag='compress')
contentEncodingKind.deflate = contentEncodingKind._CF_enumeration.addEnumeration(unicode_value='deflate', tag='deflate')
contentEncodingKind.exi = contentEncodingKind._CF_enumeration.addEnumeration(unicode_value='exi', tag='exi')
contentEncodingKind.pack200_gzip = contentEncodingKind._CF_enumeration.addEnumeration(unicode_value='pack200-gzip', tag='pack200_gzip')
contentEncodingKind.Other = contentEncodingKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
contentEncodingKind._InitializeFacetMap(contentEncodingKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'contentEncodingKind', contentEncodingKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}controlCodeKind
class controlCodeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This element describes the type of switching to send.  The enumeration list is: Pulse on, Pulse off, Latch on, and Latch off."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'controlCodeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1053, 1)
    _Documentation = 'This element describes the type of switching to send.  The enumeration list is: Pulse on, Pulse off, Latch on, and Latch off.'
controlCodeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=controlCodeKind, enum_prefix=None)
controlCodeKind.Pulse_on = controlCodeKind._CF_enumeration.addEnumeration(unicode_value='Pulse on', tag='Pulse_on')
controlCodeKind.Pulse_off = controlCodeKind._CF_enumeration.addEnumeration(unicode_value='Pulse off', tag='Pulse_off')
controlCodeKind.Latch_on = controlCodeKind._CF_enumeration.addEnumeration(unicode_value='Latch on', tag='Latch_on')
controlCodeKind.Latch_off = controlCodeKind._CF_enumeration.addEnumeration(unicode_value='Latch off', tag='Latch_off')
controlCodeKind.Other = controlCodeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
controlCodeKind._InitializeFacetMap(controlCodeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'controlCodeKind', controlCodeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}controlEventKind
class controlEventKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'controlEventKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1065, 1)
    _Documentation = None
controlEventKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=controlEventKind, enum_prefix=None)
controlEventKind.Initiate = controlEventKind._CF_enumeration.addEnumeration(unicode_value='Initiate', tag='Initiate')
controlEventKind.Restore = controlEventKind._CF_enumeration.addEnumeration(unicode_value='Restore', tag='Restore')
controlEventKind.Other = controlEventKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
controlEventKind._InitializeFacetMap(controlEventKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'controlEventKind', controlEventKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}controlStatusKind
class controlStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """These are the control status indications.  The equivalent DNP 3.0 status codes are:             
Control accepted = 0                                 
Operate message received after arm timer timed out (Select timeout)= 1 Point not operated because point not selected before operation (Point not selected)= 2 Control request not accepted; formatting errors in control action (Formatting errors in control request)= 3                                                                  
Control operation not supported for this point (Control not supported) = 4 Control queue is full = 5                              
Control request not accepted, control hardware problems (Hardware failure)= 6 Point already selected - undefined in DNP 3.0               """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'controlStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1101, 1)
    _Documentation = 'These are the control status indications.  The equivalent DNP 3.0 status codes are:             \nControl accepted = 0                                 \nOperate message received after arm timer timed out (Select timeout)= 1 Point not operated because point not selected before operation (Point not selected)= 2 Control request not accepted; formatting errors in control action (Formatting errors in control request)= 3                                                                  \nControl operation not supported for this point (Control not supported) = 4 Control queue is full = 5                              \nControl request not accepted, control hardware problems (Hardware failure)= 6 Point already selected - undefined in DNP 3.0               '
controlStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=controlStatusKind, enum_prefix=None)
controlStatusKind.Unknown = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
controlStatusKind.ControlAccepted = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='ControlAccepted', tag='ControlAccepted')
controlStatusKind.SelectTimeout = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='SelectTimeout', tag='SelectTimeout')
controlStatusKind.PointNotSelected = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='PointNotSelected', tag='PointNotSelected')
controlStatusKind.FormattingErrorsInControlRequest = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='FormattingErrorsInControlRequest', tag='FormattingErrorsInControlRequest')
controlStatusKind.ControlNotSupported = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='ControlNotSupported', tag='ControlNotSupported')
controlStatusKind.ControlQueueFull = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='ControlQueueFull', tag='ControlQueueFull')
controlStatusKind.HardwareFailure = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='HardwareFailure', tag='HardwareFailure')
controlStatusKind.PointAlreadySelected = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='PointAlreadySelected', tag='PointAlreadySelected')
controlStatusKind.Other = controlStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
controlStatusKind._InitializeFacetMap(controlStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'controlStatusKind', controlStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}cumDemandType
class cumDemandType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cumDemandType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1122, 1)
    _Documentation = None
cumDemandType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=cumDemandType, enum_prefix=None)
cumDemandType.Max = cumDemandType._CF_enumeration.addEnumeration(unicode_value='Max', tag='Max')
cumDemandType.Min = cumDemandType._CF_enumeration.addEnumeration(unicode_value='Min', tag='Min')
cumDemandType.ContinousMax = cumDemandType._CF_enumeration.addEnumeration(unicode_value='ContinousMax', tag='ContinousMax')
cumDemandType.ContinousMin = cumDemandType._CF_enumeration.addEnumeration(unicode_value='ContinousMin', tag='ContinousMin')
cumDemandType._InitializeFacetMap(cumDemandType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'cumDemandType', cumDemandType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}currencyCode
class currencyCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Three letter currency code as standardized in ISO4217-2001. Typically is the two letter Internet domain code for the country followed by a one letter designator for the currency; for instance the USA dollar is USD."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'currencyCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1130, 1)
    _Documentation = 'Three letter currency code as standardized in ISO4217-2001. Typically is the two letter Internet domain code for the country followed by a one letter designator for the currency; for instance the USA dollar is USD.'
currencyCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=currencyCode, enum_prefix=None)
currencyCode.USD = currencyCode._CF_enumeration.addEnumeration(unicode_value='USD', tag='USD')
currencyCode.EUR = currencyCode._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
currencyCode.ADF = currencyCode._CF_enumeration.addEnumeration(unicode_value='ADF', tag='ADF')
currencyCode.ADP = currencyCode._CF_enumeration.addEnumeration(unicode_value='ADP', tag='ADP')
currencyCode.AED = currencyCode._CF_enumeration.addEnumeration(unicode_value='AED', tag='AED')
currencyCode.AFN = currencyCode._CF_enumeration.addEnumeration(unicode_value='AFN', tag='AFN')
currencyCode.ALL = currencyCode._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
currencyCode.AMD = currencyCode._CF_enumeration.addEnumeration(unicode_value='AMD', tag='AMD')
currencyCode.ANG = currencyCode._CF_enumeration.addEnumeration(unicode_value='ANG', tag='ANG')
currencyCode.AOA = currencyCode._CF_enumeration.addEnumeration(unicode_value='AOA', tag='AOA')
currencyCode.ARS = currencyCode._CF_enumeration.addEnumeration(unicode_value='ARS', tag='ARS')
currencyCode.ATS = currencyCode._CF_enumeration.addEnumeration(unicode_value='ATS', tag='ATS')
currencyCode.AUD = currencyCode._CF_enumeration.addEnumeration(unicode_value='AUD', tag='AUD')
currencyCode.AWG = currencyCode._CF_enumeration.addEnumeration(unicode_value='AWG', tag='AWG')
currencyCode.AZN = currencyCode._CF_enumeration.addEnumeration(unicode_value='AZN', tag='AZN')
currencyCode.BAM = currencyCode._CF_enumeration.addEnumeration(unicode_value='BAM', tag='BAM')
currencyCode.BBD = currencyCode._CF_enumeration.addEnumeration(unicode_value='BBD', tag='BBD')
currencyCode.BDT = currencyCode._CF_enumeration.addEnumeration(unicode_value='BDT', tag='BDT')
currencyCode.BEF = currencyCode._CF_enumeration.addEnumeration(unicode_value='BEF', tag='BEF')
currencyCode.BGN = currencyCode._CF_enumeration.addEnumeration(unicode_value='BGN', tag='BGN')
currencyCode.BHD = currencyCode._CF_enumeration.addEnumeration(unicode_value='BHD', tag='BHD')
currencyCode.BIF = currencyCode._CF_enumeration.addEnumeration(unicode_value='BIF', tag='BIF')
currencyCode.BMD = currencyCode._CF_enumeration.addEnumeration(unicode_value='BMD', tag='BMD')
currencyCode.BND = currencyCode._CF_enumeration.addEnumeration(unicode_value='BND', tag='BND')
currencyCode.BOB = currencyCode._CF_enumeration.addEnumeration(unicode_value='BOB', tag='BOB')
currencyCode.BOV = currencyCode._CF_enumeration.addEnumeration(unicode_value='BOV', tag='BOV')
currencyCode.BRL = currencyCode._CF_enumeration.addEnumeration(unicode_value='BRL', tag='BRL')
currencyCode.BSD = currencyCode._CF_enumeration.addEnumeration(unicode_value='BSD', tag='BSD')
currencyCode.BTN = currencyCode._CF_enumeration.addEnumeration(unicode_value='BTN', tag='BTN')
currencyCode.BWP = currencyCode._CF_enumeration.addEnumeration(unicode_value='BWP', tag='BWP')
currencyCode.BYR = currencyCode._CF_enumeration.addEnumeration(unicode_value='BYR', tag='BYR')
currencyCode.BZD = currencyCode._CF_enumeration.addEnumeration(unicode_value='BZD', tag='BZD')
currencyCode.CAD = currencyCode._CF_enumeration.addEnumeration(unicode_value='CAD', tag='CAD')
currencyCode.CDF = currencyCode._CF_enumeration.addEnumeration(unicode_value='CDF', tag='CDF')
currencyCode.CHE = currencyCode._CF_enumeration.addEnumeration(unicode_value='CHE', tag='CHE')
currencyCode.CHF = currencyCode._CF_enumeration.addEnumeration(unicode_value='CHF', tag='CHF')
currencyCode.CHW = currencyCode._CF_enumeration.addEnumeration(unicode_value='CHW', tag='CHW')
currencyCode.CLF = currencyCode._CF_enumeration.addEnumeration(unicode_value='CLF', tag='CLF')
currencyCode.CLP = currencyCode._CF_enumeration.addEnumeration(unicode_value='CLP', tag='CLP')
currencyCode.CNY = currencyCode._CF_enumeration.addEnumeration(unicode_value='CNY', tag='CNY')
currencyCode.COP = currencyCode._CF_enumeration.addEnumeration(unicode_value='COP', tag='COP')
currencyCode.COU = currencyCode._CF_enumeration.addEnumeration(unicode_value='COU', tag='COU')
currencyCode.CRC = currencyCode._CF_enumeration.addEnumeration(unicode_value='CRC', tag='CRC')
currencyCode.CUP = currencyCode._CF_enumeration.addEnumeration(unicode_value='CUP', tag='CUP')
currencyCode.CVE = currencyCode._CF_enumeration.addEnumeration(unicode_value='CVE', tag='CVE')
currencyCode.CYP = currencyCode._CF_enumeration.addEnumeration(unicode_value='CYP', tag='CYP')
currencyCode.CZK = currencyCode._CF_enumeration.addEnumeration(unicode_value='CZK', tag='CZK')
currencyCode.DEM = currencyCode._CF_enumeration.addEnumeration(unicode_value='DEM', tag='DEM')
currencyCode.DJF = currencyCode._CF_enumeration.addEnumeration(unicode_value='DJF', tag='DJF')
currencyCode.DKK = currencyCode._CF_enumeration.addEnumeration(unicode_value='DKK', tag='DKK')
currencyCode.DOP = currencyCode._CF_enumeration.addEnumeration(unicode_value='DOP', tag='DOP')
currencyCode.DZD = currencyCode._CF_enumeration.addEnumeration(unicode_value='DZD', tag='DZD')
currencyCode.EEK = currencyCode._CF_enumeration.addEnumeration(unicode_value='EEK', tag='EEK')
currencyCode.EGP = currencyCode._CF_enumeration.addEnumeration(unicode_value='EGP', tag='EGP')
currencyCode.ERN = currencyCode._CF_enumeration.addEnumeration(unicode_value='ERN', tag='ERN')
currencyCode.ESP = currencyCode._CF_enumeration.addEnumeration(unicode_value='ESP', tag='ESP')
currencyCode.ETB = currencyCode._CF_enumeration.addEnumeration(unicode_value='ETB', tag='ETB')
currencyCode.FIM = currencyCode._CF_enumeration.addEnumeration(unicode_value='FIM', tag='FIM')
currencyCode.FJD = currencyCode._CF_enumeration.addEnumeration(unicode_value='FJD', tag='FJD')
currencyCode.FKP = currencyCode._CF_enumeration.addEnumeration(unicode_value='FKP', tag='FKP')
currencyCode.FRF = currencyCode._CF_enumeration.addEnumeration(unicode_value='FRF', tag='FRF')
currencyCode.GBP = currencyCode._CF_enumeration.addEnumeration(unicode_value='GBP', tag='GBP')
currencyCode.GEL = currencyCode._CF_enumeration.addEnumeration(unicode_value='GEL', tag='GEL')
currencyCode.GHS = currencyCode._CF_enumeration.addEnumeration(unicode_value='GHS', tag='GHS')
currencyCode.GIP = currencyCode._CF_enumeration.addEnumeration(unicode_value='GIP', tag='GIP')
currencyCode.GMD = currencyCode._CF_enumeration.addEnumeration(unicode_value='GMD', tag='GMD')
currencyCode.GNF = currencyCode._CF_enumeration.addEnumeration(unicode_value='GNF', tag='GNF')
currencyCode.GRD = currencyCode._CF_enumeration.addEnumeration(unicode_value='GRD', tag='GRD')
currencyCode.GTQ = currencyCode._CF_enumeration.addEnumeration(unicode_value='GTQ', tag='GTQ')
currencyCode.GYD = currencyCode._CF_enumeration.addEnumeration(unicode_value='GYD', tag='GYD')
currencyCode.HKD = currencyCode._CF_enumeration.addEnumeration(unicode_value='HKD', tag='HKD')
currencyCode.HNL = currencyCode._CF_enumeration.addEnumeration(unicode_value='HNL', tag='HNL')
currencyCode.HRK = currencyCode._CF_enumeration.addEnumeration(unicode_value='HRK', tag='HRK')
currencyCode.HTG = currencyCode._CF_enumeration.addEnumeration(unicode_value='HTG', tag='HTG')
currencyCode.HUF = currencyCode._CF_enumeration.addEnumeration(unicode_value='HUF', tag='HUF')
currencyCode.IDR = currencyCode._CF_enumeration.addEnumeration(unicode_value='IDR', tag='IDR')
currencyCode.IEP = currencyCode._CF_enumeration.addEnumeration(unicode_value='IEP', tag='IEP')
currencyCode.ILS = currencyCode._CF_enumeration.addEnumeration(unicode_value='ILS', tag='ILS')
currencyCode.INR = currencyCode._CF_enumeration.addEnumeration(unicode_value='INR', tag='INR')
currencyCode.IQD = currencyCode._CF_enumeration.addEnumeration(unicode_value='IQD', tag='IQD')
currencyCode.IRR = currencyCode._CF_enumeration.addEnumeration(unicode_value='IRR', tag='IRR')
currencyCode.ISK = currencyCode._CF_enumeration.addEnumeration(unicode_value='ISK', tag='ISK')
currencyCode.ITL = currencyCode._CF_enumeration.addEnumeration(unicode_value='ITL', tag='ITL')
currencyCode.JMD = currencyCode._CF_enumeration.addEnumeration(unicode_value='JMD', tag='JMD')
currencyCode.JOD = currencyCode._CF_enumeration.addEnumeration(unicode_value='JOD', tag='JOD')
currencyCode.JPY = currencyCode._CF_enumeration.addEnumeration(unicode_value='JPY', tag='JPY')
currencyCode.KES = currencyCode._CF_enumeration.addEnumeration(unicode_value='KES', tag='KES')
currencyCode.KGS = currencyCode._CF_enumeration.addEnumeration(unicode_value='KGS', tag='KGS')
currencyCode.KHR = currencyCode._CF_enumeration.addEnumeration(unicode_value='KHR', tag='KHR')
currencyCode.KMF = currencyCode._CF_enumeration.addEnumeration(unicode_value='KMF', tag='KMF')
currencyCode.KPW = currencyCode._CF_enumeration.addEnumeration(unicode_value='KPW', tag='KPW')
currencyCode.KRW = currencyCode._CF_enumeration.addEnumeration(unicode_value='KRW', tag='KRW')
currencyCode.KWD = currencyCode._CF_enumeration.addEnumeration(unicode_value='KWD', tag='KWD')
currencyCode.KYD = currencyCode._CF_enumeration.addEnumeration(unicode_value='KYD', tag='KYD')
currencyCode.KZT = currencyCode._CF_enumeration.addEnumeration(unicode_value='KZT', tag='KZT')
currencyCode.LAK = currencyCode._CF_enumeration.addEnumeration(unicode_value='LAK', tag='LAK')
currencyCode.LBP = currencyCode._CF_enumeration.addEnumeration(unicode_value='LBP', tag='LBP')
currencyCode.LKR = currencyCode._CF_enumeration.addEnumeration(unicode_value='LKR', tag='LKR')
currencyCode.LRD = currencyCode._CF_enumeration.addEnumeration(unicode_value='LRD', tag='LRD')
currencyCode.LSL = currencyCode._CF_enumeration.addEnumeration(unicode_value='LSL', tag='LSL')
currencyCode.LTL = currencyCode._CF_enumeration.addEnumeration(unicode_value='LTL', tag='LTL')
currencyCode.LUF = currencyCode._CF_enumeration.addEnumeration(unicode_value='LUF', tag='LUF')
currencyCode.LVL = currencyCode._CF_enumeration.addEnumeration(unicode_value='LVL', tag='LVL')
currencyCode.LYD = currencyCode._CF_enumeration.addEnumeration(unicode_value='LYD', tag='LYD')
currencyCode.MAD = currencyCode._CF_enumeration.addEnumeration(unicode_value='MAD', tag='MAD')
currencyCode.MCF = currencyCode._CF_enumeration.addEnumeration(unicode_value='MCF', tag='MCF')
currencyCode.MDL = currencyCode._CF_enumeration.addEnumeration(unicode_value='MDL', tag='MDL')
currencyCode.MGA = currencyCode._CF_enumeration.addEnumeration(unicode_value='MGA', tag='MGA')
currencyCode.MKD = currencyCode._CF_enumeration.addEnumeration(unicode_value='MKD', tag='MKD')
currencyCode.MMK = currencyCode._CF_enumeration.addEnumeration(unicode_value='MMK', tag='MMK')
currencyCode.MNT = currencyCode._CF_enumeration.addEnumeration(unicode_value='MNT', tag='MNT')
currencyCode.MOP = currencyCode._CF_enumeration.addEnumeration(unicode_value='MOP', tag='MOP')
currencyCode.MRO = currencyCode._CF_enumeration.addEnumeration(unicode_value='MRO', tag='MRO')
currencyCode.MTL = currencyCode._CF_enumeration.addEnumeration(unicode_value='MTL', tag='MTL')
currencyCode.MUR = currencyCode._CF_enumeration.addEnumeration(unicode_value='MUR', tag='MUR')
currencyCode.MVR = currencyCode._CF_enumeration.addEnumeration(unicode_value='MVR', tag='MVR')
currencyCode.MWK = currencyCode._CF_enumeration.addEnumeration(unicode_value='MWK', tag='MWK')
currencyCode.MXN = currencyCode._CF_enumeration.addEnumeration(unicode_value='MXN', tag='MXN')
currencyCode.MXV = currencyCode._CF_enumeration.addEnumeration(unicode_value='MXV', tag='MXV')
currencyCode.MYR = currencyCode._CF_enumeration.addEnumeration(unicode_value='MYR', tag='MYR')
currencyCode.MZN = currencyCode._CF_enumeration.addEnumeration(unicode_value='MZN', tag='MZN')
currencyCode.NAD = currencyCode._CF_enumeration.addEnumeration(unicode_value='NAD', tag='NAD')
currencyCode.NGN = currencyCode._CF_enumeration.addEnumeration(unicode_value='NGN', tag='NGN')
currencyCode.NIO = currencyCode._CF_enumeration.addEnumeration(unicode_value='NIO', tag='NIO')
currencyCode.NLG = currencyCode._CF_enumeration.addEnumeration(unicode_value='NLG', tag='NLG')
currencyCode.NOK = currencyCode._CF_enumeration.addEnumeration(unicode_value='NOK', tag='NOK')
currencyCode.NPR = currencyCode._CF_enumeration.addEnumeration(unicode_value='NPR', tag='NPR')
currencyCode.NZD = currencyCode._CF_enumeration.addEnumeration(unicode_value='NZD', tag='NZD')
currencyCode.OMR = currencyCode._CF_enumeration.addEnumeration(unicode_value='OMR', tag='OMR')
currencyCode.PAB = currencyCode._CF_enumeration.addEnumeration(unicode_value='PAB', tag='PAB')
currencyCode.PEN = currencyCode._CF_enumeration.addEnumeration(unicode_value='PEN', tag='PEN')
currencyCode.PGK = currencyCode._CF_enumeration.addEnumeration(unicode_value='PGK', tag='PGK')
currencyCode.PHP = currencyCode._CF_enumeration.addEnumeration(unicode_value='PHP', tag='PHP')
currencyCode.PKR = currencyCode._CF_enumeration.addEnumeration(unicode_value='PKR', tag='PKR')
currencyCode.PLN = currencyCode._CF_enumeration.addEnumeration(unicode_value='PLN', tag='PLN')
currencyCode.PTE = currencyCode._CF_enumeration.addEnumeration(unicode_value='PTE', tag='PTE')
currencyCode.PYG = currencyCode._CF_enumeration.addEnumeration(unicode_value='PYG', tag='PYG')
currencyCode.QAR = currencyCode._CF_enumeration.addEnumeration(unicode_value='QAR', tag='QAR')
currencyCode.RON = currencyCode._CF_enumeration.addEnumeration(unicode_value='RON', tag='RON')
currencyCode.RSD = currencyCode._CF_enumeration.addEnumeration(unicode_value='RSD', tag='RSD')
currencyCode.RUB = currencyCode._CF_enumeration.addEnumeration(unicode_value='RUB', tag='RUB')
currencyCode.RWF = currencyCode._CF_enumeration.addEnumeration(unicode_value='RWF', tag='RWF')
currencyCode.SAR = currencyCode._CF_enumeration.addEnumeration(unicode_value='SAR', tag='SAR')
currencyCode.SBD = currencyCode._CF_enumeration.addEnumeration(unicode_value='SBD', tag='SBD')
currencyCode.SCR = currencyCode._CF_enumeration.addEnumeration(unicode_value='SCR', tag='SCR')
currencyCode.SDG = currencyCode._CF_enumeration.addEnumeration(unicode_value='SDG', tag='SDG')
currencyCode.SEK = currencyCode._CF_enumeration.addEnumeration(unicode_value='SEK', tag='SEK')
currencyCode.SGD = currencyCode._CF_enumeration.addEnumeration(unicode_value='SGD', tag='SGD')
currencyCode.SHP = currencyCode._CF_enumeration.addEnumeration(unicode_value='SHP', tag='SHP')
currencyCode.SIT = currencyCode._CF_enumeration.addEnumeration(unicode_value='SIT', tag='SIT')
currencyCode.SKK = currencyCode._CF_enumeration.addEnumeration(unicode_value='SKK', tag='SKK')
currencyCode.SLL = currencyCode._CF_enumeration.addEnumeration(unicode_value='SLL', tag='SLL')
currencyCode.SML = currencyCode._CF_enumeration.addEnumeration(unicode_value='SML', tag='SML')
currencyCode.SOS = currencyCode._CF_enumeration.addEnumeration(unicode_value='SOS', tag='SOS')
currencyCode.SRD = currencyCode._CF_enumeration.addEnumeration(unicode_value='SRD', tag='SRD')
currencyCode.STD = currencyCode._CF_enumeration.addEnumeration(unicode_value='STD', tag='STD')
currencyCode.SYP = currencyCode._CF_enumeration.addEnumeration(unicode_value='SYP', tag='SYP')
currencyCode.SZL = currencyCode._CF_enumeration.addEnumeration(unicode_value='SZL', tag='SZL')
currencyCode.THB = currencyCode._CF_enumeration.addEnumeration(unicode_value='THB', tag='THB')
currencyCode.TJS = currencyCode._CF_enumeration.addEnumeration(unicode_value='TJS', tag='TJS')
currencyCode.TMM = currencyCode._CF_enumeration.addEnumeration(unicode_value='TMM', tag='TMM')
currencyCode.TND = currencyCode._CF_enumeration.addEnumeration(unicode_value='TND', tag='TND')
currencyCode.TOP = currencyCode._CF_enumeration.addEnumeration(unicode_value='TOP', tag='TOP')
currencyCode.TRY = currencyCode._CF_enumeration.addEnumeration(unicode_value='TRY', tag='TRY')
currencyCode.TTD = currencyCode._CF_enumeration.addEnumeration(unicode_value='TTD', tag='TTD')
currencyCode.TWD = currencyCode._CF_enumeration.addEnumeration(unicode_value='TWD', tag='TWD')
currencyCode.TZS = currencyCode._CF_enumeration.addEnumeration(unicode_value='TZS', tag='TZS')
currencyCode.UAH = currencyCode._CF_enumeration.addEnumeration(unicode_value='UAH', tag='UAH')
currencyCode.UGX = currencyCode._CF_enumeration.addEnumeration(unicode_value='UGX', tag='UGX')
currencyCode.USN = currencyCode._CF_enumeration.addEnumeration(unicode_value='USN', tag='USN')
currencyCode.USS = currencyCode._CF_enumeration.addEnumeration(unicode_value='USS', tag='USS')
currencyCode.UYU = currencyCode._CF_enumeration.addEnumeration(unicode_value='UYU', tag='UYU')
currencyCode.UZS = currencyCode._CF_enumeration.addEnumeration(unicode_value='UZS', tag='UZS')
currencyCode.VAL = currencyCode._CF_enumeration.addEnumeration(unicode_value='VAL', tag='VAL')
currencyCode.VEF = currencyCode._CF_enumeration.addEnumeration(unicode_value='VEF', tag='VEF')
currencyCode.VND = currencyCode._CF_enumeration.addEnumeration(unicode_value='VND', tag='VND')
currencyCode.VUV = currencyCode._CF_enumeration.addEnumeration(unicode_value='VUV', tag='VUV')
currencyCode.WST = currencyCode._CF_enumeration.addEnumeration(unicode_value='WST', tag='WST')
currencyCode.XAF = currencyCode._CF_enumeration.addEnumeration(unicode_value='XAF', tag='XAF')
currencyCode.XAG = currencyCode._CF_enumeration.addEnumeration(unicode_value='XAG', tag='XAG')
currencyCode.XAU = currencyCode._CF_enumeration.addEnumeration(unicode_value='XAU', tag='XAU')
currencyCode.XBA = currencyCode._CF_enumeration.addEnumeration(unicode_value='XBA', tag='XBA')
currencyCode.XBB = currencyCode._CF_enumeration.addEnumeration(unicode_value='XBB', tag='XBB')
currencyCode.XBC = currencyCode._CF_enumeration.addEnumeration(unicode_value='XBC', tag='XBC')
currencyCode.XBD = currencyCode._CF_enumeration.addEnumeration(unicode_value='XBD', tag='XBD')
currencyCode.XCD = currencyCode._CF_enumeration.addEnumeration(unicode_value='XCD', tag='XCD')
currencyCode.XDR = currencyCode._CF_enumeration.addEnumeration(unicode_value='XDR', tag='XDR')
currencyCode.XEU = currencyCode._CF_enumeration.addEnumeration(unicode_value='XEU', tag='XEU')
currencyCode.XFU = currencyCode._CF_enumeration.addEnumeration(unicode_value='XFU', tag='XFU')
currencyCode.XOF = currencyCode._CF_enumeration.addEnumeration(unicode_value='XOF', tag='XOF')
currencyCode.XPD = currencyCode._CF_enumeration.addEnumeration(unicode_value='XPD', tag='XPD')
currencyCode.XPF = currencyCode._CF_enumeration.addEnumeration(unicode_value='XPF', tag='XPF')
currencyCode.XPT = currencyCode._CF_enumeration.addEnumeration(unicode_value='XPT', tag='XPT')
currencyCode.XTS = currencyCode._CF_enumeration.addEnumeration(unicode_value='XTS', tag='XTS')
currencyCode.XXX = currencyCode._CF_enumeration.addEnumeration(unicode_value='XXX', tag='XXX')
currencyCode.YER = currencyCode._CF_enumeration.addEnumeration(unicode_value='YER', tag='YER')
currencyCode.ZAR = currencyCode._CF_enumeration.addEnumeration(unicode_value='ZAR', tag='ZAR')
currencyCode.ZMK = currencyCode._CF_enumeration.addEnumeration(unicode_value='ZMK', tag='ZMK')
currencyCode.ZWD = currencyCode._CF_enumeration.addEnumeration(unicode_value='ZWD', tag='ZWD')
currencyCode.Other = currencyCode._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
currencyCode._InitializeFacetMap(currencyCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'currencyCode', currencyCode)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}currentUnits
class currentUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'currentUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1337, 1)
    _Documentation = None
currentUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=currentUnits, enum_prefix=None)
currentUnits.Unknown = currentUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
currentUnits.A = currentUnits._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
currentUnits.mA = currentUnits._CF_enumeration.addEnumeration(unicode_value='mA', tag='mA')
currentUnits.kA = currentUnits._CF_enumeration.addEnumeration(unicode_value='kA', tag='kA')
currentUnits.MA = currentUnits._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
currentUnits.microA = currentUnits._CF_enumeration.addEnumeration(unicode_value='microA', tag='microA')
currentUnits.PerUnit = currentUnits._CF_enumeration.addEnumeration(unicode_value='PerUnit', tag='PerUnit')
currentUnits.Percent = currentUnits._CF_enumeration.addEnumeration(unicode_value='Percent', tag='Percent')
currentUnits.Other = currentUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
currentUnits._InitializeFacetMap(currentUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'currentUnits', currentUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}cutActionKind
class cutActionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cutActionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1361, 1)
    _Documentation = None
cutActionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=cutActionKind, enum_prefix=None)
cutActionKind.Unknown = cutActionKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
cutActionKind.InitiateCut = cutActionKind._CF_enumeration.addEnumeration(unicode_value='InitiateCut', tag='InitiateCut')
cutActionKind.RestoreCut = cutActionKind._CF_enumeration.addEnumeration(unicode_value='RestoreCut', tag='RestoreCut')
cutActionKind.Other = cutActionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
cutActionKind._InitializeFacetMap(cutActionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'cutActionKind', cutActionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}dayLabelKind
class dayLabelKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dayLabelKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1380, 1)
    _Documentation = None
dayLabelKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dayLabelKind, enum_prefix=None)
dayLabelKind.M = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='M', tag='M')
dayLabelKind.T = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
dayLabelKind.W = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
dayLabelKind.Th = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='Th', tag='Th')
dayLabelKind.F = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
dayLabelKind.Sa = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='Sa', tag='Sa')
dayLabelKind.Su = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='Su', tag='Su')
dayLabelKind.Weekdays = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='Weekdays', tag='Weekdays')
dayLabelKind.WeekendDays = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='WeekendDays', tag='WeekendDays')
dayLabelKind.Other = dayLabelKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
dayLabelKind._InitializeFacetMap(dayLabelKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'dayLabelKind', dayLabelKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}dayNumber
class dayNumber (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Day number within a month."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dayNumber')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1422, 1)
    _Documentation = 'Day number within a month.'
dayNumber._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dayNumber, enum_prefix=None)
dayNumber.n1 = dayNumber._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
dayNumber.n2 = dayNumber._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
dayNumber.n3 = dayNumber._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
dayNumber.n4 = dayNumber._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
dayNumber.n5 = dayNumber._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
dayNumber.n6 = dayNumber._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
dayNumber.n7 = dayNumber._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
dayNumber.n8 = dayNumber._CF_enumeration.addEnumeration(unicode_value='8', tag='n8')
dayNumber.n9 = dayNumber._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
dayNumber.n10 = dayNumber._CF_enumeration.addEnumeration(unicode_value='10', tag='n10')
dayNumber.n11 = dayNumber._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
dayNumber.n12 = dayNumber._CF_enumeration.addEnumeration(unicode_value='12', tag='n12')
dayNumber.n13 = dayNumber._CF_enumeration.addEnumeration(unicode_value='13', tag='n13')
dayNumber.n14 = dayNumber._CF_enumeration.addEnumeration(unicode_value='14', tag='n14')
dayNumber.n15 = dayNumber._CF_enumeration.addEnumeration(unicode_value='15', tag='n15')
dayNumber.n16 = dayNumber._CF_enumeration.addEnumeration(unicode_value='16', tag='n16')
dayNumber.n17 = dayNumber._CF_enumeration.addEnumeration(unicode_value='17', tag='n17')
dayNumber.n18 = dayNumber._CF_enumeration.addEnumeration(unicode_value='18', tag='n18')
dayNumber.n19 = dayNumber._CF_enumeration.addEnumeration(unicode_value='19', tag='n19')
dayNumber.n20 = dayNumber._CF_enumeration.addEnumeration(unicode_value='20', tag='n20')
dayNumber.n21 = dayNumber._CF_enumeration.addEnumeration(unicode_value='21', tag='n21')
dayNumber.n22 = dayNumber._CF_enumeration.addEnumeration(unicode_value='22', tag='n22')
dayNumber.n23 = dayNumber._CF_enumeration.addEnumeration(unicode_value='23', tag='n23')
dayNumber.n24 = dayNumber._CF_enumeration.addEnumeration(unicode_value='24', tag='n24')
dayNumber.n25 = dayNumber._CF_enumeration.addEnumeration(unicode_value='25', tag='n25')
dayNumber.n26 = dayNumber._CF_enumeration.addEnumeration(unicode_value='26', tag='n26')
dayNumber.n27 = dayNumber._CF_enumeration.addEnumeration(unicode_value='27', tag='n27')
dayNumber.n28 = dayNumber._CF_enumeration.addEnumeration(unicode_value='28', tag='n28')
dayNumber.n29 = dayNumber._CF_enumeration.addEnumeration(unicode_value='29', tag='n29')
dayNumber.n30 = dayNumber._CF_enumeration.addEnumeration(unicode_value='30', tag='n30')
dayNumber.n31 = dayNumber._CF_enumeration.addEnumeration(unicode_value='31', tag='n31')
dayNumber._InitializeFacetMap(dayNumber._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'dayNumber', dayNumber)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}degreeUnits
class degreeUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'degreeUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1460, 1)
    _Documentation = None
degreeUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=degreeUnits, enum_prefix=None)
degreeUnits.Degrees = degreeUnits._CF_enumeration.addEnumeration(unicode_value='Degrees', tag='Degrees')
degreeUnits._InitializeFacetMap(degreeUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'degreeUnits', degreeUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}depositStatusKind
class depositStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This enumeration describes the status of the account deposit.  "Paid" implies that the customer has paid the account deposit and the utility is currently holding that deposit.  "Unpaid" implies that the deposit amount is due from the customer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'depositStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1479, 1)
    _Documentation = 'This enumeration describes the status of the account deposit.  "Paid" implies that the customer has paid the account deposit and the utility is currently holding that deposit.  "Unpaid" implies that the deposit amount is due from the customer.'
depositStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=depositStatusKind, enum_prefix=None)
depositStatusKind.Paid = depositStatusKind._CF_enumeration.addEnumeration(unicode_value='Paid', tag='Paid')
depositStatusKind.PartlyPaid = depositStatusKind._CF_enumeration.addEnumeration(unicode_value='PartlyPaid', tag='PartlyPaid')
depositStatusKind.DepositInstallation = depositStatusKind._CF_enumeration.addEnumeration(unicode_value='DepositInstallation', tag='DepositInstallation')
depositStatusKind.Unpaid = depositStatusKind._CF_enumeration.addEnumeration(unicode_value='Unpaid', tag='Unpaid')
depositStatusKind.Other = depositStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
depositStatusKind._InitializeFacetMap(depositStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'depositStatusKind', depositStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}designRoleKind
class designRoleKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'designRoleKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1510, 1)
    _Documentation = None
designRoleKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=designRoleKind, enum_prefix=None)
designRoleKind.Alternative = designRoleKind._CF_enumeration.addEnumeration(unicode_value='Alternative', tag='Alternative')
designRoleKind.Part = designRoleKind._CF_enumeration.addEnumeration(unicode_value='Part', tag='Part')
designRoleKind.Other = designRoleKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
designRoleKind._InitializeFacetMap(designRoleKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'designRoleKind', designRoleKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}deviceStatus
class deviceStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'deviceStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1529, 1)
    _Documentation = None
deviceStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=deviceStatus, enum_prefix=None)
deviceStatus.Unknown = deviceStatus._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
deviceStatus.On = deviceStatus._CF_enumeration.addEnumeration(unicode_value='On', tag='On')
deviceStatus.Off = deviceStatus._CF_enumeration.addEnumeration(unicode_value='Off', tag='Off')
deviceStatus.OutofService = deviceStatus._CF_enumeration.addEnumeration(unicode_value='OutofService', tag='OutofService')
deviceStatus.PowerLimitation = deviceStatus._CF_enumeration.addEnumeration(unicode_value='PowerLimitation', tag='PowerLimitation')
deviceStatus.Other = deviceStatus._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
deviceStatus._InitializeFacetMap(deviceStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'deviceStatus', deviceStatus)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}deviceType
class deviceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This enumeration holds the type of equipment for which the requestor is interested in receiving the allowable names using the GetElectricalEquipment method.  Acceptable values for deviceType include: Overhead (for all overhead line types whether transmission, primary or secondary), Underground (for all underground conductor types, whether transmission,  primary or secondary), ZsmConductor (for the specification of a generic self and mutual impedance, which may be used for source impedances among other uses), ZabcConductor (for the specification of a generic impedance, which may be used for source impedances among other uses), Transformer (used for all transformer banks), Regulator (used for all regulator banks), Device (used for switching banks and overcurrent device banks) and Other (for other unspecified equipment). """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'deviceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1539, 1)
    _Documentation = 'This enumeration holds the type of equipment for which the requestor is interested in receiving the allowable names using the GetElectricalEquipment method.  Acceptable values for deviceType include: Overhead (for all overhead line types whether transmission, primary or secondary), Underground (for all underground conductor types, whether transmission,  primary or secondary), ZsmConductor (for the specification of a generic self and mutual impedance, which may be used for source impedances among other uses), ZabcConductor (for the specification of a generic impedance, which may be used for source impedances among other uses), Transformer (used for all transformer banks), Regulator (used for all regulator banks), Device (used for switching banks and overcurrent device banks) and Other (for other unspecified equipment). '
deviceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=deviceType, enum_prefix=None)
deviceType.Overhead = deviceType._CF_enumeration.addEnumeration(unicode_value='Overhead', tag='Overhead')
deviceType.Underground = deviceType._CF_enumeration.addEnumeration(unicode_value='Underground', tag='Underground')
deviceType.ZsmConductor = deviceType._CF_enumeration.addEnumeration(unicode_value='ZsmConductor', tag='ZsmConductor')
deviceType.ZabcConductor = deviceType._CF_enumeration.addEnumeration(unicode_value='ZabcConductor', tag='ZabcConductor')
deviceType.Transformer = deviceType._CF_enumeration.addEnumeration(unicode_value='Transformer', tag='Transformer')
deviceType.Regulator = deviceType._CF_enumeration.addEnumeration(unicode_value='Regulator', tag='Regulator')
deviceType.Device = deviceType._CF_enumeration.addEnumeration(unicode_value='Device', tag='Device')
deviceType.Other = deviceType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
deviceType._InitializeFacetMap(deviceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'deviceType', deviceType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}districtTypeKind
class districtTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'districtTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1565, 1)
    _Documentation = None
districtTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=districtTypeKind, enum_prefix=None)
districtTypeKind.Unknown = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
districtTypeKind.Ambulance = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Ambulance', tag='Ambulance')
districtTypeKind.Board = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Board', tag='Board')
districtTypeKind.Fire = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Fire', tag='Fire')
districtTypeKind.Franchise = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Franchise', tag='Franchise')
districtTypeKind.MosquitoControl = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='MosquitoControl', tag='MosquitoControl')
districtTypeKind.Operations = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Operations', tag='Operations')
districtTypeKind.School = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='School', tag='School')
districtTypeKind.Sanitation = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Sanitation', tag='Sanitation')
districtTypeKind.Tax = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Tax', tag='Tax')
districtTypeKind.Water = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Water', tag='Water')
districtTypeKind.WaterAndSanitation = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='WaterAndSanitation', tag='WaterAndSanitation')
districtTypeKind.Other = districtTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
districtTypeKind._InitializeFacetMap(districtTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'districtTypeKind', districtTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}documentType
class documentType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This attribute establishes whether the data exchange constitutes all of the elements for all of the data instances (i.e., "dump") or incremental data (i.e., "incremental")."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'documentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1582, 1)
    _Documentation = 'This attribute establishes whether the data exchange constitutes all of the elements for all of the data instances (i.e., "dump") or incremental data (i.e., "incremental").'
documentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=documentType, enum_prefix=None)
documentType.Incremental = documentType._CF_enumeration.addEnumeration(unicode_value='Incremental', tag='Incremental')
documentType.Dump = documentType._CF_enumeration.addEnumeration(unicode_value='Dump', tag='Dump')
documentType._InitializeFacetMap(documentType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'documentType', documentType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}domainMemberAction
class domainMemberAction (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'domainMemberAction')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1591, 1)
    _Documentation = None
domainMemberAction._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=domainMemberAction, enum_prefix=None)
domainMemberAction.Created = domainMemberAction._CF_enumeration.addEnumeration(unicode_value='Created', tag='Created')
domainMemberAction.Changed = domainMemberAction._CF_enumeration.addEnumeration(unicode_value='Changed', tag='Changed')
domainMemberAction.Deleted = domainMemberAction._CF_enumeration.addEnumeration(unicode_value='Deleted', tag='Deleted')
domainMemberAction._InitializeFacetMap(domainMemberAction._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'domainMemberAction', domainMemberAction)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}domainNameAction
class domainNameAction (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'domainNameAction')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1598, 1)
    _Documentation = None
domainNameAction._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=domainNameAction, enum_prefix=None)
domainNameAction.Create = domainNameAction._CF_enumeration.addEnumeration(unicode_value='Create', tag='Create')
domainNameAction.Change = domainNameAction._CF_enumeration.addEnumeration(unicode_value='Change', tag='Change')
domainNameAction.Delete = domainNameAction._CF_enumeration.addEnumeration(unicode_value='Delete', tag='Delete')
domainNameAction._InitializeFacetMap(domainNameAction._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'domainNameAction', domainNameAction)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}driveType
class driveType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of drive on this meter (from ANSI C12.19).
0 - Piston
1 - Disc
2 - Multi-jet
3 - Turbine
4 - Compound
5 - Propeller
6 - Ultra-sonic
7 - Magnetically-coupled
8 - Differential pressure
9 - Mass
10 - Variable area
11 - Open channel
12 - Oscillatory
13 - Other"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'driveType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1605, 1)
    _Documentation = 'Type of drive on this meter (from ANSI C12.19).\n0 - Piston\n1 - Disc\n2 - Multi-jet\n3 - Turbine\n4 - Compound\n5 - Propeller\n6 - Ultra-sonic\n7 - Magnetically-coupled\n8 - Differential pressure\n9 - Mass\n10 - Variable area\n11 - Open channel\n12 - Oscillatory\n13 - Other'
driveType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=driveType, enum_prefix=None)
driveType.n0 = driveType._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
driveType.n1 = driveType._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
driveType.n2 = driveType._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
driveType.n3 = driveType._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
driveType.n4 = driveType._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
driveType.n5 = driveType._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
driveType.n6 = driveType._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
driveType.n7 = driveType._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
driveType.n8 = driveType._CF_enumeration.addEnumeration(unicode_value='8', tag='n8')
driveType.n9 = driveType._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
driveType.n10 = driveType._CF_enumeration.addEnumeration(unicode_value='10', tag='n10')
driveType.n11 = driveType._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
driveType.n12 = driveType._CF_enumeration.addEnumeration(unicode_value='12', tag='n12')
driveType.n13 = driveType._CF_enumeration.addEnumeration(unicode_value='13', tag='n13')
driveType._InitializeFacetMap(driveType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'driveType', driveType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}DRProgramEnrollmentStatusKind
class DRProgramEnrollmentStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The permissible values of DRProgramEnrollmentStatus are: 'Active', 'Inactive', 'Pending', 'Other' and 'Unknown'. Active status means that the DRProgramEnrollment has a participation start date in the past and a participation end date in the future, even if control is not currently active. A status of Inactive implies that the DRProgramEnrollment has a participation start date in the future or a participation end date in the past. A status of Pending means that the DRProgramEnrollDate is in the past, but that the DRProgramEnrollment has a participation start date in the future. The Other and Unknown statuses are included for extensibility, but their use is discouraged. If the DRProgramEnrollmentStatus is set to be Other, the DR Program Enrollment Agent should populate the OtherDRProgramEnrollmentStatus element with the non-standard status value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DRProgramEnrollmentStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1654, 1)
    _Documentation = "The permissible values of DRProgramEnrollmentStatus are: 'Active', 'Inactive', 'Pending', 'Other' and 'Unknown'. Active status means that the DRProgramEnrollment has a participation start date in the past and a participation end date in the future, even if control is not currently active. A status of Inactive implies that the DRProgramEnrollment has a participation start date in the future or a participation end date in the past. A status of Pending means that the DRProgramEnrollDate is in the past, but that the DRProgramEnrollment has a participation start date in the future. The Other and Unknown statuses are included for extensibility, but their use is discouraged. If the DRProgramEnrollmentStatus is set to be Other, the DR Program Enrollment Agent should populate the OtherDRProgramEnrollmentStatus element with the non-standard status value."
DRProgramEnrollmentStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DRProgramEnrollmentStatusKind, enum_prefix=None)
DRProgramEnrollmentStatusKind.Unknown = DRProgramEnrollmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DRProgramEnrollmentStatusKind.Active = DRProgramEnrollmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
DRProgramEnrollmentStatusKind.Inactive = DRProgramEnrollmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Inactive', tag='Inactive')
DRProgramEnrollmentStatusKind.Pending = DRProgramEnrollmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Pending', tag='Pending')
DRProgramEnrollmentStatusKind.Other = DRProgramEnrollmentStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
DRProgramEnrollmentStatusKind._InitializeFacetMap(DRProgramEnrollmentStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DRProgramEnrollmentStatusKind', DRProgramEnrollmentStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}DRProgramStatusKind
class DRProgramStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The status of this DRProgram.  Active means a program for which the end date is in the future and enrollments can be accepted (regardless of DR is currently in effect); Suspended means that a customer can be enrolled in the program, but no DR signals will be sent; Rescinded means new customers can no longer be enrolled in the program, but existing customers can continue to participate in the program until the end date of the program."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DRProgramStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1677, 1)
    _Documentation = 'The status of this DRProgram.  Active means a program for which the end date is in the future and enrollments can be accepted (regardless of DR is currently in effect); Suspended means that a customer can be enrolled in the program, but no DR signals will be sent; Rescinded means new customers can no longer be enrolled in the program, but existing customers can continue to participate in the program until the end date of the program.'
DRProgramStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DRProgramStatusKind, enum_prefix=None)
DRProgramStatusKind.Other = DRProgramStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
DRProgramStatusKind.Active = DRProgramStatusKind._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
DRProgramStatusKind.Suspended = DRProgramStatusKind._CF_enumeration.addEnumeration(unicode_value='Suspended', tag='Suspended')
DRProgramStatusKind.Rescinded = DRProgramStatusKind._CF_enumeration.addEnumeration(unicode_value='Rescinded', tag='Rescinded')
DRProgramStatusKind.Unknown = DRProgramStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DRProgramStatusKind._InitializeFacetMap(DRProgramStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DRProgramStatusKind', DRProgramStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}durationDescription
class durationDescription (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'durationDescription')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1701, 1)
    _Documentation = None
durationDescription._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=durationDescription, enum_prefix=None)
durationDescription.cycle = durationDescription._CF_enumeration.addEnumeration(unicode_value='cycle', tag='cycle')
durationDescription.second = durationDescription._CF_enumeration.addEnumeration(unicode_value='second', tag='second')
durationDescription.minute = durationDescription._CF_enumeration.addEnumeration(unicode_value='minute', tag='minute')
durationDescription.hour = durationDescription._CF_enumeration.addEnumeration(unicode_value='hour', tag='hour')
durationDescription.day = durationDescription._CF_enumeration.addEnumeration(unicode_value='day', tag='day')
durationDescription.week = durationDescription._CF_enumeration.addEnumeration(unicode_value='week', tag='week')
durationDescription.month = durationDescription._CF_enumeration.addEnumeration(unicode_value='month', tag='month')
durationDescription.year = durationDescription._CF_enumeration.addEnumeration(unicode_value='year', tag='year')
durationDescription._InitializeFacetMap(durationDescription._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'durationDescription', durationDescription)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}electricTopologyElementKind
class electricTopologyElementKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'electricTopologyElementKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1713, 1)
    _Documentation = None
electricTopologyElementKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=electricTopologyElementKind, enum_prefix=None)
electricTopologyElementKind.ACLineSegment = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='ACLineSegment', tag='ACLineSegment')
electricTopologyElementKind.capacitorBank = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='capacitorBank', tag='capacitorBank')
electricTopologyElementKind.overcurrentDeviceBank = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='overcurrentDeviceBank', tag='overcurrentDeviceBank')
electricTopologyElementKind.regulatorBank = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='regulatorBank', tag='regulatorBank')
electricTopologyElementKind.switchingDeviceBank = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='switchingDeviceBank', tag='switchingDeviceBank')
electricTopologyElementKind.transformerBank = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='transformerBank', tag='transformerBank')
electricTopologyElementKind.equivalentSource = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='equivalentSource', tag='equivalentSource')
electricTopologyElementKind.electricServicePoint = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='electricServicePoint', tag='electricServicePoint')
electricTopologyElementKind.electricMeter = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='electricMeter', tag='electricMeter')
electricTopologyElementKind.inductionMachine = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='inductionMachine', tag='inductionMachine')
electricTopologyElementKind.synchronousMachine = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='synchronousMachine', tag='synchronousMachine')
electricTopologyElementKind.streetLight = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='streetLight', tag='streetLight')
electricTopologyElementKind.securityLight = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='securityLight', tag='securityLight')
electricTopologyElementKind.trafficLight = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='trafficLight', tag='trafficLight')
electricTopologyElementKind.virtualNodeSection = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='virtualNodeSection', tag='virtualNodeSection')
electricTopologyElementKind.Other = electricTopologyElementKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
electricTopologyElementKind._InitializeFacetMap(electricTopologyElementKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'electricTopologyElementKind', electricTopologyElementKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}eMailTypeKind
class eMailTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of e-mail address."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'eMailTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1755, 1)
    _Documentation = 'Type of e-mail address.'
eMailTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=eMailTypeKind, enum_prefix=None)
eMailTypeKind.Unknown = eMailTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
eMailTypeKind.Personal = eMailTypeKind._CF_enumeration.addEnumeration(unicode_value='Personal', tag='Personal')
eMailTypeKind.Business = eMailTypeKind._CF_enumeration.addEnumeration(unicode_value='Business', tag='Business')
eMailTypeKind.Alternate = eMailTypeKind._CF_enumeration.addEnumeration(unicode_value='Alternate', tag='Alternate')
eMailTypeKind.Other = eMailTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
eMailTypeKind._InitializeFacetMap(eMailTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'eMailTypeKind', eMailTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}endDeviceStateKind
class endDeviceStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'endDeviceStateKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1767, 1)
    _Documentation = None
endDeviceStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=endDeviceStateKind, enum_prefix=None)
endDeviceStateKind.Unknown = endDeviceStateKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
endDeviceStateKind.InService = endDeviceStateKind._CF_enumeration.addEnumeration(unicode_value='InService', tag='InService')
endDeviceStateKind.OutofService = endDeviceStateKind._CF_enumeration.addEnumeration(unicode_value='OutofService', tag='OutofService')
endDeviceStateKind.Defective = endDeviceStateKind._CF_enumeration.addEnumeration(unicode_value='Defective', tag='Defective')
endDeviceStateKind.Outaged = endDeviceStateKind._CF_enumeration.addEnumeration(unicode_value='Outaged', tag='Outaged')
endDeviceStateKind.StartingUp = endDeviceStateKind._CF_enumeration.addEnumeration(unicode_value='StartingUp', tag='StartingUp')
endDeviceStateKind.ShuttingDown = endDeviceStateKind._CF_enumeration.addEnumeration(unicode_value='ShuttingDown', tag='ShuttingDown')
endDeviceStateKind.NoResponse = endDeviceStateKind._CF_enumeration.addEnumeration(unicode_value='NoResponse', tag='NoResponse')
endDeviceStateKind.Other = endDeviceStateKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
endDeviceStateKind._InitializeFacetMap(endDeviceStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'endDeviceStateKind', endDeviceStateKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}equipmentTypeKind
class equipmentTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equipmentTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1830, 1)
    _Documentation = None
equipmentTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=equipmentTypeKind, enum_prefix=None)
equipmentTypeKind.Unknown = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
equipmentTypeKind.Conductor = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Conductor', tag='Conductor')
equipmentTypeKind.ConcentricNeutralCable = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='ConcentricNeutralCable', tag='ConcentricNeutralCable')
equipmentTypeKind.TapeShieldCable = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='TapeShieldCable', tag='TapeShieldCable')
equipmentTypeKind.LineConstruction = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='LineConstruction', tag='LineConstruction')
equipmentTypeKind.SecondaryConductor = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='SecondaryConductor', tag='SecondaryConductor')
equipmentTypeKind.ServiceDrop = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='ServiceDrop', tag='ServiceDrop')
equipmentTypeKind.MaterialAttributes = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='MaterialAttributes', tag='MaterialAttributes')
equipmentTypeKind.LineEnvironmentalAttributes = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='LineEnvironmentalAttributes', tag='LineEnvironmentalAttributes')
equipmentTypeKind.ROWAttributes = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='ROWAttributes', tag='ROWAttributes')
equipmentTypeKind.Material = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Material', tag='Material')
equipmentTypeKind.Transformer = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Transformer', tag='Transformer')
equipmentTypeKind.Regulator = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Regulator', tag='Regulator')
equipmentTypeKind.Breaker = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Breaker', tag='Breaker')
equipmentTypeKind.Fuse = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Fuse', tag='Fuse')
equipmentTypeKind.Recloser = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Recloser', tag='Recloser')
equipmentTypeKind.Sectionalizer = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Sectionalizer', tag='Sectionalizer')
equipmentTypeKind.Switch = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Switch', tag='Switch')
equipmentTypeKind.LoadMix = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='LoadMix', tag='LoadMix')
equipmentTypeKind.ZsmImpedance = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='ZsmImpedance', tag='ZsmImpedance')
equipmentTypeKind.InductionMachine = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='InductionMachine', tag='InductionMachine')
equipmentTypeKind.SynchronousMachine = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='SynchronousMachine', tag='SynchronousMachine')
equipmentTypeKind.Other = equipmentTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
equipmentTypeKind._InitializeFacetMap(equipmentTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'equipmentTypeKind', equipmentTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}extType
class extType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1857, 1)
    _Documentation = None
extType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=extType, enum_prefix=None)
extType.anySimpleType = extType._CF_enumeration.addEnumeration(unicode_value='anySimpleType', tag='anySimpleType')
extType.anyType = extType._CF_enumeration.addEnumeration(unicode_value='anyType', tag='anyType')
extType.anyURI = extType._CF_enumeration.addEnumeration(unicode_value='anyURI', tag='anyURI')
extType.base64Binary = extType._CF_enumeration.addEnumeration(unicode_value='base64Binary', tag='base64Binary')
extType.boolean = extType._CF_enumeration.addEnumeration(unicode_value='boolean', tag='boolean')
extType.byte = extType._CF_enumeration.addEnumeration(unicode_value='byte', tag='byte')
extType.date = extType._CF_enumeration.addEnumeration(unicode_value='date', tag='date')
extType.dateTime = extType._CF_enumeration.addEnumeration(unicode_value='dateTime', tag='dateTime')
extType.decimal = extType._CF_enumeration.addEnumeration(unicode_value='decimal', tag='decimal')
extType.double = extType._CF_enumeration.addEnumeration(unicode_value='double', tag='double')
extType.duration = extType._CF_enumeration.addEnumeration(unicode_value='duration', tag='duration')
extType.ENTITIES = extType._CF_enumeration.addEnumeration(unicode_value='ENTITIES', tag='ENTITIES')
extType.ENTITY = extType._CF_enumeration.addEnumeration(unicode_value='ENTITY', tag='ENTITY')
extType.float = extType._CF_enumeration.addEnumeration(unicode_value='float', tag='float')
extType.gDay = extType._CF_enumeration.addEnumeration(unicode_value='gDay', tag='gDay')
extType.gMonth = extType._CF_enumeration.addEnumeration(unicode_value='gMonth', tag='gMonth')
extType.gMonthDay = extType._CF_enumeration.addEnumeration(unicode_value='gMonthDay', tag='gMonthDay')
extType.gYear = extType._CF_enumeration.addEnumeration(unicode_value='gYear', tag='gYear')
extType.gYearMonth = extType._CF_enumeration.addEnumeration(unicode_value='gYearMonth', tag='gYearMonth')
extType.hexBinary = extType._CF_enumeration.addEnumeration(unicode_value='hexBinary', tag='hexBinary')
extType.ID = extType._CF_enumeration.addEnumeration(unicode_value='ID', tag='ID')
extType.IDREF = extType._CF_enumeration.addEnumeration(unicode_value='IDREF', tag='IDREF')
extType.IDREFS = extType._CF_enumeration.addEnumeration(unicode_value='IDREFS', tag='IDREFS')
extType.int = extType._CF_enumeration.addEnumeration(unicode_value='int', tag='int')
extType.integer = extType._CF_enumeration.addEnumeration(unicode_value='integer', tag='integer')
extType.language = extType._CF_enumeration.addEnumeration(unicode_value='language', tag='language')
extType.long = extType._CF_enumeration.addEnumeration(unicode_value='long', tag='long')
extType.Name = extType._CF_enumeration.addEnumeration(unicode_value='Name', tag='Name')
extType.NCName = extType._CF_enumeration.addEnumeration(unicode_value='NCName', tag='NCName')
extType.negativeInteger = extType._CF_enumeration.addEnumeration(unicode_value='negativeInteger', tag='negativeInteger')
extType.NMTOKEN = extType._CF_enumeration.addEnumeration(unicode_value='NMTOKEN', tag='NMTOKEN')
extType.NMTOKENS = extType._CF_enumeration.addEnumeration(unicode_value='NMTOKENS', tag='NMTOKENS')
extType.nonNegativeInteger = extType._CF_enumeration.addEnumeration(unicode_value='nonNegativeInteger', tag='nonNegativeInteger')
extType.nonPositiveInteger = extType._CF_enumeration.addEnumeration(unicode_value='nonPositiveInteger', tag='nonPositiveInteger')
extType.normalizedString = extType._CF_enumeration.addEnumeration(unicode_value='normalizedString', tag='normalizedString')
extType.NOTATION = extType._CF_enumeration.addEnumeration(unicode_value='NOTATION', tag='NOTATION')
extType.positiveInteger = extType._CF_enumeration.addEnumeration(unicode_value='positiveInteger', tag='positiveInteger')
extType.QName = extType._CF_enumeration.addEnumeration(unicode_value='QName', tag='QName')
extType.short = extType._CF_enumeration.addEnumeration(unicode_value='short', tag='short')
extType.string = extType._CF_enumeration.addEnumeration(unicode_value='string', tag='string')
extType.time = extType._CF_enumeration.addEnumeration(unicode_value='time', tag='time')
extType.token = extType._CF_enumeration.addEnumeration(unicode_value='token', tag='token')
extType.unsignedByte = extType._CF_enumeration.addEnumeration(unicode_value='unsignedByte', tag='unsignedByte')
extType.unsignedInt = extType._CF_enumeration.addEnumeration(unicode_value='unsignedInt', tag='unsignedInt')
extType.unsignedLong = extType._CF_enumeration.addEnumeration(unicode_value='unsignedLong', tag='unsignedLong')
extType.unsignedShort = extType._CF_enumeration.addEnumeration(unicode_value='unsignedShort', tag='unsignedShort')
extType._InitializeFacetMap(extType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'extType', extType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}fieldNameKind
class fieldNameKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Acceptable values of the fieldName parameter used to express measured quantities or other values in a MultiSpeak formattedBlock or readingValue.readingTypeCode."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fieldNameKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1907, 1)
    _Documentation = 'Acceptable values of the fieldName parameter used to express measured quantities or other values in a MultiSpeak formattedBlock or readingValue.readingTypeCode.'
fieldNameKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fieldNameKind, enum_prefix=None)
fieldNameKind.Unknown = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
fieldNameKind.PosKWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PosKWh', tag='PosKWh')
fieldNameKind.NegKWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='NegKWh', tag='NegKWh')
fieldNameKind.PosKWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PosKWhDateTime', tag='PosKWhDateTime')
fieldNameKind.NegKWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='NegKWhDateTime', tag='NegKWhDateTime')
fieldNameKind.MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='MaxDemand', tag='MaxDemand')
fieldNameKind.MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='MaxDemandDateTime', tag='MaxDemandDateTime')
fieldNameKind.CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='CumulativeDemand', tag='CumulativeDemand')
fieldNameKind.CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='CumulativeDemandDateTime', tag='CumulativeDemandDateTime')
fieldNameKind.TOU1kWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU1kWh', tag='TOU1kWh')
fieldNameKind.TOU1kWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU1kWhDateTime', tag='TOU1kWhDateTime')
fieldNameKind.TOU1MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU1MaxDemand', tag='TOU1MaxDemand')
fieldNameKind.TOU1MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU1MaxDemandDateTime', tag='TOU1MaxDemandDateTime')
fieldNameKind.TOU1CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU1CumulativeDemand', tag='TOU1CumulativeDemand')
fieldNameKind.TOU1CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU1CumulativeDemandDateTime', tag='TOU1CumulativeDemandDateTime')
fieldNameKind.TOU2kWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU2kWh', tag='TOU2kWh')
fieldNameKind.TOU2kWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU2kWhDateTime', tag='TOU2kWhDateTime')
fieldNameKind.TOU2MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU2MaxDemand', tag='TOU2MaxDemand')
fieldNameKind.TOU2MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU2MaxDemandDateTime', tag='TOU2MaxDemandDateTime')
fieldNameKind.TOU2CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU2CumulativeDemand', tag='TOU2CumulativeDemand')
fieldNameKind.TOU2CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU2CumulativeDemandDateTime', tag='TOU2CumulativeDemandDateTime')
fieldNameKind.TOU3kWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU3kWh', tag='TOU3kWh')
fieldNameKind.TOU3kWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU3kWhDateTime', tag='TOU3kWhDateTime')
fieldNameKind.TOU3MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU3MaxDemand', tag='TOU3MaxDemand')
fieldNameKind.TOU3MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU3MaxDemandDateTime', tag='TOU3MaxDemandDateTime')
fieldNameKind.TOU3CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU3CumulativeDemand', tag='TOU3CumulativeDemand')
fieldNameKind.TOU3CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU3CumulativeDemandDateTime', tag='TOU3CumulativeDemandDateTime')
fieldNameKind.TOU4kWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU4kWh', tag='TOU4kWh')
fieldNameKind.TOU4KWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU4KWhDateTime', tag='TOU4KWhDateTime')
fieldNameKind.TOU4MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU4MaxDemand', tag='TOU4MaxDemand')
fieldNameKind.TOU4MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU4MaxDemandDateTime', tag='TOU4MaxDemandDateTime')
fieldNameKind.TOU4CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU4CumulativeDemand', tag='TOU4CumulativeDemand')
fieldNameKind.TOU4CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU4CumulativeDemandDateTime', tag='TOU4CumulativeDemandDateTime')
fieldNameKind.TOU5kWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU5kWh', tag='TOU5kWh')
fieldNameKind.TOU5kWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU5kWhDateTime', tag='TOU5kWhDateTime')
fieldNameKind.TOU5MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU5MaxDemand', tag='TOU5MaxDemand')
fieldNameKind.TOU5MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU5MaxDemandDateTime', tag='TOU5MaxDemandDateTime')
fieldNameKind.TOU5CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU5CumulativeDemand', tag='TOU5CumulativeDemand')
fieldNameKind.TOU5CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TOU5CumulativeDemandDateTime', tag='TOU5CumulativeDemandDateTime')
fieldNameKind.PreviousPosKWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousPosKWh', tag='PreviousPosKWh')
fieldNameKind.PreviousNegKWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousNegKWh', tag='PreviousNegKWh')
fieldNameKind.PreviousPosKWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousPosKWhDateTime', tag='PreviousPosKWhDateTime')
fieldNameKind.PreviousNegKWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousNegKWhDateTime', tag='PreviousNegKWhDateTime')
fieldNameKind.PreviousMaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousMaxDemand', tag='PreviousMaxDemand')
fieldNameKind.PreviousMaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousMaxDemandDateTime', tag='PreviousMaxDemandDateTime')
fieldNameKind.PreviousCumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousCumulativeDemand', tag='PreviousCumulativeDemand')
fieldNameKind.PreviousCumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousCumulativeDemandDateTime', tag='PreviousCumulativeDemandDateTime')
fieldNameKind.PreviousTOU1kWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU1kWh', tag='PreviousTOU1kWh')
fieldNameKind.PreviousTOU1KWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU1KWhDateTime', tag='PreviousTOU1KWhDateTime')
fieldNameKind.PreviousTOU1MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU1MaxDemand', tag='PreviousTOU1MaxDemand')
fieldNameKind.PreviousTOU1MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU1MaxDemandDateTime', tag='PreviousTOU1MaxDemandDateTime')
fieldNameKind.PreviousTOU1CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU1CumulativeDemand', tag='PreviousTOU1CumulativeDemand')
fieldNameKind.PreviousTOU1CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU1CumulativeDemandDateTime', tag='PreviousTOU1CumulativeDemandDateTime')
fieldNameKind.PreviousTOU2kWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU2kWh', tag='PreviousTOU2kWh')
fieldNameKind.PreviousTOU2KWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU2KWhDateTime', tag='PreviousTOU2KWhDateTime')
fieldNameKind.PreviousTOU2MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU2MaxDemand', tag='PreviousTOU2MaxDemand')
fieldNameKind.PreviousTOU2MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU2MaxDemandDateTime', tag='PreviousTOU2MaxDemandDateTime')
fieldNameKind.PreviousTOU2CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU2CumulativeDemand', tag='PreviousTOU2CumulativeDemand')
fieldNameKind.PreviousTOU2CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU2CumulativeDemandDateTime', tag='PreviousTOU2CumulativeDemandDateTime')
fieldNameKind.PreviousTOU3kWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU3kWh', tag='PreviousTOU3kWh')
fieldNameKind.PreviousTOU3KWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU3KWhDateTime', tag='PreviousTOU3KWhDateTime')
fieldNameKind.PreviousTOU3MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU3MaxDemand', tag='PreviousTOU3MaxDemand')
fieldNameKind.PreviousTOU3MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU3MaxDemandDateTime', tag='PreviousTOU3MaxDemandDateTime')
fieldNameKind.PreviousTOU3CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU3CumulativeDemand', tag='PreviousTOU3CumulativeDemand')
fieldNameKind.PreviousTOU3CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU3CumulativeDemandDateTime', tag='PreviousTOU3CumulativeDemandDateTime')
fieldNameKind.PreviousTOU4kWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU4kWh', tag='PreviousTOU4kWh')
fieldNameKind.PreviousTOU4KWhDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU4KWhDateTime', tag='PreviousTOU4KWhDateTime')
fieldNameKind.PreviousTOU4MaxDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU4MaxDemand', tag='PreviousTOU4MaxDemand')
fieldNameKind.PreviousTOU4MaxDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU4MaxDemandDateTime', tag='PreviousTOU4MaxDemandDateTime')
fieldNameKind.PreviousTOU4CumulativeDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU4CumulativeDemand', tag='PreviousTOU4CumulativeDemand')
fieldNameKind.PreviousTOU4CumulativeDemandDateTime = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousTOU4CumulativeDemandDateTime', tag='PreviousTOU4CumulativeDemandDateTime')
fieldNameKind.Voltage = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='Voltage', tag='Voltage')
fieldNameKind.MinVoltage = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='MinVoltage', tag='MinVoltage')
fieldNameKind.MaxVoltage = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='MaxVoltage', tag='MaxVoltage')
fieldNameKind.ServiceType = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='ServiceType', tag='ServiceType')
fieldNameKind.RatePeriod = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='RatePeriod', tag='RatePeriod')
fieldNameKind.MomentaryOutage = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='MomentaryOutage', tag='MomentaryOutage')
fieldNameKind.MomentaryEvent = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='MomentaryEvent', tag='MomentaryEvent')
fieldNameKind.SustainedOutage = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='SustainedOutage', tag='SustainedOutage')
fieldNameKind.LoadActionCode = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='LoadActionCode', tag='LoadActionCode')
fieldNameKind.OutageStatus = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='OutageStatus', tag='OutageStatus')
fieldNameKind.MeterNumber = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='MeterNumber', tag='MeterNumber')
fieldNameKind.SerialNumber = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='SerialNumber', tag='SerialNumber')
fieldNameKind.Manufacturer = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='Manufacturer', tag='Manufacturer')
fieldNameKind.AMIVendor = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='AMIVendor', tag='AMIVendor')
fieldNameKind.AMIDeviceType = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='AMIDeviceType', tag='AMIDeviceType')
fieldNameKind.BillingCycle = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='BillingCycle', tag='BillingCycle')
fieldNameKind.SubstationName = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='SubstationName', tag='SubstationName')
fieldNameKind.SubstationCode = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='SubstationCode', tag='SubstationCode')
fieldNameKind.Feeder = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='Feeder', tag='Feeder')
fieldNameKind.PhaseCode = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PhaseCode', tag='PhaseCode')
fieldNameKind.Frequency = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='Frequency', tag='Frequency')
fieldNameKind.SignalStrength = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='SignalStrength', tag='SignalStrength')
fieldNameKind.Tamper = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='Tamper', tag='Tamper')
fieldNameKind.Leak = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='Leak', tag='Leak')
fieldNameKind.CustomerID = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='CustomerID', tag='CustomerID')
fieldNameKind.ServiceLocationID = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='ServiceLocationID', tag='ServiceLocationID')
fieldNameKind.AccountNumber = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='AccountNumber', tag='AccountNumber')
fieldNameKind.CommunicationsAddress = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='CommunicationsAddress', tag='CommunicationsAddress')
fieldNameKind.CalcDm1 = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='CalcDm1', tag='CalcDm1')
fieldNameKind.CalcDm1T = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='CalcDm1T', tag='CalcDm1T')
fieldNameKind.CalcDm1D = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='CalcDm1D', tag='CalcDm1D')
fieldNameKind.PreviousCoincidentKVA = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousCoincidentKVA', tag='PreviousCoincidentKVA')
fieldNameKind.PreviousCoincidentKVAR = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousCoincidentKVAR', tag='PreviousCoincidentKVAR')
fieldNameKind.PFAvg = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PFAvg', tag='PFAvg')
fieldNameKind.PFCoincident1 = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PFCoincident1', tag='PFCoincident1')
fieldNameKind.PFCoincident2 = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PFCoincident2', tag='PFCoincident2')
fieldNameKind.RollingKW1 = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='RollingKW1', tag='RollingKW1')
fieldNameKind.RollingKW2 = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='RollingKW2', tag='RollingKW2')
fieldNameKind.MaxMUDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='MaxMUDemand', tag='MaxMUDemand')
fieldNameKind.MaxMUDemandDate = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='MaxMUDemandDate', tag='MaxMUDemandDate')
fieldNameKind.PreviousMaxMUDemand = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousMaxMUDemand', tag='PreviousMaxMUDemand')
fieldNameKind.PreviousMaxMUDemandDate = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PreviousMaxMUDemandDate', tag='PreviousMaxMUDemandDate')
fieldNameKind.CollectorName = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='CollectorName', tag='CollectorName')
fieldNameKind.UnscaledReading = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='UnscaledReading', tag='UnscaledReading')
fieldNameKind.kWhADRR = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='kWhADRR', tag='kWhADRR')
fieldNameKind.kWhBDRR = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='kWhBDRR', tag='kWhBDRR')
fieldNameKind.NetKWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='NetKWh', tag='NetKWh')
fieldNameKind.TotalKWh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TotalKWh', tag='TotalKWh')
fieldNameKind.PosKVAh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PosKVAh', tag='PosKVAh')
fieldNameKind.NegKVAh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='NegKVAh', tag='NegKVAh')
fieldNameKind.TotalKVAh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TotalKVAh', tag='TotalKVAh')
fieldNameKind.PosKVARh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='PosKVARh', tag='PosKVARh')
fieldNameKind.NegKVARh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='NegKVARh', tag='NegKVARh')
fieldNameKind.TotalKVARh = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='TotalKVARh', tag='TotalKVARh')
fieldNameKind.CorrectedGasVolume = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='CorrectedGasVolume', tag='CorrectedGasVolume')
fieldNameKind.UncorrectedGasVolume = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='UncorrectedGasVolume', tag='UncorrectedGasVolume')
fieldNameKind.WaterVolume = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='WaterVolume', tag='WaterVolume')
fieldNameKind.Other = fieldNameKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
fieldNameKind._InitializeFacetMap(fieldNameKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'fieldNameKind', fieldNameKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}flowDemandType
class flowDemandType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flowDemandType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2502, 1)
    _Documentation = None
flowDemandType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=flowDemandType, enum_prefix=None)
flowDemandType.Max = flowDemandType._CF_enumeration.addEnumeration(unicode_value='Max', tag='Max')
flowDemandType.Min = flowDemandType._CF_enumeration.addEnumeration(unicode_value='Min', tag='Min')
flowDemandType._InitializeFacetMap(flowDemandType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'flowDemandType', flowDemandType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}fluidType
class fluidType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of fluid measured by this meter (from ANSI C12.19).

0 - Potable water.
1 - Hot water.
2 - Non-potable water.
3 - Sewage primary water.
4 - Sewage secondary water.
5 - Sewage tertiary water
6 - Other"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fluidType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2508, 1)
    _Documentation = 'Type of fluid measured by this meter (from ANSI C12.19).\n\n0 - Potable water.\n1 - Hot water.\n2 - Non-potable water.\n3 - Sewage primary water.\n4 - Sewage secondary water.\n5 - Sewage tertiary water\n6 - Other'
fluidType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fluidType, enum_prefix=None)
fluidType.n0 = fluidType._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
fluidType.n1 = fluidType._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
fluidType.n2 = fluidType._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
fluidType.n3 = fluidType._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
fluidType.n4 = fluidType._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
fluidType.n5 = fluidType._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
fluidType.n6 = fluidType._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
fluidType._InitializeFacetMap(fluidType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'fluidType', fluidType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}frequencyUnits
class frequencyUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'frequencyUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2530, 1)
    _Documentation = None
frequencyUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=frequencyUnits, enum_prefix=None)
frequencyUnits.Unknown = frequencyUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
frequencyUnits.Hz = frequencyUnits._CF_enumeration.addEnumeration(unicode_value='Hz', tag='Hz')
frequencyUnits.CyclesPerSecond = frequencyUnits._CF_enumeration.addEnumeration(unicode_value='CyclesPerSecond', tag='CyclesPerSecond')
frequencyUnits.Other = frequencyUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
frequencyUnits._InitializeFacetMap(frequencyUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'frequencyUnits', frequencyUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}gearDriveSize
class gearDriveSize (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Gear drive size code from ANSI C12.19:
          English        Metric
0 -   None             None
1 -  1/2 cu ft        .01 or .015 cu m
2 - 1.0 cu ft        .02 cu m
3 - 2 cu ft           .05 cu m
4 - 5 cu ft           0.1 cu m
5 - 10 cu ft         0.2 cu m
6 - 100 cu ft       1.0 cu m
7 - 1000 cu ft     10 cu m"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gearDriveSize')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2538, 1)
    _Documentation = 'Gear drive size code from ANSI C12.19:\n          English        Metric\n0 -   None             None\n1 -  1/2 cu ft        .01 or .015 cu m\n2 - 1.0 cu ft        .02 cu m\n3 - 2 cu ft           .05 cu m\n4 - 5 cu ft           0.1 cu m\n5 - 10 cu ft         0.2 cu m\n6 - 100 cu ft       1.0 cu m\n7 - 1000 cu ft     10 cu m'
gearDriveSize._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=gearDriveSize, enum_prefix=None)
gearDriveSize.n0 = gearDriveSize._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
gearDriveSize.n1 = gearDriveSize._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
gearDriveSize.n2 = gearDriveSize._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
gearDriveSize.n3 = gearDriveSize._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
gearDriveSize.n4 = gearDriveSize._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
gearDriveSize.n5 = gearDriveSize._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
gearDriveSize.n6 = gearDriveSize._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
gearDriveSize.n7 = gearDriveSize._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
gearDriveSize._InitializeFacetMap(gearDriveSize._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'gearDriveSize', gearDriveSize)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}guyAgainst
class guyAgainst (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'guyAgainst')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2562, 1)
    _Documentation = None
guyAgainst._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=guyAgainst, enum_prefix=None)
guyAgainst.Unknown = guyAgainst._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
guyAgainst.DeadEnd = guyAgainst._CF_enumeration.addEnumeration(unicode_value='DeadEnd', tag='DeadEnd')
guyAgainst.Angle = guyAgainst._CF_enumeration.addEnumeration(unicode_value='Angle', tag='Angle')
guyAgainst.StormRight = guyAgainst._CF_enumeration.addEnumeration(unicode_value='StormRight', tag='StormRight')
guyAgainst.StormLeft = guyAgainst._CF_enumeration.addEnumeration(unicode_value='StormLeft', tag='StormLeft')
guyAgainst.Other = guyAgainst._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
guyAgainst._InitializeFacetMap(guyAgainst._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'guyAgainst', guyAgainst)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}guyType
class guyType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of structure guy."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'guyType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2588, 1)
    _Documentation = 'Type of structure guy.'
guyType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=guyType, enum_prefix=None)
guyType.Unknown = guyType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
guyType.Down = guyType._CF_enumeration.addEnumeration(unicode_value='Down', tag='Down')
guyType.DoubleDown = guyType._CF_enumeration.addEnumeration(unicode_value='DoubleDown', tag='DoubleDown')
guyType.Other = guyType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
guyType._InitializeFacetMap(guyType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'guyType', guyType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}guyWireKind
class guyWireKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This is the type of guy wire."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'guyWireKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2599, 1)
    _Documentation = 'This is the type of guy wire.'
guyWireKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=guyWireKind, enum_prefix=None)
guyWireKind.Unknown = guyWireKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
guyWireKind.CommonGrade = guyWireKind._CF_enumeration.addEnumeration(unicode_value='CommonGrade', tag='CommonGrade')
guyWireKind.SiemensMartin = guyWireKind._CF_enumeration.addEnumeration(unicode_value='SiemensMartin', tag='SiemensMartin')
guyWireKind.HighStrength = guyWireKind._CF_enumeration.addEnumeration(unicode_value='HighStrength', tag='HighStrength')
guyWireKind.ExtraHighStrength = guyWireKind._CF_enumeration.addEnumeration(unicode_value='ExtraHighStrength', tag='ExtraHighStrength')
guyWireKind.UtilitiesGrade = guyWireKind._CF_enumeration.addEnumeration(unicode_value='UtilitiesGrade', tag='UtilitiesGrade')
guyWireKind.Other = guyWireKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
guyWireKind._InitializeFacetMap(guyWireKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'guyWireKind', guyWireKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}guyWireSizeUnitKind
class guyWireSizeUnitKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The units for measuring guy wire diameter."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'guyWireSizeUnitKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2613, 1)
    _Documentation = 'The units for measuring guy wire diameter.'
guyWireSizeUnitKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=guyWireSizeUnitKind, enum_prefix=None)
guyWireSizeUnitKind.Unknown = guyWireSizeUnitKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
guyWireSizeUnitKind.Inches = guyWireSizeUnitKind._CF_enumeration.addEnumeration(unicode_value='Inches', tag='Inches')
guyWireSizeUnitKind.Millimeters = guyWireSizeUnitKind._CF_enumeration.addEnumeration(unicode_value='Millimeters', tag='Millimeters')
guyWireSizeUnitKind.Other = guyWireSizeUnitKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
guyWireSizeUnitKind._InitializeFacetMap(guyWireSizeUnitKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'guyWireSizeUnitKind', guyWireSizeUnitKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}historyEventTypeKind
class historyEventTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'historyEventTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2668, 1)
    _Documentation = None
historyEventTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=historyEventTypeKind, enum_prefix=None)
historyEventTypeKind.Unknown = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
historyEventTypeKind.Created = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Created', tag='Created')
historyEventTypeKind.Modified = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Modified', tag='Modified')
historyEventTypeKind.IssuedToMobile = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='IssuedToMobile', tag='IssuedToMobile')
historyEventTypeKind.CheckedOut = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='CheckedOut', tag='CheckedOut')
historyEventTypeKind.CheckedIn = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='CheckedIn', tag='CheckedIn')
historyEventTypeKind.StatusChanged = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='StatusChanged', tag='StatusChanged')
historyEventTypeKind.Acknowledged = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Acknowledged', tag='Acknowledged')
historyEventTypeKind.Copied = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Copied', tag='Copied')
historyEventTypeKind.Deleted = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Deleted', tag='Deleted')
historyEventTypeKind.DesignReviewed = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='DesignReviewed', tag='DesignReviewed')
historyEventTypeKind.Released = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Released', tag='Released')
historyEventTypeKind.Closed = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Closed', tag='Closed')
historyEventTypeKind.Inspected = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Inspected', tag='Inspected')
historyEventTypeKind.Other = historyEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
historyEventTypeKind._InitializeFacetMap(historyEventTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'historyEventTypeKind', historyEventTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}ignitionStateKind
class ignitionStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """State of the ignition switch in the vehicle."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ignitionStateKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2698, 1)
    _Documentation = 'State of the ignition switch in the vehicle.'
ignitionStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ignitionStateKind, enum_prefix=None)
ignitionStateKind.Unknown = ignitionStateKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ignitionStateKind.On = ignitionStateKind._CF_enumeration.addEnumeration(unicode_value='On', tag='On')
ignitionStateKind.Off = ignitionStateKind._CF_enumeration.addEnumeration(unicode_value='Off', tag='Off')
ignitionStateKind.Other = ignitionStateKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
ignitionStateKind._InitializeFacetMap(ignitionStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ignitionStateKind', ignitionStateKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}incidentPriorityKind
class incidentPriorityKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentPriorityKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2709, 1)
    _Documentation = None
incidentPriorityKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=incidentPriorityKind, enum_prefix=None)
incidentPriorityKind.Unknown = incidentPriorityKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
incidentPriorityKind.OutagePriority = incidentPriorityKind._CF_enumeration.addEnumeration(unicode_value='OutagePriority', tag='OutagePriority')
incidentPriorityKind.PriorityCustomer = incidentPriorityKind._CF_enumeration.addEnumeration(unicode_value='PriorityCustomer', tag='PriorityCustomer')
incidentPriorityKind.EmergencyServices = incidentPriorityKind._CF_enumeration.addEnumeration(unicode_value='EmergencyServices', tag='EmergencyServices')
incidentPriorityKind.MedicalNecessity = incidentPriorityKind._CF_enumeration.addEnumeration(unicode_value='MedicalNecessity', tag='MedicalNecessity')
incidentPriorityKind.Low = incidentPriorityKind._CF_enumeration.addEnumeration(unicode_value='Low', tag='Low')
incidentPriorityKind.Other = incidentPriorityKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
incidentPriorityKind._InitializeFacetMap(incidentPriorityKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'incidentPriorityKind', incidentPriorityKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}incidentReporterKind
class incidentReporterKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentReporterKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2731, 1)
    _Documentation = None
incidentReporterKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=incidentReporterKind, enum_prefix=None)
incidentReporterKind.Unknown = incidentReporterKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
incidentReporterKind.Consumer = incidentReporterKind._CF_enumeration.addEnumeration(unicode_value='Consumer', tag='Consumer')
incidentReporterKind.Witness = incidentReporterKind._CF_enumeration.addEnumeration(unicode_value='Witness', tag='Witness')
incidentReporterKind.Worker = incidentReporterKind._CF_enumeration.addEnumeration(unicode_value='Worker', tag='Worker')
incidentReporterKind.EmergencyServices = incidentReporterKind._CF_enumeration.addEnumeration(unicode_value='EmergencyServices', tag='EmergencyServices')
incidentReporterKind.Other = incidentReporterKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
incidentReporterKind._InitializeFacetMap(incidentReporterKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'incidentReporterKind', incidentReporterKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}incidentReportSourceKind
class incidentReportSourceKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The source of the reported outage incident."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentReportSourceKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2779, 1)
    _Documentation = 'The source of the reported outage incident.'
incidentReportSourceKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=incidentReportSourceKind, enum_prefix=None)
incidentReportSourceKind.Unknown = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
incidentReportSourceKind.CallToIVR = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='CallToIVR', tag='CallToIVR')
incidentReportSourceKind.CallToCSR = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='CallToCSR', tag='CallToCSR')
incidentReportSourceKind.CallToDispatcher = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='CallToDispatcher', tag='CallToDispatcher')
incidentReportSourceKind.SMS = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='SMS', tag='SMS')
incidentReportSourceKind.EMail = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='EMail', tag='EMail')
incidentReportSourceKind.MobileApp = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='MobileApp', tag='MobileApp')
incidentReportSourceKind.WebPortal = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='WebPortal', tag='WebPortal')
incidentReportSourceKind.CallBackResult = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='CallBackResult', tag='CallBackResult')
incidentReportSourceKind.Other = incidentReportSourceKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
incidentReportSourceKind._InitializeFacetMap(incidentReportSourceKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'incidentReportSourceKind', incidentReportSourceKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}incidentReportStatusKind
class incidentReportStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentReportStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2839, 1)
    _Documentation = None
incidentReportStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=incidentReportStatusKind, enum_prefix=None)
incidentReportStatusKind.Unknown = incidentReportStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
incidentReportStatusKind.InQueue = incidentReportStatusKind._CF_enumeration.addEnumeration(unicode_value='InQueue', tag='InQueue')
incidentReportStatusKind.Active = incidentReportStatusKind._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
incidentReportStatusKind.Closed = incidentReportStatusKind._CF_enumeration.addEnumeration(unicode_value='Closed', tag='Closed')
incidentReportStatusKind.Other = incidentReportStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
incidentReportStatusKind._InitializeFacetMap(incidentReportStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'incidentReportStatusKind', incidentReportStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}incidentResultKind
class incidentResultKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentResultKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2860, 1)
    _Documentation = None
incidentResultKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=incidentResultKind, enum_prefix=None)
incidentResultKind.Unknown = incidentResultKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
incidentResultKind.FunctioningCorrectly = incidentResultKind._CF_enumeration.addEnumeration(unicode_value='FunctioningCorrectly', tag='FunctioningCorrectly')
incidentResultKind.DisconnectedForCause = incidentResultKind._CF_enumeration.addEnumeration(unicode_value='DisconnectedForCause', tag='DisconnectedForCause')
incidentResultKind.OutageCreated = incidentResultKind._CF_enumeration.addEnumeration(unicode_value='OutageCreated', tag='OutageCreated')
incidentResultKind.ExistingOutage = incidentResultKind._CF_enumeration.addEnumeration(unicode_value='ExistingOutage', tag='ExistingOutage')
incidentResultKind.Other = incidentResultKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
incidentResultKind._InitializeFacetMap(incidentResultKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'incidentResultKind', incidentResultKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}includeAssemblyDataKind
class includeAssemblyDataKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'includeAssemblyDataKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2892, 1)
    _Documentation = None
includeAssemblyDataKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=includeAssemblyDataKind, enum_prefix=None)
includeAssemblyDataKind.Assemblies = includeAssemblyDataKind._CF_enumeration.addEnumeration(unicode_value='Assemblies', tag='Assemblies')
includeAssemblyDataKind.AssemblyDetails = includeAssemblyDataKind._CF_enumeration.addEnumeration(unicode_value='AssemblyDetails', tag='AssemblyDetails')
includeAssemblyDataKind.None_ = includeAssemblyDataKind._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
includeAssemblyDataKind.Other = includeAssemblyDataKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
includeAssemblyDataKind._InitializeFacetMap(includeAssemblyDataKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'includeAssemblyDataKind', includeAssemblyDataKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}installType
class installType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Location that meter is installed (from ANSI C12.19).

0- Outdoor - non-pit.
1- Outdoor - pit.
2- Indoor - non-pit
3- Other"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'installType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2900, 1)
    _Documentation = 'Location that meter is installed (from ANSI C12.19).\n\n0- Outdoor - non-pit.\n1- Outdoor - pit.\n2- Indoor - non-pit\n3- Other'
installType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=installType, enum_prefix=None)
installType.n0 = installType._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
installType.n1 = installType._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
installType.n2 = installType._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
installType.n3 = installType._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
installType._InitializeFacetMap(installType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'installType', installType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}internalPipeDiameter
class internalPipeDiameter (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Pipe size (from ANSI C12.19).
      English           Metric
0 - None             None
1 - 1/2"                 13 mm
2 - 5/8"                15 mm
3 - 3/4"                20 mm
4 - 1"                   25 mm
5 - 1 1/2"             40 mm
6 - 2"                   50 mm
7 - 4"                 100 mm
8 - 6"                 160 mm
9 - 8"                 200 mm
10 - 10"             250 mm
11 - 12"             300 mm
12 - 14"             350 mm
13 - 16"             400 mm
14 - 18"             450 mm
15 - 20"             500 mm
16 - 22"             Not standard 
17 - 24"             600 mm
18 - 26"             Not standard
19 - 28"             Not standard
20 - 30"             Not standard
21 - 32"             800 mm
22 - 34"             Not Standard
23 - 36"             900 mm"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'internalPipeDiameter')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2916, 1)
    _Documentation = 'Pipe size (from ANSI C12.19).\n      English           Metric\n0 - None             None\n1 - 1/2"                 13 mm\n2 - 5/8"                15 mm\n3 - 3/4"                20 mm\n4 - 1"                   25 mm\n5 - 1 1/2"             40 mm\n6 - 2"                   50 mm\n7 - 4"                 100 mm\n8 - 6"                 160 mm\n9 - 8"                 200 mm\n10 - 10"             250 mm\n11 - 12"             300 mm\n12 - 14"             350 mm\n13 - 16"             400 mm\n14 - 18"             450 mm\n15 - 20"             500 mm\n16 - 22"             Not standard \n17 - 24"             600 mm\n18 - 26"             Not standard\n19 - 28"             Not standard\n20 - 30"             Not standard\n21 - 32"             800 mm\n22 - 34"             Not Standard\n23 - 36"             900 mm'
internalPipeDiameter._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=internalPipeDiameter, enum_prefix=None)
internalPipeDiameter.n0 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
internalPipeDiameter.n1 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
internalPipeDiameter.n2 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
internalPipeDiameter.n3 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
internalPipeDiameter.n4 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
internalPipeDiameter.n5 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
internalPipeDiameter.n6 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
internalPipeDiameter.n7 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
internalPipeDiameter.n8 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='8', tag='n8')
internalPipeDiameter.n9 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
internalPipeDiameter.n10 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='10', tag='n10')
internalPipeDiameter.n11 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
internalPipeDiameter.n12 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='12', tag='n12')
internalPipeDiameter.n13 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='13', tag='n13')
internalPipeDiameter.n14 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='14', tag='n14')
internalPipeDiameter.n15 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='15', tag='n15')
internalPipeDiameter.n16 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='16', tag='n16')
internalPipeDiameter.n17 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='17', tag='n17')
internalPipeDiameter.n18 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='18', tag='n18')
internalPipeDiameter.n19 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='19', tag='n19')
internalPipeDiameter.n20 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='20', tag='n20')
internalPipeDiameter.n21 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='21', tag='n21')
internalPipeDiameter.n22 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='22', tag='n22')
internalPipeDiameter.n23 = internalPipeDiameter._CF_enumeration.addEnumeration(unicode_value='23', tag='n23')
internalPipeDiameter._InitializeFacetMap(internalPipeDiameter._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'internalPipeDiameter', internalPipeDiameter)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}lengthUnits
class lengthUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lengthUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2972, 1)
    _Documentation = None
lengthUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lengthUnits, enum_prefix=None)
lengthUnits.Unknown = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
lengthUnits.Mils = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Mils', tag='Mils')
lengthUnits.Inches = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Inches', tag='Inches')
lengthUnits.Feet = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Feet', tag='Feet')
lengthUnits.Yards = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Yards', tag='Yards')
lengthUnits.ThousandFeet = lengthUnits._CF_enumeration.addEnumeration(unicode_value='ThousandFeet', tag='ThousandFeet')
lengthUnits.Miles = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Miles', tag='Miles')
lengthUnits.Micrometers = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Micrometers', tag='Micrometers')
lengthUnits.Millimeters = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Millimeters', tag='Millimeters')
lengthUnits.Decimeters = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Decimeters', tag='Decimeters')
lengthUnits.Centimeters = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Centimeters', tag='Centimeters')
lengthUnits.Meters = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Meters', tag='Meters')
lengthUnits.HundredMeters = lengthUnits._CF_enumeration.addEnumeration(unicode_value='HundredMeters', tag='HundredMeters')
lengthUnits.Kilometers = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Kilometers', tag='Kilometers')
lengthUnits.Other = lengthUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
lengthUnits._InitializeFacetMap(lengthUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'lengthUnits', lengthUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}limitType
class limitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This enumeration along with a rated current or rated voltage indicates a limit of the effectiveness of a tariff. For instance for a tariff that is effective for three-phase service at 120/208V, the serviceVoltage would include 208V, and serviceLimitType would be "EQ"; phases would be "3". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'limitType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2991, 1)
    _Documentation = 'This enumeration along with a rated current or rated voltage indicates a limit of the effectiveness of a tariff. For instance for a tariff that is effective for three-phase service at 120/208V, the serviceVoltage would include 208V, and serviceLimitType would be "EQ"; phases would be "3". '
limitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=limitType, enum_prefix=None)
limitType.EQ = limitType._CF_enumeration.addEnumeration(unicode_value='EQ', tag='EQ')
limitType.GT = limitType._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
limitType.GTOrEq = limitType._CF_enumeration.addEnumeration(unicode_value='GTOrEq', tag='GTOrEq')
limitType.LT = limitType._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
limitType.LTOrEQ = limitType._CF_enumeration.addEnumeration(unicode_value='LTOrEQ', tag='LTOrEQ')
limitType._InitializeFacetMap(limitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'limitType', limitType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}lineConstructionEntryKind
class lineConstructionEntryKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The type of line construction entry.  Overhead=Overhead primary line contruction entry, ConcentriNeutral=Concentric neutral cable entry, TapeShield=Tape shield cable entry, Secondary=Secondary conductor entry, ServiceDrop= Service drop entry, Other, Unknown."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lineConstructionEntryKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3023, 1)
    _Documentation = 'The type of line construction entry.  Overhead=Overhead primary line contruction entry, ConcentriNeutral=Concentric neutral cable entry, TapeShield=Tape shield cable entry, Secondary=Secondary conductor entry, ServiceDrop= Service drop entry, Other, Unknown.'
lineConstructionEntryKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lineConstructionEntryKind, enum_prefix=None)
lineConstructionEntryKind.Unknown = lineConstructionEntryKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
lineConstructionEntryKind.Overhead = lineConstructionEntryKind._CF_enumeration.addEnumeration(unicode_value='Overhead', tag='Overhead')
lineConstructionEntryKind.ConcentricNeutral = lineConstructionEntryKind._CF_enumeration.addEnumeration(unicode_value='ConcentricNeutral', tag='ConcentricNeutral')
lineConstructionEntryKind.TapeShield = lineConstructionEntryKind._CF_enumeration.addEnumeration(unicode_value='TapeShield', tag='TapeShield')
lineConstructionEntryKind.Secondary = lineConstructionEntryKind._CF_enumeration.addEnumeration(unicode_value='Secondary', tag='Secondary')
lineConstructionEntryKind.ServiceDrop = lineConstructionEntryKind._CF_enumeration.addEnumeration(unicode_value='ServiceDrop', tag='ServiceDrop')
lineConstructionEntryKind.Other = lineConstructionEntryKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
lineConstructionEntryKind._InitializeFacetMap(lineConstructionEntryKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'lineConstructionEntryKind', lineConstructionEntryKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}lineDischargeClass
class lineDischargeClass (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lineDischargeClass')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3048, 1)
    _Documentation = None
lineDischargeClass._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lineDischargeClass, enum_prefix=None)
lineDischargeClass.n1 = lineDischargeClass._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
lineDischargeClass.n2 = lineDischargeClass._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
lineDischargeClass.n3 = lineDischargeClass._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
lineDischargeClass.n4 = lineDischargeClass._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
lineDischargeClass.n5 = lineDischargeClass._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
lineDischargeClass._InitializeFacetMap(lineDischargeClass._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'lineDischargeClass', lineDischargeClass)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}lineRoleKind
class lineRoleKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lineRoleKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3068, 1)
    _Documentation = None
lineRoleKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lineRoleKind, enum_prefix=None)
lineRoleKind.Unknown = lineRoleKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
lineRoleKind.Transmission = lineRoleKind._CF_enumeration.addEnumeration(unicode_value='Transmission', tag='Transmission')
lineRoleKind.Distribution = lineRoleKind._CF_enumeration.addEnumeration(unicode_value='Distribution', tag='Distribution')
lineRoleKind.Secondary = lineRoleKind._CF_enumeration.addEnumeration(unicode_value='Secondary', tag='Secondary')
lineRoleKind.Service = lineRoleKind._CF_enumeration.addEnumeration(unicode_value='Service', tag='Service')
lineRoleKind.Other = lineRoleKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
lineRoleKind._InitializeFacetMap(lineRoleKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'lineRoleKind', lineRoleKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}loadActionCodeKind
class loadActionCodeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This enumeration has codes for actions to be taken at this customer connect/disconnect device."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'loadActionCodeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3089, 1)
    _Documentation = 'This enumeration has codes for actions to be taken at this customer connect/disconnect device.'
loadActionCodeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=loadActionCodeKind, enum_prefix=None)
loadActionCodeKind.Unknown = loadActionCodeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
loadActionCodeKind.Connect = loadActionCodeKind._CF_enumeration.addEnumeration(unicode_value='Connect', tag='Connect')
loadActionCodeKind.Disconnect = loadActionCodeKind._CF_enumeration.addEnumeration(unicode_value='Disconnect', tag='Disconnect')
loadActionCodeKind.InitiatePowerLimitation = loadActionCodeKind._CF_enumeration.addEnumeration(unicode_value='InitiatePowerLimitation', tag='InitiatePowerLimitation')
loadActionCodeKind.CancelPowerLimitation = loadActionCodeKind._CF_enumeration.addEnumeration(unicode_value='CancelPowerLimitation', tag='CancelPowerLimitation')
loadActionCodeKind.Arm = loadActionCodeKind._CF_enumeration.addEnumeration(unicode_value='Arm', tag='Arm')
loadActionCodeKind.Enable = loadActionCodeKind._CF_enumeration.addEnumeration(unicode_value='Enable', tag='Enable')
loadActionCodeKind.Disable = loadActionCodeKind._CF_enumeration.addEnumeration(unicode_value='Disable', tag='Disable')
loadActionCodeKind.Other = loadActionCodeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
loadActionCodeKind._InitializeFacetMap(loadActionCodeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'loadActionCodeKind', loadActionCodeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}loadConnection
class loadConnection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Load connection for this rotating machine. 
(W for wye; D for delta)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'loadConnection')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3113, 1)
    _Documentation = 'Load connection for this rotating machine. \n(W for wye; D for delta).'
loadConnection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=loadConnection, enum_prefix=None)
loadConnection.Wye = loadConnection._CF_enumeration.addEnumeration(unicode_value='Wye', tag='Wye')
loadConnection.Delta = loadConnection._CF_enumeration.addEnumeration(unicode_value='Delta', tag='Delta')
loadConnection._InitializeFacetMap(loadConnection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'loadConnection', loadConnection)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}loadDistribution
class loadDistribution (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'loadDistribution')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3123, 1)
    _Documentation = None
loadDistribution._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=loadDistribution, enum_prefix=None)
loadDistribution.Uniform = loadDistribution._CF_enumeration.addEnumeration(unicode_value='Uniform', tag='Uniform')
loadDistribution.LoadEnd = loadDistribution._CF_enumeration.addEnumeration(unicode_value='LoadEnd', tag='LoadEnd')
loadDistribution.SourceEnd = loadDistribution._CF_enumeration.addEnumeration(unicode_value='SourceEnd', tag='SourceEnd')
loadDistribution._InitializeFacetMap(loadDistribution._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'loadDistribution', loadDistribution)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}loadingDistrictKind
class loadingDistrictKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Design loading district."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'loadingDistrictKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3141, 1)
    _Documentation = 'Design loading district.'
loadingDistrictKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=loadingDistrictKind, enum_prefix=None)
loadingDistrictKind.Unknown = loadingDistrictKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
loadingDistrictKind.Light = loadingDistrictKind._CF_enumeration.addEnumeration(unicode_value='Light', tag='Light')
loadingDistrictKind.Medium = loadingDistrictKind._CF_enumeration.addEnumeration(unicode_value='Medium', tag='Medium')
loadingDistrictKind.Heavy = loadingDistrictKind._CF_enumeration.addEnumeration(unicode_value='Heavy', tag='Heavy')
loadingDistrictKind.Other = loadingDistrictKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
loadingDistrictKind._InitializeFacetMap(loadingDistrictKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'loadingDistrictKind', loadingDistrictKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}loadInterruptibleType
class loadInterruptibleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'loadInterruptibleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3153, 1)
    _Documentation = None
loadInterruptibleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=loadInterruptibleType, enum_prefix=None)
loadInterruptibleType.General = loadInterruptibleType._CF_enumeration.addEnumeration(unicode_value='General', tag='General')
loadInterruptibleType.Interruptible = loadInterruptibleType._CF_enumeration.addEnumeration(unicode_value='Interruptible', tag='Interruptible')
loadInterruptibleType.Noninterruptible = loadInterruptibleType._CF_enumeration.addEnumeration(unicode_value='Noninterruptible', tag='Noninterruptible')
loadInterruptibleType._InitializeFacetMap(loadInterruptibleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'loadInterruptibleType', loadInterruptibleType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}loadMixConnection
class loadMixConnection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Connection for this load mix."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'loadMixConnection')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3160, 1)
    _Documentation = 'Connection for this load mix.'
loadMixConnection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=loadMixConnection, enum_prefix=None)
loadMixConnection.Unknown = loadMixConnection._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
loadMixConnection.Wye = loadMixConnection._CF_enumeration.addEnumeration(unicode_value='Wye', tag='Wye')
loadMixConnection.Delta = loadMixConnection._CF_enumeration.addEnumeration(unicode_value='Delta', tag='Delta')
loadMixConnection.Center_tap = loadMixConnection._CF_enumeration.addEnumeration(unicode_value='Center tap', tag='Center_tap')
loadMixConnection._InitializeFacetMap(loadMixConnection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'loadMixConnection', loadMixConnection)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}locationHazardKind
class locationHazardKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationHazardKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3171, 1)
    _Documentation = None
locationHazardKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=locationHazardKind, enum_prefix=None)
locationHazardKind.Access = locationHazardKind._CF_enumeration.addEnumeration(unicode_value='Access', tag='Access')
locationHazardKind.Animal = locationHazardKind._CF_enumeration.addEnumeration(unicode_value='Animal', tag='Animal')
locationHazardKind.Customer = locationHazardKind._CF_enumeration.addEnumeration(unicode_value='Customer', tag='Customer')
locationHazardKind.Safety = locationHazardKind._CF_enumeration.addEnumeration(unicode_value='Safety', tag='Safety')
locationHazardKind.Other = locationHazardKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
locationHazardKind._InitializeFacetMap(locationHazardKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'locationHazardKind', locationHazardKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}locationOutageStatusKind
class locationOutageStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Outage status of this location."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationOutageStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3205, 1)
    _Documentation = 'Outage status of this location.'
locationOutageStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=locationOutageStatusKind, enum_prefix=None)
locationOutageStatusKind.Unknown = locationOutageStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
locationOutageStatusKind.Assumed = locationOutageStatusKind._CF_enumeration.addEnumeration(unicode_value='Assumed', tag='Assumed')
locationOutageStatusKind.Confirmed = locationOutageStatusKind._CF_enumeration.addEnumeration(unicode_value='Confirmed', tag='Confirmed')
locationOutageStatusKind.Restored = locationOutageStatusKind._CF_enumeration.addEnumeration(unicode_value='Restored', tag='Restored')
locationOutageStatusKind.Scheduled = locationOutageStatusKind._CF_enumeration.addEnumeration(unicode_value='Scheduled', tag='Scheduled')
locationOutageStatusKind.StillOut = locationOutageStatusKind._CF_enumeration.addEnumeration(unicode_value='StillOut', tag='StillOut')
locationOutageStatusKind.NonPay = locationOutageStatusKind._CF_enumeration.addEnumeration(unicode_value='NonPay', tag='NonPay')
locationOutageStatusKind.NoOutage = locationOutageStatusKind._CF_enumeration.addEnumeration(unicode_value='NoOutage', tag='NoOutage')
locationOutageStatusKind.Other = locationOutageStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
locationOutageStatusKind._InitializeFacetMap(locationOutageStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'locationOutageStatusKind', locationOutageStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}locationPriorityKind
class locationPriorityKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This is a class of special priorities for a customer,  serviceLocation or usagePoint."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationPriorityKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3221, 1)
    _Documentation = 'This is a class of special priorities for a customer,  serviceLocation or usagePoint.'
locationPriorityKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=locationPriorityKind, enum_prefix=None)
locationPriorityKind.Unknown = locationPriorityKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
locationPriorityKind.EmergencyServices = locationPriorityKind._CF_enumeration.addEnumeration(unicode_value='EmergencyServices', tag='EmergencyServices')
locationPriorityKind.MedicalNecessity = locationPriorityKind._CF_enumeration.addEnumeration(unicode_value='MedicalNecessity', tag='MedicalNecessity')
locationPriorityKind.OutagePriority = locationPriorityKind._CF_enumeration.addEnumeration(unicode_value='OutagePriority', tag='OutagePriority')
locationPriorityKind.PriorityCustomer = locationPriorityKind._CF_enumeration.addEnumeration(unicode_value='PriorityCustomer', tag='PriorityCustomer')
locationPriorityKind.Other = locationPriorityKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
locationPriorityKind._InitializeFacetMap(locationPriorityKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'locationPriorityKind', locationPriorityKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}LTTriggerEventKind
class LTTriggerEventKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The is the event that triggered the collection of location tracking (AVL) data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LTTriggerEventKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3262, 1)
    _Documentation = 'The is the event that triggered the collection of location tracking (AVL) data.'
LTTriggerEventKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LTTriggerEventKind, enum_prefix=None)
LTTriggerEventKind.Unknown = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
LTTriggerEventKind.PowerOn = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='PowerOn', tag='PowerOn')
LTTriggerEventKind.PowerOff = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='PowerOff', tag='PowerOff')
LTTriggerEventKind.Moving = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='Moving', tag='Moving')
LTTriggerEventKind.Stop = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='Stop', tag='Stop')
LTTriggerEventKind.PTOOn = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='PTOOn', tag='PTOOn')
LTTriggerEventKind.PTOOff = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='PTOOff', tag='PTOOff')
LTTriggerEventKind.Alert = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='Alert', tag='Alert')
LTTriggerEventKind.TroubleLight = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='TroubleLight', tag='TroubleLight')
LTTriggerEventKind.Diagnostic = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='Diagnostic', tag='Diagnostic')
LTTriggerEventKind.Other = LTTriggerEventKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
LTTriggerEventKind._InitializeFacetMap(LTTriggerEventKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LTTriggerEventKind', LTTriggerEventKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}machineType
class machineType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'machineType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3280, 1)
    _Documentation = None
machineType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=machineType, enum_prefix=None)
machineType.Motor = machineType._CF_enumeration.addEnumeration(unicode_value='Motor', tag='Motor')
machineType.Generator = machineType._CF_enumeration.addEnumeration(unicode_value='Generator', tag='Generator')
machineType._InitializeFacetMap(machineType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'machineType', machineType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}material
class material (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'material')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3286, 1)
    _Documentation = None
material._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=material, enum_prefix=None)
material.Unknown = material._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
material.AAAC = material._CF_enumeration.addEnumeration(unicode_value='AAAC', tag='AAAC')
material.AAC = material._CF_enumeration.addEnumeration(unicode_value='AAC', tag='AAC')
material.ACAR = material._CF_enumeration.addEnumeration(unicode_value='ACAR', tag='ACAR')
material.ACSR = material._CF_enumeration.addEnumeration(unicode_value='ACSR', tag='ACSR')
material.ACSRT2 = material._CF_enumeration.addEnumeration(unicode_value='ACSRT2', tag='ACSRT2')
material.AlumoWeld = material._CF_enumeration.addEnumeration(unicode_value='AlumoWeld', tag='AlumoWeld')
material.Anaconda = material._CF_enumeration.addEnumeration(unicode_value='Anaconda', tag='Anaconda')
material.CopperWeld = material._CF_enumeration.addEnumeration(unicode_value='CopperWeld', tag='CopperWeld')
material.CopperWeldCopper = material._CF_enumeration.addEnumeration(unicode_value='CopperWeldCopper', tag='CopperWeldCopper')
material.ExpandedACSR = material._CF_enumeration.addEnumeration(unicode_value='ExpandedACSR', tag='ExpandedACSR')
material.GalvanizedSteel = material._CF_enumeration.addEnumeration(unicode_value='GalvanizedSteel', tag='GalvanizedSteel')
material.HardDrawnAluminum = material._CF_enumeration.addEnumeration(unicode_value='HardDrawnAluminum', tag='HardDrawnAluminum')
material.HardDrawnCopper = material._CF_enumeration.addEnumeration(unicode_value='HardDrawnCopper', tag='HardDrawnCopper')
material.HHHollowCopper = material._CF_enumeration.addEnumeration(unicode_value='HHHollowCopper', tag='HHHollowCopper')
material.HighStrengthSteel = material._CF_enumeration.addEnumeration(unicode_value='HighStrengthSteel', tag='HighStrengthSteel')
material.StainlessSteelStrand = material._CF_enumeration.addEnumeration(unicode_value='StainlessSteelStrand', tag='StainlessSteelStrand')
material.Other = material._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
material._InitializeFacetMap(material._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'material', material)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}materialClassKind
class materialClassKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'materialClassKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3319, 1)
    _Documentation = None
materialClassKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=materialClassKind, enum_prefix=None)
materialClassKind.Unknown = materialClassKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
materialClassKind.Expensed = materialClassKind._CF_enumeration.addEnumeration(unicode_value='Expensed', tag='Expensed')
materialClassKind.GeneralInventory = materialClassKind._CF_enumeration.addEnumeration(unicode_value='GeneralInventory', tag='GeneralInventory')
materialClassKind.SpecialEquipment = materialClassKind._CF_enumeration.addEnumeration(unicode_value='SpecialEquipment', tag='SpecialEquipment')
materialClassKind.ForRequisition = materialClassKind._CF_enumeration.addEnumeration(unicode_value='ForRequisition', tag='ForRequisition')
materialClassKind.Other = materialClassKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
materialClassKind._InitializeFacetMap(materialClassKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'materialClassKind', materialClassKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}materialUnitsKind
class materialUnitsKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'materialUnitsKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3340, 1)
    _Documentation = None
materialUnitsKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=materialUnitsKind, enum_prefix=None)
materialUnitsKind.Unknown = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
materialUnitsKind.Feet = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Feet', tag='Feet')
materialUnitsKind.Meters = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Meters', tag='Meters')
materialUnitsKind.Inches = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Inches', tag='Inches')
materialUnitsKind.Pounds = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Pounds', tag='Pounds')
materialUnitsKind.Kilograms = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Kilograms', tag='Kilograms')
materialUnitsKind.Miles = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Miles', tag='Miles')
materialUnitsKind.ThousandFeet = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='ThousandFeet', tag='ThousandFeet')
materialUnitsKind.Kilometers = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Kilometers', tag='Kilometers')
materialUnitsKind.Pair = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Pair', tag='Pair')
materialUnitsKind.Each = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Each', tag='Each')
materialUnitsKind.Hour = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Hour', tag='Hour')
materialUnitsKind.DoNotChange = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='DoNotChange', tag='DoNotChange')
materialUnitsKind.Other = materialUnitsKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
materialUnitsKind._InitializeFacetMap(materialUnitsKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'materialUnitsKind', materialUnitsKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}measurementDeviceKind
class measurementDeviceKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of measurement device."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measurementDeviceKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3358, 1)
    _Documentation = 'Type of measurement device.'
measurementDeviceKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=measurementDeviceKind, enum_prefix=None)
measurementDeviceKind.Unknown = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
measurementDeviceKind.ElectricMeter = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='ElectricMeter', tag='ElectricMeter')
measurementDeviceKind.GasMeter = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='GasMeter', tag='GasMeter')
measurementDeviceKind.WaterMeter = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='WaterMeter', tag='WaterMeter')
measurementDeviceKind.Demand = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='Demand', tag='Demand')
measurementDeviceKind.Harmonic = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='Harmonic', tag='Harmonic')
measurementDeviceKind.PhaseAngle = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='PhaseAngle', tag='PhaseAngle')
measurementDeviceKind.BusVoltage = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='BusVoltage', tag='BusVoltage')
measurementDeviceKind.BusCurrent = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='BusCurrent', tag='BusCurrent')
measurementDeviceKind.BreakerVoltage = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='BreakerVoltage', tag='BreakerVoltage')
measurementDeviceKind.BreakerCurrent = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='BreakerCurrent', tag='BreakerCurrent')
measurementDeviceKind.LineVoltage = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='LineVoltage', tag='LineVoltage')
measurementDeviceKind.LineCurrent = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='LineCurrent', tag='LineCurrent')
measurementDeviceKind.GPSClock = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='GPSClock', tag='GPSClock')
measurementDeviceKind.Temperature = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='Temperature', tag='Temperature')
measurementDeviceKind.Other = measurementDeviceKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
measurementDeviceKind._InitializeFacetMap(measurementDeviceKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'measurementDeviceKind', measurementDeviceKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}measurementDeviceStatusKind
class measurementDeviceStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measurementDeviceStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3392, 1)
    _Documentation = None
measurementDeviceStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=measurementDeviceStatusKind, enum_prefix=None)
measurementDeviceStatusKind.Unknown = measurementDeviceStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
measurementDeviceStatusKind.InService = measurementDeviceStatusKind._CF_enumeration.addEnumeration(unicode_value='InService', tag='InService')
measurementDeviceStatusKind.OutofService = measurementDeviceStatusKind._CF_enumeration.addEnumeration(unicode_value='OutofService', tag='OutofService')
measurementDeviceStatusKind.Other = measurementDeviceStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
measurementDeviceStatusKind._InitializeFacetMap(measurementDeviceStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'measurementDeviceStatusKind', measurementDeviceStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}measurementPeriod
class measurementPeriod (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Period during which this reading was taken."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measurementPeriod')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3411, 1)
    _Documentation = 'Period during which this reading was taken.'
measurementPeriod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=measurementPeriod, enum_prefix=None)
measurementPeriod.Current = measurementPeriod._CF_enumeration.addEnumeration(unicode_value='Current', tag='Current')
measurementPeriod.Previous = measurementPeriod._CF_enumeration.addEnumeration(unicode_value='Previous', tag='Previous')
measurementPeriod.Previous_Season = measurementPeriod._CF_enumeration.addEnumeration(unicode_value='Previous Season', tag='Previous_Season')
measurementPeriod._InitializeFacetMap(measurementPeriod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'measurementPeriod', measurementPeriod)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}measurementSystem
class measurementSystem (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Measurement system for meter (from C12.19).

0 - English
1 - Metric"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measurementSystem')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3421, 1)
    _Documentation = 'Measurement system for meter (from C12.19).\n\n0 - English\n1 - Metric'
measurementSystem._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=measurementSystem, enum_prefix=None)
measurementSystem.n0 = measurementSystem._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
measurementSystem.n1 = measurementSystem._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
measurementSystem._InitializeFacetMap(measurementSystem._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'measurementSystem', measurementSystem)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}mechanicalForm
class mechanicalForm (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Mechanical form of gas meter (from C12.19).

0 - Unclassified
1 - Bellows meter
2 - Rotary
3 - Turbine meter
4 - Fluidic oscillator
5 - Anemometer"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mechanicalForm')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3433, 1)
    _Documentation = 'Mechanical form of gas meter (from C12.19).\n\n0 - Unclassified\n1 - Bellows meter\n2 - Rotary\n3 - Turbine meter\n4 - Fluidic oscillator\n5 - Anemometer'
mechanicalForm._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=mechanicalForm, enum_prefix=None)
mechanicalForm.n0 = mechanicalForm._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
mechanicalForm.n1 = mechanicalForm._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
mechanicalForm.n2 = mechanicalForm._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
mechanicalForm.n3 = mechanicalForm._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
mechanicalForm.n4 = mechanicalForm._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
mechanicalForm.n5 = mechanicalForm._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
mechanicalForm._InitializeFacetMap(mechanicalForm._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'mechanicalForm', mechanicalForm)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}messageResultLevelKind
class messageResultLevelKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """It is suggested that the values of replyCode be chosen from those values included in IEC 61968-9, 2nd Ed., Annex B as extended by Appendix A of "Security in MultiSpeak-Enabled Applications: Requirements".  Values of replyCode SHOULD be of the form [category] "." [index]."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'messageResultLevelKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3464, 1)
    _Documentation = 'It is suggested that the values of replyCode be chosen from those values included in IEC 61968-9, 2nd Ed., Annex B as extended by Appendix A of "Security in MultiSpeak-Enabled Applications: Requirements".  Values of replyCode SHOULD be of the form [category] "." [index].'
messageResultLevelKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=messageResultLevelKind, enum_prefix=None)
messageResultLevelKind.Inform = messageResultLevelKind._CF_enumeration.addEnumeration(unicode_value='Inform', tag='Inform')
messageResultLevelKind.Warning = messageResultLevelKind._CF_enumeration.addEnumeration(unicode_value='Warning', tag='Warning')
messageResultLevelKind.Fatal = messageResultLevelKind._CF_enumeration.addEnumeration(unicode_value='Fatal', tag='Fatal')
messageResultLevelKind.Catastrophic = messageResultLevelKind._CF_enumeration.addEnumeration(unicode_value='Catastrophic', tag='Catastrophic')
messageResultLevelKind.Other = messageResultLevelKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
messageResultLevelKind._InitializeFacetMap(messageResultLevelKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'messageResultLevelKind', messageResultLevelKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}meterConnectionStatusKind
class meterConnectionStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The connection status of a meter. Connected means that the meter is in the circuit and can receive service, Disconnected means that the meter is out of the circuit and cannot receive service. DisconnectedNonPay means that the meter is disconnected, but the reason for the disconnection is that the account has been disconnected for non-payment."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'meterConnectionStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3487, 1)
    _Documentation = 'The connection status of a meter. Connected means that the meter is in the circuit and can receive service, Disconnected means that the meter is out of the circuit and cannot receive service. DisconnectedNonPay means that the meter is disconnected, but the reason for the disconnection is that the account has been disconnected for non-payment.'
meterConnectionStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=meterConnectionStatusKind, enum_prefix=None)
meterConnectionStatusKind.Unknown = meterConnectionStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
meterConnectionStatusKind.Connected = meterConnectionStatusKind._CF_enumeration.addEnumeration(unicode_value='Connected', tag='Connected')
meterConnectionStatusKind.Disconnected = meterConnectionStatusKind._CF_enumeration.addEnumeration(unicode_value='Disconnected', tag='Disconnected')
meterConnectionStatusKind.ConnectedOverride = meterConnectionStatusKind._CF_enumeration.addEnumeration(unicode_value='ConnectedOverride', tag='ConnectedOverride')
meterConnectionStatusKind.DisconnectedOverride = meterConnectionStatusKind._CF_enumeration.addEnumeration(unicode_value='DisconnectedOverride', tag='DisconnectedOverride')
meterConnectionStatusKind.DisconnectedNonPay = meterConnectionStatusKind._CF_enumeration.addEnumeration(unicode_value='DisconnectedNonPay', tag='DisconnectedNonPay')
meterConnectionStatusKind.Other = meterConnectionStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
meterConnectionStatusKind._InitializeFacetMap(meterConnectionStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'meterConnectionStatusKind', meterConnectionStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}meterStatusKind
class meterStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'meterStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3501, 1)
    _Documentation = None
meterStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=meterStatusKind, enum_prefix=None)
meterStatusKind.Other = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
meterStatusKind.New = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='New', tag='New')
meterStatusKind.InInventory = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='InInventory', tag='InInventory')
meterStatusKind.Installed = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='Installed', tag='Installed')
meterStatusKind.Active = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
meterStatusKind.Inactive = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='Inactive', tag='Inactive')
meterStatusKind.Connected = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='Connected', tag='Connected')
meterStatusKind.Disconnected = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='Disconnected', tag='Disconnected')
meterStatusKind.ConnectedOverride = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='ConnectedOverride', tag='ConnectedOverride')
meterStatusKind.DisconnectedOverride = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='DisconnectedOverride', tag='DisconnectedOverride')
meterStatusKind.OnHold = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='OnHold', tag='OnHold')
meterStatusKind.InForRepair = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='InForRepair', tag='InForRepair')
meterStatusKind.InTesting = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='InTesting', tag='InTesting')
meterStatusKind.Retired = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='Retired', tag='Retired')
meterStatusKind.Unknown = meterStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
meterStatusKind._InitializeFacetMap(meterStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'meterStatusKind', meterStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}modelRoleKind
class modelRoleKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'modelRoleKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3542, 1)
    _Documentation = None
modelRoleKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=modelRoleKind, enum_prefix=None)
modelRoleKind.Base = modelRoleKind._CF_enumeration.addEnumeration(unicode_value='Base', tag='Base')
modelRoleKind.Incremental = modelRoleKind._CF_enumeration.addEnumeration(unicode_value='Incremental', tag='Incremental')
modelRoleKind.Other = modelRoleKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
modelRoleKind._InitializeFacetMap(modelRoleKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'modelRoleKind', modelRoleKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}monthNumber
class monthNumber (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Month number."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'monthNumber')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3557, 1)
    _Documentation = 'Month number.'
monthNumber._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=monthNumber, enum_prefix=None)
monthNumber.n1 = monthNumber._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
monthNumber.n2 = monthNumber._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
monthNumber.n3 = monthNumber._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
monthNumber.n4 = monthNumber._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
monthNumber.n5 = monthNumber._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
monthNumber.n6 = monthNumber._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
monthNumber.n7 = monthNumber._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
monthNumber.n8 = monthNumber._CF_enumeration.addEnumeration(unicode_value='8', tag='n8')
monthNumber.n9 = monthNumber._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
monthNumber.n10 = monthNumber._CF_enumeration.addEnumeration(unicode_value='10', tag='n10')
monthNumber.n11 = monthNumber._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
monthNumber.n12 = monthNumber._CF_enumeration.addEnumeration(unicode_value='12', tag='n12')
monthNumber._InitializeFacetMap(monthNumber._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'monthNumber', monthNumber)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}motorStatusKind
class motorStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'motorStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3587, 1)
    _Documentation = None
motorStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=motorStatusKind, enum_prefix=None)
motorStatusKind.Disconnected = motorStatusKind._CF_enumeration.addEnumeration(unicode_value='Disconnected', tag='Disconnected')
motorStatusKind.LockedRotor = motorStatusKind._CF_enumeration.addEnumeration(unicode_value='LockedRotor', tag='LockedRotor')
motorStatusKind.Off = motorStatusKind._CF_enumeration.addEnumeration(unicode_value='Off', tag='Off')
motorStatusKind.Other = motorStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
motorStatusKind.Running = motorStatusKind._CF_enumeration.addEnumeration(unicode_value='Running', tag='Running')
motorStatusKind.SoftStart = motorStatusKind._CF_enumeration.addEnumeration(unicode_value='SoftStart', tag='SoftStart')
motorStatusKind.Unknown = motorStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
motorStatusKind._InitializeFacetMap(motorStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'motorStatusKind', motorStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}mountingKind
class mountingKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mountingKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3598, 1)
    _Documentation = None
mountingKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=mountingKind, enum_prefix=None)
mountingKind.Unknown = mountingKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
mountingKind.BusMounted = mountingKind._CF_enumeration.addEnumeration(unicode_value='BusMounted', tag='BusMounted')
mountingKind.PoleMounted = mountingKind._CF_enumeration.addEnumeration(unicode_value='PoleMounted', tag='PoleMounted')
mountingKind.PadMounted = mountingKind._CF_enumeration.addEnumeration(unicode_value='PadMounted', tag='PadMounted')
mountingKind.VaultMounted = mountingKind._CF_enumeration.addEnumeration(unicode_value='VaultMounted', tag='VaultMounted')
mountingKind.Substation = mountingKind._CF_enumeration.addEnumeration(unicode_value='Substation', tag='Substation')
mountingKind.Other = mountingKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
mountingKind._InitializeFacetMap(mountingKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'mountingKind', mountingKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}mspPhase
class mspPhase (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mspPhase')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3620, 1)
    _Documentation = None
mspPhase._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=mspPhase, enum_prefix=None)
mspPhase.Unknown = mspPhase._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
mspPhase.A = mspPhase._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
mspPhase.B = mspPhase._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
mspPhase.C = mspPhase._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
mspPhase.N = mspPhase._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
mspPhase._InitializeFacetMap(mspPhase._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'mspPhase', mspPhase)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}NEMAFrameKind
class NEMAFrameKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NEMAFrameKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3629, 1)
    _Documentation = None
NEMAFrameKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NEMAFrameKind, enum_prefix=None)
NEMAFrameKind.Other = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
NEMAFrameKind.A = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
NEMAFrameKind.B = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
NEMAFrameKind.C = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
NEMAFrameKind.D = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
NEMAFrameKind.E = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
NEMAFrameKind.F = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='F', tag='F')
NEMAFrameKind.G = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='G', tag='G')
NEMAFrameKind.H = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='H', tag='H')
NEMAFrameKind.J = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='J', tag='J')
NEMAFrameKind.K = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='K', tag='K')
NEMAFrameKind.L = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='L', tag='L')
NEMAFrameKind.M = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='M', tag='M')
NEMAFrameKind.N = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
NEMAFrameKind.P = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='P', tag='P')
NEMAFrameKind.R = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
NEMAFrameKind.S = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
NEMAFrameKind.T = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
NEMAFrameKind.U = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='U', tag='U')
NEMAFrameKind.V = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
NEMAFrameKind.None_ = NEMAFrameKind._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
NEMAFrameKind._InitializeFacetMap(NEMAFrameKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NEMAFrameKind', NEMAFrameKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}nominalServiceVoltageKind
class nominalServiceVoltageKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Nominal service voltages."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nominalServiceVoltageKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3676, 1)
    _Documentation = 'Nominal service voltages.'
nominalServiceVoltageKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nominalServiceVoltageKind, enum_prefix=None)
nominalServiceVoltageKind.Unknown = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
nominalServiceVoltageKind.n110 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='110', tag='n110')
nominalServiceVoltageKind.n110220 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='110/220', tag='n110220')
nominalServiceVoltageKind.n115 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='115', tag='n115')
nominalServiceVoltageKind.n115230 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='115/230', tag='n115230')
nominalServiceVoltageKind.n120 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='120', tag='n120')
nominalServiceVoltageKind.n120240 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='120/240', tag='n120240')
nominalServiceVoltageKind.n125 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='125', tag='n125')
nominalServiceVoltageKind.n125250 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='125/250', tag='n125250')
nominalServiceVoltageKind.n208Y120 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='208Y/120', tag='n208Y120')
nominalServiceVoltageKind.n216Y125 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='216Y/125', tag='n216Y125')
nominalServiceVoltageKind.n230 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='230', tag='n230')
nominalServiceVoltageKind.n240 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='240', tag='n240')
nominalServiceVoltageKind.n240120 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='240/120', tag='n240120')
nominalServiceVoltageKind.n250 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='250', tag='n250')
nominalServiceVoltageKind.n440 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='440', tag='n440')
nominalServiceVoltageKind.n460Y265 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='460Y/265', tag='n460Y265')
nominalServiceVoltageKind.n480 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='480', tag='n480')
nominalServiceVoltageKind.n480Y277 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='480Y/277', tag='n480Y277')
nominalServiceVoltageKind.n550 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='550', tag='n550')
nominalServiceVoltageKind.n575 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='575', tag='n575')
nominalServiceVoltageKind.n600 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='600', tag='n600')
nominalServiceVoltageKind.n2200 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='2200', tag='n2200')
nominalServiceVoltageKind.n2300 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='2300', tag='n2300')
nominalServiceVoltageKind.n2400 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='2400', tag='n2400')
nominalServiceVoltageKind.n4000 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='4000', tag='n4000')
nominalServiceVoltageKind.n4160 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='4160', tag='n4160')
nominalServiceVoltageKind.n4160Y2400 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='4160Y/2400', tag='n4160Y2400')
nominalServiceVoltageKind.n4600 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='4600', tag='n4600')
nominalServiceVoltageKind.n4800 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='4800', tag='n4800')
nominalServiceVoltageKind.n6600 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='6600', tag='n6600')
nominalServiceVoltageKind.n6900 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='6900', tag='n6900')
nominalServiceVoltageKind.n7200 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='7200', tag='n7200')
nominalServiceVoltageKind.n8320Y4800 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='8320Y/4800', tag='n8320Y4800')
nominalServiceVoltageKind.n11000 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='11000', tag='n11000')
nominalServiceVoltageKind.n11500 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='11500', tag='n11500')
nominalServiceVoltageKind.n12000Y6930 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='12000Y/6930', tag='n12000Y6930')
nominalServiceVoltageKind.n12470Y7200 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='12470Y7200', tag='n12470Y7200')
nominalServiceVoltageKind.n13200 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='13200', tag='n13200')
nominalServiceVoltageKind.n13200Y7620 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='13200Y/7620', tag='n13200Y7620')
nominalServiceVoltageKind.n13800 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='13800', tag='n13800')
nominalServiceVoltageKind.n13800Y7970 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='13800Y/7970', tag='n13800Y7970')
nominalServiceVoltageKind.n14400 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='14400', tag='n14400')
nominalServiceVoltageKind.n20780Y1200 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='20780Y/1200', tag='n20780Y1200')
nominalServiceVoltageKind.n22860Y13200 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='22860Y/13200', tag='n22860Y13200')
nominalServiceVoltageKind.n23000 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='23000', tag='n23000')
nominalServiceVoltageKind.n24940Y14400 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='24940Y/14400', tag='n24940Y14400')
nominalServiceVoltageKind.n33000 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='33000', tag='n33000')
nominalServiceVoltageKind.n34500 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='34500', tag='n34500')
nominalServiceVoltageKind.n34500Y19920 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='34500Y/19920', tag='n34500Y19920')
nominalServiceVoltageKind.n44000 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='44000', tag='n44000')
nominalServiceVoltageKind.n46000 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='46000', tag='n46000')
nominalServiceVoltageKind.n66000 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='66000', tag='n66000')
nominalServiceVoltageKind.n69000 = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='69000', tag='n69000')
nominalServiceVoltageKind.Other = nominalServiceVoltageKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
nominalServiceVoltageKind._InitializeFacetMap(nominalServiceVoltageKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'nominalServiceVoltageKind', nominalServiceVoltageKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}notificationModeKind
class notificationModeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'notificationModeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3738, 1)
    _Documentation = None
notificationModeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=notificationModeKind, enum_prefix=None)
notificationModeKind.Unknown = notificationModeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
notificationModeKind.IVRCall = notificationModeKind._CF_enumeration.addEnumeration(unicode_value='IVRCall', tag='IVRCall')
notificationModeKind.ManualCall = notificationModeKind._CF_enumeration.addEnumeration(unicode_value='ManualCall', tag='ManualCall')
notificationModeKind.EMail = notificationModeKind._CF_enumeration.addEnumeration(unicode_value='EMail', tag='EMail')
notificationModeKind.MobileApp = notificationModeKind._CF_enumeration.addEnumeration(unicode_value='MobileApp', tag='MobileApp')
notificationModeKind.SMS = notificationModeKind._CF_enumeration.addEnumeration(unicode_value='SMS', tag='SMS')
notificationModeKind.Other = notificationModeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
notificationModeKind._InitializeFacetMap(notificationModeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'notificationModeKind', notificationModeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}odometerReadingType
class odometerReadingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'odometerReadingType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3760, 1)
    _Documentation = None
odometerReadingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=odometerReadingType, enum_prefix=None)
odometerReadingType.Unknown = odometerReadingType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
odometerReadingType.Absolute = odometerReadingType._CF_enumeration.addEnumeration(unicode_value='Absolute', tag='Absolute')
odometerReadingType.Delta = odometerReadingType._CF_enumeration.addEnumeration(unicode_value='Delta', tag='Delta')
odometerReadingType.Other = odometerReadingType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
odometerReadingType._InitializeFacetMap(odometerReadingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'odometerReadingType', odometerReadingType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}organizationRoleKind
class organizationRoleKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The role that this organization plays in the agreement."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'organizationRoleKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3779, 1)
    _Documentation = 'The role that this organization plays in the agreement.'
organizationRoleKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=organizationRoleKind, enum_prefix=None)
organizationRoleKind.Unknown = organizationRoleKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
organizationRoleKind.RetailPowerSupplier = organizationRoleKind._CF_enumeration.addEnumeration(unicode_value='RetailPowerSupplier', tag='RetailPowerSupplier')
organizationRoleKind.BillingServiceSupplier = organizationRoleKind._CF_enumeration.addEnumeration(unicode_value='BillingServiceSupplier', tag='BillingServiceSupplier')
organizationRoleKind.BulkPowerSupplier = organizationRoleKind._CF_enumeration.addEnumeration(unicode_value='BulkPowerSupplier', tag='BulkPowerSupplier')
organizationRoleKind.Customer = organizationRoleKind._CF_enumeration.addEnumeration(unicode_value='Customer', tag='Customer')
organizationRoleKind.MarketAggregator = organizationRoleKind._CF_enumeration.addEnumeration(unicode_value='MarketAggregator', tag='MarketAggregator')
organizationRoleKind.MeteringServiceSupplier = organizationRoleKind._CF_enumeration.addEnumeration(unicode_value='MeteringServiceSupplier', tag='MeteringServiceSupplier')
organizationRoleKind.Other = organizationRoleKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
organizationRoleKind._InitializeFacetMap(organizationRoleKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'organizationRoleKind', organizationRoleKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}otherKind
class otherKind (pyxb.binding.datatypes.string):

    """If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'otherKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3794, 1)
    _Documentation = 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.'
otherKind._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'otherKind', otherKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}outageHistoryEventTypeKind
class outageHistoryEventTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outageHistoryEventTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3811, 1)
    _Documentation = None
outageHistoryEventTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=outageHistoryEventTypeKind, enum_prefix=None)
outageHistoryEventTypeKind.Unknown = outageHistoryEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
outageHistoryEventTypeKind.StartTime = outageHistoryEventTypeKind._CF_enumeration.addEnumeration(unicode_value='StartTime', tag='StartTime')
outageHistoryEventTypeKind.OutageDefined = outageHistoryEventTypeKind._CF_enumeration.addEnumeration(unicode_value='OutageDefined', tag='OutageDefined')
outageHistoryEventTypeKind.FirstDispatch = outageHistoryEventTypeKind._CF_enumeration.addEnumeration(unicode_value='FirstDispatch', tag='FirstDispatch')
outageHistoryEventTypeKind.FirstETA = outageHistoryEventTypeKind._CF_enumeration.addEnumeration(unicode_value='FirstETA', tag='FirstETA')
outageHistoryEventTypeKind.FirstArrival = outageHistoryEventTypeKind._CF_enumeration.addEnumeration(unicode_value='FirstArrival', tag='FirstArrival')
outageHistoryEventTypeKind.Completed = outageHistoryEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Completed', tag='Completed')
outageHistoryEventTypeKind.Other = outageHistoryEventTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
outageHistoryEventTypeKind._InitializeFacetMap(outageHistoryEventTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'outageHistoryEventTypeKind', outageHistoryEventTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}outageKind
class outageKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outageKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3823, 1)
    _Documentation = None
outageKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=outageKind, enum_prefix=None)
outageKind.Unknown = outageKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
outageKind.Planned = outageKind._CF_enumeration.addEnumeration(unicode_value='Planned', tag='Planned')
outageKind.Unplanned = outageKind._CF_enumeration.addEnumeration(unicode_value='Unplanned', tag='Unplanned')
outageKind.NonPay = outageKind._CF_enumeration.addEnumeration(unicode_value='NonPay', tag='NonPay')
outageKind.Other = outageKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
outageKind._InitializeFacetMap(outageKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'outageKind', outageKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}outagePriorityKind
class outagePriorityKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outagePriorityKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3843, 1)
    _Documentation = None
outagePriorityKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=outagePriorityKind, enum_prefix=None)
outagePriorityKind.Unknown = outagePriorityKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
outagePriorityKind.Critical = outagePriorityKind._CF_enumeration.addEnumeration(unicode_value='Critical', tag='Critical')
outagePriorityKind.High = outagePriorityKind._CF_enumeration.addEnumeration(unicode_value='High', tag='High')
outagePriorityKind.Normal = outagePriorityKind._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
outagePriorityKind.Low = outagePriorityKind._CF_enumeration.addEnumeration(unicode_value='Low', tag='Low')
outagePriorityKind.Other = outagePriorityKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
outagePriorityKind._InitializeFacetMap(outagePriorityKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'outagePriorityKind', outagePriorityKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}outageReasonCategoryKind
class outageReasonCategoryKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Category for the outage reporting information.  Descriptions for the category should be: "Outage Cause - This is the primary cause of the outage ; "Equipment Failure" - This is the material or equipment that failed, producing the outage; "Voltage Level" - this is the phase-to-phase voltage of the system that failed; "Weather Condition" - The weather conditions at the site of the failure at the time the outage occurred (This is not to be used for reporting a weather condition that was the primary cause of the outage - that should be reported using Outage Cause; "System Characterization" The kind of customer density at the location of the outage; "Responsible System" - The portion of the electrical system that was responsible for the outage; "Outage Condition" - The condition that the system was subject to at the time of the fault (For example, was it a Major Event Day as defined by IEEE 1366); "Interrupting Device" - The kind of interrupting device that protected customers in response to the fault; "Interrupting Device Initiation" - The manner in which the interrupting device operated at the time of the fault; "Customer Restoration" - The manner in which the customer's service was restored."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outageReasonCategoryKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3867, 1)
    _Documentation = 'Category for the outage reporting information.  Descriptions for the category should be: "Outage Cause - This is the primary cause of the outage ; "Equipment Failure" - This is the material or equipment that failed, producing the outage; "Voltage Level" - this is the phase-to-phase voltage of the system that failed; "Weather Condition" - The weather conditions at the site of the failure at the time the outage occurred (This is not to be used for reporting a weather condition that was the primary cause of the outage - that should be reported using Outage Cause; "System Characterization" The kind of customer density at the location of the outage; "Responsible System" - The portion of the electrical system that was responsible for the outage; "Outage Condition" - The condition that the system was subject to at the time of the fault (For example, was it a Major Event Day as defined by IEEE 1366); "Interrupting Device" - The kind of interrupting device that protected customers in response to the fault; "Interrupting Device Initiation" - The manner in which the interrupting device operated at the time of the fault; "Customer Restoration" - The manner in which the customer\'s service was restored.'
outageReasonCategoryKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=outageReasonCategoryKind, enum_prefix=None)
outageReasonCategoryKind.Unknown = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
outageReasonCategoryKind.OutageCause = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='OutageCause', tag='OutageCause')
outageReasonCategoryKind.EquipmentFailure = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='EquipmentFailure', tag='EquipmentFailure')
outageReasonCategoryKind.VoltageLevel = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='VoltageLevel', tag='VoltageLevel')
outageReasonCategoryKind.WeatherCondition = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='WeatherCondition', tag='WeatherCondition')
outageReasonCategoryKind.ResponsibleSystem = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='ResponsibleSystem', tag='ResponsibleSystem')
outageReasonCategoryKind.OutageCondition = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='OutageCondition', tag='OutageCondition')
outageReasonCategoryKind.InterruptingDeviceInitiation = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='InterruptingDeviceInitiation', tag='InterruptingDeviceInitiation')
outageReasonCategoryKind.CustomerRestoration = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='CustomerRestoration', tag='CustomerRestoration')
outageReasonCategoryKind.Other = outageReasonCategoryKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
outageReasonCategoryKind._InitializeFacetMap(outageReasonCategoryKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'outageReasonCategoryKind', outageReasonCategoryKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}outageStateKind
class outageStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outageStateKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3895, 1)
    _Documentation = None
outageStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=outageStateKind, enum_prefix=None)
outageStateKind.Unknown = outageStateKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
outageStateKind.Assumed = outageStateKind._CF_enumeration.addEnumeration(unicode_value='Assumed', tag='Assumed')
outageStateKind.Confirmed = outageStateKind._CF_enumeration.addEnumeration(unicode_value='Confirmed', tag='Confirmed')
outageStateKind.Restored = outageStateKind._CF_enumeration.addEnumeration(unicode_value='Restored', tag='Restored')
outageStateKind.Scheduled = outageStateKind._CF_enumeration.addEnumeration(unicode_value='Scheduled', tag='Scheduled')
outageStateKind.UnidentifiedLocation = outageStateKind._CF_enumeration.addEnumeration(unicode_value='UnidentifiedLocation', tag='UnidentifiedLocation')
outageStateKind.Other = outageStateKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
outageStateKind._InitializeFacetMap(outageStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'outageStateKind', outageStateKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}PANCommissionStatusKind
class PANCommissionStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PANCommissionStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3928, 1)
    _Documentation = None
PANCommissionStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PANCommissionStatusKind, enum_prefix=None)
PANCommissionStatusKind.Unknown = PANCommissionStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
PANCommissionStatusKind.Commissioned = PANCommissionStatusKind._CF_enumeration.addEnumeration(unicode_value='Commissioned', tag='Commissioned')
PANCommissionStatusKind.Decommissioned = PANCommissionStatusKind._CF_enumeration.addEnumeration(unicode_value='Decommissioned', tag='Decommissioned')
PANCommissionStatusKind.Other = PANCommissionStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
PANCommissionStatusKind._InitializeFacetMap(PANCommissionStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PANCommissionStatusKind', PANCommissionStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}PANRegistrationStatusKind
class PANRegistrationStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The status of a device's registration in a Premises Area Network. The set of states represent the progression of a device's pairing in the PAN. Note that the specific states supported is implementation dependent. For e.g. one implementation may only support "Registered" and "Disconnected" while another may support the full set of states."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PANRegistrationStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3959, 1)
    _Documentation = 'The status of a device\'s registration in a Premises Area Network. The set of states represent the progression of a device\'s pairing in the PAN. Note that the specific states supported is implementation dependent. For e.g. one implementation may only support "Registered" and "Disconnected" while another may support the full set of states.'
PANRegistrationStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PANRegistrationStatusKind, enum_prefix=None)
PANRegistrationStatusKind.Unknown = PANRegistrationStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
PANRegistrationStatusKind.Joining = PANRegistrationStatusKind._CF_enumeration.addEnumeration(unicode_value='Joining', tag='Joining')
PANRegistrationStatusKind.Leaving = PANRegistrationStatusKind._CF_enumeration.addEnumeration(unicode_value='Leaving', tag='Leaving')
PANRegistrationStatusKind.Connected = PANRegistrationStatusKind._CF_enumeration.addEnumeration(unicode_value='Connected', tag='Connected')
PANRegistrationStatusKind.Disconnected = PANRegistrationStatusKind._CF_enumeration.addEnumeration(unicode_value='Disconnected', tag='Disconnected')
PANRegistrationStatusKind.Other = PANRegistrationStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
PANRegistrationStatusKind._InitializeFacetMap(PANRegistrationStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PANRegistrationStatusKind', PANRegistrationStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}phaseAssociation
class phaseAssociation (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This element defines the phase measurement associations. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phaseAssociation')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3990, 1)
    _Documentation = 'This element defines the phase measurement associations. '
phaseAssociation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=phaseAssociation, enum_prefix=None)
phaseAssociation.A_B = phaseAssociation._CF_enumeration.addEnumeration(unicode_value='A-B', tag='A_B')
phaseAssociation.B_C = phaseAssociation._CF_enumeration.addEnumeration(unicode_value='B-C', tag='B_C')
phaseAssociation.C_A = phaseAssociation._CF_enumeration.addEnumeration(unicode_value='C-A', tag='C_A')
phaseAssociation.Neutral_Gnd = phaseAssociation._CF_enumeration.addEnumeration(unicode_value='Neutral-Gnd', tag='Neutral_Gnd')
phaseAssociation.A_Neutral = phaseAssociation._CF_enumeration.addEnumeration(unicode_value='A-Neutral', tag='A_Neutral')
phaseAssociation.B_Neutral = phaseAssociation._CF_enumeration.addEnumeration(unicode_value='B-Neutral', tag='B_Neutral')
phaseAssociation.C_Neutral = phaseAssociation._CF_enumeration.addEnumeration(unicode_value='C-Neutral', tag='C_Neutral')
phaseAssociation._InitializeFacetMap(phaseAssociation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'phaseAssociation', phaseAssociation)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}phaseCode
class phaseCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phaseCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4004, 1)
    _Documentation = None
phaseCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=phaseCode, enum_prefix=None)
phaseCode.Unknown = phaseCode._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
phaseCode.A = phaseCode._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
phaseCode.B = phaseCode._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
phaseCode.C = phaseCode._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
phaseCode.N = phaseCode._CF_enumeration.addEnumeration(unicode_value='N', tag='N')
phaseCode.AB = phaseCode._CF_enumeration.addEnumeration(unicode_value='AB', tag='AB')
phaseCode.AC = phaseCode._CF_enumeration.addEnumeration(unicode_value='AC', tag='AC')
phaseCode.BC = phaseCode._CF_enumeration.addEnumeration(unicode_value='BC', tag='BC')
phaseCode.ABC = phaseCode._CF_enumeration.addEnumeration(unicode_value='ABC', tag='ABC')
phaseCode.AN = phaseCode._CF_enumeration.addEnumeration(unicode_value='AN', tag='AN')
phaseCode.BN = phaseCode._CF_enumeration.addEnumeration(unicode_value='BN', tag='BN')
phaseCode.CN = phaseCode._CF_enumeration.addEnumeration(unicode_value='CN', tag='CN')
phaseCode.ABN = phaseCode._CF_enumeration.addEnumeration(unicode_value='ABN', tag='ABN')
phaseCode.ACN = phaseCode._CF_enumeration.addEnumeration(unicode_value='ACN', tag='ACN')
phaseCode.BCN = phaseCode._CF_enumeration.addEnumeration(unicode_value='BCN', tag='BCN')
phaseCode.ABCN = phaseCode._CF_enumeration.addEnumeration(unicode_value='ABCN', tag='ABCN')
phaseCode._InitializeFacetMap(phaseCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'phaseCode', phaseCode)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}phaseStatusKind
class phaseStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phaseStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4024, 1)
    _Documentation = None
phaseStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=phaseStatusKind, enum_prefix=None)
phaseStatusKind.Unknown = phaseStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
phaseStatusKind.VerifiedOpen = phaseStatusKind._CF_enumeration.addEnumeration(unicode_value='VerifiedOpen', tag='VerifiedOpen')
phaseStatusKind.VerifiedClosedWithPower = phaseStatusKind._CF_enumeration.addEnumeration(unicode_value='VerifiedClosedWithPower', tag='VerifiedClosedWithPower')
phaseStatusKind.VerifiedClosedNoPower = phaseStatusKind._CF_enumeration.addEnumeration(unicode_value='VerifiedClosedNoPower', tag='VerifiedClosedNoPower')
phaseStatusKind.VerifiedBreak = phaseStatusKind._CF_enumeration.addEnumeration(unicode_value='VerifiedBreak', tag='VerifiedBreak')
phaseStatusKind.NormalOrRestored = phaseStatusKind._CF_enumeration.addEnumeration(unicode_value='NormalOrRestored', tag='NormalOrRestored')
phaseStatusKind.Other = phaseStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
phaseStatusKind._InitializeFacetMap(phaseStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'phaseStatusKind', phaseStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}phoneTypeKind
class phoneTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of phone number."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phoneTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4057, 1)
    _Documentation = 'Type of phone number.'
phoneTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=phoneTypeKind, enum_prefix=None)
phoneTypeKind.Unknown = phoneTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
phoneTypeKind.Home = phoneTypeKind._CF_enumeration.addEnumeration(unicode_value='Home', tag='Home')
phoneTypeKind.Business = phoneTypeKind._CF_enumeration.addEnumeration(unicode_value='Business', tag='Business')
phoneTypeKind.Mobile = phoneTypeKind._CF_enumeration.addEnumeration(unicode_value='Mobile', tag='Mobile')
phoneTypeKind.BusinessMobile = phoneTypeKind._CF_enumeration.addEnumeration(unicode_value='BusinessMobile', tag='BusinessMobile')
phoneTypeKind.Pager = phoneTypeKind._CF_enumeration.addEnumeration(unicode_value='Pager', tag='Pager')
phoneTypeKind.Fax = phoneTypeKind._CF_enumeration.addEnumeration(unicode_value='Fax', tag='Fax')
phoneTypeKind.Other = phoneTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
phoneTypeKind._InitializeFacetMap(phoneTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'phoneTypeKind', phoneTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}pipeSize
class pipeSize (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Pipe size (from ANSI C12.19).
      English           Metric
0- 1/2"                 13 mm
1 - 5/8"                15 mm
2 - 3/4"                20 mm
3 - 1"                   25 mm
4 - 1 1/2"             40 mm
5 - 2"                   50 mm
6 - 3"                   80 mm
7 - 4"                 100 mm
8 - 6"                 160 mm
9 - 8"                 200 mm
10 - 10"             250 mm
11 - 12"             300 mm
12 - 14"             350 mm
13 - 16"             400 mm
14 - 18"             450 mm
15 - 20"             500 mm
16 22"                Not standard 
17 - 24"             600 mm
18 - 26"             Not standard
19 - 28"             Not standard
20 - 30"             Not standard
21 - 32"             800 mm
22 - 34"             Not Standard
23 - 36"             900 mm
24 - 40"            1000 mm
25 - 48"            1200 mm"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pipeSize')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4072, 1)
    _Documentation = 'Pipe size (from ANSI C12.19).\n      English           Metric\n0- 1/2"                 13 mm\n1 - 5/8"                15 mm\n2 - 3/4"                20 mm\n3 - 1"                   25 mm\n4 - 1 1/2"             40 mm\n5 - 2"                   50 mm\n6 - 3"                   80 mm\n7 - 4"                 100 mm\n8 - 6"                 160 mm\n9 - 8"                 200 mm\n10 - 10"             250 mm\n11 - 12"             300 mm\n12 - 14"             350 mm\n13 - 16"             400 mm\n14 - 18"             450 mm\n15 - 20"             500 mm\n16 22"                Not standard \n17 - 24"             600 mm\n18 - 26"             Not standard\n19 - 28"             Not standard\n20 - 30"             Not standard\n21 - 32"             800 mm\n22 - 34"             Not Standard\n23 - 36"             900 mm\n24 - 40"            1000 mm\n25 - 48"            1200 mm'
pipeSize._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=pipeSize, enum_prefix=None)
pipeSize.n0 = pipeSize._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
pipeSize.n1 = pipeSize._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
pipeSize.n2 = pipeSize._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
pipeSize.n3 = pipeSize._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
pipeSize.n4 = pipeSize._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
pipeSize.n5 = pipeSize._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
pipeSize.n6 = pipeSize._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
pipeSize.n7 = pipeSize._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
pipeSize.n8 = pipeSize._CF_enumeration.addEnumeration(unicode_value='8', tag='n8')
pipeSize.n9 = pipeSize._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
pipeSize.n10 = pipeSize._CF_enumeration.addEnumeration(unicode_value='10', tag='n10')
pipeSize.n11 = pipeSize._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
pipeSize.n12 = pipeSize._CF_enumeration.addEnumeration(unicode_value='12', tag='n12')
pipeSize.n13 = pipeSize._CF_enumeration.addEnumeration(unicode_value='13', tag='n13')
pipeSize.n14 = pipeSize._CF_enumeration.addEnumeration(unicode_value='14', tag='n14')
pipeSize.n15 = pipeSize._CF_enumeration.addEnumeration(unicode_value='15', tag='n15')
pipeSize.n16 = pipeSize._CF_enumeration.addEnumeration(unicode_value='16', tag='n16')
pipeSize.n17 = pipeSize._CF_enumeration.addEnumeration(unicode_value='17', tag='n17')
pipeSize.n18 = pipeSize._CF_enumeration.addEnumeration(unicode_value='18', tag='n18')
pipeSize.n19 = pipeSize._CF_enumeration.addEnumeration(unicode_value='19', tag='n19')
pipeSize.n20 = pipeSize._CF_enumeration.addEnumeration(unicode_value='20', tag='n20')
pipeSize.n21 = pipeSize._CF_enumeration.addEnumeration(unicode_value='21', tag='n21')
pipeSize.n22 = pipeSize._CF_enumeration.addEnumeration(unicode_value='22', tag='n22')
pipeSize.n23 = pipeSize._CF_enumeration.addEnumeration(unicode_value='23', tag='n23')
pipeSize.n24 = pipeSize._CF_enumeration.addEnumeration(unicode_value='24', tag='n24')
pipeSize.n25 = pipeSize._CF_enumeration.addEnumeration(unicode_value='25', tag='n25')
pipeSize._InitializeFacetMap(pipeSize._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'pipeSize', pipeSize)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}pmEventCode
class pmEventCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Power monitor event code."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pmEventCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4132, 1)
    _Documentation = 'Power monitor event code.'
pmEventCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=pmEventCode, enum_prefix=None)
pmEventCode.Unknown = pmEventCode._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
pmEventCode.LowBattery = pmEventCode._CF_enumeration.addEnumeration(unicode_value='LowBattery', tag='LowBattery')
pmEventCode.Event1 = pmEventCode._CF_enumeration.addEnumeration(unicode_value='Event1', tag='Event1')
pmEventCode.Event2 = pmEventCode._CF_enumeration.addEnumeration(unicode_value='Event2', tag='Event2')
pmEventCode.Event3 = pmEventCode._CF_enumeration.addEnumeration(unicode_value='Event3', tag='Event3')
pmEventCode.LockOut = pmEventCode._CF_enumeration.addEnumeration(unicode_value='LockOut', tag='LockOut')
pmEventCode.PowerRestored = pmEventCode._CF_enumeration.addEnumeration(unicode_value='PowerRestored', tag='PowerRestored')
pmEventCode.UndeterminedOn = pmEventCode._CF_enumeration.addEnumeration(unicode_value='UndeterminedOn', tag='UndeterminedOn')
pmEventCode.UndeterminedOff = pmEventCode._CF_enumeration.addEnumeration(unicode_value='UndeterminedOff', tag='UndeterminedOff')
pmEventCode.BrownOut = pmEventCode._CF_enumeration.addEnumeration(unicode_value='BrownOut', tag='BrownOut')
pmEventCode.HighVoltage = pmEventCode._CF_enumeration.addEnumeration(unicode_value='HighVoltage', tag='HighVoltage')
pmEventCode.NormalVoltage = pmEventCode._CF_enumeration.addEnumeration(unicode_value='NormalVoltage', tag='NormalVoltage')
pmEventCode.Other = pmEventCode._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
pmEventCode._InitializeFacetMap(pmEventCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'pmEventCode', pmEventCode)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}poleClassKind
class poleClassKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Class of this pole."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'poleClassKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4163, 1)
    _Documentation = 'Class of this pole.'
poleClassKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=poleClassKind, enum_prefix=None)
poleClassKind.Unknown = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
poleClassKind.Class1 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class1', tag='Class1')
poleClassKind.Class2 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class2', tag='Class2')
poleClassKind.Class3 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class3', tag='Class3')
poleClassKind.Class4 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class4', tag='Class4')
poleClassKind.Class5 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class5', tag='Class5')
poleClassKind.Class6 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class6', tag='Class6')
poleClassKind.Class7 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class7', tag='Class7')
poleClassKind.Class8 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class8', tag='Class8')
poleClassKind.Class9 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class9', tag='Class9')
poleClassKind.Class10 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Class10', tag='Class10')
poleClassKind.H1 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='H1', tag='H1')
poleClassKind.H2 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='H2', tag='H2')
poleClassKind.H3 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='H3', tag='H3')
poleClassKind.H4 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='H4', tag='H4')
poleClassKind.H5 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='H5', tag='H5')
poleClassKind.H6 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='H6', tag='H6')
poleClassKind.H7 = poleClassKind._CF_enumeration.addEnumeration(unicode_value='H7', tag='H7')
poleClassKind.Other = poleClassKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
poleClassKind._InitializeFacetMap(poleClassKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'poleClassKind', poleClassKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}poleTypeKind
class poleTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of pole."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'poleTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4205, 1)
    _Documentation = 'Type of pole.'
poleTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=poleTypeKind, enum_prefix=None)
poleTypeKind.Unknown = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
poleTypeKind.Aluminum = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='Aluminum', tag='Aluminum')
poleTypeKind.Concrete = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='Concrete', tag='Concrete')
poleTypeKind.Fiberglass = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='Fiberglass', tag='Fiberglass')
poleTypeKind.Galvanized = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='Galvanized', tag='Galvanized')
poleTypeKind.Steel = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='Steel', tag='Steel')
poleTypeKind.Wood = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='Wood', tag='Wood')
poleTypeKind.WoodTreated = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='WoodTreated', tag='WoodTreated')
poleTypeKind.WoodUntreated = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='WoodUntreated', tag='WoodUntreated')
poleTypeKind.Other = poleTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
poleTypeKind._InitializeFacetMap(poleTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'poleTypeKind', poleTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}poleUseKind
class poleUseKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Use of pole."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'poleUseKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4233, 1)
    _Documentation = 'Use of pole.'
poleUseKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=poleUseKind, enum_prefix=None)
poleUseKind.Unknown = poleUseKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
poleUseKind.Distribution = poleUseKind._CF_enumeration.addEnumeration(unicode_value='Distribution', tag='Distribution')
poleUseKind.Transmission = poleUseKind._CF_enumeration.addEnumeration(unicode_value='Transmission', tag='Transmission')
poleUseKind.Service = poleUseKind._CF_enumeration.addEnumeration(unicode_value='Service', tag='Service')
poleUseKind.Guy_Stub = poleUseKind._CF_enumeration.addEnumeration(unicode_value='Guy Stub', tag='Guy_Stub')
poleUseKind.Stub = poleUseKind._CF_enumeration.addEnumeration(unicode_value='Stub', tag='Stub')
poleUseKind.Other = poleUseKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
poleUseKind._InitializeFacetMap(poleUseKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'poleUseKind', poleUseKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}position
class position (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'position')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4247, 1)
    _Documentation = None
position._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=position, enum_prefix=None)
position.NormallyOpen = position._CF_enumeration.addEnumeration(unicode_value='NormallyOpen', tag='NormallyOpen')
position.NormallyClosed = position._CF_enumeration.addEnumeration(unicode_value='NormallyClosed', tag='NormallyClosed')
position.Unknown = position._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
position._InitializeFacetMap(position._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'position', position)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}powerLimitationUnits
class powerLimitationUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Units for the powerLimitationValue."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'powerLimitationUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4254, 1)
    _Documentation = 'Units for the powerLimitationValue.'
powerLimitationUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=powerLimitationUnits, enum_prefix=None)
powerLimitationUnits.kWh = powerLimitationUnits._CF_enumeration.addEnumeration(unicode_value='kWh', tag='kWh')
powerLimitationUnits.kW = powerLimitationUnits._CF_enumeration.addEnumeration(unicode_value='kW', tag='kW')
powerLimitationUnits.A = powerLimitationUnits._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
powerLimitationUnits._InitializeFacetMap(powerLimitationUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'powerLimitationUnits', powerLimitationUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}powerStatusKind
class powerStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Outage status for this electric service."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'powerStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4275, 1)
    _Documentation = 'Outage status for this electric service.'
powerStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=powerStatusKind, enum_prefix=None)
powerStatusKind.StatusUnknown = powerStatusKind._CF_enumeration.addEnumeration(unicode_value='StatusUnknown', tag='StatusUnknown')
powerStatusKind.PowerOff = powerStatusKind._CF_enumeration.addEnumeration(unicode_value='PowerOff', tag='PowerOff')
powerStatusKind.PowerOn = powerStatusKind._CF_enumeration.addEnumeration(unicode_value='PowerOn', tag='PowerOn')
powerStatusKind.Other = powerStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
powerStatusKind._InitializeFacetMap(powerStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'powerStatusKind', powerStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}premisesDisplayMessageKind
class premisesDisplayMessageKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'premisesDisplayMessageKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4286, 1)
    _Documentation = None
premisesDisplayMessageKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=premisesDisplayMessageKind, enum_prefix=None)
premisesDisplayMessageKind.Unknown = premisesDisplayMessageKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
premisesDisplayMessageKind.BillingMessage = premisesDisplayMessageKind._CF_enumeration.addEnumeration(unicode_value='BillingMessage', tag='BillingMessage')
premisesDisplayMessageKind.Message = premisesDisplayMessageKind._CF_enumeration.addEnumeration(unicode_value='Message', tag='Message')
premisesDisplayMessageKind.Other = premisesDisplayMessageKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
premisesDisplayMessageKind._InitializeFacetMap(premisesDisplayMessageKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'premisesDisplayMessageKind', premisesDisplayMessageKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}premisesDisplayMessageStatusKind
class premisesDisplayMessageStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'premisesDisplayMessageStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4294, 1)
    _Documentation = None
premisesDisplayMessageStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=premisesDisplayMessageStatusKind, enum_prefix=None)
premisesDisplayMessageStatusKind.Unknown = premisesDisplayMessageStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
premisesDisplayMessageStatusKind.Accepted = premisesDisplayMessageStatusKind._CF_enumeration.addEnumeration(unicode_value='Accepted', tag='Accepted')
premisesDisplayMessageStatusKind.Cancelled = premisesDisplayMessageStatusKind._CF_enumeration.addEnumeration(unicode_value='Cancelled', tag='Cancelled')
premisesDisplayMessageStatusKind.Displayed = premisesDisplayMessageStatusKind._CF_enumeration.addEnumeration(unicode_value='Displayed', tag='Displayed')
premisesDisplayMessageStatusKind.Off = premisesDisplayMessageStatusKind._CF_enumeration.addEnumeration(unicode_value='Off', tag='Off')
premisesDisplayMessageStatusKind.Expired = premisesDisplayMessageStatusKind._CF_enumeration.addEnumeration(unicode_value='Expired', tag='Expired')
premisesDisplayMessageStatusKind.Other = premisesDisplayMessageStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
premisesDisplayMessageStatusKind._InitializeFacetMap(premisesDisplayMessageStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'premisesDisplayMessageStatusKind', premisesDisplayMessageStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}pressureCompensationType
class pressureCompensationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Gas meter pressure compensation type code from ANSI C12.19:

0 - Uncompensated
1 - Mechanical
2 - Sensor"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pressureCompensationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4347, 1)
    _Documentation = 'Gas meter pressure compensation type code from ANSI C12.19:\n\n0 - Uncompensated\n1 - Mechanical\n2 - Sensor'
pressureCompensationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=pressureCompensationType, enum_prefix=None)
pressureCompensationType.n0 = pressureCompensationType._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
pressureCompensationType.n1 = pressureCompensationType._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
pressureCompensationType.n2 = pressureCompensationType._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
pressureCompensationType._InitializeFacetMap(pressureCompensationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'pressureCompensationType', pressureCompensationType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}pressureUnits
class pressureUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pressureUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4361, 1)
    _Documentation = None
pressureUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=pressureUnits, enum_prefix=None)
pressureUnits.Unknown = pressureUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
pressureUnits.Pascal = pressureUnits._CF_enumeration.addEnumeration(unicode_value='Pascal', tag='Pascal')
pressureUnits.NewtonPerSquareMeter = pressureUnits._CF_enumeration.addEnumeration(unicode_value='NewtonPerSquareMeter', tag='NewtonPerSquareMeter')
pressureUnits.PSI = pressureUnits._CF_enumeration.addEnumeration(unicode_value='PSI', tag='PSI')
pressureUnits.Bar = pressureUnits._CF_enumeration.addEnumeration(unicode_value='Bar', tag='Bar')
pressureUnits.Barye = pressureUnits._CF_enumeration.addEnumeration(unicode_value='Barye', tag='Barye')
pressureUnits.Atmosphere = pressureUnits._CF_enumeration.addEnumeration(unicode_value='Atmosphere', tag='Atmosphere')
pressureUnits.Millibar = pressureUnits._CF_enumeration.addEnumeration(unicode_value='Millibar', tag='Millibar')
pressureUnits.InchOfHg = pressureUnits._CF_enumeration.addEnumeration(unicode_value='InchOfHg', tag='InchOfHg')
pressureUnits.MillimeterOfHg = pressureUnits._CF_enumeration.addEnumeration(unicode_value='MillimeterOfHg', tag='MillimeterOfHg')
pressureUnits.InchOfWater = pressureUnits._CF_enumeration.addEnumeration(unicode_value='InchOfWater', tag='InchOfWater')
pressureUnits.MillimeterOfWater = pressureUnits._CF_enumeration.addEnumeration(unicode_value='MillimeterOfWater', tag='MillimeterOfWater')
pressureUnits.Kip = pressureUnits._CF_enumeration.addEnumeration(unicode_value='Kip', tag='Kip')
pressureUnits.PoundForce = pressureUnits._CF_enumeration.addEnumeration(unicode_value='PoundForce', tag='PoundForce')
pressureUnits.Other = pressureUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
pressureUnits._InitializeFacetMap(pressureUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'pressureUnits', pressureUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}presumedElementStateKind
class presumedElementStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'presumedElementStateKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4380, 1)
    _Documentation = None
presumedElementStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=presumedElementStateKind, enum_prefix=None)
presumedElementStateKind.Unknown = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
presumedElementStateKind.PossibleBreak = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='PossibleBreak', tag='PossibleBreak')
presumedElementStateKind.PossibleClosed = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='PossibleClosed', tag='PossibleClosed')
presumedElementStateKind.PossibleOpen = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='PossibleOpen', tag='PossibleOpen')
presumedElementStateKind.PredictedBreak = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='PredictedBreak', tag='PredictedBreak')
presumedElementStateKind.PredictedClosed = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='PredictedClosed', tag='PredictedClosed')
presumedElementStateKind.PredictedOpen = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='PredictedOpen', tag='PredictedOpen')
presumedElementStateKind.TempBreak = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='TempBreak', tag='TempBreak')
presumedElementStateKind.TempClosed = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='TempClosed', tag='TempClosed')
presumedElementStateKind.TempOpen = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='TempOpen', tag='TempOpen')
presumedElementStateKind.UplinePredictedOpen = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='UplinePredictedOpen', tag='UplinePredictedOpen')
presumedElementStateKind.UplineTempBreak = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='UplineTempBreak', tag='UplineTempBreak')
presumedElementStateKind.UplineTempClosed = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='UplineTempClosed', tag='UplineTempClosed')
presumedElementStateKind.UplineTempOpen = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='UplineTempOpen', tag='UplineTempOpen')
presumedElementStateKind.UplineVerifiedClosedNoPower = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='UplineVerifiedClosedNoPower', tag='UplineVerifiedClosedNoPower')
presumedElementStateKind.VerifiedBreak = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='VerifiedBreak', tag='VerifiedBreak')
presumedElementStateKind.VerifiedClosedNoPower = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='VerifiedClosedNoPower', tag='VerifiedClosedNoPower')
presumedElementStateKind.VerifiedClosedWithPower = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='VerifiedClosedWithPower', tag='VerifiedClosedWithPower')
presumedElementStateKind.VerifiedOpen = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='VerifiedOpen', tag='VerifiedOpen')
presumedElementStateKind.NormalOrRestored = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='NormalOrRestored', tag='NormalOrRestored')
presumedElementStateKind.NoChange = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='NoChange', tag='NoChange')
presumedElementStateKind.Other = presumedElementStateKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
presumedElementStateKind._InitializeFacetMap(presumedElementStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'presumedElementStateKind', presumedElementStateKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}priorityType
class priorityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Designation of importance level of this event."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'priorityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4417, 1)
    _Documentation = 'Designation of importance level of this event.'
priorityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=priorityType, enum_prefix=None)
priorityType.Unknown = priorityType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
priorityType.Normal = priorityType._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
priorityType.NeedsAttention = priorityType._CF_enumeration.addEnumeration(unicode_value='NeedsAttention', tag='NeedsAttention')
priorityType.Urgent = priorityType._CF_enumeration.addEnumeration(unicode_value='Urgent', tag='Urgent')
priorityType.Other = priorityType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
priorityType._InitializeFacetMap(priorityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'priorityType', priorityType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}PTOStateKind
class PTOStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """State of the vehicle power take-off unit, if any."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PTOStateKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4440, 1)
    _Documentation = 'State of the vehicle power take-off unit, if any.'
PTOStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PTOStateKind, enum_prefix=None)
PTOStateKind.Unknown = PTOStateKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
PTOStateKind.On = PTOStateKind._CF_enumeration.addEnumeration(unicode_value='On', tag='On')
PTOStateKind.Off = PTOStateKind._CF_enumeration.addEnumeration(unicode_value='Off', tag='Off')
PTOStateKind.None_ = PTOStateKind._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
PTOStateKind.Other = PTOStateKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
PTOStateKind._InitializeFacetMap(PTOStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PTOStateKind', PTOStateKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}qualityDescriptionKind
class qualityDescriptionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'qualityDescriptionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4463, 1)
    _Documentation = None
qualityDescriptionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=qualityDescriptionKind, enum_prefix=None)
qualityDescriptionKind.Unknown = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
qualityDescriptionKind.Measured = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='Measured', tag='Measured')
qualityDescriptionKind.Default = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='Default', tag='Default')
qualityDescriptionKind.Estimated = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='Estimated', tag='Estimated')
qualityDescriptionKind.Calculated = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='Calculated', tag='Calculated')
qualityDescriptionKind.Initial = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='Initial', tag='Initial')
qualityDescriptionKind.Last = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='Last', tag='Last')
qualityDescriptionKind.Failed = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='Failed', tag='Failed')
qualityDescriptionKind.ScanInhibited = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='ScanInhibited', tag='ScanInhibited')
qualityDescriptionKind.OldData = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='OldData', tag='OldData')
qualityDescriptionKind.AlarmInhibited = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='AlarmInhibited', tag='AlarmInhibited')
qualityDescriptionKind.Other = qualityDescriptionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
qualityDescriptionKind._InitializeFacetMap(qualityDescriptionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'qualityDescriptionKind', qualityDescriptionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}quantityType
class quantityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'quantityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4479, 1)
    _Documentation = None
quantityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=quantityType, enum_prefix=None)
quantityType.summation = quantityType._CF_enumeration.addEnumeration(unicode_value='summation', tag='summation')
quantityType.demand = quantityType._CF_enumeration.addEnumeration(unicode_value='demand', tag='demand')
quantityType.consumption = quantityType._CF_enumeration.addEnumeration(unicode_value='consumption', tag='consumption')
quantityType.value = quantityType._CF_enumeration.addEnumeration(unicode_value='value', tag='value')
quantityType._InitializeFacetMap(quantityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'quantityType', quantityType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}RCDStateKind
class RCDStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The current state of this remote connect/disconnect device (CDDevice)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RCDStateKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4498, 1)
    _Documentation = 'The current state of this remote connect/disconnect device (CDDevice).'
RCDStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RCDStateKind, enum_prefix=None)
RCDStateKind.Unknown = RCDStateKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
RCDStateKind.Connected = RCDStateKind._CF_enumeration.addEnumeration(unicode_value='Connected', tag='Connected')
RCDStateKind.Disconnected = RCDStateKind._CF_enumeration.addEnumeration(unicode_value='Disconnected', tag='Disconnected')
RCDStateKind.Armed = RCDStateKind._CF_enumeration.addEnumeration(unicode_value='Armed', tag='Armed')
RCDStateKind.Enabled = RCDStateKind._CF_enumeration.addEnumeration(unicode_value='Enabled', tag='Enabled')
RCDStateKind.Disabled = RCDStateKind._CF_enumeration.addEnumeration(unicode_value='Disabled', tag='Disabled')
RCDStateKind.InTransition = RCDStateKind._CF_enumeration.addEnumeration(unicode_value='InTransition', tag='InTransition')
RCDStateKind.PowerLimitation = RCDStateKind._CF_enumeration.addEnumeration(unicode_value='PowerLimitation', tag='PowerLimitation')
RCDStateKind.Other = RCDStateKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
RCDStateKind._InitializeFacetMap(RCDStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RCDStateKind', RCDStateKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}reactiveEnergyUnits
class reactiveEnergyUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reactiveEnergyUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4522, 1)
    _Documentation = None
reactiveEnergyUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=reactiveEnergyUnits, enum_prefix=None)
reactiveEnergyUnits.Unknown = reactiveEnergyUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
reactiveEnergyUnits.VArh = reactiveEnergyUnits._CF_enumeration.addEnumeration(unicode_value='VArh', tag='VArh')
reactiveEnergyUnits.KVArh = reactiveEnergyUnits._CF_enumeration.addEnumeration(unicode_value='KVArh', tag='KVArh')
reactiveEnergyUnits.MVArh = reactiveEnergyUnits._CF_enumeration.addEnumeration(unicode_value='MVArh', tag='MVArh')
reactiveEnergyUnits.GVArh = reactiveEnergyUnits._CF_enumeration.addEnumeration(unicode_value='GVArh', tag='GVArh')
reactiveEnergyUnits.mVArh = reactiveEnergyUnits._CF_enumeration.addEnumeration(unicode_value='mVArh', tag='mVArh')
reactiveEnergyUnits.microVArh = reactiveEnergyUnits._CF_enumeration.addEnumeration(unicode_value='microVArh', tag='microVArh')
reactiveEnergyUnits.Other = reactiveEnergyUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
reactiveEnergyUnits._InitializeFacetMap(reactiveEnergyUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'reactiveEnergyUnits', reactiveEnergyUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}reactivePowerUnits
class reactivePowerUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reactivePowerUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4534, 1)
    _Documentation = None
reactivePowerUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=reactivePowerUnits, enum_prefix=None)
reactivePowerUnits.Unknown = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
reactivePowerUnits.mVAr = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='mVAr', tag='mVAr')
reactivePowerUnits.VAr = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='VAr', tag='VAr')
reactivePowerUnits.kVAr = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='kVAr', tag='kVAr')
reactivePowerUnits.MVAr = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='MVAr', tag='MVAr')
reactivePowerUnits.GVAr = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='GVAr', tag='GVAr')
reactivePowerUnits.microVAr = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='microVAr', tag='microVAr')
reactivePowerUnits.PerUnit = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='PerUnit', tag='PerUnit')
reactivePowerUnits.Percent = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='Percent', tag='Percent')
reactivePowerUnits.Other = reactivePowerUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
reactivePowerUnits._InitializeFacetMap(reactivePowerUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'reactivePowerUnits', reactivePowerUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}readingSchedulingResult
class readingSchedulingResult (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'readingSchedulingResult')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4548, 1)
    _Documentation = None
readingSchedulingResult._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=readingSchedulingResult, enum_prefix=None)
readingSchedulingResult.Accepted = readingSchedulingResult._CF_enumeration.addEnumeration(unicode_value='Accepted', tag='Accepted')
readingSchedulingResult.Rejected = readingSchedulingResult._CF_enumeration.addEnumeration(unicode_value='Rejected', tag='Rejected')
readingSchedulingResult.RejectedInPart = readingSchedulingResult._CF_enumeration.addEnumeration(unicode_value='RejectedInPart', tag='RejectedInPart')
readingSchedulingResult.Other = readingSchedulingResult._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
readingSchedulingResult._InitializeFacetMap(readingSchedulingResult._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'readingSchedulingResult', readingSchedulingResult)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}readingStatus
class readingStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This is the meter reading status as defined by ANSI C12.19."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'readingStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4556, 1)
    _Documentation = 'This is the meter reading status as defined by ANSI C12.19.'
readingStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=readingStatus, enum_prefix=None)
readingStatus.Other = readingStatus._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
readingStatus.suspiciousRead = readingStatus._CF_enumeration.addEnumeration(unicode_value='suspiciousRead', tag='suspiciousRead')
readingStatus.DSTinEffect = readingStatus._CF_enumeration.addEnumeration(unicode_value='DSTinEffect', tag='DSTinEffect')
readingStatus.manuallyUpdated = readingStatus._CF_enumeration.addEnumeration(unicode_value='manuallyUpdated', tag='manuallyUpdated')
readingStatus.manuallyEntered = readingStatus._CF_enumeration.addEnumeration(unicode_value='manuallyEntered', tag='manuallyEntered')
readingStatus.reset = readingStatus._CF_enumeration.addEnumeration(unicode_value='reset', tag='reset')
readingStatus.seasonChange = readingStatus._CF_enumeration.addEnumeration(unicode_value='seasonChange', tag='seasonChange')
readingStatus.firstRead = readingStatus._CF_enumeration.addEnumeration(unicode_value='firstRead', tag='firstRead')
readingStatus.billingRead = readingStatus._CF_enumeration.addEnumeration(unicode_value='billingRead', tag='billingRead')
readingStatus.afterCorrection = readingStatus._CF_enumeration.addEnumeration(unicode_value='afterCorrection', tag='afterCorrection')
readingStatus.beforeCorrection = readingStatus._CF_enumeration.addEnumeration(unicode_value='beforeCorrection', tag='beforeCorrection')
readingStatus.finalRead = readingStatus._CF_enumeration.addEnumeration(unicode_value='finalRead', tag='finalRead')
readingStatus._InitializeFacetMap(readingStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'readingStatus', readingStatus)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}realEnergyUnits
class realEnergyUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'realEnergyUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4575, 1)
    _Documentation = None
realEnergyUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=realEnergyUnits, enum_prefix=None)
realEnergyUnits.Unknown = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
realEnergyUnits.Wh = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='Wh', tag='Wh')
realEnergyUnits.kWh = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='kWh', tag='kWh')
realEnergyUnits.MWh = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='MWh', tag='MWh')
realEnergyUnits.GWh = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='GWh', tag='GWh')
realEnergyUnits.mWh = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='mWh', tag='mWh')
realEnergyUnits.microWh = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='microWh', tag='microWh')
realEnergyUnits.TWh = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='TWh', tag='TWh')
realEnergyUnits.PWh = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='PWh', tag='PWh')
realEnergyUnits.BTU = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='BTU', tag='BTU')
realEnergyUnits.Therrm = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='Therrm', tag='Therrm')
realEnergyUnits.Erg = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='Erg', tag='Erg')
realEnergyUnits.Calorie = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='Calorie', tag='Calorie')
realEnergyUnits.eV = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='eV', tag='eV')
realEnergyUnits.Joule = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='Joule', tag='Joule')
realEnergyUnits.Other = realEnergyUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
realEnergyUnits._InitializeFacetMap(realEnergyUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'realEnergyUnits', realEnergyUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}realPowerUnits
class realPowerUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'realPowerUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4595, 1)
    _Documentation = None
realPowerUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=realPowerUnits, enum_prefix=None)
realPowerUnits.Unknown = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
realPowerUnits.W = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
realPowerUnits.kW = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='kW', tag='kW')
realPowerUnits.MW = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
realPowerUnits.GW = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
realPowerUnits.mW = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='mW', tag='mW')
realPowerUnits.microW = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='microW', tag='microW')
realPowerUnits.PerUnit = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='PerUnit', tag='PerUnit')
realPowerUnits.Percent = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='Percent', tag='Percent')
realPowerUnits.Other = realPowerUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
realPowerUnits._InitializeFacetMap(realPowerUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'realPowerUnits', realPowerUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}receivableKind
class receivableKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The type of accounts receivable."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'receivableKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4609, 1)
    _Documentation = 'The type of accounts receivable.'
receivableKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=receivableKind, enum_prefix=None)
receivableKind.Other = receivableKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
receivableKind.Current = receivableKind._CF_enumeration.addEnumeration(unicode_value='Current', tag='Current')
receivableKind.Balance = receivableKind._CF_enumeration.addEnumeration(unicode_value='Balance', tag='Balance')
receivableKind.n30 = receivableKind._CF_enumeration.addEnumeration(unicode_value='30', tag='n30')
receivableKind.n60 = receivableKind._CF_enumeration.addEnumeration(unicode_value='60', tag='n60')
receivableKind.n90 = receivableKind._CF_enumeration.addEnumeration(unicode_value='90', tag='n90')
receivableKind.CutOffAmount = receivableKind._CF_enumeration.addEnumeration(unicode_value='CutOffAmount', tag='CutOffAmount')
receivableKind.AmountToCollect = receivableKind._CF_enumeration.addEnumeration(unicode_value='AmountToCollect', tag='AmountToCollect')
receivableKind._InitializeFacetMap(receivableKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'receivableKind', receivableKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}recurringPaymentAuthorizationModeKind
class recurringPaymentAuthorizationModeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The means by which the recurring payment authorization was received."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'recurringPaymentAuthorizationModeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4632, 1)
    _Documentation = 'The means by which the recurring payment authorization was received.'
recurringPaymentAuthorizationModeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=recurringPaymentAuthorizationModeKind, enum_prefix=None)
recurringPaymentAuthorizationModeKind.Web = recurringPaymentAuthorizationModeKind._CF_enumeration.addEnumeration(unicode_value='Web', tag='Web')
recurringPaymentAuthorizationModeKind.Phone = recurringPaymentAuthorizationModeKind._CF_enumeration.addEnumeration(unicode_value='Phone', tag='Phone')
recurringPaymentAuthorizationModeKind.Paper = recurringPaymentAuthorizationModeKind._CF_enumeration.addEnumeration(unicode_value='Paper', tag='Paper')
recurringPaymentAuthorizationModeKind.Other = recurringPaymentAuthorizationModeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
recurringPaymentAuthorizationModeKind._InitializeFacetMap(recurringPaymentAuthorizationModeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'recurringPaymentAuthorizationModeKind', recurringPaymentAuthorizationModeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}regulatorBankConnectionKind
class regulatorBankConnectionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Connection for this bank of regulators."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'regulatorBankConnectionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4654, 1)
    _Documentation = 'Connection for this bank of regulators.'
regulatorBankConnectionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=regulatorBankConnectionKind, enum_prefix=None)
regulatorBankConnectionKind.Uknown = regulatorBankConnectionKind._CF_enumeration.addEnumeration(unicode_value='Uknown', tag='Uknown')
regulatorBankConnectionKind.Wye3Ph = regulatorBankConnectionKind._CF_enumeration.addEnumeration(unicode_value='Wye3Ph', tag='Wye3Ph')
regulatorBankConnectionKind.Delta3Ph = regulatorBankConnectionKind._CF_enumeration.addEnumeration(unicode_value='Delta3Ph', tag='Delta3Ph')
regulatorBankConnectionKind.LineNeutral = regulatorBankConnectionKind._CF_enumeration.addEnumeration(unicode_value='LineNeutral', tag='LineNeutral')
regulatorBankConnectionKind.OpenDelta = regulatorBankConnectionKind._CF_enumeration.addEnumeration(unicode_value='OpenDelta', tag='OpenDelta')
regulatorBankConnectionKind.ClosedDelta = regulatorBankConnectionKind._CF_enumeration.addEnumeration(unicode_value='ClosedDelta', tag='ClosedDelta')
regulatorBankConnectionKind.Other = regulatorBankConnectionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
regulatorBankConnectionKind._InitializeFacetMap(regulatorBankConnectionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'regulatorBankConnectionKind', regulatorBankConnectionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}regulatorWindingType
class regulatorWindingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The regulator winding type (A,B)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'regulatorWindingType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4668, 1)
    _Documentation = 'The regulator winding type (A,B).'
regulatorWindingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=regulatorWindingType, enum_prefix=None)
regulatorWindingType.A = regulatorWindingType._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
regulatorWindingType.B = regulatorWindingType._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
regulatorWindingType.Unknown = regulatorWindingType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
regulatorWindingType._InitializeFacetMap(regulatorWindingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'regulatorWindingType', regulatorWindingType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}relationTypeKind
class relationTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relationTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4689, 1)
    _Documentation = None
relationTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=relationTypeKind, enum_prefix=None)
relationTypeKind.Child = relationTypeKind._CF_enumeration.addEnumeration(unicode_value='Child', tag='Child')
relationTypeKind.Parent = relationTypeKind._CF_enumeration.addEnumeration(unicode_value='Parent', tag='Parent')
relationTypeKind.Sibling = relationTypeKind._CF_enumeration.addEnumeration(unicode_value='Sibling', tag='Sibling')
relationTypeKind.Other = relationTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
relationTypeKind._InitializeFacetMap(relationTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'relationTypeKind', relationTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}relayKind
class relayKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This element carries a parameter to describe the action to be taken.  The enumeration is: normal, trip and close."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relayKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4697, 1)
    _Documentation = 'This element carries a parameter to describe the action to be taken.  The enumeration is: normal, trip and close.'
relayKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=relayKind, enum_prefix=None)
relayKind.Normal = relayKind._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
relayKind.Trip = relayKind._CF_enumeration.addEnumeration(unicode_value='Trip', tag='Trip')
relayKind.Close = relayKind._CF_enumeration.addEnumeration(unicode_value='Close', tag='Close')
relayKind.Other = relayKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
relayKind._InitializeFacetMap(relayKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'relayKind', relayKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}replyCodeCategoryKind
class replyCodeCategoryKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """It is suggested that the values of replyCode be chosen from those values included in IEC 61968-9, 2nd Ed., Annex B as extended by Appendix A of "Security in MultiSpeak-Enabled Applications: Requirements".  Values of replyCode SHOULD be of the form [category] "." [index]."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'replyCodeCategoryKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4733, 1)
    _Documentation = 'It is suggested that the values of replyCode be chosen from those values included in IEC 61968-9, 2nd Ed., Annex B as extended by Appendix A of "Security in MultiSpeak-Enabled Applications: Requirements".  Values of replyCode SHOULD be of the form [category] "." [index].'
replyCodeCategoryKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=replyCodeCategoryKind, enum_prefix=None)
replyCodeCategoryKind.n0 = replyCodeCategoryKind._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
replyCodeCategoryKind.n1 = replyCodeCategoryKind._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
replyCodeCategoryKind.n2 = replyCodeCategoryKind._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
replyCodeCategoryKind.n3 = replyCodeCategoryKind._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
replyCodeCategoryKind.n4 = replyCodeCategoryKind._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
replyCodeCategoryKind.n5 = replyCodeCategoryKind._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
replyCodeCategoryKind.n6 = replyCodeCategoryKind._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
replyCodeCategoryKind.n7 = replyCodeCategoryKind._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
replyCodeCategoryKind.Other = replyCodeCategoryKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
replyCodeCategoryKind._InitializeFacetMap(replyCodeCategoryKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'replyCodeCategoryKind', replyCodeCategoryKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}requestByType
class requestByType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This element indicates the type schedule request.  On means schedule this work to be done at the time indicateded in the requestedByValue element. Before and after are interptreted similarly; Immediate indicates that the work should be done as soon as possible."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'requestByType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4781, 1)
    _Documentation = 'This element indicates the type schedule request.  On means schedule this work to be done at the time indicateded in the requestedByValue element. Before and after are interptreted similarly; Immediate indicates that the work should be done as soon as possible.'
requestByType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=requestByType, enum_prefix=None)
requestByType.Before = requestByType._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
requestByType.On = requestByType._CF_enumeration.addEnumeration(unicode_value='On', tag='On')
requestByType.After = requestByType._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
requestByType.Immediate = requestByType._CF_enumeration.addEnumeration(unicode_value='Immediate', tag='Immediate')
requestByType.Other = requestByType._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
requestByType._InitializeFacetMap(requestByType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'requestByType', requestByType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}requestedAccumulationModeKind
class requestedAccumulationModeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'requestedAccumulationModeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4807, 1)
    _Documentation = None
requestedAccumulationModeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=requestedAccumulationModeKind, enum_prefix=None)
requestedAccumulationModeKind.Unknown = requestedAccumulationModeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
requestedAccumulationModeKind.AccumulatedStatus = requestedAccumulationModeKind._CF_enumeration.addEnumeration(unicode_value='AccumulatedStatus', tag='AccumulatedStatus')
requestedAccumulationModeKind.IndividualDevices = requestedAccumulationModeKind._CF_enumeration.addEnumeration(unicode_value='IndividualDevices', tag='IndividualDevices')
requestedAccumulationModeKind.Other = requestedAccumulationModeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
requestedAccumulationModeKind._InitializeFacetMap(requestedAccumulationModeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'requestedAccumulationModeKind', requestedAccumulationModeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}requestedNumberKind
class requestedNumberKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'requestedNumberKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4815, 1)
    _Documentation = None
requestedNumberKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=requestedNumberKind, enum_prefix=None)
requestedNumberKind.Unknown = requestedNumberKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
requestedNumberKind.ServiceOrder = requestedNumberKind._CF_enumeration.addEnumeration(unicode_value='ServiceOrder', tag='ServiceOrder')
requestedNumberKind.WorkOrder = requestedNumberKind._CF_enumeration.addEnumeration(unicode_value='WorkOrder', tag='WorkOrder')
requestedNumberKind.Other = requestedNumberKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
requestedNumberKind._InitializeFacetMap(requestedNumberKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'requestedNumberKind', requestedNumberKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}resistivityUnits
class resistivityUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resistivityUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4834, 1)
    _Documentation = None
resistivityUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=resistivityUnits, enum_prefix=None)
resistivityUnits.Unknown = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
resistivityUnits.OhmMeter = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='OhmMeter', tag='OhmMeter')
resistivityUnits.OhmInch = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='OhmInch', tag='OhmInch')
resistivityUnits.OhmCentimeter = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='OhmCentimeter', tag='OhmCentimeter')
resistivityUnits.MicroOhmCentimeter = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='MicroOhmCentimeter', tag='MicroOhmCentimeter')
resistivityUnits.MicroOhmInch = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='MicroOhmInch', tag='MicroOhmInch')
resistivityUnits.StatOhmCentimeter = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='StatOhmCentimeter', tag='StatOhmCentimeter')
resistivityUnits.AbOhmCentimeterCircular = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='AbOhmCentimeterCircular', tag='AbOhmCentimeterCircular')
resistivityUnits.CircularMilOhmPerFoot = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='CircularMilOhmPerFoot', tag='CircularMilOhmPerFoot')
resistivityUnits.Other = resistivityUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
resistivityUnits._InitializeFacetMap(resistivityUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'resistivityUnits', resistivityUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}resolvedLevelKind
class resolvedLevelKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Indicates if this call was resolved to a specific meter or address."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resolvedLevelKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4859, 1)
    _Documentation = 'Indicates if this call was resolved to a specific meter or address.'
resolvedLevelKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=resolvedLevelKind, enum_prefix=None)
resolvedLevelKind.Unknown = resolvedLevelKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
resolvedLevelKind.Meter = resolvedLevelKind._CF_enumeration.addEnumeration(unicode_value='Meter', tag='Meter')
resolvedLevelKind.Address = resolvedLevelKind._CF_enumeration.addEnumeration(unicode_value='Address', tag='Address')
resolvedLevelKind.Unresolved = resolvedLevelKind._CF_enumeration.addEnumeration(unicode_value='Unresolved', tag='Unresolved')
resolvedLevelKind.Other = resolvedLevelKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
resolvedLevelKind._InitializeFacetMap(resolvedLevelKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'resolvedLevelKind', resolvedLevelKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}resourceStateKind
class resourceStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resourceStateKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4882, 1)
    _Documentation = None
resourceStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=resourceStateKind, enum_prefix=None)
resourceStateKind.Unknown = resourceStateKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
resourceStateKind.Dispatched = resourceStateKind._CF_enumeration.addEnumeration(unicode_value='Dispatched', tag='Dispatched')
resourceStateKind.Acknowledged = resourceStateKind._CF_enumeration.addEnumeration(unicode_value='Acknowledged', tag='Acknowledged')
resourceStateKind.Enroute = resourceStateKind._CF_enumeration.addEnumeration(unicode_value='Enroute', tag='Enroute')
resourceStateKind.OnSite = resourceStateKind._CF_enumeration.addEnumeration(unicode_value='OnSite', tag='OnSite')
resourceStateKind.Other = resourceStateKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
resourceStateKind._InitializeFacetMap(resourceStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'resourceStateKind', resourceStateKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}responseCodeKind
class responseCodeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'responseCodeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4927, 1)
    _Documentation = None
responseCodeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=responseCodeKind, enum_prefix=None)
responseCodeKind.Success = responseCodeKind._CF_enumeration.addEnumeration(unicode_value='Success', tag='Success')
responseCodeKind.Failure = responseCodeKind._CF_enumeration.addEnumeration(unicode_value='Failure', tag='Failure')
responseCodeKind.Error = responseCodeKind._CF_enumeration.addEnumeration(unicode_value='Error', tag='Error')
responseCodeKind.Other = responseCodeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
responseCodeKind._InitializeFacetMap(responseCodeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'responseCodeKind', responseCodeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}resultsKind
class resultsKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of analysis for which results are given (load flow,  short circuit, other )"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resultsKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4935, 1)
    _Documentation = 'Type of analysis for which results are given (load flow,  short circuit, other )'
resultsKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=resultsKind, enum_prefix=None)
resultsKind.LoadFlow = resultsKind._CF_enumeration.addEnumeration(unicode_value='LoadFlow', tag='LoadFlow')
resultsKind.ShortCircuit = resultsKind._CF_enumeration.addEnumeration(unicode_value='ShortCircuit', tag='ShortCircuit')
resultsKind.Other = resultsKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
resultsKind._InitializeFacetMap(resultsKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'resultsKind', resultsKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}SCADAFunctionKind
class SCADAFunctionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SCADAFunctionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4967, 1)
    _Documentation = None
SCADAFunctionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SCADAFunctionKind, enum_prefix=None)
SCADAFunctionKind.Select = SCADAFunctionKind._CF_enumeration.addEnumeration(unicode_value='Select', tag='Select')
SCADAFunctionKind.Operate = SCADAFunctionKind._CF_enumeration.addEnumeration(unicode_value='Operate', tag='Operate')
SCADAFunctionKind.Direct_operate = SCADAFunctionKind._CF_enumeration.addEnumeration(unicode_value='Direct operate', tag='Direct_operate')
SCADAFunctionKind.Other = SCADAFunctionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
SCADAFunctionKind._InitializeFacetMap(SCADAFunctionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SCADAFunctionKind', SCADAFunctionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}SCADAPointKind
class SCADAPointKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of SCADA point."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SCADAPointKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4975, 1)
    _Documentation = 'Type of SCADA point.'
SCADAPointKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SCADAPointKind, enum_prefix=None)
SCADAPointKind.Status = SCADAPointKind._CF_enumeration.addEnumeration(unicode_value='Status', tag='Status')
SCADAPointKind.Analog = SCADAPointKind._CF_enumeration.addEnumeration(unicode_value='Analog', tag='Analog')
SCADAPointKind.Accumulator = SCADAPointKind._CF_enumeration.addEnumeration(unicode_value='Accumulator', tag='Accumulator')
SCADAPointKind.Other = SCADAPointKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
SCADAPointKind._InitializeFacetMap(SCADAPointKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SCADAPointKind', SCADAPointKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}serviceKind
class serviceKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The type of utility service."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4997, 1)
    _Documentation = 'The type of utility service.'
serviceKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=serviceKind, enum_prefix=None)
serviceKind.Unknown = serviceKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
serviceKind.Electric = serviceKind._CF_enumeration.addEnumeration(unicode_value='Electric', tag='Electric')
serviceKind.Gas = serviceKind._CF_enumeration.addEnumeration(unicode_value='Gas', tag='Gas')
serviceKind.Water = serviceKind._CF_enumeration.addEnumeration(unicode_value='Water', tag='Water')
serviceKind.Propane = serviceKind._CF_enumeration.addEnumeration(unicode_value='Propane', tag='Propane')
serviceKind.Refuse = serviceKind._CF_enumeration.addEnumeration(unicode_value='Refuse', tag='Refuse')
serviceKind.Sewer = serviceKind._CF_enumeration.addEnumeration(unicode_value='Sewer', tag='Sewer')
serviceKind.Telecom = serviceKind._CF_enumeration.addEnumeration(unicode_value='Telecom', tag='Telecom')
serviceKind.TV = serviceKind._CF_enumeration.addEnumeration(unicode_value='TV', tag='TV')
serviceKind.Cable = serviceKind._CF_enumeration.addEnumeration(unicode_value='Cable', tag='Cable')
serviceKind.Heating = serviceKind._CF_enumeration.addEnumeration(unicode_value='Heating', tag='Heating')
serviceKind.Steam = serviceKind._CF_enumeration.addEnumeration(unicode_value='Steam', tag='Steam')
serviceKind.Transportation = serviceKind._CF_enumeration.addEnumeration(unicode_value='Transportation', tag='Transportation')
serviceKind.Internet = serviceKind._CF_enumeration.addEnumeration(unicode_value='Internet', tag='Internet')
serviceKind.All = serviceKind._CF_enumeration.addEnumeration(unicode_value='All', tag='All')
serviceKind.Other = serviceKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
serviceKind._InitializeFacetMap(serviceKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'serviceKind', serviceKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}servicePriorityKind
class servicePriorityKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This enumeration establishes categories for service priority (sometimes called special needs).  Additional information may be given in the prioritySubtype."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'servicePriorityKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5026, 1)
    _Documentation = 'This enumeration establishes categories for service priority (sometimes called special needs).  Additional information may be given in the prioritySubtype.'
servicePriorityKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=servicePriorityKind, enum_prefix=None)
servicePriorityKind.Unknown = servicePriorityKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
servicePriorityKind.OutagePriority = servicePriorityKind._CF_enumeration.addEnumeration(unicode_value='OutagePriority', tag='OutagePriority')
servicePriorityKind.PriorityCustomer = servicePriorityKind._CF_enumeration.addEnumeration(unicode_value='PriorityCustomer', tag='PriorityCustomer')
servicePriorityKind.EmergencyServices = servicePriorityKind._CF_enumeration.addEnumeration(unicode_value='EmergencyServices', tag='EmergencyServices')
servicePriorityKind.MedicalNecessity = servicePriorityKind._CF_enumeration.addEnumeration(unicode_value='MedicalNecessity', tag='MedicalNecessity')
servicePriorityKind.Other = servicePriorityKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
servicePriorityKind._InitializeFacetMap(servicePriorityKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'servicePriorityKind', servicePriorityKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}serviceStatusKind
class serviceStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5064, 1)
    _Documentation = None
serviceStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=serviceStatusKind, enum_prefix=None)
serviceStatusKind.Unknown = serviceStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
serviceStatusKind.Active = serviceStatusKind._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
serviceStatusKind.Inactive = serviceStatusKind._CF_enumeration.addEnumeration(unicode_value='Inactive', tag='Inactive')
serviceStatusKind.Retired = serviceStatusKind._CF_enumeration.addEnumeration(unicode_value='Retired', tag='Retired')
serviceStatusKind.Other = serviceStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
serviceStatusKind._InitializeFacetMap(serviceStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'serviceStatusKind', serviceStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}sizeUnits
class sizeUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sizeUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5096, 1)
    _Documentation = None
sizeUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=sizeUnits, enum_prefix=None)
sizeUnits.Unknown = sizeUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
sizeUnits.AWG = sizeUnits._CF_enumeration.addEnumeration(unicode_value='AWG', tag='AWG')
sizeUnits.kcmil = sizeUnits._CF_enumeration.addEnumeration(unicode_value='kcmil', tag='kcmil')
sizeUnits.MCM = sizeUnits._CF_enumeration.addEnumeration(unicode_value='MCM', tag='MCM')
sizeUnits.mmSquare = sizeUnits._CF_enumeration.addEnumeration(unicode_value='mmSquare', tag='mmSquare')
sizeUnits.Other = sizeUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
sizeUnits._InitializeFacetMap(sizeUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'sizeUnits', sizeUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}spanTypeKind
class spanTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'spanTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5117, 1)
    _Documentation = None
spanTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=spanTypeKind, enum_prefix=None)
spanTypeKind.Unknown = spanTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
spanTypeKind.Primary = spanTypeKind._CF_enumeration.addEnumeration(unicode_value='Primary', tag='Primary')
spanTypeKind.Secondary = spanTypeKind._CF_enumeration.addEnumeration(unicode_value='Secondary', tag='Secondary')
spanTypeKind.Service = spanTypeKind._CF_enumeration.addEnumeration(unicode_value='Service', tag='Service')
spanTypeKind.Underbuild = spanTypeKind._CF_enumeration.addEnumeration(unicode_value='Underbuild', tag='Underbuild')
spanTypeKind.None_ = spanTypeKind._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
spanTypeKind.Other = spanTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
spanTypeKind._InitializeFacetMap(spanTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'spanTypeKind', spanTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}spatialFeatureKind
class spatialFeatureKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'spatialFeatureKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5128, 1)
    _Documentation = None
spatialFeatureKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=spatialFeatureKind, enum_prefix=None)
spatialFeatureKind.Unknown = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
spatialFeatureKind.ACLineSegment = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='ACLineSegment', tag='ACLineSegment')
spatialFeatureKind.anchor = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='anchor', tag='anchor')
spatialFeatureKind.breaker = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='breaker', tag='breaker')
spatialFeatureKind.capacitor = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='capacitor', tag='capacitor')
spatialFeatureKind.capacitorBank = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='capacitorBank', tag='capacitorBank')
spatialFeatureKind.capacitorBankSwitch = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='capacitorBankSwitch', tag='capacitorBankSwitch')
spatialFeatureKind.CDDevice = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='CDDevice', tag='CDDevice')
spatialFeatureKind.conduit = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='conduit', tag='conduit')
spatialFeatureKind.cut = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='cut', tag='cut')
spatialFeatureKind.downGuy = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='downGuy', tag='downGuy')
spatialFeatureKind.elbow = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='elbow', tag='elbow')
spatialFeatureKind.electricMeter = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='electricMeter', tag='electricMeter')
spatialFeatureKind.fuse = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='fuse', tag='fuse')
spatialFeatureKind.gasMeter = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='gasMeter', tag='gasMeter')
spatialFeatureKind.inductionMachine = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='inductionMachine', tag='inductionMachine')
spatialFeatureKind.jumper = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='jumper', tag='jumper')
spatialFeatureKind.loadManagementDevice = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='loadManagementDevice', tag='loadManagementDevice')
spatialFeatureKind.measurementDevice = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='measurementDevice', tag='measurementDevice')
spatialFeatureKind.meterBase = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='meterBase', tag='meterBase')
spatialFeatureKind.module = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='module', tag='module')
spatialFeatureKind.otherSpatialFeature = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='otherSpatialFeature', tag='otherSpatialFeature')
spatialFeatureKind.outageDetectionDevice = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='outageDetectionDevice', tag='outageDetectionDevice')
spatialFeatureKind.overcurrentDeviceBank = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='overcurrentDeviceBank', tag='overcurrentDeviceBank')
spatialFeatureKind.parcel = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='parcel', tag='parcel')
spatialFeatureKind.pole = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='pole', tag='pole')
spatialFeatureKind.powerMonitor = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='powerMonitor', tag='powerMonitor')
spatialFeatureKind.powerSystemDevice = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='powerSystemDevice', tag='powerSystemDevice')
spatialFeatureKind.premises = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='premises', tag='premises')
spatialFeatureKind.premisesDisplay = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='premisesDisplay', tag='premisesDisplay')
spatialFeatureKind.primaryCabinet = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='primaryCabinet', tag='primaryCabinet')
spatialFeatureKind.propaneMeter = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='propaneMeter', tag='propaneMeter')
spatialFeatureKind.pushPole = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='pushPole', tag='pushPole')
spatialFeatureKind.recloser = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='recloser', tag='recloser')
spatialFeatureKind.regulator = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='regulator', tag='regulator')
spatialFeatureKind.regulatorBank = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='regulatorBank', tag='regulatorBank')
spatialFeatureKind.riser = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='riser', tag='riser')
spatialFeatureKind.secondaryJunctionBox = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='secondaryJunctionBox', tag='secondaryJunctionBox')
spatialFeatureKind.sectionalizer = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='sectionalizer', tag='sectionalizer')
spatialFeatureKind.securityLight = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='securityLight', tag='securityLight')
spatialFeatureKind.serviceLocation = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='serviceLocation', tag='serviceLocation')
spatialFeatureKind.spanGuy = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='spanGuy', tag='spanGuy')
spatialFeatureKind.streetLight = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='streetLight', tag='streetLight')
spatialFeatureKind.substation = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='substation', tag='substation')
spatialFeatureKind.surgeArrestor = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='surgeArrestor', tag='surgeArrestor')
spatialFeatureKind.switch = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='switch', tag='switch')
spatialFeatureKind.switchingDeviceBank = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='switchingDeviceBank', tag='switchingDeviceBank')
spatialFeatureKind.synchronousMachine = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='synchronousMachine', tag='synchronousMachine')
spatialFeatureKind.trafficLight = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='trafficLight', tag='trafficLight')
spatialFeatureKind.transformer = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='transformer', tag='transformer')
spatialFeatureKind.transformerBank = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='transformerBank', tag='transformerBank')
spatialFeatureKind.waterMeter = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='waterMeter', tag='waterMeter')
spatialFeatureKind.Other = spatialFeatureKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
spatialFeatureKind._InitializeFacetMap(spatialFeatureKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'spatialFeatureKind', spatialFeatureKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}speedUnits
class speedUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'speedUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5200, 1)
    _Documentation = None
speedUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=speedUnits, enum_prefix=None)
speedUnits.Unknown = speedUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
speedUnits.mph = speedUnits._CF_enumeration.addEnumeration(unicode_value='mph', tag='mph')
speedUnits.feetPerSecond = speedUnits._CF_enumeration.addEnumeration(unicode_value='feetPerSecond', tag='feetPerSecond')
speedUnits.kmPerHour = speedUnits._CF_enumeration.addEnumeration(unicode_value='kmPerHour', tag='kmPerHour')
speedUnits.kmPerSecond = speedUnits._CF_enumeration.addEnumeration(unicode_value='kmPerSecond', tag='kmPerSecond')
speedUnits.mPerSecond = speedUnits._CF_enumeration.addEnumeration(unicode_value='mPerSecond', tag='mPerSecond')
speedUnits.Other = speedUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
speedUnits._InitializeFacetMap(speedUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'speedUnits', speedUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}splitActionKind
class splitActionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This is the action taken on the original outage during an outageSplit."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'splitActionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5225, 1)
    _Documentation = 'This is the action taken on the original outage during an outageSplit.'
splitActionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=splitActionKind, enum_prefix=None)
splitActionKind.OriginalOutageDeleted = splitActionKind._CF_enumeration.addEnumeration(unicode_value='OriginalOutageDeleted', tag='OriginalOutageDeleted')
splitActionKind.OriginalOutageRetained = splitActionKind._CF_enumeration.addEnumeration(unicode_value='OriginalOutageRetained', tag='OriginalOutageRetained')
splitActionKind.Other = splitActionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
splitActionKind._InitializeFacetMap(splitActionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'splitActionKind', splitActionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}standardEntryClassKind
class standardEntryClassKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'standardEntryClassKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5246, 1)
    _Documentation = None
standardEntryClassKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=standardEntryClassKind, enum_prefix=None)
standardEntryClassKind.n27 = standardEntryClassKind._CF_enumeration.addEnumeration(unicode_value='27', tag='n27')
standardEntryClassKind.n28 = standardEntryClassKind._CF_enumeration.addEnumeration(unicode_value='28', tag='n28')
standardEntryClassKind.n37 = standardEntryClassKind._CF_enumeration.addEnumeration(unicode_value='37', tag='n37')
standardEntryClassKind.n38 = standardEntryClassKind._CF_enumeration.addEnumeration(unicode_value='38', tag='n38')
standardEntryClassKind.Other = standardEntryClassKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
standardEntryClassKind._InitializeFacetMap(standardEntryClassKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'standardEntryClassKind', standardEntryClassKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}stationStatusKind
class stationStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stationStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5282, 1)
    _Documentation = None
stationStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stationStatusKind, enum_prefix=None)
stationStatusKind.Unknown = stationStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
stationStatusKind.Construction = stationStatusKind._CF_enumeration.addEnumeration(unicode_value='Construction', tag='Construction')
stationStatusKind.Retire = stationStatusKind._CF_enumeration.addEnumeration(unicode_value='Retire', tag='Retire')
stationStatusKind.Existing = stationStatusKind._CF_enumeration.addEnumeration(unicode_value='Existing', tag='Existing')
stationStatusKind.Other = stationStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
stationStatusKind._InitializeFacetMap(stationStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stationStatusKind', stationStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}statusIdentifierKind
class statusIdentifierKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Status identifiers (See enumerationslist)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'statusIdentifierKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5303, 1)
    _Documentation = 'Status identifiers (See enumerationslist).'
statusIdentifierKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=statusIdentifierKind, enum_prefix=None)
statusIdentifierKind.Unknown = statusIdentifierKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
statusIdentifierKind.Open = statusIdentifierKind._CF_enumeration.addEnumeration(unicode_value='Open', tag='Open')
statusIdentifierKind.Closed = statusIdentifierKind._CF_enumeration.addEnumeration(unicode_value='Closed', tag='Closed')
statusIdentifierKind.Travel = statusIdentifierKind._CF_enumeration.addEnumeration(unicode_value='Travel', tag='Travel')
statusIdentifierKind.OutofService = statusIdentifierKind._CF_enumeration.addEnumeration(unicode_value='OutofService', tag='OutofService')
statusIdentifierKind.Other = statusIdentifierKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
statusIdentifierKind._InitializeFacetMap(statusIdentifierKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'statusIdentifierKind', statusIdentifierKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}statusOfUnitKind
class statusOfUnitKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'statusOfUnitKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5338, 1)
    _Documentation = None
statusOfUnitKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=statusOfUnitKind, enum_prefix=None)
statusOfUnitKind.Unknown = statusOfUnitKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
statusOfUnitKind.C = statusOfUnitKind._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
statusOfUnitKind.R = statusOfUnitKind._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
statusOfUnitKind.E = statusOfUnitKind._CF_enumeration.addEnumeration(unicode_value='E', tag='E')
statusOfUnitKind.CAndR = statusOfUnitKind._CF_enumeration.addEnumeration(unicode_value='CAndR', tag='CAndR')
statusOfUnitKind.RAndE = statusOfUnitKind._CF_enumeration.addEnumeration(unicode_value='RAndE', tag='RAndE')
statusOfUnitKind.CRAndE = statusOfUnitKind._CF_enumeration.addEnumeration(unicode_value='CRAndE', tag='CRAndE')
statusOfUnitKind.Other = statusOfUnitKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
statusOfUnitKind._InitializeFacetMap(statusOfUnitKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'statusOfUnitKind', statusOfUnitKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}submissionPurposeKind
class submissionPurposeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'submissionPurposeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5385, 1)
    _Documentation = None
submissionPurposeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=submissionPurposeKind, enum_prefix=None)
submissionPurposeKind.Unknown = submissionPurposeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
submissionPurposeKind.Proposed = submissionPurposeKind._CF_enumeration.addEnumeration(unicode_value='Proposed', tag='Proposed')
submissionPurposeKind.Estimated = submissionPurposeKind._CF_enumeration.addEnumeration(unicode_value='Estimated', tag='Estimated')
submissionPurposeKind.Requisition = submissionPurposeKind._CF_enumeration.addEnumeration(unicode_value='Requisition', tag='Requisition')
submissionPurposeKind.AsBuilt = submissionPurposeKind._CF_enumeration.addEnumeration(unicode_value='AsBuilt', tag='AsBuilt')
submissionPurposeKind.Other = submissionPurposeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
submissionPurposeKind._InitializeFacetMap(submissionPurposeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'submissionPurposeKind', submissionPurposeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}sUnits
class sUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5395, 1)
    _Documentation = None
sUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=sUnits, enum_prefix=None)
sUnits.Unknown = sUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
sUnits.microS = sUnits._CF_enumeration.addEnumeration(unicode_value='microS', tag='microS')
sUnits.mS = sUnits._CF_enumeration.addEnumeration(unicode_value='mS', tag='mS')
sUnits.S = sUnits._CF_enumeration.addEnumeration(unicode_value='S', tag='S')
sUnits.kS = sUnits._CF_enumeration.addEnumeration(unicode_value='kS', tag='kS')
sUnits.MS = sUnits._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
sUnits.Siemens = sUnits._CF_enumeration.addEnumeration(unicode_value='Siemens', tag='Siemens')
sUnits.mho = sUnits._CF_enumeration.addEnumeration(unicode_value='mho', tag='mho')
sUnits.Other = sUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
sUnits._InitializeFacetMap(sUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'sUnits', sUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}switchingEndStateKind
class switchingEndStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The desired end state for the device being operated on during this switching step. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'switchingEndStateKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5408, 1)
    _Documentation = 'The desired end state for the device being operated on during this switching step. '
switchingEndStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=switchingEndStateKind, enum_prefix=None)
switchingEndStateKind.Open = switchingEndStateKind._CF_enumeration.addEnumeration(unicode_value='Open', tag='Open')
switchingEndStateKind.Closed = switchingEndStateKind._CF_enumeration.addEnumeration(unicode_value='Closed', tag='Closed')
switchingEndStateKind.TaggedOpen = switchingEndStateKind._CF_enumeration.addEnumeration(unicode_value='TaggedOpen', tag='TaggedOpen')
switchingEndStateKind.TaggedClosed = switchingEndStateKind._CF_enumeration.addEnumeration(unicode_value='TaggedClosed', tag='TaggedClosed')
switchingEndStateKind.Grounded = switchingEndStateKind._CF_enumeration.addEnumeration(unicode_value='Grounded', tag='Grounded')
switchingEndStateKind.Ungrounded = switchingEndStateKind._CF_enumeration.addEnumeration(unicode_value='Ungrounded', tag='Ungrounded')
switchingEndStateKind.Isolated = switchingEndStateKind._CF_enumeration.addEnumeration(unicode_value='Isolated', tag='Isolated')
switchingEndStateKind.InService = switchingEndStateKind._CF_enumeration.addEnumeration(unicode_value='InService', tag='InService')
switchingEndStateKind.Other = switchingEndStateKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
switchingEndStateKind._InitializeFacetMap(switchingEndStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'switchingEndStateKind', switchingEndStateKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}switchingStepOperationKind
class switchingStepOperationKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Operation to be performed during a switching step."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'switchingStepOperationKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5438, 1)
    _Documentation = 'Operation to be performed during a switching step.'
switchingStepOperationKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=switchingStepOperationKind, enum_prefix=None)
switchingStepOperationKind.Open = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='Open', tag='Open')
switchingStepOperationKind.Close = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='Close', tag='Close')
switchingStepOperationKind.CheckOpen = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='CheckOpen', tag='CheckOpen')
switchingStepOperationKind.CheckClosed = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='CheckClosed', tag='CheckClosed')
switchingStepOperationKind.InstallGround = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='InstallGround', tag='InstallGround')
switchingStepOperationKind.RemoveGround = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='RemoveGround', tag='RemoveGround')
switchingStepOperationKind.SetTags = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='SetTags', tag='SetTags')
switchingStepOperationKind.RemoveTag = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='RemoveTag', tag='RemoveTag')
switchingStepOperationKind.TagClosed = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='TagClosed', tag='TagClosed')
switchingStepOperationKind.TagOpen = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='TagOpen', tag='TagOpen')
switchingStepOperationKind.Other = switchingStepOperationKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
switchingStepOperationKind._InitializeFacetMap(switchingStepOperationKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'switchingStepOperationKind', switchingStepOperationKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}switchingStepStatusKind
class switchingStepStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The status of this switching step.  Possible enumerations include: Proposed, Instructed, Confirmed, Aborted, Skipped, Other. The supported values of stepStatus should be discovered by a call to GetDomainsByDomainName on the application that is the system of record for switching orders."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'switchingStepStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5470, 1)
    _Documentation = 'The status of this switching step.  Possible enumerations include: Proposed, Instructed, Confirmed, Aborted, Skipped, Other. The supported values of stepStatus should be discovered by a call to GetDomainsByDomainName on the application that is the system of record for switching orders.'
switchingStepStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=switchingStepStatusKind, enum_prefix=None)
switchingStepStatusKind.Proposed = switchingStepStatusKind._CF_enumeration.addEnumeration(unicode_value='Proposed', tag='Proposed')
switchingStepStatusKind.Instructed = switchingStepStatusKind._CF_enumeration.addEnumeration(unicode_value='Instructed', tag='Instructed')
switchingStepStatusKind.Confirmed = switchingStepStatusKind._CF_enumeration.addEnumeration(unicode_value='Confirmed', tag='Confirmed')
switchingStepStatusKind.Aborted = switchingStepStatusKind._CF_enumeration.addEnumeration(unicode_value='Aborted', tag='Aborted')
switchingStepStatusKind.Completed = switchingStepStatusKind._CF_enumeration.addEnumeration(unicode_value='Completed', tag='Completed')
switchingStepStatusKind.Skipped = switchingStepStatusKind._CF_enumeration.addEnumeration(unicode_value='Skipped', tag='Skipped')
switchingStepStatusKind.Other = switchingStepStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
switchingStepStatusKind._InitializeFacetMap(switchingStepStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'switchingStepStatusKind', switchingStepStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}switchTypeKind
class switchTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of capacitor switch control used in this section."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'switchTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5509, 1)
    _Documentation = 'Type of capacitor switch control used in this section.'
switchTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=switchTypeKind, enum_prefix=None)
switchTypeKind.Unknown = switchTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
switchTypeKind.Manual = switchTypeKind._CF_enumeration.addEnumeration(unicode_value='Manual', tag='Manual')
switchTypeKind.Voltage = switchTypeKind._CF_enumeration.addEnumeration(unicode_value='Voltage', tag='Voltage')
switchTypeKind.Current = switchTypeKind._CF_enumeration.addEnumeration(unicode_value='Current', tag='Current')
switchTypeKind.ReactiveAmps = switchTypeKind._CF_enumeration.addEnumeration(unicode_value='ReactiveAmps', tag='ReactiveAmps')
switchTypeKind.Time = switchTypeKind._CF_enumeration.addEnumeration(unicode_value='Time', tag='Time')
switchTypeKind.Temperature = switchTypeKind._CF_enumeration.addEnumeration(unicode_value='Temperature', tag='Temperature')
switchTypeKind.Other = switchTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
switchTypeKind._InitializeFacetMap(switchTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'switchTypeKind', switchTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}tagKind
class tagKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The kind of clearanceTag.  Enumerated values include: HoldOpen - this means that the device shall be maintained in the open position while the tag is in effect; HoldClosed - this means that the device shall be maintained in the closed position while the tag is in effect; Full - this means that no action is permitted to be taken on this device and no reporting is to be made; Information - this tag type is attached to include information on the device state, but that no inhibition is placed on the operation or reporting on the device; Control - this means that no control action is to be taken on the device, but reporting may be performed; Alarm - this means that alarming is to be suppressed while the tag is in effect; Scan - this means that scanning is to be inhibited while the tag is in effect; Other - system will provide a vendor-specific tagKind."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tagKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5524, 1)
    _Documentation = 'The kind of clearanceTag.  Enumerated values include: HoldOpen - this means that the device shall be maintained in the open position while the tag is in effect; HoldClosed - this means that the device shall be maintained in the closed position while the tag is in effect; Full - this means that no action is permitted to be taken on this device and no reporting is to be made; Information - this tag type is attached to include information on the device state, but that no inhibition is placed on the operation or reporting on the device; Control - this means that no control action is to be taken on the device, but reporting may be performed; Alarm - this means that alarming is to be suppressed while the tag is in effect; Scan - this means that scanning is to be inhibited while the tag is in effect; Other - system will provide a vendor-specific tagKind.'
tagKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tagKind, enum_prefix=None)
tagKind.HoldOpen = tagKind._CF_enumeration.addEnumeration(unicode_value='HoldOpen', tag='HoldOpen')
tagKind.HoldClosed = tagKind._CF_enumeration.addEnumeration(unicode_value='HoldClosed', tag='HoldClosed')
tagKind.Full = tagKind._CF_enumeration.addEnumeration(unicode_value='Full', tag='Full')
tagKind.Information = tagKind._CF_enumeration.addEnumeration(unicode_value='Information', tag='Information')
tagKind.Control = tagKind._CF_enumeration.addEnumeration(unicode_value='Control', tag='Control')
tagKind.Alarm = tagKind._CF_enumeration.addEnumeration(unicode_value='Alarm', tag='Alarm')
tagKind.Scan = tagKind._CF_enumeration.addEnumeration(unicode_value='Scan', tag='Scan')
tagKind.Other = tagKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
tagKind._InitializeFacetMap(tagKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tagKind', tagKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}temperatureCompensationType
class temperatureCompensationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Gas meter temperature compensation type code from ANSI C12.19:

0 - Uncompensated
1 - Mechanical
2 - Sensor"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'temperatureCompensationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5585, 1)
    _Documentation = 'Gas meter temperature compensation type code from ANSI C12.19:\n\n0 - Uncompensated\n1 - Mechanical\n2 - Sensor'
temperatureCompensationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=temperatureCompensationType, enum_prefix=None)
temperatureCompensationType.n0 = temperatureCompensationType._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
temperatureCompensationType.n1 = temperatureCompensationType._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
temperatureCompensationType.n2 = temperatureCompensationType._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
temperatureCompensationType._InitializeFacetMap(temperatureCompensationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'temperatureCompensationType', temperatureCompensationType)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}temperatureUnits
class temperatureUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'temperatureUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5599, 1)
    _Documentation = None
temperatureUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=temperatureUnits, enum_prefix=None)
temperatureUnits.Unknown = temperatureUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
temperatureUnits.degreesC = temperatureUnits._CF_enumeration.addEnumeration(unicode_value='degreesC', tag='degreesC')
temperatureUnits.degreesK = temperatureUnits._CF_enumeration.addEnumeration(unicode_value='degreesK', tag='degreesK')
temperatureUnits.degreesF = temperatureUnits._CF_enumeration.addEnumeration(unicode_value='degreesF', tag='degreesF')
temperatureUnits.Other = temperatureUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
temperatureUnits._InitializeFacetMap(temperatureUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'temperatureUnits', temperatureUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}thermalCoefficientOfResistanceUnits
class thermalCoefficientOfResistanceUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermalCoefficientOfResistanceUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5608, 1)
    _Documentation = None
thermalCoefficientOfResistanceUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=thermalCoefficientOfResistanceUnits, enum_prefix=None)
thermalCoefficientOfResistanceUnits.Unknown = thermalCoefficientOfResistanceUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
thermalCoefficientOfResistanceUnits.ReciprocalDegreesC = thermalCoefficientOfResistanceUnits._CF_enumeration.addEnumeration(unicode_value='ReciprocalDegreesC', tag='ReciprocalDegreesC')
thermalCoefficientOfResistanceUnits.ReciprocalDegreesK = thermalCoefficientOfResistanceUnits._CF_enumeration.addEnumeration(unicode_value='ReciprocalDegreesK', tag='ReciprocalDegreesK')
thermalCoefficientOfResistanceUnits.ReciprocalDegreesF = thermalCoefficientOfResistanceUnits._CF_enumeration.addEnumeration(unicode_value='ReciprocalDegreesF', tag='ReciprocalDegreesF')
thermalCoefficientOfResistanceUnits.Other = thermalCoefficientOfResistanceUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
thermalCoefficientOfResistanceUnits._InitializeFacetMap(thermalCoefficientOfResistanceUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'thermalCoefficientOfResistanceUnits', thermalCoefficientOfResistanceUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}thermostatFanStatusKind
class thermostatFanStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermostatFanStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5628, 1)
    _Documentation = None
thermostatFanStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=thermostatFanStatusKind, enum_prefix=None)
thermostatFanStatusKind.Unknown = thermostatFanStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
thermostatFanStatusKind.Auto = thermostatFanStatusKind._CF_enumeration.addEnumeration(unicode_value='Auto', tag='Auto')
thermostatFanStatusKind.On = thermostatFanStatusKind._CF_enumeration.addEnumeration(unicode_value='On', tag='On')
thermostatFanStatusKind.Cycle = thermostatFanStatusKind._CF_enumeration.addEnumeration(unicode_value='Cycle', tag='Cycle')
thermostatFanStatusKind.Other = thermostatFanStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
thermostatFanStatusKind._InitializeFacetMap(thermostatFanStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'thermostatFanStatusKind', thermostatFanStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}thermostatHoldKind
class thermostatHoldKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermostatHoldKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5637, 1)
    _Documentation = None
thermostatHoldKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=thermostatHoldKind, enum_prefix=None)
thermostatHoldKind.On = thermostatHoldKind._CF_enumeration.addEnumeration(unicode_value='On', tag='On')
thermostatHoldKind.Off = thermostatHoldKind._CF_enumeration.addEnumeration(unicode_value='Off', tag='Off')
thermostatHoldKind.Override = thermostatHoldKind._CF_enumeration.addEnumeration(unicode_value='Override', tag='Override')
thermostatHoldKind.Unknown = thermostatHoldKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
thermostatHoldKind.Vacation = thermostatHoldKind._CF_enumeration.addEnumeration(unicode_value='Vacation', tag='Vacation')
thermostatHoldKind.Other = thermostatHoldKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
thermostatHoldKind._InitializeFacetMap(thermostatHoldKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'thermostatHoldKind', thermostatHoldKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}thermostatModeKind
class thermostatModeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermostatModeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5658, 1)
    _Documentation = None
thermostatModeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=thermostatModeKind, enum_prefix=None)
thermostatModeKind.Unknown = thermostatModeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
thermostatModeKind.Off = thermostatModeKind._CF_enumeration.addEnumeration(unicode_value='Off', tag='Off')
thermostatModeKind.Heat = thermostatModeKind._CF_enumeration.addEnumeration(unicode_value='Heat', tag='Heat')
thermostatModeKind.Cool = thermostatModeKind._CF_enumeration.addEnumeration(unicode_value='Cool', tag='Cool')
thermostatModeKind.Auto = thermostatModeKind._CF_enumeration.addEnumeration(unicode_value='Auto', tag='Auto')
thermostatModeKind.Other = thermostatModeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
thermostatModeKind._InitializeFacetMap(thermostatModeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'thermostatModeKind', thermostatModeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}thicknessUnits
class thicknessUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thicknessUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5668, 1)
    _Documentation = None
thicknessUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=thicknessUnits, enum_prefix=None)
thicknessUnits.Unknown = thicknessUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
thicknessUnits.Mils = thicknessUnits._CF_enumeration.addEnumeration(unicode_value='Mils', tag='Mils')
thicknessUnits.Inches = thicknessUnits._CF_enumeration.addEnumeration(unicode_value='Inches', tag='Inches')
thicknessUnits.Micrometers = thicknessUnits._CF_enumeration.addEnumeration(unicode_value='Micrometers', tag='Micrometers')
thicknessUnits.Millimeters = thicknessUnits._CF_enumeration.addEnumeration(unicode_value='Millimeters', tag='Millimeters')
thicknessUnits.Centimeters = thicknessUnits._CF_enumeration.addEnumeration(unicode_value='Centimeters', tag='Centimeters')
thicknessUnits.Microns = thicknessUnits._CF_enumeration.addEnumeration(unicode_value='Microns', tag='Microns')
thicknessUnits.Other = thicknessUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
thicknessUnits._InitializeFacetMap(thicknessUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'thicknessUnits', thicknessUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}timeSpan
class timeSpan (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeSpan')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5680, 1)
    _Documentation = None
timeSpan._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=timeSpan, enum_prefix=None)
timeSpan.specifiedStartStop = timeSpan._CF_enumeration.addEnumeration(unicode_value='specifiedStartStop', tag='specifiedStartStop')
timeSpan.instantaneous = timeSpan._CF_enumeration.addEnumeration(unicode_value='instantaneous', tag='instantaneous')
timeSpan.perCycle = timeSpan._CF_enumeration.addEnumeration(unicode_value='perCycle', tag='perCycle')
timeSpan._InitializeFacetMap(timeSpan._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'timeSpan', timeSpan)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}timeUnits
class timeUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Units of time"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5687, 1)
    _Documentation = 'Units of time'
timeUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=timeUnits, enum_prefix=None)
timeUnits.Unknown = timeUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
timeUnits.Milliseconds = timeUnits._CF_enumeration.addEnumeration(unicode_value='Milliseconds', tag='Milliseconds')
timeUnits.Seconds = timeUnits._CF_enumeration.addEnumeration(unicode_value='Seconds', tag='Seconds')
timeUnits.Minutes = timeUnits._CF_enumeration.addEnumeration(unicode_value='Minutes', tag='Minutes')
timeUnits.Hours = timeUnits._CF_enumeration.addEnumeration(unicode_value='Hours', tag='Hours')
timeUnits.Days = timeUnits._CF_enumeration.addEnumeration(unicode_value='Days', tag='Days')
timeUnits.Weeks = timeUnits._CF_enumeration.addEnumeration(unicode_value='Weeks', tag='Weeks')
timeUnits.Months = timeUnits._CF_enumeration.addEnumeration(unicode_value='Months', tag='Months')
timeUnits.Years = timeUnits._CF_enumeration.addEnumeration(unicode_value='Years', tag='Years')
timeUnits.Other = timeUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
timeUnits._InitializeFacetMap(timeUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'timeUnits', timeUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}treatmentKind
class treatmentKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Pole treatment type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'treatmentKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5715, 1)
    _Documentation = 'Pole treatment type.'
treatmentKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=treatmentKind, enum_prefix=None)
treatmentKind.Unknown = treatmentKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
treatmentKind.Butt = treatmentKind._CF_enumeration.addEnumeration(unicode_value='Butt', tag='Butt')
treatmentKind.Natural = treatmentKind._CF_enumeration.addEnumeration(unicode_value='Natural', tag='Natural')
treatmentKind.Penta = treatmentKind._CF_enumeration.addEnumeration(unicode_value='Penta', tag='Penta')
treatmentKind.Creosote = treatmentKind._CF_enumeration.addEnumeration(unicode_value='Creosote', tag='Creosote')
treatmentKind.CCA = treatmentKind._CF_enumeration.addEnumeration(unicode_value='CCA', tag='CCA')
treatmentKind.Chemonite = treatmentKind._CF_enumeration.addEnumeration(unicode_value='Chemonite', tag='Chemonite')
treatmentKind.Napthena = treatmentKind._CF_enumeration.addEnumeration(unicode_value='Napthena', tag='Napthena')
treatmentKind.Cellon = treatmentKind._CF_enumeration.addEnumeration(unicode_value='Cellon', tag='Cellon')
treatmentKind.Other = treatmentKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
treatmentKind._InitializeFacetMap(treatmentKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'treatmentKind', treatmentKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}unitActionKind
class unitActionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Action, if any, to be taken at this location.  If the system of record does not support Transfer of units, then it should interpret this action as being the same as "Construction".  If the system of record does not support Salvage then it should interpret salvage as being the same as "Retire"."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitActionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5746, 1)
    _Documentation = 'Action, if any, to be taken at this location.  If the system of record does not support Transfer of units, then it should interpret this action as being the same as "Construction".  If the system of record does not support Salvage then it should interpret salvage as being the same as "Retire".'
unitActionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=unitActionKind, enum_prefix=None)
unitActionKind.Unknown = unitActionKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
unitActionKind.Abandon = unitActionKind._CF_enumeration.addEnumeration(unicode_value='Abandon', tag='Abandon')
unitActionKind.Construction = unitActionKind._CF_enumeration.addEnumeration(unicode_value='Construction', tag='Construction')
unitActionKind.Existing = unitActionKind._CF_enumeration.addEnumeration(unicode_value='Existing', tag='Existing')
unitActionKind.NoAction = unitActionKind._CF_enumeration.addEnumeration(unicode_value='NoAction', tag='NoAction')
unitActionKind.Retire = unitActionKind._CF_enumeration.addEnumeration(unicode_value='Retire', tag='Retire')
unitActionKind.Transfer = unitActionKind._CF_enumeration.addEnumeration(unicode_value='Transfer', tag='Transfer')
unitActionKind.Salvage = unitActionKind._CF_enumeration.addEnumeration(unicode_value='Salvage', tag='Salvage')
unitActionKind.All = unitActionKind._CF_enumeration.addEnumeration(unicode_value='All', tag='All')
unitActionKind.Other = unitActionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
unitActionKind._InitializeFacetMap(unitActionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'unitActionKind', unitActionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}unitPrefixKind
class unitPrefixKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitPrefixKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5795, 1)
    _Documentation = None
unitPrefixKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=unitPrefixKind, enum_prefix=None)
unitPrefixKind.Maximum = unitPrefixKind._CF_enumeration.addEnumeration(unicode_value='Maximum', tag='Maximum')
unitPrefixKind.Minimum = unitPrefixKind._CF_enumeration.addEnumeration(unicode_value='Minimum', tag='Minimum')
unitPrefixKind.Average = unitPrefixKind._CF_enumeration.addEnumeration(unicode_value='Average', tag='Average')
unitPrefixKind.Instantaneous = unitPrefixKind._CF_enumeration.addEnumeration(unicode_value='Instantaneous', tag='Instantaneous')
unitPrefixKind.Cumulative = unitPrefixKind._CF_enumeration.addEnumeration(unicode_value='Cumulative', tag='Cumulative')
unitPrefixKind.Quantity = unitPrefixKind._CF_enumeration.addEnumeration(unicode_value='Quantity', tag='Quantity')
unitPrefixKind.Other = unitPrefixKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
unitPrefixKind._InitializeFacetMap(unitPrefixKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'unitPrefixKind', unitPrefixKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}unitTypeKind
class unitTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Type of material management assembly."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5828, 1)
    _Documentation = 'Type of material management assembly.'
unitTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=unitTypeKind, enum_prefix=None)
unitTypeKind.Other = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
unitTypeKind.Anchor = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='Anchor', tag='Anchor')
unitTypeKind.OhPrimaryConductor = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='OhPrimaryConductor', tag='OhPrimaryConductor')
unitTypeKind.UgPrimaryConductor = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='UgPrimaryConductor', tag='UgPrimaryConductor')
unitTypeKind.OhSecondaryConductor = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='OhSecondaryConductor', tag='OhSecondaryConductor')
unitTypeKind.UgSecondaryConductor = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='UgSecondaryConductor', tag='UgSecondaryConductor')
unitTypeKind.Conductor = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='Conductor', tag='Conductor')
unitTypeKind.Guy = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='Guy', tag='Guy')
unitTypeKind.OhAssembly = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='OhAssembly', tag='OhAssembly')
unitTypeKind.OhPrimary = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='OhPrimary', tag='OhPrimary')
unitTypeKind.OhSecondary = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='OhSecondary', tag='OhSecondary')
unitTypeKind.OhTransformer = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='OhTransformer', tag='OhTransformer')
unitTypeKind.Overhead = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='Overhead', tag='Overhead')
unitTypeKind.Pole = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='Pole', tag='Pole')
unitTypeKind.SubUnit = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='SubUnit', tag='SubUnit')
unitTypeKind.UgAssembly = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='UgAssembly', tag='UgAssembly')
unitTypeKind.UgPrimary = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='UgPrimary', tag='UgPrimary')
unitTypeKind.UgSecondary = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='UgSecondary', tag='UgSecondary')
unitTypeKind.UgTransformer = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='UgTransformer', tag='UgTransformer')
unitTypeKind.Underground = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='Underground', tag='Underground')
unitTypeKind.Conduit = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='Conduit', tag='Conduit')
unitTypeKind.Duct = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='Duct', tag='Duct')
unitTypeKind.LaborOnly = unitTypeKind._CF_enumeration.addEnumeration(unicode_value='LaborOnly', tag='LaborOnly')
unitTypeKind._InitializeFacetMap(unitTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'unitTypeKind', unitTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}uomKind
class uomKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This is the list of units of measure from ANSI C12.19"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uomKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5872, 1)
    _Documentation = 'This is the list of units of measure from ANSI C12.19'
uomKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=uomKind, enum_prefix=None)
uomKind.Acre_ft = uomKind._CF_enumeration.addEnumeration(unicode_value='Acre ft', tag='Acre_ft')
uomKind.Amps = uomKind._CF_enumeration.addEnumeration(unicode_value='Amps', tag='Amps')
uomKind.Amps_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='Amps RMS', tag='Amps_RMS')
uomKind.Amps_squared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='Amps squared RMS', tag='Amps_squared_RMS')
uomKind.atmospheres = uomKind._CF_enumeration.addEnumeration(unicode_value='atmospheres', tag='atmospheres')
uomKind.Bar = uomKind._CF_enumeration.addEnumeration(unicode_value='Bar', tag='Bar')
uomKind.ccf = uomKind._CF_enumeration.addEnumeration(unicode_value='ccf', tag='ccf')
uomKind.ccf_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='ccf per Hr', tag='ccf_per_Hr')
uomKind.cm = uomKind._CF_enumeration.addEnumeration(unicode_value='cm', tag='cm')
uomKind.Corrosion = uomKind._CF_enumeration.addEnumeration(unicode_value='Corrosion', tag='Corrosion')
uomKind.Counter = uomKind._CF_enumeration.addEnumeration(unicode_value='Counter', tag='Counter')
uomKind.cubic_feet = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic feet', tag='cubic_feet')
uomKind.cubic_feet_corrected = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic feet corrected', tag='cubic_feet_corrected')
uomKind.cubic_feet_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic feet per Hr', tag='cubic_feet_per_Hr')
uomKind.cubic_feet_per_Hr_corrected = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic feet per Hr corrected', tag='cubic_feet_per_Hr_corrected')
uomKind.cubic_feet_per_Hr_uncorrected = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic feet per Hr uncorrected', tag='cubic_feet_per_Hr_uncorrected')
uomKind.cubic_feet_uncorrected = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic feet uncorrected', tag='cubic_feet_uncorrected')
uomKind.cubic_meter = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic meter', tag='cubic_meter')
uomKind.cubic_meter_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic meter per Hr', tag='cubic_meter_per_Hr')
uomKind.cubic_meters_corrected = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic meters corrected', tag='cubic_meters_corrected')
uomKind.cubic_meters_per_Hr_corrected = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic meters per Hr corrected', tag='cubic_meters_per_Hr_corrected')
uomKind.cubic_meters_per_Hr_uncorrected = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic meters per Hr uncorrected', tag='cubic_meters_per_Hr_uncorrected')
uomKind.cubic_meters_uncorrected = uomKind._CF_enumeration.addEnumeration(unicode_value='cubic meters uncorrected', tag='cubic_meters_uncorrected')
uomKind.Current_phase_angle = uomKind._CF_enumeration.addEnumeration(unicode_value='Current phase angle', tag='Current_phase_angle')
uomKind.Date = uomKind._CF_enumeration.addEnumeration(unicode_value='Date', tag='Date')
uomKind.Date_time = uomKind._CF_enumeration.addEnumeration(unicode_value='Date time', tag='Date_time')
uomKind.deg_C = uomKind._CF_enumeration.addEnumeration(unicode_value='deg C', tag='deg_C')
uomKind.deg_F = uomKind._CF_enumeration.addEnumeration(unicode_value='deg F', tag='deg_F')
uomKind.deg_K = uomKind._CF_enumeration.addEnumeration(unicode_value='deg K', tag='deg_K')
uomKind.Differential_pascal = uomKind._CF_enumeration.addEnumeration(unicode_value='Differential pascal', tag='Differential_pascal')
uomKind.Differential_pound_per_square_inch = uomKind._CF_enumeration.addEnumeration(unicode_value='Differential pound per square inch', tag='Differential_pound_per_square_inch')
uomKind.dm = uomKind._CF_enumeration.addEnumeration(unicode_value='dm', tag='dm')
uomKind.Dollar = uomKind._CF_enumeration.addEnumeration(unicode_value='Dollar', tag='Dollar')
uomKind.feet_per_second = uomKind._CF_enumeration.addEnumeration(unicode_value='feet per second', tag='feet_per_second')
uomKind.Frequency = uomKind._CF_enumeration.addEnumeration(unicode_value='Frequency', tag='Frequency')
uomKind.ft = uomKind._CF_enumeration.addEnumeration(unicode_value='ft', tag='ft')
uomKind.ft_of_water = uomKind._CF_enumeration.addEnumeration(unicode_value='ft of water', tag='ft_of_water')
uomKind.GQ = uomKind._CF_enumeration.addEnumeration(unicode_value='GQ', tag='GQ')
uomKind.GQh = uomKind._CF_enumeration.addEnumeration(unicode_value='GQh', tag='GQh')
uomKind.Gram_square_cm = uomKind._CF_enumeration.addEnumeration(unicode_value='Gram square cm', tag='Gram_square_cm')
uomKind.GVA = uomKind._CF_enumeration.addEnumeration(unicode_value='GVA', tag='GVA')
uomKind.GVAh = uomKind._CF_enumeration.addEnumeration(unicode_value='GVAh', tag='GVAh')
uomKind.GVAR = uomKind._CF_enumeration.addEnumeration(unicode_value='GVAR', tag='GVAR')
uomKind.GVARh = uomKind._CF_enumeration.addEnumeration(unicode_value='GVARh', tag='GVARh')
uomKind.GW = uomKind._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
uomKind.GWh = uomKind._CF_enumeration.addEnumeration(unicode_value='GWh', tag='GWh')
uomKind.IMP_gl = uomKind._CF_enumeration.addEnumeration(unicode_value='IMP gl', tag='IMP_gl')
uomKind.IMP_gl_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='IMP gl per Hr', tag='IMP_gl_per_Hr')
uomKind.inches = uomKind._CF_enumeration.addEnumeration(unicode_value='inches', tag='inches')
uomKind.Inches_H2O_column = uomKind._CF_enumeration.addEnumeration(unicode_value='Inches H2O column', tag='Inches_H2O_column')
uomKind.Inches_HG_column = uomKind._CF_enumeration.addEnumeration(unicode_value='Inches HG column', tag='Inches_HG_column')
uomKind.inches_of_water = uomKind._CF_enumeration.addEnumeration(unicode_value='inches of water', tag='inches_of_water')
uomKind.Interval_timer = uomKind._CF_enumeration.addEnumeration(unicode_value='Interval timer', tag='Interval_timer')
uomKind.Ionization = uomKind._CF_enumeration.addEnumeration(unicode_value='Ionization', tag='Ionization')
uomKind.Joules = uomKind._CF_enumeration.addEnumeration(unicode_value='Joules', tag='Joules')
uomKind.Joules_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='Joules per Hr', tag='Joules_per_Hr')
uomKind.kAmps = uomKind._CF_enumeration.addEnumeration(unicode_value='kAmps', tag='kAmps')
uomKind.kAmps_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='kAmps RMS', tag='kAmps_RMS')
uomKind.kAmps_squared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='kAmps squared RMS', tag='kAmps_squared_RMS')
uomKind.kJoules = uomKind._CF_enumeration.addEnumeration(unicode_value='kJoules', tag='kJoules')
uomKind.kJoules_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='kJoules per Hr', tag='kJoules_per_Hr')
uomKind.km = uomKind._CF_enumeration.addEnumeration(unicode_value='km', tag='km')
uomKind.km_per_hour = uomKind._CF_enumeration.addEnumeration(unicode_value='km per hour', tag='km_per_hour')
uomKind.km_per_second = uomKind._CF_enumeration.addEnumeration(unicode_value='km per second', tag='km_per_second')
uomKind.kQ = uomKind._CF_enumeration.addEnumeration(unicode_value='kQ', tag='kQ')
uomKind.kQh = uomKind._CF_enumeration.addEnumeration(unicode_value='kQh', tag='kQh')
uomKind.kV = uomKind._CF_enumeration.addEnumeration(unicode_value='kV', tag='kV')
uomKind.kV_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='kV RMS', tag='kV_RMS')
uomKind.kVA = uomKind._CF_enumeration.addEnumeration(unicode_value='kVA', tag='kVA')
uomKind.kVAh = uomKind._CF_enumeration.addEnumeration(unicode_value='kVAh', tag='kVAh')
uomKind.kVAR = uomKind._CF_enumeration.addEnumeration(unicode_value='kVAR', tag='kVAR')
uomKind.kVARh = uomKind._CF_enumeration.addEnumeration(unicode_value='kVARh', tag='kVARh')
uomKind.kVsquared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='kVsquared RMS', tag='kVsquared_RMS')
uomKind.kW = uomKind._CF_enumeration.addEnumeration(unicode_value='kW', tag='kW')
uomKind.kWh = uomKind._CF_enumeration.addEnumeration(unicode_value='kWh', tag='kWh')
uomKind.liters = uomKind._CF_enumeration.addEnumeration(unicode_value='liters', tag='liters')
uomKind.m = uomKind._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
uomKind.m_per_second = uomKind._CF_enumeration.addEnumeration(unicode_value='m per second', tag='m_per_second')
uomKind.mAmps = uomKind._CF_enumeration.addEnumeration(unicode_value='mAmps', tag='mAmps')
uomKind.Mamps = uomKind._CF_enumeration.addEnumeration(unicode_value='Mamps', tag='Mamps')
uomKind.Mamps_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='Mamps RMS', tag='Mamps_RMS')
uomKind.mAmps_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='mAmps RMS', tag='mAmps_RMS')
uomKind.mAmps_squared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='mAmps squared RMS', tag='mAmps_squared_RMS')
uomKind.Mamps_squared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='Mamps squared RMS', tag='Mamps_squared_RMS')
uomKind.Meter_HG_column = uomKind._CF_enumeration.addEnumeration(unicode_value='Meter HG column', tag='Meter_HG_column')
uomKind.micro_m = uomKind._CF_enumeration.addEnumeration(unicode_value='micro m', tag='micro_m')
uomKind.microAmps = uomKind._CF_enumeration.addEnumeration(unicode_value='microAmps', tag='microAmps')
uomKind.microAmps_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='microAmps RMS', tag='microAmps_RMS')
uomKind.microAmps_squared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='microAmps squared RMS', tag='microAmps_squared_RMS')
uomKind.microJoules = uomKind._CF_enumeration.addEnumeration(unicode_value='microJoules', tag='microJoules')
uomKind.microJoules_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='microJoules per Hr', tag='microJoules_per_Hr')
uomKind.microQ = uomKind._CF_enumeration.addEnumeration(unicode_value='microQ', tag='microQ')
uomKind.microQh = uomKind._CF_enumeration.addEnumeration(unicode_value='microQh', tag='microQh')
uomKind.microV = uomKind._CF_enumeration.addEnumeration(unicode_value='microV', tag='microV')
uomKind.microV_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='microV RMS', tag='microV_RMS')
uomKind.microVA = uomKind._CF_enumeration.addEnumeration(unicode_value='microVA', tag='microVA')
uomKind.microVAh = uomKind._CF_enumeration.addEnumeration(unicode_value='microVAh', tag='microVAh')
uomKind.microVAR = uomKind._CF_enumeration.addEnumeration(unicode_value='microVAR', tag='microVAR')
uomKind.microVARh = uomKind._CF_enumeration.addEnumeration(unicode_value='microVARh', tag='microVARh')
uomKind.microVsquared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='microVsquared RMS', tag='microVsquared_RMS')
uomKind.microW = uomKind._CF_enumeration.addEnumeration(unicode_value='microW', tag='microW')
uomKind.microWh = uomKind._CF_enumeration.addEnumeration(unicode_value='microWh', tag='microWh')
uomKind.Minutes_on_battery = uomKind._CF_enumeration.addEnumeration(unicode_value='Minutes on battery', tag='Minutes_on_battery')
uomKind.MJoules = uomKind._CF_enumeration.addEnumeration(unicode_value='MJoules', tag='MJoules')
uomKind.mJoules = uomKind._CF_enumeration.addEnumeration(unicode_value='mJoules', tag='mJoules')
uomKind.MJoules_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='MJoules per Hr', tag='MJoules_per_Hr')
uomKind.mJoules_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='mJoules per Hr', tag='mJoules_per_Hr')
uomKind.mm = uomKind._CF_enumeration.addEnumeration(unicode_value='mm', tag='mm')
uomKind.mph = uomKind._CF_enumeration.addEnumeration(unicode_value='mph', tag='mph')
uomKind.mQ = uomKind._CF_enumeration.addEnumeration(unicode_value='mQ', tag='mQ')
uomKind.MQ = uomKind._CF_enumeration.addEnumeration(unicode_value='MQ', tag='MQ')
uomKind.mQh = uomKind._CF_enumeration.addEnumeration(unicode_value='mQh', tag='mQh')
uomKind.MQh = uomKind._CF_enumeration.addEnumeration(unicode_value='MQh', tag='MQh')
uomKind.mV = uomKind._CF_enumeration.addEnumeration(unicode_value='mV', tag='mV')
uomKind.MV = uomKind._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
uomKind.mV_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='mV RMS', tag='mV_RMS')
uomKind.MV_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='MV RMS', tag='MV_RMS')
uomKind.MVA = uomKind._CF_enumeration.addEnumeration(unicode_value='MVA', tag='MVA')
uomKind.mVA = uomKind._CF_enumeration.addEnumeration(unicode_value='mVA', tag='mVA')
uomKind.mVAh = uomKind._CF_enumeration.addEnumeration(unicode_value='mVAh', tag='mVAh')
uomKind.MVAh = uomKind._CF_enumeration.addEnumeration(unicode_value='MVAh', tag='MVAh')
uomKind.mVAR = uomKind._CF_enumeration.addEnumeration(unicode_value='mVAR', tag='mVAR')
uomKind.MVAR = uomKind._CF_enumeration.addEnumeration(unicode_value='MVAR', tag='MVAR')
uomKind.mVARh = uomKind._CF_enumeration.addEnumeration(unicode_value='mVARh', tag='mVARh')
uomKind.MVARh = uomKind._CF_enumeration.addEnumeration(unicode_value='MVARh', tag='MVARh')
uomKind.MVsquared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='MVsquared RMS', tag='MVsquared_RMS')
uomKind.mVsquared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='mVsquared RMS', tag='mVsquared_RMS')
uomKind.MW = uomKind._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
uomKind.mW = uomKind._CF_enumeration.addEnumeration(unicode_value='mW', tag='mW')
uomKind.MWh = uomKind._CF_enumeration.addEnumeration(unicode_value='MWh', tag='MWh')
uomKind.mWh = uomKind._CF_enumeration.addEnumeration(unicode_value='mWh', tag='mWh')
uomKind.Nbr_of_amps_T_H_D__excess = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of amps T.H.D. excess', tag='Nbr_of_amps_T_H_D__excess')
uomKind.Nbr_of_demand_resets = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of demand resets', tag='Nbr_of_demand_resets')
uomKind.Nbr_of_encoder_tamper = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of encoder tamper', tag='Nbr_of_encoder_tamper')
uomKind.Nbr_of_excursion_high = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of excursion high', tag='Nbr_of_excursion_high')
uomKind.Nbr_of_excursion_low = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of excursion low', tag='Nbr_of_excursion_low')
uomKind.Nbr_of_inversion = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of inversion', tag='Nbr_of_inversion')
uomKind.Nbr_of_physical_tamper = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of physical tamper', tag='Nbr_of_physical_tamper')
uomKind.Nbr_of_power_loss = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of power loss', tag='Nbr_of_power_loss')
uomKind.Nbr_of_power_outage = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of power outage', tag='Nbr_of_power_outage')
uomKind.Nbr_of_pulse = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of pulse', tag='Nbr_of_pulse')
uomKind.Nbr_of_removal = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of removal', tag='Nbr_of_removal')
uomKind.Nbr_of_reprogramming = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of reprogramming', tag='Nbr_of_reprogramming')
uomKind.Nbr_of_reverse_rotation = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of reverse rotation', tag='Nbr_of_reverse_rotation')
uomKind.Nbr_of_sag = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of sag', tag='Nbr_of_sag')
uomKind.Nbr_of_swells = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of swells', tag='Nbr_of_swells')
uomKind.Nbr_of_times_programmed = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of times programmed', tag='Nbr_of_times_programmed')
uomKind.Nbr_of_V_T_H_D__excess = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of V T.H.D. excess', tag='Nbr_of_V_T_H_D__excess')
uomKind.Nbr_of_voltage_unbalance = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of voltage unbalance', tag='Nbr_of_voltage_unbalance')
uomKind.Nbr_of_watchdog = uomKind._CF_enumeration.addEnumeration(unicode_value='Nbr of watchdog', tag='Nbr_of_watchdog')
uomKind.Normal_voltage_period = uomKind._CF_enumeration.addEnumeration(unicode_value='Normal voltage period', tag='Normal_voltage_period')
uomKind.percent = uomKind._CF_enumeration.addEnumeration(unicode_value='percent', tag='percent')
uomKind.percent_relative_humidity = uomKind._CF_enumeration.addEnumeration(unicode_value='percent relative humidity', tag='percent_relative_humidity')
uomKind.PH_factor = uomKind._CF_enumeration.addEnumeration(unicode_value='PH factor', tag='PH_factor')
uomKind.pounds_per_square_foot = uomKind._CF_enumeration.addEnumeration(unicode_value='pounds per square foot', tag='pounds_per_square_foot')
uomKind.Power_factor = uomKind._CF_enumeration.addEnumeration(unicode_value='Power factor', tag='Power_factor')
uomKind.PPM_chlorine = uomKind._CF_enumeration.addEnumeration(unicode_value='PPM chlorine', tag='PPM_chlorine')
uomKind.PPM_lead = uomKind._CF_enumeration.addEnumeration(unicode_value='PPM lead', tag='PPM_lead')
uomKind.PPM_odorant = uomKind._CF_enumeration.addEnumeration(unicode_value='PPM odorant', tag='PPM_odorant')
uomKind.PPM_SO2 = uomKind._CF_enumeration.addEnumeration(unicode_value='PPM SO2', tag='PPM_SO2')
uomKind.Q = uomKind._CF_enumeration.addEnumeration(unicode_value='Q', tag='Q')
uomKind.Qh = uomKind._CF_enumeration.addEnumeration(unicode_value='Qh', tag='Qh')
uomKind.Sense_input = uomKind._CF_enumeration.addEnumeration(unicode_value='Sense input', tag='Sense_input')
uomKind.Static_pascal = uomKind._CF_enumeration.addEnumeration(unicode_value='Static pascal', tag='Static_pascal')
uomKind.Static_pound_per_square_inch = uomKind._CF_enumeration.addEnumeration(unicode_value='Static pound per square inch', tag='Static_pound_per_square_inch')
uomKind.T_H_D__Current = uomKind._CF_enumeration.addEnumeration(unicode_value='T.H.D. Current', tag='T_H_D__Current')
uomKind.T_H_D__Voltage = uomKind._CF_enumeration.addEnumeration(unicode_value='T.H.D. Voltage', tag='T_H_D__Voltage')
uomKind.Therm = uomKind._CF_enumeration.addEnumeration(unicode_value='Therm', tag='Therm')
uomKind.Therm_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='Therm per Hr', tag='Therm_per_Hr')
uomKind.Time = uomKind._CF_enumeration.addEnumeration(unicode_value='Time', tag='Time')
uomKind.turbidity = uomKind._CF_enumeration.addEnumeration(unicode_value='turbidity', tag='turbidity')
uomKind.US_gl = uomKind._CF_enumeration.addEnumeration(unicode_value='US gl', tag='US_gl')
uomKind.US_gl_per_Hr = uomKind._CF_enumeration.addEnumeration(unicode_value='US gl per Hr', tag='US_gl_per_Hr')
uomKind.V = uomKind._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
uomKind.V_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='V RMS', tag='V_RMS')
uomKind.VA = uomKind._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
uomKind.VAh = uomKind._CF_enumeration.addEnumeration(unicode_value='VAh', tag='VAh')
uomKind.VAR = uomKind._CF_enumeration.addEnumeration(unicode_value='VAR', tag='VAR')
uomKind.VARh = uomKind._CF_enumeration.addEnumeration(unicode_value='VARh', tag='VARh')
uomKind.Voltage_phase_angle = uomKind._CF_enumeration.addEnumeration(unicode_value='Voltage phase angle', tag='Voltage_phase_angle')
uomKind.Vsquared_RMS = uomKind._CF_enumeration.addEnumeration(unicode_value='Vsquared RMS', tag='Vsquared_RMS')
uomKind.W = uomKind._CF_enumeration.addEnumeration(unicode_value='W', tag='W')
uomKind.Wh = uomKind._CF_enumeration.addEnumeration(unicode_value='Wh', tag='Wh')
uomKind.Other = uomKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
uomKind._InitializeFacetMap(uomKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'uomKind', uomKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}variantCodeStatusKind
class variantCodeStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'variantCodeStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6063, 1)
    _Documentation = None
variantCodeStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=variantCodeStatusKind, enum_prefix=None)
variantCodeStatusKind.Active = variantCodeStatusKind._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
variantCodeStatusKind.Inactive = variantCodeStatusKind._CF_enumeration.addEnumeration(unicode_value='Inactive', tag='Inactive')
variantCodeStatusKind.Other = variantCodeStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
variantCodeStatusKind._InitializeFacetMap(variantCodeStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'variantCodeStatusKind', variantCodeStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}variantTypeKind
class variantTypeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A type name that would specify the purpose of the assembly variant used. The enumeration list includes: Unknown, PoleVar, WireVar, NeutVar, MiscVar, Var1, Var2, Var3, Var4 and Other.  A vendor may use any other value by choosing "Other" from this list and including the optional otherKind attribute, which SHALL be populated with the desired value. Only one variant may be used on a specific materialManagementAssembly."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'variantTypeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6084, 1)
    _Documentation = 'A type name that would specify the purpose of the assembly variant used. The enumeration list includes: Unknown, PoleVar, WireVar, NeutVar, MiscVar, Var1, Var2, Var3, Var4 and Other.  A vendor may use any other value by choosing "Other" from this list and including the optional otherKind attribute, which SHALL be populated with the desired value. Only one variant may be used on a specific materialManagementAssembly.'
variantTypeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=variantTypeKind, enum_prefix=None)
variantTypeKind.Unknown = variantTypeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
variantTypeKind.Pole = variantTypeKind._CF_enumeration.addEnumeration(unicode_value='Pole', tag='Pole')
variantTypeKind.Wire = variantTypeKind._CF_enumeration.addEnumeration(unicode_value='Wire', tag='Wire')
variantTypeKind.Neutral = variantTypeKind._CF_enumeration.addEnumeration(unicode_value='Neutral', tag='Neutral')
variantTypeKind.Misc = variantTypeKind._CF_enumeration.addEnumeration(unicode_value='Misc', tag='Misc')
variantTypeKind.Other = variantTypeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
variantTypeKind._InitializeFacetMap(variantTypeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'variantTypeKind', variantTypeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}verifiedElementActionKind
class verifiedElementActionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'verifiedElementActionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6108, 1)
    _Documentation = None
verifiedElementActionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=verifiedElementActionKind, enum_prefix=None)
verifiedElementActionKind.Unknown = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
verifiedElementActionKind.VerifiedOpen = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='VerifiedOpen', tag='VerifiedOpen')
verifiedElementActionKind.VerifiedBreak = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='VerifiedBreak', tag='VerifiedBreak')
verifiedElementActionKind.VerifiedClosedNoPower = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='VerifiedClosedNoPower', tag='VerifiedClosedNoPower')
verifiedElementActionKind.VerifiedClosedWithPower = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='VerifiedClosedWithPower', tag='VerifiedClosedWithPower')
verifiedElementActionKind.TempOpen = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='TempOpen', tag='TempOpen')
verifiedElementActionKind.TempBreak = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='TempBreak', tag='TempBreak')
verifiedElementActionKind.TempClosed = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='TempClosed', tag='TempClosed')
verifiedElementActionKind.NormalOrRestored = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='NormalOrRestored', tag='NormalOrRestored')
verifiedElementActionKind.NoChange = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='NoChange', tag='NoChange')
verifiedElementActionKind.Other = verifiedElementActionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
verifiedElementActionKind._InitializeFacetMap(verifiedElementActionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'verifiedElementActionKind', verifiedElementActionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}voltageUnits
class voltageUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'voltageUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6159, 1)
    _Documentation = None
voltageUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=voltageUnits, enum_prefix=None)
voltageUnits.Unknown = voltageUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
voltageUnits.V = voltageUnits._CF_enumeration.addEnumeration(unicode_value='V', tag='V')
voltageUnits.kV = voltageUnits._CF_enumeration.addEnumeration(unicode_value='kV', tag='kV')
voltageUnits.MV = voltageUnits._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
voltageUnits.GV = voltageUnits._CF_enumeration.addEnumeration(unicode_value='GV', tag='GV')
voltageUnits.mV = voltageUnits._CF_enumeration.addEnumeration(unicode_value='mV', tag='mV')
voltageUnits.microV = voltageUnits._CF_enumeration.addEnumeration(unicode_value='microV', tag='microV')
voltageUnits.PerUnit = voltageUnits._CF_enumeration.addEnumeration(unicode_value='PerUnit', tag='PerUnit')
voltageUnits.Percent = voltageUnits._CF_enumeration.addEnumeration(unicode_value='Percent', tag='Percent')
voltageUnits.Other = voltageUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
voltageUnits._InitializeFacetMap(voltageUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'voltageUnits', voltageUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}weightUnits
class weightUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'weightUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6173, 1)
    _Documentation = None
weightUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=weightUnits, enum_prefix=None)
weightUnits.Unknown = weightUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
weightUnits.Pound = weightUnits._CF_enumeration.addEnumeration(unicode_value='Pound', tag='Pound')
weightUnits.Kilogram = weightUnits._CF_enumeration.addEnumeration(unicode_value='Kilogram', tag='Kilogram')
weightUnits.Gram = weightUnits._CF_enumeration.addEnumeration(unicode_value='Gram', tag='Gram')
weightUnits.Centigram = weightUnits._CF_enumeration.addEnumeration(unicode_value='Centigram', tag='Centigram')
weightUnits.Milligram = weightUnits._CF_enumeration.addEnumeration(unicode_value='Milligram', tag='Milligram')
weightUnits.Microgram = weightUnits._CF_enumeration.addEnumeration(unicode_value='Microgram', tag='Microgram')
weightUnits.Tonne = weightUnits._CF_enumeration.addEnumeration(unicode_value='Tonne', tag='Tonne')
weightUnits.Grain = weightUnits._CF_enumeration.addEnumeration(unicode_value='Grain', tag='Grain')
weightUnits.Ounce = weightUnits._CF_enumeration.addEnumeration(unicode_value='Ounce', tag='Ounce')
weightUnits.Stone = weightUnits._CF_enumeration.addEnumeration(unicode_value='Stone', tag='Stone')
weightUnits.LongTon = weightUnits._CF_enumeration.addEnumeration(unicode_value='LongTon', tag='LongTon')
weightUnits.ShortTon = weightUnits._CF_enumeration.addEnumeration(unicode_value='ShortTon', tag='ShortTon')
weightUnits.Other = weightUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
weightUnits._InitializeFacetMap(weightUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'weightUnits', weightUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}windingCodeKind
class windingCodeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Transformer winding connection code."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'windingCodeKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6202, 1)
    _Documentation = 'Transformer winding connection code.'
windingCodeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=windingCodeKind, enum_prefix=None)
windingCodeKind.Unknown = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
windingCodeKind.DYOne = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='DYOne', tag='DYOne')
windingCodeKind.YY = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='YY', tag='YY')
windingCodeKind.DY = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='DY', tag='DY')
windingCodeKind.GroundedYD = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='GroundedYD', tag='GroundedYD')
windingCodeKind.UngroundedYD = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='UngroundedYD', tag='UngroundedYD')
windingCodeKind.OpenYD = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='OpenYD', tag='OpenYD')
windingCodeKind.DD = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='DD', tag='DD')
windingCodeKind.YYGroundedImpedance = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='YYGroundedImpedance', tag='YYGroundedImpedance')
windingCodeKind.YY3PhCoreType = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='YY3PhCoreType', tag='YY3PhCoreType')
windingCodeKind.DDOne = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='DDOne', tag='DDOne')
windingCodeKind.DDOpen = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='DDOpen', tag='DDOpen')
windingCodeKind.YYDGrounded = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='YYDGrounded', tag='YYDGrounded')
windingCodeKind.YDOne = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='YDOne', tag='YDOne')
windingCodeKind.DYOpen = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='DYOpen', tag='DYOpen')
windingCodeKind.CenterTapSecondary = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='CenterTapSecondary', tag='CenterTapSecondary')
windingCodeKind.Other = windingCodeKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
windingCodeKind._InitializeFacetMap(windingCodeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'windingCodeKind', windingCodeKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}windingConnectionKind
class windingConnectionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Connection for the transformer winding."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'windingConnectionKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6237, 1)
    _Documentation = 'Connection for the transformer winding.'
windingConnectionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=windingConnectionKind, enum_prefix=None)
windingConnectionKind.Unknown = windingConnectionKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
windingConnectionKind.Delta = windingConnectionKind._CF_enumeration.addEnumeration(unicode_value='Delta', tag='Delta')
windingConnectionKind.Wye = windingConnectionKind._CF_enumeration.addEnumeration(unicode_value='Wye', tag='Wye')
windingConnectionKind.Zigzag = windingConnectionKind._CF_enumeration.addEnumeration(unicode_value='Zigzag', tag='Zigzag')
windingConnectionKind.Center_tap = windingConnectionKind._CF_enumeration.addEnumeration(unicode_value='Center tap', tag='Center_tap')
windingConnectionKind.Other = windingConnectionKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
windingConnectionKind._InitializeFacetMap(windingConnectionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'windingConnectionKind', windingConnectionKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}workRequestStatusKind
class workRequestStatusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workRequestStatusKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6261, 1)
    _Documentation = None
workRequestStatusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=workRequestStatusKind, enum_prefix=None)
workRequestStatusKind.Unknown = workRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
workRequestStatusKind.Received = workRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='Received', tag='Received')
workRequestStatusKind.Approved = workRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='Approved', tag='Approved')
workRequestStatusKind.Denied = workRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='Denied', tag='Denied')
workRequestStatusKind.Other = workRequestStatusKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
workRequestStatusKind._InitializeFacetMap(workRequestStatusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'workRequestStatusKind', workRequestStatusKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}workStatusCategoryKind
class workStatusCategoryKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This type may be used by the system of record to categorize work statuses to allow data requests to be sorted into groups of like work Status.  The system or records own the mapping between workStatusCodes and workStatusCategories."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workStatusCategoryKind')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6284, 1)
    _Documentation = 'This type may be used by the system of record to categorize work statuses to allow data requests to be sorted into groups of like work Status.  The system or records own the mapping between workStatusCodes and workStatusCategories.'
workStatusCategoryKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=workStatusCategoryKind, enum_prefix=None)
workStatusCategoryKind.Active = workStatusCategoryKind._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
workStatusCategoryKind.Other = workStatusCategoryKind._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
workStatusCategoryKind.Inactive = workStatusCategoryKind._CF_enumeration.addEnumeration(unicode_value='Inactive', tag='Inactive')
workStatusCategoryKind.All = workStatusCategoryKind._CF_enumeration.addEnumeration(unicode_value='All', tag='All')
workStatusCategoryKind._InitializeFacetMap(workStatusCategoryKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'workStatusCategoryKind', workStatusCategoryKind)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}zUnits
class zUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'zUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6295, 1)
    _Documentation = None
zUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=zUnits, enum_prefix=None)
zUnits.Unknown = zUnits._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
zUnits.Ohms = zUnits._CF_enumeration.addEnumeration(unicode_value='Ohms', tag='Ohms')
zUnits.Percent = zUnits._CF_enumeration.addEnumeration(unicode_value='Percent', tag='Percent')
zUnits.PerUnit = zUnits._CF_enumeration.addEnumeration(unicode_value='PerUnit', tag='PerUnit')
zUnits.Total = zUnits._CF_enumeration.addEnumeration(unicode_value='Total', tag='Total')
zUnits.Other = zUnits._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
zUnits._InitializeFacetMap(zUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'zUnits', zUnits)

# Atomic simple type: {http://www.multispeak.org/V5.0/enumerations}serviceLimitType
class serviceLimitType (limitType):

    """This enumeration along with a rated current or rated voltage indicates a limit of the effectiveness of a tariff. For instance for a tariff that is effective for three-phase service at 120/208V, the serviceVoltage would include 208V, and serviceLimitType would be "EQ"; phases would be "3". """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceLimitType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5020, 1)
    _Documentation = 'This enumeration along with a rated current or rated voltage indicates a limit of the effectiveness of a tariff. For instance for a tariff that is effective for three-phase service at 120/208V, the serviceVoltage would include 208V, and serviceLimitType would be "EQ"; phases would be "3". '
serviceLimitType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'serviceLimitType', serviceLimitType)

# Complex type {http://www.multispeak.org/V5.0/enumerations}accountStatus with content type SIMPLE
class accountStatus (pyxb.binding.basis.complexTypeDefinition):
    """The status of a customer account that is associated with the customer's service point."""
    _TypeDefinition = accountStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'accountStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 39, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is accountStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_accountStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 45, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 45, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'accountStatus', accountStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}actionCode with content type SIMPLE
class actionCode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}actionCode with content type SIMPLE"""
    _TypeDefinition = actionCodeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actionCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 114, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is actionCodeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_actionCode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 117, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 117, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'actionCode', actionCode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}actionTaken with content type SIMPLE
class actionTaken (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}actionTaken with content type SIMPLE"""
    _TypeDefinition = actionTakenKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actionTaken')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 146, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is actionTakenKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_actionTaken_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 149, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 149, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    
    # Attribute disconnectionMeans uses Python identifier disconnectionMeans
    __disconnectionMeans = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'disconnectionMeans'), 'disconnectionMeans', '__httpwww_multispeak_orgV5_0enumerations_actionTaken_disconnectionMeans', pyxb.binding.datatypes.string)
    __disconnectionMeans._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 154, 4)
    __disconnectionMeans._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 154, 4)
    
    disconnectionMeans = property(__disconnectionMeans.value, __disconnectionMeans.set, None, 'If the actionTaken enumeration is "Disconnected", this attribute can give additional information about how the disconnection was performed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind,
        __disconnectionMeans.name() : __disconnectionMeans
    })
Namespace.addCategoryObject('typeBinding', 'actionTaken', actionTaken)


# Complex type {http://www.multispeak.org/V5.0/enumerations}addressType with content type SIMPLE
class addressType (pyxb.binding.basis.complexTypeDefinition):
    """Type of address. For instance, billing, mailing, service location, etc."""
    _TypeDefinition = addressKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addressType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 200, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is addressKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_addressType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 206, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 206, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'addressType', addressType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}allowableTransactionType with content type SIMPLE
class allowableTransactionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}allowableTransactionType with content type SIMPLE"""
    _TypeDefinition = allowableTransactionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'allowableTransactionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 227, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is allowableTransactionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_allowableTransactionType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 230, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 230, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'allowableTransactionType', allowableTransactionType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}analogCondition with content type SIMPLE
class analogCondition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}analogCondition with content type SIMPLE"""
    _TypeDefinition = analogConditionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'analogCondition')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 238, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is analogConditionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_analogCondition_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 241, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 241, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'analogCondition', analogCondition)


# Complex type {http://www.multispeak.org/V5.0/enumerations}assetStatus with content type SIMPLE
class assetStatus (pyxb.binding.basis.complexTypeDefinition):
    """This is a description of the status of an asset."""
    _TypeDefinition = assetStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'assetStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 307, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is assetStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_assetStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 313, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 313, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'assetStatus', assetStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}assignmentStatus with content type SIMPLE
class assignmentStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}assignmentStatus with content type SIMPLE"""
    _TypeDefinition = assignmentStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'assignmentStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 367, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is assignmentStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_assignmentStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 370, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 370, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'assignmentStatus', assignmentStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}associatedDateType with content type SIMPLE
class associatedDateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}associatedDateType with content type SIMPLE"""
    _TypeDefinition = associatedDateKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'associatedDateType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 424, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is associatedDateKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_associatedDateType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 427, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 427, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'associatedDateType', associatedDateType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}authorizationMode with content type SIMPLE
class authorizationMode (pyxb.binding.basis.complexTypeDefinition):
    """The means by which the recurring payment authorization was received."""
    _TypeDefinition = recurringPaymentAuthorizationModeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'authorizationMode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 435, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is recurringPaymentAuthorizationModeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_authorizationMode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 441, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 441, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'authorizationMode', authorizationMode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}authorizationType with content type SIMPLE
class authorizationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}authorizationType with content type SIMPLE"""
    _TypeDefinition = authorizatonTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'authorizationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 449, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is authorizatonTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_authorizationType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 452, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 452, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'authorizationType', authorizationType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}balanceType with content type SIMPLE
class balanceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}balanceType with content type SIMPLE"""
    _TypeDefinition = balanceKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'balanceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 479, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is balanceKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_balanceType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 482, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 482, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'balanceType', balanceType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}billingItemsType with content type SIMPLE
class billingItemsType (pyxb.binding.basis.complexTypeDefinition):
    """Class of billing terms."""
    _TypeDefinition = billingItemsKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'billingItemsType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 520, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is billingItemsKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_billingItemsType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 526, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 526, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'billingItemsType', billingItemsType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}billingTerms with content type SIMPLE
class billingTerms (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}billingTerms with content type SIMPLE"""
    _TypeDefinition = billingTermsKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'billingTerms')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 534, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is billingTermsKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_billingTerms_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 537, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 537, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'billingTerms', billingTerms)


# Complex type {http://www.multispeak.org/V5.0/enumerations}calculationMethod with content type SIMPLE
class calculationMethod (pyxb.binding.basis.complexTypeDefinition):
    """This element describes whether the variant was chosen by the user or automatically chosen by the software."""
    _TypeDefinition = calculationMethodKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'calculationMethod')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 565, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is calculationMethodKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_calculationMethod_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 571, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 571, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'calculationMethod', calculationMethod)


# Complex type {http://www.multispeak.org/V5.0/enumerations}callBackType with content type SIMPLE
class callBackType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}callBackType with content type SIMPLE"""
    _TypeDefinition = callBackTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'callBackType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 598, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is callBackTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_callBackType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 601, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 601, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'callBackType', callBackType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}capacitorSwitchStatus with content type SIMPLE
class capacitorSwitchStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}capacitorSwitchStatus with content type SIMPLE"""
    _TypeDefinition = capacitorSwitchStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'capacitorSwitchStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 651, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is capacitorSwitchStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_capacitorSwitchStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 654, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 654, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'capacitorSwitchStatus', capacitorSwitchStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}cardinalHeadingType with content type SIMPLE
class cardinalHeadingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}cardinalHeadingType with content type SIMPLE"""
    _TypeDefinition = cardinalHeadingKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cardinalHeadingType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 766, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is cardinalHeadingKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_cardinalHeadingType_otherKind', pyxb.binding.datatypes.string)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 769, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 769, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'cardinalHeadingType', cardinalHeadingType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}CDReasonCode with content type SIMPLE
class CDReasonCode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}CDReasonCode with content type SIMPLE"""
    _TypeDefinition = CDReasonCodeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CDReasonCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 777, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is CDReasonCodeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_CDReasonCode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 780, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 780, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'CDReasonCode', CDReasonCode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}conduitMaterial with content type SIMPLE
class conduitMaterial (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}conduitMaterial with content type SIMPLE"""
    _TypeDefinition = conduitMaterialKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'conduitMaterial')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 822, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is conduitMaterialKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_conduitMaterial_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 825, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 825, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'conduitMaterial', conduitMaterial)


# Complex type {http://www.multispeak.org/V5.0/enumerations}connectivityStatus with content type SIMPLE
class connectivityStatus (pyxb.binding.basis.complexTypeDefinition):
    """This is the commodity flow status for a customer service point.  FOr instance for tan electric service point, this enumeration establishes whether or not the service is connected so that electric power can flow to the service."""
    _TypeDefinition = connectivityStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'connectivityStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 853, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is connectivityStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_connectivityStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 859, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 859, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'connectivityStatus', connectivityStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}constructionGrade with content type SIMPLE
class constructionGrade (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}constructionGrade with content type SIMPLE"""
    _TypeDefinition = constructionGradeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'constructionGrade')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 883, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is constructionGradeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_constructionGrade_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 886, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 886, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'constructionGrade', constructionGrade)


# Complex type {http://www.multispeak.org/V5.0/enumerations}constructionLevel with content type SIMPLE
class constructionLevel (pyxb.binding.basis.complexTypeDefinition):
    """This is the physical level at which the line is constructed."""
    _TypeDefinition = constructionLevelKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'constructionLevel')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 903, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is constructionLevelKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_constructionLevel_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 909, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 909, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'constructionLevel', constructionLevel)


# Complex type {http://www.multispeak.org/V5.0/enumerations}constructionReferenceType with content type SIMPLE
class constructionReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """This enumeration gives context to a constructionItem as part of an ACLineSegment."""
    _TypeDefinition = constructionReferenceKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'constructionReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 941, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is constructionReferenceKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_constructionReferenceType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 947, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 947, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'constructionReferenceType', constructionReferenceType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}constructionType with content type SIMPLE
class constructionType (pyxb.binding.basis.complexTypeDefinition):
    """Construction type code for construction at this location. This field is used to specify whether the units applied to this station use the hot labor estimates or the cold labor estimates.  Suggested enumerations are (Hot and Cold)."""
    _TypeDefinition = constTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'constructionType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 955, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is constTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_constructionType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 961, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 961, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'constructionType', constructionType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}contactRequestStatus with content type SIMPLE
class contactRequestStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}contactRequestStatus with content type SIMPLE"""
    _TypeDefinition = contactRequestStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contactRequestStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 980, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is contactRequestStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_contactRequestStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 983, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 983, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'contactRequestStatus', contactRequestStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}contentEncodingType with content type SIMPLE
class contentEncodingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}contentEncodingType with content type SIMPLE"""
    _TypeDefinition = contentEncodingKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contentEncodingType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1031, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is contentEncodingKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_contentEncodingType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1034, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1034, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'contentEncodingType', contentEncodingType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}controlCode with content type SIMPLE
class controlCode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}controlCode with content type SIMPLE"""
    _TypeDefinition = controlCodeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'controlCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1042, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is controlCodeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_controlCode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1045, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1045, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'controlCode', controlCode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}controlEventType with content type SIMPLE
class controlEventType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}controlEventType with content type SIMPLE"""
    _TypeDefinition = controlEventKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'controlEventType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1072, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is controlEventKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_controlEventType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1075, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1075, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'controlEventType', controlEventType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}controlStatus with content type SIMPLE
class controlStatus (pyxb.binding.basis.complexTypeDefinition):
    """These are the control status indications.  The equivalent DNP 3.0 status codes are:             
Control accepted = 0                                 
Operate message received after arm timer timed out (Select timeout)= 1 Point not operated because point not selected before operation (Point not selected)= 2 Control request not accepted; formatting errors in control action (Formatting errors in control request)= 3                                                                  
Control operation not supported for this point (Control not supported) = 4 Control queue is full = 5                              
Control request not accepted, control hardware problems (Hardware failure)= 6 Point already selected - undefined in DNP 3.0               """
    _TypeDefinition = controlStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'controlStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1083, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is controlStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_controlStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1093, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1093, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'controlStatus', controlStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}cutAction with content type SIMPLE
class cutAction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}cutAction with content type SIMPLE"""
    _TypeDefinition = cutActionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cutAction')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1350, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is cutActionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_cutAction_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1353, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1353, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'cutAction', cutAction)


# Complex type {http://www.multispeak.org/V5.0/enumerations}dayLabel with content type SIMPLE
class dayLabel (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}dayLabel with content type SIMPLE"""
    _TypeDefinition = dayLabelKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dayLabel')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1369, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is dayLabelKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_dayLabel_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1372, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1372, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'dayLabel', dayLabel)


# Complex type {http://www.multispeak.org/V5.0/enumerations}depositStatus with content type SIMPLE
class depositStatus (pyxb.binding.basis.complexTypeDefinition):
    """This enumeration gives the status of this deposit on a customer account."""
    _TypeDefinition = depositStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'depositStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1465, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is depositStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_depositStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1471, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1471, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'depositStatus', depositStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}designRole with content type SIMPLE
class designRole (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}designRole with content type SIMPLE"""
    _TypeDefinition = designRoleKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'designRole')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1499, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is designRoleKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_designRole_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1502, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1502, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'designRole', designRole)


# Complex type {http://www.multispeak.org/V5.0/enumerations}districtType with content type SIMPLE
class districtType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}districtType with content type SIMPLE"""
    _TypeDefinition = districtTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'districtType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1554, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is districtTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_districtType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1557, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1557, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'districtType', districtType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}DRProgramEnrollmentStatus with content type SIMPLE
class DRProgramEnrollmentStatus (pyxb.binding.basis.complexTypeDefinition):
    """The permissible values of DRProgramEnrollmentStatus are: 'Active', 'Inactive', 'Pending', 'Other' and 'Unknown'. Active status means that the DRProgramEnrollment has a participation start date in the past and a participation end date in the future, even if control is not currently active. A status of Inactive implies that the DRProgramEnrollment has a participation start date in the future or a participation end date in the past. A status of Pending means that the DRProgramEnrollDate is in the past, but that the DRProgramEnrollment has a participation start date in the future. The Other and Unknown statuses are included for extensibility, but their use is discouraged. If the DRProgramEnrollmentStatus is set to be Other, the DR Program Enrollment Agent should populate the OtherDRProgramEnrollmentStatus element with the non-standard status value."""
    _TypeDefinition = DRProgramEnrollmentStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DRProgramEnrollmentStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1640, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is DRProgramEnrollmentStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_DRProgramEnrollmentStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1646, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1646, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'DRProgramEnrollmentStatus', DRProgramEnrollmentStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}DRProgramStatus with content type SIMPLE
class DRProgramStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}DRProgramStatus with content type SIMPLE"""
    _TypeDefinition = DRProgramStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DRProgramStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1666, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is DRProgramStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_DRProgramStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1669, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1669, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'DRProgramStatus', DRProgramStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}electricTopologyElementType with content type SIMPLE
class electricTopologyElementType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}electricTopologyElementType with content type SIMPLE"""
    _TypeDefinition = electricTopologyElementKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'electricTopologyElementType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1733, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is electricTopologyElementKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_electricTopologyElementType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1736, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1736, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'electricTopologyElementType', electricTopologyElementType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}eMailType with content type SIMPLE
class eMailType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}eMailType with content type SIMPLE"""
    _TypeDefinition = eMailTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'eMailType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1744, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is eMailTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_eMailType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1747, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1747, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'eMailType', eMailType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}endDeviceStateType with content type SIMPLE
class endDeviceStateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}endDeviceStateType with content type SIMPLE"""
    _TypeDefinition = endDeviceStateKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'endDeviceStateType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1808, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is endDeviceStateKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_endDeviceStateType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1811, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1811, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'endDeviceStateType', endDeviceStateType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}equipmentType with content type SIMPLE
class equipmentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}equipmentType with content type SIMPLE"""
    _TypeDefinition = equipmentTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equipmentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1819, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is equipmentTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_equipmentType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1822, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 1822, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'equipmentType', equipmentType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}fieldNameType with content type SIMPLE
class fieldNameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}fieldNameType with content type SIMPLE"""
    _TypeDefinition = fieldNameKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fieldNameType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2491, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is fieldNameKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_fieldNameType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2494, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2494, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'fieldNameType', fieldNameType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}guyWireSizeUnits with content type SIMPLE
class guyWireSizeUnits (pyxb.binding.basis.complexTypeDefinition):
    """Guy wire diameter units."""
    _TypeDefinition = guyWireSizeUnitKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'guyWireSizeUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2632, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is guyWireSizeUnitKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_guyWireSizeUnits_otherKind', pyxb.binding.datatypes.string)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2638, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2638, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'guyWireSizeUnits', guyWireSizeUnits)


# Complex type {http://www.multispeak.org/V5.0/enumerations}guyWireType with content type SIMPLE
class guyWireType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}guyWireType with content type SIMPLE"""
    _TypeDefinition = guyWireKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'guyWireType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2646, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is guyWireKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_guyWireType_otherKind', pyxb.binding.datatypes.string)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2649, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2649, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'guyWireType', guyWireType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}historyEventType with content type SIMPLE
class historyEventType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}historyEventType with content type SIMPLE"""
    _TypeDefinition = historyEventTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'historyEventType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2657, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is historyEventTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_historyEventType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2660, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2660, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'historyEventType', historyEventType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}ignitionState with content type SIMPLE
class ignitionState (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}ignitionState with content type SIMPLE"""
    _TypeDefinition = ignitionStateKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ignitionState')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2687, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is ignitionStateKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_ignitionState_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2690, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2690, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'ignitionState', ignitionState)


# Complex type {http://www.multispeak.org/V5.0/enumerations}incidentPriorityType with content type SIMPLE
class incidentPriorityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}incidentPriorityType with content type SIMPLE"""
    _TypeDefinition = incidentPriorityKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentPriorityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2720, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is incidentPriorityKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_incidentPriorityType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2723, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2723, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'incidentPriorityType', incidentPriorityType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}incidentReporterType with content type SIMPLE
class incidentReporterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}incidentReporterType with content type SIMPLE"""
    _TypeDefinition = incidentReporterKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentReporterType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2757, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is incidentReporterKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_incidentReporterType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2760, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2760, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'incidentReporterType', incidentReporterType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}incidentReportSource with content type SIMPLE
class incidentReportSource (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}incidentReportSource with content type SIMPLE"""
    _TypeDefinition = incidentReportSourceKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentReportSource')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2768, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is incidentReportSourceKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_incidentReportSource_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2771, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2771, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'incidentReportSource', incidentReportSource)


# Complex type {http://www.multispeak.org/V5.0/enumerations}incidentReportStatus with content type SIMPLE
class incidentReportStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}incidentReportStatus with content type SIMPLE"""
    _TypeDefinition = incidentReportStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentReportStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2828, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is incidentReportStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_incidentReportStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2831, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2831, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'incidentReportStatus', incidentReportStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}incidentResultType with content type SIMPLE
class incidentResultType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}incidentResultType with content type SIMPLE"""
    _TypeDefinition = incidentResultKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'incidentResultType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2870, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is incidentResultKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_incidentResultType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2873, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2873, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'incidentResultType', incidentResultType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}includeAssemblyData with content type SIMPLE
class includeAssemblyData (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}includeAssemblyData with content type SIMPLE"""
    _TypeDefinition = includeAssemblyDataKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'includeAssemblyData')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2881, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is includeAssemblyDataKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_includeAssemblyData_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2884, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 2884, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'includeAssemblyData', includeAssemblyData)


# Complex type {http://www.multispeak.org/V5.0/enumerations}lineConstructionEntryType with content type SIMPLE
class lineConstructionEntryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}lineConstructionEntryType with content type SIMPLE"""
    _TypeDefinition = lineConstructionEntryKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lineConstructionEntryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3037, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is lineConstructionEntryKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_lineConstructionEntryType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3040, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3040, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'lineConstructionEntryType', lineConstructionEntryType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}lineRole with content type SIMPLE
class lineRole (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}lineRole with content type SIMPLE"""
    _TypeDefinition = lineRoleKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lineRole')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3057, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is lineRoleKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_lineRole_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3060, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3060, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'lineRole', lineRole)


# Complex type {http://www.multispeak.org/V5.0/enumerations}loadActionCode with content type SIMPLE
class loadActionCode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}loadActionCode with content type SIMPLE"""
    _TypeDefinition = loadActionCodeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'loadActionCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3078, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is loadActionCodeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_loadActionCode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3081, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3081, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'loadActionCode', loadActionCode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}loadingDistrict with content type SIMPLE
class loadingDistrict (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}loadingDistrict with content type SIMPLE"""
    _TypeDefinition = loadingDistrictKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'loadingDistrict')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3130, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is loadingDistrictKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_loadingDistrict_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3133, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3133, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'loadingDistrict', loadingDistrict)


# Complex type {http://www.multispeak.org/V5.0/enumerations}locationHazardType with content type SIMPLE
class locationHazardType (pyxb.binding.basis.complexTypeDefinition):
    """This value describes hazards associated with this location.  Examples of locationHazardTypes include "Customer", "Animal", "Safety", "Access", etc.  """
    _TypeDefinition = locationHazardKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationHazardType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3180, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is locationHazardKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_locationHazardType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3186, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3186, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'locationHazardType', locationHazardType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}locationOutageStatus with content type SIMPLE
class locationOutageStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}locationOutageStatus with content type SIMPLE"""
    _TypeDefinition = locationOutageStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationOutageStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3194, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is locationOutageStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_locationOutageStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3197, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3197, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'locationOutageStatus', locationOutageStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}locationPriorityType with content type SIMPLE
class locationPriorityType (pyxb.binding.basis.complexTypeDefinition):
    """This is a classification of special priority for a customer, serviceLocation, or usagePoint."""
    _TypeDefinition = locationPriorityKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationPriorityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3234, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is locationPriorityKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_locationPriorityType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3240, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3240, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'locationPriorityType', locationPriorityType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}locationTrackingTriggerEvent with content type SIMPLE
class locationTrackingTriggerEvent (pyxb.binding.basis.complexTypeDefinition):
    """The is the event that triggered the collection of location tracking (AVL) data."""
    _TypeDefinition = LTTriggerEventKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationTrackingTriggerEvent')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3248, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is LTTriggerEventKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_locationTrackingTriggerEvent_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3254, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3254, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'locationTrackingTriggerEvent', locationTrackingTriggerEvent)


# Complex type {http://www.multispeak.org/V5.0/enumerations}materialClass with content type SIMPLE
class materialClass (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}materialClass with content type SIMPLE"""
    _TypeDefinition = materialClassKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'materialClass')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3308, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is materialClassKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_materialClass_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3311, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3311, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'materialClass', materialClass)


# Complex type {http://www.multispeak.org/V5.0/enumerations}materialUnits with content type SIMPLE
class materialUnits (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}materialUnits with content type SIMPLE"""
    _TypeDefinition = materialUnitsKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'materialUnits')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3329, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is materialUnitsKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_materialUnits_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3332, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3332, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'materialUnits', materialUnits)


# Complex type {http://www.multispeak.org/V5.0/enumerations}measurementDeviceStatus with content type SIMPLE
class measurementDeviceStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}measurementDeviceStatus with content type SIMPLE"""
    _TypeDefinition = measurementDeviceStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measurementDeviceStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3381, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is measurementDeviceStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_measurementDeviceStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3384, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3384, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'measurementDeviceStatus', measurementDeviceStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}measurementDeviceType with content type SIMPLE
class measurementDeviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}measurementDeviceType with content type SIMPLE"""
    _TypeDefinition = measurementDeviceKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'measurementDeviceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3400, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is measurementDeviceKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_measurementDeviceType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3403, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3403, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'measurementDeviceType', measurementDeviceType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}messageResultLevel with content type SIMPLE
class messageResultLevel (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}messageResultLevel with content type SIMPLE"""
    _TypeDefinition = messageResultLevelKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'messageResultLevel')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3453, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is messageResultLevelKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_messageResultLevel_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3456, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3456, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'messageResultLevel', messageResultLevel)


# Complex type {http://www.multispeak.org/V5.0/enumerations}meterConnectionStatus with content type SIMPLE
class meterConnectionStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}meterConnectionStatus with content type SIMPLE"""
    _TypeDefinition = meterConnectionStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'meterConnectionStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3476, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is meterConnectionStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_meterConnectionStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3479, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3479, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'meterConnectionStatus', meterConnectionStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}meterStatusType with content type SIMPLE
class meterStatusType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}meterStatusType with content type SIMPLE"""
    _TypeDefinition = meterStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'meterStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3520, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is meterStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_meterStatusType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3523, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3523, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'meterStatusType', meterStatusType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}modelRole with content type SIMPLE
class modelRole (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}modelRole with content type SIMPLE"""
    _TypeDefinition = modelRoleKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'modelRole')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3531, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is modelRoleKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_modelRole_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3534, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3534, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'modelRole', modelRole)


# Complex type {http://www.multispeak.org/V5.0/enumerations}motorStatus with content type SIMPLE
class motorStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}motorStatus with content type SIMPLE"""
    _TypeDefinition = motorStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'motorStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3576, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is motorStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_motorStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3579, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3579, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'motorStatus', motorStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}mountingType with content type SIMPLE
class mountingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}mountingType with content type SIMPLE"""
    _TypeDefinition = mountingKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mountingType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3609, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is mountingKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_mountingType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3612, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3612, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'mountingType', mountingType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}NEMAType with content type SIMPLE
class NEMAType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}NEMAType with content type SIMPLE"""
    _TypeDefinition = NEMAFrameKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NEMAType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3654, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is NEMAFrameKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_NEMAType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3657, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3657, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'NEMAType', NEMAType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}nominalServiceVoltage with content type SIMPLE
class nominalServiceVoltage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}nominalServiceVoltage with content type SIMPLE"""
    _TypeDefinition = nominalServiceVoltageKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nominalServiceVoltage')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3665, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is nominalServiceVoltageKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_nominalServiceVoltage_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3668, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3668, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'nominalServiceVoltage', nominalServiceVoltage)


# Complex type {http://www.multispeak.org/V5.0/enumerations}notificationModeType with content type SIMPLE
class notificationModeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}notificationModeType with content type SIMPLE"""
    _TypeDefinition = notificationModeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'notificationModeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3749, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is notificationModeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_notificationModeType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3752, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3752, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'notificationModeType', notificationModeType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}organizationRole with content type SIMPLE
class organizationRole (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}organizationRole with content type SIMPLE"""
    _TypeDefinition = organizationRoleKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'organizationRole')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3768, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is organizationRoleKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_organizationRole_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3771, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3771, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'organizationRole', organizationRole)


# Complex type {http://www.multispeak.org/V5.0/enumerations}outageHistoryEventType with content type SIMPLE
class outageHistoryEventType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}outageHistoryEventType with content type SIMPLE"""
    _TypeDefinition = outageHistoryEventTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outageHistoryEventType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3800, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is outageHistoryEventTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_outageHistoryEventType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3803, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3803, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'outageHistoryEventType', outageHistoryEventType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}outagePriority with content type SIMPLE
class outagePriority (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}outagePriority with content type SIMPLE"""
    _TypeDefinition = outagePriorityKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outagePriority')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3832, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is outagePriorityKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_outagePriority_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3835, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3835, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'outagePriority', outagePriority)


# Complex type {http://www.multispeak.org/V5.0/enumerations}outageReasonCategory with content type SIMPLE
class outageReasonCategory (pyxb.binding.basis.complexTypeDefinition):
    """Category for the outage reporting information.  Descriptions for the category should be: "Outage Cause - This is the primary cause of the outage ; "Equipment Failure" - This is the material or equipment that failed, producing the outage; "Voltage Level" - this is the phase-to-phase voltage of the system that failed; "Weather Condition" - The weather conditions at the site of the failure at the time the outage occurred (This is not to be used for reporting a weather condition that was the primary cause of the outage - that should be reported using Outage Cause; "System Characterization" The kind of customer density at the location of the outage; "Responsible System" - The portion of the electrical system that was responsible for the outage; "Outage Condition" - The condition that the system was subject to at the time of the fault (For example, was it a Major Event Day as defined by IEEE 1366); "Interrupting Device" - The kind of interrupting device that protected customers in response to the fault; "Interrupting Device Initiation" - The manner in which the interrupting device operated at the time of the fault; "Customer Restoration" - The manner in which the customer's service was restored."""
    _TypeDefinition = outageReasonCategoryKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outageReasonCategory')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3853, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is outageReasonCategoryKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_outageReasonCategory_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3859, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3859, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'outageReasonCategory', outageReasonCategory)


# Complex type {http://www.multispeak.org/V5.0/enumerations}outageState with content type SIMPLE
class outageState (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}outageState with content type SIMPLE"""
    _TypeDefinition = outageStateKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outageState')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3884, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is outageStateKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_outageState_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3887, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3887, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'outageState', outageState)


# Complex type {http://www.multispeak.org/V5.0/enumerations}outageType with content type SIMPLE
class outageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}outageType with content type SIMPLE"""
    _TypeDefinition = outageKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outageType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3906, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is outageKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_outageType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3909, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3909, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'outageType', outageType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}PANCommissionStatus with content type SIMPLE
class PANCommissionStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}PANCommissionStatus with content type SIMPLE"""
    _TypeDefinition = PANCommissionStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PANCommissionStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3917, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is PANCommissionStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_PANCommissionStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3920, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3920, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'PANCommissionStatus', PANCommissionStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}PANRegistrationStatus with content type SIMPLE
class PANRegistrationStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}PANRegistrationStatus with content type SIMPLE"""
    _TypeDefinition = PANRegistrationStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PANRegistrationStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3948, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is PANRegistrationStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_PANRegistrationStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3951, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 3951, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'PANRegistrationStatus', PANRegistrationStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}phaseStatusType with content type SIMPLE
class phaseStatusType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}phaseStatusType with content type SIMPLE"""
    _TypeDefinition = phaseStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phaseStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4035, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is phaseStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_phaseStatusType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4038, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4038, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'phaseStatusType', phaseStatusType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}phoneType with content type SIMPLE
class phoneType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}phoneType with content type SIMPLE"""
    _TypeDefinition = phoneTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phoneType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4046, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is phoneTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_phoneType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4049, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4049, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'phoneType', phoneType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}poleClass with content type SIMPLE
class poleClass (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}poleClass with content type SIMPLE"""
    _TypeDefinition = poleClassKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'poleClass')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4152, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is poleClassKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_poleClass_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4155, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4155, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'poleClass', poleClass)


# Complex type {http://www.multispeak.org/V5.0/enumerations}poleType with content type SIMPLE
class poleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}poleType with content type SIMPLE"""
    _TypeDefinition = poleTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'poleType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4189, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is poleTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_poleType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4192, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4192, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    
    # Attribute poleSubType uses Python identifier poleSubType
    __poleSubType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'poleSubType'), 'poleSubType', '__httpwww_multispeak_orgV5_0enumerations_poleType_poleSubType', pyxb.binding.datatypes.string)
    __poleSubType._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4197, 4)
    __poleSubType._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4197, 4)
    
    poleSubType = property(__poleSubType.value, __poleSubType.set, None, 'This is additional information about the pole type.  For instance, for a wood pole type, this would be the species.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind,
        __poleSubType.name() : __poleSubType
    })
Namespace.addCategoryObject('typeBinding', 'poleType', poleType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}poleUse with content type SIMPLE
class poleUse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}poleUse with content type SIMPLE"""
    _TypeDefinition = poleUseKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'poleUse')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4222, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is poleUseKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_poleUse_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4225, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4225, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'poleUse', poleUse)


# Complex type {http://www.multispeak.org/V5.0/enumerations}powerStatus with content type SIMPLE
class powerStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}powerStatus with content type SIMPLE"""
    _TypeDefinition = powerStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'powerStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4264, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is powerStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_powerStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4267, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4267, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'powerStatus', powerStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}premisesDisplayMessageStatusType with content type SIMPLE
class premisesDisplayMessageStatusType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}premisesDisplayMessageStatusType with content type SIMPLE"""
    _TypeDefinition = premisesDisplayMessageStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'premisesDisplayMessageStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4325, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is premisesDisplayMessageStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_premisesDisplayMessageStatusType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4328, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4328, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'premisesDisplayMessageStatusType', premisesDisplayMessageStatusType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}premisesDisplayMessageType with content type SIMPLE
class premisesDisplayMessageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}premisesDisplayMessageType with content type SIMPLE"""
    _TypeDefinition = premisesDisplayMessageKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'premisesDisplayMessageType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4336, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is premisesDisplayMessageKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_premisesDisplayMessageType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4339, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4339, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'premisesDisplayMessageType', premisesDisplayMessageType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}presumedElementStateType with content type SIMPLE
class presumedElementStateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}presumedElementStateType with content type SIMPLE"""
    _TypeDefinition = presumedElementStateKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'presumedElementStateType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4406, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is presumedElementStateKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_presumedElementStateType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4409, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4409, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'presumedElementStateType', presumedElementStateType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}PTOState with content type SIMPLE
class PTOState (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}PTOState with content type SIMPLE"""
    _TypeDefinition = PTOStateKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PTOState')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4429, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is PTOStateKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_PTOState_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4432, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4432, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'PTOState', PTOState)


# Complex type {http://www.multispeak.org/V5.0/enumerations}qualityDescription with content type SIMPLE
class qualityDescription (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}qualityDescription with content type SIMPLE"""
    _TypeDefinition = qualityDescriptionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'qualityDescription')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4452, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is qualityDescriptionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_qualityDescription_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4455, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4455, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'qualityDescription', qualityDescription)


# Complex type {http://www.multispeak.org/V5.0/enumerations}RCDState with content type SIMPLE
class RCDState (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}RCDState with content type SIMPLE"""
    _TypeDefinition = RCDStateKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RCDState')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4487, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is RCDStateKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_RCDState_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4490, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4490, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'RCDState', RCDState)


# Complex type {http://www.multispeak.org/V5.0/enumerations}regulatorBankConnectionCode with content type SIMPLE
class regulatorBankConnectionCode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}regulatorBankConnectionCode with content type SIMPLE"""
    _TypeDefinition = regulatorBankConnectionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'regulatorBankConnectionCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4643, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is regulatorBankConnectionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_regulatorBankConnectionCode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4646, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4646, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'regulatorBankConnectionCode', regulatorBankConnectionCode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}relationType with content type SIMPLE
class relationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}relationType with content type SIMPLE"""
    _TypeDefinition = relationTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4678, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is relationTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_relationType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4681, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4681, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'relationType', relationType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}relayType with content type SIMPLE
class relayType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}relayType with content type SIMPLE"""
    _TypeDefinition = relayKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'relayType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4708, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is relayKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_relayType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4711, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4711, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'relayType', relayType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}replyCodeCategory with content type SIMPLE
class replyCodeCategory (pyxb.binding.basis.complexTypeDefinition):
    """It is suggested that the values of replyCode be chosen from those values included in IEC 61968-9, 2nd Ed., Annex B as extended by Appendix A of "Security in MultiSpeak-Enabled Applications: Requirements".  Values of replyCode SHOULD be of the form [category] "." [index]."""
    _TypeDefinition = replyCodeCategoryKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'replyCodeCategory')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4719, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is replyCodeCategoryKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_replyCodeCategory_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4725, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4725, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'replyCodeCategory', replyCodeCategory)


# Complex type {http://www.multispeak.org/V5.0/enumerations}requestedAccumulationMode with content type SIMPLE
class requestedAccumulationMode (pyxb.binding.basis.complexTypeDefinition):
    """If this element is populated, the receiver  of the object SHALL return in subsequent DemandResponseEventStatusNotifications the statuses accumulated in the requested mode. Accumulation modes are either "IndividualDevices" in which case the receiver SHALL return the statuses of each device individually, or "AccumulatedStatus" in which case the reciever SHAL return  a summary of the DR event status, accumulated into possible statuses and expressed in percentage for each status. """
    _TypeDefinition = requestedAccumulationModeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'requestedAccumulationMode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4793, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is requestedAccumulationModeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_requestedAccumulationMode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4799, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4799, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'requestedAccumulationMode', requestedAccumulationMode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}requestedNumberType with content type SIMPLE
class requestedNumberType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}requestedNumberType with content type SIMPLE"""
    _TypeDefinition = requestedNumberKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'requestedNumberType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4823, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is requestedNumberKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_requestedNumberType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4826, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4826, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'requestedNumberType', requestedNumberType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}resolvedLevel with content type SIMPLE
class resolvedLevel (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}resolvedLevel with content type SIMPLE"""
    _TypeDefinition = resolvedLevelKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resolvedLevel')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4848, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is resolvedLevelKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_resolvedLevel_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4851, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4851, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'resolvedLevel', resolvedLevel)


# Complex type {http://www.multispeak.org/V5.0/enumerations}resourceState with content type SIMPLE
class resourceState (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}resourceState with content type SIMPLE"""
    _TypeDefinition = resourceStateKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resourceState')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4871, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is resourceStateKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_resourceState_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4874, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4874, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'resourceState', resourceState)


# Complex type {http://www.multispeak.org/V5.0/enumerations}responseCode with content type SIMPLE
class responseCode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}responseCode with content type SIMPLE"""
    _TypeDefinition = responseCodeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'responseCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4916, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is responseCodeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_responseCode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4919, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4919, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'responseCode', responseCode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}resultsType with content type SIMPLE
class resultsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}resultsType with content type SIMPLE"""
    _TypeDefinition = resultsKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resultsType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4945, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is resultsKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_resultsType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4948, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4948, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'resultsType', resultsType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}SCADAFunction with content type SIMPLE
class SCADAFunction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}SCADAFunction with content type SIMPLE"""
    _TypeDefinition = SCADAFunctionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SCADAFunction')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4956, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is SCADAFunctionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_SCADAFunction_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4959, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4959, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'SCADAFunction', SCADAFunction)


# Complex type {http://www.multispeak.org/V5.0/enumerations}SCADAPointType with content type SIMPLE
class SCADAPointType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}SCADAPointType with content type SIMPLE"""
    _TypeDefinition = SCADAPointKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SCADAPointType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4986, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is SCADAPointKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_SCADAPointType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4989, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 4989, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'SCADAPointType', SCADAPointType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}servicePriorityType with content type SIMPLE
class servicePriorityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}servicePriorityType with content type SIMPLE"""
    _TypeDefinition = servicePriorityKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'servicePriorityType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5039, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is servicePriorityKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_servicePriorityType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5042, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5042, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'servicePriorityType', servicePriorityType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}serviceStatus with content type SIMPLE
class serviceStatus (pyxb.binding.basis.complexTypeDefinition):
    """The service status that is associated with a customer service point."""
    _TypeDefinition = serviceStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5050, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is serviceStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_serviceStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5056, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5056, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'serviceStatus', serviceStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}serviceType with content type SIMPLE
class serviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}serviceType with content type SIMPLE"""
    _TypeDefinition = serviceKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5085, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is serviceKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_serviceType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5088, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5088, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'serviceType', serviceType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}spanType with content type SIMPLE
class spanType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}spanType with content type SIMPLE"""
    _TypeDefinition = spanTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'spanType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5106, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is spanTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_spanType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5109, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5109, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'spanType', spanType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}spatialFeatureType with content type SIMPLE
class spatialFeatureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}spatialFeatureType with content type SIMPLE"""
    _TypeDefinition = spatialFeatureKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'spatialFeatureType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5189, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is spatialFeatureKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_spatialFeatureType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5192, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5192, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'spatialFeatureType', spatialFeatureType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}splitAction with content type SIMPLE
class splitAction (pyxb.binding.basis.complexTypeDefinition):
    """This is the action that is to be taken on the original outage as part of an outageSplit."""
    _TypeDefinition = splitActionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'splitAction')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5211, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is splitActionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_splitAction_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5217, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5217, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'splitAction', splitAction)


# Complex type {http://www.multispeak.org/V5.0/enumerations}standardEntryClass with content type SIMPLE
class standardEntryClass (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}standardEntryClass with content type SIMPLE"""
    _TypeDefinition = standardEntryClassKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'standardEntryClass')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5235, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is standardEntryClassKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_standardEntryClass_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5238, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5238, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'standardEntryClass', standardEntryClass)


# Complex type {http://www.multispeak.org/V5.0/enumerations}stationStatus with content type SIMPLE
class stationStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}stationStatus with content type SIMPLE"""
    _TypeDefinition = stationStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stationStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5271, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is stationStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_stationStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5274, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5274, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'stationStatus', stationStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}statusIdentifierType with content type SIMPLE
class statusIdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}statusIdentifierType with content type SIMPLE"""
    _TypeDefinition = statusIdentifierKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'statusIdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5316, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is statusIdentifierKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_statusIdentifierType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5319, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5319, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'statusIdentifierType', statusIdentifierType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}statusOfUnit with content type SIMPLE
class statusOfUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}statusOfUnit with content type SIMPLE"""
    _TypeDefinition = statusOfUnitKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'statusOfUnit')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5327, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is statusOfUnitKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_statusOfUnit_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5330, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5330, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'statusOfUnit', statusOfUnit)


# Complex type {http://www.multispeak.org/V5.0/enumerations}submissionPurpose with content type SIMPLE
class submissionPurpose (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}submissionPurpose with content type SIMPLE"""
    _TypeDefinition = submissionPurposeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'submissionPurpose')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5374, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is submissionPurposeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_submissionPurpose_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5377, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5377, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'submissionPurpose', submissionPurpose)


# Complex type {http://www.multispeak.org/V5.0/enumerations}switchingEndStateType with content type SIMPLE
class switchingEndStateType (pyxb.binding.basis.complexTypeDefinition):
    """The desired end state for the device being operated on during this switching step. """
    _TypeDefinition = switchingEndStateKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'switchingEndStateType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5424, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is switchingEndStateKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_switchingEndStateType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5430, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5430, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'switchingEndStateType', switchingEndStateType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}switchingStepOperationType with content type SIMPLE
class switchingStepOperationType (pyxb.binding.basis.complexTypeDefinition):
    """The operation to be performed during a switching step."""
    _TypeDefinition = switchingStepOperationKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'switchingStepOperationType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5456, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is switchingStepOperationKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_switchingStepOperationType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5462, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5462, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'switchingStepOperationType', switchingStepOperationType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}switchingStepStatusType with content type SIMPLE
class switchingStepStatusType (pyxb.binding.basis.complexTypeDefinition):
    """The status of this switching step.  Possible enumerations include: Proposed, Instructed, Confirmed, Aborted, Skipped, Other. The supported values of stepStatus should be discovered by a call to GetDomainsByDomainName on the application that is the system of record for switching orders."""
    _TypeDefinition = switchingStepStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'switchingStepStatusType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5484, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is switchingStepStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_switchingStepStatusType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5490, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5490, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'switchingStepStatusType', switchingStepStatusType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}switchType with content type SIMPLE
class switchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}switchType with content type SIMPLE"""
    _TypeDefinition = switchTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'switchType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5498, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is switchTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_switchType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5501, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5501, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'switchType', switchType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}tagType with content type SIMPLE
class tagType (pyxb.binding.basis.complexTypeDefinition):
    """The type of clearanceTag placed as part of a clearanceCertificate."""
    _TypeDefinition = tagKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tagType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5571, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is tagKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_tagType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5577, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5577, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'tagType', tagType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}thermostatFanStatus with content type SIMPLE
class thermostatFanStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}thermostatFanStatus with content type SIMPLE"""
    _TypeDefinition = thermostatFanStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermostatFanStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5617, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is thermostatFanStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_thermostatFanStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5620, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5620, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'thermostatFanStatus', thermostatFanStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}thermostatMode with content type SIMPLE
class thermostatMode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}thermostatMode with content type SIMPLE"""
    _TypeDefinition = thermostatModeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'thermostatMode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5647, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is thermostatModeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_thermostatMode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5650, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5650, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'thermostatMode', thermostatMode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}treatment with content type SIMPLE
class treatment (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}treatment with content type SIMPLE"""
    _TypeDefinition = treatmentKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'treatment')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5704, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is treatmentKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_treatment_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5707, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5707, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'treatment', treatment)


# Complex type {http://www.multispeak.org/V5.0/enumerations}unitAction with content type SIMPLE
class unitAction (pyxb.binding.basis.complexTypeDefinition):
    """Action, if any, to be taken at this location (Unknown, Abandon, Construction, Existing, NoAction, Retire, Transfer, Salvage, All, Other).  If the system of record does not support Transfer of units, then it should interpret this action as being the same as "Construction".  If the system of record does not support Salvage then it should interpret salvage as being the same as "Retire"."""
    _TypeDefinition = unitActionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitAction')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5732, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is unitActionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_unitAction_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5738, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5738, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'unitAction', unitAction)


# Complex type {http://www.multispeak.org/V5.0/enumerations}unitPrefixType with content type SIMPLE
class unitPrefixType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}unitPrefixType with content type SIMPLE"""
    _TypeDefinition = unitPrefixKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitPrefixType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5806, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is unitPrefixKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_unitPrefixType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5809, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5809, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'unitPrefixType', unitPrefixType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}unitType with content type SIMPLE
class unitType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}unitType with content type SIMPLE"""
    _TypeDefinition = unitTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unitType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5817, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is unitTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_unitType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5820, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5820, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'unitType', unitType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}uom with content type SIMPLE
class uom (pyxb.binding.basis.complexTypeDefinition):
    """Extensible enumeration for units of measure."""
    _TypeDefinition = uomKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uom')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5858, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is uomKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_uom_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5864, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 5864, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'uom', uom)


# Complex type {http://www.multispeak.org/V5.0/enumerations}variantType with content type SIMPLE
class variantType (pyxb.binding.basis.complexTypeDefinition):
    """A type name that would specify the purpose of the assembly variant used. The enumeration list includes: Unknown, Pole, Wire, Neutral, Misc and Other.  A vendor may use any other value by choosing "Other" from this list and including the optional otherKind attribute, which SHALL be populated with the desired value. Only one variant may be used on a specific materialManagementAssembly."""
    _TypeDefinition = variantTypeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'variantType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6070, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is variantTypeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_variantType_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6076, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6076, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'variantType', variantType)


# Complex type {http://www.multispeak.org/V5.0/enumerations}verifiedElementAction with content type SIMPLE
class verifiedElementAction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}verifiedElementAction with content type SIMPLE"""
    _TypeDefinition = verifiedElementActionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'verifiedElementAction')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6097, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is verifiedElementActionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_verifiedElementAction_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6100, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6100, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'verifiedElementAction', verifiedElementAction)


# Complex type {http://www.multispeak.org/V5.0/enumerations}windingCode with content type SIMPLE
class windingCode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}windingCode with content type SIMPLE"""
    _TypeDefinition = windingCodeKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'windingCode')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6191, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is windingCodeKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_windingCode_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6194, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6194, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'windingCode', windingCode)


# Complex type {http://www.multispeak.org/V5.0/enumerations}windingConnection with content type SIMPLE
class windingConnection (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}windingConnection with content type SIMPLE"""
    _TypeDefinition = windingConnectionKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'windingConnection')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6226, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is windingConnectionKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_windingConnection_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6229, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6229, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'windingConnection', windingConnection)


# Complex type {http://www.multispeak.org/V5.0/enumerations}workRequestStatus with content type SIMPLE
class workRequestStatus (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.multispeak.org/V5.0/enumerations}workRequestStatus with content type SIMPLE"""
    _TypeDefinition = workRequestStatusKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workRequestStatus')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6250, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is workRequestStatusKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_workRequestStatus_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6253, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6253, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'workRequestStatus', workRequestStatus)


# Complex type {http://www.multispeak.org/V5.0/enumerations}workStatusCategory with content type SIMPLE
class workStatusCategory (pyxb.binding.basis.complexTypeDefinition):
    """This type may be used by the system of record to categorize work statuses to allow data requests to be sorted into groups of like work Status.  The system or records own the mapping between workStatusCodes and workStatusCategories."""
    _TypeDefinition = workStatusCategoryKind
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workStatusCategory')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6270, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is workStatusCategoryKind
    
    # Attribute otherKind uses Python identifier otherKind
    __otherKind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'otherKind'), 'otherKind', '__httpwww_multispeak_orgV5_0enumerations_workStatusCategory_otherKind', otherKind)
    __otherKind._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6276, 4)
    __otherKind._UseLocation = pyxb.utils.utility.Location('C:\\Users\\d3m907\\Documents\\projects\\GMLC\\MS-SPEAK\\Specification-v5\\MultiSpeak V507_Endpoints\\xsd\\mspEnumerations.xsd', 6276, 4)
    
    otherKind = property(__otherKind.value, __otherKind.set, None, 'If no acceptable hard enumeration value is available, the choice "Other" SHALL be used and the extended enumeration SHALL be included in this attribute.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __otherKind.name() : __otherKind
    })
Namespace.addCategoryObject('typeBinding', 'workStatusCategory', workStatusCategory)

