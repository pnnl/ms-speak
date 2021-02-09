
pkglib_LTLIBRARIES=srv_msp.la

AM_CPPFLAGS=-I$(top_srcdir)/ -I$(top_srcdir)/include/ -I$(top_builddir)/include/ -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -I/usr/include/libxml2

srv_msp_la_LIBADD = @MODULES_LIBADD@ -lglib-2.0 -luuid -lxml2
srv_msp_la_CFLAGS=  @MODULES_CFLAGS@
srv_msp_la_LDFLAGS= -module -avoid-version
srv_msp_la_SOURCES = srv_msp.c srv_msp_body.c


EXTRA_DIST= makefile.w32 srv_msp.def srv_msp_body.h
