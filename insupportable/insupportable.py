# -*- coding: utf-8 -*-

import sys
from  warnings import warn 


PY3 = 'PY3'
PY2 = 'PY2'


_PY2=PY2
_PY3=PY3

# featuresets = (name, support, predicate)


feature_mapping = dict()


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

class Feature(object):
    """
    A feature/option/patch...etc that might be dropped at some point in the future. 

    """

    def __init__(self, name, predicate):
        self.name = name
        self.predicate = predicate


class DiscreatFeature(Feature):
    pass

class VersionnedFeature(Feature):
    
    def __init__(self, name, predicate):
        super().__init__(name, predicate)


class FeatureGroup(object):

    def __init__(self, *args):
        self.features = args


#class FeatureTracker(object):
#
#    def __init__(self, *args):
#        self.args = args
#
#        self._known_versions = [f.name for g in args for f in g.features]
#
#
#    def support(indetifier):
#        pass





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


        self.known_keys = []
        for feat in self.featuresets : 
            self.known_keys.extend(feat.keys())

        self.known_keys=set(self.known_keys)

        import copy
        self.predicates = copy.copy(predicates)

    def add_feature(self, name, predicate, supported=True):
        if callable(predicate):
            predicate = predicate()
        self.predicates['name'] = predicate
        self.known_keys.add(name)
        self.featuresets.append({name:supported})

    def _known_version(self, version):
        return (version in self.known_keys)

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
                
            return self.predicates.get(version, True)




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
