from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4103   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Soldier',                              # 9
        'Soldier',                              # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Armand',                               # 17
        'Ellie',                                # 18
        'Troy',                                 # 19
        'Martin',                               # 20
        'Marian',                               # 21
        'Helena',                               # 22
        'Noel',                                 # 23
        'Becker',                               # 24
        'Palmer',                               # 25
        'Soldier',                              # 26
        'Soldier',                              # 27
        'Soldier',                              # 28
        'Soldier',                              # 29
        'Special Ops Soldier',                  # 30
        'Special Ops Soldier',                  # 31
        'Special Ops Soldier',                  # 32
        'Miele',                                # 33
        'Godfrey',                              # 34
        'Sister Ellen',                         # 35
        'Visitor',                              # 36
        'Visitor',                              # 37
        'Visitor',                              # 38
        'Visitor',                              # 39
        'Visitor',                              # 40
        'Visitor',                              # 41
        'Visitor',                              # 42
        'Visitor',                              # 43
        'Visitor',                              # 44
        'Visitor',                              # 45
        'Visitor',                              # 46
        'Visitor',                              # 47
        'Grancel - West Block',                 # 48
        'Grancel Castle',                       # 49
        'Grancel - East Block',                 # 50
        'Grancel - South Block',                # 51
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 66000,
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH02490 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01290 ._CH',             # 08
        'ED6_DT07/CH01200 ._CH',             # 09
        'ED6_DT07/CH01610 ._CH',             # 0A
        'ED6_DT07/CH01040 ._CH',             # 0B
        'ED6_DT07/CH01120 ._CH',             # 0C
        'ED6_DT07/CH01410 ._CH',             # 0D
        'ED6_DT07/CH01120 ._CH',             # 0E
        'ED6_DT07/CH01060 ._CH',             # 0F
        'ED6_DT07/CH01030 ._CH',             # 10
        'ED6_DT07/CH01130 ._CH',             # 11
        'ED6_DT07/CH01230 ._CH',             # 12
        'ED6_DT07/CH01220 ._CH',             # 13
        'ED6_DT07/CH02500 ._CH',             # 14
        'ED6_DT07/CH01680 ._CH',             # 15
        'ED6_DT07/CH01100 ._CH',             # 16
        'ED6_DT07/CH01110 ._CH',             # 17
        'ED6_DT07/CH01050 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH02490P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01290P._CP',             # 08
        'ED6_DT07/CH01200P._CP',             # 09
        'ED6_DT07/CH01610P._CP',             # 0A
        'ED6_DT07/CH01040P._CP',             # 0B
        'ED6_DT07/CH01120P._CP',             # 0C
        'ED6_DT07/CH01410P._CP',             # 0D
        'ED6_DT07/CH01120P._CP',             # 0E
        'ED6_DT07/CH01060P._CP',             # 0F
        'ED6_DT07/CH01030P._CP',             # 10
        'ED6_DT07/CH01130P._CP',             # 11
        'ED6_DT07/CH01230P._CP',             # 12
        'ED6_DT07/CH01220P._CP',             # 13
        'ED6_DT07/CH02500P._CP',             # 14
        'ED6_DT07/CH01680P._CP',             # 15
        'ED6_DT07/CH01100P._CP',             # 16
        'ED6_DT07/CH01110P._CP',             # 17
        'ED6_DT07/CH01050P._CP',             # 18
    )

    DeclNpc(
        X                   = -2980,
        Z                   = 0,
        Y                   = 68330,
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
        X                   = 3120,
        Z                   = 0,
        Y                   = 68420,
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
        X                   = -32570,
        Z                   = 0,
        Y                   = 50050,
        Direction           = 90,
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
        X                   = -9530,
        Z                   = 250,
        Y                   = 32240,
        Direction           = 90,
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
        X                   = 9480,
        Z                   = 250,
        Y                   = 37480,
        Direction           = 270,
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
        X                   = 560,
        Z                   = 0,
        Y                   = 39030,
        Direction           = 225,
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
        X                   = -370,
        Z                   = 0,
        Y                   = 38160,
        Direction           = 45,
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
        X                   = 3800,
        Z                   = 0,
        Y                   = 65780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 45,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
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
        InitScenaIndex      = 3,
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
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 6490,
        Z                   = 0,
        Y                   = 43840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -2950,
        Z                   = 0,
        Y                   = 63820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -7440,
        Z                   = 0,
        Y                   = 49400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -6340,
        Z                   = 0,
        Y                   = 52120,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 6490,
        Z                   = 0,
        Y                   = 43840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -2950,
        Z                   = 0,
        Y                   = 63820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 3660,
        Z                   = 0,
        Y                   = 64440,
        Direction           = 356,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -7400,
        Z                   = 250,
        Y                   = 59390,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 4750,
        Z                   = 0,
        Y                   = 10320,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -710,
        Z                   = 0,
        Y                   = 68870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -5260,
        Z                   = 0,
        Y                   = 66960,
        Direction           = 131,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -5940,
        Z                   = 0,
        Y                   = 65580,
        Direction           = 30,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -8140,
        Z                   = 250,
        Y                   = 56080,
        Direction           = 219,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -10060,
        Z                   = 250,
        Y                   = 56020,
        Direction           = 149,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -9190,
        Z                   = 250,
        Y                   = 54240,
        Direction           = 9,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 7480,
        Z                   = 250,
        Y                   = 59730,
        Direction           = 267,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 9690,
        Z                   = 250,
        Y                   = 50490,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 7050,
        Z                   = 250,
        Y                   = 50520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 9510,
        Z                   = 0,
        Y                   = 44040,
        Direction           = 96,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 8700,
        Z                   = 0,
        Y                   = 44910,
        Direction           = 108,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 7190,
        Z                   = 250,
        Y                   = 38180,
        Direction           = 258,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = -7530,
        Z                   = 250,
        Y                   = 44220,
        Direction           = 37,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = -40080,
        Z                   = 0,
        Y                   = 17660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 100,
        Z                   = 0,
        Y                   = 104130,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40430,
        Z                   = 0,
        Y                   = 64060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 0,
        Y                   = -3500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 18520,
        Y                   = 0,
        Z                   = 44050,
        Range               = 1500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 48,
    )


    ScpFunction(
        "Function_0_6F2",          # 00, 0
        "Function_1_93C",          # 01, 1
        "Function_2_B15",          # 02, 2
        "Function_3_B2A",          # 03, 3
        "Function_4_CA7",          # 04, 4
        "Function_5_CED",          # 05, 5
        "Function_6_EFE",          # 06, 6
        "Function_7_F58",          # 07, 7
        "Function_8_FE5",          # 08, 8
        "Function_9_107C",         # 09, 9
        "Function_10_1183",        # 0A, 10
        "Function_11_11A7",        # 0B, 11
        "Function_12_11E8",        # 0C, 12
        "Function_13_147A",        # 0D, 13
        "Function_14_17DC",        # 0E, 14
        "Function_15_1856",        # 0F, 15
        "Function_16_1C2A",        # 10, 16
        "Function_17_1EB1",        # 11, 17
        "Function_18_2163",        # 12, 18
        "Function_19_2420",        # 13, 19
        "Function_20_2457",        # 14, 20
        "Function_21_247F",        # 15, 21
        "Function_22_2549",        # 16, 22
        "Function_23_313F",        # 17, 23
        "Function_24_3731",        # 18, 24
        "Function_25_45F5",        # 19, 25
        "Function_26_468D",        # 1A, 26
        "Function_27_4733",        # 1B, 27
        "Function_28_4814",        # 1C, 28
        "Function_29_48DA",        # 1D, 29
        "Function_30_4B3D",        # 1E, 30
        "Function_31_4EC7",        # 1F, 31
        "Function_32_4F3B",        # 20, 32
        "Function_33_4F5E",        # 21, 33
        "Function_34_4FF1",        # 22, 34
        "Function_35_50A5",        # 23, 35
        "Function_36_512E",        # 24, 36
        "Function_37_5217",        # 25, 37
        "Function_38_5263",        # 26, 38
        "Function_39_52EF",        # 27, 39
        "Function_40_53F0",        # 28, 40
        "Function_41_5446",        # 29, 41
        "Function_42_5491",        # 2A, 42
        "Function_43_54EF",        # 2B, 43
        "Function_44_55B6",        # 2C, 44
        "Function_45_55B7",        # 2D, 45
        "Function_46_5614",        # 2E, 46
        "Function_47_5853",        # 2F, 47
        "Function_48_59A0",        # 30, 48
    )


    def Function_0_6F2(): pass

    label("Function_0_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_70E")
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 43)
    OP_B1("t4103_n")

    label("loc_70E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (110, "loc_71A"),
        (SWITCH_DEFAULT, "loc_730"),
    )


    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    OP_A2(0x62C)
    Event(0, 47)

    label("loc_72D")

    Jump("loc_730")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7F4")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -7310, 250, 28970, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -9190, 250, 29720, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -9190, 250, 28210, 90)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x10)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x10)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x10)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x10)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x10)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x10)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    Jump("loc_93B")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_848")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -3840, 0, 67340, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -2760, 0, 67340, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_93B")

    label("loc_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_897")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3820, 0, 66400, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2760, 0, 66400, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_93B")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8B5")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_93B")

    label("loc_8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8D3")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_93B")

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_8F1")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_93B")

    label("loc_8F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_911")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 3080, 0, 67910, 0)
    Jump("loc_93B")

    label("loc_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_920")
    ClearChrFlags(0x22, 0x80)
    Jump("loc_93B")

    label("loc_920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_92A")
    Jump("loc_93B")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_934")
    Jump("loc_93B")

    label("loc_934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_93B")

    label("loc_93B")

    Return()

    # Function_0_6F2 end

    def Function_1_93C(): pass

    label("Function_1_93C")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x3005E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_981")
    OP_B1("t4103_y")
    Jump("loc_98A")

    label("loc_981")

    OP_B1("t4103_n")

    label("loc_98A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CC")
    OP_72(0x6, 0x8)
    OP_72(0x6, 0x20)
    OP_72(0x6, 0x2)
    OP_6F(0x6, 0)
    OP_72(0x2, 0x10)
    OP_72(0x5, 0x8)
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x2)
    OP_6F(0x5, 0)
    OP_72(0x3, 0x10)

    label("loc_9CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A38")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_43(0x8, 0x1, 0x0, 0x2E)
    OP_43(0x9, 0x1, 0x0, 0x2E)
    OP_43(0xA, 0x1, 0x0, 0x2E)
    OP_43(0xB, 0x1, 0x0, 0x2E)
    OP_43(0xC, 0x1, 0x0, 0x2E)
    OP_43(0xD, 0x1, 0x0, 0x2E)
    OP_43(0xE, 0x1, 0x0, 0x2E)
    OP_43(0xF, 0x1, 0x0, 0x2E)

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_B14")
    OP_72(0x7, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    SetMapFlags(0x800)
    OP_1B(0x7, 0x0, 0x2)
    OP_1B(0x6, 0x0, 0x2)
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -40, 250, 54930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 90, 0, 39630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 90, 250, 20100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_B14")

    Return()

    # Function_1_93C end

    def Function_2_B15(): pass

    label("Function_2_B15")

    ClearMapFlags(0x800)
    ClearMapFlags(0x2000000)
    OP_1B(0x7, 0x0, 0xFFFF)
    OP_1B(0x6, 0x0, 0xFFFF)
    Return()

    # Function_2_B15 end

    def Function_3_B2A(): pass

    label("Function_3_B2A")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_C91")

    label("loc_B4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B68")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_C91")

    label("loc_B68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B81")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_C91")

    label("loc_B81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_C91")

    label("loc_B9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_C91")

    label("loc_BB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_C91")

    label("loc_BCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_C91")

    label("loc_BE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_C91")

    label("loc_BFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C17")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_C91")

    label("loc_C17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C30")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_C91")

    label("loc_C30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C49")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_C91")

    label("loc_C49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C62")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_C91")

    label("loc_C62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_C91")

    label("loc_C7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C91")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_C91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_C91")

    label("loc_CA6")

    Return()

    # Function_3_B2A end

    def Function_4_CA7(): pass

    label("Function_4_CA7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CEC")
    SetChrPos(0xFE, 31870, 0, 62980, 270)
    OP_8E(0xFE, 0xC6C, 0x0, 0xF604, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x40CE, 0x7D0, 0x0)
    Jump("Function_4_CA7")

    label("loc_CEC")

    Return()

    # Function_4_CA7 end

    def Function_5_CED(): pass

    label("Function_5_CED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EFD")
    SetChrPos(0xFE, -40860, 0, 28340, 0)
    OP_8E(0xFE, 0xFFFF6064, 0x0, 0xBAE0, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF624E, 0x0, 0xC422, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF9F48, 0xFA, 0xF1F4, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(400)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFE674, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xCED6, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xF276, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFF16E, 0x0, 0xFD84, 0x2328, 0x0)
    OP_8E(0xFE, 0x9B8C, 0x0, 0xFD84, 0x2328, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 39650, 0, 62210, 90)
    OP_8E(0xFE, 0x67A2, 0x0, 0xF302, 0x2328, 0x0)
    OP_8E(0xFE, 0x56B8, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2A9E, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xDC00, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xC030, 0x2328, 0x0)
    OP_8E(0xFE, 0x2BE8, 0xFA, 0xB6D0, 0x2328, 0x0)
    OP_8E(0xFE, 0x402E, 0xFA, 0xB6D0, 0x2328, 0x0)
    Sleep(400)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x8E12, 0x2328, 0x0)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x1F04, 0x2328, 0x0)
    Sleep(2000)
    Jump("Function_5_CED")

    label("loc_EFD")

    Return()

    # Function_5_CED end

    def Function_6_EFE(): pass

    label("Function_6_EFE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F57")
    SetChrPos(0xFE, -4340, 0, 16160, 0)
    OP_8E(0xFE, 0xFFFFEF0C, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0x6B58, 0x9C4, 0x0)
    Jump("Function_6_EFE")

    label("loc_F57")

    Return()

    # Function_6_EFE end

    def Function_7_F58(): pass

    label("Function_7_F58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FE4")
    OP_8E(0xFE, 0x195A, 0x0, 0xB95A, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x195A, 0x0, 0xAB40, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x195A, 0x0, 0x9DDA, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x195A, 0x0, 0xAB40, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    Jump("Function_7_F58")

    label("loc_FE4")

    Return()

    # Function_7_F58 end

    def Function_8_FE5(): pass

    label("Function_8_FE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_107B")
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0x5528, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xF94C, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_8_FE5")

    label("loc_107B")

    Return()

    # Function_8_FE5 end

    def Function_9_107C(): pass

    label("Function_9_107C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1182")
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF65E6, 0x0, 0xBBE4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0x9592, 0x9C4, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF676C, 0x0, 0xC1E8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFE2F0, 0x0, 0xC0F8, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_9_107C")

    label("loc_1182")

    Return()

    # Function_9_107C end

    def Function_10_1183(): pass

    label("Function_10_1183")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11A6")
    OP_8D(0xFE, -7060, 65710, 5760, 62220, 3000)
    Jump("Function_10_1183")

    label("loc_11A6")

    Return()

    # Function_10_1183 end

    def Function_11_11A7(): pass

    label("Function_11_11A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11E7")
    OP_8E(0xFE, 0x11C6, 0x0, 0xEE84, 0xAF0, 0x0)
    Sleep(3000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x128E, 0x0, 0x2850, 0xAF0, 0x0)
    Jump("Function_11_11A7")

    label("loc_11E7")

    Return()

    # Function_11_11A7 end

    def Function_12_11E8(): pass

    label("Function_12_11E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 6)), scpexpr(EXPR_END)), "loc_12DF")

    ChrTalk(    #0
        0xFE,
        "I-I get lost easily, you see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I still don't know the streets of\x01",
            "Grancel very well, and they're\x01",
            "just...so confusing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#010FThat's quite unfortunate. I hope\x01",
            "you're able to find your way back,\x01",
            "though. Please, be careful!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1476")

    label("loc_12DF")

    OP_A2(0x67E)

    ChrTalk(    #3
        0xFE,
        "It's...it's you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#001FHey, Sister Ellen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#014FWhat are you doing in a place\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #6
        0xFE,
        (
            "I was sent out on an errand,\x01",
            "but...I got lost along the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#010FWould you like us to show\x01",
            "you back to the cathedral?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Oh, thank you, but no. One of\x01",
            "the soldiers already told me\x01",
            "how to get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#000FOh, okay then. Be careful,\x01",
            "though!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "I will. Thank you.\x02",
    )

    CloseMessageWindow()

    label("loc_1476")

    TalkEnd(0xFE)
    Return()

    # Function_12_11E8 end

    def Function_13_147A(): pass

    label("Function_13_147A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_14B3")

    ChrTalk(    #11
        0xFE,
        (
            "Haven't felt this good in a\x01",
            "long time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D8")

    label("loc_14B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1565")

    ChrTalk(    #12
        0xFE,
        "*yaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I think I'll check out that coffee\x01",
            "house in the West Block and get\x01",
            "something to wake myself up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Well, the soldiers are sure\x01",
            "up early, it seems.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D8")

    label("loc_1565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_178B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_160B")

    ChrTalk(    #15
        0xFE,
        "Guard duty must be the pits.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "All I'm doing is...well...loitering.\x01",
            "But those soldiers keep on questioning\x01",
            "me like I'm some kinda terrorist!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1788")

    label("loc_160B")

    OP_A2(0x10)

    ChrTalk(    #17
        0xFE,
        (
            "Wow, that final match was cra-zy!\x01",
            "I was drinking so much to...erm...\x01",
            "commemorate the victory...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "...I wound up waking up in a very unfamiliar\x01",
            "place this morning. In circumstances I...would\x01",
            "prefer not to recount, thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Guard duty must be the pits.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "All I'm doing is...well...loitering.\x01",
            "But those soldiers keep on questioning\x01",
            "me like I'm some kinda terrorist!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1788")

    Jump("loc_17D8")

    label("loc_178B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1795")
    Jump("loc_17D8")

    label("loc_1795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_179F")
    Jump("loc_17D8")

    label("loc_179F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_17A9")
    Jump("loc_17D8")

    label("loc_17A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_17B3")
    Jump("loc_17D8")

    label("loc_17B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_17BD")
    Jump("loc_17D8")

    label("loc_17BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_17C7")
    Jump("loc_17D8")

    label("loc_17C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_17D1")
    Jump("loc_17D8")

    label("loc_17D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_17D8")

    label("loc_17D8")

    TalkEnd(0xFE)
    Return()

    # Function_13_147A end

    def Function_14_17DC(): pass

    label("Function_14_17DC")

    TalkBegin(0xFE)

    ChrTalk(    #21
        0xFE,
        (
            "I hear the bracers who won the\x01",
            "tournament were the same ones\x01",
            "who stopped the coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "How amazing is that?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_17DC end

    def Function_15_1856(): pass

    label("Function_15_1856")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_18B3")

    ChrTalk(    #23
        0xFE,
        (
            "Please move along! Dawdling is seen as\x01",
            "suspicious, and WILL be questioned!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C26")

    label("loc_18B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_18BD")
    Jump("loc_1C26")

    label("loc_18BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1968")

    ChrTalk(    #24
        0xFE,
        (
            "The Birthday Celebration's\x01",
            "almost upon us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I'm hoping to catch those terrorists\x01",
            "before it ends...so we can go out on\x01",
            "a happy note this year, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C26")

    label("loc_1968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_19AF")

    ChrTalk(    #26
        0xFE,
        "Looks like the finals're over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "I wonder who won...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C26")

    label("loc_19AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1A71")

    ChrTalk(    #28
        0xFE,
        (
            "I don't much care for those Special\x01",
            "Ops guys, so personally, I'm rooting\x01",
            "for the bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "...Though if you tell anyone I said\x01",
            "that, I'll have you drawn and quartered!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B43")

    label("loc_1A71")

    OP_A2(0x8)

    ChrTalk(    #30
        0xFE,
        "So, final match today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I don't much care for those Special\x01",
            "Ops guys, so personally, I'm rooting\x01",
            "for the bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "...Though if you tell anyone I said\x01",
            "that, I'll have you drawn and quartered!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B43")

    Jump("loc_1C26")

    label("loc_1B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1BF7")

    ChrTalk(    #33
        0xFE,
        (
            "I don't like to be a wet blanket during\x01",
            "such a festive time, but I have my orders,\x01",
            "and I intend to follow them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Civilian cooperation is greatly\x01",
            "appreciated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C26")

    label("loc_1BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C01")
    Jump("loc_1C26")

    label("loc_1C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C0B")
    Jump("loc_1C26")

    label("loc_1C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1C15")
    Jump("loc_1C26")

    label("loc_1C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1C1F")
    Jump("loc_1C26")

    label("loc_1C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1C26")

    label("loc_1C26")

    TalkEnd(0xFE)
    Return()

    # Function_15_1856 end

    def Function_16_1C2A(): pass

    label("Function_16_1C2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1C91")

    ChrTalk(    #35
        0xFE,
        "Nothing to report!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I'm going to hit the town myself\x01",
            "after my watch is finished.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1C9B")
    Jump("loc_1EAD")

    label("loc_1C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CF2")

    ChrTalk(    #37
        0xFE,
        (
            "If you see anything unusual or\x01",
            "unlawful, please be sure to let\x01",
            "us know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D65")

    ChrTalk(    #38
        0xFE,
        (
            "The Royal Guardsmen? Terrorists?\x01",
            "Really?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Personally, I don't buy a word\x01",
            "of it. Don't WANT to!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1E04")

    ChrTalk(    #40
        0xFE,
        (
            "I mean, if I find one of them\x01",
            "and he puts up any kind of fight\x01",
            "at all...I'm done for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Those guys pretty much wrote the\x01",
            "book on bad-assery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1E7E")

    ChrTalk(    #42
        0xFE,
        (
            "If you see anyone you suspect might\x01",
            "be a member of the Royal Guard, please\x01",
            "let one of us know immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAD")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1E88")
    Jump("loc_1EAD")

    label("loc_1E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E92")
    Jump("loc_1EAD")

    label("loc_1E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1E9C")
    Jump("loc_1EAD")

    label("loc_1E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1EA6")
    Jump("loc_1EAD")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1EAD")

    label("loc_1EAD")

    TalkEnd(0xFE)
    Return()

    # Function_16_1C2A end

    def Function_17_1EB1(): pass

    label("Function_17_1EB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1F92")

    ChrTalk(    #43
        0xFE,
        (
            "I just don't think they did it... I mean,\x01",
            "if they did anything, they were probably\x01",
            "just trying to protect Her Majesty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Seriously, they're model soldiers!\x01",
            "How can we have anything BUT\x01",
            "respect for them?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_1F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1F9C")
    Jump("loc_215F")

    label("loc_1F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2057")

    ChrTalk(    #45
        0xFE,
        (
            "I just don't buy that the Royal\x01",
            "Guardsmen are terrorists. It's\x01",
            "pure crazy talk!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "We like to talk that they're\x01",
            "all just pomp and ceremony,\x01",
            "but we really do know better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_2057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_20BF")

    ChrTalk(    #47
        0xFE,
        "Nothing to report here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "My replacement should be here\x01",
            "any moment now. THANK AIDIOS.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_20BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_20F1")

    ChrTalk(    #49
        0xFE,
        "Sorry, but I'm busy at the moment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_20F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2130")

    ChrTalk(    #50
        0xFE,
        (
            "Sorry, I'm on watch. And you're\x01",
            "distracting me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_2130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_213A")
    Jump("loc_215F")

    label("loc_213A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2144")
    Jump("loc_215F")

    label("loc_2144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_214E")
    Jump("loc_215F")

    label("loc_214E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2158")
    Jump("loc_215F")

    label("loc_2158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_215F")

    label("loc_215F")

    TalkEnd(0xFE)
    Return()

    # Function_17_1EB1 end

    def Function_18_2163(): pass

    label("Function_18_2163")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_21FA")

    ChrTalk(    #51
        0xFE,
        (
            "Colonel Richard was behind the\x01",
            "coup d'etat... I still can't\x01",
            "believe it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Hell, I don't WANT to believe it!\x01",
            "I respected that man!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_21FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2204")
    Jump("loc_241C")

    label("loc_2204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_22AC")

    ChrTalk(    #53
        0xFE,
        (
            "Look, you're in the way. Please,\x01",
            "just...move along, already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "The terrorists could be anywhere.\x01",
            "AnyONE. I've got to keep a close\x01",
            "eye on the crowd...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_22AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2342")

    ChrTalk(    #55
        0xFE,
        (
            "So apparently, the Special Ops\x01",
            "team lost the match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Didn't think the bracers would\x01",
            "be able to take them. But oh,\x01",
            "how wrong I was!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2398")

    ChrTalk(    #57
        0xFE,
        (
            "Colonel Richard is an incredible\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Seriously, don't you agree?\x02",
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_2398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_23ED")

    ChrTalk(    #59
        0xFE,
        (
            "Bracer or not, I'll arrest you\x01",
            "if you do anything suspicious.\x01",
            "Got it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241C")

    label("loc_23ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_23F7")
    Jump("loc_241C")

    label("loc_23F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2401")
    Jump("loc_241C")

    label("loc_2401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_240B")
    Jump("loc_241C")

    label("loc_240B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2415")
    Jump("loc_241C")

    label("loc_2415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_241C")

    label("loc_241C")

    TalkEnd(0xFE)
    Return()

    # Function_18_2163 end

    def Function_19_2420(): pass

    label("Function_19_2420")

    TalkBegin(0xFE)

    ChrTalk(    #60
        0xFE,
        (
            "Hmm... Nope, nothing to report\x01",
            "here. Drat!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2420 end

    def Function_20_2457(): pass

    label("Function_20_2457")

    TalkBegin(0xFE)

    ChrTalk(    #61
        0xFE,
        "Hey, move it! Outta my way!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2457 end

    def Function_21_247F(): pass

    label("Function_21_247F")

    TalkBegin(0xFE)

    ChrTalk(    #62
        0xFE,
        (
            "We Special Ops have been charged\x01",
            "with protecting the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "And we don't need anyone else for the job.\x01",
            "We can handle it on our own--and would\x01",
            "actually PREFER to handle it on our own.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_247F end

    def Function_22_2549(): pass

    label("Function_22_2549")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_25F0")

    ChrTalk(    #64
        0xFE,
        (
            "I finally got to see the queen, for\x01",
            "the first time in...I don't even\x01",
            "know how long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "As soon as I saw her face, all\x01",
            "my worries just melted away!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313B")

    label("loc_25F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_26BD")

    ChrTalk(    #66
        0xFE,
        (
            "Seems all the regular, run-of-the-mill\x01",
            "soldiers have been ordered away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Those black-armored guys are even\x01",
            "guarding the castle gates!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Something about that...just doesn't\x01",
            "bode well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313B")

    label("loc_26BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_28ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2790")

    ChrTalk(    #69
        0xFE,
        (
            "With the tournament over it's\x01",
            "almost time for the queen's\x01",
            "Birthday Celebration. But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Nobody knows anything about Her\x01",
            "Majesty's illness, or...what's\x01",
            "happening around here in general!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EA")

    label("loc_2790")

    OP_A2(0x5)

    ChrTalk(    #71
        0xFE,
        (
            "With the tournament over it'll\x01",
            "soon be time for the queen's\x01",
            "Birthday Celebration. But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Nobody knows anything about Her\x01",
            "Majesty's illness, or...what's\x01",
            "happening around here in general!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I guess it makes sense that Duke Dunan would be\x01",
            "acting in place of the queen, given the circum-\x01",
            "stances. But still...why don't we know more?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EA")

    Jump("loc_313B")

    label("loc_28ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2936")

    ChrTalk(    #74
        0xFE,
        (
            "Evening already? I guess I'd\x01",
            "better start heading home...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313B")

    label("loc_2936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_29F9")

    ChrTalk(    #75
        0xFE,
        (
            "Today's already the last day\x01",
            "of the tournament. Time sure\x01",
            "does fly, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "I guess that means I should head\x01",
            "to the arena. Today's match seems\x01",
            "like it's not to be missed!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313B")

    label("loc_29F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2A6F")

    ChrTalk(    #77
        0xFE,
        (
            "I've seen those black-armored\x01",
            "soldiers going in and out of\x01",
            "the castle before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "But who are they?\x02",
    )

    CloseMessageWindow()
    Jump("loc_313B")

    label("loc_2A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2C0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2B13")

    ChrTalk(    #79
        0xFE,
        (
            "You know that open area in front\x01",
            "of the castle gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "On the day of the Birthday\x01",
            "Celebration, you can see Her\x01",
            "Majesty if you stand there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C07")

    label("loc_2B13")

    OP_A2(0x5)

    ChrTalk(    #81
        0xFE,
        (
            "You know that open area in front\x01",
            "of the castle gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "On the day of the Birthday\x01",
            "Celebration, you can see Her\x01",
            "Majesty if you stand there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "...You could in previous years,\x01",
            "anyway. But this year? No idea\x01",
            "if she'll even show up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C07")

    Jump("loc_313B")

    label("loc_2C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2E7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2D19")

    ChrTalk(    #84
        0xFE,
        (
            "The Garden Terrace in the castle catches the\x01",
            "breeze from Lake Valleria, and the smell of\x01",
            "the greenery there is just...so relaxing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "It's under lockdown right now, but once\x01",
            "the castle reopens, I HIGHLY recommend\x01",
            "going up there to check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7B")

    label("loc_2D19")

    OP_A2(0x5)

    ChrTalk(    #86
        0xFE,
        (
            "Any other year, you'd be able to\x01",
            "tour the inside of the castle--\x01",
            "Garden Terrace and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "And that Garden Terrace... Ohh man, the breeze\x01",
            "from Lake Valleria spreads around the smells of\x01",
            "all its greenery. It's just...so serene!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "It's under lockdown right now, but once\x01",
            "the castle reopens, I HIGHLY recommend\x01",
            "going up there to check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E7B")

    Jump("loc_313B")

    label("loc_2E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2F22")

    ChrTalk(    #89
        0xFE,
        (
            "Until just recently, you used\x01",
            "to be able to sign up to tour\x01",
            "the inside of the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "But after the queen got sick,\x01",
            "they locked the place down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313B")

    label("loc_2F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F7E")

    ChrTalk(    #91
        0xFE,
        (
            "If Queen Alicia is the pride of\x01",
            "Liberl, then Duke Dunan is its\x01",
            "shame.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3065")

    label("loc_2F7E")

    OP_A2(0x5)

    ChrTalk(    #92
        0xFE,
        (
            "Earlier, Duke Dunan was standing\x01",
            "out in front of the castle gate,\x01",
            "looking a bit flustered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "I can't believe he's standing\x01",
            "in for Her Majesty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "If Queen Alicia is the pride of\x01",
            "Liberl, then Duke Dunan is its\x01",
            "shame.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3065")

    Jump("loc_313B")

    label("loc_3068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_313B")

    ChrTalk(    #95
        0xFE,
        (
            "Even with the tournament underway,\x01",
            "there are fewer tourists here than\x01",
            "usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Probably because the castle's under lockdown.\x01",
            "I mean, people come for the tournament...but\x01",
            "they stay for the castle!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313B")

    TalkEnd(0xFE)
    Return()

    # Function_22_2549 end

    def Function_23_313F(): pass

    label("Function_23_313F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_31B1")

    ChrTalk(    #97
        0xFE,
        (
            "Messengers don't get off for the\x01",
            "Queen's Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "The service industry sucks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_31B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3260")

    ChrTalk(    #99
        0xFE,
        (
            "The landing port's closed. No one\x01",
            "can get in or out of the country\x01",
            "right now. Not by air, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Once I finish this delivery,\x01",
            "my work's done for the day!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_3260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_32CE")

    ChrTalk(    #101
        0xFE,
        (
            "Yesterday there were a lot\x01",
            "of soldiers patrolling the\x01",
            "landing port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "What happened there?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_32CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3336")

    ChrTalk(    #103
        0xFE,
        (
            "The next issue of the Liberl\x01",
            "News is a tournament special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "I can't wait to read it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_3336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_33FA")

    ChrTalk(    #105
        0xFE,
        (
            "Soldiers keep stopping me for questions,\x01",
            "and honestly, it's making my job take\x01",
            "three times longer than it has to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "It's definitely...not good for\x01",
            "the blood pressure, let's say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_33FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3459")

    ChrTalk(    #107
        0xFE,
        "So, next delivery is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Whoa, is it evening already?!\x01",
            "I'd better hurry up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_3459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_34E1")

    ChrTalk(    #109
        0xFE,
        "Let's see here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "After I deliver this package, I think\x01",
            "I'll head back to the landing port and\x01",
            "have myself a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_34E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3561")

    ChrTalk(    #111
        0xFE,
        (
            "You know what's annoying? Not\x01",
            "being able to read the delivery\x01",
            "address on a package.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "LEARN TO WRITE, PEOPLE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_3561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_35FA")

    ChrTalk(    #113
        0xFE,
        (
            "If only I didn't have work, I\x01",
            "could go see the tournament...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "But for a delivery boy, tourist\x01",
            "season just means MORE work...\x01",
            "Le sigh!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_35FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_36C5")

    ChrTalk(    #115
        0xFE,
        (
            "When I came back to the landing port to pick\x01",
            "up the mail, the Arseille was completely\x01",
            "surrounded by soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "No idea what was going on, and nobody\x01",
            "seemed to be offering any answers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_36C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_372D")

    ChrTalk(    #117
        0xFE,
        "So, next package...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Man, this city is freaking HUGE.\x01",
            "I hate being a delivery boy here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_372D")

    TalkEnd(0xFE)
    Return()

    # Function_23_313F end

    def Function_24_3731(): pass

    label("Function_24_3731")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3867")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_37A8")

    ChrTalk(    #119
        0xFE,
        (
            "Times may be tough, but at least\x01",
            "Colonel Bright's back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "We've just got to hang in there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3864")

    label("loc_37A8")

    OP_A2(0x7)

    ChrTalk(    #121
        0xFE,
        (
            "Ugh, this is just what I was afraid of...\x01",
            "Lots and lots of backed-up deliveries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Times may be tough, but at least\x01",
            "Colonel Bright's back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "We've just got to hang in there!\x02",
    )

    CloseMessageWindow()

    label("loc_3864")

    Jump("loc_45F1")

    label("loc_3867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3923")

    ChrTalk(    #124
        0xFE,
        (
            "So without warning, the Royal Garrison's\x01",
            "been completely replaced by these Special\x01",
            "Ops guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Can't help but think something\x01",
            "terrible must be happening in\x01",
            "the castle...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F1")

    label("loc_3923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_39A8")

    ChrTalk(    #126
        0xFE,
        (
            "Everywhere you go, you see those\x01",
            "Special Ops soldiers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "And yet, they haven't found\x01",
            "even one Royal Guardsman yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F1")

    label("loc_39A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3B77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3A74")

    ChrTalk(    #128
        0xFE,
        (
            "Those guys at the Intelligence\x01",
            "Division look so smug when\x01",
            "they start with the questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "You'd think they'd show some\x01",
            "modicum of compassion, since\x01",
            "we're loyal citizens and all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B74")

    label("loc_3A74")

    OP_A2(0x7)

    ChrTalk(    #130
        0xFE,
        (
            "Those guys at the Intelligence\x01",
            "Division act so smarmy when\x01",
            "they start with the questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "You'd think they'd show some\x01",
            "modicum of compassion, since\x01",
            "we're loyal citizens and all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Especially Captain Amalthea...\x01",
            "She's the worst of them all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B74")

    Jump("loc_45F1")

    label("loc_3B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3C32")

    ChrTalk(    #133
        0xFE,
        (
            "Rumor has it the Arseille's\x01",
            "been seized by the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Colonel Richard doesn't strike me as\x01",
            "a particularly cheery person. And I\x01",
            "doubt I'm alone in thinking that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D60")

    label("loc_3C32")

    OP_A2(0x7)

    ChrTalk(    #135
        0xFE,
        (
            "Rumor has it the Arseille's\x01",
            "been seized by the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I know the Royal Guardsmen used it for official\x01",
            "business on occasion...but it's actually the\x01",
            "royal family's ship, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Colonel Richard doesn't strike me as\x01",
            "a particularly cheery person. And I\x01",
            "doubt I'm alone in thinking that!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D60")

    Jump("loc_45F1")

    label("loc_3D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3E4A")

    ChrTalk(    #138
        0xFE,
        (
            "Colonel Richard seems to be\x01",
            "having a devil of a time\x01",
            "finding the Royal Guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "This new Intelligence Division is going to \x01",
            "run into trouble trying to get the people\x01",
            "of the city to cooperate with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F76")

    label("loc_3E4A")

    OP_A2(0x7)

    ChrTalk(    #140
        0xFE,
        (
            "Colonel Richard seems to be\x01",
            "having a devil of a time\x01",
            "finding the Royal Guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "The Royal Guardsmen have been\x01",
            "popular with the citizens for\x01",
            "a very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "This new Intelligence Division is going to \x01",
            "run into trouble trying to get the people\x01",
            "of the city to cooperate with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F76")

    Jump("loc_45F1")

    label("loc_3F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_41B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4010")

    ChrTalk(    #143
        0xFE,
        (
            "Even among officials like me, there are an\x01",
            "awful lot of people who are going to sympathize\x01",
            "with the Royal Guard, no matter what.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41B4")

    label("loc_4010")

    OP_A2(0x7)

    ChrTalk(    #144
        0xFE,
        (
            "Even among officials like me, there are an\x01",
            "awful lot of people who are going to sympathize\x01",
            "with the Royal Guard, no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "At the time of the terrorist attack, they were\x01",
            "supposed to be at the Erbe Royal Villa performing\x01",
            "drills. And only Intel says they weren't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "One would think that's a pretty solid alibi with\x01",
            "lots of witnesses...but the duke still issued\x01",
            "arrest warrants for every one of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41B4")

    Jump("loc_45F1")

    label("loc_41B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_428D")

    ChrTalk(    #147
        0xFE,
        (
            "I actually was off on vacation on the day\x01",
            "it happened, and saw some Intel troops lead-\x01",
            "ing some Royal Guardsmen away. It was scary!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Lieutenant Schwarz must've\x01",
            "really pissed SOMEBODY off!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4394")

    label("loc_428D")

    OP_A2(0x7)

    ChrTalk(    #149
        0xFE,
        (
            "I actually was off on vacation on the day\x01",
            "it happened, and saw some Intel troops lead-\x01",
            "ing some Royal Guardsmen away. It was scary!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "All the soldiers left behind in\x01",
            "the castle were arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "Lieutenant Schwarz must've\x01",
            "really pissed SOMEBODY off!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4394")

    Jump("loc_45F1")

    label("loc_4397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4467")

    ChrTalk(    #152
        0xFE,
        (
            "What am I to do with this sudden vacation?\x01",
            "I have to admit, the usual euphoric vacation\x01",
            "feelings are TOTALLY lacking right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I'm really worried about what's\x01",
            "going on inside the castle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F1")

    label("loc_4467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4528")

    ChrTalk(    #154
        0xFE,
        (
            "Colonel Richard has been seen\x01",
            "going in and out of the castle\x01",
            "quite a lot as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "Her Majesty's probably been running\x01",
            "him ragged, if she's as sick as the\x01",
            "rumors suggest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F1")

    label("loc_4528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_45F1")

    ChrTalk(    #156
        0xFE,
        (
            "I work in the castle, but the\x01",
            "duke suddenly ordered me to take\x01",
            "some time off. Forced vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "It doesn't make much sense to\x01",
            "me that the government takes\x01",
            "off while the queen is ill...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45F1")

    TalkEnd(0xFE)
    Return()

    # Function_24_3731 end

    def Function_25_45F5(): pass

    label("Function_25_45F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4628")

    ChrTalk(    #158
        0xFE,
        "Ha, Ha, Ha! Roll call, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4689")

    label("loc_4628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4632")
    Jump("loc_4689")

    label("loc_4632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_463C")
    Jump("loc_4689")

    label("loc_463C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4646")
    Jump("loc_4689")

    label("loc_4646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4650")
    Jump("loc_4689")

    label("loc_4650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_465A")
    Jump("loc_4689")

    label("loc_465A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4664")
    Jump("loc_4689")

    label("loc_4664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_466E")
    Jump("loc_4689")

    label("loc_466E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4678")
    Jump("loc_4689")

    label("loc_4678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4682")
    Jump("loc_4689")

    label("loc_4682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4689")

    label("loc_4689")

    TalkEnd(0xFE)
    Return()

    # Function_25_45F5 end

    def Function_26_468D(): pass

    label("Function_26_468D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_46CE")

    ChrTalk(    #159
        0xFE,
        "My husband...has a lot of energy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "Geez...\x02",
    )

    CloseMessageWindow()
    Jump("loc_472F")

    label("loc_46CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_46D8")
    Jump("loc_472F")

    label("loc_46D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_46E2")
    Jump("loc_472F")

    label("loc_46E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_46EC")
    Jump("loc_472F")

    label("loc_46EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_46F6")
    Jump("loc_472F")

    label("loc_46F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4700")
    Jump("loc_472F")

    label("loc_4700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_470A")
    Jump("loc_472F")

    label("loc_470A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4714")
    Jump("loc_472F")

    label("loc_4714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_471E")
    Jump("loc_472F")

    label("loc_471E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4728")
    Jump("loc_472F")

    label("loc_4728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_472F")

    label("loc_472F")

    TalkEnd(0xFE)
    Return()

    # Function_26_468D end

    def Function_27_4733(): pass

    label("Function_27_4733")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_47AF")

    ChrTalk(    #161
        0xFE,
        (
            "How many times are you going to take\x01",
            "roll call, Dad? How many times will\x01",
            "it take until you're satisfied?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4810")

    label("loc_47AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_47B9")
    Jump("loc_4810")

    label("loc_47B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_47C3")
    Jump("loc_4810")

    label("loc_47C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_47CD")
    Jump("loc_4810")

    label("loc_47CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_47D7")
    Jump("loc_4810")

    label("loc_47D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_47E1")
    Jump("loc_4810")

    label("loc_47E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_47EB")
    Jump("loc_4810")

    label("loc_47EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_47F5")
    Jump("loc_4810")

    label("loc_47F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_47FF")
    Jump("loc_4810")

    label("loc_47FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4809")
    Jump("loc_4810")

    label("loc_4809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4810")

    label("loc_4810")

    TalkEnd(0xFE)
    Return()

    # Function_27_4733 end

    def Function_28_4814(): pass

    label("Function_28_4814")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_4852")

    ChrTalk(    #162
        0xFE,
        (
            "I'd love to see the inside of\x01",
            "the castle...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48D6")

    label("loc_4852")

    OP_A2(0x12)

    ChrTalk(    #163
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "This is Grancel Castle, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "...Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "Where were we going to meet, again?\x01",
            "I've completely forgotten!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D6")

    TalkEnd(0xFE)
    Return()

    # Function_28_4814 end

    def Function_29_48DA(): pass

    label("Function_29_48DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4A17")

    ChrTalk(    #167
        0xFE,
        (
            "I was going to propose here when suddenly,\x01",
            "the castle gates opened and all these Royal\x01",
            "Guardsmen and bracers came running through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "I thought they'd come to...stop\x01",
            "me from proposing, or something!\x01",
            "Yeah, it's silly, I know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "I lost my nerve, though, and STILL\x01",
            "haven't said anything to her...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B39")

    label("loc_4A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4A69")

    ChrTalk(    #170
        0xFE,
        "Ellie... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "I've got something very important\x01",
            "to ask you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B39")

    label("loc_4A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4AEC")

    ChrTalk(    #172
        0xFE,
        "I looked all over town...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "...and the best place to pop the\x01",
            "question is right in front of the\x01",
            "gates, I think...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B39")

    label("loc_4AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4AF6")
    Jump("loc_4B39")

    label("loc_4AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4B00")
    Jump("loc_4B39")

    label("loc_4B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4B0A")
    Jump("loc_4B39")

    label("loc_4B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4B14")
    Jump("loc_4B39")

    label("loc_4B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4B1E")
    Jump("loc_4B39")

    label("loc_4B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4B28")
    Jump("loc_4B39")

    label("loc_4B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4B32")
    Jump("loc_4B39")

    label("loc_4B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4B39")

    label("loc_4B39")

    TalkEnd(0xFE)
    Return()

    # Function_29_48DA end

    def Function_30_4B3D(): pass

    label("Function_30_4B3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4C76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C06")

    ChrTalk(    #174
        0xFE,
        (
            "I can't believe something like\x01",
            "that happened while I was standing\x01",
            "RIGHT THERE...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "But I mustn't let myself get so\x01",
            "easily bothered. The climax of\x01",
            "our trip is still to come!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C73")

    label("loc_4C06")

    OP_A2(0x1)

    ChrTalk(    #176
        0xFE,
        (
            "The queen and princess were both\x01",
            "so beautiful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "That big commotion was sure a\x01",
            "shocker, though!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C73")

    Jump("loc_4EC3")

    label("loc_4C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4D04")

    ChrTalk(    #178
        0xFE,
        (
            "Oh, Armand... I think it's time.\x01",
            "Our time...is now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "...What'll I do...if he hears\x01",
            "my heart racing? Should I even\x01",
            "care...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC3")

    label("loc_4D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4DAA")

    ChrTalk(    #180
        0xFE,
        (
            "Armand's been thinking about\x01",
            "something all day, but he\x01",
            "won't tell me what it is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "He can be such a meanie! Time to\x01",
            "bust out the pouty face!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E73")

    label("loc_4DAA")

    OP_A2(0x1)

    ChrTalk(    #182
        0xFE,
        (
            "Armand's been talking to himself\x01",
            "all day today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "I know he's got something on\x01",
            "his mind, but he just won't tell\x01",
            "me what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "He can be such a meanie! Time to\x01",
            "bust out the pouty face!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E73")

    Jump("loc_4EC3")

    label("loc_4E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4E80")
    Jump("loc_4EC3")

    label("loc_4E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4E8A")
    Jump("loc_4EC3")

    label("loc_4E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4E94")
    Jump("loc_4EC3")

    label("loc_4E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4E9E")
    Jump("loc_4EC3")

    label("loc_4E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EA8")
    Jump("loc_4EC3")

    label("loc_4EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4EB2")
    Jump("loc_4EC3")

    label("loc_4EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4EBC")
    Jump("loc_4EC3")

    label("loc_4EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4EC3")

    label("loc_4EC3")

    TalkEnd(0xFE)
    Return()

    # Function_30_4B3D end

    def Function_31_4EC7(): pass

    label("Function_31_4EC7")

    TalkBegin(0xFE)

    ChrTalk(    #185
        0xFE,
        (
            "I put my wallet in my belt so\x01",
            "it wouldn't get stolen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "But...now I can't find it!\x01",
            "Where'd it go?!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_4EC7 end

    def Function_32_4F3B(): pass

    label("Function_32_4F3B")

    TalkBegin(0xFE)

    ChrTalk(    #187
        0xFE,
        "Daddy, I want a drink!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_4F3B end

    def Function_33_4F5E(): pass

    label("Function_33_4F5E")

    TalkBegin(0xFE)

    ChrTalk(    #188
        0xFE,
        "Yeah, it was right at that corner...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I saw a girl who looked juuust\x01",
            "like Princess Klaudia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "I wonder if it really WAS her...?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_4F5E end

    def Function_34_4FF1(): pass

    label("Function_34_4FF1")

    TalkBegin(0xFE)

    ChrTalk(    #191
        0xFE,
        "Oh, come now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "The princess was only just standing\x01",
            "on the castle terrace!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "How could she have changed clothes\x01",
            "and gotten all the way here in such\x01",
            "a short time?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_4FF1 end

    def Function_35_50A5(): pass

    label("Function_35_50A5")

    TalkBegin(0xFE)

    ChrTalk(    #194
        0xFE,
        (
            "Good point. I withdraw my\x01",
            "observation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "Still, you don't see too many\x01",
            "students in their uniforms\x01",
            "away from the school...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_50A5 end

    def Function_36_512E(): pass

    label("Function_36_512E")

    TalkBegin(0xFE)

    ChrTalk(    #196
        0xFE,
        (
            "Such beautiful buildings! They\x01",
            "all have such architectural and\x01",
            "historical flair to them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "And yet, there's a certain humble simplicity\x01",
            "to them, as well. Quite a contrast to the\x01",
            "architecture prominent in the Republic!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_512E end

    def Function_37_5217(): pass

    label("Function_37_5217")

    TalkBegin(0xFE)

    ChrTalk(    #198
        0xFE,
        "Awwww...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "This is why I hate going places\x01",
            "with you, Daddy!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_5217 end

    def Function_38_5263(): pass

    label("Function_38_5263")

    TalkBegin(0xFE)

    ChrTalk(    #200
        0xFE,
        "Here we go! Say 'fuzzy pickles'!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "We don't have to stay here. A\x01",
            "picture and trip to the toilet\x01",
            "is memory enough. Free, too!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_5263 end

    def Function_39_52EF(): pass

    label("Function_39_52EF")

    TalkBegin(0xFE)

    ChrTalk(    #202
        0xFE,
        (
            "This is our daughter's present\x01",
            "to us for our anniversary.\x01",
            "A trip to the Royal Capital!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "And during the Birthday Celebration,\x01",
            "no less! Best present EVER!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "I've always wanted to visit the\x01",
            "capital at least once before I\x01",
            "bite the big one...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_52EF end

    def Function_40_53F0(): pass

    label("Function_40_53F0")

    TalkBegin(0xFE)

    ChrTalk(    #205
        0xFE,
        "Are...are we really staying HERE?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "It's quite an impressive building!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_53F0 end

    def Function_41_5446(): pass

    label("Function_41_5446")

    TalkBegin(0xFE)

    ChrTalk(    #207
        0xFE,
        (
            "Since I've come all this way,\x01",
            "I might as well take a tour,\x01",
            "no?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_5446 end

    def Function_42_5491(): pass

    label("Function_42_5491")

    TalkBegin(0xFE)

    ChrTalk(    #208
        0xFE,
        "So...where am I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Without a map, I'm hopelessly\x01",
            "lost. Always. Even back home!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_5491 end

    def Function_43_54EF(): pass

    label("Function_43_54EF")

    EventBegin(0x0)
    OP_6D(2190, 0, 46270, 0)
    OP_67(0, 29260, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(432, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    StopSound(0x9C40, 0x3D090, 0x0)
    FadeToBright(2000, 0)

    def lambda_5553():
        OP_6C(90000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5553)
    Sleep(1000)

    def lambda_5568():
        OP_6D(10350, 3620, 43920, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5568)

    def lambda_5580():
        OP_67(0, 3740, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5580)
    StopSound(0x9C40, 0x249F0, 0x2710)
    Sleep(10000)
    ClearMapFlags(0x100000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_54EF end

    def Function_44_55B6(): pass

    label("Function_44_55B6")

    Return()

    # Function_44_55B6 end

    def Function_45_55B7(): pass

    label("Function_45_55B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5613")
    OP_8E(0xFE, 0xED8, 0x0, 0x9E3E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF466, 0x0, 0x9E3E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF466, 0x0, 0x10018, 0xBB8, 0x0)
    OP_8E(0xFE, 0xED8, 0x0, 0x100F4, 0xBB8, 0x0)
    Jump("Function_45_55B7")

    label("loc_5613")

    Return()

    # Function_45_55B7 end

    def Function_46_5614(): pass

    label("Function_46_5614")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5852")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5647")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5764")

    label("loc_5647")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_566D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5764")

    label("loc_566D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5693")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5764")

    label("loc_5693")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56BA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5764")

    label("loc_56BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56E0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5764")

    label("loc_56E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5706")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5764")

    label("loc_5706")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_572B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5764")

    label("loc_572B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5750")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5764")

    label("loc_5750")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5764")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_584F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    OP_69(0xFE, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5840")

    ChrTalk(    #210
        0xFE,
        "Hey, you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#000F(Crap!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x102,
        "#010F(They found us...)\x02",
    )

    CloseMessageWindow()

    label("loc_5840")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_584F")

    Jump("Function_46_5614")

    label("loc_5852")

    Return()

    # Function_46_5614 end

    def Function_47_5853(): pass

    label("Function_47_5853")

    EventBegin(0x0)
    OP_6D(17700, 510, 43970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    OP_6C(90000, 0)
    SetChrPos(0x101, 17540, 510, 44210, 270)
    SetChrPos(0x102, 17540, 510, 43360, 270)

    ChrTalk(    #213
        0x101,
        "#000FWha...!\x02",
    )

    CloseMessageWindow()

    def lambda_58CC():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58CC)
    OP_6D(4010, 0, 38720, 3000)
    SetChrPos(0x101, 13280, 250, 49870, 225)
    SetChrPos(0x102, 14070, 250, 49980, 225)
    Sleep(1000)
    OP_6D(13610, 250, 50130, 3000)

    ChrTalk(    #214
        0x102,
        (
            "#010F(They're already looking for us.)\x02\x03",

            "(We need to get to the cathedral\x01",
            "without anyone spotting us.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        "#000F(Right.)\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_47_5853 end

    def Function_48_59A0(): pass

    label("Function_48_59A0")

    SetPlaceName(0xB4)
    Return()

    # Function_48_59A0 end

    SaveToFile()

Try(main)
