# Copyright (C) 2001, 2002  Internet Software Consortium.
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND INTERNET SOFTWARE CONSORTIUM
# DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# INTERNET SOFTWARE CONSORTIUM BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
# FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
# WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# $Id: Makefile.in,v 1.12.2.3 2002/08/05 06:57:11 marka Exp $

srcdir =        .

top_srcdir =    .


LIBINTERFACE = 1
LIBREVISION = 0
LIBAGE = 1

DAEMON_OBJS=bsd/daemon.o
STRSEP_OBJS=bsd/strsep.o

BSDOBJS=   bsd/ftruncate.o bsd/gettimeofday.o \
        bsd/mktemp.o bsd/putenv.o bsd/readv.o bsd/setenv.o \
	bsd/setitimer.o bsd/strcasecmp.o bsd/strdup.o \
        bsd/strerror.o bsd/strpbrk.o bsd/strtoul.o bsd/utimes.o \
        bsd/writev.o

DSTOBJS= dst/dst_api.o dst/hmac_link.o dst/md5_dgst.o dst/support.o

INETOBJS= inet/inet_addr.o inet/inet_cidr_ntop.o inet/inet_cidr_pton.o \
	inet/inet_data.o inet/inet_lnaof.o inet/inet_makeaddr.o \
	inet/inet_net_ntop.o inet/inet_net_pton.o inet/inet_neta.o \
	inet/inet_netof.o inet/inet_network.o inet/inet_ntoa.o \
	inet/inet_ntop.o inet/inet_pton.o inet/nsap_addr.o

WANT_IRS_THREADS_OBJS=	irs/gethostent_r.o irs/getnetgrent_r.o \
	irs/getprotoent_r.o irs/getservent_r.o

WANT_IRS_NISGR_OBJS= irs/nis_gr.o 
WANT_IRS_GR_OBJS= irs/dns_gr.o irs/irp_gr.o irs/lcl_gr.o irs/gen_gr.o \
	irs/getgrent.o  ${WANT_IRS_THREADSGR_OBJS}

WANT_IRS_THREADSPW_OBJS=irs/getpwent_r.o
WANT_IRS_NISPW_OBJS= irs/nis_pw.o
WANT_IRS_DBPW_OBJS=irs/irp_pw.o irs/lcl_pw.o
WANT_IRS_PW_OBJS= irs/dns_pw.o irs/gen_pw.o irs/getpwent.o \
	  ${WANT_IRS_THREADSPW_OBJS}

WANT_IRS_NIS_OBJS= irs/nis_ho.o irs/nis_ng.o irs/nis_nw.o \
	irs/nis_pr.o irs/nis_sv.o

IRSOBJS=   ${WANT_IRS_THREADS_OBJS} \
	 \
	irs/dns.o irs/dns_ho.o irs/dns_nw.o irs/dns_pr.o \
	irs/dns_sv.o irs/gai_strerror.o irs/gen.o irs/gen_ho.o \
	irs/gen_ng.o irs/gen_nw.o irs/gen_pr.o irs/gen_sv.o \
	irs/getaddrinfo.o irs/gethostent.o  irs/getnameinfo.o \
	irs/getnetent.o irs/getnetent_r.o irs/getnetgrent.o \
	irs/getprotoent.o irs/getservent.o irs/hesiod.o \
	irs/irp.o irs/irp_ho.o irs/irp_ng.o irs/irp_nw.o \
	irs/irp_pr.o irs/irp_sv.o irs/irpmarshall.o irs/irs_data.o \
	irs/lcl.o irs/lcl_ho.o irs/lcl_ng.o irs/lcl_nw.o \
	irs/lcl_pr.o irs/lcl_sv.o irs/nis.o irs/nul_ng.o irs/util.o

WANT_IRS_THREADSGR_OBJS=irs/getgrent_r.o

