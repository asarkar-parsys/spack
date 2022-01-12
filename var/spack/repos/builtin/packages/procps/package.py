# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Procps(AutotoolsPackage):
    """Command line and full screen utilities for browsing procfs, a "pseudo"
    file system dynamically generated by the kernel to provide information
    about the status of entries in its process table."""

    homepage = "https://gitlab.com/procps-ng/procps"
    git      = "https://gitlab.com/procps-ng/procps.git"

    version('master', branch='master')
    version('3.3.15', tag='v3.3.15')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('pkgconfig@0.9.0:', type='build')
    depends_on('dejagnu',  type='test')
    depends_on('iconv')
    depends_on('gettext')
    depends_on('ncurses')

    conflicts('platform=darwin', msg='procps is linux-only')

    def autoreconf(self, spec, prefix):
        sh = which('sh')
        sh('autogen.sh')

    def configure_args(self):
        return [
            '--with-libiconv-prefix={0}'.format(self.spec['iconv'].prefix),
            '--with-libintl-prefix={0}'.format(self.spec['gettext'].prefix),
            '--with-ncurses',
            # Required to avoid libintl linking errors
            '--disable-nls',
        ]
