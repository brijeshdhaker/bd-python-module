#
# /home/brijeshdhaker/.ipython/profile_default
#

#
c.InteractiveShellApp.extensions = ['autoreload']

#
c.IPKernelApp.extensions = ['sql']

# Execute the configuration command on startup
c.InteractiveShellApp.exec_lines = [
    "%config SqlMagic.displaylimit = 25"
]