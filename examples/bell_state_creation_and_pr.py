import qcs

def make_psi_plus(_r):
    _r.SetKet("00")
    _r.HadN(0)
    _r.CNot(0,1)
    
def make_psi_minus(_r):
    _r.SetKet("10")
    _r.HadN(0)
    _r.CNot(0,1)

def make_phi_plus(_r):
    _r.SetKet("10")
    _r.HadN(1)
    _r.CNot(1,0)
    
def make_phi_minus(_r):
    _r.SetKet("11")
    _r.HadN(0)
    _r.CNot(0,1)

r=qcs.QuantumReg(2)
r.Reset()

make_psi_plus(r)
print "psi+"
r.Pr()

make_psi_minus(r)
print "psi-"
r.Pr()

make_phi_plus(r)
print "phi+"
r.Pr()

make_phi_minus(r)
print "phi-"
r.Pr()


