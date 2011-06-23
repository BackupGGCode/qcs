import qcs

_D_LEVEL = 3;

#
# |psi_{p,q}> = X^q_d(1) H(0)_d Z^p_d(0) CNOT_d(0,1) |00>
#
def make_psi(_r,p,q):
	_r.Reset()
	for i in range(0,q):
		_r.NotN(1)
	_r.HadN(0)
	for i in range(0,p):
		_r.PauliZ(0) 
	_r.CNot(0,1)	
	
def detect_bell_state( _r ):
	_r.HadN(2)
	_r.CNot(2,0)
	_r.CNot(2,1)
	_r.HadN_Conj(2) 
	#print "a1 measure"
	#_r.Pr()
	#print "a1 measure cleanup"
	#_r.Cleanup()
	#_r.Pr()
	a1=_r.MeasureOneQudit( 2 )
	#print "a1=", a1
	_r.CNot_Conj(0,3)  
	_r.CNot(1,3)
	#print "a2 measure
	#_r.Pr()
	#print "a2 measure cleanup"
	#_r.Cleanup()
	#_r.Pr()
	a2=_r.MeasureOneQudit(3)
	#print "a2=", a2
	return a1,a2

r=qcs.QuantumReg( 4, _D_LEVEL )
r.Reset()

make_psi(r,2,0)
print("d-level psi state")
r.Pr()

a1,a2=detect_bell_state(r)
print()
print("a1="+str(a1)+ " a2="+str(a2))
print()
r.Pr()


