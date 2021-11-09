class OutOfRange(Exception):
    def __init__(self,*args):
        if args:
             self.message = args[0]
        else:
            self.message = "Untracked errror with data"

    def __str__(self):
        print('calling str')
        if self.message:
            return 'Invalid data input: {0}'.format(self.message)

def IsValid(mask):
    is_zero = False

    for i in range(0,4):

        if mask[i]==255:
            continue

        if is_zero and mask[i] !=0:
           raise OutOfRange("Incorrect form of mask") 
        elif is_zero:
            continue
        octate = 255
        for n in range(0,6):

            if mask[i] == octate - 2**n or mask[i]==0: 
               is_zero = True
               break
        if is_zero:
            continue
        raise OutOfRange("Incorrect form of mask")