#!/bin/bash

echo
echo

find ../ -name \*.tar.gz | grep -v updatePackages | sort

echo
echo
echo "beta or alpha versions: "
find ../ -name \*.tar.gz | grep -E "alpha|beta|-rc" | sort
