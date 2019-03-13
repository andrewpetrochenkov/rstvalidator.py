#!/usr/bin/env bash
{ set +x; } 2>/dev/null

path="${BASH_SOURCE[0]%/*}"/error.rst
( set -x; python -m rstvalidator "$path" )
[[ $? != 0 ]]
