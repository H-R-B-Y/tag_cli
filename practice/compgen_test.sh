#!/usr/bin/bash

_zaso()
{
    local dir="$(pwd)"

    pushd "$dir" >/dev/null
    find * -maxdepth 0 2>/dev/null
    popd >/dev/null
}

_comp_with_find()
{
    local cur dir      
    local IFS=$'\n'

    cur="$1"
    dir="$2"

    compopt -o filenames 2>/dev/null
    COMPREPLY=( $( compgen -W "$(python3 ./compgen_predefined.py)" -- "$cur" ) );
	echo "${COMP_WORDS[COMP_CWORD]}" >> ~/Documents/COMP
}

function tagTest() {
	echo "$1"
	echo "$2"
}

complete -F _comp_with_find tagTest