""" BLS signature scheme """
from bplib.bp import BpGroup, G2Elem
from .utils import *


def setup(q=1):
	""" generate all public parameters """
	assert q > 0
	G = BpGroup()
	(g1, g2) = G.gen1(), G.gen2()
	(e, o) = G.pair, G.order()
	return (G, o, g1, g2, e)


def ttp_keygen(params, t, n, q):
	""" generate keys for threshold signature (executed by a TTP) """
	assert n >= t and t > 0 and q > 0
	(G, o, g1, hs, g2, e) = params
	# generate polynomials
	v = [o.random() for _ in range(0,t)]
	w = [[o.random() for _ in range(0,t)] for __ in range(q)]
	# generate shares
	x = [poly_eval(v,i) % o for i in range(1,n+1)]
	y = [[poly_eval(wj,i) % o for wj in w] for i in range(1,n+1)]
	# set keys
	sk = list(zip(x, y))
	vk = [(g2, x[i]*g2, [y[i][j]*g2 for j in range(len(y[i]))]) for i in range(len(sk))]
	return (sk, vk)


def aggregate_vk(params, vk, threshold=True):
	""" aggregate the verification keys """
	(G, o, g1, hs, g2, e) = params
	(_, alpha, beta) = zip(*vk)
	t = len(vk)
	q = len(beta[0])
	# evaluate all lagrange basis polynomial li(0)
	l = [lagrange_basis(t, o, i, 0) for i in range(1,t+1)] if threshold else [1 for _ in range(t)]
	# aggregate keys
	aggr_alpha = ec_sum([l[i]*alpha[i] for i in range(t)])
	aggr_beta = [ec_sum([l[i]*beta[i][j] for i in range(t)]) for j in range(q)]
	return (g2, aggr_alpha, aggr_beta)


def sign(params, sk, m):
	""" sign attributes """
	assert len(m) > 0
	(G, o, g1, hs, g2, e) = params
	(x, y) = sk
	
	# TODO


def aggregate_sigma(params, sigs, threshold=True):
	""" aggregate partial credentials """
	(G, o, g1, hs, g2, e) = params
	t = len(sigs)
	# evaluate all lagrange basis polynomial li(0)
	l = [lagrange_basis(t, o, i, 0) for i in range(1,t+1)] if threshold else [1 for _ in range(t)]
	# aggregate sigature
	(h, s) = zip(*sigs)
	aggr_s = ec_sum([l[i]*s[i] for i in range(t)])
	return (h[0], aggr_s)



def verify(params, aggr_vk, sigma, public_m):
	""" verify credentials """
	(G, o, g1, h1, g2, e) = params
	(g2, _, beta) = aggr_vk
	(h, s) = sigma
	
	# TODO


