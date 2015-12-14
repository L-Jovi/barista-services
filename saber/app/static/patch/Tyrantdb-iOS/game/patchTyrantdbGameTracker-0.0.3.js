require('NSString, NSMutableString, NSNumber, NSUTF8StringEncoding');
require('NSDictionary, NSMutableDictionary');
require('NSData, NSJSONSerialization, NSUserDefaults');
require('NSURL, NSURLConnection, NSURLRequest, NSMutableURLRequest');
require('NSNotificationCenter, NSInvocationOperation, NSOperationQueue');


var utils = {
    test_echo: function(){
        console.log('****** test utils method here ******');
    },
    isEmpty: function(map) {
        for(var key in map) {
            if (map.hasOwnProperty(key)) {
               return false;
            }
        }
        return true;
    },
    getObjCount: function(obj){
        return Object.keys(obj).length;
    },
    getter: function(obj, name, flag){
        rules = {
            'toJS': function(obj, name){
                return obj.valueForKey(name).toJS();
            },
            'default': function(){
                return obj.valueForKey(name);
            }
        }
        return rules[flag](obj, name);
    },
    // attention to that args order, [value] first and [name] second
    setter: function(obj, value, name){
        return obj.setValue_forKey(value, name);
    }
}


defineClass('Tyrantdb', {
    setAccount_module_catogery_debug: function(account, module, catogery, debug) {
        /* args mapping type below */
        var jsAccount = account.toJS();
        var jsModule = module.toJS();
        var jsCatogery = catogery.toJS();
        var jsDebug;
        if(debug){
            jsDebug = true;
        }else{
            jsDebug = false;
        }
        /* end args mapping */

        if(!jsAccount || !jsAccount.length){
            console.log("tyrantdb: Account is empty, need a nonempty string.");
            return false;
        }
        if(!jsCatogery || !jsCatogery.length){
            console.log("tyrantdb: Catogery is empty, need a nonempty string.");
            return false;
        }

        if(jsDebug){
            utils['setter'](self, 1, '_debug');
        }else{
            utils['setter'](self, 0, '_debug');
        }
        if(utils['getter'](self, '_debug', 'default')){
            utils['setter'](self, jsAccount + '-debug', '_index');
        }else{
            utils['setter'](self, jsAccount, '_index');
        }
        if(jsModule || jsModule.length){
            utils['setter'](self, jsModule, '_module');
        }

        return true;
    },

    event_setProperties_setIp_setTimestamp: function(name, properties, ip, timestamp) {
        var jsName = name.toJS();
        var jsProperties = properties.toJS();
        var jsIp = ip.toJS();
        var jsTimestamp = timestamp.toJS();

        var _jsIndex = utils['getter'](self, '_index', 'toJS');
        var _jsIdentify = utils['getter'](self, '_identify', 'toJS');

        if(!_jsIndex){
            console.log("tyrantdb: Haven't set account yet, please call setAccount first.");
            return false;
        }
        if(!_jsIdentify){
            console.log("tyrantdb: Haven't set identify yet, please call autoIdentify or identify first.");
            return false;
        }
        if(!jsName || !jsName.length){
            console.log("tyrantdb: Name is empty, will do nothing.");
            return false;
        }

        var data = {
            identify: _jsIdentify,
            index: _jsIndex,
            name: jsName
        }

        var _jsModule = utils['getter'](self, '_module', 'toJS');
        if(!utils['isEmpty'](jsProperties) && utils['getObjCount'](jsProperties)){
            data['properties'] = jsProperties;
        }
        if(jsIp && jsIp.length){
            data['ip'] = jsIp;
        }
        if(jsTimestamp && jsTimestamp.length){
            data['timestamp'] = jsTimestamp;
        }
        if(_jsModule){
            data['module'] = _jsModule;
        }

        self.sendTyrantdb_api(data, "event");

        return data;
    },

    sendTyrantdbJs_api: function(data, api) {
        // I use origin [data] with suitable oc type
        var _jsErrorCount = utils['getter'](self, '_errorCount', 'default');
        var jsApi = api.toJS();

        //   var jsonData = NSData.alloc().init();
        //   jsonData = NSJSONSerialization.dataWithJSONObject_options_error(data, 0, null);
        //   console.log(typeof jsonData, jsonData);
        //   if (null != jsonData) {
        //       console.log('@@@');
        //       var jsonString = NSString.alloc().initWithData_encoding(jsonData, NSUTF8StringEncoding);
        //       console.log('###');
        //       console.log(typeof tyrantdbHost, tyrantdbHost);

        //       var postString = jsonString.stringByAddingPercentEscapesUsingEncoding(NSUTF8StringEncoding).stringByReplacingOccurrencesOfString_withString("+", "%2B");
        //       var postData = postString.dataUsingEncoding(NSUTF8StringEncoding);

        //       // var urlString = NSMutableString.alloc().initWithFormat(tyrantdbHost, api);
        //       var urlString = NSMutableString.alloc();
        //       urlString = tyrantdbHost + api;
        //       console.log(typeof urlString, urlString);
        //       var url = NSURL.alloc().initWithString(urlString);

        //       var request = NSMutableURLRequest.alloc().initWithURL_cachePolicy_timeoutInterval(url, NSURLRequestReloadIgnoringLocalCacheData, 5);
        //       request.setHTTPShouldHandleCookies(NO);
        //       request.setHTTPBody(postData);
        //       request.setHTTPMethod("POST");

        //       var sendInfo = NSMutableDictionary.alloc().initWithCapacity(1);
        //       sendInfo.setObject_forKey(request, "request");

        //       return sendInfo;
        //   }else{
        //       NSLog("%", "tyrantdb: JSON encode error.");
        //       return 0;
        //   }
    },

    identify_setProperties_setIp_setTimestamp: function(identify, properties, ip, timestamp) {
        var jsIdentify = identify.toJS();
        var jsProperties = properties.toJS();
        var jsIp = ip.toJS();
        var jsTimestamp = timestamp.toJS();
        var _jsIndex = utils['getter'](self, '_index', 'toJS');
        var _jsIdentify = utils['getter'](self, '_identify', 'toJS');
        
        if(!_jsIndex){
            console.log("tyrantdb: Haven't set account yet, please call setAccount first.");
            return false;
        }
        if((!jsIdentify || !jsIdentify.length) && utils['isEmpty'](jsProperties) || !utils['getObjCount'](jsProperties)){
            console.log("tyrantdb: Identify and properties are both empty, will do nothing.");
            return false;
        }
        if((!jsIdentify || !jsIdentify.length) && !_jsIdentify){
            console.log("tyrantdb: Haven't set identify yet, please specify an identify first.");
            return false;
        }

        if(jsIdentify && jsIdentify.length){
            if(jsIdentify == _jsIdentify){
                if(utils['isEmpty'](jsProperties) || !utils['getObjCount'](jsProperties)){
                    return false;
                }
            }else{
                _jsIdentify = jsIdentify;
                utils['setter'](self, _jsIdentify, '_identify');

                var _jsUserDefaults = NSUserDefaults.alloc().init();
                _jsUserDefaults = utils['getter'](self, '_userDefaults', 'default');
                var _jsKey = utils['getter'](self, '_key', 'toJS');

                if(_jsUserDefaults){
                    _jsUserDefaults.setObject_forKey(_jsIdentify, _jsKey);
                    _jsUserDefaults.synchronize();
                }
                self.saveSSKeychainWithValue_key(_jsIdentify, _jsKey);
            }
        }

        _jsIdentify = utils['getter'](self, '_identify', 'toJS');
        var data = NSMutableDictionary.alloc().init();
        data.setObject_forKey(_jsIdentify, 'identify');
        data.setObject_forKey(_jsIndex, 'index');

        if(!utils['isEmpty'](jsProperties) && utils['getObjCount'](jsProperties)){
            data.setObject_forKey(jsProperties, 'properties');
        }
        if(jsIp && jsIp.length){
            data.setObject_forKey(jsIp, 'ip');
        }
        if(jsTimestamp && jsTimestamp.length){
            data.setObject_forKey(jsTimestamp, 'timestamp');
        }

        var _jsModule = utils['getter'](self, '_module', 'toJS');
        if(_jsModule){
            data.setObject_forKey(_jsModule, 'module');
        }

        return data;
    },

    blockedSend: function(sendInfo) {
        // in view of aiming at oc type [NSMutableURLRequest] make no sense with [toJS()]
        // here I retain origin variable
        if (!sendInfo || !sendInfo.isKindOfClass(NSDictionary.class())) {
            console.log("tyrantdb: Non NSDictionary object given to send, will do nothing.");
            return false;
        }

        var info = sendInfo;
        var request = info.objectForKey('request');
        if(!request){
            console.log('tyrantdb: Invalid send info given to send, will do nothing.');
            return false;
        }

        var data = null;
        for (var i = 0; i < 3; i++) {
            data = NSURLConnection.sendSynchronousRequest_returningResponse_error(request, null, null);

            if (data) {
                break;
            }
        }

        return true;
    }
});


defineClass('TyrantdbGameTracker', {}, {
    testQueueJs_channel_debug_delegate: function(appId, channel, debug, delegate) {
        /* set _queue */
        _queue = NSOperationQueue.alloc().init();
        _queue.setMaxConcurrentOperationCount(1);
        _queue.addOperation(NSInvocationOperation.alloc().initWithTarget_selector_object(delegate, 'onStartOperation', null));

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object(delegate, "enterBackgroundOperation", "UIApplicationDidEnterBackgroundNotification", null);
        
        console.log('👉  version 0.0.3 👈  ');
    },

    setUserJs_userType_userSex_userAge_userName: function(userId, userType, userSex, userAge, userName) {
        return {};
    },

    setLevel: function(level) {
        var _jsTyrantdbUser = TyrantdbGameTracker.__tyrantdbUser();
        return;
    }
});
