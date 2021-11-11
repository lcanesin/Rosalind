#!/home/hades/anaconda3/bin/python

import sys
import errno

class TerminalColor:
  ERRO = '\033[91m'
  NORMAL = '\033[0m'


def translate2rna(sequence_file):
  with open(sequence_file) as seq_file:
    sequence = ''
    for line in seq_file:
      sequence = sequence + line
    translate_table = sequence.maketrans("T","U")
    return sequence.translate(translate_table) 


def help():
  print (TerminalColor.ERRO +
         "É necessário informar o arquivo com a sequencia de DNA." +
         TerminalColor.NORMAL)
  print (TerminalColor.ERRO +
         "Sintaxe: {} <sequence_file>".format(sys.argv[0]) +
         TerminalColor.NORMAL)


if __name__ == '__main__':
  if len(sys.argv) < 2 :
    help()
    sys.exit(errno.EPERM)
  elif sys.argv[1].isnumeric():
    help()
    print(TerminalColor.ERRO +
          'O primeiro argumento deve ser o arquivo com a sequencia' +
          TerminalColor.NORMAL)
    sys.exit(errno.EINVAL)
  else :
    rna_sequence = translate2rna(sys.argv[1])
    print (rna_sequence)