ISCOBJS= isc/assertions.o isc/base64.o isc/bitncmp.o isc/ctl_clnt.o \
	isc/ctl_p.o isc/ctl_srvr.o isc/ev_connects.o isc/ev_files.o \
	isc/ev_streams.o isc/ev_timers.o isc/ev_waits.o \
	isc/eventlib.o isc/heap.o isc/hex.o isc/logging.o \
	isc/memcluster.o isc/movefile.o isc/tree.o

NAMESEROBJS= nameser/ns_date.o nameser/ns_name.o nameser/ns_netint.o \
	nameser/ns_parse.o nameser/ns_print.o  nameser/ns_samedomain.o \
	nameser/ns_sign.o nameser/ns_ttl.o nameser/ns_verify.o

RESOLVOBJS= resolv/herror.o resolv/res_comp.o resolv/res_data.o \
	resolv/res_debug.o resolv/res_findzonecut.o resolv/res_init.o \
	resolv/res_mkquery.o resolv/res_mkupdate.o resolv/res_query.o \
	resolv/res_send.o resolv/res_sendsigned.o resolv/res_update.o

SUBDIRS = bsd dst include inet irs isc nameser resolv port/cygwin/include

TARGETS= timestamp
OBJS=	${BSDOBJS} ${DSTOBJS} ${INETOBJS} ${IRSOBJS} ${ISCOBJS} \
	${NAMESEROBJS} ${RESOLVOBJS}


# Copyright (C) 1998-2001  Internet Software Consortium.
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND INTERNET SOFTWARE CONSORTIUM
# DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# INTERNET SOFTWARE CONSORTIUM BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
# FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
# WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# $Id: rules.in,v 1.3.2.1.4.1 2003/02/17 01:35:20 marka Exp $

###
### Common Makefile rules for BIND 9.
###

###
### Paths
###
### Note: paths that vary by Makefile MUST NOT be listed
### here, or they won't get expanded correctly.

prefix =	/usr/local
exec_prefix =	${prefix}
bindir =	${exec_prefix}/bin
sbindir =	${exec_prefix}/sbin
includedir =	${prefix}/bind/include
libdir =	${exec_prefix}/lib
sysconfdir =	${prefix}/etc
localstatedir =	${prefix}/var
mandir =	${prefix}/man

DESTDIR =
MAKEDEFS= 'DESTDIR=${DESTDIR}'

MAKE=make

top_builddir =	/NetSec/bind-9.2.2/lib/bind
abs_top_srcdir = /NetSec/bind-9.2.2/lib/bind

###
### All
###
### Makefile may define:
###	TARGETS

all: subdirs ${TARGETS}

###
### Subdirectories
###
### Makefile may define:
###	SUBDIRS

ALL_SUBDIRS = ${SUBDIRS} nulldir

#
# We use a single-colon rule so that additional dependencies of
# subdirectories can be specified after the inclusion of this file.
# The "depend" target is treated the same way.
#
subdirs:
	@for i in ${ALL_SUBDIRS}; do \
		if [ "$$i" != "nulldir" -a -d $$i ]; then \
			echo "making all in `pwd`/$$i"; \
			(cd $$i; ${MAKE} ${MAKEDEFS} all) || exit 1; \
		fi \
	done

install clean distclean::
	@for i in ${ALL_SUBDIRS}; do \
		if [ "$$i" != "nulldir" -a -d $$i ]; then \
			echo "making $@ in `pwd`/$$i"; \
			(cd $$i; ${MAKE} ${MAKEDEFS} $@) || exit 1; \
		fi \
	done

###
### C Programs
###
### Makefile must define
###	CC
### Makefile may define
###	CFLAGS
###	CINCLUDES
###	CDEFINES
###	CWARNINGS
### User may define externally
###     EXT_CFLAGS

CC = 		gcc
CFLAGS =	-g -O2
STD_CINCLUDES =	
STD_CDEFINES =	
STD_CWARNINGS =	 -W -Wall -Wmissing-prototypes -Wcast-qual -Wwrite-strings

