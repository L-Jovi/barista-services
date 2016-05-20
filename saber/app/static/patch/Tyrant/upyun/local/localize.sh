#!/bin/bash

cp db/stable/patchTyrantdb.js db/current/patchTyrantdb.js
sed -in 's/1.4.1/1.4.2/g' db/current/patchTyrantdb.js
cp db/stable/patchTyrantdb.js db/edge/patchTyrantdb.js
sed -in 's/1.4.1/1.4.3/g' db/edge/patchTyrantdb.js

cp game/stable/patchTyrantdbGameTracker.js game/current/patchTyrantdbGameTracker.js
sed -in 's/1.4.1/1.4.2/g' game/current/patchTyrantdbGameTracker.js
cp game/stable/patchTyrantdbGameTracker.js game/edge/patchTyrantdbGameTracker.js
sed -in 's/1.4.1/1.4.3/g' game/edge/patchTyrantdbGameTracker.js
