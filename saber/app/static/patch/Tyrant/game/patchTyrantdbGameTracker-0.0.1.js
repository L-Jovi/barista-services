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


defineClass('TyrantdbGameTracker', {}, {
    testQueueJs_channel_debug_delegate: function(appId, channel, debug, delegate) {
        /* set _queue */
        _queue = NSOperationQueue.alloc().init();
        _queue.setMaxConcurrentOperationCount(1);
        _queue.addOperation(NSInvocationOperation.alloc().initWithTarget_selector_object(delegate, 'onStartOperation', null));

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object(delegate, "enterBackgroundOperation", "UIApplicationDidEnterBackgroundNotification", null);
        
        console.log('👉  version game 0.0.1');
    },

    setUserJs_userType_userSex_userAge_userName: function(userId, userType, userSex, userAge, userName) {
        return {};
    },

    setLevel: function(level) {
        var _jsTyrantdbUser = TyrantdbGameTracker.__tyrantdbUser();
        return;
    }
});
