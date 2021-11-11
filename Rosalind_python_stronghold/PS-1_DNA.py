#!/home/hades/anaconda3/bin/python

import sys
import errno

class TerminalColor:
  ERRO = '\033[91m'
  NORMAL = '\033[0m'


def count_bases(sequence_file):
  with open(sequence_file) as seq_file:
    sequence = ''
    for line in seq_file:
      sequence = sequence + line
    output = str(sequence.count('A'))
    output = output + ' ' + str(sequence.count('C'))
    output = output + ' ' + str(sequence.count('G'))
    output = output + ' ' + str(sequence.count('T'))
    return output


def help():
  print (TerminalColor.ERRO +
         "É necessário informar o arquivo com a sequencia nucleotídica." +
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
    base_count = count_bases(sys.argv[1])
    print (base_count)

