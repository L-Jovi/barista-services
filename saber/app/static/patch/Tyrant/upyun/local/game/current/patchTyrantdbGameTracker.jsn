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
    testJSPatchQueue_channel_debug_delegate: function(appId, channel, debug, delegate) {
        /* set _queue */
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object(delegate, "enterBackgroundOperation", "UIApplicationDidEnterBackgroundNotification", null);
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object(delegate, "becomeActiveOperation", "UIApplicationDidBecomeActiveNotification", null);
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object(delegate, "willTerminateOperation", "UIApplicationWillTerminateNotification", null);

        _queue = NSOperationQueue.alloc().init();
        _queue.setMaxConcurrentOperationCount(1);
        _queue.addOperation(NSInvocationOperation.alloc().initWithTarget_selector_object(delegate, 'onStartOperation', null));
        
        console.log('🍮  version game 1.4.1 - [testQueue]');
    },

    testJSPatchSetUser_userType_userSex_userAge_userName: function(userId, userType, userSex, userAge, userName) {
        return;
    },

    testJSPatchSetLevel: function(level) {
        var _jsTyrantdbUser = TyrantdbGameTracker.getTyrantdbUser();
        return;
    }
});
