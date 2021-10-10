import re


def solution(new_id):
    # step 1
    new_id = new_id.lower()

    # step 2
    new_id = re.sub(
        '\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\=|\+|\[|\{|\]|\}|\:|\?|\,|\<|\>|\/', '', new_id)

    # step 3
    while True:
        prev_id = new_id
        new_id = new_id.replace('..', '.')

        if new_id == prev_id:
            break

    # step 4
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')

    # step 5
    if new_id == '':
        new_id = new_id + 'a'

    # step 6
    if len(new_id) >= 16:
        new_id = new_id[0:15]

    new_id = new_id.rstrip('.')

    # step 7
    while True:
        if len(new_id) >= 3:
            break
        else:
            new_id = new_id + new_id[-1]

    return new_id
