# Do not import DEFAULT_QUALITIES directly
# Use QualityManager instead
DEFAULT_QUALITIES = [
    
    # 3 notes
    # ("",(0, 1, 6)),
    # ("",(0, 1, 7)),
    ('sus2', (0, 2, 7)), # suspended 2nd
    ("aug9",(0, 2, 8)),
    ('dim', (0, 3, 6)), # diminished triad
    ('m', (0, 3, 7)), # min
    # ("",(0, 3, 8)), # bVI maj
    ("m6",(0, 3, 9)),
    # Not to confuse Ab5 with A(b5)
    ('(b5)', (0, 4, 6)),
    ('', (0, 4, 7)), # maj
    ('aug', (0, 4, 8)), # augmented triad
    # ("",(0, 4, 9)), # VI min
    ("7",(0, 4, 10)),
    # ("",(0, 5, 6)),
    ('sus4', (0, 5, 7)), # suspended 4th
    # ("",(0, 5, 8)), # IV min
    # ("",(0, 5, 9)), # IV maj
    ("7sus4",(0, 5, 10)),
    ("△sus4",(0, 5, 11)),
    # ("",(0, 6, 7)),
    # ("",(0, 6, 8)),
    ("°7",(0, 6, 9)),
    ("7b5",(0, 6, 10)),
    ("△b5",(0, 6, 11)),
    
    
    # 4 notes
    ("dim(b9)",(0, 1, 3, 6)),
    ("mb9",(0, 1, 3, 7)),
    # ("",(0, 1, 3, 8)), # bVIadd11/R
    ("dim(b9)",(0, 1, 3, 9)), 
    ("(b5b9)",(0, 1, 4, 6)),
    ("addb9",(0, 1, 4, 7)), 
    ("aug(b9)",(0, 1, 4, 8)), 
    # ("",(0, 1, 4, 9)), # MVI/R
    # ("",(0, 1, 4, 10)), # bIIdim/R
    ("sus(b9)",(0, 1, 5, 7)),
    # ("",(0, 1, 5, 8)), # bII△/R
    # ("",(0, 1, 5, 9)), # IVb5/R
    # ("",(0, 1, 5, 10)), # domVIIm/R
    # ("",(0, 1, 5, 11)), # bII7/R
    # ("",(0, 1, 6, 8)), # bIIsus/R
    ("dim(b9)",(0, 1, 6, 9)),
    # ("",(0, 1, 6, 10)), # bV/R
    # ("",(0, 1, 6, 11)), # majVII/R
    # ("",(0, 1, 6, 12)),
    # ("",(0, 1, 7, 9)),
    # ("",(0, 1, 7, 10)),
    # ("",(0, 1, 7, 11)),
    # ("",(0, 1, 7, 12)),
    # ("",(0, 1, 7, 13)),
    # ("",(0, 2, 3, 6)),
    # ("",(0, 2, 3, 7)),
    # ("",(0, 2, 3, 8)),
    # ("",(0, 2, 3, 9)),
    # ("",(0, 2, 4, 6)),
    # ("",(0, 2, 4, 7)),
    # ("",(0, 2, 4, 8)),
    # ("",(0, 2, 4, 9)),
    # ("",(0, 2, 4, 10)),
    # ("",(0, 2, 5, 6)),
    ('sus4add2', (0, 2, 5, 7)),
    # ("",(0, 2, 5, 8)),
    # ("",(0, 2, 5, 9)),
    # ("",(0, 2, 5, 10)),
    # ("",(0, 2, 5, 11)),
    # ("",(0, 2, 6, 7)),
    # ("",(0, 2, 6, 8)),
    # ("",(0, 2, 6, 9)),
    # ("",(0, 2, 6, 10)),
    # ("",(0, 2, 6, 11)),
    # ("",(0, 2, 6, 12)),
    # ("",(0, 2, 7, 8)),
    # ("",(0, 2, 7, 9)),
    ('7sus2', (0, 2, 7, 10)),
    ('△sus2', (0, 2, 7, 11)),
    # ("",(0, 2, 7, 12)),
    # ("",(0, 2, 7, 13)),
    # ("",(0, 2, 8, 9)),
    # ("",(0, 2, 8, 10)),
    # ("",(0, 2, 8, 11)),
    # ("",(0, 2, 8, 12)),
    # ("",(0, 2, 8, 13)),
    # ("",(0, 2, 8, 14)),
    # ("",(0, 3, 4, 6)),
    # ("",(0, 3, 4, 7)),
    # ("",(0, 3, 4, 8)),
    # ("",(0, 3, 4, 9)),
    # ("",(0, 3, 4, 10)),
    # ("",(0, 3, 5, 6)),
    ('madd4', (0, 3, 5, 7)),
    # ("",(0, 3, 5, 8)),
    # ("",(0, 3, 5, 9)),
    # ("",(0, 3, 5, 10)),
    # ("",(0, 3, 5, 11)),
    # ("",(0, 3, 6, 7)),
    ('dim6', (0, 3, 6, 8)),
    ('°7', (0, 3, 6, 9)), # full diminished 7
    ('m7b5', (0, 3, 6, 10)),
    ('ø7', (0, 3, 6, 10)), # half dim 7 (equiv. to m7b5)
    # ("",(0, 3, 6, 11)),
    # ("",(0, 3, 6, 12)),
    # ("",(0, 3, 7, 8)),
    ('m6', (0, 3, 7, 9)),
    ('m7', (0, 3, 7, 10)), # minor 7
    ('m△', (0, 3, 7, 11)), # minor maj7
    # ("",(0, 3, 7, 12)),
    # ("",(0, 3, 7, 13)),
    ('madd9', (0, 3, 7, 14)),
    # ("",(0, 3, 8, 9)),
    ('m7#5', (0, 3, 8, 10)),
    # ("",(0, 3, 8, 11)),
    # ("",(0, 3, 8, 12)),
    # ("",(0, 3, 8, 13)),
    # ("",(0, 3, 8, 14)),
    # ("",(0, 3, 9, 10)),
    # ("",(0, 3, 9, 11)),
    # ("",(0, 3, 9, 12)),
    # ("",(0, 3, 9, 13)),
    # ("",(0, 3, 9, 14)),
    # ("",(0, 3, 9, 15)),
    ('add4', (0, 4, 5, 7)),
    # ("",(0, 4, 5, 8)),
    # ("",(0, 4, 5, 9)),
    # ("",(0, 4, 5, 10)),
    # ("",(0, 4, 5, 11)),
    # ("",(0, 4, 6, 7)),
    # ("",(0, 4, 6, 8)),
    # ("",(0, 4, 6, 9)),
    ('7b5', (0, 4, 6, 10)),
    ('△b5', (0, 4, 6, 11)),
    # ("",(0, 4, 6, 12)),
    # ("",(0, 4, 7, 8)),
    # ('6', (0, 4, 7, 9)),
    ('7', (0, 4, 7, 10)), # dominant 7
    ('△', (0, 4, 7, 11)), # maj7
    # ("",(0, 4, 7, 12)),
    # ("",(0, 4, 7, 13)),
    ('add9', (0, 4, 7, 14)),
    ('add11', (0, 4, 7, 17)),
    # ("",(0, 4, 8, 9)),
    ('7#5', (0, 4, 8, 10)),
    ('△#5', (0, 4, 8, 11)),
    # ("",(0, 4, 8, 12)),
    # ("",(0, 4, 8, 13)),
    # ("",(0, 4, 8, 14)),
    # ("",(0, 4, 9, 10)),
    # ("",(0, 4, 9, 11)),
    # ("",(0, 4, 9, 12)),
    # ("",(0, 4, 9, 13)),
    # ("",(0, 4, 9, 14)),
    # ("",(0, 4, 9, 15)),
    # ("",(0, 4, 10, 11)),
    # ("",(0, 4, 10, 12)),
    # ("",(0, 4, 10, 13)),
    # ("",(0, 4, 10, 14)),
    # ("",(0, 4, 10, 15)),
    # ("",(0, 4, 10, 16)),
    # ("",(0, 5, 6, 8)),
    # ("",(0, 5, 6, 9)),
    # ("",(0, 5, 6, 10)),
    # ("",(0, 5, 6, 11)),
    # ("",(0, 5, 6, 12)),
    # ("",(0, 5, 7, 8)),
    # ("",(0, 5, 7, 9)),
    ('7sus4', (0, 5, 7, 10)),
    ('△sus4', (0, 5, 7, 11)),
    # ("",(0, 5, 7, 12)),
    # ("",(0, 5, 7, 13)),
    ('sus4add9', (0, 5, 7, 14)),
    # ("",(0, 5, 8, 9)),
    # ("",(0, 5, 8, 10)),
    # ("",(0, 5, 8, 11)),
    # ("",(0, 5, 8, 12)),
    # ("",(0, 5, 8, 13)),
    # ("",(0, 5, 8, 14)),
    # ("",(0, 5, 9, 10)),
    # ("",(0, 5, 9, 11)),
    # ("",(0, 5, 9, 12)),
    # ("",(0, 5, 9, 13)),
    # ("",(0, 5, 9, 14)),
    # ("",(0, 5, 9, 15)),
    # ("",(0, 5, 10, 11)),
    # ("",(0, 5, 10, 12)),
    # ("",(0, 5, 10, 13)),
    # ("",(0, 5, 10, 14)),
    # ("",(0, 5, 10, 15)),
    # ("",(0, 5, 10, 16)),
    # ("",(0, 5, 11, 12)),
    # ("",(0, 5, 11, 13)),
    # ("",(0, 5, 11, 14)),
    # ("",(0, 5, 11, 15)),
    # ("",(0, 5, 11, 16)),
    # ("",(0, 5, 11, 17)),
    # ("",(0, 6, 7, 9)),
    # ("",(0, 6, 7, 10)),
    # ("",(0, 6, 7, 11)),
    # ("",(0, 6, 7, 12)),
    # ("",(0, 6, 7, 13)),
    # ("",(0, 6, 8, 9)),
    # ("",(0, 6, 8, 10)),
    # ("",(0, 6, 8, 11)),
    # ("",(0, 6, 8, 12)),
    # ("",(0, 6, 8, 13)),
    # ("",(0, 6, 8, 14)),
    # ("",(0, 6, 9, 10)),
    # ("",(0, 6, 9, 11)),
    # ("",(0, 6, 9, 12)),
    # ("",(0, 6, 9, 13)),
    # ("",(0, 6, 9, 14)),
    # ("",(0, 6, 9, 15)),
    # ("",(0, 6, 10, 11)),
    # ("",(0, 6, 10, 12)),
    # ("",(0, 6, 10, 13)),
    # ("",(0, 6, 10, 14)),
    # ("",(0, 6, 10, 15)),
    # ("",(0, 6, 10, 16)),
    # ("",(0, 6, 11, 12)),
    # ("",(0, 6, 11, 13)),
    # ("",(0, 6, 11, 14)),
    # ("",(0, 6, 11, 15)),
    # ("",(0, 6, 11, 16)),
    # ("",(0, 6, 11, 17)),
    # ("",(0, 6, 12, 13)),
    # ("",(0, 6, 12, 14)),
    # ("",(0, 6, 12, 15)),
    # ("",(0, 6, 12, 16)),
    # ("",(0, 6, 12, 17)),
    # ("",(0, 6, 12, 18)),
    
    
    # 5 notes
    ('m69', (0, 3, 7, 9, 14)),
    ('69', (0, 4, 7, 9, 14)),
    ('9', (0, 4, 7, 10, 14)),
    ('m9', (0, 3, 7, 10, 14)),
    ('△9', (0, 4, 7, 11, 14)), # major 9
    ('9sus4', (0, 5, 7, 10, 14)),
    ('7b9', (0, 4, 7, 10, 13)),
    ('7#9', (0, 4, 7, 10, 15)),
    ('m7b9', (0, 3, 7, 10, 13)),
    ('9b5', (0, 4, 6, 10, 14)),
    ('9#5', (0, 4, 8, 10, 14)),
    ('7#9b5', (0, 4, 6, 10, 15)),
    ('7#9#5', (0, 4, 8, 10, 15)),
    ('m7b9b5', (0, 3, 6, 10, 13)),
    ('7b9b5', (0, 4, 6, 10, 13)),
    ('7b9#5', (0, 4, 8, 10, 13)),
    ('7#11', (0, 4, 7, 10, 18)),
    ('△#11', (0, 4, 7, 11, 18)),
    ('△b9', (0, 4, 7, 11, 13)),
    ('7b13', (0, 4, 7, 10, 20)),
    ('m7add11', (0, 3, 7, 10, 17)),
    ('△add11', (0, 4, 7, 11, 17)),
    ('m△add11', (0, 3, 7, 11, 17)),
    ('m△b9', (0, 3, 7, 11, 13)),
    ('m△9', (0, 3, 7, 11, 14)),
    ('13', (0, 4, 9, 10, 14)), # the babylon sisters chord
    ('13', (0, 4, 10, 14, 21)),

    
    # 6 notes
    ('9#11', (0, 4, 7, 10, 14, 18)),
    ('13', (0, 4, 7, 10, 14, 21)),
    ('13b9', (0, 4, 7, 10, 13, 21)),
    ('13#9', (0, 4, 7, 10, 15, 21)),
    ('13#11', (0, 4, 7, 10, 18, 21)),
    ('△add13', (0, 4, 7, 9, 11, 14)),
    ('11', (0, 4, 7, 10, 14, 17)),
    ('△11', (0, 4, 7, 11, 14, 17)), # major 11
    ('m11', (0, 3, 7, 10, 14, 17)),
    ('7b9#9', (0, 4, 7, 10, 13, 15)),
    ('7b9#11', (0, 4, 7, 10, 13, 18)),
    ('7#9#11', (0, 4, 7, 10, 15, 18)),
    
    #7 notes
    ('7b9b13', (0, 4, 7, 10, 13, 17, 20)),
    ('13', (0, 4, 7, 10, 14, 17, 21))

]

'''
NUMBER KEY

0: ROOT
1: bII
2: II
3: mIII
4: III
5: IV
6: #IV / bV
7: V
8: #V / bVI
9: VI
10: domVII
11: majVII
12: ROOT
----------
13: b9
14: 9
15: #9
16: sIII
17: 11
18: #11
19: sV
20: b13
21: 13
22: sVII
23: smajVII
24: ROOT
'''
