#!/bin/sh

version=$1

# replace current patch file name to older one
{
    cp demo.bak$version.js demo.js
} || {
    cp demo.bak.js demo.js
}

echo "js patch file will be replaced from your command ..\n"
echo "from [demo.bak$version.js] to [demo.js]\n"
say=`echo "replace finished, 👍  well done!"`

cowsay $say | lolcat
