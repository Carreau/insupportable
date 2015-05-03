# -*- coding: utf-8 -*-

import sys
from  warnings import warn 


class Dum(object):
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name

PY3 = Dum('PY3')
PY2 = Dum('PY2') 

PY3 = 'PY3'
PY2 = 'PY2'


_PY2=PY2
_PY3=PY3

# featuresets = (name, support, predicate)

predicates = {
 PY2:(sys.version_info.major == 2),
 PY3:(sys.version_info.major == 3),
}

pyxy = {}

for i in range(7):
    pystr = 'PY3'+str(i)
    predicates[pystr] = (sys.version_info == (3,i))
    predicates[pystr+'+'] = (sys.version_info >= (3,i))
    pyxy[pystr]=True
    pyxy[pystr+'+']=False



#support.config

class S(object):

    def __init__(self, PY2=True, PY3=True, config=() ):
        self.PY3_supported = PY2
        self.PY2_supported = PY3
        self.level=2
        self.featuresets = [
                { _PY2:PY2,
                  _PY3:PY3
        }]
        self.featuresets.append(pyxy)
        self.featuresets.extend(config)


        self.know_keys = []
        for feat in self.featuresets : 
            self.know_keys.extend(feat.keys())

        self.know_keys=set(self.know_keys)

    def _known_version(self, version):
        return (version in self.know_keys)

    def _alone_version(self, version):
        for fset in self.featuresets:
            if version in fset: 
                return len([v for k,v in fset.items() if v])==1


    def _get_featureset_support(self, version): 
        for fset in self.featuresets:
            if version in fset: 
                return fset[version]
        return False

        


    def support(self, version): 
        """
        return `True` if current python version match version passed. 
        
        raise a deprecation warning if only PY2 or PY3 is supported as you probably
        have a conditional that should be removed. 

        """

        if not self._known_version(version):
            warn("unknown feature: %s"%version)
            return True
        else:
            if not self._get_featureset_support(version):
                warn("You are not supporting %s anymore "%str(version), UserWarning, self.level)
            if self._alone_version(version):
                warn("%s is the last supported feature of this group, you can simplifiy this logic. "%str(version), UserWarning,self.level)
                
            return predicates.get(version, True)




        if (not self.PY3_supported) or (not self.PY2_supported):
            warn("You are only supporting 1 version of Python", UserWarning, self.level)

        if version == PY3:
            return sys.version_info.major == 3
        elif version == PY2:
            return sys.version_info.major == 2


class CFunction(object):

    def __init__(self, name, *args,**kwargs):
        self.s = S(*args, **kwargs)
        self.name = name

    def __call__(self, *args,**kwargs):
        sub = getattr(self.s, self.name) 
        return sub(*args, **kwargs)

    def config(self, *args, **kwargs):
        self.s = S(*args, **kwargs)
        self.s.level = 3


support = CFunction('support')
