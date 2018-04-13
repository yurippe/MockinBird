"""
"""

# Created on 2013.08.30
#
# Author: Giovanni Cannata
#
# Copyright 2013 - 2018 Giovanni Cannata
#
# This file is part of ldap3.
#
# ldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.

from .. import SEQUENCE_TYPES

# Holds info about OIDs.
# Each OID info is a named tuple with the following attributes:
# oid - the OID number
# type - type of OID
# name - description of OID
# doc - reference document of OID
#
# Source of information is IANA ldap-parameters.txt, oid-registry and products documentation as of 2013.08.21


# OID database definition
OID_CONTROL = 'CONTROL'
OID_EXTENSION = 'EXTENSION'
OID_FEATURE = 'FEATURE'
OID_UNSOLICITED_NOTICE = 'UNSOLICITED_NOTICE'
OID_ATTRIBUTE_TYPE = 'ATTRIBUTE_TYPE'
OID_DIT_CONTENT_RULE = 'DIT_CONTENT_RULE'
OID_LDAP_URL_EXTENSION = 'LDAP_URL_EXTENSION'
OID_FAMILY = 'FAMILY'
OID_MATCHING_RULE = 'MATCHING_RULE'
OID_NAME_FORM = 'NAME_FORM'
OID_OBJECT_CLASS = 'OBJECT_CLASS'
OID_ADMINISTRATIVE_ROLE = 'ADMINISTRATIVE_ROLE'
OID_LDAP_SYNTAX = 'LDAP_SYNTAX'

# class kind
CLASS_STRUCTURAL = 'STRUCTURAL'
CLASS_ABSTRACT = 'ABSTRACT'
CLASS_AUXILIARY = 'AUXILIARY'

# attribute kind
ATTRIBUTE_USER_APPLICATION = 'USER_APPLICATION'
ATTRIBUTE_DIRECTORY_OPERATION = 'DIRECTORY_OPERATION'
ATTRIBUTE_DISTRIBUTED_OPERATION = 'DISTRIBUTED_OPERATION'
ATTRIBUTE_DSA_OPERATION = 'DSA_OPERATION'


def constant_to_oid_kind(oid_kind):
    if oid_kind == OID_CONTROL:
        return 'Control'
    elif oid_kind == OID_EXTENSION:
        return 'Extension'
    elif oid_kind == OID_FEATURE:
        return 'Feature'
    elif oid_kind == OID_UNSOLICITED_NOTICE:
        return 'Unsolicited Notice'
    elif oid_kind == OID_ATTRIBUTE_TYPE:
        return 'Attribute Type'
    elif oid_kind == OID_DIT_CONTENT_RULE:
        return 'DIT Content Rule'
    elif oid_kind == OID_LDAP_URL_EXTENSION:
        return 'LDAP URL Extension'
    elif oid_kind == OID_FAMILY:
        return 'Family'
    elif oid_kind == OID_MATCHING_RULE:
        return 'Matching Rule'
    elif oid_kind == OID_NAME_FORM:
        return 'Name Form'
    elif oid_kind == OID_OBJECT_CLASS:
        return 'Object Class'
    elif oid_kind == OID_ADMINISTRATIVE_ROLE:
        return 'Administrative Role'
    elif oid_kind == OID_LDAP_SYNTAX:
        return 'LDAP Syntax'
    else:
        return 'Unknown'


def decode_oids(sequence):
    if sequence:
        return sorted([Oids.get(oid, (oid, None, None, None)) for oid in sequence if oid])
    return list()


def decode_syntax(syntax):
    if not syntax:
        return None
    return Oids.get(syntax, None)


def oid_to_string(oid):
    s = oid[0]
    if oid[2]:
        s += ' - ' + ((', '.join(oid[2])) if isinstance(oid[2], SEQUENCE_TYPES) else oid[2])
    s += (' - ' + constant_to_oid_kind(oid[1])) if oid[1] is not None else ''
    s += (' - ' + oid[3]) if oid[3] else ''

    return s

