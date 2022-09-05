"""Module utils."""
__author__ = 'Joan A. Pinol  (japinol)'

from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Size(NamedTuple):
    w: int
    h: int


def pretty_dict_print(d, indent=0):
    for key, value in d.items():
        print('\t' * indent, f"{str(key):22}", '-->', end='')
        if isinstance(value, dict):
            print('')
            pretty_dict_print(value, indent + 1)
        else:
            print('\t' * (indent + 1), '{:>10}'.format(str(value)))


def pretty_dict_to_string(d, indent=0, with_last_new_line=False, res='', firt_time=True):
    for key, value in d.items():
        res = '%s%s%s%s' % (res, '\t' * indent, f"{str(key):22}", '-->')
        if isinstance(value, dict):
            res = '%s\n' % res
            res = '%s%s' % (res, pretty_dict_to_string(value, indent + 1, res='', firt_time=False))
        else:
            res = '{}{}{:>10}\n'.format(res, '\t' * (indent + 1), str(value))
    if firt_time and not with_last_new_line:
        res = res[:-1]
    return res


def write_list_to_file(file, value, open_method='a'):
    with open(file, open_method) as fout:
        for line in value:
            fout.write(line)
    value = []


def file_read_list(file_name, lines_to_read):
    res = []
    try:
        with open(file_name, "r") as file_in:
            i = 0
            for line in file_in:
                if i <= lines_to_read:
                    res.append(line.lower().replace('\n', '').replace(' ', ''))
                i += 1
    except FileNotFoundError:
        res = False
        print(f"File does not exist: {file_name}")
    except Exception:
        res = False
    return res
