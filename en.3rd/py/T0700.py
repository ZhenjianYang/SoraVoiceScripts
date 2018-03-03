from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0700   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0700.x',
        MapIndex            = 9,
        MapDefaultBGM       = "ed60010",
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
        'Estelle',                              # 9
        'Joshua',                               # 10
        'Cassius',                              # 11
        'Alan',                                 # 12
        'Cecilia',                              # 13
        'Cecilia Shadow',                       # 14
        'Scherazard',                           # 15
        'Luke',                                 # 16
        'Pat',                                  # 17
        'Claire',                               # 18
        'Aina',                                 # 19
        'Elissa',                               # 20
        'Tio',                                  # 21
        'Stella',                               # 22
        'Elger',                                # 23
        'Father Divine',                        # 24
        'Mayor Klaus',                          # 25
        'Ridge',                                # 26
        'Rinon',                                # 27
        'Kitty',                                # 28
        'Bloom',                                # 29
        'Fate',                                 # 30
        'Yuni',                                 # 31
        'Melders',                              # 32
        'Freddy',                               # 33
        'Paddington',                           # 34
        'Densel',                               # 35
        'Tabitha',                              # 36
        'Mine Chief Gaton',                     # 37
        'Armand',                               # 38
        'Ellie',                                # 39
        'Ida',                                  # 40
        'Aryll',                                # 41
        'Faulkner',                             # 42
        'Maggy',                                # 43
        'Verne',                                # 44
        'Radford',                              # 45
        'Franz',                                # 46
        'Hannah',                               # 47
        'Chere',                                # 48
        'Will',                                 # 49
        'Target Camera',                        # 50
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
        'ED6_DT27/CH03000 ._CH',             # 00
        'ED6_DT27/CH03200 ._CH',             # 01
        'ED6_DT07/CH02000 ._CH',             # 02
        'ED6_DT07/CH00020 ._CH',             # 03
        'ED6_DT07/CH01160 ._CH',             # 04
        'ED6_DT07/CH01060 ._CH',             # 05
        'ED6_DT07/CH01070 ._CH',             # 06
        'ED6_DT07/CH02560 ._CH',             # 07
        'ED6_DT07/CH02490 ._CH',             # 08
        'ED6_DT07/CH02480 ._CH',             # 09
        'ED6_DT07/CH01690 ._CH',             # 0A
        'ED6_DT07/CH01680 ._CH',             # 0B
        'ED6_DT07/CH01400 ._CH',             # 0C
        'ED6_DT07/CH02350 ._CH',             # 0D
        'ED6_DT07/CH01760 ._CH',             # 0E
        'ED6_DT07/CH01040 ._CH',             # 0F
        'ED6_DT07/CH01770 ._CH',             # 10
        'ED6_DT07/CH01010 ._CH',             # 11
        'ED6_DT07/CH01020 ._CH',             # 12
        'ED6_DT07/CH01170 ._CH',             # 13
        'ED6_DT07/CH01000 ._CH',             # 14
        'ED6_DT07/CH01250 ._CH',             # 15
        'ED6_DT07/CH01280 ._CH',             # 16
        'ED6_DT07/CH01130 ._CH',             # 17
        'ED6_DT07/CH01530 ._CH',             # 18
        'ED6_DT07/CH01140 ._CH',             # 19
        'ED6_DT07/CH01150 ._CH',             # 1A
        'ED6_DT07/CH01030 ._CH',             # 1B
        'ED6_DT27/CH03880 ._CH',             # 1C
        'ED6_DT07/CH01270 ._CH',             # 1D
        'ED6_DT07/CH01110 ._CH',             # 1E
        'ED6_DT07/CH01560 ._CH',             # 1F
        'ED6_DT07/CH01020 ._CH',             # 20
        'ED6_DT07/CH01290 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT27/CH03000P._CP',             # 00
        'ED6_DT27/CH03200P._CP',             # 01
        'ED6_DT07/CH02000P._CP',             # 02
        'ED6_DT07/CH00020P._CP',             # 03
        'ED6_DT07/CH01160P._CP',             # 04
        'ED6_DT07/CH01060P._CP',             # 05
        'ED6_DT07/CH01070P._CP',             # 06
        'ED6_DT07/CH02560P._CP',             # 07
        'ED6_DT07/CH02490P._CP',             # 08
        'ED6_DT07/CH02480P._CP',             # 09
        'ED6_DT07/CH01690P._CP',             # 0A
        'ED6_DT07/CH01680P._CP',             # 0B
        'ED6_DT07/CH01400P._CP',             # 0C
        'ED6_DT07/CH02350P._CP',             # 0D
        'ED6_DT07/CH01760P._CP',             # 0E
        'ED6_DT07/CH01040P._CP',             # 0F
        'ED6_DT07/CH01770P._CP',             # 10
        'ED6_DT07/CH01010P._CP',             # 11
        'ED6_DT07/CH01020P._CP',             # 12
        'ED6_DT07/CH01170P._CP',             # 13
        'ED6_DT07/CH01000P._CP',             # 14
        'ED6_DT07/CH01250P._CP',             # 15
        'ED6_DT07/CH01280P._CP',             # 16
        'ED6_DT07/CH01130P._CP',             # 17
        'ED6_DT07/CH01530P._CP',             # 18
        'ED6_DT07/CH01140P._CP',             # 19
        'ED6_DT07/CH01150P._CP',             # 1A
        'ED6_DT07/CH01030P._CP',             # 1B
        'ED6_DT27/CH03880P._CP',             # 1C
        'ED6_DT07/CH01270P._CP',             # 1D
        'ED6_DT07/CH01110P._CP',             # 1E
        'ED6_DT07/CH01560P._CP',             # 1F
        'ED6_DT07/CH01020P._CP',             # 20
        'ED6_DT07/CH01290P._CP',             # 21
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        Unknown3            = 39,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E1,
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


    ScpFunction(
        "Function_0_6FA",          # 00, 0
        "Function_1_719",          # 01, 1
        "Function_2_8C7",          # 02, 2
        "Function_3_A44",          # 03, 3
        "Function_4_AA0",          # 04, 4
        "Function_5_3D56",         # 05, 5
        "Function_6_4050",         # 06, 6
        "Function_7_4373",         # 07, 7
        "Function_8_702F",         # 08, 8
        "Function_9_708F",         # 09, 9
        "Function_10_710D",        # 0A, 10
        "Function_11_7158",        # 0B, 11
        "Function_12_71A6",        # 0C, 12
        "Function_13_71BB",        # 0D, 13
        "Function_14_7224",        # 0E, 14
        "Function_15_7292",        # 0F, 15
    )


    def Function_0_6FA(): pass

    label("Function_0_6FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_718")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_718")

    Return()

    # Function_0_6FA end

    def Function_1_719(): pass

    label("Function_1_719")

    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Return()

    # Function_1_719 end

    def Function_2_8C7(): pass

    label("Function_2_8C7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_A2E")

    label("loc_8EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_905")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_A2E")

    label("loc_905")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_A2E")

    label("loc_91E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_937")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_A2E")

    label("loc_937")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_950")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_A2E")

    label("loc_950")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_969")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_A2E")

    label("loc_969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_A2E")

    label("loc_982")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_A2E")

    label("loc_99B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B4")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_A2E")

    label("loc_9B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CD")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_A2E")

    label("loc_9CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_A2E")

    label("loc_9E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_A2E")

    label("loc_9FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A18")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_A2E")

    label("loc_A18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_A2E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A43")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A2E")

    label("loc_A43")

    Return()

    # Function_2_8C7 end

    def Function_3_A44(): pass

    label("Function_3_A44")

    OP_82(0x81, 0x2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x05Obtained \x1F\x65\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_E3(0x4, 0x13, 0x1)
    OP_3E(0x365, 1)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_3_A44 end

    def Function_4_AA0(): pass

    label("Function_4_AA0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 36140, 0, 35830, 180)
    OP_72(0x40F, 0x0)
    ExitThread()
    OP_A1(0x14, 0xF)
    SetChrPos(0x14, 56000, -3075, 35200, 0)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_A1(0x15, 0xC)
    SetChrPos(0x15, 55800, -3070, 35000, 0)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x1)
    ClearChrFlags(0x16, 0x80)
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
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 43740, 4000, 32990, 270)
    SetChrPos(0x11, 43720, 4000, 34060, 270)
    SetChrPos(0x12, 43100, 4000, 35150, 180)
    OP_71(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x16, 42000, 4000, 33240, 90)
    SetChrPos(0x1A, 42090, 4000, 32280, 90)
    SetChrPos(0x1E, 40950, 4000, 31260, 45)
    SetChrPos(0x1D, 41060, 4000, 32380, 90)
    SetChrPos(0x1B, 44300, 4000, 35440, 180)
    SetChrPos(0x1C, 44300, 4000, 36700, 180)
    SetChrPos(0x1F, 40950, 4000, 34330, 90)
    SetChrPos(0x20, 40940, 4000, 33340, 90)
    SetChrPos(0x19, 42040, 4000, 34900, 135)
    SetChrPos(0x17, 42330, 4000, 31310, 45)
    SetChrPos(0x18, 43030, 4000, 30800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x2D, 42920, 4000, 39540, 180)
    SetChrPos(0x2E, 43580, 4000, 39510, 180)
    SetChrPos(0x23, 39520, 4000, 35140, 90)
    SetChrPos(0x22, 40510, 4000, 35190, 90)
    SetChrPos(0x27, 41440, 4000, 39940, 180)
    SetChrPos(0x28, 43500, 4000, 36830, 180)
    SetChrPos(0x35, 40870, 4000, 28980, 45)
    SetChrPos(0x36, 42200, 4000, 28940, 0)
    SetChrPos(0x37, 42020, 4000, 30060, 45)
    SetChrPos(0x38, 40850, 4000, 30090, 45)
    SetChrPos(0x21, 44310, 4000, 38580, 180)
    SetChrPos(0x24, 40160, 4000, 36500, 90)
    SetChrPos(0x25, 39240, 4000, 37340, 135)
    SetChrPos(0x26, 38860, 4000, 36350, 90)
    SetChrPos(0x29, 41840, 4000, 39070, 180)
    SetChrPos(0x2A, 40700, 4000, 37860, 135)
    SetChrPos(0x2B, 41440, 4000, 37460, 135)
    SetChrPos(0x2C, 39180, 4000, 38430, 135)
    SetChrPos(0x2F, 41780, 4000, 36080, 135)
    SetChrPos(0x30, 42090, 4000, 37260, 135)
    SetChrPos(0x31, 42510, 4000, 38350, 180)
    SetChrPos(0x32, 40390, 4000, 38960, 135)
    SetChrPos(0x33, 39090, 4000, 39260, 135)
    SetChrPos(0x34, 43240, 4000, 37580, 180)
    OP_C4(0x0, 0x800)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1 op#A op#5
        "\x18\x07\x00#35A#40WOn the final day...#200W\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C4(0x1, 0x800)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x75, 0x1, 0x32)
    OP_6D(33900, 6950, 10430, 0)
    OP_67(0, 7770, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(44000, 0)
    OP_6E(501, 0)
    OP_1D(0x1)

    def lambda_EF6():
        OP_6D(41200, 6950, 32130, 6000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_EF6)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    Fade(1000)
    OP_24(0x75, 0x46)
    OP_6D(43390, 4000, 34380, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(44000, 0)
    OP_6E(361, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #2
        0x10,
        (
            "#1008F#11PWow! I can't believe how many people came to\x01",
            "see us off...\x01\x02\x03",

            "#1012FThanks for coming.\x02\x03",

            "It means a lot that you came to be here with us.\x02\x03",

            "#1017FSo, as I think you all know, Joshua and I are\x01",
            "going to be away from Liberl for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        (
            "#1053F#5PWe'll be traveling around the continent doing\x01",
            "our bracer work from the various guilds in the\x01",
            "countries we visit.\x02\x03",

            "#1043FWe might be away for quite some time, too.\x02\x03",

            "Right now, we intend to travel across basically\x01",
            "the whole continent.\x02\x03",

            "#1041FBut one day, we will come back here to Rolent.\x01",
            "We promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#1016F#11PYeah. We will.\x02\x03",

            "We'll make sure we've grown so much that\x01",
            "you won't be able to believe your eyes when\x01",
            "we come back, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0xBF, 0x0, 0x64)
    OP_43(0x101, 0x3, 0x0, 0x6)
    Sleep(3000)
    OP_43(0x0, 0x0, 0x0, 0xF)
    OP_44(0x101, 0x3)
    Sleep(1500)

    ChrTalk(    #5
        0x12,
        (
            "#83F#5P*sigh* I still can't believe you decided all of this\x01",
            "on your own without ever consulting your loving\x01",
            "papa.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6D(41950, 4000, 34200, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(270000, 0)
    OP_6E(361, 0)
    SetChrPos(0x12, 42800, 4000, 35050, 135)
    SetChrPos(0x19, 41150, 4000, 35520, 135)

    def lambda_131D():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_131D)
    Sleep(100)

    def lambda_1330():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1330)
    Sleep(100)
    OP_8C(0x16, 45, 400)
    Sleep(300)

    ChrTalk(    #6
        0x16,
        "#023F#5POh, didn't they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "#80F#11PThey did not. That made taking time off to come\x01",
            "see them off a real pain, let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#1052F#6PSorry about that, Dad. We realize we didn't\x01",
            "give you much notice with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#1012F#6PIt's something we discussed seriously, though.\x02\x03",

            "#1025FHopefully you'll be able to believe what we're\x01",
            "doing is for the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x12,
        (
            "#85F#11PAs long as you've given serious thought to what \x01",
            "you're doing, you have my support.\x02\x03",

            "#80FSo go out there and do what you want to.\x01",
            "I'll always be right here waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#1017F#6PGood to hear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        "#1054F#6PThanks, Dad.\x02",
    )

    CloseMessageWindow()

    def lambda_15AA():
        OP_6D(41200, 4000, 32950, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_15AA)

    def lambda_15C2():
        OP_6C(258000, 1500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_15C2)
    OP_8C(0x16, 90, 400)
    Sleep(100)

    def lambda_15DE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_15DE)
    Sleep(100)

    def lambda_15F1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15F1)
    Sleep(100)

    def lambda_1604():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1604)

    def lambda_1612():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1612)

    def lambda_1620():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_1620)
    WaitChrThread(0x39, 0x0)
    Sleep(500)

    ChrTalk(    #13
        0x16,
        (
            "#026F#5PYou're both veteran bracers at this point,\x01",
            "so I'm sure you don't need much in the way\x01",
            "of advice. Instead, I'll keep this simple.\x02\x03",

            "#027FFrom now on, it'll be up to you to decide\x01",
            "what you need to learn and what you need\x01",
            "to know.\x02\x03",

            "Focus on improving your powers of discernment.\x01",
            "That's all I'll say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#1053F#12PWe'll be sure to take it to heart.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1A,
        (
            "#740F#5PLife as a bracer is very different in other countries\x01",
            "compared to how it is here, as I'm sure you're about\x01",
            "to find out...\x02\x03",

            "#741F...but the fundamentals are the same. Just do as we\x01",
            "taught you here, and I'm sure you'll be just fine. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#1006F#6PThanks. I'm sure all we were taught will come in \x01",
            "handy if we ever find ourselves in a bind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x16,
        (
            "#526F#5PHaha. Oh, I'm sure you'll be able to handle\x01",
            "anything you find yourselves up against.\x01",
            "We taught you ourselves, after all.\x02\x03",

            "#525FFollow your hearts with your heads held high.\x01",
            "You'll be just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#1041F#12PThat means a lot to us.\x02\x03",

            "#1053FWe can't thank you enough for all you've taught\x01",
            "us over the years...and I'm sure it will keep coming\x01",
            "in handy in the future, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "#1017F#6PHeehee. For real. We really owe you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x16,
        (
            "#021F#5POh, there's no need to thank me. I've just done\x01",
            "what I always can as your big sister.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #21
        0x1D,
        (
            "#5PDon't drink or eat anything that seems funny\x01",
            "while you're away, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x1D,
        (
            "#5PMake sure you brush your teeth before bed, too,\x01",
            "and that you don't get so caught up in work you\x01",
            "forget to shower!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1D,
        "#5PAnd... And...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1E, 45, 400)

    ChrTalk(    #24
        0x1E,
        "#5PE-Easy now, Stella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x1E,
        (
            "#5PShe's not a child anymore, you know. She knows\x01",
            "how to take care of herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1D,
        (
            "#5PI hope she can. Because if you don't look after\x01",
            "yourself, Estelle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x1D,
        "#5P#3S...I'll be showing up in your DREAMS. #2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#1054F#12PHahaha... The scary part is, I wouldn't put it\x01",
            "past you to find a way to do that.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #29
        0x10,
        (
            "#1016F#6PD-Don't worry! That REALLY won't be necessary,\x01",
            "I swear.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 90, 400)

    ChrTalk(    #30
        0x1E,
        "#5PYou take good care of her, too, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1E,
        (
            "#5PAnd remember, there's always a job available\x01",
            "for you at my shop if you want it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x1E,
        "#5PSo come back safely, you hear?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 225, 400)
    Sleep(300)

    ChrTalk(    #33
        0x11,
        (
            "#1053F#12PI will.\x02\x03",

            "#1041FPlease take care of yourselves while we're away.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #34
        0x1B,
        (
            "#11P*sniffle* *sniffle* I don't want you to goooooo,\x01",
            "Estelle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1B,
        "#11PY-You won't forget about me, will you?\x02",
    )

    CloseMessageWindow()

    def lambda_1F5F():
        OP_6D(42850, 4000, 35770, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_1F5F)

    def lambda_1F77():
        OP_6C(305000, 1500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_1F77)

    def lambda_1F87():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F87)
    Sleep(100)

    def lambda_1F9A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F9A)
    Sleep(100)

    def lambda_1FAD():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1FAD)
    Sleep(100)
    WaitChrThread(0x39, 0x0)

    def lambda_1FC5():
        OP_8F(0xFE, 0xAD0C, 0xFA0, 0x8D68, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_1FC5)
    WaitChrThread(0x1C, 0x0)
    Sleep(300)

    ChrTalk(    #36
        0x1C,
        "#11PCome on, now! Stop crying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#1016F#6PHaha... Of course I won't.\x02\x03",

            "#1017FWhen we've settled in at wherever we end up next,\x01",
            "we'll write to you right away, okay?\x02\x03",

            "Look after Elissa while I'm away, okay, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x1C,
        "#11PI will, I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x1C,
        (
            "#11PYou make sure not to let Joshua get away while\x01",
            "you're out of the country, too, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        "#1044F#5P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        "#1016F#6PDuly noted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x38,
        "#11PDo you two really have to go?\x02",
    )

    CloseMessageWindow()

    def lambda_2192():
        OP_6D(41000, 4000, 31450, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_2192)

    def lambda_21AA():
        OP_6C(270000, 1500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_21AA)

    def lambda_21BA():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21BA)
    Sleep(100)

    def lambda_21CD():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21CD)

    def lambda_21DB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_21DB)
    WaitChrThread(0x39, 0x0)
    Sleep(300)

    ChrTalk(    #43
        0x37,
        "#1PJ-Joshuaaaaaa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x37,
        "#1P*sniffle* *sob*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x35,
        (
            "#5POh, look at that. You've got the twins crying\x01",
            "buckets now, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x36,
        "#1PIt's no surprise this would be hard on them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x36,
        (
            "#1PYou've have been looking after them since\x01",
            "they were babies. Of course they'll miss you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "#1016F#6PAhaha. I've got tons of great memories with\x01",
            "them to keep me company while we're away,\x01",
            "thankfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#1041F#12PIt's probably going to be a while before\x01",
            "we can see any of you again...\x02\x03",

            "#1049F...but you'll never leave our thoughts.\x01",
            "Promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x38,
        "#5PI'm gonna miss you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x37,
        "#1P*sniffle* *sniffle*\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(43820, 4000, 34400, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(44000, 0)
    OP_6E(361, 0)
    SetChrPos(0x19, 42040, 4000, 34900, 135)
    SetChrPos(0x12, 43100, 4000, 35150, 180)
    OP_0D()
    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Female Voice")

    AnonymousTalk(    #52
        (
            "\x07\x05The Bose-bound airliner will be departing shortly.\x02\x03",

            "All passengers, please board the airship at this\x01",
            "time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_253C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_253C)
    Sleep(100)

    def lambda_254F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_254F)
    Sleep(100)

    ChrTalk(    #53
        0x16,
        "#524F#6POh, dear... Looks like we're out of time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x20,
        "#600F#6PWell, then. Take care of yourselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        "#1017F#11PWe will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        "#1053F#5PYou, too, sir.\x02",
    )

    CloseMessageWindow()

    def lambda_2600():
        OP_6D(44150, 4000, 33400, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2600)

    def lambda_2618():

        label("loc_2618")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2618")

    QueueWorkItem2(0x16, 1, lambda_2618)

    def lambda_2629():

        label("loc_2629")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2629")

    QueueWorkItem2(0x1A, 1, lambda_2629)

    def lambda_263A():

        label("loc_263A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_263A")

    QueueWorkItem2(0x1E, 1, lambda_263A)

    def lambda_264B():

        label("loc_264B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_264B")

    QueueWorkItem2(0x1D, 1, lambda_264B)

    def lambda_265C():

        label("loc_265C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_265C")

    QueueWorkItem2(0x1B, 1, lambda_265C)

    def lambda_266D():

        label("loc_266D")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_266D")

    QueueWorkItem2(0x1C, 1, lambda_266D)

    def lambda_267E():

        label("loc_267E")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_267E")

    QueueWorkItem2(0x1F, 1, lambda_267E)

    def lambda_268F():

        label("loc_268F")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_268F")

    QueueWorkItem2(0x20, 1, lambda_268F)

    def lambda_26A0():

        label("loc_26A0")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_26A0")

    QueueWorkItem2(0x19, 1, lambda_26A0)

    def lambda_26B1():

        label("loc_26B1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_26B1")

    QueueWorkItem2(0x17, 1, lambda_26B1)

    def lambda_26C2():

        label("loc_26C2")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_26C2")

    QueueWorkItem2(0x18, 1, lambda_26C2)

    def lambda_26D3():

        label("loc_26D3")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_26D3")

    QueueWorkItem2(0x35, 1, lambda_26D3)

    def lambda_26E4():

        label("loc_26E4")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_26E4")

    QueueWorkItem2(0x36, 1, lambda_26E4)

    def lambda_26F5():

        label("loc_26F5")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_26F5")

    QueueWorkItem2(0x37, 1, lambda_26F5)

    def lambda_2706():

        label("loc_2706")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2706")

    QueueWorkItem2(0x38, 1, lambda_2706)

    def lambda_2717():

        label("loc_2717")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2717")

    QueueWorkItem2(0x22, 1, lambda_2717)

    def lambda_2728():

        label("loc_2728")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2728")

    QueueWorkItem2(0x23, 1, lambda_2728)

    def lambda_2739():

        label("loc_2739")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2739")

    QueueWorkItem2(0x2F, 1, lambda_2739)

    def lambda_274A():

        label("loc_274A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_274A")

    QueueWorkItem2(0x32, 1, lambda_274A)

    def lambda_275B():

        label("loc_275B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_275B")

    QueueWorkItem2(0x26, 1, lambda_275B)

    def lambda_276C():

        label("loc_276C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_276C")

    QueueWorkItem2(0x2A, 1, lambda_276C)

    def lambda_277D():

        label("loc_277D")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_277D")

    QueueWorkItem2(0x2B, 1, lambda_277D)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x11, 0x0, 0x0, 0xB)
    Sleep(1000)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)

    ChrTalk(    #57 op#A
        0x12,
        "#82F#5P#20A...Joshua.\x02",
    )

    Sleep(500)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x10, 0x0)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 315, 400)
    Sleep(500)

    ChrTalk(    #58
        0x12,
        "#85F#5PHave you made up your mind, then?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #59
        0x11,
        (
            "#1041F#5PI have.\x02\x03",

            "#1053FI want to be Joshua Bright after all.\x02\x03",

            "I know the name distinction might not be a big deal\x01",
            "in the eyes of others, but it is for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #60
        0x11,
        (
            "#1043F#12PIt's part of me taking the first--and most difficult--\x01",
            "step on this journey. It's part of making choices\x01",
            "only I can make for myself.\x02\x03",

            "By the time we come back home, I want to have the\x01",
            "strength to proudly declare living the rest of my life\x01",
            "alongside you, Estelle, and everyone in Rolent.\x02\x03",

            "#1053FEven after taking that first difficult step, it's not like\x01",
            "I can guarantee it'll get any easier. Maybe on some\x01",
            "days, it'll be so hard that I'll want to give up.\x02\x03",

            "Right now, though... Right now, I'm more than happy\x01",
            "to go out there and find my own path to walk.\x02\x03",

            "#1041FIf I can do that, I can finally feel like I'm working\x01",
            "towards becoming the person I want to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12,
        (
            "#80F#5PVery well, then.\x02\x03",

            "#81FHaha. That's the kind of positive attitude\x01",
            "I wanted to see. It suits you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x11,
        (
            "#1054F#12PHeh...\x02\x03",

            "#1053FThanks. That's the best compliment you\x01",
            "could've possibly given me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x10,
        (
            "#1007F#11PI swear... What is it with the men in our family?\x02\x03",

            "#1019FWould it kill the two of you to talk so that the\x01",
            "rest of us can understand what you're saying?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #64
        0x10,
        (
            "#1006F#11PBut whatever. Come on, Joshua! Get on board,\x01",
            "or you're gonna be left behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #65
        0x11,
        "#1049F#6PI'm coming, I'm coming.\x02",
    )

    CloseMessageWindow()

    def lambda_2DDE():

        label("loc_2DDE")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_2DDE")

    QueueWorkItem2(0x12, 1, lambda_2DDE)

    def lambda_2DEF():
        OP_6D(48590, 4000, 31980, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2DEF)
    OP_8C(0x10, 90, 400)

    def lambda_2E0E():
        OP_8E(0xFE, 0xCF08, 0x1022, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2E0E)

    def lambda_2E29():
        OP_8E(0xFE, 0xCF08, 0x1022, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2E29)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x1E, 0x1)
    OP_44(0x1D, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x35, 0x1)
    OP_44(0x36, 0x1)
    OP_44(0x37, 0x1)
    OP_44(0x38, 0x1)
    OP_44(0x22, 0x1)
    OP_44(0x23, 0x1)
    OP_44(0x2F, 0x1)
    OP_44(0x32, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x2A, 0x1)
    OP_44(0x2B, 0x1)
    SetChrPos(0x10, 53660, 4130, 30220, 270)
    SetChrPos(0x11, 53740, 4130, 31140, 270)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    OP_72(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x16, 43540, 4000, 30950, 90)
    SetChrPos(0x12, 43160, 4000, 32119, 90)
    SetChrPos(0x1A, 42790, 4000, 30400, 90)
    SetChrPos(0x17, 43600, 4000, 29910, 90)
    SetChrPos(0x18, 43220, 4000, 29340, 90)
    SetChrPos(0x19, 43940, 4000, 28350, 90)
    SetChrPos(0x1B, 42720, 4000, 32960, 90)
    SetChrPos(0x1C, 42680, 4000, 33840, 90)
    SetChrPos(0x35, 41010, 4000, 32229, 90)
    SetChrPos(0x36, 41110, 4000, 31080, 90)
    SetChrPos(0x37, 42010, 4000, 31420, 90)
    SetChrPos(0x38, 41980, 4000, 32259, 90)
    SetChrPos(0x1E, 42060, 4000, 29640, 90)
    SetChrPos(0x1D, 42230, 4000, 28560, 90)
    SetChrPos(0x1F, 40750, 4000, 30070, 90)
    SetChrPos(0x20, 40670, 4000, 29150, 90)
    SetChrPos(0x22, 41250, 4000, 33520, 90)
    SetChrPos(0x23, 41370, 4000, 34320, 90)
    SetChrPos(0x32, 40040, 4000, 34890, 90)
    SetChrPos(0x25, 42090, 4000, 34950, 90)
    SetChrPos(0x26, 43240, 4000, 34520, 90)
    SetChrPos(0x28, 43480, 4000, 36760, 90)
    SetChrPos(0x27, 43320, 4000, 37670, 90)
    SetChrPos(0x2D, 43000, 4000, 39160, 90)
    SetChrPos(0x2E, 43010, 4000, 39830, 90)
    SetChrPos(0x21, 42210, 4000, 37270, 90)
    SetChrPos(0x2F, 41020, 4000, 36130, 90)
    SetChrPos(0x30, 41820, 4000, 36360, 90)
    SetChrPos(0x33, 39660, 4000, 36180, 90)
    SetChrPos(0x2C, 39810, 4000, 37000, 90)
    SetChrPos(0x29, 40170, 4000, 38030, 90)
    SetChrPos(0x24, 41370, 4000, 38160, 90)
    SetChrPos(0x2A, 41330, 4000, 38970, 90)
    SetChrPos(0x2B, 41330, 4000, 40000, 90)
    SetChrPos(0x34, 39690, 4000, 39230, 90)
    SetChrPos(0x31, 42390, 4000, 38320, 90)
    SetChrPos(0x13, 39360, 4000, 37960, 90)
    OP_6D(46470, 3930, 32210, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(315000, 0)
    OP_6E(384, 0)
    OP_6D(46620, 4180, 31500, 0)
    OP_67(0, 3480, -10000, 0)
    OP_6B(3850, 0)
    OP_6C(283000, 0)
    OP_6E(223, 0)
    OP_6D(46380, 4140, 31540, 0)
    OP_67(0, 3450, -10000, 0)
    OP_6B(3710, 0)
    OP_6C(279000, 0)
    OP_6E(223, 0)
    SetChrPos(0x101, 52700, 4130, 30780, 0)
    SetChrFlags(0x101, 0x80)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0x10,
        "#1018F#6PWell, see you around!\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #67
        0x17,
        "#5P...E-Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x17,
        (
            "#5PWhen you come back here next, I'm gonna\x01",
            "be a bracer just like you! I am!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        "#1016F#6PAhaha. Now THAT I want to see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x17,
        "#5PYou don't think I can do it, do you?!\x02",
    )

    CloseMessageWindow()

    def lambda_3342():
        OP_96(0xFE, 0xAA50, 0xFA0, 0x74D6, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3342)

    ChrTalk(    #71
        0x17,
        (
            "#5PI'm serious! By the time you get back,\x01",
            "I'll be a bracer! I swear!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 0x1)
    OP_62(0x18, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #72
        0x18,
        "#5PI... I think I wanna become one, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x18,
        "#5PSo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x11,
        "#1041F#12PDon't worry. We'll be back. We promise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "#1012F#6PI can't wait to work you two to the ground as coworkers.\x01",
            "I'll be counting on you to have my back!\x02\x03",

            "#1006FSo don't let us down, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x17,
        "#5PI-I won't!\x02",
    )

    CloseMessageWindow()
    OP_6D(44600, 4130, 31790, 1500)
    Sleep(500)

    ChrTalk(    #77
        0x12,
        (
            "#85F#5PNever forget that there's always a home\x01",
            "for you here.\x02\x03",

            "#80FNo matter how long you're away, that will\x01",
            "never change!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "#1053F#11PWe won't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        "#1017F#5PThanks, Dad!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #80
        0x10,
        "#1018F#1P#3SWe'll see you later!\x02",
    )

    Sleep(50)

    ChrTalk(    #81
        0x11,
        "#1041F#2P#3SWe'll see you later!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()
    Sleep(300)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(1000)
    OP_24(0x75, 0x64)
    Sleep(1000)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x12C)
    Sleep(1800)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0xF, 0x32)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x3C)
    OP_73(0xF)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x77, 0x1, 0x64)
    Fade(500)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(45940, -5080, 40300, 0)
    OP_67(0, 9350, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(315000, 0)
    OP_6E(621, 0)
    OP_43(0x101, 0x3, 0x0, 0x5)

    def lambda_36BE():
        OP_8F(0xFE, 0xDAC0, 0xFFFFF7E5, 0x8980, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_36BE)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xF, 61)
    OP_70(0xF, 0xA0)
    OP_73(0xF)
    OP_71(0x200F, 0x0)
    ExitThread()
    OP_6F(0xF, 161)
    OP_70(0xF, 0x104)
    WaitChrThread(0x14, 0x0)
    OP_0D()

    def lambda_3709():

        label("loc_3709")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3709")

    QueueWorkItem2(0x12, 1, lambda_3709)

    def lambda_371A():

        label("loc_371A")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_371A")

    QueueWorkItem2(0x16, 1, lambda_371A)

    def lambda_372B():

        label("loc_372B")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_372B")

    QueueWorkItem2(0x1A, 1, lambda_372B)

    def lambda_373C():

        label("loc_373C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_373C")

    QueueWorkItem2(0x1E, 1, lambda_373C)

    def lambda_374D():

        label("loc_374D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_374D")

    QueueWorkItem2(0x1D, 1, lambda_374D)

    def lambda_375E():

        label("loc_375E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_375E")

    QueueWorkItem2(0x1B, 1, lambda_375E)

    def lambda_376F():

        label("loc_376F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_376F")

    QueueWorkItem2(0x1C, 1, lambda_376F)

    def lambda_3780():

        label("loc_3780")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3780")

    QueueWorkItem2(0x1F, 1, lambda_3780)

    def lambda_3791():

        label("loc_3791")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3791")

    QueueWorkItem2(0x20, 1, lambda_3791)

    def lambda_37A2():

        label("loc_37A2")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_37A2")

    QueueWorkItem2(0x19, 1, lambda_37A2)

    def lambda_37B3():

        label("loc_37B3")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_37B3")

    QueueWorkItem2(0x35, 1, lambda_37B3)

    def lambda_37C4():

        label("loc_37C4")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_37C4")

    QueueWorkItem2(0x36, 1, lambda_37C4)

    def lambda_37D5():

        label("loc_37D5")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_37D5")

    QueueWorkItem2(0x37, 1, lambda_37D5)

    def lambda_37E6():

        label("loc_37E6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_37E6")

    QueueWorkItem2(0x38, 1, lambda_37E6)

    def lambda_37F7():

        label("loc_37F7")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_37F7")

    QueueWorkItem2(0x22, 1, lambda_37F7)

    def lambda_3808():

        label("loc_3808")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3808")

    QueueWorkItem2(0x23, 1, lambda_3808)

    def lambda_3819():

        label("loc_3819")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3819")

    QueueWorkItem2(0x2F, 1, lambda_3819)

    def lambda_382A():

        label("loc_382A")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_382A")

    QueueWorkItem2(0x32, 1, lambda_382A)

    def lambda_383B():

        label("loc_383B")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_383B")

    QueueWorkItem2(0x25, 1, lambda_383B)

    def lambda_384C():

        label("loc_384C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_384C")

    QueueWorkItem2(0x26, 1, lambda_384C)

    def lambda_385D():

        label("loc_385D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_385D")

    QueueWorkItem2(0x2A, 1, lambda_385D)

    def lambda_386E():

        label("loc_386E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_386E")

    QueueWorkItem2(0x2B, 1, lambda_386E)

    def lambda_387F():

        label("loc_387F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_387F")

    QueueWorkItem2(0x34, 1, lambda_387F)

    def lambda_3890():

        label("loc_3890")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3890")

    QueueWorkItem2(0x33, 1, lambda_3890)

    def lambda_38A1():

        label("loc_38A1")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_38A1")

    QueueWorkItem2(0x31, 1, lambda_38A1)

    def lambda_38B2():

        label("loc_38B2")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_38B2")

    QueueWorkItem2(0x30, 1, lambda_38B2)

    def lambda_38C3():

        label("loc_38C3")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_38C3")

    QueueWorkItem2(0x2F, 1, lambda_38C3)

    def lambda_38D4():

        label("loc_38D4")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_38D4")

    QueueWorkItem2(0x2E, 1, lambda_38D4)

    def lambda_38E5():

        label("loc_38E5")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_38E5")

    QueueWorkItem2(0x2D, 1, lambda_38E5)

    def lambda_38F6():

        label("loc_38F6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_38F6")

    QueueWorkItem2(0x2C, 1, lambda_38F6)

    def lambda_3907():

        label("loc_3907")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3907")

    QueueWorkItem2(0x27, 1, lambda_3907)

    def lambda_3918():

        label("loc_3918")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3918")

    QueueWorkItem2(0x28, 1, lambda_3918)

    def lambda_3929():

        label("loc_3929")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3929")

    QueueWorkItem2(0x29, 1, lambda_3929)

    def lambda_393A():

        label("loc_393A")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_393A")

    QueueWorkItem2(0x21, 1, lambda_393A)

    def lambda_394B():
        OP_6D(45940, -5080, 49300, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_394B)

    def lambda_3963():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3963)

    def lambda_397E():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_397E)
    Sleep(200)

    def lambda_399E():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_399E)

    def lambda_39B9():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_39B9)
    Sleep(200)

    def lambda_39D9():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_39D9)

    def lambda_39F4():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_39F4)
    Sleep(200)

    def lambda_3A14():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3A14)

    def lambda_3A2F():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3A2F)
    Sleep(200)
    OP_43(0x17, 0x0, 0x0, 0x8)
    OP_43(0x18, 0x0, 0x0, 0x9)

    def lambda_3A5D():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3A5D)

    def lambda_3A78():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3A78)
    Sleep(200)

    def lambda_3A98():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3A98)

    def lambda_3AB3():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3AB3)
    Sleep(200)

    def lambda_3AD3():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3AD3)

    def lambda_3AEE():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3AEE)
    Sleep(200)

    def lambda_3B0E():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3B0E)

    def lambda_3B29():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3B29)
    Sleep(200)

    def lambda_3B49():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3B49)

    def lambda_3B64():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3B64)
    Sleep(200)

    def lambda_3B84():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3B84)

    def lambda_3B9F():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3B9F)
    Sleep(200)

    def lambda_3BBF():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3BBF)

    def lambda_3BDA():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3BDA)
    Sleep(200)

    def lambda_3BFA():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3BFA)

    def lambda_3C15():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3C15)
    Sleep(200)

    def lambda_3C35():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3C35)

    def lambda_3C50():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3C50)
    Sleep(200)

    def lambda_3C70():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3C70)

    def lambda_3C8B():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3C8B)
    Sleep(200)

    def lambda_3CAB():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3CAB)

    def lambda_3CC6():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3CC6)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(100)
    FadeToDark(2000, 0, -1)
    Sleep(200)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    OP_0D()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x40D, 0x0)
    ExitThread()
    SetMapFlags(0x2000000)
    OP_A2(0x250A)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_AA0 end

    def Function_5_3D56(): pass

    label("Function_5_3D56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_404F")
    OP_62(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    Sleep(100)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x2C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x31, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x26, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    Sleep(200)
    OP_62(0x32, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x34, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x36, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x37, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x38, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("Function_5_3D56")

    label("loc_404F")

    Return()

    # Function_5_3D56 end

    def Function_6_4050(): pass

    label("Function_6_4050")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4372")
    OP_62(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x18, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x2C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x31, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x26, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    Sleep(200)
    OP_62(0x32, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x34, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x36, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x37, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x38, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("Function_6_4050")

    label("loc_4372")

    Return()

    # Function_6_4050 end

    def Function_7_4373(): pass

    label("Function_7_4373")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 36140, 0, 35830, 180)
    OP_72(0x40F, 0x0)
    ExitThread()
    OP_A1(0x14, 0xF)
    SetChrPos(0x14, 56000, -3075, 35200, 0)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_A1(0x15, 0xC)
    SetChrPos(0x15, 55800, -3070, 35000, 0)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x16, 43310, 4000, 32130, 270)
    SetChrPos(0x1A, 43360, 4000, 30880, 270)
    SetChrPos(0x19, 43180, 4000, 28810, 270)
    SetChrPos(0x1B, 42150, 4000, 29690, 270)
    SetChrPos(0x1C, 42220, 4000, 28730, 270)
    SetChrPos(0x1D, 41020, 4000, 29970, 270)
    SetChrPos(0x1E, 41040, 4000, 29000, 270)
    SetChrPos(0x1F, 44000, 4000, 33920, 270)
    SetChrPos(0x20, 44130, 4000, 33080, 270)
    SetChrPos(0x21, 43790, 4000, 35600, 225)
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
    SetChrPos(0x22, 39620, 4000, 35330, 225)
    SetChrPos(0x23, 40480, 4000, 35190, 225)
    SetChrPos(0x24, 40160, 4000, 36500, 225)
    SetChrPos(0x25, 39240, 4000, 37340, 225)
    SetChrPos(0x26, 38860, 4000, 36350, 225)
    SetChrPos(0x27, 41100, 4000, 34450, 225)
    SetChrPos(0x28, 40810, 4000, 33360, 225)
    SetChrPos(0x29, 41840, 4000, 39070, 225)
    SetChrPos(0x2A, 40700, 4000, 37860, 225)
    SetChrPos(0x2B, 41440, 4000, 37460, 225)
    SetChrPos(0x2C, 39180, 4000, 38430, 225)
    SetChrPos(0x2D, 42000, 4000, 34240, 225)
    SetChrPos(0x2E, 42420, 4000, 33780, 225)
    SetChrPos(0x2F, 41780, 4000, 36080, 225)
    SetChrPos(0x30, 42090, 4000, 37260, 180)
    SetChrPos(0x31, 42510, 4000, 38350, 225)
    SetChrPos(0x32, 40390, 4000, 38960, 225)
    SetChrPos(0x33, 39090, 4000, 39260, 225)
    SetChrPos(0x34, 43240, 4000, 37580, 225)
    SetChrPos(0x35, 42100, 4000, 32540, 270)
    SetChrPos(0x36, 42120, 4000, 31510, 270)
    SetChrPos(0x37, 41020, 4000, 32100, 270)
    SetChrPos(0x38, 40820, 4000, 31060, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 34900, 0, 130, 0)
    SetChrPos(0x11, 34180, 0, -860, 0)
    SetChrPos(0x12, 35160, 0, -1350, 0)

    def lambda_470D():
        OP_8E(0xFE, 0x870A, 0x0, 0x21F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_470D)
    Sleep(100)

    def lambda_472D():
        OP_8E(0xFE, 0x83F4, 0x0, 0x1D88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_472D)
    Sleep(100)

    def lambda_474D():
        OP_8E(0xFE, 0x8840, 0x0, 0x1B94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_474D)
    OP_6D(35380, 0, 11930, 0)
    OP_67(0, 7370, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(44000, 0)
    OP_6E(339, 0)

    def lambda_47A5():
        OP_6B(2520, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_47A5)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x17, 34520, 0, 25380, 180)
    SetChrPos(0x18, 35890, 0, 25130, 180)

    def lambda_47F0():
        OP_8E(0xFE, 0x8692, 0x0, 0x3AAC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_47F0)
    Sleep(100)

    def lambda_4810():
        OP_8E(0xFE, 0x8A5C, 0x0, 0x3A2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_4810)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #82
        0x17,
        "#5PHaha. There you are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x18,
        "#2PWhat took the two of you so long?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        "#1000F#6PLuke! Pat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x11,
        "#1040F#4PDid the two of you come to see us off?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x17,
        "#5PWe did, but we're not the only ones who did!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x18,
        "#2PCome with us!\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0xD)
    OP_43(0x18, 0x0, 0x0, 0xE)
    Sleep(1500)

    def lambda_493C():
        OP_6D(36710, 0, 27640, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_493C)

    def lambda_4954():
        OP_67(0, 7420, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4954)

    def lambda_496C():
        OP_6B(2420, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_496C)

    def lambda_497C():
        OP_8E(0xFE, 0x8A52, 0x0, 0x6856, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_497C)
    Sleep(150)

    def lambda_499C():
        OP_8E(0xFE, 0x873C, 0x0, 0x637E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_499C)
    Sleep(300)

    def lambda_49BC():
        OP_8E(0xFE, 0x8B2E, 0x0, 0x61E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_49BC)
    WaitChrThread(0x10, 0x0)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)

    ChrTalk(    #88
        0x10,
        "#1000F#4PWow!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #89
        0x11,
        (
            "#1040F#6PHaha...\x02\x03",

            "Wow... I really wasn't expecting this many people\x01",
            "to be here.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(42400, 2000, 35220, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(44000, 0)
    OP_6E(358, 0)

    def lambda_4AB6():
        OP_6D(42400, 4400, 35220, 2500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4AB6)
    OP_0D()
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #90
        0x1D,
        "#2PEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x1E,
        "#2PHaha. We've been waiting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x22,
        "#5PHey, you two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x2C,
        "#5PI decided to come along too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x21,
        "#5PMe, too! Glad the weather's so nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x2D,
        "#5PWe're here to bless you, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x2E,
        "#2PHeehee. That we are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x36,
        (
            "#2PYou could have told us yourselves that you were\x01",
            "leaving, though! I thought we were closer than\x01",
            "that!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x35, 0x38, 400)
    Sleep(200)

    ChrTalk(    #98
        0x35,
        "#5PLook, it's Joshua and Estelle.\x02",
    )

    CloseMessageWindow()
    OP_96(0x38, 0x9F74, 0x1194, 0x7954, 0x12C, 0x1770)

    ChrTalk(    #99
        0x38,
        "#2PSo it is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x37,
        "#5PGood luck, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x2F,
        "#2POh, if it isn't Mr. and Mrs. Bracer!\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #102
        0x30,
        "Nyaaaa!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, 36460, 0, 33620, 90)
    SetChrPos(0x11, 35410, 0, 33510, 90)
    SetChrPos(0x12, 35820, 0, 32360, 90)
    Sleep(300)
    Fade(500)
    OP_6D(37330, 0, 34840, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(44000, 0)
    OP_6E(358, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #103
        0x10,
        "#1000F#5PW-Wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        (
            "#1040F#6PTh-This feels like basically the entire population\x01",
            "of Rolent has come to see us off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x12,
        "#80F#4P*sigh* You two sure are popular.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x13,
        (
            "#5PAll right, the airship's ready to go as soon as\x01",
            "the two of you are.\x02\x03",

            "You've still got a bit more time to say your\x01",
            "farewells, but it'd help if you finished the\x01",
            "boarding procedures right away, if you could.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4EE3():
        OP_6D(37510, 0, 36000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4EE3)

    def lambda_4EFB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4EFB)
    Sleep(100)

    def lambda_4F0E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4F0E)
    Sleep(100)
    OP_8C(0x12, 0, 400)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #107
        0x10,
        "#1000F#4PO-Oh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x11,
        "#1040F#6PWe'll get to that right away, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10,
        "#1000F#4PYeah.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x10, 43740, 4000, 32990, 270)
    SetChrPos(0x11, 43720, 4000, 34060, 270)
    SetChrPos(0x12, 44090, 4000, 35540, 225)
    OP_71(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x16, 42000, 4000, 33240, 90)
    SetChrPos(0x1A, 42090, 4000, 32280, 90)
    SetChrPos(0x1E, 40950, 4000, 31260, 90)
    SetChrPos(0x1D, 41060, 4000, 32380, 90)
    SetChrPos(0x1B, 43100, 4000, 35150, 180)
    SetChrPos(0x1C, 42040, 4000, 34900, 135)
    SetChrPos(0x1F, 40950, 4000, 34330, 90)
    SetChrPos(0x20, 40940, 4000, 33340, 90)
    SetChrPos(0x19, 43180, 4000, 28810, 0)
    SetChrPos(0x17, 42330, 4000, 31310, 45)
    SetChrPos(0x18, 43030, 4000, 30800, 0)
    SetChrPos(0x2D, 42920, 4000, 39540, 180)
    SetChrPos(0x2E, 43580, 4000, 39510, 180)
    SetChrPos(0x23, 39520, 4000, 35140, 90)
    SetChrPos(0x22, 40510, 4000, 35190, 90)
    SetChrPos(0x27, 41440, 4000, 39940, 180)
    SetChrPos(0x28, 43500, 4000, 36830, 180)
    SetChrPos(0x35, 42020, 4000, 30060, 0)
    SetChrPos(0x36, 42200, 4000, 28940, 0)
    SetChrPos(0x37, 40850, 4000, 30090, 45)
    SetChrPos(0x38, 40870, 4000, 28980, 45)
    SetChrPos(0x21, 44310, 4000, 38580, 180)
    SetChrPos(0x24, 40160, 4000, 36500, 90)
    SetChrPos(0x25, 39240, 4000, 37340, 135)
    SetChrPos(0x26, 38860, 4000, 36350, 90)
    SetChrPos(0x29, 41840, 4000, 39070, 180)
    SetChrPos(0x2A, 40700, 4000, 37860, 135)
    SetChrPos(0x2B, 41440, 4000, 37460, 135)
    SetChrPos(0x2C, 39180, 4000, 38430, 135)
    SetChrPos(0x2F, 41780, 4000, 36080, 135)
    SetChrPos(0x30, 42090, 4000, 37260, 135)
    SetChrPos(0x31, 42510, 4000, 38350, 180)
    SetChrPos(0x32, 40390, 4000, 38960, 135)
    SetChrPos(0x33, 39090, 4000, 39260, 135)
    SetChrPos(0x34, 43240, 4000, 37580, 180)
    OP_6D(43390, 4000, 34380, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(44000, 0)
    OP_6E(361, 0)
    OP_22(0x75, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #110
        0x10,
        (
            "#1000F#2PThanks so much for coming to see us off, everyone.\x02\x03",

            "I still can't believe just how many people came,\x01",
            "though.\x02\x03",

            "But now you are... While I realize this is sudden,\x01",
            "Joshua and I are heading off to the Empire for a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x11,
        (
            "#1040F#5PWe're intending to keep doing guild work over\x01",
            "there while traveling around remote regions\x01",
            "of the country.\x02\x03",

            "It's not because there's anything major going on\x01",
            "that you don't know about, though, don't worry\x01",
            "about that.\x02\x03",

            "And we promise we'll return to Rolent one day.\x01",
            "We promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        (
            "#1000F#2PYeah, we will.\x02\x03",

            "We'll be sure to improve ourselves loads while\x01",
            "we're away so you won't believe how much we've\x01",
            "grown the next time you see us, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xBF, 0x0, 0x64)
    Sleep(3000)
    OP_43(0x0, 0x0, 0x0, 0xF)
    Sleep(200)

    ChrTalk(    #113
        0x16,
        (
            "#020F#6PHeehee. I'm sure you will.\x02\x03",

            "Regardless, you're both veterans now. Just follow\x01",
            "your hearts and I'm sure you'll be just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x11,
        "#1040F#5PThank you, Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        (
            "#1000F#2PYou really have done so much for us...\x02\x03",

            "We can't thank you enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x16,
        (
            "#020F#6PHaha. Oh, don't start looking all sad, now.\x02\x03",

            "It's not like we're never going to meet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        "#1000F#2P...Yeah, I suppose you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x1A,
        (
            "#740F#6PI'll be looking forward to seeing just how much\x01",
            "you've grown when we next meet.\x02\x03",

            "Take care of yourselves while you're away, all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        "#1000F#2PThanks, Aina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x11,
        "#1040F#5PWe really do appreciate all you've done for us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x1D,
        (
            "#6PDon't drink or eat anything that seems funny while\x01",
            "you're away, Estelle!\x02\x03",

            "If bread's got mold on it, it's not meant to be\x01",
            "eaten!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 0, 400)
    Sleep(200)

    ChrTalk(    #122
        0x1E,
        (
            "#4PC-Come on, now, Stella...\x02\x03",

            "Estelle's a grown woman. I'm pretty sure she has\x01",
            "enough common sense in her head to know that.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 180, 400)

    ChrTalk(    #123
        0x1D,
        (
            "#5PI-I know that, but it doesn't stop me from being\x01",
            "worried about her!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 90, 400)
    Sleep(200)

    ChrTalk(    #124
        0x1D,
        (
            "#6PIf I could go with the two of them and look after\x01",
            "them myself, I would!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #125
        0x10,
        (
            "#1000F#2PI swear... You don't need to overreact that much.\x02\x03",

            "We will be careful, though, we promise. Especially\x01",
            "as we'll be going to lots of places neither of us\x01",
            "has ever been before.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 90, 400)

    ChrTalk(    #126
        0x1D,
        (
            "#6P*sniffle* Just come back to us safe and sound, okay?\x02\x03",

            "Take good care of her, okay, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x1E,
        "#6PWe'll both be counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        (
            "#1040F#5PI won't let you down.\x02\x03",

            "Please take care of yourselves, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x1B,
        (
            "#5P*sniffle* *sniffle* Esteeeeeelleeeee...\x02\x03",

            "Y-You won't forget about us while you're away,\x01",
            "will you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B9B():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5B9B)
    Sleep(100)

    def lambda_5BAE():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5BAE)
    Sleep(100)
    OP_8C(0x1C, 90, 400)

    ChrTalk(    #130
        0x1C,
        (
            "#6POh come on, Elissa... Let's save her the \x01",
            "waterworks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x10,
        (
            "#1000F#2PHa... Haha...\x02\x03",

            "When we've settled in at wherever we end up next,\x01",
            "we'll write to you right away, okay?\x02\x03",

            "Look after Elissa while I'm away, okay, Tio?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1C, 135, 400)

    ChrTalk(    #132
        0x1C,
        (
            "#6PI will, I will.\x02\x03",

            "You make sure not to let Joshua get away while\x01",
            "you're out of the country, too, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x11,
        "#1040F#2P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10,
        "#1000F#2PHeehee. I'll keep that in mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x20,
        "#600F#6PWell, then. Do take care of yourselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x1F,
        (
            "#6PNo matter where your travels may take you, be\x01",
            "sure never to lose sight of who you are.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DF6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5DF6)
    Sleep(100)
    OP_8C(0x10, 270, 400)

    ChrTalk(    #137
        0x11,
        (
            "#1040F#5PThank you, both of you.\x02\x03",

            "We'll be sure to take your words to heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x10,
        "#1000F#2PYou two take care of yourselves, too, all right?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Female Voice")

    AnonymousTalk(    #139
        (
            "\x07\x05The Bose-bound airliner will be departing \x01",
            "shortly.\x02\x03",

            "All passengers, please board the airship now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #140
        0x10,
        "#1000F#2POh...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #141
        0x12,
        "#80F#5PLooks like we're out of time.\x02",
    )

    CloseMessageWindow()

    def lambda_5F7D():
        OP_6D(45030, 4000, 35310, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5F7D)
    OP_8C(0x11, 0, 400)
    OP_8C(0x10, 0, 400)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #142
        0x11,
        "#1040F#6PWell, then, Dad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x12,
        (
            "#80F#5PYeah. This is farewell for now. Go and do exactly\x01",
            "what you want to do. We'll all be waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x10,
        "#1000F#4PWe will.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    def lambda_6056():
        OP_6D(48590, 4000, 31980, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6056)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x11, 0x0, 0x0, 0xB)

    def lambda_607C():

        label("loc_607C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_607C")

    QueueWorkItem2(0x12, 1, lambda_607C)

    def lambda_608D():

        label("loc_608D")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_608D")

    QueueWorkItem2(0x16, 1, lambda_608D)

    def lambda_609E():

        label("loc_609E")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_609E")

    QueueWorkItem2(0x1A, 1, lambda_609E)

    def lambda_60AF():

        label("loc_60AF")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_60AF")

    QueueWorkItem2(0x1E, 1, lambda_60AF)

    def lambda_60C0():

        label("loc_60C0")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_60C0")

    QueueWorkItem2(0x1D, 1, lambda_60C0)

    def lambda_60D1():

        label("loc_60D1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_60D1")

    QueueWorkItem2(0x1B, 1, lambda_60D1)

    def lambda_60E2():

        label("loc_60E2")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_60E2")

    QueueWorkItem2(0x1C, 1, lambda_60E2)

    def lambda_60F3():

        label("loc_60F3")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_60F3")

    QueueWorkItem2(0x1F, 1, lambda_60F3)

    def lambda_6104():

        label("loc_6104")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_6104")

    QueueWorkItem2(0x20, 1, lambda_6104)

    def lambda_6115():

        label("loc_6115")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_6115")

    QueueWorkItem2(0x19, 1, lambda_6115)

    def lambda_6126():

        label("loc_6126")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_6126")

    QueueWorkItem2(0x17, 1, lambda_6126)

    def lambda_6137():

        label("loc_6137")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_6137")

    QueueWorkItem2(0x18, 1, lambda_6137)

    def lambda_6148():

        label("loc_6148")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_6148")

    QueueWorkItem2(0x35, 1, lambda_6148)

    def lambda_6159():

        label("loc_6159")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_6159")

    QueueWorkItem2(0x36, 1, lambda_6159)

    def lambda_616A():

        label("loc_616A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_616A")

    QueueWorkItem2(0x37, 1, lambda_616A)

    def lambda_617B():

        label("loc_617B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_617B")

    QueueWorkItem2(0x38, 1, lambda_617B)

    def lambda_618C():

        label("loc_618C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_618C")

    QueueWorkItem2(0x22, 1, lambda_618C)

    def lambda_619D():

        label("loc_619D")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_619D")

    QueueWorkItem2(0x23, 1, lambda_619D)

    def lambda_61AE():

        label("loc_61AE")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_61AE")

    QueueWorkItem2(0x2F, 1, lambda_61AE)

    def lambda_61BF():

        label("loc_61BF")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_61BF")

    QueueWorkItem2(0x32, 1, lambda_61BF)

    def lambda_61D0():

        label("loc_61D0")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_61D0")

    QueueWorkItem2(0x26, 1, lambda_61D0)

    def lambda_61E1():

        label("loc_61E1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_61E1")

    QueueWorkItem2(0x2A, 1, lambda_61E1)

    def lambda_61F2():

        label("loc_61F2")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_61F2")

    QueueWorkItem2(0x2B, 1, lambda_61F2)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x1E, 0x1)
    OP_44(0x1D, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x35, 0x1)
    OP_44(0x36, 0x1)
    OP_44(0x37, 0x1)
    OP_44(0x38, 0x1)
    OP_44(0x22, 0x1)
    OP_44(0x23, 0x1)
    OP_44(0x2F, 0x1)
    OP_44(0x32, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x2A, 0x1)
    OP_44(0x2B, 0x1)
    SetChrPos(0x10, 53660, 4130, 30220, 270)
    SetChrPos(0x11, 53740, 4130, 31140, 270)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    OP_72(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x16, 43540, 4000, 30950, 90)
    SetChrPos(0x12, 43160, 4000, 32119, 90)
    SetChrPos(0x1A, 42790, 4000, 30400, 90)
    SetChrPos(0x17, 43600, 4000, 29910, 90)
    SetChrPos(0x18, 43220, 4000, 29340, 90)
    SetChrPos(0x19, 43940, 4000, 28350, 90)
    SetChrPos(0x1B, 42720, 4000, 32960, 90)
    SetChrPos(0x1C, 42680, 4000, 33840, 90)
    SetChrPos(0x35, 41010, 4000, 32229, 90)
    SetChrPos(0x36, 41110, 4000, 31080, 90)
    SetChrPos(0x37, 42010, 4000, 31420, 90)
    SetChrPos(0x38, 41980, 4000, 32259, 90)
    SetChrPos(0x1E, 42060, 4000, 29640, 90)
    SetChrPos(0x1D, 42230, 4000, 28560, 90)
    SetChrPos(0x1F, 40750, 4000, 30070, 90)
    SetChrPos(0x20, 40670, 4000, 29150, 90)
    SetChrPos(0x22, 41250, 4000, 33520, 90)
    SetChrPos(0x23, 41370, 4000, 34320, 90)
    SetChrPos(0x32, 40040, 4000, 34890, 90)
    SetChrPos(0x25, 42090, 4000, 34950, 90)
    SetChrPos(0x26, 43240, 4000, 34520, 90)
    SetChrPos(0x28, 43480, 4000, 36760, 90)
    SetChrPos(0x27, 43320, 4000, 37670, 90)
    SetChrPos(0x2D, 43000, 4000, 39160, 90)
    SetChrPos(0x2E, 43010, 4000, 39830, 90)
    SetChrPos(0x21, 42210, 4000, 37270, 90)
    SetChrPos(0x2F, 41020, 4000, 36130, 90)
    SetChrPos(0x30, 41820, 4000, 36360, 90)
    SetChrPos(0x33, 39660, 4000, 36180, 90)
    SetChrPos(0x2C, 39810, 4000, 37000, 90)
    SetChrPos(0x29, 40170, 4000, 38030, 90)
    SetChrPos(0x24, 41370, 4000, 38160, 90)
    SetChrPos(0x2A, 41330, 4000, 38970, 90)
    SetChrPos(0x2B, 41330, 4000, 40000, 90)
    SetChrPos(0x34, 39690, 4000, 39230, 90)
    SetChrPos(0x31, 42390, 4000, 38320, 90)
    SetChrPos(0x13, 39360, 4000, 37960, 90)
    OP_6D(46470, 3930, 32210, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(315000, 0)
    OP_6E(384, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #145
        0x10,
        "#1000F#5PWell, goodbye for now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x1A,
        "#740FGood luck, both of you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x16,
        "#020FTake care of yourselves!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x11,
        "#1040F#5PWe will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x10,
        (
            "#1000F#5PYou, too, Schera.\x02\x03",

            "Don't go drinking so much you never wake up again\x01",
            "while we're away, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x16,
        (
            "#020FHaha. If you're that worried about my drinking\x01",
            "habits, maybe you should join me for a session\x01",
            "so you can keep an eye on me sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x18,
        "Do your best! I'll be cheering you on from here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x17,
        (
            "Estelle!\x02\x03",

            "I'm serious! By the time you get back, I'll be\x01",
            "a bracer, I swear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x19,
        (
            "#5PIf you end up in the Imperial Chronicle,\x01",
            "get in contact right away!\x02\x03",

            "I want to know! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x11,
        "#1040F#5PHaha. Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x10,
        "#1000F#5PTake care, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x12,
        (
            "#80FEstelle, Joshua...\x02\x03",

            "...Make sure you do return here one day, all\x01",
            "right?\x02\x03",

            "This is your home, and it always will be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x11,
        (
            "#1040F#5PWe will, Dad.\x02\x03",

            "We promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10,
        (
            "#1000F#5PHeehee...\x02\x03",

            "Don't worry, we most definitely will!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(2000)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x12C)
    Sleep(1800)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0xF, 0x32)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x3C)
    OP_73(0xF)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x77, 0x1, 0x64)
    Fade(500)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(45940, -5080, 40300, 0)
    OP_67(0, 9350, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(315000, 0)
    OP_6E(621, 0)

    def lambda_6997():
        OP_8F(0xFE, 0xDAC0, 0xFFFFF7E5, 0x8980, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6997)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xF, 61)
    OP_70(0xF, 0xA0)
    OP_73(0xF)
    OP_71(0x200F, 0x0)
    ExitThread()
    OP_6F(0xF, 161)
    OP_70(0xF, 0x104)
    WaitChrThread(0x14, 0x0)
    OP_0D()

    def lambda_69E2():

        label("loc_69E2")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_69E2")

    QueueWorkItem2(0x12, 1, lambda_69E2)

    def lambda_69F3():

        label("loc_69F3")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_69F3")

    QueueWorkItem2(0x16, 1, lambda_69F3)

    def lambda_6A04():

        label("loc_6A04")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A04")

    QueueWorkItem2(0x1A, 1, lambda_6A04)

    def lambda_6A15():

        label("loc_6A15")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A15")

    QueueWorkItem2(0x1E, 1, lambda_6A15)

    def lambda_6A26():

        label("loc_6A26")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A26")

    QueueWorkItem2(0x1D, 1, lambda_6A26)

    def lambda_6A37():

        label("loc_6A37")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A37")

    QueueWorkItem2(0x1B, 1, lambda_6A37)

    def lambda_6A48():

        label("loc_6A48")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A48")

    QueueWorkItem2(0x1C, 1, lambda_6A48)

    def lambda_6A59():

        label("loc_6A59")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A59")

    QueueWorkItem2(0x1F, 1, lambda_6A59)

    def lambda_6A6A():

        label("loc_6A6A")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A6A")

    QueueWorkItem2(0x20, 1, lambda_6A6A)

    def lambda_6A7B():

        label("loc_6A7B")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A7B")

    QueueWorkItem2(0x19, 1, lambda_6A7B)

    def lambda_6A8C():

        label("loc_6A8C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A8C")

    QueueWorkItem2(0x35, 1, lambda_6A8C)

    def lambda_6A9D():

        label("loc_6A9D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6A9D")

    QueueWorkItem2(0x36, 1, lambda_6A9D)

    def lambda_6AAE():

        label("loc_6AAE")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6AAE")

    QueueWorkItem2(0x37, 1, lambda_6AAE)

    def lambda_6ABF():

        label("loc_6ABF")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6ABF")

    QueueWorkItem2(0x38, 1, lambda_6ABF)

    def lambda_6AD0():

        label("loc_6AD0")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6AD0")

    QueueWorkItem2(0x22, 1, lambda_6AD0)

    def lambda_6AE1():

        label("loc_6AE1")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6AE1")

    QueueWorkItem2(0x23, 1, lambda_6AE1)

    def lambda_6AF2():

        label("loc_6AF2")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6AF2")

    QueueWorkItem2(0x2F, 1, lambda_6AF2)

    def lambda_6B03():

        label("loc_6B03")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B03")

    QueueWorkItem2(0x32, 1, lambda_6B03)

    def lambda_6B14():

        label("loc_6B14")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B14")

    QueueWorkItem2(0x25, 1, lambda_6B14)

    def lambda_6B25():

        label("loc_6B25")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B25")

    QueueWorkItem2(0x26, 1, lambda_6B25)

    def lambda_6B36():

        label("loc_6B36")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B36")

    QueueWorkItem2(0x2A, 1, lambda_6B36)

    def lambda_6B47():

        label("loc_6B47")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B47")

    QueueWorkItem2(0x2B, 1, lambda_6B47)

    def lambda_6B58():

        label("loc_6B58")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B58")

    QueueWorkItem2(0x34, 1, lambda_6B58)

    def lambda_6B69():

        label("loc_6B69")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B69")

    QueueWorkItem2(0x33, 1, lambda_6B69)

    def lambda_6B7A():

        label("loc_6B7A")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B7A")

    QueueWorkItem2(0x31, 1, lambda_6B7A)

    def lambda_6B8B():

        label("loc_6B8B")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B8B")

    QueueWorkItem2(0x30, 1, lambda_6B8B)

    def lambda_6B9C():

        label("loc_6B9C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6B9C")

    QueueWorkItem2(0x2F, 1, lambda_6B9C)

    def lambda_6BAD():

        label("loc_6BAD")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6BAD")

    QueueWorkItem2(0x2E, 1, lambda_6BAD)

    def lambda_6BBE():

        label("loc_6BBE")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6BBE")

    QueueWorkItem2(0x2D, 1, lambda_6BBE)

    def lambda_6BCF():

        label("loc_6BCF")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6BCF")

    QueueWorkItem2(0x2C, 1, lambda_6BCF)

    def lambda_6BE0():

        label("loc_6BE0")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6BE0")

    QueueWorkItem2(0x27, 1, lambda_6BE0)

    def lambda_6BF1():

        label("loc_6BF1")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6BF1")

    QueueWorkItem2(0x28, 1, lambda_6BF1)

    def lambda_6C02():

        label("loc_6C02")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6C02")

    QueueWorkItem2(0x29, 1, lambda_6C02)

    def lambda_6C13():

        label("loc_6C13")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_6C13")

    QueueWorkItem2(0x21, 1, lambda_6C13)

    def lambda_6C24():
        OP_6D(45940, -5080, 49300, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6C24)

    def lambda_6C3C():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6C3C)

    def lambda_6C57():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6C57)
    Sleep(200)

    def lambda_6C77():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6C77)

    def lambda_6C92():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6C92)
    Sleep(200)

    def lambda_6CB2():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6CB2)

    def lambda_6CCD():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6CCD)
    Sleep(200)

    def lambda_6CED():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6CED)

    def lambda_6D08():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6D08)
    Sleep(200)
    OP_43(0x17, 0x0, 0x0, 0x8)
    OP_43(0x18, 0x0, 0x0, 0x9)

    def lambda_6D36():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6D36)

    def lambda_6D51():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6D51)
    Sleep(200)

    def lambda_6D71():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6D71)

    def lambda_6D8C():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6D8C)
    Sleep(200)

    def lambda_6DAC():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6DAC)

    def lambda_6DC7():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6DC7)
    Sleep(200)

    def lambda_6DE7():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6DE7)

    def lambda_6E02():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6E02)
    Sleep(200)

    def lambda_6E22():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6E22)

    def lambda_6E3D():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6E3D)
    Sleep(200)

    def lambda_6E5D():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6E5D)

    def lambda_6E78():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6E78)
    Sleep(200)

    def lambda_6E98():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6E98)

    def lambda_6EB3():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6EB3)
    Sleep(200)

    def lambda_6ED3():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6ED3)

    def lambda_6EEE():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6EEE)
    Sleep(200)

    def lambda_6F0E():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6F0E)

    def lambda_6F29():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6F29)
    Sleep(200)

    def lambda_6F49():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6F49)

    def lambda_6F64():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6F64)
    Sleep(200)

    def lambda_6F84():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6F84)

    def lambda_6F9F():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6F9F)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(100)
    FadeToDark(2000, 0, -1)
    Sleep(200)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    OP_0D()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x40D, 0x0)
    ExitThread()
    SetMapFlags(0x2000000)
    OP_A2(0x250A)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_4373 end

    def Function_8_702F(): pass

    label("Function_8_702F")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 315, 400)
    OP_8E(0xFE, 0xA74E, 0xFA0, 0x7A26, 0x1388, 0x0)
    OP_8E(0xFE, 0xAB54, 0xFA0, 0x7CA6, 0x1388, 0x0)
    OP_8E(0xFE, 0xADB6, 0xFAA, 0xB5B8, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_8_702F end

    def Function_9_708F(): pass

    label("Function_9_708F")

    Sleep(300)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xAA78, 0xFA0, 0x7454, 0x1388, 0x0)
    OP_8E(0xFE, 0xA74E, 0xFA0, 0x7A26, 0x1388, 0x0)
    OP_8E(0xFE, 0xAB54, 0xFA0, 0x7CA6, 0x1388, 0x0)
    OP_8E(0xFE, 0xAC80, 0xFA0, 0xB068, 0x1388, 0x0)
    Sleep(300)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_9_708F end

    def Function_10_710D(): pass

    label("Function_10_710D")

    OP_8C(0xFE, 225, 400)
    OP_43(0x18, 0x0, 0x0, 0xC)
    OP_8E(0xFE, 0xA8A2, 0xFA0, 0x7D50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA8A2, 0xFA0, 0x7918, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB2AC, 0x1068, 0x7918, 0x7D0, 0x0)
    Return()

    # Function_10_710D end

    def Function_11_7158(): pass

    label("Function_11_7158")

    Sleep(300)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_8E(0xFE, 0xA992, 0xFA0, 0x807A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA8A2, 0xFA0, 0x7D50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA8A2, 0xFA0, 0x7918, 0x7D0, 0x0)
    Return()

    # Function_11_7158 end

    def Function_12_71A6(): pass

    label("Function_12_71A6")

    OP_8F(0xFE, 0xA85C, 0xFA0, 0x73F0, 0x5DC, 0x0)
    Return()

    # Function_12_71A6 end

    def Function_13_71BB(): pass

    label("Function_13_71BB")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x8804, 0x0, 0x6716, 0x1770, 0x0)
    OP_8E(0xFE, 0x8188, 0x0, 0x825A, 0x1770, 0x0)
    OP_8E(0xFE, 0x820A, 0x7D0, 0x9934, 0x1770, 0x0)
    OP_8E(0xFE, 0x951A, 0xFA0, 0x997A, 0x1770, 0x0)
    SetChrPos(0xFE, 42290, 4000, 30690, 270)
    Return()

    # Function_13_71BB end

    def Function_14_7224(): pass

    label("Function_14_7224")

    Sleep(200)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x8C14, 0x0, 0x64E6, 0x1770, 0x0)
    OP_8E(0xFE, 0x8188, 0x0, 0x825A, 0x1770, 0x0)
    OP_8E(0xFE, 0x820A, 0x7D0, 0x9934, 0x1770, 0x0)
    OP_8E(0xFE, 0x951A, 0xFA0, 0x997A, 0x1770, 0x0)
    SetChrPos(0xFE, 43090, 4000, 29830, 270)
    Return()

    # Function_14_7224 end

    def Function_15_7292(): pass

    label("Function_15_7292")

    OP_24(0xBF, 0x5A)
    Sleep(100)
    OP_24(0xBF, 0x50)
    Sleep(100)
    OP_24(0xBF, 0x46)
    Sleep(100)
    OP_24(0xBF, 0x3C)
    Sleep(100)
    OP_24(0xBF, 0x32)
    Sleep(100)
    OP_24(0xBF, 0x1E)
    Sleep(100)
    OP_24(0xBF, 0x14)
    Sleep(100)
    OP_24(0xBF, 0xA)
    Sleep(100)
    OP_24(0xBF, 0x0)
    OP_23(0xBF)
    Return()

    # Function_15_7292 end

    SaveToFile()

Try(main)
