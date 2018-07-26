from mit_cs1_1_2.mitAbstractCollector import mitAbstractCollector
from mit_cs1_1_2.onlineldavb import OnlineLDA
import mit_csl_1_2.onlineldavb onlineldavb
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





    # vocab =
    # K =
    # D =
    # alpha =
    # eta =
    # tau0 =
    # kappa =
    #
    # _lda = OnlineLDA(vocab, K, D, alpha, eta, tau0, kappa)

    # Vizualize

if __name__ == '__main__':
    main()