from typing import List

from .chord import Chord
from .quality import QualityManager
from .utils import note_to_val
import itertools
import numpy as np


def find_chords_from_notes(notes: List[str], rap: dict, key: int, slash) -> List[Chord]:
    """ Find possible chords consisted from notes

    :param notes: List of note arranged from lower note. ex) ["C", "Eb", "G"]
    :return: List of chord
    """
    if not notes:
        raise ValueError("Please specify notes which consist a chord.")
    if slash == 'n':      
        root = notes[0]
    else:
        root = slash
    root_and_positions = []
    for rotated_notes in get_all_rotated_notes(notes):
        rotated_root = rotated_notes[0]
        root_and_positions.append((rotated_root, notes_to_positions(rotated_notes, rotated_notes[0])))
    print(root_and_positions)
    rap[key] = root_and_positions
    chords = []
    for temp_root, positions in root_and_positions:
        quality = QualityManager().find_quality_from_components(temp_root, positions)
        if quality is None:
            continue
        if temp_root == root:
            chord = "{}{}".format(root, quality)
        else:
            chord = "{}{}/{}".format(temp_root, quality, root)
        chords.append(Chord(chord))
    return chords


def notes_to_positions(notes: List[str], root: str) -> List[int]:
    """ Get notes positions from the root note

    >>> notes_to_positions(["C", "E", "G"], "C")
    [0, 4, 7]

    :param notes: List of notes
    :param root: Root note
    :return: List of note positions
    """
    root_pos = note_to_val(root)
    current_pos = root_pos
    positions = []
    for note in notes:
        note_pos = note_to_val(note)
        if note_pos < current_pos:
            note_pos += 12 * ((current_pos - note_pos) // 12 + 1)
        positions.append(note_pos - root_pos)
        current_pos = note_pos
    return positions


def get_all_rotated_notes(notes: List[str]) -> List[List[str]]:
    """ Get all rotated notes

    get_all_rotated_notes([A,C,E]) -> [[A,C,E],[C,E,A],[E,A,C]]
    """
    #ROTATIONS
    # notes_list = []
    # for x in range(len(notes)):
        # notes_list.append(notes[x:] + notes[:x])
    
    #ALL PERMS
    notes_list = list(itertools.permutations(notes))
    return notes_list

def get_modded_raps(rap, key):
    raps = rap[key]
    for root, pos in raps:
        pos = np.array(pos)
        modpos = (pos[1:]-pos[1]).tolist()
        print([root, modpos])

# [[0, 8, 11, 15, 17],
# [0, 8, 11, 17, 27],
# [0, 8, 15, 23, 29],
# [0, 8, 15, 17, 23],
# [0, 8, 17, 23, 27],
# [0, 8, 17, 27, 35],
# [0, 11, 20, 27, 29],
# [0, 11, 20, 29, 39],
# [0, 11, 15, 20, 29],
# [0, 11, 15, 17, 20],
# [0, 11, 17, 20, 27],
# [0, 11, 17, 27, 32]]
