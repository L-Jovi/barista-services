require('NSString, NSMutableString, NSNumber');
require('NSDictionary, NSMutableDictionary');
require('NSData, NSJSONSerialization, NSUserDefaults');
require('NSURL, NSURLConnection, NSURLRequest, NSMutableURLRequest');
require('NSNotificationCenter, NSInvocationOperation, NSOperationQueue');

var NSUTF8StringEncoding = 4;

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
        console.log('🍮  enter JSPatch logic [setAccount]');

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

        self.generateKey_catogery_debug(account, catogery, debug);
        utils['setter'](self, self.generateKey_catogery_debug(account, catogery, debug), '_key');
        utils['setter'](self, NSUserDefaults.standardUserDefaults(), '_userDefaults');

        utils['setter'](self, NSOperationQueue.alloc().init(), '_queue');
        utils['getter'](self, '_queue', 'default').setMaxConcurrentOperationCount(1);
        utils['setter'](self, 0, '_errorCount');

        if(!utils['getter'](self, '_userDefaults', 'default')){
            console.log("tyrantdb: NSUserDefaults is not avaliable, some information will be lost.");
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
        // pay attention to argument [data] type mapping [NSData]
        var _jsErrorCount = utils['getter'](self, '_errorCount', 'default');
        var jsApi = api.toJS();

        var jsonData = NSJSONSerialization.dataWithJSONObject_options_error(data, 0, null);
        if(jsonData){
            var jsonString = NSString.alloc().initWithData_encoding(jsonData, NSUTF8StringEncoding).stringByAddingPercentEscapesUsingEncoding(NSUTF8StringEncoding);
            var postString = jsonString.stringByAddingPercentEscapesUsingEncoding(NSUTF8StringEncoding).stringByReplacingOccurrencesOfString_withString('+', '%2B');
            var postData = postString.dataUsingEncoding(NSUTF8StringEncoding);
            var tyrantdbHost = self.tyrantdbHost();
            var urlString = NSMutableString.alloc().initWithFormat("%s%s", tyrantdbHost, api);
            var jsUrlString = urlString.toJS();

            var url = NSURL.alloc().initWithString(urlString);
            var request = NSMutableURLRequest.alloc().initWithURL_cachePolicy_timeoutInterval(url, NSURLRequestReloadIgnoringLocalCacheData, 5);
            request.setHTTPShouldHandleCookies(false);
            request.setHTTPBody(postData);
            request.setHTTPMethod("POST");
        }
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
        console.log('👉  version db 1.4.3');

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
