from animations.fur import fur
from animations.seizure import seizure 
from animations.kanye import kanye
from animations.dos import dos
from animations.worm import worm
from animations.rain import rain
from animations.cylon import cylon
from animations.diags import diags
from animations.emotes import emotes

## Generate a list of all animation classes
import sys
def all():
    results = []
    module = sys.modules['animations']
    for name in dir(module):
        x = getattr(module, name)
        if isinstance(x, type) and name[:2] != "__":
            results.append(x)
    return results

## Select a random animation
import random
def rand():
    results = all()
    return results[random.randint(0, len(results)-1)]
