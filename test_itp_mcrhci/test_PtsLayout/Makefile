#-------------------------------------------------------------------------------
# Makefile - procedures/thriver/test_archiver
#
# Copyright (C) Massachusetts General Hospital (MGH)
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# The target ...

ifneq ($(APP), unittest)
    override APP = integration
endif

all: test

#-------------------------------------------------------------------------------
# Code documentation generation

DOCGEN = sphinx

#-------------------------------------------------------------------------------
# Common include for APP modules

include $(TCS_MAKEDIR)/make.integration

#-------------------------------------------------------------------------------
# clean and clobber etc.

CLOBBER += *.pyc      \
	       *.log      \
           index.html \
           xml_report

include $(TCS_MAKEDIR)/make.tidy
