/* config.h.  Generated automatically by configure.  */
/* config.h.in.  Generated automatically from configure.in by autoheader.  */
/*
 * Copyright (C) 1999-2001  Internet Software Consortium.
 *
 * Permission to use, copy, modify, and distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND INTERNET SOFTWARE CONSORTIUM
 * DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
 * INTERNET SOFTWARE CONSORTIUM BE LIABLE FOR ANY SPECIAL, DIRECT,
 * INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
 * FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
 * NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
 * WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

/* $Id: config.h.in,v 1.47.2.1 2001/10/22 23:28:08 gson Exp $ */

/***
 *** This file is not to be included by any public header files, because
 *** it does not get installed.
 ***/

/* Define to empty if the keyword does not work.  */
/* #undef const */

/* Define as __inline if that's what the C compiler calls it.  */
#define inline 

/* Define to `unsigned' if <sys/types.h> doesn't define.  */
/* #undef size_t */

/* Define if you have the ANSI C header files.  */
#define STDC_HEADERS 1

/* Define if you can safely include both <sys/time.h> and <time.h>.  */
#define TIME_WITH_SYS_TIME 1

/* Define if your processor stores words with the most significant
   byte first (like Motorola and SPARC, unlike Intel and VAX).  */
/* #undef WORDS_BIGENDIAN */

/* define to `int' if <sys/types.h> doesn't define.  */
/* #undef ssize_t */

/* define on DEC OSF to enable 4.4BSD style sa_len support */
/* #undef _SOCKADDR_LEN */

/* define if your system needs pthread_init() before using pthreads */
/* #undef NEED_PTHREAD_INIT */

/* define if your system has sigwait() */
/* #undef HAVE_SIGWAIT */

/* define if sigwait() is the UnixWare flavor */
/* #undef HAVE_UNIXWARE_SIGWAIT */

/* define on Solaris to get sigwait() to work using pthreads semantics */
/* #undef _POSIX_PTHREAD_SEMANTICS */

/* define if LinuxThreads is in use */
/* #undef HAVE_LINUXTHREADS */

/* define if sysconf() is available */
/* #undef HAVE_SYSCONF */

/* define if sysctlbyname() is available */
/* #undef HAVE_SYSCTLBYNAME */

/* define if catgets() is available */
#define HAVE_CATGETS 1

/* define if you have the NET_RT_IFLIST sysctl variable. */
/* #undef HAVE_IFLIST_SYSCTL */

/* define if chroot() is available */
#define HAVE_CHROOT 1

/* define if struct addrinfo exists */
#define HAVE_ADDRINFO 1

/* define if getaddrinfo() exists */
#define HAVE_GETADDRINFO 1

/* define if gai_strerror() exists */
#define HAVE_GAISTRERROR 1

/* define if pthread_setconcurrency() should be called to tell the
 * OS how many threads we might want to run.
 */
/* #undef CALL_PTHREAD_SETCONCURRENCY */

/* define if IPv6 is not disabled */
#define WANT_IPV6 1

/* define if flockfile() is available */
#define HAVE_FLOCKFILE 1

/* define if getc_unlocked() is available */
#define HAVE_GETCUNLOCKED 1

/* Shut up warnings about sputaux in stdio.h on BSD/OS pre-4.1 */
/* #undef SHUTUP_SPUTAUX */
#ifdef SHUTUP_SPUTAUX
struct __sFILE;
extern __inline int __sputaux(int _c, struct __sFILE *_p);
#endif

/* Shut up warnings about missing sigwait prototype on BSD/OS 4.0* */
/* #undef SHUTUP_SIGWAIT */
#ifdef SHUTUP_SIGWAIT
int sigwait(const unsigned int *set, int *sig);
#endif

/* Shut up warnings from gcc -Wcast-qual on BSD/OS 4.1. */
/* #undef SHUTUP_STDARG_CAST */
#if defined(SHUTUP_STDARG_CAST) && defined(__GNUC__)
#include <stdarg.h>  /* Grr.  Must be included *every time*. */
/*
 * The silly continuation line is to keep configure from
 * commenting out the #undef.
 */
#undef \
 va_start
#define va_start(ap, last) \
 do { \
  union { const void *konst; long *var; } _u; \
  _u.konst = &(last); \
  ap = (va_list)(_u.var + __va_words(__typeof(last))); \
 } while (0)
#endif /* SHUTUP_STDARG_CAST && __GNUC__ */

/* define if the system has a random number generating device */
#define PATH_RANDOMDEV "/dev/random"

/* define if pthread_attr_getstacksize() is available */
/* #undef HAVE_PTHREAD_ATTR_GETSTACKSIZE */

/* define if you have strerror in the C library. */
#define HAVE_STRERROR 1

/* Define if you have the <dlfcn.h> header file.  */
/* #undef HAVE_DLFCN_H */

/* Define if you have the <fcntl.h> header file.  */
#define HAVE_FCNTL_H 1

/* Define if you have the <linux/capability.h> header file.  */
/* #undef HAVE_LINUX_CAPABILITY_H */

/* Define if you have the <sys/prctl.h> header file.  */
/* #undef HAVE_SYS_PRCTL_H */

/* Define if you have the <sys/select.h> header file.  */
#define HAVE_SYS_SELECT_H 1

/* Define if you have the <sys/sockio.h> header file.  */
/* #undef HAVE_SYS_SOCKIO_H */

/* Define if you have the <sys/sysctl.h> header file.  */
/* #undef HAVE_SYS_SYSCTL_H */

/* Define if you have the <sys/time.h> header file.  */
#define HAVE_SYS_TIME_H 1

/* Define if you have the <unistd.h> header file.  */
#define HAVE_UNISTD_H 1

/* Define if you have the nsl library (-lnsl).  */
/* #undef HAVE_LIBNSL */

/* Define if you have the pthread library (-lpthread).  */
/* #undef HAVE_LIBPTHREAD */

/* Define if you have the socket library (-lsocket).  */
/* #undef HAVE_LIBSOCKET */
