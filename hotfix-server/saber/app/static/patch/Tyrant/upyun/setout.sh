#!/bin/bash

DB_JSNAME="patchTyrantdb.js"
GAME_JSNAME="patchTyrantdbGameTracker.js"

ORIG_DB_PATH="./local/db/stable/$DB_JSNAME"
ORIG_GAME_PATH="./local/game/stable/$GAME_JSNAME"
TARGET_DB_PATH="./cloud/db/$DB_JSNAME"
TARGET_GAME_PATH="./cloud/game/$GAME_JSNAME"

UPLOAD_DB_URL="http://v0.api.upyun.com/tyrantdb-sdk/db/1.4.1/patch/rc1/$DB_JSNAME"
UPLOAD_GAME_URL="http://v0.api.upyun.com/tyrantdb-sdk/game/1.4.1/patch/rc1/$GAME_JSNAME"
UPYUN_DB_URL=`cat ./cloud/db/revision.json | jq .remotePatchSrcBaseUrl | sed "s/\"//g"`
UPYUN_GAME_URL=`cat ./cloud/game/revision.json | jq .remotePatchSrcBaseUrl | sed "s/\"//g"`


function action_cp(){
    if [[ -f $1 ]]
    then
        read -p "👉  find target file [ $1 ], continue?    Y/n" confirm
        if [[ $confirm == "" ]] || [[ $confirm == "y" ]] || [[ $confirm == "Y" ]]
        then
            cp $1 $2
            echo "exec cp action from [ $1 ] to [ $2 ] done." | lolcat
        else
            echo 'abort.'
        fi
    else
        echo "target [ $1 ] not find, abort."
    fi
}

function action_upload(){
    echo "👉  finish all js resource cp, prepare upload [ $1 ] now."
    read -p "continue?    Y/n" confirm
    if [[ $confirm == "" ]] || [[ $confirm == "y" ]] || [[ $confirm == "Y" ]]
    then
        curl -XPUT $1 -H "Authorization: Basic dHlyYW50ZGI6TDl0azRZUnhxOEVkaGlCSw==" -T $2
        echo "send PUT upload to [ $1 ] done." | lolcat
    else
        echo 'abort.'
    fi
}

function action_get(){
    read -p "👉  want to have look for remote [ $1 ]?    Y/n" confirm
    if [[ $confirm == "" ]] || [[ $confirm == "y" ]] || [[ $confirm == "Y" ]]
    then
        http GET $1
    else
        echo 'abort.'
    fi
}


action_cp $ORIG_DB_PATH $TARGET_DB_PATH
action_cp $ORIG_GAME_PATH $TARGET_GAME_PATH

action_upload $UPLOAD_DB_URL $TARGET_DB_PATH
action_upload $UPLOAD_GAME_URL $TARGET_GAME_PATH

action_get $UPYUN_DB_URL
action_get $UPYUN_GAME_URL
