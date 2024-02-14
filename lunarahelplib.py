# made this library to help devs program lunara

class LunaraHelpLib():
    def isanint(self, thing):
        try:
            int(thing)
            return True
        except:
            return False