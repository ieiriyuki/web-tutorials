## The public facing ip of the whole JupyterHub application
#          (specifically referred to as the proxy).
#
#          This is the address on which the proxy will listen. The default is to
#          listen on all interfaces. This is the only address through which JupyterHub
#          should be accessed by users.
#
#          .. deprecated: 0.9
#              Use JupyterHub.bind_url
#  Default: ''
c.JupyterHub.ip = '0.0.0.0'

## The public facing port of the proxy.
#
#          This is the port on which the proxy will listen.
#          This is the only port through which JupyterHub
#          should be accessed by users.
#
#          .. deprecated: 0.9
#              Use JupyterHub.bind_url
#  Default: 8000
# c.JupyterHub.port = 8000

## The IP address (or hostname) the single-user server should listen on.
#
#  Usually either '127.0.0.1' (default) or '0.0.0.0'.
#
#  The JupyterHub proxy implementation should be able to send packets to this
#  interface.
#
#  Subclasses which launch remotely or in containers should override the default
#  to '0.0.0.0'.
#
#  .. versionchanged:: 2.0
#      Default changed to '127.0.0.1', from ''.
#      In most cases, this does not result in a change in behavior,
#      as '' was interpreted as 'unspecified',
#      which used the subprocesses' own default, itself usually '127.0.0.1'.
#  Default: '127.0.0.1'
c.Spawner.ip = '0.0.0.0'

## The port for single-user servers to listen on.
#
#  Defaults to `0`, which uses a randomly allocated port number each time.
#
#  If set to a non-zero value, all Spawners will use the same port, which only
#  makes sense if each server is on a different address, e.g. in containers.
#
#  New in version 0.7.
#  Default: 0
# c.Spawner.port = 0

## Set of users that will have admin rights on this JupyterHub.
#
#  Note: As of JupyterHub 2.0, full admin rights should not be required, and more
#  precise permissions can be managed via roles.
#
#  Admin users have extra privileges:
#   - Use the admin panel to see list of users logged in
#   - Add / remove users in some authenticators
#   - Restart / halt the hub
#   - Start / stop users' single-user servers
#   - Can access each individual users' single-user server (if configured)
#
#  Admin access should be treated the same way root access is.
#
#  Defaults to an empty set, in which case no user has admin access.
#  Default: set()
# c.Authenticator.admin_users = set()

## Set of usernames that are allowed to log in.
#
#  Use this with supported authenticators to restrict which users can log in.
#  This is an additional list that further restricts users, beyond whatever
#  restrictions the authenticator has in place. Any user in this list is granted
#  the 'user' role on hub startup.
#
#  If empty, does not perform any additional restriction.
#
#  .. versionchanged:: 1.2
#      `Authenticator.whitelist` renamed to `allowed_users`
#  Default: set()
# c.Authenticator.allowed_users = set()