# tuple structure: (oid, kind, name, docs)
p1 = {
# administrative role
          '2.5.23.1': ('2.5.23.1', OID_ADMINISTRATIVE_ROLE, 'autonomousArea', 'RFC3672'),
          '2.5.23.2': ('2.5.23.2', OID_ADMINISTRATIVE_ROLE, 'accessControlSpecificArea', 'RFC3672'),
          '2.5.23.3': ('2.5.23.3', OID_ADMINISTRATIVE_ROLE, 'accessControlInnerArea', 'RFC3672'),
          '2.5.23.4': ('2.5.23.4', OID_ADMINISTRATIVE_ROLE, 'subschemaAdminSpecificArea', 'RFC3672'),
          '2.5.23.5': ('2.5.23.5', OID_ADMINISTRATIVE_ROLE, 'collectiveAttributeSpecificArea', 'RFC3672'),
          '2.5.23.6': ('2.5.23.6', OID_ADMINISTRATIVE_ROLE, 'collectiveAttributeInnerArea', 'RFC3672'),

          # attributes type
          '0.9.2342.19200300.100.1.1': ('0.9.2342.19200300.100.1.1', OID_ATTRIBUTE_TYPE, ['uid', 'userId'], 'RFC4519'),
          '0.9.2342.19200300.100.1.2': ('0.9.2342.19200300.100.1.2', OID_ATTRIBUTE_TYPE, 'textEncodedORAddress', 'RFC1274'),
          '0.9.2342.19200300.100.1.3': ('0.9.2342.19200300.100.1.3', OID_ATTRIBUTE_TYPE, ['mail', 'RFC822Mailbox'], 'RFC4524'),
          '0.9.2342.19200300.100.1.4': ('0.9.2342.19200300.100.1.4', OID_ATTRIBUTE_TYPE, 'info', 'RFC4524'),
          '0.9.2342.19200300.100.1.5': ('0.9.2342.19200300.100.1.5', OID_ATTRIBUTE_TYPE, ['drink', 'favouriteDrink'], 'RFC4524'),
          '0.9.2342.19200300.100.1.6': ('0.9.2342.19200300.100.1.6', OID_ATTRIBUTE_TYPE, 'roomNumber', 'RFC4524'),
          '0.9.2342.19200300.100.1.7': ('0.9.2342.19200300.100.1.7', OID_ATTRIBUTE_TYPE, 'photo', 'RFC1274'),
          '0.9.2342.19200300.100.1.8': ('0.9.2342.19200300.100.1.8', OID_ATTRIBUTE_TYPE, 'userClass', 'RFC4524'),
          '0.9.2342.19200300.100.1.9': ('0.9.2342.19200300.100.1.9', OID_ATTRIBUTE_TYPE, 'host', 'RFC4524'),
          '0.9.2342.19200300.100.1.10': ('0.9.2342.19200300.100.1.10', OID_ATTRIBUTE_TYPE, 'manager', 'RFC4524'),
          '0.9.2342.19200300.100.1.11': ('0.9.2342.19200300.100.1.11', OID_ATTRIBUTE_TYPE, 'documentIdentifier', 'RFC4524'),
          '0.9.2342.19200300.100.1.12': ('0.9.2342.19200300.100.1.12', OID_ATTRIBUTE_TYPE, 'documentTitle', 'RFC4524'),
          '0.9.2342.19200300.100.1.13': ('0.9.2342.19200300.100.1.13', OID_ATTRIBUTE_TYPE, 'documentVersion', 'RFC4524'),
          '0.9.2342.19200300.100.1.14': ('0.9.2342.19200300.100.1.14', OID_ATTRIBUTE_TYPE, 'documentAuthor', 'RFC4524'),
          '0.9.2342.19200300.100.1.15': ('0.9.2342.19200300.100.1.15', OID_ATTRIBUTE_TYPE, 'documentLocation', 'RFC4524'),
          '0.9.2342.19200300.100.1.20': ('0.9.2342.19200300.100.1.20', OID_ATTRIBUTE_TYPE, ['homePhone', 'homeTelephone'], 'RFC4524'),
          '0.9.2342.19200300.100.1.21': ('0.9.2342.19200300.100.1.21', OID_ATTRIBUTE_TYPE, 'secretary', 'RFC4524'),
          '0.9.2342.19200300.100.1.22': ('0.9.2342.19200300.100.1.22', OID_ATTRIBUTE_TYPE, 'otherMailbox', 'RFC1274'),
          '0.9.2342.19200300.100.1.23': ('0.9.2342.19200300.100.1.23', OID_ATTRIBUTE_TYPE, 'lastModifiedTime', 'RFC1274'),
          '0.9.2342.19200300.100.1.24': ('0.9.2342.19200300.100.1.24', OID_ATTRIBUTE_TYPE, 'lastModifiedBy', 'RFC1274'),
          '0.9.2342.19200300.100.1.25': ('0.9.2342.19200300.100.1.25', OID_ATTRIBUTE_TYPE, ['DC', 'domainComponent'], 'RFC4519'),
          '0.9.2342.19200300.100.1.26': ('0.9.2342.19200300.100.1.26', OID_ATTRIBUTE_TYPE, 'aRecord', 'RFC1274'),
          '0.9.2342.19200300.100.1.27': ('0.9.2342.19200300.100.1.27', OID_ATTRIBUTE_TYPE, 'mDRecord', 'RFC1274'),
          '0.9.2342.19200300.100.1.28': ('0.9.2342.19200300.100.1.28', OID_ATTRIBUTE_TYPE, 'mXRecord', 'RFC1274'),
          '0.9.2342.19200300.100.1.29': ('0.9.2342.19200300.100.1.29', OID_ATTRIBUTE_TYPE, 'nSRecord', 'RFC1274'),
          '0.9.2342.19200300.100.1.30': ('0.9.2342.19200300.100.1.30', OID_ATTRIBUTE_TYPE, 'sOARecord', 'RFC1274'),
          '0.9.2342.19200300.100.1.31': ('0.9.2342.19200300.100.1.31', OID_ATTRIBUTE_TYPE, 'cNAMERecord', 'RFC1274'),
          '0.9.2342.19200300.100.1.37': ('0.9.2342.19200300.100.1.37', OID_ATTRIBUTE_TYPE, 'associatedDomain', 'RFC4524'),
          '0.9.2342.19200300.100.1.38': ('0.9.2342.19200300.100.1.38', OID_ATTRIBUTE_TYPE, 'associatedName', 'RFC4524'),
          '0.9.2342.19200300.100.1.39': ('0.9.2342.19200300.100.1.39', OID_ATTRIBUTE_TYPE, 'homePostalAddress', 'RFC4524'),
          '0.9.2342.19200300.100.1.40': ('0.9.2342.19200300.100.1.40', OID_ATTRIBUTE_TYPE, 'personalTitle', 'RFC4524'),
          '0.9.2342.19200300.100.1.41': ('0.9.2342.19200300.100.1.41', OID_ATTRIBUTE_TYPE, ['mobile', 'mobileTelephoneNumber'], 'RFC4524'),
          '0.9.2342.19200300.100.1.42': ('0.9.2342.19200300.100.1.42', OID_ATTRIBUTE_TYPE, ['pager', 'pagerTelephoneNumber'], 'RFC4524'),
          '0.9.2342.19200300.100.1.43': ('0.9.2342.19200300.100.1.43', OID_ATTRIBUTE_TYPE, ['co', 'friendlyCountryName'], 'RFC4524'),
          '0.9.2342.19200300.100.1.44': ('0.9.2342.19200300.100.1.44', OID_ATTRIBUTE_TYPE, 'uniqueIdentifier', 'RFC4524'),
          '0.9.2342.19200300.100.1.45': ('0.9.2342.19200300.100.1.45', OID_ATTRIBUTE_TYPE, 'organizationalStatus', 'RFC4524'),
          '0.9.2342.19200300.100.1.46': ('0.9.2342.19200300.100.1.46', OID_ATTRIBUTE_TYPE, 'janetMailbox', 'RFC1274'),
          '0.9.2342.19200300.100.1.47': ('0.9.2342.19200300.100.1.47', OID_ATTRIBUTE_TYPE, 'mailPreferenceOption', 'RFC1274'),
          '0.9.2342.19200300.100.1.48': ('0.9.2342.19200300.100.1.48', OID_ATTRIBUTE_TYPE, 'buildingName', 'RFC4524'),
          '0.9.2342.19200300.100.1.49': ('0.9.2342.19200300.100.1.49', OID_ATTRIBUTE_TYPE, 'dSAQuality', 'RFC1274'),
          '0.9.2342.19200300.100.1.50': ('0.9.2342.19200300.100.1.50', OID_ATTRIBUTE_TYPE, 'singleLevelQuality', 'RFC4524'),
          '0.9.2342.19200300.100.1.51': ('0.9.2342.19200300.100.1.51', OID_ATTRIBUTE_TYPE, 'subtreeMinimumQuality', 'RFC1274'),
          '0.9.2342.19200300.100.1.52': ('0.9.2342.19200300.100.1.52', OID_ATTRIBUTE_TYPE, 'subtreeMaximumQuality', 'RFC1274'),
          '0.9.2342.19200300.100.1.53': ('0.9.2342.19200300.100.1.53', OID_ATTRIBUTE_TYPE, 'personalSignature', 'RFC1274'),
          '0.9.2342.19200300.100.1.54': ('0.9.2342.19200300.100.1.54', OID_ATTRIBUTE_TYPE, 'dITRedirect', 'RFC1274'),
          '0.9.2342.19200300.100.1.55': ('0.9.2342.19200300.100.1.55', OID_ATTRIBUTE_TYPE, 'audio', 'RFC1274'),
          '0.9.2342.19200300.100.1.56': ('0.9.2342.19200300.100.1.56', OID_ATTRIBUTE_TYPE, 'documentPublisher', 'RFC4524'),
          '0.9.2342.19200300.100.1.60': ('0.9.2342.19200300.100.1.60', OID_ATTRIBUTE_TYPE, 'jpegPhoto', 'RFC2798'),
          '1.2.840.113549.1.9.1': ('1.2.840.113549.1.9.1', OID_ATTRIBUTE_TYPE, ['email', 'emailAddress'], 'RFC3280'),
          '1.2.840.113556.1.4.478': ('1.2.840.113556.1.4.478', OID_ATTRIBUTE_TYPE, 'calCalURI', 'RFC2739'),
          '1.2.840.113556.1.4.479': ('1.2.840.113556.1.4.479', OID_ATTRIBUTE_TYPE, 'calFBURL', 'RFC2739'),
          '1.2.840.113556.1.4.480': ('1.2.840.113556.1.4.480', OID_ATTRIBUTE_TYPE, 'calCAPURI', 'RFC2739'),
          '1.2.840.113556.1.4.481': ('1.2.840.113556.1.4.481', OID_ATTRIBUTE_TYPE, 'calCalAdrURI', 'RFC2739'),
          '1.2.840.113556.1.4.482': ('1.2.840.113556.1.4.482', OID_ATTRIBUTE_TYPE, 'calOtherCalURIs', 'RFC2739'),
          '1.2.840.113556.1.4.483': ('1.2.840.113556.1.4.483', OID_ATTRIBUTE_TYPE, 'calOtherFBURLs', 'RFC2739'),
          '1.2.840.113556.1.4.484': ('1.2.840.113556.1.4.484', OID_ATTRIBUTE_TYPE, 'calOtherCAPURIs', 'RFC2739'),
          '1.2.840.113556.1.4.485': ('1.2.840.113556.1.4.485', OID_ATTRIBUTE_TYPE, 'calOtherCalAdrURIs', 'RFC2739'),
          '1.3.18.0.2.4.1107': ('1.3.18.0.2.4.1107', OID_ATTRIBUTE_TYPE, 'printer-xri-supported', 'RFC3712'),
          '1.3.18.0.2.4.1108': ('1.3.18.0.2.4.1108', OID_ATTRIBUTE_TYPE, 'printer-aliases', 'RFC3712'),
          '1.3.18.0.2.4.1109': ('1.3.18.0.2.4.1109', OID_ATTRIBUTE_TYPE, 'printer-charset-configured', 'RFC3712'),
          '1.3.18.0.2.4.1110': ('1.3.18.0.2.4.1110', OID_ATTRIBUTE_TYPE, 'printer-job-priority-supported', 'RFC3712'),
          '1.3.18.0.2.4.1111': ('1.3.18.0.2.4.1111', OID_ATTRIBUTE_TYPE, 'printer-job-k-octets-supported', 'RFC3712'),
          '1.3.18.0.2.4.1112': ('1.3.18.0.2.4.1112', OID_ATTRIBUTE_TYPE, 'printer-current-operator', 'RFC3712'),
          '1.3.18.0.2.4.1113': ('1.3.18.0.2.4.1113', OID_ATTRIBUTE_TYPE, 'printer-service-person', 'RFC3712'),
          '1.3.18.0.2.4.1114': ('1.3.18.0.2.4.1114', OID_ATTRIBUTE_TYPE, 'printer-delivery-orientation-supported', 'RFC3712'),
          '1.3.18.0.2.4.1115': ('1.3.18.0.2.4.1115', OID_ATTRIBUTE_TYPE, 'printer-stacking-order-supported', 'RFC3712'),
          '1.3.18.0.2.4.1116': ('1.3.18.0.2.4.1116', OID_ATTRIBUTE_TYPE, 'printer-output-features-supported', 'RFC3712'),
          '1.3.18.0.2.4.1117': ('1.3.18.0.2.4.1117', OID_ATTRIBUTE_TYPE, 'printer-media-local-supported', 'RFC3712'),
          '1.3.18.0.2.4.1118': ('1.3.18.0.2.4.1118', OID_ATTRIBUTE_TYPE, 'printer-copies-supported', 'RFC3712'),
          '1.3.18.0.2.4.1119': ('1.3.18.0.2.4.1119', OID_ATTRIBUTE_TYPE, 'printer-natural-language-configured', 'RFC3712'),
          '1.3.18.0.2.4.1120': ('1.3.18.0.2.4.1120', OID_ATTRIBUTE_TYPE, 'printer-print-quality-supported', 'RFC3712'),
          '1.3.18.0.2.4.1121': ('1.3.18.0.2.4.1121', OID_ATTRIBUTE_TYPE, 'printer-resolution-supported', 'RFC3712'),
          '1.3.18.0.2.4.1122': ('1.3.18.0.2.4.1122', OID_ATTRIBUTE_TYPE, 'printer-media-supported', 'RFC3712'),
          '1.3.18.0.2.4.1123': ('1.3.18.0.2.4.1123', OID_ATTRIBUTE_TYPE, 'printer-sides-supported', 'RFC3712'),
          '1.3.18.0.2.4.1124': ('1.3.18.0.2.4.1124', OID_ATTRIBUTE_TYPE, 'printer-number-up-supported', 'RFC3712'),
          '1.3.18.0.2.4.1125': ('1.3.18.0.2.4.1125', OID_ATTRIBUTE_TYPE, 'printer-finishings-supported', 'RFC3712'),
          '1.3.18.0.2.4.1126': ('1.3.18.0.2.4.1126', OID_ATTRIBUTE_TYPE, 'printer-pages-per-minute-color', 'RFC3712'),
          '1.3.18.0.2.4.1127': ('1.3.18.0.2.4.1127', OID_ATTRIBUTE_TYPE, 'printer-pages-per-minute', 'RFC3712'),
          '1.3.18.0.2.4.1128': ('1.3.18.0.2.4.1128', OID_ATTRIBUTE_TYPE, 'printer-compression-supported', 'RFC3712'),
          '1.3.18.0.2.4.1129': ('1.3.18.0.2.4.1129', OID_ATTRIBUTE_TYPE, 'printer-color-supported', 'RFC3712'),
          '1.3.18.0.2.4.1130': ('1.3.18.0.2.4.1130', OID_ATTRIBUTE_TYPE, 'printer-document-format-supported', 'RFC3712'),
          '1.3.18.0.2.4.1131': ('1.3.18.0.2.4.1131', OID_ATTRIBUTE_TYPE, 'printer-charset-supported', 'RFC3712'),
          '1.3.18.0.2.4.1132': ('1.3.18.0.2.4.1132', OID_ATTRIBUTE_TYPE, 'printer-multiple-document-jobs-supported', 'RFC3712'),
          '1.3.18.0.2.4.1133': ('1.3.18.0.2.4.1133', OID_ATTRIBUTE_TYPE, 'printer-ipp-versions-supported', 'RFC3712'),
          '1.3.18.0.2.4.1134': ('1.3.18.0.2.4.1134', OID_ATTRIBUTE_TYPE, 'printer-more-info', 'RFC3712'),
          '1.3.18.0.2.4.1135': ('1.3.18.0.2.4.1135', OID_ATTRIBUTE_TYPE, 'printer-name', 'RFC3712'),
          '1.3.18.0.2.4.1136': ('1.3.18.0.2.4.1136', OID_ATTRIBUTE_TYPE, 'printer-location', 'RFC3712'),
          '1.3.18.0.2.4.1137': ('1.3.18.0.2.4.1137', OID_ATTRIBUTE_TYPE, 'printer-generated-natural-language-supported', 'RFC3712'),
          '1.3.18.0.2.4.1138': ('1.3.18.0.2.4.1138', OID_ATTRIBUTE_TYPE, 'printer-make-and-model', 'RFC3712'),
          '1.3.18.0.2.4.1139': ('1.3.18.0.2.4.1139', OID_ATTRIBUTE_TYPE, 'printer-info', 'RFC3712'),
          '1.3.18.0.2.4.1140': ('1.3.18.0.2.4.1140', OID_ATTRIBUTE_TYPE, 'printer-uri', 'RFC3712'),
          '1.3.6.1.1.10.4.1': ('1.3.6.1.1.10.4.1', OID_ATTRIBUTE_TYPE, 'uddiBusinessKey', 'RFC4403'),
          '1.3.6.1.1.10.4.2': ('1.3.6.1.1.10.4.2', OID_ATTRIBUTE_TYPE, 'uddiAuthorizedName', 'RFC4403'),
          '1.3.6.1.1.10.4.3': ('1.3.6.1.1.10.4.3', OID_ATTRIBUTE_TYPE, 'uddiOperator', 'RFC4403'),
          '1.3.6.1.1.10.4.4': ('1.3.6.1.1.10.4.4', OID_ATTRIBUTE_TYPE, 'uddiName', 'RFC4403'),
          '1.3.6.1.1.10.4.5': ('1.3.6.1.1.10.4.5', OID_ATTRIBUTE_TYPE, 'uddiDescription', 'RFC4403'),
          '1.3.6.1.1.10.4.6': ('1.3.6.1.1.10.4.6', OID_ATTRIBUTE_TYPE, 'uddiDiscoveryURLs', 'RFC4403'),
          '1.3.6.1.1.10.4.7': ('1.3.6.1.1.10.4.7', OID_ATTRIBUTE_TYPE, 'uddiUseType', 'RFC4403'),
          '1.3.6.1.1.10.4.8': ('1.3.6.1.1.10.4.8', OID_ATTRIBUTE_TYPE, 'uddiPersonName', 'RFC4403'),
          '1.3.6.1.1.10.4.9': ('1.3.6.1.1.10.4.9', OID_ATTRIBUTE_TYPE, 'uddiPhone', 'RFC4403'),
          '1.3.6.1.1.10.4.10': ('1.3.6.1.1.10.4.10', OID_ATTRIBUTE_TYPE, 'uddiEMail', 'RFC4403'),
          '1.3.6.1.1.10.4.11': ('1.3.6.1.1.10.4.11', OID_ATTRIBUTE_TYPE, 'uddiSortCode', 'RFC4403'),
          '1.3.6.1.1.10.4.12': ('1.3.6.1.1.10.4.12', OID_ATTRIBUTE_TYPE, 'uddiTModelKey', 'RFC4403'),
          '1.3.6.1.1.10.4.13': ('1.3.6.1.1.10.4.13', OID_ATTRIBUTE_TYPE, 'uddiAddressLine', 'RFC4403'),
          '1.3.6.1.1.10.4.14': ('1.3.6.1.1.10.4.14', OID_ATTRIBUTE_TYPE, 'uddiIdentifierBag', 'RFC4403'),
          '1.3.6.1.1.10.4.15': ('1.3.6.1.1.10.4.15', OID_ATTRIBUTE_TYPE, 'uddiCategoryBag', 'RFC4403'),
          '1.3.6.1.1.10.4.16': ('1.3.6.1.1.10.4.16', OID_ATTRIBUTE_TYPE, 'uddiKeyedReference', 'RFC4403'),
          '1.3.6.1.1.10.4.17': ('1.3.6.1.1.10.4.17', OID_ATTRIBUTE_TYPE, 'uddiServiceKey', 'RFC4403'),
          '1.3.6.1.1.10.4.18': ('1.3.6.1.1.10.4.18', OID_ATTRIBUTE_TYPE, 'uddiBindingKey', 'RFC4403'),
          '1.3.6.1.1.10.4.19': ('1.3.6.1.1.10.4.19', OID_ATTRIBUTE_TYPE, 'uddiAccessPoint', 'RFC4403'),
          '1.3.6.1.1.10.4.20': ('1.3.6.1.1.10.4.20', OID_ATTRIBUTE_TYPE, 'uddiHostingRedirector', 'RFC4403'),
          '1.3.6.1.1.10.4.21': ('1.3.6.1.1.10.4.21', OID_ATTRIBUTE_TYPE, 'uddiInstanceDescription', 'RFC4403'),
          '1.3.6.1.1.10.4.22': ('1.3.6.1.1.10.4.22', OID_ATTRIBUTE_TYPE, 'uddiInstanceParms', 'RFC4403'),
          '1.3.6.1.1.10.4.23': ('1.3.6.1.1.10.4.23', OID_ATTRIBUTE_TYPE, 'uddiOverviewDescription', 'RFC4403'),
          '1.3.6.1.1.10.4.24': ('1.3.6.1.1.10.4.24', OID_ATTRIBUTE_TYPE, 'uddiOverviewURL', 'RFC4403'),
          '1.3.6.1.1.10.4.25': ('1.3.6.1.1.10.4.25', OID_ATTRIBUTE_TYPE, 'uddiFromKey', 'RFC4403'),
          '1.3.6.1.1.10.4.26': ('1.3.6.1.1.10.4.26', OID_ATTRIBUTE_TYPE, 'uddiToKey', 'RFC4403'),
          '1.3.6.1.1.10.4.27': ('1.3.6.1.1.10.4.27', OID_ATTRIBUTE_TYPE, 'uddiUUID', 'RFC4403'),
          '1.3.6.1.1.10.4.28': ('1.3.6.1.1.10.4.28', OID_ATTRIBUTE_TYPE, 'uddiIsHidden', 'RFC4403'),
          '1.3.6.1.1.10.4.29': ('1.3.6.1.1.10.4.29', OID_ATTRIBUTE_TYPE, 'uddiIsProjection', 'RFC4403'),
          '1.3.6.1.1.10.4.30': ('1.3.6.1.1.10.4.30', OID_ATTRIBUTE_TYPE, 'uddiLang', 'RFC4403'),
          '1.3.6.1.1.10.4.31': ('1.3.6.1.1.10.4.31', OID_ATTRIBUTE_TYPE, 'uddiv3BusinessKey', 'RFC4403'),
          '1.3.6.1.1.10.4.32': ('1.3.6.1.1.10.4.32', OID_ATTRIBUTE_TYPE, 'uddiv3ServiceKey', 'RFC4403'),
          '1.3.6.1.1.10.4.33': ('1.3.6.1.1.10.4.33', OID_ATTRIBUTE_TYPE, 'uddiv3BindingKey', 'RFC4403'),
          '1.3.6.1.1.10.4.34': ('1.3.6.1.1.10.4.34', OID_ATTRIBUTE_TYPE, 'uddiv3TmodelKey', 'RFC4403'),
          '1.3.6.1.1.10.4.35': ('1.3.6.1.1.10.4.35', OID_ATTRIBUTE_TYPE, 'uddiv3DigitalSignature', 'RFC4403'),
          '1.3.6.1.1.10.4.36': ('1.3.6.1.1.10.4.36', OID_ATTRIBUTE_TYPE, 'uddiv3NodeId', 'RFC4403'),
          '1.3.6.1.1.10.4.37': ('1.3.6.1.1.10.4.37', OID_ATTRIBUTE_TYPE, 'uddiv3EntityModificationTime', 'RFC4403'),
          '1.3.6.1.1.10.4.38': ('1.3.6.1.1.10.4.38', OID_ATTRIBUTE_TYPE, 'uddiv3SubscriptionKey', 'RFC4403'),
          '1.3.6.1.1.10.4.39': ('1.3.6.1.1.10.4.39', OID_ATTRIBUTE_TYPE, 'uddiv3SubscriptionFilter', 'RFC4403'),
          '1.3.6.1.1.10.4.40': ('1.3.6.1.1.10.4.40', OID_ATTRIBUTE_TYPE, 'uddiv3NotificationInterval', 'RFC4403'),
          '1.3.6.1.1.10.4.41': ('1.3.6.1.1.10.4.41', OID_ATTRIBUTE_TYPE, 'uddiv3MaxEntities', 'RFC4403'),
          '1.3.6.1.1.10.4.42': ('1.3.6.1.1.10.4.42', OID_ATTRIBUTE_TYPE, 'uddiv3ExpiresAfter', 'RFC4403'),
          '1.3.6.1.1.10.4.43': ('1.3.6.1.1.10.4.43', OID_ATTRIBUTE_TYPE, 'uddiv3BriefResponse', 'RFC4403'),
          '1.3.6.1.1.10.4.44': ('1.3.6.1.1.10.4.44', OID_ATTRIBUTE_TYPE, 'uddiv3EntityKey', 'RFC4403'),
          '1.3.6.1.1.10.4.45': ('1.3.6.1.1.10.4.45', OID_ATTRIBUTE_TYPE, 'uddiv3EntityCreationTime', 'RFC4403'),
          '1.3.6.1.1.10.4.46': ('1.3.6.1.1.10.4.46', OID_ATTRIBUTE_TYPE, 'uddiv3EntityDeletionTime', 'RFC4403'),
          '1.3.6.1.1.11.2.1': ('1.3.6.1.1.11.2.1', OID_ATTRIBUTE_TYPE, 'vPIMTelephoneNumber', 'RFC4237'),
          '1.3.6.1.1.11.2.2': ('1.3.6.1.1.11.2.2', OID_ATTRIBUTE_TYPE, 'vPIMRfc822Mailbox', 'RFC4237'),
          '1.3.6.1.1.11.2.3': ('1.3.6.1.1.11.2.3', OID_ATTRIBUTE_TYPE, 'vPIMSpokenName', 'RFC4237'),
          '1.3.6.1.1.11.2.4': ('1.3.6.1.1.11.2.4', OID_ATTRIBUTE_TYPE, 'vPIMSupportedUABehaviors', 'RFC4237'),
          '1.3.6.1.1.11.2.5': ('1.3.6.1.1.11.2.5', OID_ATTRIBUTE_TYPE, 'vPIMSupportedAudioMediaTypes', 'RFC4237'),
          '1.3.6.1.1.11.2.6': ('1.3.6.1.1.11.2.6', OID_ATTRIBUTE_TYPE, 'vPIMSupportedMessageContext', 'RFC4237'),
          '1.3.6.1.1.11.2.7': ('1.3.6.1.1.11.2.7', OID_ATTRIBUTE_TYPE, 'vPIMTextName', 'RFC4237'),
          '1.3.6.1.1.11.2.8': ('1.3.6.1.1.11.2.8', OID_ATTRIBUTE_TYPE, 'vPIMExtendedAbsenceStatus', 'RFC4237'),
          '1.3.6.1.1.11.2.9': ('1.3.6.1.1.11.2.9', OID_ATTRIBUTE_TYPE, 'vPIMMaxMessageSize', 'RFC4237'),
          '1.3.6.1.1.11.2.10': ('1.3.6.1.1.11.2.10', OID_ATTRIBUTE_TYPE, 'vPIMSubMailboxes', 'RFC4237'),
          '1.3.6.1.1.16.4': ('1.3.6.1.1.16.4', OID_ATTRIBUTE_TYPE, 'entryUUID', 'RFC4530'),
          '1.3.6.1.1.20': ('1.3.6.1.1.20', OID_ATTRIBUTE_TYPE, 'entryDN', 'RFC5020'),
          '1.3.6.1.1.6.2.3': ('1.3.6.1.1.6.2.3', OID_ATTRIBUTE_TYPE, 'pcimKeywords', 'RFC3703'),
          '1.3.6.1.1.6.2.4': ('1.3.6.1.1.6.2.4', OID_ATTRIBUTE_TYPE, 'pcimGroupName', 'RFC3703'),
          '1.3.6.1.1.6.2.5': ('1.3.6.1.1.6.2.5', OID_ATTRIBUTE_TYPE, 'pcimRuleName', 'RFC3703'),
          '1.3.6.1.1.6.2.6': ('1.3.6.1.1.6.2.6', OID_ATTRIBUTE_TYPE, 'pcimRuleEnabled', 'RFC3703'),
          '1.3.6.1.1.6.2.7': ('1.3.6.1.1.6.2.7', OID_ATTRIBUTE_TYPE, 'pcimRuleConditionListType', 'RFC3703'),
          '1.3.6.1.1.6.2.8': ('1.3.6.1.1.6.2.8', OID_ATTRIBUTE_TYPE, 'pcimRuleConditionList', 'RFC3703'),
          '1.3.6.1.1.6.2.9': ('1.3.6.1.1.6.2.9', OID_ATTRIBUTE_TYPE, 'pcimRuleActionList', 'RFC3703'),
          '1.3.6.1.1.6.2.10': ('1.3.6.1.1.6.2.10', OID_ATTRIBUTE_TYPE, 'pcimRuleValidityPeriodList', 'RFC3703'),
          '1.3.6.1.1.6.2.11': ('1.3.6.1.1.6.2.11', OID_ATTRIBUTE_TYPE, 'pcimRuleUsage', 'RFC3703'),
          '1.3.6.1.1.6.2.12': ('1.3.6.1.1.6.2.12', OID_ATTRIBUTE_TYPE, 'pcimRulePriority', 'RFC3703'),
          '1.3.6.1.1.6.2.13': ('1.3.6.1.1.6.2.13', OID_ATTRIBUTE_TYPE, 'pcimRuleMandatory', 'RFC3703'),
          '1.3.6.1.1.6.2.14': ('1.3.6.1.1.6.2.14', OID_ATTRIBUTE_TYPE, 'pcimRuleSequencedActions', 'RFC3703'),
          '1.3.6.1.1.6.2.15': ('1.3.6.1.1.6.2.15', OID_ATTRIBUTE_TYPE, 'pcimRoles', 'RFC3703'),
          '1.3.6.1.1.6.2.16': ('1.3.6.1.1.6.2.16', OID_ATTRIBUTE_TYPE, 'pcimConditionGroupNumber', 'RFC3703'),
          '1.3.6.1.1.6.2.17': ('1.3.6.1.1.6.2.17', OID_ATTRIBUTE_TYPE, 'pcimConditionNegated', 'RFC3703'),
          '1.3.6.1.1.6.2.18': ('1.3.6.1.1.6.2.18', OID_ATTRIBUTE_TYPE, 'pcimConditionName', 'RFC3703'),
          '1.3.6.1.1.6.2.19': ('1.3.6.1.1.6.2.19', OID_ATTRIBUTE_TYPE, 'pcimConditionDN', 'RFC3703'),
          '1.3.6.1.1.6.2.20': ('1.3.6.1.1.6.2.20', OID_ATTRIBUTE_TYPE, 'pcimValidityConditionName', 'RFC3703'),
          '1.3.6.1.1.6.2.21': ('1.3.6.1.1.6.2.21', OID_ATTRIBUTE_TYPE, 'pcimTimePeriodConditionDN', 'RFC3703'),
          '1.3.6.1.1.6.2.22': ('1.3.6.1.1.6.2.22', OID_ATTRIBUTE_TYPE, 'pcimActionName', 'RFC3703'),
          '1.3.6.1.1.6.2.23': ('1.3.6.1.1.6.2.23', OID_ATTRIBUTE_TYPE, 'pcimActionOrder', 'RFC3703'),
          '1.3.6.1.1.6.2.24': ('1.3.6.1.1.6.2.24', OID_ATTRIBUTE_TYPE, 'pcimActionDN', 'RFC3703'),
          '1.3.6.1.1.6.2.25': ('1.3.6.1.1.6.2.25', OID_ATTRIBUTE_TYPE, 'pcimTPCTime', 'RFC3703'),
          '1.3.6.1.1.6.2.26': ('1.3.6.1.1.6.2.26', OID_ATTRIBUTE_TYPE, 'pcimTPCMonthOfYearMask', 'RFC3703'),
          '1.3.6.1.1.6.2.27': ('1.3.6.1.1.6.2.27', OID_ATTRIBUTE_TYPE, 'pcimTPCDayOfMonthMask', 'RFC3703'),
          '1.3.6.1.1.6.2.28': ('1.3.6.1.1.6.2.28', OID_ATTRIBUTE_TYPE, 'pcimTPCDayOfWeekMask', 'RFC3703'),
          '1.3.6.1.1.6.2.29': ('1.3.6.1.1.6.2.29', OID_ATTRIBUTE_TYPE, 'pcimTPCTimeOfDayMask', 'RFC3703'),
          '1.3.6.1.1.6.2.30': ('1.3.6.1.1.6.2.30', OID_ATTRIBUTE_TYPE, 'pcimTPCLocalOrUtcTime', 'RFC3703'),
          '1.3.6.1.1.6.2.31': ('1.3.6.1.1.6.2.31', OID_ATTRIBUTE_TYPE, 'pcimVendorConstraintData', 'RFC3703'),
          '1.3.6.1.1.6.2.32': ('1.3.6.1.1.6.2.32', OID_ATTRIBUTE_TYPE, 'pcimVendorConstraintEncoding', 'RFC3703'),
          '1.3.6.1.1.6.2.33': ('1.3.6.1.1.6.2.33', OID_ATTRIBUTE_TYPE, 'pcimVendorActionData', 'RFC3703'),
          '1.3.6.1.1.6.2.34': ('1.3.6.1.1.6.2.34', OID_ATTRIBUTE_TYPE, 'pcimVendorActionEncoding', 'RFC3703'),
          '1.3.6.1.1.6.2.35': ('1.3.6.1.1.6.2.35', OID_ATTRIBUTE_TYPE, 'pcimPolicyInstanceName', 'RFC3703'),
          '1.3.6.1.1.6.2.36': ('1.3.6.1.1.6.2.36', OID_ATTRIBUTE_TYPE, 'pcimRepositoryName', 'RFC3703'),
          '1.3.6.1.1.6.2.37': ('1.3.6.1.1.6.2.37', OID_ATTRIBUTE_TYPE, 'pcimSubtreesAuxContainedSet', 'RFC3703'),
          '1.3.6.1.1.6.2.38': ('1.3.6.1.1.6.2.38', OID_ATTRIBUTE_TYPE, 'pcimGroupsAuxContainedSet', 'RFC3703'),
          '1.3.6.1.1.6.2.39': ('1.3.6.1.1.6.2.39', OID_ATTRIBUTE_TYPE, 'pcimRulesAuxContainedSet', 'RFC3703'),
          '1.3.6.1.1.9.2.1': ('1.3.6.1.1.9.2.1', OID_ATTRIBUTE_TYPE, 'pcelsPolicySetName', 'RFC4104'),
          '1.3.6.1.1.9.2.2': ('1.3.6.1.1.9.2.2', OID_ATTRIBUTE_TYPE, 'pcelsDecisionStrategy', 'RFC4104'),
          '1.3.6.1.1.9.2.3': ('1.3.6.1.1.9.2.3', OID_ATTRIBUTE_TYPE, 'pcelsPolicySetList', 'RFC4104'),
          '1.3.6.1.1.9.2.4': ('1.3.6.1.1.9.2.4', OID_ATTRIBUTE_TYPE, 'pcelsPriority', 'RFC4104'),
          '1.3.6.1.1.9.2.5': ('1.3.6.1.1.9.2.5', OID_ATTRIBUTE_TYPE, 'pcelsPolicySetDN', 'RFC4104'),
          '1.3.6.1.1.9.2.6': ('1.3.6.1.1.9.2.6', OID_ATTRIBUTE_TYPE, 'pcelsConditionListType', 'RFC4104'),
          '1.3.6.1.1.9.2.7': ('1.3.6.1.1.9.2.7', OID_ATTRIBUTE_TYPE, 'pcelsConditionList', 'RFC4104'),
          '1.3.6.1.1.9.2.8': ('1.3.6.1.1.9.2.8', OID_ATTRIBUTE_TYPE, 'pcelsActionList', 'RFC4104'),
          '1.3.6.1.1.9.2.9': ('1.3.6.1.1.9.2.9', OID_ATTRIBUTE_TYPE, 'pcelsSequencedActions', 'RFC4104'),
          '1.3.6.1.1.9.2.10': ('1.3.6.1.1.9.2.10', OID_ATTRIBUTE_TYPE, 'pcelsExecutionStrategy', 'RFC4104'),
          '1.3.6.1.1.9.2.11': ('1.3.6.1.1.9.2.11', OID_ATTRIBUTE_TYPE, 'pcelsVariableDN', 'RFC4104'),
          '1.3.6.1.1.9.2.12': ('1.3.6.1.1.9.2.12', OID_ATTRIBUTE_TYPE, 'pcelsValueDN', 'RFC4104'),
          '1.3.6.1.1.9.2.13': ('1.3.6.1.1.9.2.13', OID_ATTRIBUTE_TYPE, 'pcelsIsMirrored', 'RFC4104'),
          '1.3.6.1.1.9.2.14': ('1.3.6.1.1.9.2.14', OID_ATTRIBUTE_TYPE, 'pcelsVariableName', 'RFC4104'),
          '1.3.6.1.1.9.2.15': ('1.3.6.1.1.9.2.15', OID_ATTRIBUTE_TYPE, 'pcelsExpectedValueList', 'RFC4104'),
          '1.3.6.1.1.9.2.16': ('1.3.6.1.1.9.2.16', OID_ATTRIBUTE_TYPE, 'pcelsVariableModelClass', 'RFC4104'),
          '1.3.6.1.1.9.2.17': ('1.3.6.1.1.9.2.17', OID_ATTRIBUTE_TYPE, 'pcelsVariableModelProperty', 'RFC4104'),
          '1.3.6.1.1.9.2.18': ('1.3.6.1.1.9.2.18', OID_ATTRIBUTE_TYPE, 'pcelsExpectedValueTypes', 'RFC4104'),
          '1.3.6.1.1.9.2.19': ('1.3.6.1.1.9.2.19', OID_ATTRIBUTE_TYPE, 'pcelsValueName', 'RFC4104'),
          '1.3.6.1.1.9.2.20': ('1.3.6.1.1.9.2.20', OID_ATTRIBUTE_TYPE, 'pcelsIPv4AddrList', 'RFC4104'),
          '1.3.6.1.1.9.2.21': ('1.3.6.1.1.9.2.21', OID_ATTRIBUTE_TYPE, 'pcelsIPv6AddrList', 'RFC4104'),
          '1.3.6.1.1.9.2.22': ('1.3.6.1.1.9.2.22', OID_ATTRIBUTE_TYPE, 'pcelsMACAddrList', 'RFC4104'),
          '1.3.6.1.1.9.2.23': ('1.3.6.1.1.9.2.23', OID_ATTRIBUTE_TYPE, 'pcelsStringList', 'RFC4104'),
          '1.3.6.1.1.9.2.24': ('1.3.6.1.1.9.2.24', OID_ATTRIBUTE_TYPE, 'pcelsBitStringList', 'RFC4104'),
          '1.3.6.1.1.9.2.25': ('1.3.6.1.1.9.2.25', OID_ATTRIBUTE_TYPE, 'pcelsIntegerList', 'RFC4104'),
          '1.3.6.1.1.9.2.26': ('1.3.6.1.1.9.2.26', OID_ATTRIBUTE_TYPE, 'pcelsBoolean', 'RFC4104'),
          '1.3.6.1.1.9.2.27': ('1.3.6.1.1.9.2.27', OID_ATTRIBUTE_TYPE, 'pcelsReusableContainerName', 'RFC4104'),
          '1.3.6.1.1.9.2.28': ('1.3.6.1.1.9.2.28', OID_ATTRIBUTE_TYPE, 'pcelsReusableContainerList', 'RFC4104'),
          '1.3.6.1.1.9.2.29': ('1.3.6.1.1.9.2.29', OID_ATTRIBUTE_TYPE, 'pcelsRole', 'RFC4104'),
          '1.3.6.1.1.9.2.30': ('1.3.6.1.1.9.2.30', OID_ATTRIBUTE_TYPE, 'pcelsRoleCollectionName', 'RFC4104'),
          '1.3.6.1.1.9.2.31': ('1.3.6.1.1.9.2.31', OID_ATTRIBUTE_TYPE, 'pcelsElementList', 'RFC4104'),
          '1.3.6.1.1.9.2.32': ('1.3.6.1.1.9.2.32', OID_ATTRIBUTE_TYPE, 'pcelsFilterName', 'RFC4104'),
          '1.3.6.1.1.9.2.33': ('1.3.6.1.1.9.2.33', OID_ATTRIBUTE_TYPE, 'pcelsFilterIsNegated', 'RFC4104'),
          '1.3.6.1.1.9.2.34': ('1.3.6.1.1.9.2.34', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrVersion', 'RFC4104'),
          '1.3.6.1.1.9.2.35': ('1.3.6.1.1.9.2.35', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrSourceAddress', 'RFC4104'),
          '1.3.6.1.1.9.2.36': ('1.3.6.1.1.9.2.36', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrSourceAddressEndOfRange', 'RFC4104'),
          '1.3.6.1.1.9.2.37': ('1.3.6.1.1.9.2.37', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrSourceMask', 'RFC4104'),
          '1.3.6.1.1.9.2.38': ('1.3.6.1.1.9.2.38', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrDestAddress', 'RFC4104'),
          '1.3.6.1.1.9.2.39': ('1.3.6.1.1.9.2.39', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrDestAddressEndOfRange', 'RFC4104'),
          '1.3.6.1.1.9.2.40': ('1.3.6.1.1.9.2.40', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrDestMask', 'RFC4104'),
          '1.3.6.1.1.9.2.41': ('1.3.6.1.1.9.2.41', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrProtocolID', 'RFC4104'),
          '1.3.6.1.1.9.2.42': ('1.3.6.1.1.9.2.42', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrSourcePortStart', 'RFC4104'),
          '1.3.6.1.1.9.2.43': ('1.3.6.1.1.9.2.43', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrSourcePortEnd', 'RFC4104'),
          '1.3.6.1.1.9.2.44': ('1.3.6.1.1.9.2.44', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrDestPortStart', 'RFC4104'),
          '1.3.6.1.1.9.2.45': ('1.3.6.1.1.9.2.45', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrDestPortEnd', 'RFC4104'),
          '1.3.6.1.1.9.2.46': ('1.3.6.1.1.9.2.46', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrDSCPList', 'RFC4104'),
          '1.3.6.1.1.9.2.47': ('1.3.6.1.1.9.2.47', OID_ATTRIBUTE_TYPE, 'pcelsIPHdrFlowLabel', 'RFC4104'),
          '1.3.6.1.1.9.2.48': ('1.3.6.1.1.9.2.48', OID_ATTRIBUTE_TYPE, 'pcels8021HdrSourceMACAddress', 'RFC4104'),
          '1.3.6.1.1.9.2.49': ('1.3.6.1.1.9.2.49', OID_ATTRIBUTE_TYPE, 'pcels8021HdrSourceMACMask', 'RFC4104'),
          '1.3.6.1.1.9.2.50': ('1.3.6.1.1.9.2.50', OID_ATTRIBUTE_TYPE, 'pcels8021HdrDestMACAddress', 'RFC4104'),
          '1.3.6.1.1.9.2.51': ('1.3.6.1.1.9.2.51', OID_ATTRIBUTE_TYPE, 'pcels8021HdrDestMACMask', 'RFC4104'),
          '1.3.6.1.1.9.2.52': ('1.3.6.1.1.9.2.52', OID_ATTRIBUTE_TYPE, 'pcels8021HdrProtocolID', 'RFC4104'),
          '1.3.6.1.1.9.2.53': ('1.3.6.1.1.9.2.53', OID_ATTRIBUTE_TYPE, 'pcels8021HdrPriority', 'RFC4104'),
          '1.3.6.1.1.9.2.54': ('1.3.6.1.1.9.2.54', OID_ATTRIBUTE_TYPE, 'pcels8021HdrVLANID', 'RFC4104'),
          '1.3.6.1.1.9.2.55': ('1.3.6.1.1.9.2.55', OID_ATTRIBUTE_TYPE, 'pcelsFilterListName', 'RFC4104'),
          '1.3.6.1.1.9.2.56': ('1.3.6.1.1.9.2.56', OID_ATTRIBUTE_TYPE, 'pcelsFilterDirection', 'RFC4104'),
          '1.3.6.1.1.9.2.57': ('1.3.6.1.1.9.2.57', OID_ATTRIBUTE_TYPE, 'pcelsFilterEntryList', 'RFC4104'),
          '1.3.6.1.1.9.2.58': ('1.3.6.1.1.9.2.58', OID_ATTRIBUTE_TYPE, 'pcelsVendorVariableData', 'RFC4104'),
          '1.3.6.1.1.9.2.59': ('1.3.6.1.1.9.2.59', OID_ATTRIBUTE_TYPE, 'pcelsVendorVariableEncoding', 'RFC4104'),
          '1.3.6.1.1.9.2.60': ('1.3.6.1.1.9.2.60', OID_ATTRIBUTE_TYPE, 'pcelsVendorValueData', 'RFC4104'),
          '1.3.6.1.1.9.2.61': ('1.3.6.1.1.9.2.61', OID_ATTRIBUTE_TYPE, 'pcelsVendorValueEncoding', 'RFC4104'),
          '1.3.6.1.1.9.2.62': ('1.3.6.1.1.9.2.62', OID_ATTRIBUTE_TYPE, 'pcelsRuleValidityPeriodList', 'RFC4104'),
          '1.3.6.1.4.1.11.1.3.1.1.0': ('1.3.6.1.4.1.11.1.3.1.1.0', OID_ATTRIBUTE_TYPE, 'defaultServerList', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.1': ('1.3.6.1.4.1.11.1.3.1.1.1', OID_ATTRIBUTE_TYPE, 'defaultSearchBase', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.2': ('1.3.6.1.4.1.11.1.3.1.1.2', OID_ATTRIBUTE_TYPE, 'preferredServerList', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.3': ('1.3.6.1.4.1.11.1.3.1.1.3', OID_ATTRIBUTE_TYPE, 'search_time_limit', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.4': ('1.3.6.1.4.1.11.1.3.1.1.4', OID_ATTRIBUTE_TYPE, 'bindTimeLimit', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.5': ('1.3.6.1.4.1.11.1.3.1.1.5', OID_ATTRIBUTE_TYPE, 'followReferrals', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.6': ('1.3.6.1.4.1.11.1.3.1.1.6', OID_ATTRIBUTE_TYPE, 'authenticationMethod', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.7': ('1.3.6.1.4.1.11.1.3.1.1.7', OID_ATTRIBUTE_TYPE, 'profileTTL', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.9': ('1.3.6.1.4.1.11.1.3.1.1.9', OID_ATTRIBUTE_TYPE, 'attributeMap', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.10': ('1.3.6.1.4.1.11.1.3.1.1.10', OID_ATTRIBUTE_TYPE, 'credentialLevel', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.11': ('1.3.6.1.4.1.11.1.3.1.1.11', OID_ATTRIBUTE_TYPE, 'objectclassMap', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.12': ('1.3.6.1.4.1.11.1.3.1.1.12', OID_ATTRIBUTE_TYPE, 'defaultSearchScope', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.13': ('1.3.6.1.4.1.11.1.3.1.1.13', OID_ATTRIBUTE_TYPE, 'serviceCredentialLevel', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.14': ('1.3.6.1.4.1.11.1.3.1.1.14', OID_ATTRIBUTE_TYPE, 'serviceSearchDescriptor', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.15': ('1.3.6.1.4.1.11.1.3.1.1.15', OID_ATTRIBUTE_TYPE, 'serviceAuthenticationMethod', 'RFC4876'),
          '1.3.6.1.4.1.11.1.3.1.1.16': ('1.3.6.1.4.1.11.1.3.1.1.16', OID_ATTRIBUTE_TYPE, 'dereferenceAliases', 'RFC4876'),
          '1.3.6.1.4.1.1466.101.119.3': ('1.3.6.1.4.1.1466.101.119.3', OID_ATTRIBUTE_TYPE, 'entryTtl', 'RFC2589'),
          '1.3.6.1.4.1.1466.101.119.4': ('1.3.6.1.4.1.1466.101.119.4', OID_ATTRIBUTE_TYPE, 'dynamicSubtrees', 'RFC2589'),
          '1.3.6.1.4.1.1466.101.120.1': ('1.3.6.1.4.1.1466.101.120.1', OID_ATTRIBUTE_TYPE, 'administratorsAddress', 'Mark_Wahl'),
          '1.3.6.1.4.1.1466.101.120.5': ('1.3.6.1.4.1.1466.101.120.5', OID_ATTRIBUTE_TYPE, 'namingContexts', 'RFC4512'),
          '1.3.6.1.4.1.1466.101.120.6': ('1.3.6.1.4.1.1466.101.120.6', OID_ATTRIBUTE_TYPE, 'altServer', 'RFC4512'),
          '1.3.6.1.4.1.1466.101.120.7': ('1.3.6.1.4.1.1466.101.120.7', OID_ATTRIBUTE_TYPE, 'supportedExtension', 'RFC4512'),
          '1.3.6.1.4.1.1466.101.120.13': ('1.3.6.1.4.1.1466.101.120.13', OID_ATTRIBUTE_TYPE, 'supportedControl', 'RFC4512'),
          '1.3.6.1.4.1.1466.101.120.14': ('1.3.6.1.4.1.1466.101.120.14', OID_ATTRIBUTE_TYPE, 'supportedSASLMechanisms', 'RFC4512'),
          '1.3.6.1.4.1.1466.101.120.15': ('1.3.6.1.4.1.1466.101.120.15', OID_ATTRIBUTE_TYPE, 'supportedLDAPVersion', 'RFC4512'),
          '1.3.6.1.4.1.1466.101.120.16': ('1.3.6.1.4.1.1466.101.120.16', OID_ATTRIBUTE_TYPE, 'ldapSyntaxes', 'RFC4512'),
          '1.3.6.1.4.1.16572.2.2.1': ('1.3.6.1.4.1.16572.2.2.1', OID_ATTRIBUTE_TYPE, 'providerCertificateHash', 'RFC6109'),
          '1.3.6.1.4.1.16572.2.2.2': ('1.3.6.1.4.1.16572.2.2.2', OID_ATTRIBUTE_TYPE, 'providerCertificate', 'RFC6109'),
          '1.3.6.1.4.1.16572.2.2.3': ('1.3.6.1.4.1.16572.2.2.3', OID_ATTRIBUTE_TYPE, 'providerName', 'RFC6109'),
          '1.3.6.1.4.1.16572.2.2.4': ('1.3.6.1.4.1.16572.2.2.4', OID_ATTRIBUTE_TYPE, 'mailReceipt', 'RFC6109'),
          '1.3.6.1.4.1.16572.2.2.5': ('1.3.6.1.4.1.16572.2.2.5', OID_ATTRIBUTE_TYPE, 'managedDomains', 'RFC6109'),
          '1.3.6.1.4.1.16572.2.2.6': ('1.3.6.1.4.1.16572.2.2.6', OID_ATTRIBUTE_TYPE, 'LDIFLocationURL', 'RFC6109'),
          '1.3.6.1.4.1.16572.2.2.7': ('1.3.6.1.4.1.16572.2.2.7', OID_ATTRIBUTE_TYPE, 'providerUnit', 'RFC6109'),
          '1.3.6.1.4.1.250.1.57': ('1.3.6.1.4.1.250.1.57', OID_ATTRIBUTE_TYPE, 'labeledURI', 'RFC2079'),
          '1.3.6.1.4.1.31103.1.1': ('1.3.6.1.4.1.31103.1.1', OID_ATTRIBUTE_TYPE, 'fedfsUuid', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.2': ('1.3.6.1.4.1.31103.1.2', OID_ATTRIBUTE_TYPE, 'fedfsNetAddr', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.3': ('1.3.6.1.4.1.31103.1.3', OID_ATTRIBUTE_TYPE, 'fedfsNetPort', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.4': ('1.3.6.1.4.1.31103.1.4', OID_ATTRIBUTE_TYPE, 'fedfsFsnUuid', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.5': ('1.3.6.1.4.1.31103.1.5', OID_ATTRIBUTE_TYPE, 'fedfsNsdbName', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.6': ('1.3.6.1.4.1.31103.1.6', OID_ATTRIBUTE_TYPE, 'fedfsNsdbPort', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.7': ('1.3.6.1.4.1.31103.1.7', OID_ATTRIBUTE_TYPE, 'fedfsNcePrefix', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.8': ('1.3.6.1.4.1.31103.1.8', OID_ATTRIBUTE_TYPE, 'fedfsFslUuid', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.9': ('1.3.6.1.4.1.31103.1.9', OID_ATTRIBUTE_TYPE, 'fedfsFslHost', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.10': ('1.3.6.1.4.1.31103.1.10', OID_ATTRIBUTE_TYPE, 'fedfsFslPort', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.11': ('1.3.6.1.4.1.31103.1.11', OID_ATTRIBUTE_TYPE, 'fedfsFslTTL', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.12': ('1.3.6.1.4.1.31103.1.12', OID_ATTRIBUTE_TYPE, 'fedfsAnnotation', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.13': ('1.3.6.1.4.1.31103.1.13', OID_ATTRIBUTE_TYPE, 'fedfsDescr', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.14': ('1.3.6.1.4.1.31103.1.14', OID_ATTRIBUTE_TYPE, 'fedfsNceDN', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.15': ('1.3.6.1.4.1.31103.1.15', OID_ATTRIBUTE_TYPE, 'fedfsFsnTTL', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.100': ('1.3.6.1.4.1.31103.1.100', OID_ATTRIBUTE_TYPE, 'fedfsNfsPath', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.101': ('1.3.6.1.4.1.31103.1.101', OID_ATTRIBUTE_TYPE, 'fedfsNfsMajorVer', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.102': ('1.3.6.1.4.1.31103.1.102', OID_ATTRIBUTE_TYPE, 'fedfsNfsMinorVer', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.103': ('1.3.6.1.4.1.31103.1.103', OID_ATTRIBUTE_TYPE, 'fedfsNfsCurrency', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.104': ('1.3.6.1.4.1.31103.1.104', OID_ATTRIBUTE_TYPE, 'fedfsNfsGenFlagWritable', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.105': ('1.3.6.1.4.1.31103.1.105', OID_ATTRIBUTE_TYPE, 'fedfsNfsGenFlagGoing', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.106': ('1.3.6.1.4.1.31103.1.106', OID_ATTRIBUTE_TYPE, 'fedfsNfsGenFlagSplit', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.107': ('1.3.6.1.4.1.31103.1.107', OID_ATTRIBUTE_TYPE, 'fedfsNfsTransFlagRdma', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.108': ('1.3.6.1.4.1.31103.1.108', OID_ATTRIBUTE_TYPE, 'fedfsNfsClassSimul', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.109': ('1.3.6.1.4.1.31103.1.109', OID_ATTRIBUTE_TYPE, 'fedfsNfsClassHandle', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.110': ('1.3.6.1.4.1.31103.1.110', OID_ATTRIBUTE_TYPE, 'fedfsNfsClassFileid', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.111': ('1.3.6.1.4.1.31103.1.111', OID_ATTRIBUTE_TYPE, 'fedfsNfsClassWritever', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.112': ('1.3.6.1.4.1.31103.1.112', OID_ATTRIBUTE_TYPE, 'fedfsNfsClassChange', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.113': ('1.3.6.1.4.1.31103.1.113', OID_ATTRIBUTE_TYPE, 'fedfsNfsClassReaddir', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.114': ('1.3.6.1.4.1.31103.1.114', OID_ATTRIBUTE_TYPE, 'fedfsNfsReadRank', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.115': ('1.3.6.1.4.1.31103.1.115', OID_ATTRIBUTE_TYPE, 'fedfsNfsReadOrder', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.116': ('1.3.6.1.4.1.31103.1.116', OID_ATTRIBUTE_TYPE, 'fedfsNfsWriteRank', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.117': ('1.3.6.1.4.1.31103.1.117', OID_ATTRIBUTE_TYPE, 'fedfsNfsWriteOrder', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.118': ('1.3.6.1.4.1.31103.1.118', OID_ATTRIBUTE_TYPE, 'fedfsNfsVarSub', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.119': ('1.3.6.1.4.1.31103.1.119', OID_ATTRIBUTE_TYPE, 'fedfsNfsValidFor', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.31103.1.120': ('1.3.6.1.4.1.31103.1.120', OID_ATTRIBUTE_TYPE, 'fedfsNfsURI', 'RFC-ietf-nfsv4-federated-fs-protocol-15'),
          '1.3.6.1.4.1.4203.1.3.5': ('1.3.6.1.4.1.4203.1.3.5', OID_ATTRIBUTE_TYPE, 'supportedFeatures', 'RFC4512'),
          '1.3.6.1.4.1.453.7.2.1': ('1.3.6.1.4.1.453.7.2.1', OID_ATTRIBUTE_TYPE, 'textTableKey', 'RFC2293'),
          '1.3.6.1.4.1.453.7.2.2': ('1.3.6.1.4.1.453.7.2.2', OID_ATTRIBUTE_TYPE, 'textTableValue', 'RFC2293'),
          '1.3.6.1.4.1.453.7.2.3': ('1.3.6.1.4.1.453.7.2.3', OID_ATTRIBUTE_TYPE, ['associatedX400Gateway', 'distinguishedNameTableKey'], 'RFC2164-RFC2293'),
          '1.3.6.1.4.1.453.7.2.6': ('1.3.6.1.4.1.453.7.2.6', OID_ATTRIBUTE_TYPE, 'associatedORAddress', 'RFC2164'),
          '1.3.6.1.4.1.453.7.2.7': ('1.3.6.1.4.1.453.7.2.7', OID_ATTRIBUTE_TYPE, 'oRAddressComponentType', 'RFC2164'),
          '1.3.6.1.4.1.453.7.2.8': ('1.3.6.1.4.1.453.7.2.8', OID_ATTRIBUTE_TYPE, 'associatedInternetGateway', 'RFC2164'),
          '1.3.6.1.4.1.453.7.2.9': ('1.3.6.1.4.1.453.7.2.9', OID_ATTRIBUTE_TYPE, 'mcgamTables', 'RFC2164'),
          '2.16.840.1.113730.3.1.34': ('2.16.840.1.113730.3.1.34', OID_ATTRIBUTE_TYPE, 'ref', 'RFC3296'),
          '2.5.18.1': ('2.5.18.1', OID_ATTRIBUTE_TYPE, 'createTimestamp', 'RFC4512'),
          '2.5.18.2': ('2.5.18.2', OID_ATTRIBUTE_TYPE, 'modifyTimestamp', 'RFC4512'),
          '2.5.18.3': ('2.5.18.3', OID_ATTRIBUTE_TYPE, 'creatorsName', 'RFC4512'),
          '2.5.18.4': ('2.5.18.4', OID_ATTRIBUTE_TYPE, 'modifiersName', 'RFC4512'),
          '2.5.18.5': ('2.5.18.5', OID_ATTRIBUTE_TYPE, 'administrativeRole', 'RFC3672'),
          '2.5.18.6': ('2.5.18.6', OID_ATTRIBUTE_TYPE, 'subtreeSpecification', 'RFC3672'),
          '2.5.18.7': ('2.5.18.7', OID_ATTRIBUTE_TYPE, 'collectiveExclusions', 'RFC3671'),
          '2.5.18.10': ('2.5.18.10', OID_ATTRIBUTE_TYPE, 'subschemaSubentry', 'RFC4512'),
          '2.5.18.12': ('2.5.18.12', OID_ATTRIBUTE_TYPE, 'collectiveAttributeSubentries', 'RFC3671'),
          '2.5.21.1': ('2.5.21.1', OID_ATTRIBUTE_TYPE, 'dITStructureRules', 'RFC4512'),
          '2.5.21.2': ('2.5.21.2', OID_ATTRIBUTE_TYPE, 'dITContentRules', 'RFC4512'),
          '2.5.21.4': ('2.5.21.4', OID_ATTRIBUTE_TYPE, 'matchingRules', 'RFC4512'),
          '2.5.21.5': ('2.5.21.5', OID_ATTRIBUTE_TYPE, 'attributeTypes', 'RFC4512'),
          '2.5.21.6': ('2.5.21.6', OID_ATTRIBUTE_TYPE, 'objectClasses', 'RFC4512'),
          '2.5.21.7': ('2.5.21.7', OID_ATTRIBUTE_TYPE, 'nameForms', 'RFC4512'),
          '2.5.21.8': ('2.5.21.8', OID_ATTRIBUTE_TYPE, 'matchingRuleUse', 'RFC4512'),
          '2.5.21.9': ('2.5.21.9', OID_ATTRIBUTE_TYPE, 'structuralObjectClass', 'RFC4512'),
          '2.5.21.10': ('2.5.21.10', OID_ATTRIBUTE_TYPE, 'governingStructureRule', 'RFC4512'),
          '2.5.4.0': ('2.5.4.0', OID_ATTRIBUTE_TYPE, 'objectClass', 'RFC4512'),
          '2.5.4.1': ('2.5.4.1', OID_ATTRIBUTE_TYPE, ['aliasedEntryName', 'aliasedObjectName'], 'X.501-RFC4512'),
          '2.5.4.2': ('2.5.4.2', OID_ATTRIBUTE_TYPE, 'knowledgeInformation', 'RFC2256'),
          '2.5.4.3': ('2.5.4.3', OID_ATTRIBUTE_TYPE, ['cn', 'commonName'], 'RFC4519'),
          '2.5.4.4': ('2.5.4.4', OID_ATTRIBUTE_TYPE, ['sn', 'surname'], 'RFC4519'),
          '2.5.4.5': ('2.5.4.5', OID_ATTRIBUTE_TYPE, 'serialNumber', 'RFC4519'),
          '2.5.4.6': ('2.5.4.6', OID_ATTRIBUTE_TYPE, ['c', 'countryName'], 'RFC4519'),
          '2.5.4.7': ('2.5.4.7', OID_ATTRIBUTE_TYPE, ['L', 'localityName'], 'RFC4519'),
          '2.5.4.7.1': ('2.5.4.7.1', OID_ATTRIBUTE_TYPE, 'c-l', 'RFC3671'),
          '2.5.4.8': ('2.5.4.8', OID_ATTRIBUTE_TYPE, ['st', 'stateOrProvinceName'], 'RFC4519-RFC2256'),
          '2.5.4.8.1': ('2.5.4.8.1', OID_ATTRIBUTE_TYPE, 'c-st', 'RFC3671'),
          '2.5.4.9': ('2.5.4.9', OID_ATTRIBUTE_TYPE, ['street', 'streetAddress'], 'RFC4519-RFC2256'),
          '2.5.4.9.1': ('2.5.4.9.1', OID_ATTRIBUTE_TYPE, 'c-street', 'RFC3671'),
          '2.5.4.10': ('2.5.4.10', OID_ATTRIBUTE_TYPE, ['o', 'organizationName'], 'RFC4519'),
          '2.5.4.10.1': ('2.5.4.10.1', OID_ATTRIBUTE_TYPE, 'c-o', 'RFC3671'),
          '2.5.4.11': ('2.5.4.11', OID_ATTRIBUTE_TYPE, ['ou', 'organizationalUnitName'], 'RFC4519'),
          '2.5.4.11.1': ('2.5.4.11.1', OID_ATTRIBUTE_TYPE, 'c-ou', 'RFC3671'),
          '2.5.4.12': ('2.5.4.12', OID_ATTRIBUTE_TYPE, 'title', 'RFC4519'),
          '2.5.4.13': ('2.5.4.13', OID_ATTRIBUTE_TYPE, 'description', 'RFC4519'),
          '2.5.4.14': ('2.5.4.14', OID_ATTRIBUTE_TYPE, 'searchGuide', 'RFC4519'),
          '2.5.4.15': ('2.5.4.15', OID_ATTRIBUTE_TYPE, 'businessCategory', 'RFC4519'),
          '2.5.4.16': ('2.5.4.16', OID_ATTRIBUTE_TYPE, 'postalAddress', 'RFC4519'),
          '2.5.4.16.1': ('2.5.4.16.1', OID_ATTRIBUTE_TYPE, 'c-PostalAddress', 'RFC3671'),
          '2.5.4.17': ('2.5.4.17', OID_ATTRIBUTE_TYPE, 'postalCode', 'RFC4519'),
          '2.5.4.17.1': ('2.5.4.17.1', OID_ATTRIBUTE_TYPE, 'c-PostalCode', 'RFC3671'),
          '2.5.4.18': ('2.5.4.18', OID_ATTRIBUTE_TYPE, 'postOfficeBox', 'RFC4519'),
          '2.5.4.18.1': ('2.5.4.18.1', OID_ATTRIBUTE_TYPE, 'c-PostOfficeBox', 'RFC3671'),
          '2.5.4.19': ('2.5.4.19', OID_ATTRIBUTE_TYPE, 'physicalDeliveryOfficeName', 'RFC4519'),
          '2.5.4.19.1': ('2.5.4.19.1', OID_ATTRIBUTE_TYPE, 'c-PhysicalDeliveryOffice', 'RFC3671'),
          '2.5.4.20': ('2.5.4.20', OID_ATTRIBUTE_TYPE, 'telephoneNumber', 'RFC4519'),
          '2.5.4.20.1': ('2.5.4.20.1', OID_ATTRIBUTE_TYPE, 'c-TelephoneNumber', 'RFC3671'),
          '2.5.4.21': ('2.5.4.21', OID_ATTRIBUTE_TYPE, 'telexNumber', 'RFC4519'),
          '2.5.4.21.1': ('2.5.4.21.1', OID_ATTRIBUTE_TYPE, 'c-TelexNumber', 'RFC3671'),
          '2.5.4.22': ('2.5.4.22', OID_ATTRIBUTE_TYPE, 'teletexTerminalIdentifier', 'RFC4519'),
          '2.5.4.23': ('2.5.4.23', OID_ATTRIBUTE_TYPE, 'facsimileTelephoneNumber', 'RFC4519'),
          '2.5.4.23.1': ('2.5.4.23.1', OID_ATTRIBUTE_TYPE, 'c-FacsimileTelephoneNumber', 'RFC3671'),
          '2.5.4.24': ('2.5.4.24', OID_ATTRIBUTE_TYPE, 'x121Address', 'RFC4519'),
          '2.5.4.25': ('2.5.4.25', OID_ATTRIBUTE_TYPE, 'internationaliSDNNumber', 'RFC4519'),
          '2.5.4.25.1': ('2.5.4.25.1', OID_ATTRIBUTE_TYPE, 'c-InternationalISDNNumber', 'RFC3671'),
          '2.5.4.26': ('2.5.4.26', OID_ATTRIBUTE_TYPE, 'registeredAddress', 'RFC4519'),
          '2.5.4.27': ('2.5.4.27', OID_ATTRIBUTE_TYPE, 'destinationIndicator', 'RFC4519'),
          '2.5.4.28': ('2.5.4.28', OID_ATTRIBUTE_TYPE, 'preferredDeliveryMethod', 'RFC4519'),
          '2.5.4.29': ('2.5.4.29', OID_ATTRIBUTE_TYPE, 'presentationAddress', 'RFC2256'),
          '2.5.4.30': ('2.5.4.30', OID_ATTRIBUTE_TYPE, 'supportedApplicationContext', 'RFC2256'),
          '2.5.4.31': ('2.5.4.31', OID_ATTRIBUTE_TYPE, 'member', 'RFC4519'),
          '2.5.4.32': ('2.5.4.32', OID_ATTRIBUTE_TYPE, 'owner', 'RFC4519'),
          '2.5.4.33': ('2.5.4.33', OID_ATTRIBUTE_TYPE, 'roleOccupant', 'RFC4519'),
          '2.5.4.34': ('2.5.4.34', OID_ATTRIBUTE_TYPE, 'seeAlso', 'RFC4519'),
          '2.5.4.35': ('2.5.4.35', OID_ATTRIBUTE_TYPE, 'userPassword', 'RFC4519'),
          '2.5.4.36': ('2.5.4.36', OID_ATTRIBUTE_TYPE, 'userCertificate', 'RFC4523'),
          '2.5.4.37': ('2.5.4.37', OID_ATTRIBUTE_TYPE, 'cACertificate', 'RFC4523'),
          '2.5.4.38': ('2.5.4.38', OID_ATTRIBUTE_TYPE, 'authorityRevocationList', 'RFC4523'),
          '2.5.4.39': ('2.5.4.39', OID_ATTRIBUTE_TYPE, 'certificateRevocationList', 'RFC4523'),
          '2.5.4.40': ('2.5.4.40', OID_ATTRIBUTE_TYPE, 'crossCertificatePair', 'RFC4523'),
          '2.5.4.41': ('2.5.4.41', OID_ATTRIBUTE_TYPE, 'name', 'RFC4519'),
          '2.5.4.42': ('2.5.4.42', OID_ATTRIBUTE_TYPE, 'givenName', 'RFC4519'),
          '2.5.4.43': ('2.5.4.43', OID_ATTRIBUTE_TYPE, 'initials', 'RFC4519'),
          '2.5.4.44': ('2.5.4.44', OID_ATTRIBUTE_TYPE, 'generationQualifier', 'RFC4519'),
          '2.5.4.45': ('2.5.4.45', OID_ATTRIBUTE_TYPE, 'x500UniqueIdentifier', 'RFC4519'),
          '2.5.4.46': ('2.5.4.46', OID_ATTRIBUTE_TYPE, 'dnQualifier', 'RFC4519'),
          '2.5.4.47': ('2.5.4.47', OID_ATTRIBUTE_TYPE, 'enhancedSearchGuide', 'RFC4519'),
          '2.5.4.48': ('2.5.4.48', OID_ATTRIBUTE_TYPE, 'protocolInformation', 'RFC2256'),
          '2.5.4.49': ('2.5.4.49', OID_ATTRIBUTE_TYPE, 'distinguishedName', 'RFC4519'),
          '2.5.4.50': ('2.5.4.50', OID_ATTRIBUTE_TYPE, 'uniqueMember', 'RFC4519'),
          '2.5.4.51': ('2.5.4.51', OID_ATTRIBUTE_TYPE, 'houseIdentifier', 'RFC4519'),
          '2.5.4.52': ('2.5.4.52', OID_ATTRIBUTE_TYPE, 'supportedAlgorithms', 'RFC4523'),
          '2.5.4.53': ('2.5.4.53', OID_ATTRIBUTE_TYPE, 'deltaRevocationList', 'RFC4523'),
          '2.5.4.54': ('2.5.4.54', OID_ATTRIBUTE_TYPE, 'dmdName', 'RFC2256'),
          '2.5.4.65': ('2.5.4.65', OID_ATTRIBUTE_TYPE, 'pseudonym', 'RFC3280'),
          '2.16.840.1.113719.1.1.4.1.501': ('2.16.840.1.113719.1.1.4.1.501', OID_ATTRIBUTE_TYPE, 'GUID', 'NOVELL'),
          '2.16.840.1.113719.1.27.4.50': ('2.16.840.1.113719.1.27.4.50', OID_ATTRIBUTE_TYPE, 'localEntryID', 'NOVELL'),
          '2.16.840.1.113730.3.8.3.1': ('2.16.840.1.113730.3.8.3.1', OID_ATTRIBUTE_TYPE, 'ipaUniqueID', 'freeIPA'),
          '2.16.840.1.113730.3.8.3.2': ('2.16.840.1.113730.3.8.3.2', OID_ATTRIBUTE_TYPE, 'ipaClientVersion', 'freeIPA'),
          '2.16.840.1.113730.3.8.3.3': ('2.16.840.1.113730.3.8.3.3', OID_ATTRIBUTE_TYPE, 'enrolledBy', 'freeIPA'),
          '2.16.840.1.113730.3.8.3.4': ('2.16.840.1.113730.3.8.3.4', OID_ATTRIBUTE_TYPE, 'fqdn', 'freeIPA'),
          '2.16.840.1.113730.3.8.3.18': ('2.16.840.1.113730.3.8.3.18', OID_ATTRIBUTE_TYPE, 'managedBy', 'freeIPA'),
          '2.16.840.1.113730.3.8.3.24': ('2.16.840.1.113730.3.8.3.24', OID_ATTRIBUTE_TYPE, 'ipaEntitlementId', 'freeIPA'),

}
