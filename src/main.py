from config import BaseOptions
from embed import Embed
from extract import Extract


if __name__ == '__main__':
    opt = BaseOptions().parse()   # get options

    if opt.emb:
        print("Embedding")
        encrypt = Embed(opt)
        encrypt.integrate_embedding()
    elif opt.ext:
        print("Extracting")
        decrypt = Extract(opt)
        decrypt.integrate_extraction()
