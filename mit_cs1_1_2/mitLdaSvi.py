# class mitLdaSvi
#
# variant of Matthew Hoffman's onlinedavb
#
# Arguments:
# K: Number of topics
# vocab: A set of words to recognize. When analyzing documents, any word
#         not in this set will be ignored.
# D: Total number of documents in the population.For a fixed corpus,
#     this is the size of the corpus.In the truly online setting, this
#     can be an estimate of the maximum number of documents that could
#     ever be seen.
# alpha: Hyperparameter for prior on weight vectors theta
# eta: Hyperparameter for prior on topics beta
# tau0: A(positive) learning parameter that downweights early iterations
# kappa: Learning rate: exponential decay rate - --should be between
#     (0.5, 1.0] to guarantee asymptotic convergence.
#
# Note that if you pass the same set of D documents in every time and
#     set kappa = 0 this  class can also be used to do batch VB.
import numpy

class mitLdaSvi:

    def __init__(self,vocab,K,D,alpha,eta,tau,kappa,docs,iterations):
        self._vocab = vocab
        self._V = len(vocab)
        self._K = K
        self._D = D
        self._alpha = alpha
        self._eta = eta
        self._tau = tau
        self._kappa = kappa
        self._lambda = 1*n.random.gamma(100.,1./100.,(self_K,self._V))
        self._Elogbeta = dirichlet_expectation(self._lambda)
        self._expElogbeta = numpy.exp(self_Elogbeta)
        self.ct = 0
        self._iterations = iterations

    def dirichlet_expectation(alpha):
        if(len(alpha.shape)==1):
            return(psi(alpha)-psi(numpy.sum(alpha)))
        return(psi(alpha)-psi(numpy.sum(alpha,1))[:,numpy.newaxis])



