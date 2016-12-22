
import re

class B():
    def __init__(self,cls,**params):
        self.args=params
        self.cls=cls
        
    def p(self):
        print(self.args)
        print(*self.args)
        #print(**self.args)
        self.c=self.cls(**self.args)
        self.c.p()
        
    def show(self):
        print(dict(self.args).keys())
        
    # seperate args into smote_enn and classifier
    def get_smote_enn_and_classifier_args(self):
        smote_enn_args={}
        classifier_args={}
        for key in dict(self.args).keys():
            if re.search('smote$|enn$', key):
                smote_enn_args[key]=self.args[key]
            else:
                classifier_args[key]=self.args[key]
        return smote_enn_args, classifier_args

class C():
    def __init__(self, **params):
        self.args=params
    def p(self):
        print(self.args)

        
#c=C(key='fisrt',another=100)
#c.p()

b=B(C,key_smote='fisrt',another_enn=100,weight=0.85,smote_abc=15)
# b.p()

l=b.args
d=B(C,**l)
#d.p()
d.show()
sv, ov = d.get_smote_enn_and_classifier_args()
e=B(C,**sv)
e.show()