.SUFFIXES:
.SUFFIXES: .c .o

ALWAYS_INCLUDES = -I${top_builddir} -I${abs_top_srcdir}/port/cygwin/include
ALWAYS_DEFINES = -D_REENTRANT
ALWAYS_WARNINGS =

ALL_CPPFLAGS = \
	${ALWAYS_INCLUDES} ${CINCLUDES} ${STD_CINCLUDES} \
	${ALWAYS_DEFINES} ${CDEFINES} ${STD_CDEFINES}

ALL_CFLAGS = ${EXT_CFLAGS} ${CFLAGS} \
	${ALL_CPPFLAGS} \
	${ALWAYS_WARNINGS} ${STD_CWARNINGS} ${CWARNINGS}

.c.o:
	${LIBTOOL} ${CC} ${ALL_CFLAGS} -c $<

SHELL = /bin/sh
LIBTOOL = 
PURIFY = 

MKDEP = ${SHELL} ${top_builddir}/make/mkdep

cleandir: distclean

clean distclean::
	rm -f *.o *.lo *.la core *.core
	rm -rf .libs

distclean::
	rm -f Makefile

depend:
	@for i in ${ALL_SUBDIRS}; do \
		if [ "$$i" != "nulldir" -a -d $$i ]; then \
			echo "making depend in `pwd`/$$i"; \
			(cd $$i; ${MAKE} ${MAKEDEFS} $@) || exit 1; \
		fi \
	done
	@if [ X"${SRCS}" != X -a X"${PSRCS}" != X ] ; then \
		echo ${MKDEP} ${ALL_CPPFLAGS} ${SRCS}; \
		${MKDEP} ${ALL_CPPFLAGS} ${SRCS}; \
		echo ${MKDEP} -ap ${ALL_CPPFLAGS} ${PSRCS}; \
		${MKDEP} -ap ${ALL_CPPFLAGS} ${PSRCS}; \
		${DEPENDEXTRA} \
	elif [ X"${SRCS}" != X ] ; then \
		echo ${MKDEP} ${ALL_CPPFLAGS} ${SRCS}; \
		${MKDEP} ${ALL_CPPFLAGS} ${SRCS}; \
		${DEPENDEXTRA} \
	elif [ X"${PSRCS}" != X ] ; then \
		echo ${MKDEP} ${ALL_CPPFLAGS} ${PSRCS}; \
		${MKDEP} -p ${ALL_CPPFLAGS} ${PSRCS}; \
		${DEPENDEXTRA} \
	fi

FORCE:

###
### Libraries
###

AR =		/usr/bin/ar
ARFLAGS =	cruv
RANLIB =	ranlib

###
### Installation
###

INSTALL =		/usr/bin/install -c
INSTALL_PROGRAM =	${INSTALL}
INSTALL_DATA =		${INSTALL} -m 644

libbind.a: ${OBJS}
	${AR} ${ARFLAGS} $@ ${OBJS}
	${RANLIB} $@

libbind.la: ${OBJS}
	${LIBTOOL} --mode=link \
	${CC} ${ALL_CFLAGS} -o libbind.la -rpath ${libdir} \
		-version-info ${LIBINTERFACE}:${LIBREVISION}:${LIBAGE} \
		${OBJS} ${LIBS}

timestamp: libbind.a
	touch timestamp

installdirs:
	$(SHELL) ${top_srcdir}/mkinstalldirs ${DESTDIR}${libdir}

install:: timestamp installdirs
	${LIBTOOL} ${INSTALL_DATA} libbind.a ${DESTDIR}${libdir}


clean distclean::
	rm -f libbind.a libbind.la

distclean::
	rm -f make/rules make/includes make/mkdep

distclean::
	rm -f config.cache config.h config.log config.status libtool
	rm -f port_before.h port_after.h

man:
