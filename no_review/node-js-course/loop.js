// start

const pendingTimers = [];
const pendingOSTasks = [];
const pendingOperations = [];

// new timers, tasks, operations are recorded from myFile running
myFile.runContents();

function shouldContinue() {
    // check one: any pending setTimeout, setInterval or setImmediate?
    // check two: eny pending OS tasks? (like server listening to port)
    // check three: any pending long running operations? (like fs modules)
    return pendingTimers.length || pendingOSTasks.length || pendingOperations.length;
}

// entire body executes in one 'tick'
while(shouldContinue()) {
    // 1) node looks at pendingTimers and sees if any functions are ready to be called
    // (setTimeout, setInterval)

    // 2) node looks at pendingOSTasks and pendingOperations and calls relevant callbacks

    // 3) pause execution. continue when..
    //  - new pending pendingOSTask is done
    //  - new pending pendingOperation is done
    //  - timer is about to complete

    // 4) look at pendingTimers. call any setImmediate
    // handle any 'close' events
}

// end