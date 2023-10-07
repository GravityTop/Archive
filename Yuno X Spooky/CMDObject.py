
class CMDObj:
    name = None    # main tag / name  ([help] admin)
    alias = [] # other names      ([?] admin)
    function = None# pointer to specified function calls
    
    min_argc = 0
    max_argc = 0
    
    def __init__(self):
        return
        
    def setup(self, name, function):
        self.name = name
        self.function = function
        return self
        
    def set_argc(self, min, max):
        self.min_argc = min
        self.max_argc = max
        return self

    def addAlias(self, name):
        self.alias.append(name)
        return self
        
    def matches(self, othername):
        if self.name == othername: 
            return 1
        else:
            for str in self.alias:
                if othername == str:
                    return 1
            return 0
            
    async def execute(self, message, cmd, args, buf):
        if len(args) >= self.min_argc and len(args) <= self.max_argc:
            await self.function(message, cmd, args, buf)
        else:  
            await print("Invalid arg count... MIN "+self.min_argc+" MAX" +self.max_argc)
        return

class CMDHdl:
    message = None
    cmdobjs = []
    origBuffer = None
    strippedBuffer = None
    args = []
    cmd = None# set to args[0]
    

    def _setup(self, buffer):
        self.args = buffer.split(" ")
        self.cmd = self.args[0]
        return

    def __init__(self, cmdlist, message):
        self.message = message
        self.cmdobjs = cmdlist
        self.origBuffer = message.content
        self.strippedBuffer = self.origBuffer.strip("\r").strip("\n")
        self._setup(self.strippedBuffer)
        return
    
    async def process(self):
        if self.cmdobjs is not None:
            for cmdobj in self.cmdobjs:
                if cmdobj.matches(self.cmd) == 1:
                    print("Executing CMD "+self.strippedBuffer)
                    await cmdobj.execute(self.message, self.cmd, self.args, self.strippedBuffer)
                    return
                continue
            #print("Cmd "+self.cmd+" not found!")
            return
        print("No registered commands!")
        return
