import ldap
import os
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
l = ldap.initialize('ldap://172.17.0.2:636')
l.set_option(ldap.OPT_REFERRALS, 0)
l.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
l.set_option(ldap.OPT_X_TLS_CACERTFILE, os.getcwd()+"/ldap.crt")
l.set_option(ldap.OPT_X_TLS,ldap.OPT_X_TLS_DEMAND)
l.set_option(ldap.OPT_X_TLS_DEMAND, True)
l.set_option(ldap.OPT_DEBUG_LEVEL, 255)
##l.simple_bind_s("admin@tester.com","password")
# Force libldap to create a new SSL context (must be last TLS option!)
l.set_option(ldap.OPT_X_TLS_NEWCTX, 0)
l.start_tls_s()

#!/usr/bin/env python
#import ldap, sys
#LDAP_SERVER = 'ldaps://ldap.example.com:636'
#LDAP_BASE = 'dc=example,dc=com'

#try:
#    conn = ldap.initialize(LDAP_SERVER)
#except ldap.LDAPError, e:
#    sys.stderr.write("Fatal Error.n")
#    raise
LDAP_BASE = 'dc=example,dc=org'
# this may or may not raise an error, e.g. TLS error -8172
items = l.search_s(LDAP_BASE, ldap.SCOPE_SUBTREE, attrlist=['dn'])