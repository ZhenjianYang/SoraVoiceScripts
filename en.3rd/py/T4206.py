from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4206   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4206.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T4206   ._SN',
            'ED6_DT21/T4206_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Kevin',                                # 9
        'Estelle',                              # 10
        'Joshua',                               # 11
        'Scherazard',                           # 12
        'Olivier',                              # 13
        'Princess Klaudia',                     # 14
        'Agate',                                # 15
        'Tita',                                 # 16
        'Zin',                                  # 17
        'Anelace',                              # 18
        'Josette',                              # 19
        'Captain Schwarz',                      # 20
        'Major Vander',                         # 21
        'Richard',                              # 22
        'Lt. Colonel Cid',                      # 23
        'Kanone',                               # 24
        'Mayor Klaus',                          # 25
        'Mayor Maybelle',                       # 26
        'Dean Collins',                         # 27
        'Factory Chief Murdock',                # 28
        'Lila',                                 # 29
        'Queen Alicia',                         # 30
        'Duke Dunan',                           # 31
        'Ambassador Crainagh',                  # 32
        'Butler Phillip',                       # 33
        'Head Maid Hilda',                      # 34
        'Sieg',                                 # 35
        'Ambassador Cochrane',                  # 36
        'Elnan',                                # 37
        'Kurt',                                 # 38
        'Grant',                                # 39
        'Carna',                                # 40
        'General Morgan',                       # 41
        'Cassius',                              # 42
        'Don',                                  # 43
        'Kyle',                                 # 44
        'Professor Russell',                    # 45
        'Nial',                                 # 46
        'Dorothy',                              # 47
        'Head Cook Gervais',                    # 48
        'Folk',                                 # 49
        'Regis',                                # 50
        'Sanders',                              # 51
        'Shea',                                 # 52
        'Sorella',                              # 53
        'Nage',                                 # 54
        'Panna',                                # 55
        'Primrose',                             # 56
        'Ekle',                                 # 57
        'Royal Guardsman',                      # 58
        'Royal Guardsman',                      # 59
        'Royal Guardsman',                      # 60
        'Royal Guardsman',                      # 61
        'Mayor Norman',                         # 62
        'Booze Glass',                          # 63
        'Target Camera',                        # 64
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03080 ._CH',             # 00
        'ED6_DT27/CH03000 ._CH',             # 01
        'ED6_DT27/CH03200 ._CH',             # 02
        'ED6_DT07/CH00020 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT27/CH03960 ._CH',             # 05
        'ED6_DT07/CH00050 ._CH',             # 06
        'ED6_DT07/CH00060 ._CH',             # 07
        'ED6_DT07/CH00070 ._CH',             # 08
        'ED6_DT07/CH01630 ._CH',             # 09
        'ED6_DT27/CH03270 ._CH',             # 0A
        'ED6_DT07/CH02090 ._CH',             # 0B
        'ED6_DT27/CH03570 ._CH',             # 0C
        'ED6_DT07/CH02030 ._CH',             # 0D
        'ED6_DT27/CH03590 ._CH',             # 0E
        'ED6_DT07/CH02100 ._CH',             # 0F
        'ED6_DT07/CH02350 ._CH',             # 10
        'ED6_DT07/CH02360 ._CH',             # 11
        'ED6_DT07/CH02600 ._CH',             # 12
        'ED6_DT07/CH02620 ._CH',             # 13
        'ED6_DT07/CH02370 ._CH',             # 14
        'ED6_DT07/CH02010 ._CH',             # 15
        'ED6_DT07/CH02140 ._CH',             # 16
        'ED6_DT27/CH03710 ._CH',             # 17
        'ED6_DT07/CH02470 ._CH',             # 18
        'ED6_DT07/CH02460 ._CH',             # 19
        'ED6_DT07/CH02323 ._CH',             # 1A
        'ED6_DT27/CH03720 ._CH',             # 1B
        'ED6_DT07/CH02610 ._CH',             # 1C
        'ED6_DT07/CH02560 ._CH',             # 1D
        'ED6_DT07/CH02380 ._CH',             # 1E
        'ED6_DT07/CH02400 ._CH',             # 1F
        'ED6_DT07/CH02580 ._CH',             # 20
        'ED6_DT07/CH01620 ._CH',             # 21
        'ED6_DT07/CH01260 ._CH',             # 22
        'ED6_DT07/CH01240 ._CH',             # 23
        'ED6_DT07/CH02080 ._CH',             # 24
        'ED6_DT27/CH03670 ._CH',             # 25
        'ED6_DT07/CH02110 ._CH',             # 26
        'ED6_DT07/CH02120 ._CH',             # 27
        'ED6_DT07/CH02020 ._CH',             # 28
        'ED6_DT07/CH02440 ._CH',             # 29
        'ED6_DT07/CH02060 ._CH',             # 2A
        'ED6_DT06/CH20063 ._CH',             # 2B
        'ED6_DT07/CH01280 ._CH',             # 2C
        'ED6_DT07/CH01520 ._CH',             # 2D
        'ED6_DT07/CH01350 ._CH',             # 2E
        'ED6_DT07/CH02540 ._CH',             # 2F
        'ED6_DT07/CH01320 ._CH',             # 30
        'ED6_DT06/CH20127 ._CH',             # 31
        'ED6_DT06/CH20064 ._CH',             # 32
        'ED6_DT07/CH01200 ._CH',             # 33
        'ED6_DT06/CH20021 ._CH',             # 34
    )

    AddCharChipPat(
        'ED6_DT27/CH03080P._CP',             # 00
        'ED6_DT27/CH03000P._CP',             # 01
        'ED6_DT27/CH03200P._CP',             # 02
        'ED6_DT07/CH00020P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT27/CH03960P._CP',             # 05
        'ED6_DT07/CH00050P._CP',             # 06
        'ED6_DT07/CH00060P._CP',             # 07
        'ED6_DT07/CH00070P._CP',             # 08
        'ED6_DT07/CH01630P._CP',             # 09
        'ED6_DT27/CH03270P._CP',             # 0A
        'ED6_DT07/CH02090P._CP',             # 0B
        'ED6_DT27/CH03570P._CP',             # 0C
        'ED6_DT07/CH02030P._CP',             # 0D
        'ED6_DT27/CH03590P._CP',             # 0E
        'ED6_DT07/CH02100P._CP',             # 0F
        'ED6_DT07/CH02350P._CP',             # 10
        'ED6_DT07/CH02360P._CP',             # 11
        'ED6_DT07/CH02600P._CP',             # 12
        'ED6_DT07/CH02620P._CP',             # 13
        'ED6_DT07/CH02370P._CP',             # 14
        'ED6_DT07/CH02010P._CP',             # 15
        'ED6_DT07/CH02140P._CP',             # 16
        'ED6_DT27/CH03710P._CP',             # 17
        'ED6_DT07/CH02470P._CP',             # 18
        'ED6_DT07/CH02460P._CP',             # 19
        'ED6_DT07/CH02323P._CP',             # 1A
        'ED6_DT27/CH03720P._CP',             # 1B
        'ED6_DT07/CH02610P._CP',             # 1C
        'ED6_DT07/CH02560P._CP',             # 1D
        'ED6_DT07/CH02380P._CP',             # 1E
        'ED6_DT07/CH02400P._CP',             # 1F
        'ED6_DT07/CH02580P._CP',             # 20
        'ED6_DT07/CH01620P._CP',             # 21
        'ED6_DT07/CH01260P._CP',             # 22
        'ED6_DT07/CH01240P._CP',             # 23
        'ED6_DT07/CH02080P._CP',             # 24
        'ED6_DT27/CH03670P._CP',             # 25
        'ED6_DT07/CH02110P._CP',             # 26
        'ED6_DT07/CH02120P._CP',             # 27
        'ED6_DT07/CH02020P._CP',             # 28
        'ED6_DT07/CH02440P._CP',             # 29
        'ED6_DT07/CH02060P._CP',             # 2A
        'ED6_DT06/CH20063P._CP',             # 2B
        'ED6_DT07/CH01280P._CP',             # 2C
        'ED6_DT07/CH01520P._CP',             # 2D
        'ED6_DT07/CH01350P._CP',             # 2E
        'ED6_DT07/CH02540P._CP',             # 2F
        'ED6_DT07/CH01320P._CP',             # 30
        'ED6_DT06/CH20127P._CP',             # 31
        'ED6_DT06/CH20064P._CP',             # 32
        'ED6_DT07/CH01200P._CP',             # 33
        'ED6_DT06/CH20021P._CP',             # 34
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 60,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 52,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 56,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 55,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 58,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 57,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 53,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 54,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 62,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 61,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 51,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 50,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 47,
        ChipIndex           = 0x2F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 59,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327732,
        ChipIndex           = 0x34,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3700,
        Y                   = 10000,
        Z                   = 83810,
        Range               = 4050,
        Unknown_10          = 0x4E20,
        Unknown_14          = 0x127C8,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )


    DeclActor(
        TriggerX            = 12130,
        TriggerZ            = 12000,
        TriggerY            = 53740,
        TriggerRange        = 1000,
        ActorX              = 12130,
        ActorZ              = 14000,
        ActorY              = 53740,
        Flags               = 0x7E,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_996",          # 00, 0
        "Function_1_9E9",          # 01, 1
        "Function_2_CAC",          # 02, 2
        "Function_3_E29",          # 03, 3
        "Function_4_F66",          # 04, 4
        "Function_5_108D",         # 05, 5
        "Function_6_11AD",         # 06, 6
        "Function_7_12AB",         # 07, 7
        "Function_8_12E8",         # 08, 8
        "Function_9_1451",         # 09, 9
        "Function_10_1959",        # 0A, 10
        "Function_11_1E2F",        # 0B, 11
        "Function_12_1FB8",        # 0C, 12
        "Function_13_2005",        # 0D, 13
        "Function_14_204E",        # 0E, 14
        "Function_15_2091",        # 0F, 15
        "Function_16_2266",        # 10, 16
        "Function_17_2552",        # 11, 17
        "Function_18_4774",        # 12, 18
        "Function_19_47BC",        # 13, 19
        "Function_20_47FD",        # 14, 20
        "Function_21_9950",        # 15, 21
        "Function_22_9992",        # 16, 22
        "Function_23_99D4",        # 17, 23
        "Function_24_99FD",        # 18, 24
        "Function_25_9A26",        # 19, 25
        "Function_26_9F89",        # 1A, 26
        "Function_27_A017",        # 1B, 27
        "Function_28_A16E",        # 1C, 28
        "Function_29_A942",        # 1D, 29
        "Function_30_AB19",        # 1E, 30
        "Function_31_ADBA",        # 1F, 31
        "Function_32_B1D8",        # 20, 32
        "Function_33_B275",        # 21, 33
        "Function_34_B2FF",        # 22, 34
        "Function_35_B5B1",        # 23, 35
        "Function_36_B6DF",        # 24, 36
        "Function_37_BC39",        # 25, 37
        "Function_38_BD30",        # 26, 38
        "Function_39_BEBA",        # 27, 39
        "Function_40_C2FE",        # 28, 40
        "Function_41_C3DF",        # 29, 41
        "Function_42_C535",        # 2A, 42
        "Function_43_C9EB",        # 2B, 43
        "Function_44_CAA7",        # 2C, 44
        "Function_45_CC1E",        # 2D, 45
        "Function_46_CC8A",        # 2E, 46
        "Function_47_D2DB",        # 2F, 47
        "Function_48_D362",        # 30, 48
        "Function_49_DA17",        # 31, 49
        "Function_50_DAF7",        # 32, 50
        "Function_51_DBFF",        # 33, 51
        "Function_52_DF94",        # 34, 52
        "Function_53_E375",        # 35, 53
        "Function_54_E6FA",        # 36, 54
        "Function_55_E7FD",        # 37, 55
        "Function_56_E8DB",        # 38, 56
        "Function_57_E97C",        # 39, 57
        "Function_58_ECBA",        # 3A, 58
        "Function_59_EEE2",        # 3B, 59
        "Function_60_F0BE",        # 3C, 60
        "Function_61_F4A8",        # 3D, 61
        "Function_62_F634",        # 3E, 62
    )


    def Function_0_996(): pass

    label("Function_0_996")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_9C1")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)
    Jump("loc_9DD")

    label("loc_9C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_9DD")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 2)), scpexpr(EXPR_END)), "loc_9E8")
    Call(0, 9)

    label("loc_9E8")

    Return()

    # Function_0_996 end

    def Function_1_9E9(): pass

    label("Function_1_9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 2)), scpexpr(EXPR_END)), "loc_9F9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F9")

    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_A4E")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_A4E")

    OP_51(0x102, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x21, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x30, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x31, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x32, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x33, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x34, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x35, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x36, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x37, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x38, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x39, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x40, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x41, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x42, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x43, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x44, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x45, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_9E9 end

    def Function_2_CAC(): pass

    label("Function_2_CAC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD1")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_E13")

    label("loc_CD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEA")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_E13")

    label("loc_CEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D03")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_E13")

    label("loc_D03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1C")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_E13")

    label("loc_D1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D35")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_E13")

    label("loc_D35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4E")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_E13")

    label("loc_D4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D67")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_E13")

    label("loc_D67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D80")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_E13")

    label("loc_D80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D99")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_E13")

    label("loc_D99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB2")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_E13")

    label("loc_DB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCB")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_E13")

    label("loc_DCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE4")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_E13")

    label("loc_DE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFD")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_E13")

    label("loc_DFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E13")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_E13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E28")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_E13")

    label("loc_E28")

    Return()

    # Function_2_CAC end

    def Function_3_E29(): pass

    label("Function_3_E29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F65")
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFB776, 0x36B0, 0x1228C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC964, 0x36B0, 0x1214C, 0x7D0, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFC93C, 0x36B0, 0x12B2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x36B0, 0x12D0E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE124, 0x36B0, 0x13696, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFE124, 0x36B0, 0x13696, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x36B0, 0x12D0E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC93C, 0x36B0, 0x12B2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC964, 0x36B0, 0x1214C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFB776, 0x36B0, 0x1228C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB7BC, 0x36B0, 0x11A3A, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Jump("Function_3_E29")

    label("loc_F65")

    Return()

    # Function_3_E29 end

    def Function_4_F66(): pass

    label("Function_4_F66")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_108C")
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0x2EA4, 0x36B0, 0x11954, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2E72, 0x36B0, 0x13042, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x44FC, 0x36B0, 0x12EA8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x639C, 0x2EE0, 0x14BF4, 0x7D0, 0x0)
    Sleep(3000)
    OP_8C(0xFE, 225, 400)
    Sleep(300)
    OP_8E(0xFE, 0x4B14, 0x36B0, 0x13272, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4B5A, 0x36B0, 0x11B20, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_8E(0xFE, 0x4AA6, 0x36B0, 0x10C8E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x39DA, 0x36B0, 0x10AFE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3386, 0x36B0, 0x11058, 0x7D0, 0x0)
    OP_8E(0xFE, 0x33A4, 0x36B0, 0x11990, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    Jump("Function_4_F66")

    label("loc_108C")

    Return()

    # Function_4_F66 end

    def Function_5_108D(): pass

    label("Function_5_108D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11AC")
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFF1A0, 0x2EE0, 0xD4E4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 225, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFE908, 0x2EE0, 0xCBCA, 0x7D0, 0x0)
    Sleep(3000)
    OP_8C(0xFE, 90, 400)
    Sleep(300)
    OP_8E(0xFE, 0xB9A, 0x2EE0, 0xCB70, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x1090, 0x2EE0, 0xC8AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x17DE, 0x2EE0, 0xC256, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(3000)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFFA9C, 0x2EE0, 0xC8C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFBF0, 0x2EE0, 0xD430, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_5_108D")

    label("loc_11AC")

    Return()

    # Function_5_108D end

    def Function_6_11AD(): pass

    label("Function_6_11AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12AA")
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    OP_8E(0xFE, 0x5BE, 0x2EE0, 0xF7F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x28, 0x2EE0, 0xF85C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFE8D6, 0x2EE0, 0xFBA4, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(2500)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFE872, 0x2EE0, 0xF190, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(3500)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFE890, 0x2EE0, 0xF8D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3FC, 0x2EE0, 0xF636, 0x7D0, 0x0)
    OP_8E(0xFE, 0x456, 0x2EE0, 0xE9FC, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2500)
    Jump("Function_6_11AD")

    label("loc_12AA")

    Return()

    # Function_6_11AD end

    def Function_7_12AB(): pass

    label("Function_7_12AB")

    OP_8E(0xFE, 0x1B30, 0x36B0, 0x13BB4, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1EA, 0x33C2, 0x122DC, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFE480, 0x2EE0, 0xF21C, 0xFA0, 0x0)
    Return()

    # Function_7_12AB end

    def Function_8_12E8(): pass

    label("Function_8_12E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1450")
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(100, 16777215, 50)
    PlayEffect(0x0, 0xFF, 0x36, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    FadeToBright(100, 16777215)
    Sleep(600)
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(100, 16777215, 50)
    PlayEffect(0x0, 0xFF, 0x36, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    FadeToBright(100, 16777215)
    Sleep(1000)
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(100, 16777215, 50)
    PlayEffect(0x0, 0xFF, 0x36, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    FadeToBright(100, 16777215)
    Sleep(100)
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(100, 16777215, 50)
    PlayEffect(0x0, 0xFF, 0x36, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    FadeToBright(100, 16777215)
    Sleep(800)
    Jump("Function_8_12E8")

    label("loc_1450")

    Return()

    # Function_8_12E8 end

    def Function_9_1451(): pass

    label("Function_9_1451")

    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    SetChrFlags(0x2A, 0x4)
    SetChrPos(0x25, 11100, 12000, 55420, 270)
    SetChrPos(0x15, 11100, 12000, 57370, 90)
    SetChrPos(0x2A, 12190, 13600, 53700, 270)
    SetChrPos(0x31, -43010, 16000, 80590, 270)
    SetChrPos(0x30, -15740, 14000, 71720, 270)
    SetChrPos(0x1E, -12600, 14000, 75360, 180)
    SetChrPos(0x1D, 28180, 12000, 86160, 270)
    SetChrPos(0x1F, 31990, 12000, 90520, 225)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160D")
    SetChrPos(0x11, 10730, 14000, 80650, 270)
    Jump("loc_161E")

    label("loc_160D")

    SetChrPos(0x11, -8100, 12000, 58540, 180)

    label("loc_161E")

    SetChrPos(0x10, 1640, 12000, 64860, 270)
    SetChrPos(0x13, -24430, 12000, 86170, 270)
    SetChrPos(0x14, -25960, 12000, 87460, 180)
    SetChrPos(0x20, -11680, 14000, 77850, 0)
    SetChrPos(0x22, -9630, 14000, 81250, 270)
    SetChrPos(0x23, -9930, 14000, 77850, 0)
    SetChrPos(0x21, -11540, 14000, 81250, 90)
    SetChrPos(0x24, -12720, 14000, 81970, 90)
    SetChrPos(0x45, -13460, 14000, 79230, 90)
    SetChrPos(0x46, -25100, 12540, 86150, 0)
    OP_51(0x46, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x46, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x46, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x18, 8580, 12000, 65660, 270)
    SetChrPos(0x2B, 7080, 12000, 66950, 180)
    SetChrPos(0x2C, -4950, 12000, 54140, 45)
    SetChrPos(0x19, -5220, 12000, 57140, 270)
    SetChrPos(0x2D, -3420, 12000, 55740, 225)
    SetChrPos(0x2E, -5950, 12000, 59520, 225)
    SetChrPos(0x2F, -6530, 12000, 60440, 225)
    SetChrPos(0x32, -7010, 12000, 66950, 180)
    SetChrPos(0x33, -5490, 12000, 65800, 270)
    SetChrPos(0x1A, -8100, 12000, 57040, 0)
    SetChrPos(0x16, 15630, 14000, 70450, 0)
    SetChrPos(0x17, 15640, 14000, 71750, 180)
    SetChrPos(0x34, 18430, 14000, 70910, 270)
    SetChrPos(0x26, 6410, 12000, 56280, 180)
    SetChrPos(0x27, 6320, 12000, 54850, 0)
    SetChrPos(0x28, 5680, 12000, 57010, 180)
    SetChrPos(0x1B, 7900, 12000, 52560, 270)
    SetChrPos(0x1C, 6050, 12000, 52380, 90)
    SetChrPos(0x29, 13170, 12000, 60300, 270)
    SetChrPos(0x3B, 14190, 12000, 59700, 270)
    SetChrPos(0x3C, 14190, 12000, 58700, 270)
    SetChrPos(0x3D, -1040, 12000, 54320, 90)
    SetChrPos(0x3E, 1110, 12000, 59900, 270)
    SetChrPos(0x3F, 13220, 14000, 72080, 0)
    SetChrPos(0x40, -18500, 14000, 72250, 90)
    OP_43(0x3D, 0x0, 0x0, 0x5)
    OP_43(0x3E, 0x0, 0x0, 0x6)
    OP_43(0x3F, 0x0, 0x0, 0x4)
    OP_43(0x40, 0x0, 0x0, 0x3)
    SetChrPos(0x35, 12210, 12000, 57070, 270)
    SetChrPos(0x36, 6500, 12000, 60670, 270)
    SetChrPos(0x37, -9900, 12000, 53370, 90)
    SetChrPos(0x38, -12590, 14000, 73030, 0)
    SetChrPos(0x39, -8189, 12000, 60260, 180)
    SetChrPos(0x3A, -140, 12000, 58190, 0)
    SetChrPos(0x41, 3100, 14000, 82400, 180)
    SetChrPos(0x42, -3100, 14000, 82400, 180)
    SetChrPos(0x43, 2900, 18000, 102900, 180)
    SetChrPos(0x44, -2900, 18000, 102900, 180)
    Return()

    # Function_9_1451 end

    def Function_10_1959(): pass

    label("Function_10_1959")

    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    SetChrFlags(0x2A, 0x4)
    SetChrPos(0x25, 11100, 12000, 57370, 270)
    SetChrPos(0x15, 11100, 12000, 55420, 270)
    SetChrPos(0x2A, 12190, 13600, 53700, 270)
    SetChrPos(0x31, -15750, 14000, 70680, 270)
    SetChrPos(0x30, -15740, 14000, 72330, 270)
    SetChrPos(0x1E, -18510, 14000, 71980, 90)
    SetChrPos(0x1D, 28180, 12000, 86160, 270)
    SetChrPos(0x1F, 31990, 12000, 90520, 225)
    SetChrPos(0x11, 10730, 14000, 80650, 270)
    SetChrPos(0x10, -8560, 12000, 50990, 72)
    SetChrPos(0x13, 5400, 12000, 65540, 90)
    SetChrPos(0x14, 3300, 12000, 55670, 90)
    SetChrPos(0x18, 6930, 12000, 66970, 180)
    SetChrPos(0x20, -11680, 14000, 77850, 0)
    SetChrPos(0x22, -9600, 14000, 80610, 180)
    SetChrPos(0x23, -9930, 14000, 77850, 0)
    SetChrPos(0x21, -11440, 14000, 80600, 180)
    SetChrPos(0x24, -12300, 14000, 81520, 180)
    SetChrPos(0x45, -13460, 14000, 79230, 90)
    SetChrPos(0x46, -25080, 12540, 86200, 0)
    OP_51(0x46, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x488), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x46, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x488), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x46, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x488), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x2B, 4960, 12000, 59240, 0)
    SetChrPos(0x2C, -4950, 12000, 54140, 0)
    SetChrPos(0x19, -3410, 12000, 60630, 271)
    SetChrPos(0x2D, -4900, 12000, 59240, 347)
    SetChrPos(0x2E, -6590, 12000, 60600, 83)
    SetChrPos(0x2F, -4990, 12000, 62170, 180)
    SetChrPos(0x32, -7010, 12000, 66950, 180)
    SetChrPos(0x33, -5490, 12000, 65800, 270)
    SetChrPos(0x1A, -6910, 12000, 64040, 0)
    SetChrPos(0x16, 8460, 12000, 65500, 270)
    SetChrPos(0x17, 15650, 14000, 72520, 90)
    SetChrPos(0x34, 18400, 14000, 72340, 270)
    SetChrPos(0x26, 6410, 12000, 56280, 180)
    SetChrPos(0x27, 5060, 12000, 54150, 0)
    SetChrPos(0x28, 5680, 12000, 57010, 180)
    SetChrPos(0x1B, 7900, 12000, 52560, 270)
    SetChrPos(0x1C, 4980, 12000, 57050, 180)
    SetChrPos(0x3B, 4500, 12000, 69580, 270)
    SetChrPos(0x3C, 4500, 12000, 68580, 270)
    SetChrPos(0x3D, 4550, 12000, 67550, 270)
    SetChrPos(0x3E, 5740, 12000, 69730, 270)
    SetChrPos(0x3F, 5690, 12000, 68690, 270)
    SetChrPos(0x40, 5640, 12000, 67650, 270)
    OP_43(0x3D, 0x0, 0x0, 0x2)
    OP_43(0x3E, 0x0, 0x0, 0x2)
    OP_43(0x3F, 0x0, 0x0, 0x2)
    OP_43(0x40, 0x0, 0x0, 0x2)
    SetChrPos(0x35, -5470, 14000, 76850, 45)
    SetChrPos(0x36, -4230, 14000, 76860, 45)
    SetChrPos(0x37, -4780, 12000, 69830, 90)
    SetChrPos(0x38, -4780, 12000, 68730, 90)
    SetChrPos(0x39, -6010, 12000, 69770, 90)
    SetChrPos(0x3A, -6010, 12000, 68730, 90)
    SetChrPos(0x41, 2900, 18000, 102900, 180)
    SetChrPos(0x42, -2900, 18000, 102900, 180)
    SetChrPos(0x43, 3100, 14000, 82400, 180)
    SetChrPos(0x44, -3100, 14000, 82400, 180)
    Return()

    # Function_10_1959 end

    def Function_11_1E2F(): pass

    label("Function_11_1E2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FB7")
    PlayEffect(0x0, 0x0, 0xFF, 50930, 45000, 99710, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(1500)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x1, 0xFF, 60300, 35000, 90770, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(3000)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 48640, 37000, 115840, 0, 0, 0, 3500, 2000, 3500, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(1500)
    OP_82(0x2, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 55640, 42000, 100840, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(2500)
    OP_82(0x2, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 50640, 40000, 115840, 0, 0, 0, 2500, 4500, 2500, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(3000)
    OP_82(0x2, 0x2)
    Jump("Function_11_1E2F")

    label("loc_1FB7")

    Return()

    # Function_11_1E2F end

    def Function_12_1FB8(): pass

    label("Function_12_1FB8")

    OP_8C(0xFE, 225, 400)
    Sleep(300)
    OP_8E(0xFE, 0x9682, 0x3E80, 0x1333A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x712A, 0x36B0, 0x10DF6, 0x7D0, 0x0)
    SetChrPos(0xFE, 11100, 12000, 57370, 270)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_12_1FB8 end

    def Function_13_2005(): pass

    label("Function_13_2005")

    OP_8C(0xFE, 45, 400)
    Sleep(300)
    OP_8E(0xFE, 0x2E72, 0x2EE0, 0xE33A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2DAA, 0x2EE0, 0xEB28, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1144, 0x2EE0, 0xFC39, 0x7D0, 0x0)
    Return()

    # Function_13_2005 end

    def Function_14_204E(): pass

    label("Function_14_204E")


    def lambda_2054():

        label("loc_2054")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_2054")

    QueueWorkItem2(0xFE, 3, lambda_2054)
    Sleep(2500)
    OP_44(0xFE, 0x3)
    OP_8E(0xFE, 0x2B2A, 0x2EE0, 0xE614, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1144, 0x2EE0, 0xFC39, 0x7D0, 0x0)
    Return()

    # Function_14_204E end

    def Function_15_2091(): pass

    label("Function_15_2091")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2265")
    OP_22(0x183, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0xFF, 0, -12000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x1, 0xFF, 9000, -10000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0x2, 0xFF, -11000, -13000, -1560, 45, 50, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1500)
    PlayEffect(0x7, 0x3, 0xFF, 7000, -20000, -2560, 0, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x7, 0x4, 0xFF, -6000, -21000, -2560, 0, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x5, 0xFF, -9000, -10000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0x0, 0xFF, 11000, -16000, -1560, -45, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x183, 0x0, 0x64)
    Sleep(1000)
    Jump("Function_15_2091")

    label("loc_2265")

    Return()

    # Function_15_2091 end

    def Function_16_2266(): pass

    label("Function_16_2266")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    LoadEffect(0x0, "map\\mp288_00.eff")
    LoadEffect(0x1, "map\\mp288_01.eff")
    LoadEffect(0x2, "map\\mp288_02.eff")
    LoadEffect(0x3, "map\\mp288_04.eff")
    LoadEffect(0x4, "map\\mp289_00.eff")
    LoadEffect(0x5, "map\\mp289_01.eff")
    LoadEffect(0x6, "map\\mp290_00.eff")
    LoadEffect(0x7, "map\\mp293_00.eff")
    OP_4A(0x11, 255)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x102, 40040, 16000, 78780, 315)
    SetChrPos(0x11, 39300, 16000, 78000, 315)
    OP_6D(39860, 18000, 79820, 0)
    OP_67(0, 8320, -10000, 0)
    OP_6B(1920, 0)
    OP_6C(5000, 0)
    OP_6E(381, 0)
    OP_43(0x102, 0x3, 0x0, 0xF)

    def lambda_2389():
        OP_6D(39860, 16000, 79820, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2389)

    def lambda_23A1():
        OP_67(0, 6320, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23A1)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x102, 0x1)
    Sleep(2000)

    def lambda_23D2():
        OP_6B(1500, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23D2)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_44(0x102, 0x0)
    OP_44(0x102, 0x3)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "\x18\x07\x0C#40WYou see, Estelle...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Sleep(3000)
    OP_F7(0x9, 0x3, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00Side Story [The Banquet] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2543")
    Sleep(1000)
    OP_28(0x7, 0x4, 0x10)
    OP_28(0x7, 0x4, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_24C8")
    Jump("loc_2509")

    label("loc_24C8")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "\x06\x07\x05Received the recipe for \x07\x02Luxurious Lunch\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_2509")

    AddMira(3500)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "\x07\x05Received \x07\x023,500 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2543")

    OP_A2(0x2504)
    NewScene("ED6_DT21/U4204   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_16_2266 end

    def Function_17_2552(): pass

    label("Function_17_2552")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(191)
    SetChrPos(0x102, 10620, 14000, 77890, 270)
    Call(0, 10)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x25, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrFlags(0x28, 0x40)
    OP_4A(0x41, 0)
    OP_4A(0x42, 0)
    SetChrChipByIndex(0x41, 49)
    SetChrChipByIndex(0x42, 49)
    SetChrSubChip(0x41, 0)
    SetChrSubChip(0x42, 0)
    OP_4A(0x43, 0)
    OP_4A(0x44, 0)
    SetChrChipByIndex(0x43, 49)
    SetChrChipByIndex(0x44, 49)
    SetChrSubChip(0x43, 0)
    SetChrSubChip(0x44, 0)
    SetChrPos(0x25, 570, 14000, 79770, 180)
    SetChrPos(0x15, -550, 14000, 80170, 180)
    SetChrPos(0x26, 1010, 14000, 81490, 180)
    SetChrPos(0x1B, 10, 14000, 83200, 180)
    SetChrPos(0x29, -1420, 14000, 83200, 180)
    SetChrPos(0x28, 1350, 14000, 83200, 180)
    OP_4A(0x25, 0)
    OP_4A(0x15, 0)
    OP_4A(0x26, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x29, 0)
    OP_4A(0x28, 0)
    OP_8C(0x10, 0, 0)
    OP_8C(0x13, 0, 0)
    OP_8C(0x14, 0, 0)
    OP_8C(0x16, 0, 0)
    OP_8C(0x18, 0, 0)
    OP_8C(0x19, 0, 0)
    OP_8C(0x1A, 0, 0)
    OP_8C(0x2E, 0, 0)
    OP_8C(0x2F, 0, 0)
    OP_8C(0x32, 0, 0)
    OP_8C(0x33, 0, 0)
    OP_8C(0x1C, 0, 0)
    OP_8C(0x20, 90, 0)
    OP_8C(0x21, 90, 0)
    OP_8C(0x22, 90, 0)
    OP_8C(0x23, 90, 0)
    OP_8C(0x24, 90, 0)
    OP_8C(0x30, 90, 0)
    OP_8C(0x31, 90, 0)
    OP_8C(0x17, 315, 0)
    OP_8C(0x34, 315, 0)
    OP_4A(0x10, 0)
    OP_4A(0x11, 0)
    OP_4A(0x13, 0)
    OP_4A(0x14, 0)
    OP_4A(0x15, 0)
    OP_4A(0x16, 0)
    OP_4A(0x17, 0)
    OP_4A(0x18, 0)
    OP_4A(0x19, 0)
    OP_4A(0x1A, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1E, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x20, 0)
    OP_4A(0x21, 0)
    OP_4A(0x22, 0)
    OP_4A(0x23, 0)
    OP_4A(0x24, 0)
    OP_4A(0x25, 0)
    OP_4A(0x26, 0)
    OP_4A(0x27, 0)
    OP_4A(0x28, 0)
    OP_4A(0x29, 0)
    OP_4A(0x2A, 0)
    OP_4A(0x2B, 0)
    OP_4A(0x2C, 0)
    OP_4A(0x2D, 0)
    OP_4A(0x2E, 0)
    OP_4A(0x2F, 0)
    OP_4A(0x30, 0)
    OP_4A(0x31, 0)
    OP_4A(0x32, 0)
    OP_4A(0x33, 0)
    OP_4A(0x34, 0)
    OP_4A(0x35, 0)
    OP_4A(0x36, 0)
    OP_4A(0x37, 0)
    OP_4A(0x38, 0)
    OP_4A(0x39, 0)
    OP_4A(0x3A, 0)
    OP_4A(0x3B, 0)
    OP_4A(0x3C, 0)
    OP_4A(0x3D, 0)
    OP_4A(0x3E, 0)
    OP_4A(0x3F, 0)
    OP_4A(0x40, 0)
    OP_4A(0x45, 0)
    OP_4A(0x41, 0)
    OP_4A(0x42, 0)
    OP_4A(0x43, 0)
    OP_4A(0x44, 0)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    Sleep(1500)
    OP_6D(-840, 14000, 79350, 0)
    OP_67(0, 4120, -10000, 0)
    OP_6B(3210, 0)
    OP_6C(60000, 0)
    OP_6E(334, 0)

    def lambda_2839():
        OP_6D(-9700, 14000, 74820, 8000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_2839)

    def lambda_2851():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_2851)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Queen Alicia")

    AnonymousTalk(    #4 op#A op#5
        (
            "\x07\x00#40AAt one point, this very capital was placed in\x01",
            "grave danger...\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(500)
    Fade(1000)
    OP_44(0x47, 0xFF)
    OP_6D(500, 12000, 56180, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(3840, 0)
    OP_6C(36000, 0)
    OP_6E(262, 0)

    def lambda_291D():
        OP_6D(-500, 12000, 68180, 9000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_291D)

    def lambda_2935():
        OP_6C(53000, 9000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_2935)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Queen Alicia")

    AnonymousTalk(    #5 op#A op#5
        (
            "\x07\x00#50A...but thanks to the efforts of everyone here\x01",
            "and many others, all is well.\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    LoadEffect(0x0, "map\\mp032_00.eff")
    Fade(1000)
    OP_44(0x47, 0xFF)
    OP_6D(0, 14000, 83260, 0)
    OP_67(0, 2810, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(0, 0)
    OP_6E(368, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #6
        0x25,
        (
            "#094F#5PThis humble banquet is intended to be an occasion\x01",
            "to celebrate that fact, as well as to honor all those\x01",
            "who contributed to making it a reality.\x02\x03",

            "#090FIf you would, Klaudia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x15,
        "#1873F#5POf course.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2B00():
        OP_8E(0xFE, 0xFFFFFDDA, 0x36B0, 0x13542, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2B00)
    WaitChrThread(0x15, 0x1)
    Sleep(500)

    ChrTalk(    #8
        0x15,
        (
            "#1810F#5PAll those invited to today's party contributed in\x01",
            "one way or another to protecting the peace of \x01",
            "Liberl by ending the peril we were faced with.\x02\x03",

            "#1817FWhether it was extending a helping hand to those\x01",
            "in need or working to fight off the threats that\x01",
            "instilled fear in the hearts of our people.\x02\x03",

            "As this country's future monarch, I would like to \x01",
            "extend my deepest gratitude to each and every\x01",
            "one of you.\x02\x03",

            "#1818FThank you all very much.\x02\x03",

            "Holding this party is nothing compared to all that\x01",
            "you have done, but...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x35, 0x80)
    SetChrFlags(0x35, 0x40)
    SetChrPos(0x35, 9720, 14000, 76650, 270)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x40)
    SetChrPos(0x36, 8750, 14000, 77790, 270)

    ChrTalk(    #9
        0x35,
        "#1PWe JUST made it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x36,
        (
            "#1PWh-Whew... We're finally here...\x02\x03",

            "F-Food! Someone give me fooood!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DC9():
        OP_8E(0xFE, 0xFBE, 0x36B0, 0x12B6A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_2DC9)
    WaitChrThread(0x35, 0x1)
    Sleep(150)

    def lambda_2DEE():

        label("loc_2DEE")

        TurnDirection(0xFE, 0x36, 400)
        OP_48()
        Jump("loc_2DEE")

    QueueWorkItem2(0x35, 2, lambda_2DEE)
    Sleep(500)

    ChrTalk(    #11
        0x35,
        (
            "#142F#3PThe hell are you doing?! Eating can wait!\x01",
            "You've got pictures to take!\x02\x03",

            "#144FThe crown princess' speech might be finishing\x01",
            "soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x36,
        "#1P*sigh* Awwwwww, okay...\x02",
    )

    CloseMessageWindow()

    def lambda_2EB2():
        OP_8E(0xFE, 0x1388, 0x36B0, 0x12FDE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_2EB2)
    WaitChrThread(0x36, 0x1)
    OP_44(0x35, 0x2)

    def lambda_2ED6():
        OP_8C(0xFE, 315, 500)
        ExitThread()

    QueueWorkItem(0x35, 2, lambda_2ED6)
    OP_8C(0x36, 315, 500)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x36, 50)
    SetChrSubChip(0x36, 0)
    OP_0D()
    OP_43(0x36, 0x1, 0x0, 0x8)
    Sleep(2000)

    ChrTalk(    #13
        0x15,
        (
            "#1815F#5P...Erm...\x02\x03",

            "Well, I do hope you will all enjoy your time \x01",
            "here all the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x26,
        (
            "#225F#5PI'm sure you are all busy men and women, burdened\x01",
            "by a great many responsibilities and concerns...\x02\x03",

            "#220F...but today, I would ask that you all cast those\x01",
            "aside in order to rest, relax, and enjoy yourselves.\x02\x03",

            "The food on offer here is some of the finest in\x01",
            "Liberl, so by all means, partake until you can no\x01",
            "more!\x02\x03",

            "#221FAnd may the Goddess bless this nation!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xBF, 0x0, 0x64)
    OP_20(0x7D0)
    Sleep(2000)
    OP_21()
    OP_44(0x36, 0x1)
    FadeToBright(100, 16777215)
    OP_1D(0x4B)
    Sleep(500)

    def lambda_30FD():

        label("loc_30FD")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_30FD")

    QueueWorkItem2(0x36, 2, lambda_30FD)

    def lambda_310E():

        label("loc_310E")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_310E")

    QueueWorkItem2(0x35, 2, lambda_310E)

    def lambda_311F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_311F)
    Sleep(100)

    def lambda_313F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_313F)
    Sleep(100)

    def lambda_315F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_315F)
    Sleep(100)

    def lambda_317F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_317F)
    Sleep(100)

    def lambda_319F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_319F)
    Sleep(100)

    def lambda_31BF():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_31BF)
    Sleep(3000)
    Fade(1000)
    OP_6D(12000, 14000, 80820, 0)
    OP_67(0, 4830, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    OP_44(0x25, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x29, 0x1)
    OP_44(0x28, 0x1)
    OP_44(0x36, 0x1)
    OP_44(0x36, 0x2)
    OP_44(0x35, 0x2)
    OP_4B(0x25, 0)
    OP_4B(0x15, 0)
    OP_4B(0x26, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x29, 0)
    OP_4B(0x28, 0)
    SetChrChipByIndex(0x36, 43)
    SetChrSubChip(0x36, 0)
    OP_4B(0x41, 0)
    OP_4B(0x42, 0)
    SetChrChipByIndex(0x41, 48)
    SetChrChipByIndex(0x42, 48)
    SetChrSubChip(0x41, 0)
    SetChrSubChip(0x42, 0)
    OP_4B(0x43, 0)
    OP_4B(0x44, 0)
    SetChrChipByIndex(0x43, 48)
    SetChrChipByIndex(0x44, 48)
    SetChrSubChip(0x43, 0)
    SetChrSubChip(0x44, 0)
    ClearChrFlags(0x25, 0x40)
    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x26, 0x40)
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x29, 0x40)
    ClearChrFlags(0x28, 0x40)
    Call(0, 9)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_72(0x405, 0x0)
    ExitThread()
    OP_4A(0x3D, 0)
    OP_4A(0x3E, 0)
    OP_4A(0x3F, 0)
    OP_4A(0x40, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #15
        0x11,
        (
            "#1017F#5PKloe really is something else, huh?\x02\x03",

            "I'm not sure I could dress super nice,\x01",
            "get up in front of a crowd like this, and\x01",
            "make a big speech the way she just did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1053F#11PYeah, she is. She said she wasn't feeling\x01",
            "confident about how she'd do as crown\x01",
            "princess before...\x02\x03",

            "#1041F...but from where I'm standing, she's doing\x01",
            "just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#1008F#5PSeeing her is making me kinda jealous, though.\x02\x03",

            "#1016FI wish I could pull off fancy dresses the way\x01",
            "she does...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x11, 400)
    Sleep(300)

    ChrTalk(    #18
        0x102,
        "#1044F#12P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #19
        0x11,
        "#1019F#5PYou got somethin' to say, mister?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1053F#12POh, it's nothing.\x02\x03",

            "#1041FYou're just not all that girly most of the time,\x01",
            "so it always takes me by surprise when you\x01",
            "suddenly are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        (
            "#1013F#5PWhat do you mean, I'm not girly?!\x02\x03",

            "#1007FSure, lately we've been so busy with helping\x01",
            "get Liberl back in shape so I haven't even had\x01",
            "time to go back home...\x02\x03",

            "#1019F...but that doesn't mean I don't wanna wear\x01",
            "a pretty dress or something once in a while,\x01",
            "you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1049F#12PI know, I know.\x02\x03",

            "#1054FStill, it really is surprising just how much\x01",
            "you've grown even in these past few weeks.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x11,
        "#1004F#5P...I have?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#1053F#12PWell, it's been pretty tough running up and\x01",
            "down the country so much, but you've kept\x01",
            "up with ease.\x02\x03",

            "And your judgments as a bracer are getting\x01",
            "more spot on with every decision you make.\x02\x03",

            "#1041FFancy dress or not, I think you're a pretty\x01",
            "wonderful person, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#1008F#5PA-Ahaha...\x02\x03",

            "#1016FI don't know why, but it's weird hearing you pile\x01",
            "on the compliments so much...\x02\x03",

            "#1017FBut what can I say? I'm glad that things seem\x01",
            "to have finally calmed down a bit on the work\x01",
            "front these past few days.\x02\x03",

            "The capital might not be entirely the way it was,\x01",
            "but it's getting there.\x02\x03",

            "I think we can finally afford to take a breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1053F#12P...Yeah.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x11, 225, 500)
    Sleep(300)

    ChrTalk(    #27
        0x11,
        "#1004F#5POh, look!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_3A72():
        OP_8C(0x102, 225, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A72)
    SetChrPos(0x39, -9350, 12000, 61660, 180)
    SetChrPos(0x2E, -3880, 12000, 59720, 315)
    SetChrPos(0x2F, -3900, 12000, 61790, 225)
    SetChrPos(0x1A, -8100, 12000, 57040, 270)
    SetChrPos(0x19, -8100, 12000, 58540, 270)

    def lambda_3AD5():
        OP_6D(-7020, 12000, 59000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_3AD5)

    def lambda_3AED():
        OP_6C(40000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_3AED)

    def lambda_3AFD():
        OP_6B(2720, 2500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_3AFD)

    def lambda_3B0D():
        OP_67(0, 6700, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_3B0D)
    WaitChrThread(0x47, 0x0)
    Sleep(500)

    ChrTalk(    #28
        0x11,
        "#1008F#6PLook at all that food!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1040F#12PThe chefs in the castle supposedly made\x01",
            "the entire spread, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(800)
    OP_6D(12000, 14000, 80820, 0)
    OP_67(0, 4830, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x11,
        (
            "#1006F#5PThere's no way I'm missing out on this!\x02\x03",

            "I didn't get to enjoy the food back during\x01",
            "the birthday festivities, so now's my time\x01",
            "to pig out big time!\x02\x03",

            "#1001FHeehee! I'm gonna eat until I barf!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(400)

    ChrTalk(    #31
        0x11,
        (
            "#1018F#5PStay right here, okay, Joshua? I'm gonna\x01",
            "go scope out the goods!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D14():

        label("loc_3D14")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_3D14")

    QueueWorkItem2(0x102, 1, lambda_3D14)
    OP_8C(0x11, 270, 400)
    Sleep(300)
    OP_43(0x11, 0x1, 0x0, 0x7)

    def lambda_3D38():
        OP_6D(7900, 14000, 79710, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_3D38)

    def lambda_3D50():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_3D50)
    WaitChrThread(0x47, 0x0)
    Sleep(3000)
    OP_44(0x102, 0x1)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_6D(11610, 14000, 78880, 1500)
    OP_44(0x11, 0x1)
    SetChrPos(0x39, -8189, 12000, 60260, 180)
    SetChrPos(0x2E, -5950, 12000, 59520, 225)
    SetChrPos(0x2F, -6530, 12000, 60440, 225)
    SetChrPos(0x1A, -8100, 12000, 57040, 0)
    SetChrPos(0x19, -5220, 12000, 57140, 270)
    SetChrPos(0x11, -8100, 12000, 58540, 180)
    SetChrSubChip(0x11, 0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #32
        0x102,
        (
            "#1054F#5P...She might have grown in some areas,\x01",
            "but she's still got a ways to go in others.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x35, 800, 14000, 77890, 90)
    SetChrPos(0x36, 800, 14000, 78900, 90)

    def lambda_3E90():
        OP_8E(0xFE, 0x221A, 0x36B0, 0x13042, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_3E90)
    Sleep(600)

    def lambda_3EB0():
        OP_8E(0xFE, 0x17D4, 0x36B0, 0x13434, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_3EB0)
    Sleep(1000)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3EE7():

        label("loc_3EE7")

        TurnDirection(0xFE, 0x35, 400)
        OP_48()
        Jump("loc_3EE7")

    QueueWorkItem2(0x102, 2, lambda_3EE7)
    WaitChrThread(0x35, 0x1)

    ChrTalk(    #33
        0x35,
        (
            "#141F#6PHey, look! How you doin', Joshua?\x02\x03",

            "Estelle not here with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#1053F#11PShe just went to get food a second ago,\x01",
            "actually.\x02\x03",

            "#1040FAre you two here more for work than fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x35,
        (
            "#147F#6PBingo. There aren't many occasions where this\x01",
            "many famous faces are gathered in one place.\x02\x03",

            "There was no way we could pass up the chance\x01",
            "to come and score some interviews!\x02\x03",

            "#141FDon't think you're getting out of here without \x01",
            "answering some questions, either. We'll get to\x01",
            "you two later.\x02\x03",

            "So no going home until you've spoken to us, all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#1054F#11PHaha... All right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x35,
        "#147F#6PGreat! Next up is the crown princess!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x35, 0x36, 500)
    Sleep(300)

    ChrTalk(    #38
        0x35,
        "#144F#11PHop to it, Dorothy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x36,
        "#154F#6P#40WI-I can't go on... I need something to eat...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    OP_9E(0x36, 0x14, 0x0, 0x190, 0x9C4)
    Sleep(800)

    ChrTalk(    #40
        0x36,
        "#152F#6P#40WLet me have something to eat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x35,
        (
            "#144F#11PNot until we're done! Questions to ask,\x01",
            "photos to take!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x35, 0x3, 0x0, 0x12)

    def lambda_4285():

        label("loc_4285")

        TurnDirection(0xFE, 0x35, 1000)
        OP_48()
        Jump("loc_4285")

    QueueWorkItem2(0x36, 2, lambda_4285)
    Sleep(200)
    OP_62(0x36, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)
    OP_44(0x36, 0x2)

    ChrTalk(    #42 op#A op#5
        0x36,
        "#152F#5P#30AWhy are you so meeeeeeeeean?\x05\x02",
    )

    CloseMessageWindow()
    OP_43(0x36, 0x3, 0x0, 0x13)
    WaitChrThread(0x36, 0x3)

    ChrTalk(    #43
        0x102,
        (
            "#1053F#5PHaha... He's even more fired up today than usual.\x02\x03",

            "#1044FI wonder how Estelle's doing?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x36, 0x3)
    OP_44(0x102, 0x2)
    ClearChrFlags(0x35, 0x40)
    ClearChrFlags(0x36, 0x40)
    OP_4B(0x35, 0)
    OP_4B(0x36, 0)
    SetChrPos(0x35, 12210, 12000, 57070, 270)
    SetChrPos(0x36, 6500, 12000, 60670, 270)

    def lambda_4393():
        OP_6D(-7020, 12000, 59000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_4393)

    def lambda_43AB():
        OP_6C(40000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_43AB)

    def lambda_43BB():
        OP_6B(2720, 2500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_43BB)

    def lambda_43CB():
        OP_67(0, 6700, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_43CB)
    WaitChrThread(0x47, 0x0)
    OP_62(0x1A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    def lambda_43FF():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_43FF)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    def lambda_4439():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4439)
    Sleep(1000)
    OP_62(0x1A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    def lambda_4473():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4473)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    def lambda_44AD():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_44AD)
    Sleep(2000)
    Fade(800)
    OP_6D(11640, 14000, 79050, 0)
    OP_67(0, 4830, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #44
        0x102,
        (
            "#1052F#5P*sigh* So much for scoping out the food...\x02\x03",

            "#1043F...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFFFF)
    Sleep(500)
    OP_8C(0x102, 270, 300)
    Sleep(400)

    ChrTalk(    #45
        0x102,
        (
            "#1035F#11P(I suppose this is as good a chance as any.)\x02\x03",

            "(I owe a lot to the people here on a personal\x01",
            "level, too.)\x02\x03",

            "#1041F(Maybe I should go around and thank them while\x01",
            "I have the chance.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(10620, 14000, 77890, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4B(0x10, 0)
    OP_4B(0x11, 0)
    OP_4B(0x13, 0)
    OP_4B(0x14, 0)
    OP_4B(0x15, 0)
    OP_4B(0x16, 0)
    OP_4B(0x17, 0)
    OP_4B(0x18, 0)
    OP_4B(0x19, 0)
    OP_4B(0x1A, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1D, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x1F, 0)
    OP_4B(0x20, 0)
    OP_4B(0x21, 0)
    OP_4B(0x22, 0)
    OP_4B(0x23, 0)
    OP_4B(0x24, 0)
    OP_4B(0x25, 0)
    OP_4B(0x26, 0)
    OP_4B(0x27, 0)
    OP_4B(0x28, 0)
    OP_4B(0x29, 0)
    OP_4B(0x2A, 0)
    OP_4B(0x2B, 0)
    OP_4B(0x2C, 0)
    OP_4B(0x2D, 0)
    OP_4B(0x2E, 0)
    OP_4B(0x2F, 0)
    OP_4B(0x30, 0)
    OP_4B(0x31, 0)
    OP_4B(0x32, 0)
    OP_4B(0x33, 0)
    OP_4B(0x34, 0)
    OP_4B(0x35, 0)
    OP_4B(0x36, 0)
    OP_4B(0x37, 0)
    OP_4B(0x38, 0)
    OP_4B(0x39, 0)
    OP_4B(0x3A, 0)
    OP_4B(0x3B, 0)
    OP_4B(0x3C, 0)
    OP_4B(0x3D, 0)
    OP_4B(0x3E, 0)
    OP_4B(0x3F, 0)
    OP_4B(0x40, 0)
    OP_4B(0x45, 0)
    OP_4B(0x41, 0)
    OP_4B(0x42, 0)
    OP_4B(0x43, 0)
    OP_4B(0x44, 0)
    OP_4B(0x3D, 0)
    OP_4B(0x3F, 0)
    OP_4B(0x3E, 0)
    OP_4B(0x40, 0)
    OP_A2(0x2F9A)
    EventEnd(0x0)
    Return()

    # Function_17_2552 end

    def Function_18_4774(): pass

    label("Function_18_4774")

    OP_8C(0x35, 270, 500)

    def lambda_4781():
        OP_8E(0xFE, 0xC6C, 0x36B0, 0x13042, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_4781)
    WaitChrThread(0x35, 0x1)

    def lambda_47A1():
        OP_8E(0xFE, 0xC6C, 0x2EE0, 0x10194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_47A1)
    WaitChrThread(0x35, 0x1)
    Return()

    # Function_18_4774 end

    def Function_19_47BC(): pass

    label("Function_19_47BC")


    def lambda_47C2():
        OP_8E(0xFE, 0xC6C, 0x36B0, 0x129A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_47C2)
    WaitChrThread(0x36, 0x1)

    def lambda_47E2():
        OP_8E(0xFE, 0xC6C, 0x36B0, 0x11170, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_47E2)
    WaitChrThread(0x36, 0x1)
    Return()

    # Function_19_47BC end

    def Function_20_47FD(): pass

    label("Function_20_47FD")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    OP_6D(-130, 14000, 78620, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x41, 0x80)
    SetChrFlags(0x42, 0x80)
    SetChrPos(0x102, -130, 14000, 78620, 0)
    OP_4A(0x40, 255)
    SetChrPos(0x40, -13960, 14000, 73930, 90)
    Sleep(1000)
    FadeToBright(2000, 0)

    def lambda_4893():
        OP_6D(500, 14000, 82000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4893)
    OP_8E(0x102, 0x0, 0x36B0, 0x13E20, 0x5DC, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #46
        0x102,
        (
            "#1053F#6P...Okay, I think that's about everyone now.\x02\x03",

            "There were a few people I didn't get to talk\x01",
            "to, though, so hopefully I can make another\x01",
            "round of the party later once they're free.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x35, 255)
    SetChrPos(0x35, -1780, 12000, 70020, 0)
    SetChrFlags(0x35, 0x40)

    def lambda_499F():
        OP_6D(500, 14000, 78700, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_499F)

    def lambda_49B7():
        OP_8E(0xFE, 0xFFFFF90C, 0x36B0, 0x12EBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_49B7)
    WaitChrThread(0x35, 0x1)
    OP_8C(0x35, 270, 400)
    Sleep(300)
    OP_62(0x35, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #47
        0x35,
        (
            "#141F#11POh, here we go!\x02\x03",

            "Come on, Dorothy! We're talking to the military\x01",
            "guys next!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A54():

        label("loc_4A54")

        TurnDirection(0xFE, 0x35, 500)
        OP_48()
        Jump("loc_4A54")

    QueueWorkItem2(0x102, 2, lambda_4A54)
    OP_4A(0x36, 255)
    SetChrFlags(0x36, 0x40)
    SetChrPos(0x36, -840, 12000, 70900, 0)

    def lambda_4A7F():

        label("loc_4A7F")

        TurnDirection(0xFE, 0x36, 500)
        OP_48()
        Jump("loc_4A7F")

    QueueWorkItem2(0x35, 2, lambda_4A7F)
    Sleep(300)

    ChrTalk(    #48
        0x35,
        "#144F#5PGet a move on, woman! We haven't got all day!\x02",
    )

    CloseMessageWindow()

    def lambda_4AD0():
        OP_8E(0xFE, 0xFFFFFCB8, 0x36B0, 0x12AFC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_4AD0)
    WaitChrThread(0x36, 0x1)
    OP_8C(0x36, 315, 400)
    Sleep(500)

    ChrTalk(    #49
        0x36,
        (
            "#154F#11P#40WNiiiiiial...\x02\x03",

            "I don't feel too goooood...\x02\x03",

            "#152FMy stomach feels like a giant bottle of water...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x35,
        (
            "#145F#5PThat's what happens when you drink way too\x01",
            "much in a short period of time, you idiot.\x02\x03",

            "#142FBut never mind that! We've got work to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x36,
        "#154F#11PO-Okay...\x02",
    )

    CloseMessageWindow()
    OP_62(0x36, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_44(0x35, 0x2)
    OP_8C(0x35, 270, 500)

    def lambda_4C38():
        OP_8E(0xFE, 0xFFFFDCD8, 0x36B0, 0x12EBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_4C38)
    Sleep(500)

    def lambda_4C58():
        OP_8E(0xFE, 0xFFFFF90C, 0x36B0, 0x12EBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_4C58)
    WaitChrThread(0x36, 0x1)

    def lambda_4C78():
        OP_8E(0xFE, 0xFFFFDCD8, 0x36B0, 0x12EBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_4C78)

    def lambda_4C93():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x2EE)
        ExitThread()

    QueueWorkItem(0x35, 0, lambda_4C93)
    Sleep(1000)

    def lambda_4CAA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_4CAA)
    OP_44(0x102, 0x2)
    OP_8C(0x102, 270, 400)
    WaitChrThread(0x36, 0x1)
    OP_63(0x36)
    OP_4A(0x15, 255)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 0, 12000, 70340, 0)

    NpcTalk(    #52
        0x15,
        "Girl's Voice",
        "#1P...Joshua?\x02",
    )

    CloseMessageWindow()

    def lambda_4D09():
        OP_8E(0xFE, 0x0, 0x36B0, 0x13650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4D09)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4D3B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D3B)

    def lambda_4D49():
        OP_6D(1250, 14000, 81260, 4000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_4D49)

    def lambda_4D61():
        OP_67(0, 5540, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_4D61)

    def lambda_4D79():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_4D79)

    def lambda_4D89():
        OP_6C(55000, 4000)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_4D89)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x47, 0x0)

    ChrTalk(    #53
        0x102,
        (
            "#1054F#5PHey, Kloe. Finally got a bit of a break? It must \x01",
            "be exhausting having to do one interview after\x01",
            "another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x15,
        (
            "#1814F#12PWell...\x02\x03",

            "#1815FHeehee. I suppose it is a little.\x02\x03",

            "#1872FNot too bad, though. I've had to do a lot more\x01",
            "of them ever since becoming crown princess,\x01",
            "so I'm starting to get used to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#1053F#5PI can believe it.\x02\x03",

            "#1041FIt feels like I've been seeing your face in all\x01",
            "kinds of papers and magazines lately.\x02\x03",

            "I think anyone would learn to adjust after a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x15,
        "#1815F#12PWell, you know...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#1053F#5PIt probably won't be too long before it starts to\x01",
            "die down, so just hang in there.\x02\x03",

            "#1040FAll you can really do is grin and bear it until then,\x01",
            "unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x15,
        (
            "#1873F#12P...Yes, I know.\x02\x03",

            "#1810FThat's exactly what I intend to do, too. I swore\x01",
            "to myself that I would do all I could to help and\x01",
            "protect this country's people.\x02\x03",

            "Accepting a few interviews here and there is\x01",
            "the easy part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#1035F#5PWell, if you say so...\x02\x03",

            "#1054F...Haha. You really are strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x15,
        (
            "#1815F#12PI'm not so sure about that.\x02\x03",

            "I still feel as if I'm doubting myself a lot of the time.\x02\x03",

            "Like I just have to keep going out of my comfort\x01",
            "zone, feeling reckless with every push...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#1053F#5PMaybe so.\x02\x03",

            "Still doesn't change the fact that you're strong.\x01",
            "Not to me, anyway.\x02\x03",

            "#1041FI remember the strength you showed trying to\x01",
            "protect Clem when we first met, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x15,
        (
            "#1815F#12PA-Ahaha... Thank you.\x02\x03",

            "#1870FI-I nearly forgot about that.\x02\x03",

            "...\x02\x03",

            "#1873F(...Maybe now would be the best time after all?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x102,
        "#1040F#5PSomething on your mind, Kloe?\x02",
    )

    CloseMessageWindow()
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #64
        0x15,
        "Kloe",
        (
            "#1817F#12P...Umm...\x02\x03",

            "#1812FCould I have a little of your time, Joshua?\x02\x03",

            "I've got something I want to say to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1044F#5PU-Umm...\x02\x03",

            "Sure? Okay...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #66
        0x15,
        "Kloe",
        "#1817F#12PThis way, then...\x02",
    )

    CloseMessageWindow()

    def lambda_54C1():

        label("loc_54C1")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_54C1")

    QueueWorkItem2(0x102, 2, lambda_54C1)
    OP_8C(0x15, 90, 300)
    Sleep(300)

    def lambda_54DE():
        OP_6D(4320, 14000, 81910, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_54DE)
    OP_43(0x15, 0x0, 0x0, 0x18)
    Sleep(2000)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x47, 0x0)
    Sleep(2000)

    def lambda_551E():
        OP_6D(890, 14000, 82020, 2500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_551E)
    WaitChrThread(0x47, 0x0)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #67
        0x102,
        (
            "#1043F(Is it just me, or does she seem kind of bothered\x01",
            "by something?)\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x2)
    OP_8C(0x102, 225, 400)
    Sleep(300)

    ChrTalk(    #68
        0x102,
        "#1044F#5P(Where's Estelle right now, anyway?)\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_4A(0x11, 0)
    OP_4A(0x1A, 0)
    OP_4A(0x33, 0)
    OP_4A(0x32, 0)
    OP_4A(0x2F, 0)
    OP_4A(0x2E, 0)
    OP_4A(0x19, 0)
    OP_4A(0x39, 0)
    SetChrPos(0x33, -5960, 12000, 58200, 270)
    SetChrPos(0x32, -7250, 12000, 55970, 315)
    OP_8C(0x11, 270, 0)
    OP_8C(0x1A, 270, 0)
    Fade(1000)
    OP_6D(-7020, 12000, 59000, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(40000, 0)
    OP_6E(285, 0)
    OP_43(0x11, 0x3, 0x0, 0x15)
    Sleep(500)
    OP_43(0x1A, 0x3, 0x0, 0x16)
    OP_0D()

    ChrTalk(    #69
        0x1A,
        "#11P*chomp* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        "#5P*munch* *chew*\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x3)

    ChrTalk(    #71
        0x11,
        "#5P#1005F#3SI got stomachs to spare!#2S\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x11, 0x3, 0x0, 0x15)

    ChrTalk(    #72
        0x33,
        (
            "#202FOh, she's picking up her pace! This could get\x01",
            "interesting!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x1A, 0x3)
    TurnDirection(0x1A, 0x33, 1000)
    Sleep(500)

    ChrTalk(    #73
        0x1A,
        "#1564F#6PWh-Whose side are you on, anyway?!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6D(1300, 14000, 82260, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x102,
        (
            "#1052F#5P(I guess I can just leave her as she is for now.\x01",
            "She seems pretty...occupied.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #75
        0x102,
        (
            "#1043F#6P(I should go and see what Kloe wants, then.)\x02\x03",

            "(Have I done something to make her angry,\x01",
            "though? I don't feel like I have...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58DF():
        OP_8E(0xFE, 0x19C8, 0x36B0, 0x13E20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58DF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(31990, 14000, 73090, 0)
    OP_67(0, 7190, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(45000, 0)
    OP_6E(368, 0)
    OP_22(0x1CC, 0x1, 0x46)
    OP_44(0x102, 0xFF)
    SetChrPos(0x15, 42860, 16000, 80150, 90)
    SetChrPos(0x102, 30240, 14000, 70320, 45)
    OP_43(0x102, 0x0, 0x0, 0x17)
    FadeToBright(2000, 0)

    def lambda_597D():
        OP_6D(45090, 14000, 82890, 7000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_597D)
    Sleep(5000)
    OP_20(0x1388)
    WaitChrThread(0x47, 0x0)

    def lambda_59A4():
        OP_6D(43080, 16000, 80470, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_59A4)

    def lambda_59BC():
        OP_67(0, 6450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_59BC)

    def lambda_59D4():
        OP_6B(2090, 3000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_59D4)

    def lambda_59E4():
        OP_6E(332, 3000)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_59E4)
    WaitChrThread(0x47, 0x0)
    WaitChrThread(0x102, 0x0)
    Sleep(500)

    ChrTalk(    #76
        0x102,
        (
            "#1043F#6PSo, Kloe?\x02\x03",

            "#1040FWhat was it that you wanted to tell me?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0x15,
        "Kloe",
        "#1817F#5P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#1052F#6PL-Look...\x02\x03",

            "#1043FIf I've done something to offend you,\x01",
            "I'm sorry, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #79
        0x15,
        "Kloe",
        "#1870F#5P...I...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)

    def lambda_5B01():
        OP_6D(42650, 16000, 80970, 1500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_5B01)

    def lambda_5B19():
        OP_67(0, 6460, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_5B19)

    def lambda_5B31():
        OP_6B(1900, 1500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_5B31)

    def lambda_5B41():
        OP_6C(21000, 1500)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_5B41)

    def lambda_5B51():
        OP_6E(385, 1500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5B51)
    OP_8C(0x15, 250, 300)
    WaitChrThread(0x47, 0x0)
    Sleep(500)

    NpcTalk(    #80
        0x15,
        "Kloe",
        "#1812F#11PI love you, Joshua.\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFFFF)
    Sleep(500)

    ChrTalk(    #81
        0x102,
        "#1044F#6P#3S...What?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    OP_1D(0x75)
    Sleep(1000)

    NpcTalk(    #82
        0x15,
        "Kloe",
        "#1810F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        "#1042F#6PU-Umm...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x15,
        "Kloe",
        "#1812F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        "#1054F#6P#40WI... Well...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #86
        0x15,
        "Kloe",
        "#1817F#11P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #87
        0x102,
        (
            "#1052F#6P#40WI-I'm sorry...\x02\x03",

            "#1056FI'm happy you feel that way, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #88
        0x15,
        "Kloe",
        (
            "#1873F#11PHeehee...\x02\x03",

            "Don't worry. I knew exactly how you were\x01",
            "going to respond before I said anything.\x02\x03",

            "#1818FI just felt like I had to get that out before\x01",
            "I could really start moving on.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 60, 400)
    Sleep(500)

    NpcTalk(    #89
        0x15,
        "Kloe",
        "#1872F#5PThe sky sure is beautiful tonight, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        "#1044F#6PUmm... I...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #91
        0x102,
        "#1043F#6P#40WHow long have you, well...felt that way?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #92
        0x15,
        "Kloe",
        (
            "#1817F#5P...Say, Joshua?\x02\x03",

            "If you had met me before Estelle...\x02\x03",

            "#1819F...do you think you would have...well...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #93
        0x102,
        (
            "#1035F#6PNo.\x02\x03",

            "I'm pretty sure that never\x01",
            "would have happened.\x02\x03",

            "#1043FSorry.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #94
        0x15,
        "Kloe",
        (
            "#1815F#5PI told you! Don't worry.\x02\x03",

            "#1872FI can't deny there's a part of me that\x01",
            "wants to keep you all to myself...\x02\x03",

            "...but even if that were possible, I don't\x01",
            "think it would be what I truly wanted.\x02\x03",

            "#1873FBecause when it comes down to it...\x02\x03",

            "#1818F...I really love both you and Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 250, 400)
    Sleep(300)

    NpcTalk(    #95
        0x15,
        "Kloe",
        (
            "#1872F#11PThat's partly why I wanted to see that\x01",
            "troubled face of yours one last time.\x02\x03",

            "#1815FIt was worth the effort to bring out, too.\x02\x03",

            "#1818FThat was probably the best expression\x01",
            "I've seen to date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#1044F#6PI...\x02\x03",

            "#1052FUmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #97
        0x102,
        (
            "#1048F#6P...You can be kind of a bully sometimes,\x01",
            "you know that?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #98
        0x15,
        "Kloe",
        (
            "#1815F#11PMaybe. This feels like the most fun\x01",
            "I've had in some time.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6223():
        OP_6D(42000, 16000, 80640, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_6223)

    def lambda_623B():
        OP_67(0, 6930, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_623B)

    def lambda_6253():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_6253)

    def lambda_6263():
        OP_8E(0xFE, 0xA08C, 0x3E80, 0x13A56, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6263)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x47, 0x0)
    Sleep(500)

    NpcTalk(    #99
        0x15,
        "Kloe",
        (
            "#1817F#5PSooo...\x02\x03",

            "#1812F...what's on YOUR mind, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 0, 500)
    Sleep(300)

    ChrTalk(    #100
        0x102,
        "#1044F#12P#3SWhat?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 180, 400)
    Sleep(300)

    NpcTalk(    #101
        0x15,
        "Kloe",
        (
            "#1815F#5PHeehee. I can easily tell you're worried\x01",
            "about something.\x02\x03",

            "My instincts are quite sharp, or so I'd like\x01",
            "to believe. Besides...\x02\x03",

            "#1870F...I was watching you the whole time I was \x01",
            "handling that interview earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#1056F#12P...O-Oh...\x02\x03",

            "#1052FHow exactly am I supposed to take that?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #103
        0x15,
        "Kloe",
        "#1815F#5PA-Ahaha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #104
        0x15,
        "Kloe",
        (
            "#1817F#5PStill, you're hiding something, aren't you?\x02\x03",

            "#1812FAre you planning on doing something all\x01",
            "on your own again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#1043F#12P...\x02\x03",

            "#1052F*sigh* Your instincts are sharp, all right...\x02\x03",

            "#1054FEstelle surprises me from time to time,\x01",
            "too, but you're definitely up there.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #106
        0x15,
        "Kloe",
        (
            "#1873F#5PWell, that's just how us girls are.\x02\x03",

            "#1812FSo, come on. Tell me what's troubling you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #107
        0x102,
        (
            "#1035F#12PIt's nothing that major, really.\x02\x03",

            "#1040FI intend to leave Liberl by the end\x01",
            "of the month.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #108
        0x15,
        "Kloe",
        (
            "#1814F#5PB-But why?!\x02\x03",

            "#1813FThe country is finally at peace now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#1053F#12PThat's exactly why I think this is the right time.\x02\x03",

            "Ouroboros seems to have completely withdrawn\x01",
            "from the country, and the restoration efforts are\x01",
            "coming along smoothly.\x02\x03",

            "#1041FSo maybe it's about time for me to leave on a\x01",
            "journey of my own.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x2)
    OP_8C(0x102, 90, 400)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    def lambda_6815():
        OP_6B(1800, 30000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_6815)

    ChrTalk(    #110
        0x102,
        (
            "#1053F#6PIt's taken me a long time to get this far...\x02\x03",

            "...but I've finally been able to start thinking of\x01",
            "myself as a person and not some kind of broken\x01",
            "doll.\x02\x03",

            "I was finally able to achieve the very thing\x01",
            "everyone wanted for me.\x02\x03",

            "#1043F...That's been both a good thing and a bad thing.\x01",
            "Good in that I finally feel human, bad in that my\x01",
            "heart's been aching in a way it never did before.\x02\x03",

            "Broken dolls can easily look away from all the\x01",
            "terrible things they've done...but I can't do that\x01",
            "anymore.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #111
        0x15,
        "Kloe",
        "#1813F#5P...Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#1053F#6PThat's why I need to go on this journey around\x01",
            "the continent.\x02\x03",

            "So I can work towards atoning for all that I've\x01",
            "done...\x02\x03",

            "#1041FSo I can start embracing the person I now am,\x01",
            "in the truest sense of the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #113
        0x15,
        "Kloe",
        (
            "#1819F#5PI...see...\x02\x03",

            "#1813FBut if you do that, that means you won't be\x01",
            "able to see Estelle for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        (
            "#1043F#6PYeah... I know.\x02\x03",

            "#1035FIt might not even be for a while--it could\x01",
            "be a long time.\x02\x03",

            "I'm still not sure how to break that to her,\x01",
            "either... That's the part that's on my mind\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #115
        0x15,
        "Kloe",
        (
            "#1817F#5P*sigh*\x02\x03",

            "#1810FYou've still got a lot of growing up to do,\x01",
            "young man.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 0, 400)

    ChrTalk(    #116
        0x102,
        "#1044F#12P...Huh?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #117
        0x15,
        "Kloe",
        (
            "#1812F#5PIf you ask me, you should just tell her in the way\x01",
            "that comes most naturally to you.\x02\x03",

            "You don't have to write some big speech in your\x01",
            "head in advance; speak to her from your heart.\x01",
            "You believe in her, don't you?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #118
        0x15,
        "Kloe",
        (
            "#1816F#5P#3SNo matter how you phrase it, she'll understand.\x01",
            "All you have to do is get those words out there!\x02",
        )
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x96)
    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#1044F#12P#40W...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #120
        0x15,
        "Kloe",
        (
            "#1873F#5PYou owe that much to her if you love her.\x02\x01",

            "#1818FYou know that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        "#1043F#12P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #122
        0x102,
        (
            "#1053F#12PYeah, I do.\x02\x03",

            "I really am hopeless, aren't I?\x02\x03",

            "#1054FYou shouldn't have to tell me something\x01",
            "that obvious.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #123
        0x15,
        "Kloe",
        (
            "#1815F#5PYou wouldn't be you if I didn't have\x01",
            "to tell you.\x02\x03",

            "#1870FPlus, that kind of thing's part of why\x01",
            "I love you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#1056F#12P...\x02\x01",

            "#1048FPlease stop teasing me...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #125
        0x15,
        "Kloe",
        (
            "#1818F#5PTeehee.\x02\x03",

            "#1873FJust remember: it'll be okay. If anyone knows you,\x01",
            "it's Estelle.\x02\x03",

            "#1873FAlthough if you ask me, she'll...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrPos(0x11, 21600, 14000, 70600, 90)
    OP_44(0x11, 0xFF)

    NpcTalk(    #126
        0x11,
        "Energetic Voice",
        "Joshuaaa! Where are you?\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x11, 0x4)

    def lambda_7166():

        label("loc_7166")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_7166")

    QueueWorkItem2(0x102, 2, lambda_7166)

    def lambda_7177():

        label("loc_7177")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_7177")

    QueueWorkItem2(0x15, 2, lambda_7177)

    def lambda_7188():
        OP_6D(31740, 14500, 71820, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_7188)
    Sleep(1000)

    def lambda_71A5():
        OP_8E(0xFE, 0x7724, 0x36B0, 0x113C8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_71A5)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x47, 0x0)
    OP_8C(0x11, 45, 500)
    SetChrPos(0x15, 40010, 16000, 80500, 225)
    SetChrPos(0x102, 40620, 16000, 79280, 225)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #127
        0x11,
        (
            "#1001FOh, there you are!\x02\x03",

            "#1018FLook at these! They're Josette's goggles!\x02\x03",

            "#1029FHeheh. I took them from her as spoils of war!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_728E():
        OP_6D(39340, 16000, 80650, 2500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_728E)

    def lambda_72A6():
        OP_67(0, 6320, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_72A6)

    def lambda_72BE():
        OP_6B(1920, 2500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_72BE)

    def lambda_72CE():
        OP_6C(353000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_72CE)

    def lambda_72DE():
        OP_6E(375, 2500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_72DE)

    def lambda_72EE():
        OP_8E(0xFE, 0x961E, 0x3E80, 0x12E8A, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_72EE)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x47, 0x0)
    OP_44(0x102, 0x2)
    OP_44(0x15, 0x2)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #128
        0x15,
        "Kloe",
        (
            "#1872F#5PUmm...\x02\x03",

            "#1815FI'm...glad you were having fun, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x102,
        (
            "#1052F#11PMake sure you give those back to Josette later,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x11,
        (
            "#1029F#6PMaybe I will, maybe I won't! Tune in to next\x01",
            "week's issue to find out!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #131
        0x11,
        "#1004F#6P...Wait. Hold on...\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #132
        0x11,
        (
            "#1008F#6PUhhh...\x02\x03",

            "#1013FK-Kloe...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #133
        0x15,
        "Kloe",
        (
            "#1818F#5PHeehee.\x02\x03",

            "#1873FI suppose it's about time I returned to the\x01",
            "banquet now.\x02\x03",

            "#1872FYou can have Joshua back now, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x11,
        "#1004F#6PSure...?\x02",
    )

    CloseMessageWindow()

    def lambda_754F():
        OP_6D(37990, 16000, 79260, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_754F)

    def lambda_7567():
        OP_6C(5000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_7567)

    def lambda_7577():
        OP_6E(381, 3000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_7577)

    def lambda_7587():

        label("loc_7587")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_7587")

    QueueWorkItem2(0x102, 2, lambda_7587)

    def lambda_7598():

        label("loc_7598")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_7598")

    QueueWorkItem2(0x11, 2, lambda_7598)

    def lambda_75A9():
        OP_8E(0xFE, 0x8C78, 0x3E80, 0x12930, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_75A9)
    Sleep(3000)

    ChrTalk(    #135
        0x102,
        "#1035F#11PHey, Kloe?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x47, 0x0)
    OP_44(0x102, 0x2)
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x15, 45, 400)
    Sleep(300)

    ChrTalk(    #136
        0x102,
        (
            "#1043F#11PSo, umm...\x02\x03",

            "I'm not sure how to best put this, either,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #137
        0x102,
        (
            "#1053F#11P...thanks.\x02\x03",

            "I'm glad I was able to talk to you like this.\x02\x03",

            "#1041FReally, I am.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #138
        0x15,
        "Kloe",
        "#1814F#6P...Oh...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #139
        0x15,
        (
            "#1815F#6PYou're very welcome.\x02\x03",

            "#1818FWell, then. I wish you both a very pleasant night.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 225, 400)
    Sleep(300)

    def lambda_776D():
        OP_6D(36090, 16000, 77140, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_776D)

    def lambda_7785():
        OP_8E(0xFE, 0x6ACC, 0x36B0, 0x10734, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7785)
    WaitChrThread(0x47, 0x0)
    Sleep(1500)

    def lambda_77AA():
        OP_6D(39790, 16000, 79910, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_77AA)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_44(0x11, 0x2)
    WaitChrThread(0x47, 0x0)
    OP_63(0x11)
    Sleep(300)

    ChrTalk(    #140
        0x11,
        "#1008F#5PUmm... I... Uhh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #141
        0x11,
        (
            "#1016F#6PThe heck?\x02\x03",

            "#1013FSo, Joshua, what did you two,\x01",
            "you know...\x02\x03",

            "...t-talk about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        (
            "#1053F#11POh, nothing much.\x02\x03",

            "#1054FShe just gave me a bit of much-needed \x01",
            "motivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x11,
        "#1013F#6PO-Oh, really? That sure clears things up...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 225, 500)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #144
        0x102,
        (
            "#1053F#11P(It's been five years, and Estelle has\x01",
            "believed in me for every single one.)\x02\x03",

            "(And I...)\x02\x03",

            "#1041F(...I believe in her, too.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #145
        0x11,
        "#1004F#5P#3SArgh, no it doesn't! What motivation?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #146
        0x102,
        (
            "#1053F#11P...Estelle.\x02\x03",

            "#1040FI've got something I need to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x11,
        "#1004F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #148
        0x11,
        "#1006F#6PI'm all ears. What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        "#1053F#11PWell, you see...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x7D0)
    OP_22(0x183, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7B1D():
        OP_8C(0xFE, 315, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B1D)
    Sleep(100)
    OP_8C(0x11, 315, 500)

    ChrTalk(    #150
        0x11,
        "#1004F#12POh!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_7B4B():
        OP_6D(39790, 21000, 79910, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_7B4B)

    def lambda_7B63():
        OP_67(0, 6570, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_7B63)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x47, 0x1)
    OP_44(0x47, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    OP_6D(33340, 15750, 73420, 0)
    OP_67(0, 8300, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x102, 0xFF)
    SetChrPos(0x15, 37740, 16000, 77820, 45)
    SetChrPos(0x102, 30240, 14000, 70320, 45)

    def lambda_7BFD():
        OP_8E(0xFE, 0x8E58, 0x3E80, 0x12AE8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7BFD)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_7C22():
        OP_6D(37740, 16000, 77820, 4300)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_7C22)

    def lambda_7C3A():
        OP_67(0, 7300, -10000, 4300)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_7C3A)
    WaitChrThread(0x102, 0x1)
    Sleep(300)

    ChrTalk(    #151
        0x102,
        (
            "#1043FSo, Kloe?\x02\x03",

            "What was it that you wanted to tell me?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    NpcTalk(    #152
        0x15,
        "Kloe",
        "#1817F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        (
            "#1043FL-Look...\x02\x03",

            "...if I've done something to offend you,\x01",
            "I'm sorry, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(500)
    OP_8C(0x15, 225, 400)
    Sleep(500)

    NpcTalk(    #154
        0x15,
        "Kloe",
        "#1817F...I...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6B(2500, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #155
        0x15,
        "Kloe",
        "#1812FI love you, Joshua.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x75)
    Sleep(500)

    ChrTalk(    #156
        0x102,
        (
            "#1042F...\x02\x03",

            "#1044F...What?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7DAC():
        OP_6D(37600, 16000, 76620, 6000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_7DAC)

    def lambda_7DC4():
        OP_67(0, 8000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_7DC4)

    def lambda_7DDC():
        OP_6C(135000, 6000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_7DDC)
    WaitChrThread(0x47, 0x0)

    NpcTalk(    #157
        0x15,
        "Kloe",
        "#1812F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x102,
        "#1044FU-Umm...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #159
        0x15,
        "Kloe",
        "#1812F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        "#1043FI... Well...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #161
        0x15,
        "Kloe",
        "#1817F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #162
        0x102,
        "#1035FI-I'm sorry...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #163
        0x15,
        "Kloe",
        (
            "#1873FHeehee...\x02\x03",

            "Don't worry. I knew exactly how you were\x01",
            "going to respond before I said anything.\x02\x03",

            "#1815FI just felt like I had to get that out before\x01",
            "I could really start moving on.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7F54():

        label("loc_7F54")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_7F54")

    QueueWorkItem2(0x102, 2, lambda_7F54)
    OP_8C(0x15, 90, 400)
    Sleep(300)

    def lambda_7F71():
        OP_8E(0xFE, 0x9FEC, 0x3E80, 0x12FFC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7F71)
    WaitChrThread(0x15, 0x1)
    Sleep(300)

    NpcTalk(    #164
        0x15,
        "Kloe",
        "#1818FThe sky sure is beautiful tonight, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x102,
        "#1057FUmm... I...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #166
        0x102,
        "#1043FHow long have you, well...felt that way?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #167
        0x15,
        "Kloe",
        (
            "#1817F...Say, Joshua?\x02\x03",

            "If you had met me before Estelle...\x02\x03",

            "#1819F...do you think you would have...well...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #168
        0x102,
        (
            "#1035F...No.\x02\x03",

            "#1043FI'm pretty sure that would\x01",
            "never have happened.\x02\x03",

            "Sorry.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #169
        0x15,
        "Kloe",
        (
            "#1873F...I told you! Don't worry.\x02\x03",

            "I can't deny there's a part of me that\x01",
            "wants to keep you all to myself...\x02\x03",

            "...but even if that were possible, I don't\x01",
            "think it would be what I truly wanted.\x02\x03",

            "#1815FBecause when it comes down to it...\x02\x03",

            "...I really love both you and Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 270, 400)
    Sleep(500)

    NpcTalk(    #170
        0x15,
        "Kloe",
        (
            "#1810FThat's partly why I wanted to see that\x01",
            "troubled face of yours one last time.\x02\x03",

            "#1818FIt was worth the effort to bring out, too.\x02\x03",

            "That was probably the best expression\x01",
            "I've seen to date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        (
            "#1044F#40WI...#500W \x01",
            "#40WUmm...\x02\x03",

            "#1048F#20W...You can be kind of a bully sometimes,\x01",
            "you know that?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #172
        0x15,
        "Kloe",
        (
            "#1811FMaybe. This feels like the most fun\x01",
            "I've had in some time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_83C7():
        OP_6D(37960, 16000, 77020, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_83C7)

    def lambda_83DF():
        OP_67(0, 7300, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_83DF)

    def lambda_83F7():
        OP_6C(90000, 2000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_83F7)

    def lambda_8407():
        OP_8E(0xFE, 0x936C, 0x3E80, 0x12FFC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8407)
    WaitChrThread(0x15, 0x1)
    OP_8C(0x15, 225, 300)
    Sleep(300)

    NpcTalk(    #173
        0x15,
        "Kloe",
        (
            "#1817F#1P...Sooo...\x02\x03",

            "#1812F...what's on your mind, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #174
        0x102,
        "#1044FWhat?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #175
        0x15,
        "Kloe",
        (
            "#1815FHeehee. I can tell you're worried about\x01",
            "something quite easily.\x02\x03",

            "My instincts are quite sharp, or so I'd like\x01",
            "to believe. Besides...\x02\x03",

            "#1870F...I was watching you the whole time I was \x01",
            "handling that interview earlier, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        (
            "#1048F...O-Oh...\x02\x03",

            "#1056FHow exactly am I supposed to take that?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #177
        0x15,
        "Kloe",
        (
            "#1815FA-Ahaha...\x02\x03",

            "#1812FStill, you're hiding something, aren't you?\x02\x03",

            "#1812FAre you planning on doing something all\x01",
            "on your own again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        (
            "#1035F...\x02\x03",

            "#1052F*sigh* Your instincts are sharp, all right...\x02\x03",

            "Estelle surprises me from time to time,\x01",
            "too, but you're definitely up there.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #179
        0x15,
        "Kloe",
        (
            "#1818FWell, that's just how us girls are.\x02\x03",

            "#1812FSo, come on. Tell me what's on your mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #180
        0x102,
        (
            "#1035FIt's nothing that major, really.\x02\x03",

            "#1041F...I intend to leave Liberl by the end\x01",
            "of the month.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #181
        0x15,
        "Kloe",
        (
            "#1814FWhat?!\x02\x03",

            "#1812FB-But why? The country is finally at peace\x01",
            "now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        (
            "#1053FThat's exactly why I think this is the right time.\x02\x03",

            "Ouroboros seems to have completely withdrawn\x01",
            "from the country, and the restoration efforts are\x01",
            "coming along smoothly.\x02\x03",

            "#1041FSo maybe it's about time for me to leave on a\x01",
            "journey of my own.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x2)
    OP_8C(0x102, 315, 200)
    Sleep(500)

    ChrTalk(    #183
        0x102,
        (
            "#1035FIt's taken me a long time to get this far...\x02\x03",

            "...but I've finally been able to start thinking of\x01",
            "myself as a person and not some kind of broken\x01",
            "doll.\x02\x03",

            "I was finally able to achieve the very thing\x01",
            "everyone wanted for me.\x02\x03",

            "#1041F...That's been both a good thing and a bad one.\x01",
            "Good in that I finally feel human, bad in that my\x01",
            "heart's been aching in a way it never did before.\x02\x03",

            "Broken dolls can easily look away from all the\x01",
            "terrible things they've done...but I can't do that\x01",
            "anymore.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #184
        0x15,
        "Kloe",
        "#1813F...Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        (
            "#1035FThat's why I need to go on this journey around\x01",
            "the continent.\x02\x03",

            "So I can work towards atoning for all that I've\x01",
            "done...\x02\x03",

            "#1042FSo I can start embracing the person I now am,\x01",
            "in the truest sense of the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #186
        0x15,
        "Kloe",
        (
            "#1819FI...see...\x02\x03",

            "#1813FBut if you do that, that means you won't be\x01",
            "able to see Estelle for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        (
            "#1043FYeah... I know.\x02\x03",

            "It might not even be for a while--it could\x01",
            "be a long time.\x02\x03",

            "#1035FI'm still not sure how to break that to her,\x01",
            "either... That's the part that's on my mind\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)

    NpcTalk(    #188
        0x15,
        "Kloe",
        (
            "#1817F*sigh*\x02\x03",

            "You've still got a lot of growing up to do,\x01",
            "young man.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #189
        0x102,
        "#1044F...Huh?\x02",
    )

    CloseMessageWindow()

    def lambda_8E15():
        OP_8C(0xFE, 45, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8E15)

    def lambda_8E23():
        OP_8E(0xFE, 0x91DC, 0x3E80, 0x12E6C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8E23)
    WaitChrThread(0x15, 0x1)
    Fade(800)
    OP_6D(37740, 16000, 77820, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(800)

    NpcTalk(    #190
        0x15,
        "Kloe",
        (
            "#1812F#5PIf you ask me, you should just tell her in the way\x01",
            "that comes most naturally to you.\x02\x03",

            "You don't have to write some big speech in your\x01",
            "head in advance--speak to her from the heart.\x01",
            "You believe in her, don't you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #191
        0x15,
        "Kloe",
        (
            "#1816F#5PNo matter how you phrase it, she'll understand.\x01",
            "All you have to do is get those words out there!\x02",
        )
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x96)
    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #192
        0x15,
        "Kloe",
        "#1812F#5PYou owe that much to her if you love her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x102,
        (
            "#1044F...\x02\x03",

            "#1043F...But...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #194
        0x15,
        "Kloe",
        (
            "#1873F#5PJust remember: it'll be okay. If anyone knows you,\x01",
            "it's Estelle.\x02\x03",

            "#1815FAlthough if you ask me, she'll...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrPos(0x11, 21600, 14000, 70600, 90)
    OP_44(0x11, 0xFF)

    NpcTalk(    #195
        0x11,
        "Energetic Voice",
        "Joshuaaa! Where are you?\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_914E():

        label("loc_914E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_914E")

    QueueWorkItem2(0x102, 2, lambda_914E)

    def lambda_915F():
        OP_6D(31740, 14500, 71820, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_915F)
    Sleep(1000)

    def lambda_917C():
        OP_8E(0xFE, 0x7724, 0x3E80, 0x113C8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_917C)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 45, 500)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #196
        0x11,
        (
            "#1001FOh, there you are!\x02\x03",

            "#1018FLook at these! They're Josette's goggles!\x02\x03",

            "#1029FHeheh. I took them from her as spoils of war!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x15, 36500, 16000, 77620, 225)

    def lambda_924F():
        OP_6D(36900, 16000, 75800, 1500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_924F)

    def lambda_9267():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_9267)

    def lambda_9277():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_9277)

    def lambda_9287():
        OP_8E(0xFE, 0x8854, 0x3E80, 0x124F8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9287)
    WaitChrThread(0x11, 0x1)
    OP_44(0x102, 0x2)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #197
        0x15,
        "Kloe",
        (
            "#1872F#1PUmm...\x02\x03",

            "#1815FI'm...glad you were having fun, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x102,
        (
            "#1052F#1PMake sure you give those back to Josette later,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x11,
        (
            "#1029FMaybe I will, maybe I won't! Tune in to next\x01",
            "week's issue to find out!\x02\x03",

            "#1004F...Wait. Hold on...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #200
        0x11,
        (
            "#1008FUhhh...\x02\x03",

            "#1013FK-Kloe...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #201
        0x15,
        "Kloe",
        (
            "#1818F#1PHeehee.\x02\x03",

            "I suppose it's about time I returned to the\x01",
            "banquet now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9474():

        label("loc_9474")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_9474")

    QueueWorkItem2(0x11, 2, lambda_9474)

    def lambda_9485():
        OP_8E(0xFE, 0x878C, 0x3E80, 0x1282C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9485)
    WaitChrThread(0x15, 0x1)
    TurnDirection(0x102, 0x15, 500)

    ChrTalk(    #202
        0x102,
        "#1044F#1PUmm... Kloe...\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x15, 45, 400)
    Sleep(700)

    ChrTalk(    #203
        0x102,
        "#1041F#1P...thanks.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #204
        0x15,
        "Kloe",
        "#1814F#4P...Oh...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #205
        0x15,
        "#1873F#4P...You're quite welcome.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 225, 400)
    Sleep(300)

    def lambda_955E():
        OP_8E(0xFE, 0x701C, 0x36B0, 0x110BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_955E)
    Sleep(2000)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x15, 0x1)
    OP_44(0x11, 0x2)
    SetChrPos(0x15, 11100, 12000, 57370, 270)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #206
        0x11,
        "#1008FUmm... I... Uhh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #207
        0x11,
        (
            "#1008FThe heck?\x02\x03",

            "#1013FSo, Joshua, what did you two,\x01",
            "you know...\x02\x03",

            "...t-talk about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        (
            "#1053F#1POh, nothing much.\x02\x03",

            "#1054FShe just gave me a bit of much needed \x01",
            "motivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x11,
        "#1008FO-Oh, really? That sure clears things up...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 225, 500)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #210
        0x102,
        (
            "#1035F#1P(It's been five years, and Estelle has\x01",
            "believed in me for every single one.)\x02\x03",

            "(And I...)\x02\x03",

            "#1041F(...I believe in her, too.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #211
        0x11,
        "#1004FArgh, no it doesn't! What motivation?\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #212
        0x102,
        (
            "#1040F#1P...Estelle.\x02\x03",

            "I've got something I need to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x11,
        "#1004F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #214
        0x11,
        (
            "#1017F...R-Right!\x02\x03",

            "...Wh...What is it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        "#1053F#1PWell, you see...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x183, 0x0, 0x64)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(150)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_98F7():
        OP_8C(0xFE, 315, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_98F7)
    Sleep(150)
    OP_8C(0x11, 315, 300)
    Sleep(400)

    ChrTalk(    #216
        0x11,
        "#1011FOh!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_9926():
        OP_6D(36900, 17000, 75800, 1500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_9926)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_47FD end

    def Function_21_9950(): pass

    label("Function_21_9950")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9991")

    def lambda_995F():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_995F)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    Jump("Function_21_9950")

    label("loc_9991")

    Return()

    # Function_21_9950 end

    def Function_22_9992(): pass

    label("Function_22_9992")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99D3")

    def lambda_99A1():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_99A1)
    OP_62(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    Jump("Function_22_9992")

    label("loc_99D3")

    Return()

    # Function_22_9992 end

    def Function_23_99D4(): pass

    label("Function_23_99D4")

    OP_8E(0xFE, 0x965A, 0x3E80, 0x1331C, 0x5DC, 0x0)
    OP_8E(0xFE, 0xA122, 0x3E80, 0x13600, 0x5DC, 0x0)
    Return()

    # Function_23_99D4 end

    def Function_24_99FD(): pass

    label("Function_24_99FD")

    OP_8E(0xFE, 0x1BF8, 0x36B0, 0x13B82, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3D2C, 0x36B0, 0x13E70, 0x7D0, 0x0)
    Return()

    # Function_24_99FD end

    def Function_25_9A26(): pass

    label("Function_25_9A26")

    EventBegin(0x0)
    OP_4A(0x17, 0)
    OP_4A(0x16, 0)
    OP_8C(0x17, 180, 0)
    OP_8C(0x16, 0, 0)
    Fade(1000)
    OP_6D(15940, 14000, 71760, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(268, 0)
    SetChrPos(0x102, 14110, 14000, 70910, 90)
    OP_0D()
    Sleep(300)

    ChrTalk(    #217
        0x17,
        "#061FSo, when are you coming?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x16,
        "#555FHold on! I haven't even...\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_9B13():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_9B13)
    Sleep(150)
    OP_8C(0x16, 270, 400)
    Sleep(300)

    ChrTalk(    #219
        0x17,
        "#064FOh, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x16,
        "#051FHey, man. Makin' the rounds?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x102,
        (
            "#1040FSomething like that, yeah.\x02\x03",

            "Anything interesting going on with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x17,
        (
            "#560FSort of.\x02\x03",

            "Agate said he was gonna come over for dinner\x01",
            "in Zeiss a while back.\x02\x03",

            "#067FSo I was just asking him when he's free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x102,
        (
            "#1040FOh, that's right. So he did.\x02\x03",

            "When we were getting off the Arseille, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x16,
        (
            "#552FI didn't really mean it, though... It was just one\x01",
            "of those things you say in passing but don't\x01",
            "give much thought to.\x02\x03",

            "I ain't exactly swimming in free time, you know.\x01",
            "Being a bracer's busy work.\x02\x03",

            "#053FI'd like to go, sure, but I've got no idea if I'll\x01",
            "actually have the time to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x17,
        (
            "#060F...\x02\x03",

            "#562FBut I've been looking forward to you coming\x01",
            "ever since...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)
    OP_8C(0x16, 0, 500)
    Sleep(300)

    ChrTalk(    #226
        0x16,
        (
            "#055FUgh...\x02\x03",

            "O-Okay, okay! Argh... Let me think...\x02\x03",

            "#552FM-Maybe the end of the month? That should\x01",
            "be okay...\x02\x03",

            "I think that Friday's free? Think.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_8C(0x17, 180, 500)
    Sleep(300)

    ChrTalk(    #227
        0x17,
        (
            "#067FReally?!\x02\x03",

            "Heehee. Is that a promise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x16,
        "#555FY-Yeah... I guess...\x02",
    )

    CloseMessageWindow()
    OP_4B(0x17, 0)
    OP_4B(0x16, 0)
    OP_A2(0x2F9B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_9F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_9F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_9F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_9F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_9F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_9F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_9F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_9F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_9F86")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_9F86")

    EventEnd(0x0)
    Return()

    # Function_25_9A26 end

    def Function_26_9F89(): pass

    label("Function_26_9F89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_A00F")
    OP_8C(0x17, 180, 0)

    ChrTalk(    #229
        0x17,
        "#067F...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #230
        "\x07\x05Tita took out a small notebook and started scribbling in it.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_A013")

    label("loc_A00F")

    Call(0, 25)

    label("loc_A013")

    TalkEnd(0xFE)
    Return()

    # Function_26_9F89 end

    def Function_27_A017(): pass

    label("Function_27_A017")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_A166")
    OP_8C(0x16, 0, 0)
    OP_4A(0x17, 255)

    ChrTalk(    #231
        0x17,
        "#061FSo what kinds of dishes do you like?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x16,
        (
            "#053FAny old set of groceries I can shove down\x01",
            "my neck is fine by me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x17,
        "#065FN-Nothing special at all...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #234
        0x16,
        "#551FUhh... Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x102,
        (
            "#1040F(I think I'd better leave them alone for now.)\x02\x03",

            "(I wouldn't want to get in their way.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    Jump("loc_A16A")

    label("loc_A166")

    Call(0, 25)

    label("loc_A16A")

    TalkEnd(0xFE)
    Return()

    # Function_27_A017 end

    def Function_28_A16E(): pass

    label("Function_28_A16E")

    EventBegin(0x0)
    OP_4A(0x14, 0)
    OP_4A(0x13, 0)
    OP_8C(0x14, 180, 0)
    OP_8C(0x13, 270, 0)
    Fade(1000)
    OP_6D(-23910, 12000, 88040, 0)
    OP_67(0, 7210, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(276, 0)
    SetChrPos(0x102, -24200, 12000, 87770, 225)
    OP_0D()
    Sleep(300)

    ChrTalk(    #236
        0x102,
        "#1040F#5PYou two look comfortable.\x02",
    )

    CloseMessageWindow()

    def lambda_A20D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_A20D)
    Sleep(150)
    TurnDirection(0x14, 0x102, 400)
    Sleep(300)

    ChrTalk(    #237
        0x13,
        (
            "#027FOh, if it isn't Joshua.\x02\x03",

            "Care to join us for a few drinks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x14,
        (
            "#031FHaha! Don't be shy, now.\x02\x03",

            "The night is only just beginning...\x02\x03",

            "#037F...but I want to see those exquisite amber eyes\x01",
            "of yours swim before it comes to a close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x102,
        "#1048F#5P...I'm good, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x13,
        (
            "#025FAww, c'mon! We're at a celebratory banquet here!\x01",
            "Don't be such a spoilsport.\x02\x03",

            "#021FOh, I know! Why don't we have a few drinks to\x01",
            "celebrate you becoming a senior bracer at the\x01",
            "same time?\x02\x03",

            "It feels like it was ages ago, but we never did\x01",
            "get to celebrate your promotion. Only Estelle's.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #241
        0x102,
        (
            "#1035F#5P...Say, Schera?\x02\x03",

            "#1043FAbout... Well, about Luciola...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x13,
        (
            "#524FHaha...\x02\x03",

            "#021FSilly Joshua. What're you getting all worried\x01",
            "about her for?\x02\x03",

            "You really needn't be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x14,
        (
            "#035FHeh. Schera's right.\x02\x03",

            "Especially not now. We all have our concerns and\x01",
            "worries after all that happened over the past few\x01",
            "weeks and months...\x02\x03",

            "#030F...but this is not the time to be thinking about them.\x01",
            "This is the time to be making merry and drowning in\x01",
            "fine drink.\x02\x03",

            "#031FFrom sunset to sunrise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x102,
        "#1054F#5PR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x13,
        (
            "#025FI don't think there's ever a time for NOT making\x01",
            "merry as far as you're concerned.\x02\x03",

            "#027FHe's got a point, though.\x02\x03",

            "#026FOh, and while I've got the chance to say this to\x01",
            "you...no more going off on your own, you hear?\x02\x03",

            "#524FYou have no idea how worried Estelle was about\x01",
            "you after you last disappeared. I could barely\x01",
            "bring myself to watch her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x102,
        (
            "#1035F#5PI won't.\x02\x03",

            "#1040FI've got no intention of doing anything like that\x01",
            "again. I'm fine now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x13,
        "#021FWell, if you say so!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x14,
        (
            "#037FHaha. That docile expression of yours is\x01",
            "so adorable, Joshua. Don't go showing\x01",
            "off that face too much tonight, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 0)
    OP_8C(0x14, 180, 0)
    OP_4B(0x13, 0)
    OP_4B(0x14, 0)
    OP_A2(0x2F9C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_A93F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_A93F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_A93F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_A93F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_A93F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_A93F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_A93F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_A93F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_A93F")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_A93F")

    EventEnd(0x0)
    Return()

    # Function_28_A16E end

    def Function_29_A942(): pass

    label("Function_29_A942")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_AB11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_AA09")

    ChrTalk(    #249
        0x13,
        (
            "#027FAnyway, it's about time I seriously started\x01",
            "thinking about returning to Rolent, hmm?\x02\x03",

            "Hah. Maybe I've finally got what it takes to\x01",
            "beat Aina in a drinking contest, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0E")

    label("loc_AA09")


    ChrTalk(    #250
        0x13,
        (
            "#522FFeels like no amount of alcohol's enough to\x01",
            "get me drunk lately. I don't know what's up \x01",
            "with me.\x02\x03",

            "...\x02\x03",

            "#520FOn the positive side, though, maybe now I can\x01",
            "actually beat Aina in a drinking contest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x102,
        "#1048F(Trust her to find a positive in that.)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_AB0E")

    Jump("loc_AB15")

    label("loc_AB11")

    Call(0, 28)

    label("loc_AB15")

    TalkEnd(0xFE)
    Return()

    # Function_29_A942 end

    def Function_30_AB19(): pass

    label("Function_30_AB19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_ADB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_AC27")
    OP_8C(0x14, 180, 0)
    OP_4A(0x13, 255)

    ChrTalk(    #252
        0x14,
        (
            "#035FIncidentally, Schera...while you'll forgive me\x01",
            "if this is just my imagination...\x02\x03",

            "#037F...are you not drinking a liiittle too quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x13,
        "#026F...*guuulp*\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #254
        0x14,
        "#036FY-You're starting to scare me a little!\x02",
    )

    CloseMessageWindow()
    OP_4B(0x13, 255)
    Jump("loc_ADAF")

    label("loc_AC27")


    ChrTalk(    #255
        0x102,
        (
            "#1044FOlivier, is it okay if you're here in Liberl?\x01",
            "I would've thought you'd be needed back\x01",
            "in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x14,
        (
            "#030FWell, I will go back. Eventually...\x02\x03",

            "#035FFor now, however, I intend to savor the\x01",
            "lingering feelings of this whirlwind of a\x01",
            "ride.\x02\x03",

            "Remaining behind afforded me the chance to\x01",
            "attend this wonderful party, to boot. As you\x01",
            "can see, my fine instincts have yet to fail me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_ADAF")

    Jump("loc_ADB6")

    label("loc_ADB2")

    Call(0, 28)

    label("loc_ADB6")

    TalkEnd(0xFE)
    Return()

    # Function_30_AB19 end

    def Function_31_ADBA(): pass

    label("Function_31_ADBA")

    EventBegin(0x0)
    OP_4A(0x1A, 0)
    OP_4A(0x11, 0)
    OP_8C(0x1A, 0, 0)
    OP_8C(0x11, 180, 0)
    Fade(1000)
    OP_6D(-6670, 12000, 58710, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, -6770, 12000, 57530, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(    #257
        0x1A,
        (
            "#1560FHA! I figured that'd be the case.\x02\x03",

            "Looks like I'm the most fit to be at this party\x01",
            "after all.\x02\x03",

            "#1561FBecause I've been to plenty of high society \x01",
            "gatherings wearing poofy dresses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x11,
        (
            "#1009F#1PHey! Don't make it sound like I've never worn\x01",
            "a dress before!\x02\x03",

            "Because I HAVE, for your information!\x02\x03",

            "#1022FI just don't need to go around trying to convince\x01",
            "everyone that I'm not a boy! Unlike SOME people\x01",
            "I could name...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x1A,
        (
            "#1564FTry saying I look like a boy again and see what\x01",
            "happens!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x102,
        (
            "#1048F#2PLook, you two. I appreciate that you\x01",
            "have your differences...\x02\x03",

            "...but we're kind of in a really public,\x01",
            "really high-class place, here, so could\x01",
            "you take this fight somewhere else?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B0E2():
        TurnDirection(0xFE, 0x102, 600)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_B0E2)

    def lambda_B0F0():
        TurnDirection(0xFE, 0x102, 600)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_B0F0)
    WaitChrThread(0x1A, 0x2)
    Sleep(400)

    ChrTalk(    #261
        0x1A,
        "#1564F#3SShut up, Joshua!#2S\x02",
    )


    ChrTalk(    #262
        0x11,
        "#1005F#3S#1PShut up, Joshua!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()

    ChrTalk(    #263
        0x102,
        "#1052F#2P...Wow. Sorry.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1A, 0, 0)
    OP_8C(0x11, 180, 0)
    OP_4B(0x1A, 0)
    OP_4B(0x11, 0)
    OP_A2(0x2F9D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_B1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_B1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_B1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_B1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_B1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_B1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_B1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_B1D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_B1D5")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_B1D5")

    EventEnd(0x0)
    Return()

    # Function_31_ADBA end

    def Function_32_B1D8(): pass

    label("Function_32_B1D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_B26D")
    OP_8C(0x1A, 0, 0)

    ChrTalk(    #264
        0x1A,
        (
            "#1560FHah. Okay, then. Have it your way.\x02\x03",

            "How about you and me settle this with an\x01",
            "honorable duel? Think you can handle it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B271")

    label("loc_B26D")

    Call(0, 31)

    label("loc_B271")

    TalkEnd(0xFE)
    Return()

    # Function_32_B1D8 end

    def Function_33_B275(): pass

    label("Function_33_B275")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_B2F7")
    OP_8C(0x11, 180, 0)

    ChrTalk(    #265
        0x11,
        (
            "#1028FDamn right, I can! You're on!\x02\x03",

            "Just don't cry when you realize you can't\x01",
            "actually beat me, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2FB")

    label("loc_B2F7")

    Call(0, 31)

    label("loc_B2FB")

    TalkEnd(0xFE)
    Return()

    # Function_33_B275 end

    def Function_34_B2FF(): pass

    label("Function_34_B2FF")

    EventBegin(0x0)
    OP_4A(0x18, 0)
    OP_8C(0x18, 270, 0)
    Fade(1000)
    OP_6D(9760, 12000, 65970, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 8640, 12000, 64269, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x18, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x18, 0x102, 400)
    Sleep(300)

    ChrTalk(    #266
        0x18,
        "#073F#1PHow's it going, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x102,
        (
            "#1040FHello, Zin.\x02\x03",

            "Thanks again for all the help you've been\x01",
            "giving with the restoration efforts.\x02\x03",

            "I don't know what we'd have done without\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x18,
        (
            "#071F#1PHahaha! Hey, think nothing of it!\x02\x03",

            "It's all part of being a bracer, really.\x02\x03",

            "#070FCan't say how much longer I'll be able to\x01",
            "lend a helping hand, though. Gotta pack up\x01",
            "and head back home at some point.\x02\x03",

            "The political situation isn't exactly stable\x01",
            "over there, you see.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 270, 0)
    OP_4B(0x18, 0)
    OP_A2(0x2FA0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_B5AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_B5AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_B5AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_B5AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_B5AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_B5AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_B5AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_B5AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_B5AE")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_B5AE")

    EventEnd(0x0)
    Return()

    # Function_34_B2FF end

    def Function_35_B5B1(): pass

    label("Function_35_B5B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_B6D7")
    OP_8C(0x18, 270, 0)
    OP_4A(0x2B, 255)

    ChrTalk(    #269
        0x2B,
        (
            "#1110FWas that why Kilika wasn't able to make it,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x18,
        (
            "#070FYeah. The guild receptionists are basically\x01",
            "chained to their seats at the moment.\x02\x03",

            "#075FAlthough to be honest, I can't picture her\x01",
            "getting all dressed up and coming to a party\x01",
            "like this, anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x2B, 255)
    Jump("loc_B6DB")

    label("loc_B6D7")

    Call(0, 34)

    label("loc_B6DB")

    TalkEnd(0xFE)
    Return()

    # Function_35_B5B1 end

    def Function_36_B6DF(): pass

    label("Function_36_B6DF")

    EventBegin(0x0)
    OP_4A(0x1C, 0)
    OP_4A(0x1B, 0)
    OP_8C(0x1B, 270, 0)
    OP_8C(0x1C, 90, 0)
    Fade(500)
    OP_6D(8530, 12000, 54030, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    SetChrPos(0x102, 7590, 12000, 53660, 225)
    TurnDirection(0x1C, 0x102, 0)
    TurnDirection(0x1B, 0x102, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #271
        0x1B,
        (
            "#170FAh, if it isn't Joshua.\x02\x03",

            "I was just discussing the aftermath of the\x01",
            "crisis here with Major Vander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x1C,
        (
            "#270FFortunately, the Liber Ark's collapse caused\x01",
            "little direct damage by itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x1B,
        (
            "#176FThat might not have been the case if there\x01",
            "had been any ships on the lake at the time,\x01",
            "but due in part to the Orbal Shutdown\x01",
            "Phenomenon, none were.\x02\x03",

            "#170FThe tsunami afterward was quite small, too.\x01",
            "I'd say we were rather fortunate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x102,
        (
            "#1040F#5PEstelle and I were able to see as much when we\x01",
            "traveled around the lake shore.\x02\x03",

            "A few people who were watching the city collapse\x01",
            "were caught up in it and a small number of fishermen\x01",
            "were splashed with water, but that's about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x1C,
        (
            "#272FIndeed... If anything, the much greater problem\x01",
            "was the confusion that came about as a result\x01",
            "of losing orbal power.\x02\x03",

            "#270FLiberl is, after all, one of the most advanced\x01",
            "nations on the continent when it comes to orbal\x01",
            "technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x1B,
        (
            "#178FOrdinarily, that is one of our greatest strengths...\x01",
            "but in this case, it worked against us.\x02\x03",

            "#176FThe crisis has now passed, but that doesn't mean\x01",
            "our work is done. We still have plenty ahead of us\x01",
            "to take care of.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1B, 270, 0)
    OP_8C(0x1C, 90, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_A2(0x2F9E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_BC36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_BC36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_BC36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_BC36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_BC36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_BC36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_BC36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_BC36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_BC36")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_BC36")

    EventEnd(0x0)
    Return()

    # Function_36_B6DF end

    def Function_37_BC39(): pass

    label("Function_37_BC39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_BD28")

    ChrTalk(    #277
        0x1B,
        (
            "#178FLiberl's abundance of orbal technology ended\x01",
            "up working against it this time, regrettably...\x02\x03",

            "#176FThe crisis has now passed, but that doesn't mean\x01",
            "our work is done. We still have plenty ahead of us\x01",
            "to take care of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD2C")

    label("loc_BD28")

    Call(0, 36)

    label("loc_BD2C")

    TalkEnd(0xFE)
    Return()

    # Function_37_BC39 end

    def Function_38_BD30(): pass

    label("Function_38_BD30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_BEB2")

    ChrTalk(    #278
        0x1C,
        (
            "#270FThe confusion created on Erebonia's southern\x01",
            "edge as a result of the Orbal Shutdown Phenomenon\x01",
            "calmed itself down rather quickly.\x02\x03",

            "But over in Erebonia, no more is being reported about\x01",
            "the city than that it was a 'mysterious floating object.'\x02\x03",

            "#276FEither the central government is still in confusion and\x01",
            "that's why it isn't releasing any more information, or...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEB6")

    label("loc_BEB2")

    Call(0, 36)

    label("loc_BEB6")

    TalkEnd(0xFE)
    Return()

    # Function_38_BD30 end

    def Function_39_BEBA(): pass

    label("Function_39_BEBA")

    EventBegin(0x0)
    OP_4A(0x32, 0)
    OP_4A(0x33, 0)
    OP_8C(0x32, 180, 0)
    OP_8C(0x33, 270, 0)
    Fade(500)
    OP_6D(-5230, 12000, 67430, 0)
    OP_67(0, 7430, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    SetChrPos(0x102, -5230, 12000, 67430, 225)
    OP_8C(0x32, 90, 0)
    OP_8C(0x33, 0, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #279
        0x33,
        "#200FHeya, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x102,
        (
            "#1040FI didn't expect to see you guys here.\x02\x03",

            "You were invited, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x32,
        (
            "#190FSure was! An invitation just showed up out\x01",
            "of nowhere. You can imagine our surprise\x01",
            "when we saw the thing.\x02\x03",

            "No way were we turning down some high-class\x01",
            "grub, though, so we hurried on over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x102,
        "#1054FHaha... That's very like you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x33,
        (
            "#202FNot gonna deny it.\x02\x03",

            "#200FThat aside, thanks to Her Majesty pardoning us,\x01",
            "we're now free to walk around in the open.\x02\x03",

            "Feels like we should start thinking about how to\x01",
            "make a good, honest living for ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x102,
        (
            "#1040FThat's not the first time you've said that.\x02\x03",

            "Something about wanting to start up a\x01",
            "courier service, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x33,
        (
            "#204FWell, maybe, but that's not the only thing we\x01",
            "could try out.\x02\x03",

            "#200FWhatever we settle on, it should involve flying\x01",
            "the skies. That's how we've lived so far--I don't\x01",
            "want to change now.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x32, 180, 0)
    OP_8C(0x33, 270, 0)
    OP_4B(0x32, 0)
    OP_4B(0x33, 0)
    OP_A2(0x2F9F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_C2FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_C2FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_C2FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_C2FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_C2FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_C2FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_C2FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_C2FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_C2FB")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_C2FB")

    EventEnd(0x0)
    Return()

    # Function_39_BEBA end

    def Function_40_C2FE(): pass

    label("Function_40_C2FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_C3D7")
    OP_8C(0x32, 180, 0)

    ChrTalk(    #286
        0x32,
        (
            "#198F*munch* You're not gonna hear ME say no.\x02\x03",

            "All the complicated financial stuff goes right\x01",
            "over my head, so just don't count on me there.\x02\x03",

            "#490FThat might even be right up Josette's alley.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3DB")

    label("loc_C3D7")

    Call(0, 39)

    label("loc_C3DB")

    TalkEnd(0xFE)
    Return()

    # Function_40_C2FE end

    def Function_41_C3DF(): pass

    label("Function_41_C3DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_C52D")

    ChrTalk(    #287
        0x33,
        (
            "#200FStill, the best thing about starting up a company\x01",
            "is we'd be able to employ all the guys who worked\x01",
            "under us while we were in the sky bandit business.\x02\x03",

            "#203FI mean, I ain't saying it's gonna be EASY. We don't\x01",
            "have any funding, and we don't know if we'll even\x01",
            "be profitable once we do get things up and running.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C531")

    label("loc_C52D")

    Call(0, 39)

    label("loc_C531")

    TalkEnd(0xFE)
    Return()

    # Function_41_C3DF end

    def Function_42_C535(): pass

    label("Function_42_C535")

    EventBegin(0x0)
    OP_4A(0x10, 0)
    OP_8C(0x10, 270, 0)
    Fade(1000)
    OP_6D(3120, 12000, 65540, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 3060, 12000, 64830, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(    #288
        0x102,
        (
            "#1044F#11P...Kevin?\x02\x03",

            "I wasn't expecting you to still be in Liberl.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 500)
    Sleep(300)

    ChrTalk(    #289
        0x10,
        (
            "#1062F#6POh, 'sup? You were invited, too, huh? Makes sense.\x02\x03",

            "#1066FSo? Having fun?\x02\x03",

            "You better be. Take it from me--if you don't make\x01",
            "the most of times like these and eat your heart out,\x01",
            "you're gonna regret it later.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFFFF)
    Sleep(500)

    ChrTalk(    #290
        0x102,
        (
            "#1035F#11P...Thank you very much for all you did for me,\x01",
            "Kevin.\x02\x03",

            "If you hadn't come to Liberl when you did,\x01",
            "I...I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x10,
        (
            "#1840F#6PAhh, don't sweat it.\x02\x03",

            "Not like I did anything special.\x02\x03",

            "#1075FGlad to see all the side effects look about gone,\x01",
            "too. You're lookin' spiffy these days, Joshua.\x02\x03",

            "#1060FSo yeah. Just forget about owing me or whatever.\x01",
            "It's all in the past now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x102,
        (
            "#1043F#11P...\x02\x03",

            "I'm not sure if I should ask this, but are you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x10,
        (
            "#1065F#6P...Joshua.\x02\x03",

            "I'm not gonna be in Liberl for much longer,\x01",
            "so this might be the last time we meet for a\x01",
            "while.\x02\x03",

            "#1840FBut I hope we'll get the chance to see each\x01",
            "other again one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x102,
        "#1054F#11P...Yeah. I hope so, too.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 0)
    OP_4B(0x10, 0)
    OP_A2(0x2FA1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_C9E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_C9E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_C9E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_C9E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_C9E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_C9E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_C9E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_C9E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_C9E8")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_C9E8")

    EventEnd(0x0)
    Return()

    # Function_42_C535 end

    def Function_43_C9EB(): pass

    label("Function_43_C9EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_CA9F")
    OP_8C(0x10, 270, 0)

    ChrTalk(    #295
        0x10,
        (
            "#1064FDamn! This sirloin steak's like a little piece\x01",
            "of heaven in my mouth.\x02\x03",

            "#1846FI sure wish I could take a lifetime's supply of\x01",
            "it back home with me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA3")

    label("loc_CA9F")

    Call(0, 42)

    label("loc_CAA3")

    TalkEnd(0xFE)
    Return()

    # Function_43_C9EB end

    def Function_44_CAA7(): pass

    label("Function_44_CAA7")

    EventBegin(0x0)
    OP_4A(0x15, 0)
    OP_8C(0x15, 90, 0)
    OP_4A(0x35, 0)
    Fade(1000)
    OP_6D(13200, 12000, 59150, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    SetChrPos(0x102, 11770, 12000, 59360, 180)
    OP_0D()
    Sleep(300)

    ChrTalk(    #296
        0x15,
        (
            "#1872F...What? You'd like me to give a comment?\x02\x03",

            "#1815FWell...let's see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x102,
        (
            "#1054F#1P(Looks like she's being interviewed at the\x01",
            "moment.)\x02\x03",

            "(I should leave her be for now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 90, 0)
    OP_4B(0x15, 0)
    OP_4B(0x35, 0)
    OP_A2(0x2FA2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_CC1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_CC1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_CC1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_CC1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_CC1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_CC1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_CC1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_CC1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_CC1B")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_CC1B")

    EventEnd(0x0)
    Return()

    # Function_44_CAA7 end

    def Function_45_CC1E(): pass

    label("Function_45_CC1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_CC82")
    OP_8C(0x15, 90, 0)

    ChrTalk(    #298
        0x15,
        (
            "#1872F...What? You'd like me to give a comment?\x02\x03",

            "#1815FWell...let's see...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC86")

    label("loc_CC82")

    Call(0, 44)

    label("loc_CC86")

    TalkEnd(0xFE)
    Return()

    # Function_45_CC1E end

    def Function_46_CC8A(): pass

    label("Function_46_CC8A")

    EventBegin(0x0)
    OP_4A(0x31, 0)
    OP_8C(0x31, 270, 0)
    Fade(1000)
    OP_6D(-41100, 16000, 81610, 0)
    OP_67(0, 4535, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    SetChrPos(0x102, -41440, 16000, 80610, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(    #299
        0x31,
        "#1125F...Ah, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x102,
        (
            "#1040F#2PI'm surprised to see you here, Dad.\x02\x03",

            "I thought you said over the phone you wouldn't be\x01",
            "able to attend because you were so swamped?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x31, 90, 400)
    Sleep(300)

    ChrTalk(    #301
        0x31,
        (
            "#1120FOh, 'swamped' is an understatement.\x02\x03",

            "#1123FTransporting goods needed to get the country\x01",
            "back in order, making sure every area has all\x01",
            "the utilities it needs... I'm drowning in work.\x02\x03",

            "It's going to take a while longer before we can\x01",
            "say Liberl is 'back to normal,' too, I fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x102,
        (
            "#1040F#2PCome to think of it...\x02\x03",

            "...Estelle and I certainly didn't expect to find\x01",
            "soldiers even in Liberl's smaller villages, so\x01",
            "it threw us off to see as much while we were\x01",
            "helping out where we could.\x02\x03",

            "Doesn't come as a surprise if you're the one\x01",
            "responsible, though. It should go a long way\x01",
            "toward helping people feel at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x31,
        (
            "#1125FIt's times like these when we've got to do all\x01",
            "we can for one another, and the army's no\x01",
            "different.\x02\x03",

            "With Erebonia and Calvard's internal political\x01",
            "situations a mystery to us, the reorganization\x01",
            "of the army has had to be shelved for now, too.\x02\x03",

            "#1120FStill, no matter how busy a man is, everyone\x01",
            "needs to kick back in a while.\x02\x03",

            "So make sure you make the most of tonight,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x102,
        (
            "#1054F#2PI think you need to 'kick back' more than\x01",
            "I do, Dad...\x02\x03",

            "Estelle's been pretty worried about you,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x31,
        (
            "#1121FHaha! There's no need to worry about me.\x01",
            "I'm hanging in there.\x02\x03",

            "In fact, I'd say I'm taking it too easy!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x31, 270, 0)
    OP_4B(0x31, 0)
    OP_A2(0x2FA3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_D2D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_D2D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_D2D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_D2D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_D2D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_D2D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_D2D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_D2D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_D2D8")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_D2D8")

    EventEnd(0x0)
    Return()

    # Function_46_CC8A end

    def Function_47_D2DB(): pass

    label("Function_47_D2DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_D35A")

    ChrTalk(    #306
        0x31,
        (
            "#1120FDon't you worry about me.\x02\x03",

            "In fact, I'm taking it easy while passing\x01",
            "along the tough jobs to you guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35E")

    label("loc_D35A")

    Call(0, 46)

    label("loc_D35E")

    TalkEnd(0xFE)
    Return()

    # Function_47_D2DB end

    def Function_48_D362(): pass

    label("Function_48_D362")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_D46B")

    ChrTalk(    #307
        0x25,
        (
            "#090FHaha. My apologies. I didn't intend that to\x01",
            "become such a serious discussion.\x02\x03",

            "I would much prefer for tonight to be a night\x01",
            "all of this banquet's guests can enjoy rather\x01",
            "than one for serious issues.\x02\x03",

            "Please, do try and enjoy your time here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA13")

    label("loc_D46B")


    ChrTalk(    #308
        0x102,
        (
            "#1040FGood evening, Your Majesty.\x02\x03",

            "Thank you very much for inviting me today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x25,
        (
            "#090FOh, not at all. I'm pleased to see you've come.\x02\x03",

            "I've been eagerly awaiting the day we could\x01",
            "meet again.\x02\x03",

            "I hear you and Estelle have been traveling and\x01",
            "helping with the restoration efforts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x102,
        (
            "#1035FThat's correct. We both wanted to see how\x01",
            "things were across the kingdom with our own\x01",
            "eyes.\x02\x03",

            "#1035FI'm glad we did, too, because now I can finally\x01",
            "breathe a sigh of relief.\x02\x03",

            "#1040FPeople really are strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x25,
        (
            "#094F...That they are.\x02\x03",

            "I have been queen for over forty years, and the\x01",
            "strength of Liberl's citizens continues to amaze\x01",
            "me to this day.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x25, 270, 400)
    Sleep(300)

    ChrTalk(    #312
        0x25,
        (
            "#090FThere are plenty who like to credit either my\x01",
            "abilities as a ruler or orbal technology for this\x01",
            "tiny nation's good fortune...\x02\x03",

            "...but we would be nothing without its people.\x02\x03",

            "I wasn't the one who allowed us to overcome\x01",
            "the recent crisis--or the war ten years ago--\x01",
            "and neither was orbal technology.\x02\x03",

            "#094FNo, I believe it was the will of its people to live.\x01",
            "That's what I believe supports our country, both\x01",
            "then and now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x102,
        "#1042FPeople's will to live?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x25,
        "#090FIndeed.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x102, 400)
    Sleep(300)

    ChrTalk(    #315
        0x25,
        (
            "#090FYou were gracious enough to call this country\x01",
            "your second home, Joshua.\x02\x03",

            "From now on, your will to live will be another\x01",
            "great support for this nation.\x02\x03",

            "As its queen, that makes me happier than you\x01",
            "can imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x102,
        (
            "#1040F...Thank you, Your Majesty.\x02\x03",

            "#1053FYour words mean a lot to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_DA13")

    TalkEnd(0xFE)
    Return()

    # Function_48_D362 end

    def Function_49_DA17(): pass

    label("Function_49_DA17")

    TalkBegin(0xFE)
    OP_8C(0x35, 270, 0)

    ChrTalk(    #317
        0x35,
        (
            "#147FIf you would, Your Highness. A comment in\x01",
            "celebration of the fact that the crisis is past\x01",
            "now.\x02\x03",

            "Just nothing too formal, all right? I'd prefer\x01",
            "somethin' that brings out your bright and\x01",
            "cheery nature.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_DA17 end

    def Function_50_DAF7(): pass

    label("Function_50_DAF7")

    TalkBegin(0xFE)
    OP_8C(0x36, 270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 2)), scpexpr(EXPR_END)), "loc_DBB9")

    ChrTalk(    #318
        0xFE,
        (
            "#156FNial told me not to move on my own, so I'm\x01",
            "stuck here...\x02\x03",

            "#155FI still haven't gotten any foooood... I guess I'll\x01",
            "just have to fill myself up with liquids instead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBFB")

    label("loc_DBB9")


    ChrTalk(    #319
        0xFE,
        (
            "#154FUrrrghh...\x02\x03",

            "Miss Maaaaaaid... I need some foooood...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x32)

    label("loc_DBFB")

    TalkEnd(0xFE)
    Return()

    # Function_50_DAF7 end

    def Function_51_DBFF(): pass

    label("Function_51_DBFF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 7)), scpexpr(EXPR_END)), "loc_DD27")

    ChrTalk(    #320
        0x34,
        (
            "#104F*sigh* I wish it hadn't collapsed all of a sudden\x01",
            "like that to begin with.\x02\x03",

            "If I'd had just one more hour, I could have taken\x01",
            "a research sample, too...\x02\x03",

            "Ah, well. There's no point in lamenting what\x01",
            "you can't do anything about. I'll just have to\x01",
            "make do with what I've got.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF90")

    label("loc_DD27")


    ChrTalk(    #321
        0x34,
        (
            "#101FOh, Joshua!\x02\x03",

            "It's been a long time since I last saw you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x102,
        (
            "#1040FIt's good to see you again, too, Professor.\x02\x03",

            "Although speaking of the last time, I heard\x01",
            "there's a plan in motion to pull up the Liber\x01",
            "Ark from the lake and investigate it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x34,
        (
            "#100FYou heard right! It'll be carried out in\x01",
            "conjunction with the Royal Army.\x02\x03",

            "That's not to say it'll be easy, of course.\x02\x03",

            "Valleria Lake's fairly deep, so we can't start\x01",
            "hauling up bits of the city all willy nilly.\x02\x03",

            "So we're intending to work on making a map\x01",
            "of the lake's bottom using sonar first.\x02\x03",

            "#104FWhich is going to take quite some time as it is...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x27)

    label("loc_DF90")

    TalkEnd(0xFE)
    Return()

    # Function_51_DBFF end

    def Function_52_DF94(): pass

    label("Function_52_DF94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_E06D")

    ChrTalk(    #324
        0x20,
        (
            "#600FWhew... It's a relief to know I was able to\x01",
            "contribute in some way after all.\x02\x03",

            "That said, do come back to Rolent to visit,\x01",
            "Joshua.\x02\x03",

            "I'm sure everyone would be overjoyed to\x01",
            "see how you're doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E371")

    label("loc_E06D")


    ChrTalk(    #325
        0x20,
        (
            "#600FOh, Joshua! It's been quite some time since\x01",
            "I last saw you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x102,
        "#1040FIt has! I didn't know you were here, Mayor Klaus.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x20,
        (
            "#600FThe mayors of each of Liberl's cities and\x01",
            "towns were invited, I believe.\x02\x03",

            "I'm not sure why I was when I didn't do\x01",
            "all that much to contribute to anything,\x01",
            "but I decided to attend nonetheless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x102,
        (
            "#1035FThat's not true at all. I hear the food supplies\x01",
            "that were delivered to Bose and Grancel were\x01",
            "done so on your orders.\x02\x03",

            "#1040FThat was particularly well received here, and\x01",
            "we all know how dire things were at the time.\x02\x03",

            "You've got as much right to be here being\x01",
            "thanked for your efforts as anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x20,
        (
            "#602FI-It was?\x02\x03",

            "#603FWell, that's certainly a relief to hear...\x02\x03",

            "#600FThank you very much for letting me know,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_E371")

    TalkEnd(0xFE)
    Return()

    # Function_52_DF94 end

    def Function_53_E375(): pass

    label("Function_53_E375")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_E45D")

    ChrTalk(    #330
        0x28,
        (
            "#720FThe duke has been a much more positive, \x01",
            "forward-thinking man since that day.\x02\x03",

            "That fact alone makes all I did feel worthwhile.\x02\x03",

            "It feels like a huge weight has been lifted from\x01",
            "my shoulders watching him now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6F6")

    label("loc_E45D")

    OP_8C(0x28, 180, 0)
    OP_62(0x28, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x28, 0x102, 500)
    Sleep(300)

    ChrTalk(    #331
        0x28,
        (
            "#720FAh, good evening to you.\x02\x03",

            "Thank you so much for making the time\x01",
            "to attend tonight's banquet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x102,
        (
            "#1040FOh, not at all. How are you feeling now after\x01",
            "having some time to recover, Phillip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x28,
        (
            "#720FI'm feeling quite well. You're too kind.\x02\x03",

            "I do believe I may have overexerted myself--that's\x01",
            "how things are once you've reached a certain age.\x02\x03",

            "I find myself wondering whether I would have been\x01",
            "able to do more if I were thirty years younger...but\x01",
            "I suppose there's little point in doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x102,
        (
            "#1043F(I wonder what he looked like thirty years ago...)\x02\x03",

            "#1035F(...Nope. Sorry, Phillip. I just can't picture it.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_E6F6")

    TalkEnd(0xFE)
    Return()

    # Function_53_E375 end

    def Function_54_E6FA(): pass

    label("Function_54_E6FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_E771")

    ChrTalk(    #335
        0x29,
        (
            "#710FTonight's party is hosted by Her Majesty\x01",
            "in all her grace.\x02\x03",

            "So I do hope you'll enjoy yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7F9")

    label("loc_E771")


    ChrTalk(    #336
        0x29,
        (
            "#710FWhy, hello, Joshua. \x02\x03",

            "#713FTonight's party is hosted by Her Majesty\x01",
            "in all her grace.\x02\x03",

            "So I do hope you'll enjoy yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)

    label("loc_E7F9")

    TalkEnd(0xFE)
    Return()

    # Function_54_E6FA end

    def Function_55_E7FD(): pass

    label("Function_55_E7FD")

    TalkBegin(0xFE)
    OP_8C(0x22, 270, 0)

    ChrTalk(    #337
        0x22,
        (
            "#780FOh, you needn't worry about us. The academy\x01",
            "suffered no major damage as a result of what\x01",
            "happened.\x02\x03",

            "It was certainly a shock to the students, but\x01",
            "they're all back to their usual, cheery selves\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_55_E7FD end

    def Function_56_E8DB(): pass

    label("Function_56_E8DB")

    TalkBegin(0xFE)
    OP_8C(0x21, 90, 0)

    ChrTalk(    #338
        0x21,
        (
            "#615FI'd heard the academy was actually occupied\x01",
            "by armed assailants at one point.\x02\x03",

            "#618FI was ever so worried when I first heard the\x01",
            "news...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_56_E8DB end

    def Function_57_E97C(): pass

    label("Function_57_E97C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_EAB0")

    ChrTalk(    #339
        0x24,
        (
            "#620FLeft unattended, Mayor Maybelle would likely\x01",
            "work herself into her grave, so it falls to me to\x01",
            "make sure that she rests when necessary.\x02\x03",

            "I'm determined to make sure she takes a good,\x01",
            "long rest after things have settled down enough\x01",
            "in Bose.\x02\x03",

            "#621FI assure you that she's in good hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB6")

    label("loc_EAB0")


    ChrTalk(    #340
        0x24,
        "#620FIt's a pleasure to see you again, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x102,
        "#1040FYou, too, Lila. Have you been well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x24,
        (
            "#621FI have, thank you.\x02\x03",

            "#620FAlthough, I wish I could say the same for the\x01",
            "mayor. She collapsed from overworking herself\x01",
            "the other day.\x02\x03",

            "As such, I had no choice but to force her to\x01",
            "take some time off work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x102,
        "#1044FThat bad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x24,
        (
            "#620FI'm afraid so. She was finally able to rest and\x01",
            "recover enough to my satisfaction, thankfully,\x01",
            "so she's now returned to her duties.\x02\x03",

            "I assure you that she's in good hands.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_ECB6")

    TalkEnd(0xFE)
    Return()

    # Function_57_E97C end

    def Function_58_ECBA(): pass

    label("Function_58_ECBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_EDFF")

    ChrTalk(    #345
        0x23,
        (
            "#803FI'm afraid we've still got a lot of work on our plate.\x01",
            "The orbment factories under ZCF are operating at\x01",
            "less than 28% of their full capacity.\x02\x03",

            "Then we still need to finish rebuilding the Capel's\x01",
            "systems, work on overhauling the Arseille...\x02\x03",

            "#806F*sigh* My workload's not looking lighter any time\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEDE")

    label("loc_EDFF")


    ChrTalk(    #346
        0x23,
        (
            "#806FWhew... It's finally all over...\x02\x03",

            "#803FIt just goes to show that if we endure,\x01",
            "the Goddess will eventually extend Her\x01",
            "hand of salvation to us all.\x02\x03",

            "That's reassuring to know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x102,
        "#1035F(Poor Mr. Murdock...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_EEDE")

    TalkEnd(0xFE)
    Return()

    # Function_58_ECBA end

    def Function_59_EEE2(): pass

    label("Function_59_EEE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 4)), scpexpr(EXPR_END)), "loc_EF97")

    ChrTalk(    #348
        0xFE,
        (
            "I used to be a businessman, so I've been to\x01",
            "my fair share of occasions like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        (
            "...but I've never been to any with this many\x01",
            "famous people in attendance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0BA")

    label("loc_EF97")


    ChrTalk(    #350
        0xFE,
        "This is some party, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        (
            "I don't think you'll find a banquet with a guest\x01",
            "list quite like this anywhere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        (
            "I used to be a businessman, so I've been to\x01",
            "my fair share of occasions like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        (
            "...but I've never been to any with this many\x01",
            "famous people in attendance.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C)

    label("loc_F0BA")

    TalkEnd(0xFE)
    Return()

    # Function_59_EEE2 end

    def Function_60_F0BE(): pass

    label("Function_60_F0BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_F184")

    ChrTalk(    #354
        0x1E,
        (
            "#703FI'm not usually one for praying, but even\x01",
            "I found myself looking to the Goddess\x01",
            "when the Liber Ark started collapsing.\x02\x03",

            "#701FI'm so relieved you all came back to us\x01",
            "unharmed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F4A4")

    label("loc_F184")


    ChrTalk(    #355
        0x1E,
        (
            "#701FGreetings, Joshua.\x02\x03",

            "I'd like to take this chance to thank you again\x01",
            "for all your team did to thwart Ouroboros'\x01",
            "schemes and return peace to Liberl.\x02\x03",

            "The debt of gratitude we owe is beyond measure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x102,
        (
            "#1040FPlease! You're exaggerating, sir.\x02\x03",

            "We might've been the ones who entered the\x01",
            "Liber Ark, but we wouldn't have had a chance\x01",
            "of success if we were on our own.\x02\x03",

            "#1041FIt was only because of you, Richard, Kurt, and\x01",
            "the others fighting on the ground that we were\x01",
            "able to succeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x1E,
        (
            "#701FWe could certainly say the same of you, though.\x01",
            "Although, it IS true that none of us could have\x01",
            "brought about peace alone.\x02\x03",

            "Still, I've been wanting the chance to thank you\x01",
            "personally for all you did.\x02\x03",

            "The faith we had in you to see your work through\x01",
            "to the end was just what we needed to fight.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_F4A4")

    TalkEnd(0xFE)
    Return()

    # Function_60_F0BE end

    def Function_61_F4A8(): pass

    label("Function_61_F4A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 3)), scpexpr(EXPR_END)), "loc_F511")

    ChrTalk(    #358
        0x30,
        (
            "#163FThe Bracer Guild has helped us in a number of\x01",
            "ways recently.\x02\x03",

            "You have my thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F630")

    label("loc_F511")


    ChrTalk(    #359
        0x30,
        (
            "#160F...Oh, it's you.\x02\x03",

            "I've heard you've been lending a hand with the\x01",
            "restoration efforts in addition to all you did with\x01",
            "the Liber Ark.\x02\x03",

            "#163FYou have my thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x102,
        (
            "#1044FY-You're quite welcome, sir... \x01",
            "(I wasn't expecting him to thank me... \x01",
            "I wonder if something happened.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x23)

    label("loc_F630")

    TalkEnd(0xFE)
    Return()

    # Function_61_F4A8 end

    def Function_62_F634(): pass

    label("Function_62_F634")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 7)), scpexpr(EXPR_END)), "loc_F73E")

    ChrTalk(    #361
        0x2C,
        (
            "#760FThe receptionists of all the other branches\x01",
            "were too busy to come today, I'm afraid.\x02\x03",

            "#765FIt would've been nice to get together with\x01",
            "them at some point and exchange info...\x02\x03",

            "#760F...but I suppose that will just have to wait\x01",
            "for another time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8D5")

    label("loc_F73E")


    ChrTalk(    #362
        0x102,
        (
            "#1040FIt's good to see you again, Elnan.\x02\x03",

            "I heard you're here as the Bracer Guild's\x01",
            "representative today. Is that true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x2C,
        (
            "#760FIndeed. All of the other receptionists are busy,\x01",
            "you see. I was the only one able to attend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x102,
        "#1054FThat's too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x2C,
        (
            "#765FIsn't it, though? This would've been a fine time\x01",
            "for us to exchange information.\x02\x03",

            "#760FBut oh, well. There's always tomorrow, as they\x01",
            "say.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1F)

    label("loc_F8D5")

    TalkEnd(0xFE)
    Return()

    # Function_62_F634 end

    SaveToFile()

Try(main)
