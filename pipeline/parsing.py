#Organize code into functions
#Use with blocks to open files, so that they will automatically be closed
#Take advantage of Python's csv library.

#A reasonable approach would make just one pass through the file, accumulating statistics in a data structure as you go, and then write a summary of that data structure when you reach the end of the input.

from collections import OrderedDict
import csv
import re

def analyze_log(f):
    stats = OrderedDict()
    for line in f:
        re.search(…)
        …
    return stats

def write_stats(stats, f):
    out = csv.writer(f)
    out.writerow(…)
    for var in stats:
        out.writerow(…)

def main(input_filename, output_filename):
    with open(input_filename) as input_file:
        stats = analyze_log(input_file)
    with open(output_filename, 'w') as output_file:
        write_stats(stats, output_file)

if __name__ == '__main__':
    main(r'C:\Users\AEC_FULL\…\core1_sram_ReadWrite.txt',
         r'C:\Users\AEC_FULL\…\ParsedOutput.csv')



def analyze_log(f):
    stats = OrderedDict()
    for line in f:
        _, _, rw_datatype, _, core_varname, _ = line.split()
        match = re.search(r'.*[*\\](.*)', core_varname)
        if not match:
            continue
        var = match.group(1)
        match = re.search(r'([01])\\Global', core_varname)
        core = match and match.group(1) or 'X'
        rw, datatype = rw_datatype.split('-', 1)

        var_stats = stats.get(var, {'rd': {'0': 0, '1': 0, 'X': 0},
                                    'wr': {'0': 0, '1': 0, 'X': 0},
                                    'type': datatype })
        stats[var] = var_stats
        var_stats[rw][core] += 1
    return stats


def write_stats(stats, f):
    out = csv.writer(f)
    out.writerow(['Variable', 'Datatype',
                  'CORE 0', None, 'CORE 1', None, 'CORE X', None])
    out.writerow([None, None] +
                 ['Read', 'Write'] * 3)
    for var in stats:
        out.writerow([var, stats[var]['type'],
                      stats[var]['rd']['0'], stats[var]['wr']['0'],
                      stats[var]['rd']['1'], stats[var]['wr']['1'],
                      stats[var]['rd']['X'], stats[var]['wr']['X']])