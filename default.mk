# This file is part of the asdicts.
#
# Copyright (c) 2021 Serghei Iakovlev
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

# Run “make build” by default
.DEFAULT_GOAL = build

ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
PKG_NAME = asdicts

ifneq (,$(findstring xterm,${TERM}))
	GREEN := $(shell tput -Txterm setaf 2)
	RESET := $(shell tput -Txterm sgr0)
	CS = "${GREEN}~~~ "
	CE = " ~~~${RESET}"
else
	CS = "~~~ "
	CE = " ~~~"
endif

COV          =
HEADER_EXTRA =

REQUIREMENTS     = requirements.txt
REQUIREMENTS_DEV = requirements-dev.txt

PYTEST_FLAGS ?= --color=yes -v
FLAKE8_FLAGS ?= --show-source --statistics

VENV_ROOT = .venv

# PYTHON will used to create venv
ifeq ($(OS),Windows_NT)
	PYTHON  ?= python
	VENV_BIN = $(VENV_ROOT)/Scripts
else
	PYTHON  ?= python3
	VENV_BIN = $(VENV_ROOT)/bin
endif

VENV_PIP    = $(VENV_BIN)/pip
VENV_PYTHON = $(VENV_BIN)/python

# Program availability
ifndef PYTHON
$(error "Python is not available please install Python")
else
ifneq ($(OS),Windows_NT)
HAVE_PYTHON := $(shell sh -c "command -v $(PYTHON)")
ifndef HAVE_PYTHON
$(error "Python is not available please install Python")
endif
endif
endif
