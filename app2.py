import sys,ldap

# Set debugging level
ldap.set_option(ldap.OPT_DEBUG_LEVEL,0)
ldapmodule_trace_level = 1
ldapmodule_trace_file = sys.stderr

# Complete path name of the file containing all trusted CA certs
CACERTFILE='/etc/apache2/ssl.crt/ca-bundle.crt'

# TLS-related options have to be set globally since the TLS context is only initialized once

# Force cert validation
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT,ldap.OPT_X_TLS_DEMAND)
# Set path name of file containing all trusted CA certificates
ldap.set_option(ldap.OPT_X_TLS_CACERTFILE,CACERTFILE)


print( """##################################################################
# LDAPv3 connection with StartTLS
##################################################################
""")

# Create LDAPObject instance
l = ldap.initialize('ldap://172.17.0.2:636',trace_level=ldapmodule_trace_level,trace_file=ldapmodule_trace_file)

# Set LDAP protocol version used
l.protocol_version=ldap.VERSION3
# Force libldap to create a new SSL context
#l.set_option(ldap.OPT_X_TLS_NEWCTX,ldap.OPT_X_TLS_DEMAND)
# Force cert validation
#l.set_option(ldap.OPT_X_TLS_REQUIRE_CERT,ldap.OPT_X_TLS_DEMAND)
# Set path name of file containing all trusted CA certificates
#l.set_option(ldap.OPT_X_TLS_CACERTFILE,CACERTFILE)

# Now try StartTLS extended operation
l.start_tls_s()

# Try a bind to provoke failure if protocol version is not supported
l.simple_bind_s('','')

# Close connection
l.unbind_s()
