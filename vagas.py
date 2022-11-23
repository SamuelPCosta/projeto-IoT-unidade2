# USAGE
# python vagas.py -v video [-s nome_do_setor] [-c 0 ou 1]

import argparse
import numpy as np  # type: ignore
import funcoesComuns as func
import cadastro as cad
import monitorar as m

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to input video")
ap.add_argument("-s", "--setor", help="informa o nome do setor")
ap.add_argument("-c", "--cadastro", type=int, default=0,
                help="[0] - monitoramento das vagas | [1] - cadastra novo setor")
args = vars(ap.parse_args())


def main():
    func.header()
    if (args["cadastro"] == 1):
        print("[1] - Cadastre um novo setor")
        cad.cadastrar(args)
    else:
        m.monitorar()


if __name__ == '__main__':
    main()
