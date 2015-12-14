#!/bin/bash

orig_version=$1
cur_version=$2

if [[ -z $orig_version && -z $cur_version ]]
then
    echo "arguments [orig_versio] and [cur_versio] not all exists."
else
    sed -i .bak 's/"0.0.'$orig_version'"/"0.0.'$cur_version'"/g' patch.json
    echo success replace version from [ 0.0.$orig_version ]\
        to [ 0.0.$cur_version ],  well done! | lolcat
fi
