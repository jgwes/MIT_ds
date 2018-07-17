from mit_cs1_1_2.mitAbstractCollector import mitAbstractCollector
from mit_cs1_1_2.onlineldavb import OnlineLDA
import pickle

def main():

    # Collect Abstracts & Store in Collection
    _abstract_collector = mitAbstractCollector()
    print("attempting to create abstract file...")
    _abstract_collector.create_abstract_file()
    _abstract_collection_filename = _abstract_collector.get_abstract_collection_file_handler()

    _abstracts_collection_file = open(_abstract_collection_filename, 'rb')
    _abstracts_collection = pickle.load(_abstracts_collection_file)
    _abstracts_collection_file.close()

    print("printing abstracts collection...")
    print(_abstracts_collection[0])
    print(_abstracts_collection[1])

    # Call OnlineLDA
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

    vocab =
    K =
    D =
    alpha =
    eta =
    tau0 =
    kappa =

    _lda = OnlineLDA(vocab, K, D, alpha, eta, tau0, kappa)

    # Vizualize

if __name__ == '__main__':
    main()