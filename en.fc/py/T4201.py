from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4201   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Special Ops Soldier',                  # 9
        'Special Ops Soldier',                  # 10
        'Head Maid Hilda',                      # 11
        'Captain Amalthea',                     # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Special Ops Soldier',                  # 15
        'Special Ops Soldier',                  # 16
        'Special Ops Soldier',                  # 17
        'Special Ops Soldier',                  # 18
        'Special Ops Soldier',                  # 19
        'Kloe',                                 # 20
        'Olivier',                              # 21
        'Agate',                                # 22
        'Scherazard',                           # 23
        'Zin',                                  # 24
        'Tita',                                 # 25
        'Professor Russell',                    # 26
        'Cassius',                              # 27
        'Nial',                                 # 28
        'Dorothy',                              # 29
        'Major Cid',                            # 30
        'General Morgan',                       # 31
        '1st Lieutenant Schwarz',               # 32
        'Queen Alicia',                         # 33
        'Mylene',                               # 34
        'Mayor Klaus',                          # 35
        'Lila',                                 # 36
        'Mayor Maybelle',                       # 37
        'Dean Collins',                         # 38
        'Factory Chief Murdock',                # 39
        'Royal Guardsman',                      # 40
        'Royal Guardsman',                      # 41
        'Royal Guardsman',                      # 42
        'Royal Guardsman',                      # 43
        'Royal Guardsman',                      # 44
        'Royal Guardsman',                      # 45
        'Royal Guardsman',                      # 46
        'Royal Guardsman',                      # 47
        'Royal Guardsman',                      # 48
        'Royal Guardsman',                      # 49
        'Joshua',                               # 50
        'Mechanic Payton',                      # 51
        'Special Ops Frigate',                  # 52
        'Special Ops Frigate Shadow',           # 53
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01610 ._CH',             # 00
        'ED6_DT07/CH02460 ._CH',             # 01
        'ED6_DT07/CH02230 ._CH',             # 02
        'ED6_DT07/CH02240 ._CH',             # 03
        'ED6_DT07/CH02100 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00101 ._CH',             # 06
        'ED6_DT07/CH00120 ._CH',             # 07
        'ED6_DT07/CH00121 ._CH',             # 08
        'ED6_DT07/CH00140 ._CH',             # 09
        'ED6_DT07/CH00141 ._CH',             # 0A
        'ED6_DT06/CH20143 ._CH',             # 0B
        'ED6_DT07/CH00030 ._CH',             # 0C
        'ED6_DT07/CH00050 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00070 ._CH',             # 0F
        'ED6_DT07/CH00060 ._CH',             # 10
        'ED6_DT07/CH02020 ._CH',             # 11
        'ED6_DT07/CH02000 ._CH',             # 12
        'ED6_DT07/CH02060 ._CH',             # 13
        'ED6_DT06/CH20064 ._CH',             # 14
        'ED6_DT07/CH02450 ._CH',             # 15
        'ED6_DT07/CH02080 ._CH',             # 16
        'ED6_DT07/CH02090 ._CH',             # 17
        'ED6_DT07/CH02010 ._CH',             # 18
        'ED6_DT07/CH01180 ._CH',             # 19
        'ED6_DT07/CH02350 ._CH',             # 1A
        'ED6_DT07/CH02370 ._CH',             # 1B
        'ED6_DT07/CH02360 ._CH',             # 1C
        'ED6_DT07/CH02600 ._CH',             # 1D
        'ED6_DT07/CH02620 ._CH',             # 1E
        'ED6_DT06/CH20127 ._CH',             # 1F
        'ED6_DT06/CH20030 ._CH',             # 20
        'ED6_DT07/CH00010 ._CH',             # 21
        'ED6_DT07/CH00441 ._CH',             # 22
        'ED6_DT06/CH20042 ._CH',             # 23
        'ED6_DT06/CH20040 ._CH',             # 24
        'ED6_DT07/CH00440 ._CH',             # 25
        'ED6_DT07/CH00340 ._CH',             # 26
        'ED6_DT07/CH00341 ._CH',             # 27
        'ED6_DT07/CH00280 ._CH',             # 28
        'ED6_DT07/CH00281 ._CH',             # 29
        'ED6_DT07/CH01330 ._CH',             # 2A
        'ED6_DT06/CH20128 ._CH',             # 2B
        'ED6_DT07/CH01450 ._CH',             # 2C
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT07/CH02460P._CP',             # 01
        'ED6_DT07/CH02230P._CP',             # 02
        'ED6_DT07/CH02240P._CP',             # 03
        'ED6_DT07/CH02100P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00101P._CP',             # 06
        'ED6_DT07/CH00120P._CP',             # 07
        'ED6_DT07/CH00121P._CP',             # 08
        'ED6_DT07/CH00140P._CP',             # 09
        'ED6_DT07/CH00141P._CP',             # 0A
        'ED6_DT06/CH20143P._CP',             # 0B
        'ED6_DT07/CH00030P._CP',             # 0C
        'ED6_DT07/CH00050P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00070P._CP',             # 0F
        'ED6_DT07/CH00060P._CP',             # 10
        'ED6_DT07/CH02020P._CP',             # 11
        'ED6_DT07/CH02000P._CP',             # 12
        'ED6_DT07/CH02060P._CP',             # 13
        'ED6_DT06/CH20064P._CP',             # 14
        'ED6_DT07/CH02450P._CP',             # 15
        'ED6_DT07/CH02080P._CP',             # 16
        'ED6_DT07/CH02090P._CP',             # 17
        'ED6_DT07/CH02010P._CP',             # 18
        'ED6_DT07/CH01180P._CP',             # 19
        'ED6_DT07/CH02350P._CP',             # 1A
        'ED6_DT07/CH02370P._CP',             # 1B
        'ED6_DT07/CH02360P._CP',             # 1C
        'ED6_DT07/CH02600P._CP',             # 1D
        'ED6_DT07/CH02620P._CP',             # 1E
        'ED6_DT06/CH20127P._CP',             # 1F
        'ED6_DT06/CH20030P._CP',             # 20
        'ED6_DT07/CH00010P._CP',             # 21
        'ED6_DT07/CH00441P._CP',             # 22
        'ED6_DT06/CH20042P._CP',             # 23
        'ED6_DT06/CH20040P._CP',             # 24
        'ED6_DT07/CH00440P._CP',             # 25
        'ED6_DT07/CH00340P._CP',             # 26
        'ED6_DT07/CH00341P._CP',             # 27
        'ED6_DT07/CH00280P._CP',             # 28
        'ED6_DT07/CH00281P._CP',             # 29
        'ED6_DT07/CH01330P._CP',             # 2A
        'ED6_DT06/CH20128P._CP',             # 2B
        'ED6_DT07/CH01450P._CP',             # 2C
    )

    DeclNpc(
        X                   = -870,
        Z                   = 19750,
        Y                   = 107200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 910,
        Z                   = 19750,
        Y                   = 107200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1110,
        Z                   = 15350,
        Y                   = 56390,
        Direction           = 235,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -4710,
        Y                   = 18000,
        Z                   = 94670,
        Range               = 5130,
        Unknown_10          = 0x3E80,
        Unknown_14          = 0x16A1C,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -4340,
        Y                   = 19000,
        Z                   = 105990,
        Range               = 4220,
        Unknown_10          = 0x4650,
        Unknown_14          = 0x1933E,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -4280,
        Y                   = 16000,
        Z                   = 78500,
        Range               = 5010,
        Unknown_10          = 0x32C8,
        Unknown_14          = 0x1270A,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -4730,
        Y                   = 18000,
        Z                   = 98010,
        Range               = 4880,
        Unknown_10          = 0x3E80,
        Unknown_14          = 0x17534,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = 32759,
        Y                   = 15500,
        Z                   = 76820,
        Range               = 35080,
        Unknown_10          = 0x4074,
        Unknown_14          = 0x116D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -4340,
        Y                   = 21000,
        Z                   = 108990,
        Range               = 4220,
        Unknown_10          = 0x4268,
        Unknown_14          = 0x19EF6,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )


    ScpFunction(
        "Function_0_872",          # 00, 0
        "Function_1_948",          # 01, 1
        "Function_2_B5B",          # 02, 2
        "Function_3_B71",          # 03, 3
        "Function_4_CD0",          # 04, 4
        "Function_5_F17",          # 05, 5
        "Function_6_1CD6",         # 06, 6
        "Function_7_2226",         # 07, 7
        "Function_8_2A29",         # 08, 8
        "Function_9_2F8F",         # 09, 9
        "Function_10_2FBD",        # 0A, 10
        "Function_11_2FF0",        # 0B, 11
        "Function_12_3023",        # 0C, 12
        "Function_13_38F2",        # 0D, 13
        "Function_14_3C26",        # 0E, 14
        "Function_15_3DA5",        # 0F, 15
        "Function_16_4099",        # 10, 16
        "Function_17_4613",        # 11, 17
        "Function_18_468C",        # 12, 18
        "Function_19_5D70",        # 13, 19
    )


    def Function_0_872(): pass

    label("Function_0_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_889")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_8A0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_8AE")
    OP_A3(0x3FC)
    Event(0, 16)

    label("loc_8AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_8BC")
    OP_A3(0x3FD)
    Event(0, 17)

    label("loc_8BC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_8CC"),
        (101, "loc_8E2"),
        (SWITCH_DEFAULT, "loc_8F8"),
    )


    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DF")
    OP_A2(0x63D)
    Event(0, 4)

    label("loc_8DF")

    Jump("loc_8F8")

    label("loc_8E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F5")
    OP_A2(0x645)
    Event(0, 7)

    label("loc_8F5")

    Jump("loc_8F8")

    label("loc_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_END)), "loc_909")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_91D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_947")

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_947")
    SetChrChipByIndex(0x0, 1)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_947")

    Return()

    # Function_0_872 end

    def Function_1_948(): pass

    label("Function_1_948")

    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_965")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97A")

    label("loc_965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5A")
    OP_1B(0x0, 0x0, 0xE)
    OP_A1(0x33, 0x0)
    OP_A1(0x34, 0x1)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x400)
    OP_71(0x0, 0x40)
    OP_72(0x1, 0x4)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x400)
    OP_71(0x1, 0x40)
    SetChrPos(0x33, 2320, 12050, 57280, 56)
    SetChrPos(0x34, 2320, 12050, 57280, 56)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x4)
    SetChrFlags(0x32, 0x400)
    OP_6F(0x0, 360)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_END)), "loc_A5C")
    SetChrPos(0x8, -7920, 12000, 56580, 94)
    SetChrPos(0x9, -9260, 12000, 57540, 284)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 35)
    SetChrChipByIndex(0x9, 35)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_END)), "loc_AF3")
    SetChrPos(0xE, 3890, 14000, 79000, 146)
    SetChrPos(0xF, 3080, 14000, 77370, 283)
    SetChrPos(0x10, 6700, 14000, 78300, 358)
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 35)
    SetChrChipByIndex(0xF, 35)
    SetChrChipByIndex(0x10, 35)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0xE, 0x800)
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0x10, 0x800)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_END)), "loc_B5A")
    SetChrPos(0x11, -2160, 18000, 102100, 309)
    SetChrPos(0x12, 2230, 18000, 101600, 82)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x1)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x12, 0x800)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 35)
    SetChrChipByIndex(0x12, 35)

    label("loc_B5A")

    Return()

    # Function_1_948 end

    def Function_2_B5B(): pass

    label("Function_2_B5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B70")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_B5B")

    label("loc_B70")

    Return()

    # Function_2_B5B end

    def Function_3_B71(): pass

    label("Function_3_B71")

    TalkBegin(0x32)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Modify/Exchange\x01",      # 1
            "Buy\x01",                  # 2
            "Leave\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE0")
    OP_0D()
    OP_A9(0x6C)
    OP_56(0x0)
    TalkEnd(0x32)
    Return()

    label("loc_BE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF9")
    OP_0D()
    OP_A9(0x6D)
    OP_56(0x0)
    TalkEnd(0x32)
    Return()

    label("loc_BF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0A")
    TalkEnd(0x32)
    Return()

    label("loc_C0A")


    ChrTalk(    #0
        0x32,
        (
            "Just in case, I can make any\x01",
            "adjustments necessary to your\x01",
            "orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x32,
        (
            "I don't have much in the way\x01",
            "of variety, but I did make sure\x01",
            "to keep some tools handy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x32,
        "Holler if you need me.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x32)
    Return()

    # Function_3_B71 end

    def Function_4_CD0(): pass

    label("Function_4_CD0")

    EventBegin(0x0)
    OP_6D(31020, 10750, 79090, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 29890, 10750, 79270, 0)
    SetChrPos(0x102, 31020, 10750, 79090, 0)

    def lambda_D37():
        OP_8E(0xFE, 0x6CB6, 0x2EE0, 0x172E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D37)

    def lambda_D52():
        OP_8E(0xFE, 0x722E, 0x2EE0, 0x1730E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D52)

    def lambda_D6D():
        OP_6D(29660, 12000, 100020, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D6D)

    def lambda_D85():
        OP_67(0, 5000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D85)

    def lambda_D9D():
        OP_6C(12000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D9D)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #3
        0x101,
        (
            "#000FOh, wow...\x01",
            "Check that out...\x02\x03",

            "This must be the castle's\x01",
            "Garden Terrace...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #4
        0x102,
        (
            "#010FI'd say so... You can see the\x01",
            "whole lake from here, and it\x01",
            "overlooks the town, too.\x02\x03",

            "They could call this the Million\x01",
            "Mira Night View, or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#000F*sigh*... As nice as this is,\x01",
            "we really don't have time to\x01",
            "stop and enjoy it.\x02\x03",

            "We've got a job to do.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_CD0 end

    def Function_5_F17(): pass

    label("Function_5_F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_END)), "loc_F1F")
    Return()

    label("loc_F1F")

    OP_A2(0x63E)
    OP_28(0x49, 0x1, 0x400)
    EventBegin(0x0)
    OP_8C(0x101, 0, 0)
    OP_8C(0x102, 0, 0)

    ChrTalk(    #6
        0x101,
        "#000FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#010FThis must be the Royal Keep...\x02",
    )

    CloseMessageWindow()

    def lambda_F77():
        OP_8E(0xFE, 0xFFFFFCAE, 0x4650, 0x19438, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F77)

    def lambda_F92():
        OP_8E(0xFE, 0x438, 0x4650, 0x194BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F92)
    OP_6D(0, 20000, 107640, 3000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x8,
        "Hmm? Who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "Hey, you two...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #10
        0x101,
        (
            "#000FUmmm...\x02\x03",

            "We're here as guests\x01",
            "of the duke...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #11
        0x102,
        "#010FIs this where Her Majesty lives?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        "Of course it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "But for the last few days, she\x01",
            "hasn't been feeling so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "She's not seeing anyone\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#000FO-Oh, you've got it all wrong. We\x01",
            "weren't even thinking of that.\x02\x03",

            "I just thought it would be\x01",
            "amazing if she were to even\x01",
            "take notice of us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#010FDoes Princess Klaudia sleep\x01",
            "here, as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "No, it's just--\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 800)

    ChrTalk(    #18
        0x9,
        "...Hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "The princess is focused on\x01",
            "looking after Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "Neither of them has time to\x01",
            "deal with the likes of you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 280, 20000, 111970, 0)

    ChrTalk(    #21
        0xA,
        (
            "Might I inquire as to what's\x01",
            "going on here?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)

    def lambda_12BD():
        OP_8E(0xFE, 0x82, 0x4C2C, 0x1A13A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_12BD)

    def lambda_12D8():

        label("loc_12D8")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_12D8")

    QueueWorkItem2(0x8, 1, lambda_12D8)

    def lambda_12E9():
        OP_8E(0xFE, 0xFFFFF9FC, 0x4D26, 0x1A22A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_12E9)

    def lambda_1304():

        label("loc_1304")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1304")

    QueueWorkItem2(0x9, 1, lambda_1304)

    def lambda_1315():
        OP_8E(0xFE, 0xFFFFFA24, 0x4B32, 0x19EEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1315)
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #22
        0x8,
        "Madam...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "We didn't know you were\x01",
            "back already.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #24
        0xA,
        (
            "#710FThe dinner party will be starting soon, so\x01",
            "I will be returning to the maid quarters.\x02\x03",

            "And who are our guests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "They're from the team that won\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "It's only because of that victory\x01",
            "that someone of a bracer's social\x01",
            "standing would ever be invited here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#000FA 'bracer's social standing'...?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #28
        0xA,
        "Such discourtesy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "You would insult those who\x01",
            "were personally invited to\x01",
            "the royal castle?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #30
        0x8,
        (
            "No...\x01",
            "That's not what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "Those invited by the duke should be\x01",
            "treated with all the respect due to\x01",
            "those invited by Her Majesty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "I sincerely hope you have\x01",
            "not forgotten that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "...U-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#000F(Wow, she's intense...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#010F(I wonder who she is...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "But, madam... We can't just\x01",
            "allow them to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "Surely you understand the reasons\x01",
            "that the colonel laid out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "...Yes, and I'm quite tired of\x01",
            "hearing them repeated to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0x8C, 0x493E, 0x19C12, 0x7D0, 0x0)

    ChrTalk(    #39
        0xA,
        (
            "I am terribly sorry,\x01",
            "sir and madam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "Security has been heightened, and\x01",
            "as such, the Royal Keep and its\x01",
            "surroundings are off limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "If I may ask, would you mind\x01",
            "waiting in your room until the\x01",
            "dinner party begins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#000FAh... A-All right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#010FThat's fine.\x01",
            "We'll do as you ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#010FI apologize. We weren't trying\x01",
            "to cause any trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #45
        0x8,
        "Hmph...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #46
        0x9,
        (
            "Fine, then. Just don't let\x01",
            "it happen again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #47
        0xA,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        "Uh... S-Safe return to you.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(470, 15250, 86110, 0)
    SetChrPos(0x101, -620, 15500, 86640, 180)
    SetChrPos(0x102, 1430, 15500, 86590, 180)
    SetChrPos(0xA, 310, 15000, 85930, 180)

    def lambda_197C():

        label("loc_197C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_197C")

    QueueWorkItem2(0x101, 1, lambda_197C)

    def lambda_198D():

        label("loc_198D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_198D")

    QueueWorkItem2(0x102, 1, lambda_198D)

    def lambda_199E():
        OP_8E(0xFE, 0xFFFFFF24, 0x36B0, 0x139A2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_199E)

    def lambda_19B9():
        OP_8E(0xFE, 0xFFFFFC72, 0x36B0, 0x13D4E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19B9)

    def lambda_19D4():
        OP_8E(0xFE, 0x1EA, 0x36B0, 0x13EAC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_19D4)

    def lambda_19EF():
        OP_6D(-90, 14000, 81270, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19EF)
    WaitChrThread(0xA, 0x1)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #49
        0xA,
        (
            "I apologize that you were subjected\x01",
            "to such dreadful behavior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        "My name is Hilda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "I am the head maid of Grancel\x01",
            "Castle, and I oversee all of\x01",
            "the housekeeping duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#000FAh-ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#010FWe had a feeling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "#710FHmm?\x02\x03",

            "Forgive my rudeness, but are\x01",
            "we previously acquainted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#000FWell, uh... Someone told us\x01",
            "about you.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0xA, 0x258, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #56
        "\x07\x05Handed 'Julia's Letter' to Hilda.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x101, 0xFFFFFC72, 0x36B0, 0x13D4E, 0x7D0, 0x0)

    ChrTalk(    #57
        0xA,
        "#710FI know this handwriting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#000FYou see?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#010FWe also have our bracer emblems\x01",
            "and identification with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        (
            "#710FI see...\x02\x03",

            "Please, come with me to the\x01",
            "maids' sitting room.\x02\x03",

            "We can discuss the matter\x01",
            "further once we are there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4214   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_F17 end

    def Function_6_1CD6(): pass

    label("Function_6_1CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CE3")
    Return()

    label("loc_1CE3")

    OP_A2(0x643)
    OP_28(0x4A, 0x1, 0x80)
    EventBegin(0x0)
    Fade(1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x138, 1)
    SetChrPos(0x138, 10, 18500, 104830, 0)
    SetChrPos(0x101, -470, 18000, 103350, 0)
    SetChrPos(0x102, 740, 18000, 103280, 0)
    OP_6D(-70, 19000, 105810, 3000)

    ChrTalk(    #61
        0x8,
        "Hilda...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "What business do you have with\x01",
            "Her Majesty at this hour?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x138,
        (
            "#710FI'm bringing some tea and\x01",
            "spoons at her request.\x02\x03",

            "The current situation means that Her Majesty\x01",
            "is denied the right to even go about her daily\x01",
            "life as she wishes, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "Such harsh words...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "Who are these maids with you?\x01",
            "I don't recognize them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x138,
        (
            "#710FHis Grace ordered me to\x01",
            "hire on some additional staff\x01",
            "to help.\x02\x03",

            "They've only just arrived\x01",
            "at the castle today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        "Really, now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        "Hey, you're pretty cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#000FTh-Thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        "#010F...(*bows*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        "Huh?\x02",
    )

    CloseMessageWindow()
    OP_90(0x8, 0x0, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)

    ChrTalk(    #73
        0x8,
        (
            "Why do I get the feeling\x01",
            "we've met before...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 800)

    ChrTalk(    #74
        0x101,
        "#000F(Crap...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x138,
        (
            "#710FDo you stare so hard at every\x01",
            "young lady you see?\x02\x03",

            "I do hope you're not thinking\x01",
            "any untoward thoughts.\x02\x03",

            "I rather think that His Grace\x01",
            "and the colonel would disapprove.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20AA():
        OP_8C(0xFE, 0, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20AA)

    ChrTalk(    #76
        0x8,
        "H-Hey! It's not like that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "We're the elite of the Royal Army.\x01",
            "We wouldn't do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x138,
        (
            "#710FAll's well, then.\x02\x03",

            "Now, will you please allow\x01",
            "us to pass?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        "Pardon us, ladies!\x02",
    )

    CloseMessageWindow()

    def lambda_2171():
        OP_8F(0xFE, 0xFFFFF704, 0x4C2C, 0x1A194, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2171)

    ChrTalk(    #80
        0x9,
        "Please, go ahead!\x02",
    )

    CloseMessageWindow()

    def lambda_21A3():
        OP_8F(0xFE, 0x92E, 0x4C2C, 0x1A13A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_21A3)
    FadeToDark(2000, 0, -1)

    def lambda_21C8():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_21C8)
    Sleep(50)

    def lambda_21E8():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21E8)

    def lambda_2203():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2203)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4230   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1CD6 end

    def Function_7_2226(): pass

    label("Function_7_2226")

    EventBegin(0x0)
    OP_6D(-220, 20000, 107550, 0)
    SetChrPos(0x8, -2390, 19500, 107000, 180)
    SetChrPos(0x9, 2290, 19500, 106980, 180)

    def lambda_2261():

        label("loc_2261")

        TurnDirection(0xFE, 0x138, 0)
        OP_48()
        Jump("loc_2261")

    QueueWorkItem2(0x8, 2, lambda_2261)

    def lambda_2272():

        label("loc_2272")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2272")

    QueueWorkItem2(0x9, 2, lambda_2272)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x138, 1)
    SetChrPos(0x101, -990, 20000, 110860, 180)
    SetChrPos(0x102, 1070, 20000, 111050, 0)
    SetChrPos(0x138, 120, 20000, 110230, 180)

    def lambda_22C5():
        OP_8E(0xFE, 0xBE, 0x4B32, 0x19F64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_22C5)

    def lambda_22E0():
        OP_8E(0xFE, 0xFFFFFE20, 0x4D26, 0x1A310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22E0)

    def lambda_22FB():
        OP_8E(0xFE, 0x35C, 0x4D26, 0x1A310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22FB)
    WaitChrThread(0x138, 0x1)
    TurnDirection(0x138, 0x8, 400)

    ChrTalk(    #81
        0x8,
        (
            "Are you going home for\x01",
            "the day, Miss Hilda?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x138,
        (
            "#710FYes, I believe so.\x02\x03",

            "Just be sure not to do Her Majesty\x01",
            "any further discourtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        "That's not fair...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "But please, relax. We are\x01",
            "patriots to the core.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x138,
        (
            "#710FThat's good to hear.\x02\x03",

            "Now, I believe that we shall\x01",
            "be on our way.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(    #86
        0x101,
        "#000FP-Pardon me...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(    #87
        0x102,
        "#010FBy your leave...\x02",
    )

    CloseMessageWindow()

    def lambda_2488():
        OP_6D(230, 19000, 105820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2488)

    def lambda_24A0():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_24A0)
    Sleep(100)

    def lambda_24C0():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24C0)

    def lambda_24DB():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24DB)

    def lambda_24F6():
        OP_8F(0xFE, 0xFFFFFC9A, 0x4D26, 0x1A388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24F6)

    def lambda_2511():
        OP_8F(0xFE, 0x38E, 0x4D26, 0x1A388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2511)
    Sleep(1300)

    ChrTalk(    #88
        0x8,
        "By the way, ladies...\x02",
    )

    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    CloseMessageWindow()

    def lambda_2587():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_2587)

    def lambda_2595():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2595)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #89
        0x101,
        "#000F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "I don't think we ever\x01",
            "got your names.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        "May we ask them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#000FI, uh, um...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Lena\x01",         # 0
            "Schera\x01",       # 1
            "Dorothy\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2674"),
        (1, "loc_26EE"),
        (2, "loc_27CE"),
        (SWITCH_DEFAULT, "loc_2862"),
    )


    label("loc_2674")

    OP_A2(0x676)

    ChrTalk(    #93
        0x8,
        "My... Isn't that a lovely name?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "It has a pleasant ring to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#000FI...uh...\x01",
            "Th-Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2862")

    label("loc_26EE")

    OP_A2(0x677)

    ChrTalk(    #96
        0x8,
        (
            "My...\x01",
            "That's certainly a sexy name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        "You don't...look like a 'Schera,' though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#000FH-Hey! Watch your mouth!\x02\x03",

            "...Ho ho ho! Did I catch\x01",
            "you off-guard?\x02\x03",

            "S-See? I'm a very assertive,\x01",
            "s-s-sexy young woman!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2862")

    label("loc_27CE")

    OP_A2(0x678)

    ChrTalk(    #99
        0x8,
        (
            "Hmm...\x01",
            "That's a very modern name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "Pardon my saying so, but it just\x01",
            "doesn't sound right for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#000F(Ain't THAT the truth...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2862")

    label("loc_2862")


    ChrTalk(    #102
        0x9,
        "And how about you, miss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        "#010FYou may call me Karin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "Karin, you say...?\x01",
            "That's a very pretty name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#010FYou're too kind, sir.\x02\x03",

            "I'm rather fond of it myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        "Are you, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "Oh! Right. We're with the\x01",
            "Special Ops. My name is--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x138,
        (
            "#710FI think that's just about enough.\x02\x03",

            "I sense an ulterior motive at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        (
            "No... I mean, at least\x01",
            "not from us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x138,
        "#710F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "Eep! P-Please, be safe on\x01",
            "your way home.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 1)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    Return()

    # Function_7_2226 end

    def Function_8_2A29(): pass

    label("Function_8_2A29")

    EventBegin(0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_6F(0x2, 450)
    OP_72(0x2, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x9, 0x1)
    SetChrPos(0xB, 20, 12000, 46990, 180)
    SetChrPos(0x8, 940, 12000, 48110, 180)
    SetChrPos(0x9, -900, 12000, 48110, 180)
    SetChrChipByIndex(0x8, 42)
    SetChrChipByIndex(0x9, 42)
    SetChrPos(0xC, -60, 12000, 51430, 180)
    SetChrPos(0xD, 930, 12000, 52730, 180)
    SetChrPos(0xE, 930, 12000, 54640, 180)
    SetChrPos(0xF, 910, 12000, 56310, 180)
    SetChrPos(0x10, -890, 12000, 52760, 180)
    SetChrPos(0x11, -890, 12000, 54510, 180)
    SetChrPos(0x12, -890, 12000, 56510, 180)
    SetChrFlags(0x32, 0x80)
    OP_6D(-1980, 12000, 40200, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(51000, 0)
    OP_6E(280, 0)
    OP_6D(10, 12000, 46910, 2000)

    ChrTalk(    #112
        0xB,
        (
            "#187F#6PSomeone had BETTER tell me this is\x01",
            "a bad joke. Why is the gate open...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xC,
        "#3PY-Your orders, Captain?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "#3PEnemies could breach the\x01",
            "castle at any moment!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C38():
        OP_6D(-10, 12000, 48330, 800)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2C38)
    OP_8C(0xB, 0, 600)
    WaitChrThread(0xB, 0x2)

    ChrTalk(    #115
        0xB,
        (
            "#185F#4PAll remaining members of the\x01",
            "first platoon to the Foyer!\x01",
            "On the double!!\x02\x03",

            "Allow no one to enter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        "#3PY-Yes, ma'am!\x02",
    )

    CloseMessageWindow()

    def lambda_2CE0():

        label("loc_2CE0")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2CE0")

    QueueWorkItem2(0xD, 1, lambda_2CE0)

    def lambda_2CF1():

        label("loc_2CF1")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2CF1")

    QueueWorkItem2(0xE, 1, lambda_2CF1)

    def lambda_2D02():

        label("loc_2D02")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2D02")

    QueueWorkItem2(0xF, 1, lambda_2D02)

    def lambda_2D13():

        label("loc_2D13")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2D13")

    QueueWorkItem2(0x10, 1, lambda_2D13)

    def lambda_2D24():

        label("loc_2D24")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2D24")

    QueueWorkItem2(0x11, 1, lambda_2D24)

    def lambda_2D35():

        label("loc_2D35")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2D35")

    QueueWorkItem2(0x12, 1, lambda_2D35)
    SetChrChipByIndex(0xC, 34)
    OP_8E(0xC, 0x906, 0x2EE0, 0xC936, 0x1770, 0x0)
    OP_8E(0xC, 0x906, 0x2EE0, 0xCDC8, 0x1770, 0x0)
    OP_43(0xD, 0x1, 0x0, 0x9)
    OP_43(0x10, 0x1, 0x0, 0x9)
    OP_8E(0xC, 0x906, 0x2EE0, 0xD476, 0x1770, 0x0)
    OP_43(0xE, 0x1, 0x0, 0xA)
    OP_43(0x11, 0x1, 0x0, 0xA)
    OP_8E(0xC, 0x906, 0x2EE0, 0xDF66, 0x1770, 0x0)
    OP_43(0xF, 0x1, 0x0, 0xB)
    OP_43(0x12, 0x1, 0x0, 0xB)

    def lambda_2DC5():
        OP_8E(0xFE, 0x92E, 0x2EE0, 0x11FE4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DC5)
    OP_6D(10, 12000, 46910, 1000)

    ChrTalk(    #117
        0xB,
        (
            "#186F#4PWhat a disgrace...\x02\x03",

            "If the enemy is not routed\x01",
            "before I have to report to\x01",
            "His Excellency...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #118
        0x8,
        "#3PC-Captain!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x9,
        "#3PSpecial Ops Frigate inbound!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0xB, 180, 600)

    ChrTalk(    #120
        0xB,
        "#187F#6PDamn it! So that was their ploy?!\x02",
    )

    CloseMessageWindow()

    def lambda_2F3B():
        OP_6D(-9190, 19050, 36880, 1500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2F3B)

    def lambda_2F53():
        OP_67(0, 3900, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2F53)

    def lambda_2F6B():
        OP_6B(3220, 1500)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_2F6B)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/E0500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2A29 end

    def Function_9_2F8F(): pass

    label("Function_9_2F8F")

    SetChrChipByIndex(0xFE, 34)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0xCD96, 0x1770, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11FE4, 0x1770, 0x0)
    Return()

    # Function_9_2F8F end

    def Function_10_2FBD(): pass

    label("Function_10_2FBD")

    Sleep(800)
    SetChrChipByIndex(0xFE, 34)
    OP_8E(0xFE, 0x8F2, 0x2EE0, 0xD462, 0x1770, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11FE4, 0x1770, 0x0)
    Return()

    # Function_10_2FBD end

    def Function_11_2FF0(): pass

    label("Function_11_2FF0")

    Sleep(1300)
    SetChrChipByIndex(0xFE, 34)
    OP_8E(0xFE, 0x8F2, 0x2EE0, 0xDBC4, 0x1388, 0x0)
    OP_8E(0xFE, 0x92E, 0x2EE0, 0x11FE4, 0x1388, 0x0)
    Return()

    # Function_11_2FF0 end

    def Function_12_3023(): pass

    label("Function_12_3023")

    EventBegin(0x0)
    SetChrFlags(0x32, 0x80)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x4, 0xFF)
    AddParty(0x2, 0xFF)
    OP_6D(1980, 20950, 57340, 0)
    OP_67(0, 9340, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(340000, 0)
    OP_6E(413, 0)
    SetChrPos(0x8, -8810, 12000, 57910, 79)
    SetChrPos(0xB, -7640, 12000, 58590, 125)
    SetChrPos(0x9, -6650, 12000, 57720, 46)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x9, 0x1)

    def lambda_30CB():

        label("loc_30CB")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_30CB")

    QueueWorkItem2(0xB, 1, lambda_30CB)

    def lambda_30DC():

        label("loc_30DC")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_30DC")

    QueueWorkItem2(0x8, 1, lambda_30DC)

    def lambda_30ED():

        label("loc_30ED")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_30ED")

    QueueWorkItem2(0x9, 1, lambda_30ED)
    SetChrChipByIndex(0xB, 40)
    SetChrChipByIndex(0x8, 38)
    SetChrChipByIndex(0x9, 38)
    OP_A1(0x33, 0x0)
    OP_A1(0x34, 0x1)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x400)
    OP_71(0x0, 0x40)
    OP_72(0x1, 0x4)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x400)
    OP_71(0x1, 0x40)
    OP_6F(0x0, 1021)
    SetChrFlags(0x33, 0x4)
    SetChrFlags(0x34, 0x4)
    SetChrFlags(0x33, 0x40)
    SetChrFlags(0x34, 0x40)
    SetChrPos(0x101, 2880, 15350, 57740, 147)
    SetChrPos(0x103, 2880, 15350, 57740, 147)
    SetChrPos(0x105, 2880, 15350, 57740, 147)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x105, 0x80)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    SetChrPos(0x33, 2320, 22050, 57280, 56)
    SetChrPos(0x34, 2320, 12050, 57280, 56)

    def lambda_31D2():
        OP_6D(610, 15350, 55470, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_31D2)

    def lambda_31EA():
        OP_67(0, 5210, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_31EA)

    def lambda_3202():
        OP_6C(29000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3202)
    FadeToBright(2000, 0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 1110)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x34, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0x33, 0x0, 0xFFFFF448, 0x0, 0xBB8, 0x0)
    OP_91(0x33, 0x0, 0xFFFFF830, 0x0, 0x9C4, 0x0)
    OP_91(0x33, 0x0, 0xFFFFFC18, 0x0, 0x7D0, 0x0)
    PlayEffect(0x1, 0x2, 0x34, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_91(0x33, 0x0, 0xFFFFF830, 0x0, 0x7D0, 0x0)
    OP_91(0x33, 0x0, 0xFFFFFC18, 0x0, 0x5DC, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_8F(0x33, 0x910, 0x2F12, 0xDFC0, 0x3E8, 0x0)
    OP_22(0xC8, 0x0, 0x64)
    OP_23(0x79)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)

    def lambda_333C():
        OP_67(0, 7370, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_333C)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0x0, 0x78)
    OP_6F(0x0, 61)
    OP_70(0x0, 0xE6)
    OP_73(0x0)
    OP_B0(0x0, 0x3C)
    OP_6F(0x0, 231)
    OP_70(0x0, 0x168)
    OP_73(0x0)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x0, 1140)
    OP_70(0x0, 0x4B0)
    OP_73(0x0)

    def lambda_3399():

        label("loc_3399")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3399")

    QueueWorkItem2(0x101, 1, lambda_3399)

    def lambda_33AA():

        label("loc_33AA")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_33AA")

    QueueWorkItem2(0x105, 1, lambda_33AA)

    def lambda_33BB():

        label("loc_33BB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_33BB")

    QueueWorkItem2(0x103, 1, lambda_33BB)

    def lambda_33CC():
        OP_6D(-7140, 12000, 55690, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_33CC)

    def lambda_33E4():
        OP_6E(577, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_33E4)

    def lambda_33F4():
        OP_67(0, 5360, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_33F4)

    def lambda_340C():
        OP_6C(13000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_340C)

    def lambda_341C():
        OP_6B(1600, 3000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_341C)
    ClearChrFlags(0x101, 0x80)

    def lambda_3431():
        OP_8E(0xFE, 0xFFFFECB4, 0x31A6, 0xD00C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3431)
    Sleep(300)
    ClearChrFlags(0x103, 0x80)

    def lambda_3456():
        OP_8E(0xFE, 0xFFFFE3C2, 0x2EE0, 0xC8F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3456)
    Sleep(300)
    ClearChrFlags(0x105, 0x80)

    def lambda_347B():
        OP_8E(0xFE, 0xFFFFE912, 0x2EE0, 0xCB52, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_347B)
    WaitChrThread(0x101, 0x2)

    def lambda_349B():
        OP_96(0xFE, 0xFFFFE480, 0x2EE0, 0xCDDC, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_349B)
    WaitChrThread(0x103, 0x2)

    def lambda_34BE():
        OP_8E(0xFE, 0xFFFFDE7C, 0x2EE0, 0xCD00, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_34BE)
    WaitChrThread(0x105, 0x2)

    def lambda_34DE():
        OP_8E(0xFE, 0xFFFFE16A, 0x2EE0, 0xC8E6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_34DE)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #121
        0xB,
        (
            "#187FEstelle Bright!\x02\x03",

            "And...Princess Klaudia?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#006FCaptain Amalthea!\x01",
            "Stand aside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x105,
        (
            "#042FI'm here to demand the release\x01",
            "of my grandmother!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        "#186FWatch your tongue, girl!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 6)

    def lambda_35C4():
        OP_92(0xFE, 0x9, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35C4)
    Sleep(10)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 8)

    def lambda_35E8():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_35E8)
    Sleep(10)
    SetChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x105, 10)

    def lambda_360C():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_360C)
    Sleep(20)
    SetChrChipByIndex(0x8, 39)

    def lambda_362B():
        OP_92(0xFE, 0x103, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_362B)
    Sleep(10)
    SetChrChipByIndex(0x9, 39)

    def lambda_364A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_364A)
    Sleep(10)
    SetChrChipByIndex(0xB, 41)

    def lambda_3669():
        OP_92(0xFE, 0x105, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3669)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    Battle(0x3A8, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_36BD"),
        (SWITCH_DEFAULT, "loc_36C0"),
    )


    label("loc_36BD")

    OP_B4(0x0)
    Return()

    label("loc_36C0")

    EventBegin(0x0)
    OP_6D(-6850, 12000, 58770, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0xB, -7520, 12000, 58240, 12)
    SetChrPos(0x8, -7920, 12000, 56580, 94)
    SetChrPos(0x9, -9260, 12000, 57540, 284)
    SetChrPos(0x101, -5430, 12000, 58450, 270)
    SetChrPos(0x103, -5750, 12000, 60040, 225)
    SetChrPos(0x105, -4860, 12000, 59500, 270)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 36)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 35)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 35)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)
    OP_51(0x105, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #125
        0x103,
        (
            "#023FUgh...\x01",
            "What a nasty woman.\x02\x03",

            "Who was that, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#009FColonel Richard's second-in-command.\x02\x03",

            "Your stereotypical femme fatale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x103,
        (
            "#025FThat would explain it, yes.\x02\x03",

            "#020FNow, on to the Royal Keep!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x105,
        "#042FYes! Let's hurry!\x02",
    )

    CloseMessageWindow()
    OP_28(0x4E, 0x1, 0x2)
    ClearChrFlags(0x32, 0x80)
    OP_6F(0x0, 360)
    EventEnd(0x0)
    Return()

    # Function_12_3023 end

    def Function_13_38F2(): pass

    label("Function_13_38F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38FF")
    Return()

    label("loc_38FF")

    EventBegin(0x0)
    OP_A2(0x662)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xE, 13020, 14000, 78670, 270)
    SetChrPos(0xF, 14450, 14000, 79840, 270)
    SetChrPos(0x10, 14130, 14000, 77880, 270)
    SetChrChipByIndex(0xE, 38)
    SetChrChipByIndex(0xF, 37)
    SetChrChipByIndex(0x10, 37)

    ChrTalk(    #129
        0xE,
        "#3PI found them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xF,
        "#3PThis way!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 1230, 14000, 77770, 90)
    SetChrPos(0x103, -420, 14000, 78370, 90)
    SetChrPos(0x105, -300, 14000, 77020, 90)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    OP_6D(6360, 14000, 78900, 0)
    OP_0D()

    ChrTalk(    #131
        0x101,
        (
            "#004F#5PUh-oh!\x01",
            "Here they come again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x103,
        (
            "#024F#5PPersistent little buggers,\x01",
            "aren't they?\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 39)
    SetChrChipByIndex(0xF, 34)
    SetChrChipByIndex(0x10, 34)

    def lambda_3A4F():
        OP_6D(8500, 14000, 78900, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A4F)

    def lambda_3A67():
        OP_92(0xFE, 0xE, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A67)
    Sleep(10)

    def lambda_3A81():
        OP_92(0xFE, 0x10, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A81)
    Sleep(10)

    def lambda_3A9B():
        OP_92(0xFE, 0xF, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A9B)
    Sleep(20)

    def lambda_3AB5():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3AB5)
    Sleep(10)

    def lambda_3AD5():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3AD5)
    Sleep(10)

    def lambda_3AF5():
        OP_8E(0xFE, 0xFFFFAFD8, 0x36B0, 0x130EC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3AF5)
    Sleep(500)
    Battle(0x3B1, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3B28"),
        (SWITCH_DEFAULT, "loc_3B2B"),
    )


    label("loc_3B28")

    OP_B4(0x0)
    Return()

    label("loc_3B2B")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrPos(0x101, 1780, 14000, 78680, 90)
    SetChrPos(0x103, 1780, 14000, 78680, 90)
    SetChrPos(0x105, 1780, 14000, 78680, 90)
    OP_6D(1780, 14000, 78680, 0)
    SetChrPos(0xE, 3890, 14000, 79000, 146)
    SetChrPos(0xF, 3080, 14000, 77370, 283)
    SetChrPos(0x10, 6700, 14000, 78300, 358)
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 35)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 35)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 35)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0xE, 0x800)
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0x10, 0x800)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_13_38F2 end

    def Function_14_3C26(): pass

    label("Function_14_3C26")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CA5")
    OP_8C(0x101, 180, 0)
    TurnDirection(0x105, 0x101, 0)
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(    #133
        0x105,
        (
            "#043FEstelle! That way leads\x01",
            "into the castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x103,
        "#022FCome on! To the Royal Keep!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D89")

    label("loc_3CA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D05")
    OP_8C(0x105, 180, 0)
    TurnDirection(0x101, 0x105, 0)
    TurnDirection(0x103, 0x105, 0)

    ChrTalk(    #135
        0x105,
        (
            "#042FNot that way...! We have to go\x01",
            "to the Royal Keep!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D89")

    label("loc_3D05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D89")
    OP_8C(0x103, 180, 0)
    TurnDirection(0x101, 0x103, 0)
    TurnDirection(0x105, 0x103, 0)

    ChrTalk(    #136
        0x103,
        (
            "#023FWhoops! This isn't the way\x01",
            "to the Royal Keep!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#005FRight! Up the hill to the north!\x02",
    )

    CloseMessageWindow()

    label("loc_3D89")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_14_3C26 end

    def Function_15_3DA5(): pass

    label("Function_15_3DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DB2")
    Return()

    label("loc_3DB2")

    EventBegin(0x0)
    OP_A2(0x664)
    Fade(1000)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -870, 19000, 105680, 180)
    SetChrPos(0x12, 850, 19000, 105680, 180)
    SetChrChipByIndex(0x11, 37)
    SetChrChipByIndex(0x12, 37)
    SetChrPos(0x101, 100, 17250, 98200, 0)
    SetChrPos(0x103, -1300, 17000, 97610, 0)
    SetChrPos(0x105, 1670, 17000, 97720, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x103, 7)
    SetChrChipByIndex(0x105, 9)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    OP_6D(290, 18000, 103070, 0)
    OP_67(0, 7390, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(30000, 0)
    OP_6E(420, 0)
    OP_0D()

    ChrTalk(    #138
        0x11,
        "H-Here they come...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x12,
        "You shall not pass!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x105,
        "#042F#2PBut we must...and we WILL!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#005F#2PCome on!\x01",
            "Just try and stop us!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F0E():
        OP_6D(360, 18750, 105100, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F0E)

    def lambda_3F26():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F26)
    Sleep(50)

    def lambda_3F46():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3F46)
    Sleep(50)

    def lambda_3F66():
        OP_8E(0xFE, 0xFFFFFECA, 0x4B32, 0x1F676, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3F66)
    Sleep(500)
    Battle(0x3B2, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3F99"),
        (SWITCH_DEFAULT, "loc_3F9C"),
    )


    label("loc_3F99")

    OP_B4(0x0)
    Return()

    label("loc_3F9C")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrPos(0x11, -2160, 18000, 102100, 309)
    SetChrPos(0x12, 2230, 18000, 101600, 82)
    ClearChrFlags(0x11, 0x1)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x12, 0x800)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 35)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 35)
    SetChrPos(0x101, -90, 18000, 102000, 0)
    SetChrPos(0x103, -90, 18000, 102000, 0)
    SetChrPos(0x105, -90, 18000, 102000, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)
    OP_6D(-90, 18000, 102000, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_3DA5 end

    def Function_16_4099(): pass

    label("Function_16_4099")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(30, 12000, 67150, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -6690, 12000, 53510, 0)
    SetChrPos(0x102, -6380, 12000, 54650, 0)
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
    SetChrPos(0x14, -7210, 12000, 58180, 0)
    SetChrPos(0x15, -9680, 12000, 54680, 0)
    SetChrPos(0x16, -7920, 12000, 56380, 0)
    SetChrPos(0x17, -10390, 12000, 56310, 0)
    SetChrPos(0x18, 6170, 12000, 53150, 0)
    SetChrPos(0x19, 6210, 12000, 53870, 0)
    SetChrPos(0x1A, -7990, 12000, 54100, 0)
    SetChrPos(0x1B, -7550, 12000, 49770, 0)
    SetChrPos(0x1C, -6470, 12000, 48980, 0)
    SetChrPos(0x1D, -1110, 12000, 70820, 0)
    SetChrPos(0x1E, 1020, 12000, 70710, 0)
    SetChrPos(0x1F, 10, 12000, 71740, 0)
    SetChrPos(0x20, 20, 12000, 67080, 0)
    SetChrPos(0x13, 650, 12000, 68820, 0)
    SetChrPos(0x21, 6760, 12000, 57310, 0)
    SetChrPos(0x22, 5980, 12000, 57880, 0)
    SetChrPos(0x23, 7530, 12000, 55190, 0)
    SetChrPos(0x24, 6470, 12000, 55570, 0)
    SetChrPos(0x25, 9010, 12000, 57270, 0)
    SetChrPos(0x26, 9250, 12000, 55950, 0)
    SetChrPos(0x27, -2750, 12000, 62800, 90)
    SetChrPos(0x28, -2750, 12000, 61200, 90)
    SetChrPos(0x29, -2750, 12000, 59600, 90)
    SetChrPos(0x2A, -2750, 12000, 58000, 90)
    SetChrPos(0x2B, -2750, 12000, 56400, 90)
    SetChrPos(0x2C, 2750, 12000, 62800, 270)
    SetChrPos(0x2D, 2750, 12000, 61200, 270)
    SetChrPos(0x2E, 2750, 12000, 59600, 270)
    SetChrPos(0x2F, 2750, 12000, 58000, 270)
    SetChrPos(0x30, 2750, 12000, 56400, 270)

    def lambda_43AF():

        label("loc_43AF")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_43AF")

    QueueWorkItem2(0x2A, 0, lambda_43AF)

    def lambda_43C2():

        label("loc_43C2")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_43C2")

    QueueWorkItem2(0x2B, 0, lambda_43C2)

    def lambda_43D5():

        label("loc_43D5")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_43D5")

    QueueWorkItem2(0x2F, 0, lambda_43D5)

    def lambda_43E8():

        label("loc_43E8")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_43E8")

    QueueWorkItem2(0x30, 0, lambda_43E8)

    def lambda_43FB():
        OP_8E(0xFE, 0xFFFFFBAA, 0x2EE0, 0xD23C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_43FB)

    def lambda_4416():
        OP_8E(0xFE, 0x3FC, 0x2EE0, 0xD1CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4416)

    def lambda_4431():
        OP_8E(0xFE, 0xA, 0x2EE0, 0xD5D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4431)

    def lambda_444C():
        OP_8E(0xFE, 0x14, 0x2EE0, 0xC3A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_444C)

    def lambda_4467():
        OP_8E(0xFE, 0x28A, 0x2EE0, 0xCA6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4467)

    def lambda_4482():

        label("loc_4482")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4482")

    QueueWorkItem2(0x101, 1, lambda_4482)

    def lambda_4493():

        label("loc_4493")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4493")

    QueueWorkItem2(0x102, 1, lambda_4493)

    def lambda_44A4():

        label("loc_44A4")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44A4")

    QueueWorkItem2(0x14, 1, lambda_44A4)

    def lambda_44B5():

        label("loc_44B5")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44B5")

    QueueWorkItem2(0x15, 1, lambda_44B5)

    def lambda_44C6():

        label("loc_44C6")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44C6")

    QueueWorkItem2(0x16, 1, lambda_44C6)

    def lambda_44D7():

        label("loc_44D7")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44D7")

    QueueWorkItem2(0x17, 1, lambda_44D7)

    def lambda_44E8():

        label("loc_44E8")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44E8")

    QueueWorkItem2(0x18, 1, lambda_44E8)

    def lambda_44F9():

        label("loc_44F9")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_44F9")

    QueueWorkItem2(0x19, 1, lambda_44F9)

    def lambda_450A():

        label("loc_450A")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_450A")

    QueueWorkItem2(0x1A, 1, lambda_450A)

    def lambda_451B():

        label("loc_451B")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_451B")

    QueueWorkItem2(0x1B, 1, lambda_451B)

    def lambda_452C():

        label("loc_452C")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_452C")

    QueueWorkItem2(0x1C, 1, lambda_452C)

    def lambda_453D():

        label("loc_453D")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_453D")

    QueueWorkItem2(0x21, 1, lambda_453D)

    def lambda_454E():

        label("loc_454E")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_454E")

    QueueWorkItem2(0x22, 1, lambda_454E)

    def lambda_455F():

        label("loc_455F")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_455F")

    QueueWorkItem2(0x23, 1, lambda_455F)

    def lambda_4570():

        label("loc_4570")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4570")

    QueueWorkItem2(0x24, 1, lambda_4570)

    def lambda_4581():

        label("loc_4581")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4581")

    QueueWorkItem2(0x25, 1, lambda_4581)

    def lambda_4592():

        label("loc_4592")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4592")

    QueueWorkItem2(0x26, 1, lambda_4592)

    def lambda_45A3():
        OP_6D(-1510, 12000, 54280, 9000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_45A3)

    def lambda_45BB():
        OP_6E(342, 9000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_45BB)
    WaitChrThread(0x0, 0x2)
    Sleep(1000)

    def lambda_45D5():
        OP_6D(0, 12000, 47170, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_45D5)
    OP_8E(0x20, 0x1E, 0x2EE0, 0xB87E, 0x3E8, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_4099 end

    def Function_17_4613(): pass

    label("Function_17_4613")

    EventBegin(0x0)
    OP_6D(20, 12000, 70880, 0)
    OP_67(0, -2830, -10000, 0)
    OP_6B(4410, 0)
    OP_6C(359000, 0)
    OP_6E(612, 0)

    def lambda_4658():
        OP_67(0, 6070, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4658)

    def lambda_4670():
        OP_6C(35000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4670)
    Sleep(8000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4221   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_17_4613 end

    def Function_18_468C(): pass

    label("Function_18_468C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4695")
    Return()

    label("loc_4695")

    EventBegin(0x0)
    OP_77(0x41, 0x64, 0x82, 0x0, 0x0)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x4)
    SetChrFlags(0x31, 0x40)
    SetChrChipByIndex(0x31, 32)
    ClearChrFlags(0x31, 0x80)
    SetChrPos(0x31, 43230, 16000, 80440, 270)
    SetChrFlags(0x31, 0x4)

    def lambda_46D9():

        label("loc_46D9")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_46D9")

    QueueWorkItem2(0x31, 1, lambda_46D9)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x31, 400)
    Sleep(1000)

    def lambda_470F():
        OP_6D(40260, 16000, 79530, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_470F)

    def lambda_4727():
        OP_8E(0xFE, 0x9178, 0x3E80, 0x13344, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4727)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x31, 400)
    Sleep(500)
    Fade(3000)
    OP_6C(69000, 3000)
    Sleep(2000)
    OP_44(0x31, 0xFF)
    Fade(1000)
    OP_51(0x31, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x31, 33)

    ChrTalk(    #142
        0x31,
        (
            "#010F...Hey, Estelle.\x02\x03",

            "Nice night, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#000FYeah...\x02\x03",

            "There's that song again.\x02\x03",

            "'The Whereabouts of Light.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x31,
        (
            "#010FI've lost a lot...\x02\x03",

            "But this song, and this harmonica,\x01",
            "have always been with me.\x02\x03",

            "I've been thinking about\x01",
            "why I play it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#000F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x31,
        (
            "#010FMaybe it's a habit I should quit.\x02\x03",

            "I think I want to tell you...\x02\x03",

            "...what I was doing before\x01",
            "I met you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        (
            "#000FJoshua...\x02\x03",

            "Okay...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_491C():

        label("loc_491C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_491C")

    QueueWorkItem2(0x31, 1, lambda_491C)

    def lambda_492D():
        OP_8E(0xFE, 0xA8FC, 0x3E80, 0x13F42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_492D)
    Sleep(200)

    def lambda_494D():
        OP_6D(43230, 16000, 81140, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_494D)
    WaitChrThread(0x101, 0x2)
    TurnDirection(0x101, 0x31, 300)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #148
        0x31,
        (
            "#010FThis may take a while...\x01",
            "Do you mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#000FNot at all. I'll listen to\x01",
            "whatever you have to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x31,
        (
            "#010FThank you...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x31, 0xFF)
    OP_8C(0x31, 90, 300)
    Sleep(500)

    ChrTalk(    #151
        0x31,
        (
            "#010FOnce upon a time...\x02\x03",

            "There lived a little boy,\x01",
            "all by himself.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    ChrTalk(    #152
        0x31,
        (
            "#010FThis boy's heart was broken\x01",
            "because of something that\x01",
            "had happened to him.\x02\x03",

            "He forgot how to speak...to\x01",
            "feel...even to eat. All he\x01",
            "could do was play his harmonica.\x02\x03",

            "No matter how hard his caretaker tried, nothing\x01",
            "helped his heart to mend, and he grew weaker by\x01",
            "the day.\x02\x03",

            "One day, a wandering magician\x01",
            "appeared before the boy.\x02\x03",

            "'I will heal the boy's heart\x01",
            "for you,' he said.\x02\x03",

            "'Provided, of course, I am compensated.'\x02\x03",

            "And so, the boy was given over\x01",
            "into the magician's care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x31,
        (
            "#010FAs he attempted to piece the\x01",
            "broken heart back together...\x02\x03",

            "...the magician found that he\x01",
            "could shape the boy's existence\x01",
            "into anything he wished.\x02\x03",

            "And so,  the boy's new heart\x01",
            "became that of a murderer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        "#000F?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x31,
        (
            "#010FFor two years, the boy killed\x01",
            "every single day.\x02\x03",

            "Under cover of night, he\x01",
            "murdered dozens of soldiers.\x02\x03",

            "He slit the throat of a national\x01",
            "cabinet minister, who was under\x01",
            "heavily armed guard.\x02\x03",

            "Sometimes, he used explosives, which\x01",
            "maimed and killed innocent bystanders.\x02\x03",

            "At some point, the boy became known\x01",
            "as the 'Black Fang,' and the name\x01",
            "struck fear into the hearts of men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x31,
        (
            "#010FOne day, the magician gave the\x01",
            "boy an assassination order.\x02\x03",

            "His target was a hero: a man who had\x01",
            "protected his queen and nation from the\x01",
            "threat of an invading northern country.\x02\x03",

            "He was a bracer who held a special\x01",
            "rank shared only by three others\x01",
            "in the entire land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#000FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x31,
        (
            "#010FBut the target was too strong.\x02\x03",

            "He defeated the boy with all\x01",
            "the ease of a tiger swatting\x01",
            "at a playful cub.\x02\x03",

            "At that moment, some of the\x01",
            "magician's servants showed up.\x02\x03",

            "Since the boy's face had been\x01",
            "seen, he was now a loose end\x01",
            "to be tied up.\x02\x03",

            "But someone came to his aid\x01",
            "and drove the attackers away.\x02\x03",

            "It was, of course, the man\x01",
            "he had come to kill.\x02\x03",

            "And so, the boy...\x02\x03",

            "...The boy was taken to the man's\x01",
            "house, where he met a young girl...\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #161
        0x31,
        (
            "#010FHe lived there for five years,\x01",
            "always feeling like he was lost\x01",
            "in some wonderful dream.\x02\x03",

            "In the real world he would never\x01",
            "be allowed to have such dreams...\x02\x03",

            "But all dreams must end\x01",
            "at some point.\x02\x03",

            "The time was drawing near, when\x01",
            "reality could be avoided no longer.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x31, 0x101, 400)

    ChrTalk(    #162
        0x31,
        (
            "#010FAnd that's...the end of my story.\x02\x03",

            "Thank you for being patient\x01",
            "with me and listening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#000F...\x02\x03",

            "...Umm...ha ha...\x02\x03",

            "Was all that...real?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x31,
        (
            "#010FEvery syllable.\x02\x03",

            "My heart is broken.\x02\x03",

            "I'm a murderer.\x02\x03",

            "I failed in the assassination\x01",
            "of your father.\x02\x03",

            "I've been betraying you\x01",
            "for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#000F?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x31,
        (
            "#010FThe boy can't be saved from\x01",
            "his real purpose.\x02\x03",

            "His presence alone seems to\x01",
            "bring disaster and misery...\x02\x03",

            "He's just...tainted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x31,
        (
            "#010FBut now, it is time for the boy to set out\x01",
            "on a journey.\x02\x03",

            "So that he no longer brings misfortune to the\x01",
            "people he holds dear.\x02\x03",

            "He will find and stop the foul magician who\x01",
            "created the life he has led.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x31, 0xA910, 0x3E80, 0x13D26, 0x3E8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #169
        "\x07\x05Joshua handed Estelle his beloved harmonica.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x31, 0xA8DE, 0x3E80, 0x13A38, 0x3E8, 0x0)

    ChrTalk(    #170
        0x101,
        "#000FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x31,
        (
            "#010FThat's the last remnant of\x01",
            "my human heart...\x02\x03",

            "I won't be needing it any more...\x02\x03",

            "But I want you to take it.\x02\x03",

            "It's hardly an adequate way\x01",
            "to thank you for the last\x01",
            "five years...\x02\x03",

            "...but I can't think of anything better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#000F...\x02\x03",

            "...op it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x31,
        "#010FWha...?\x02",
    )

    CloseMessageWindow()

    def lambda_570C():
        OP_6D(43230, 16000, 80820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_570C)

    def lambda_5724():
        OP_6E(259, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5724)
    OP_8E(0x101, 0xA91A, 0x3E80, 0x13CA4, 0xBB8, 0x0)

    ChrTalk(    #174
        0x101,
        (
            "#000FI said, STOP IT.\x02\x03",

            "Stop talking about it like\x01",
            "it's a dream...!\x02\x03",

            "You make it sound like nothing that's\x01",
            "happened was even real to you!\x02\x03",

            "What difference does the\x01",
            "past make?!\x02\x03",

            "Your heart is broken? What\x01",
            "does that even MEAN?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x31,
        "#010FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#000FLook at me!\x02\x03",

            "Look into my eyes!\x02\x03",

            "They've ALWAYS seen that boy!\x02\x03",

            "In good times and bad!\x02\x03",

            "No matter how much the boy was\x01",
            "hurting...I always saw how hard\x01",
            "he'd keep holding on!\x02\x03",

            "Joshua...I love you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x31,
        "#010F!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#000FYou can't just leave me\x01",
            "on my own!\x02\x03",

            "My feelings won't just go\x01",
            "away when you do!\x02\x03",

            "I won't let you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x31,
        (
            "#010FEstelle...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#000F...Oh...\x02\x03",

            "(J-Joshua...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#000FWhat was that...?!\x02\x03",

            "It's so bitter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x31,
        (
            "#010F...An alkaloid sedative.\x02\x03",

            "Don't worry...\x01",
            "There are no side effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        "#000FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        (
            "#000FWh...why...?\x02\x03",

            "Why did you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x31,
        (
            "#010FMy Estelle...\x01",
            "You shine like the sun.\x02\x03",

            "My time with you was the happiest...and\x01",
            "the most painful...I've ever known.\x02\x03",

            "Just as the brightest light\x01",
            "casts the darkest shadow...\x02\x03",

            "If you stayed with me, you'd\x01",
            "find out just how disgusting\x01",
            "my true nature is...\x02\x03",

            "Sometimes, I think it would have been\x01",
            "better if we'd never met...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#000FNo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x31,
        (
            "#010FBut this time is different.\x02\x03",

            "I'm grateful that you came to see me.\x02\x03",

            "I hate that I have to run from\x01",
            "a girl who's so important to me,\x01",
            "but it's all I can do...\x02\x03",

            "But I want you to know that I'll\x01",
            "always be thinking of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        "#000FJoshua...Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x31,
        (
            "#010FThank you...for everything.\x02\x03",

            "You had me from the first moment\x01",
            "I met you. I've always loved you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)

    ChrTalk(    #191
        0x31,
        "#010FGoodbye, Estelle.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_18_468C end

    def Function_19_5D70(): pass

    label("Function_19_5D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E18")
    EventBegin(0x1)

    ChrTalk(    #192
        0x8,
        (
            "Hello, Hilda.\x01",
            "You need something else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        (
            "We're keeping watch over Her Majesty.\x01",
            "You've nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_5EA1")

    label("loc_5E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EA1")
    EventBegin(0x1)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #194
        0x8,
        (
            "The area around the Royal Keep\x01",
            "is off limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x8,
        "No one is to be admitted.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0x8, 180, 0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5EA1")

    Return()

    # Function_19_5D70 end

    SaveToFile()

Try(main)
