from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2513   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2513.x',
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
        'Jill',                                 # 9
        'Hans',                                 # 10
        'Mr. Ratio',                            # 11
        'Ms. Wiola',                            # 12
        'Ms. Millia',                           # 13
        'Mr. Effort',                           # 14
        'Rhody',                                # 15
        'Mickey',                               # 16
        'Kaden',                                # 17
        'Alice',                                # 18
        'Purity',                               # 19
        'Taylor',                               # 20
        'Logic',                                # 21
        'Argyle',                               # 22
        'Roy',                                  # 23
        'Monika',                               # 24
        'Thelma',                               # 25
        'Richelle',                             # 26
        'Patrick',                              # 27
        'Gerome',                               # 28
        'Dennis',                               # 29
        'Nikita',                               # 30
        'Felicity',                             # 31
        'Reina',                                # 32
        'Janitor Parkes',                       # 33
        'Maid Rainey',                          # 34
        'Maid Laurel',                          # 35
        'Duke Radmont',                         # 36
        'Chairman Claude',                      # 37
        'Archbishop',                           # 38
        'Assassin',                             # 39
        'Polly',                                # 40
        'Matron Theresa',                       # 41
        'Daniel',                               # 42
        'Mary',                                 # 43
        'Clem',                                 # 44
        'Dean Collins',                         # 45
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH01660 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH01430 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01080 ._CH',             # 07
        'ED6_DT07/CH01580 ._CH',             # 08
        'ED6_DT07/CH01590 ._CH',             # 09
        'ED6_DT07/CH01090 ._CH',             # 0A
        'ED6_DT07/CH01370 ._CH',             # 0B
        'ED6_DT07/CH01080 ._CH',             # 0C
        'ED6_DT07/CH01020 ._CH',             # 0D
        'ED6_DT07/CH02260 ._CH',             # 0E
        'ED6_DT07/CH02270 ._CH',             # 0F
        'ED6_DT07/CH02280 ._CH',             # 10
        'ED6_DT07/CH01350 ._CH',             # 11
        'ED6_DT07/CH02540 ._CH',             # 12
        'ED6_DT07/CH01220 ._CH',             # 13
        'ED6_DT07/CH01570 ._CH',             # 14
        'ED6_DT07/CH01670 ._CH',             # 15
        'ED6_DT07/CH01040 ._CH',             # 16
        'ED6_DT06/CH20069 ._CH',             # 17
        'ED6_DT06/CH20071 ._CH',             # 18
        'ED6_DT07/CH01083 ._CH',             # 19
        'ED6_DT07/CH02590 ._CH',             # 1A
        'ED6_DT07/CH02640 ._CH',             # 1B
        'ED6_DT07/CH02630 ._CH',             # 1C
        'ED6_DT07/CH02570 ._CH',             # 1D
        'ED6_DT07/CH02600 ._CH',             # 1E
        'ED6_DT07/CH02500 ._CH',             # 1F
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH01660P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH01430P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01080P._CP',             # 07
        'ED6_DT07/CH01580P._CP',             # 08
        'ED6_DT07/CH01590P._CP',             # 09
        'ED6_DT07/CH01090P._CP',             # 0A
        'ED6_DT07/CH01370P._CP',             # 0B
        'ED6_DT07/CH01080P._CP',             # 0C
        'ED6_DT07/CH01020P._CP',             # 0D
        'ED6_DT07/CH02260P._CP',             # 0E
        'ED6_DT07/CH02270P._CP',             # 0F
        'ED6_DT07/CH02280P._CP',             # 10
        'ED6_DT07/CH01350P._CP',             # 11
        'ED6_DT07/CH02540P._CP',             # 12
        'ED6_DT07/CH01220P._CP',             # 13
        'ED6_DT07/CH01570P._CP',             # 14
        'ED6_DT07/CH01670P._CP',             # 15
        'ED6_DT07/CH01040P._CP',             # 16
        'ED6_DT06/CH20069P._CP',             # 17
        'ED6_DT06/CH20071P._CP',             # 18
        'ED6_DT07/CH01083P._CP',             # 19
        'ED6_DT07/CH02590P._CP',             # 1A
        'ED6_DT07/CH02640P._CP',             # 1B
        'ED6_DT07/CH02630P._CP',             # 1C
        'ED6_DT07/CH02570P._CP',             # 1D
        'ED6_DT07/CH02600P._CP',             # 1E
        'ED6_DT07/CH02500P._CP',             # 1F
    )

    DeclNpc(
        X                   = 59640,
        Z                   = 1000,
        Y                   = 13450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 66040,
        Z                   = 1000,
        Y                   = 16210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 9300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2160,
        Z                   = 0,
        Y                   = 8570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3320,
        Z                   = 0,
        Y                   = 8570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2100,
        Z                   = 0,
        Y                   = 9290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 3210,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 5200,
        Z                   = 250,
        Y                   = -4530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -4160,
        Z                   = 0,
        Y                   = 5180,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -5390,
        Z                   = 0,
        Y                   = 3910,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -3890,
        Z                   = 0,
        Y                   = 1240,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -5880,
        Z                   = 0,
        Y                   = 1770,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -470,
        Z                   = 0,
        Y                   = 720,
        Direction           = 192,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -820,
        Z                   = 0,
        Y                   = -3270,
        Direction           = 1,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -3170,
        Z                   = 0,
        Y                   = -1120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 1130,
        Z                   = 0,
        Y                   = -2530,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 1380,
        Z                   = 0,
        Y                   = -300,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -2520,
        Z                   = 0,
        Y                   = -2890,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 3400,
        Z                   = 0,
        Y                   = 3800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 4400,
        Z                   = 0,
        Y                   = 200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 3100,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 6030,
        Z                   = 0,
        Y                   = 2120,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 6230,
        Z                   = 0,
        Y                   = 5420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 6240,
        Z                   = 0,
        Y                   = 3780,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -510,
        Z                   = 0,
        Y                   = 4270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 61850,
        Z                   = 1000,
        Y                   = 17310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63320,
        Z                   = 1000,
        Y                   = 15250,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 57740,
        Z                   = 1000,
        Y                   = 16980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58590,
        Z                   = 1000,
        Y                   = 17010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 59600,
        Z                   = 1000,
        Y                   = 16379,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56830,
        Z                   = 1000,
        Y                   = 16500,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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


    ScpFunction(
        "Function_0_64A",          # 00, 0
        "Function_1_8CA",          # 01, 1
        "Function_2_8F5",          # 02, 2
        "Function_3_A7D",          # 03, 3
        "Function_4_B1E",          # 04, 4
        "Function_5_C25",          # 05, 5
        "Function_6_C7E",          # 06, 6
        "Function_7_D19",          # 07, 7
        "Function_8_DA4",          # 08, 8
        "Function_9_E22",          # 09, 9
        "Function_10_E9D",         # 0A, 10
        "Function_11_ECA",         # 0B, 11
        "Function_12_F55",         # 0C, 12
        "Function_13_FC2",         # 0D, 13
        "Function_14_102D",        # 0E, 14
        "Function_15_1087",        # 0F, 15
        "Function_16_1121",        # 10, 16
        "Function_17_123D",        # 11, 17
        "Function_18_12C5",        # 12, 18
        "Function_19_131B",        # 13, 19
        "Function_20_1385",        # 14, 20
        "Function_21_13D0",        # 15, 21
        "Function_22_144D",        # 16, 22
        "Function_23_1488",        # 17, 23
        "Function_24_1672",        # 18, 24
        "Function_25_17EF",        # 19, 25
        "Function_26_18E7",        # 1A, 26
        "Function_27_1992",        # 1B, 27
        "Function_28_1A30",        # 1C, 28
        "Function_29_2357",        # 1D, 29
        "Function_30_430D",        # 1E, 30
        "Function_31_6264",        # 1F, 31
        "Function_32_62BC",        # 20, 32
        "Function_33_6323",        # 21, 33
        "Function_34_638F",        # 22, 34
        "Function_35_63FB",        # 23, 35
        "Function_36_6467",        # 24, 36
        "Function_37_6488",        # 25, 37
    )


    def Function_0_64A(): pass

    label("Function_0_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_654")
    Jump("loc_884")

    label("loc_654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_832")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
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
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 590, 0, 4100, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -820, 0, 4100, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82F")
    OP_51(0x8, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x9, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xA, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xB, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xC, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xD, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xE, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0xF, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x10, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x14, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x15, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x16, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x17, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x18, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x19, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_51(0x20, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82F")

    Jump("loc_884")

    label("loc_832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_83C")
    Jump("loc_884")

    label("loc_83C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_846")
    Jump("loc_884")

    label("loc_846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_850")
    Jump("loc_884")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_85F")
    ClearChrFlags(0x20, 0x80)
    Jump("loc_884")

    label("loc_85F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_869")
    Jump("loc_884")

    label("loc_869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_873")
    Jump("loc_884")

    label("loc_873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_87D")
    Jump("loc_884")

    label("loc_87D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_884")

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_89B")
    OP_A3(0x3FA)
    Event(0, 28)
    OP_B1("t2513_n")

    label("loc_89B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_8B2")
    OP_A3(0x3FB)
    Event(0, 29)
    OP_B1("t2513_n")

    label("loc_8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_8C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 30)

    label("loc_8C9")

    Return()

    # Function_0_64A end

    def Function_1_8CA(): pass

    label("Function_1_8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EB")
    OP_B1("t2513_y")
    Jump("loc_8F4")

    label("loc_8EB")

    OP_B1("t2513_n")

    label("loc_8F4")

    Return()

    # Function_1_8CA end

    def Function_2_8F5(): pass

    label("Function_2_8F5")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_A67")

    label("loc_925")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93E")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_A67")

    label("loc_93E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_957")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_A67")

    label("loc_957")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_970")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_A67")

    label("loc_970")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_989")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_A67")

    label("loc_989")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A2")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_A67")

    label("loc_9A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BB")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_A67")

    label("loc_9BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D4")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_A67")

    label("loc_9D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ED")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_A67")

    label("loc_9ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A06")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_A67")

    label("loc_A06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_A67")

    label("loc_A1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A38")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_A67")

    label("loc_A38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A51")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_A67")

    label("loc_A51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A67")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_A67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7C")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_A67")

    label("loc_A7C")

    Return()

    # Function_2_8F5 end

    def Function_3_A7D(): pass

    label("Function_3_A7D")

    TalkBegin(0xA)

    ChrTalk(    #0
        0xFE,
        (
            "A lot of the teachers and students\x01",
            "are really grateful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "This year's festival was truly\x01",
            "something that the royal\x01",
            "academy can boast about.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_3_A7D end

    def Function_4_B1E(): pass

    label("Function_4_B1E")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD8")
    OP_A2(0x1)

    ChrTalk(    #2
        0xFE,
        "Ha ha...thank you...all of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I'd love to kick back with a good, stiff\x01",
            "drink. Aidios knows I need it after seeing\x01",
            "Mr. Effort try on that princess costume...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C21")

    label("loc_BD8")


    ChrTalk(    #4
        0xFE,
        (
            "When we're done here, I think I\x01",
            "might hit the town with Ms. Millia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C21")

    TalkEnd(0xB)
    Return()

    # Function_4_B1E end

    def Function_5_C25(): pass

    label("Function_5_C25")

    TalkBegin(0xC)

    ChrTalk(    #5
        0xFE,
        "My, but you did a fantastic job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Good enough for me to give\x01",
            "you an 'A'.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_5_C25 end

    def Function_6_C7E(): pass

    label("Function_6_C7E")

    TalkBegin(0xD)

    ChrTalk(    #7
        0xFE,
        (
            "I'm just glad that everything\x01",
            "concluded without incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Tomorrow, the kids are going to\x01",
            "have to work harder than ever at\x01",
            "their lessons.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_6_C7E end

    def Function_7_D19(): pass

    label("Function_7_D19")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6E")
    OP_A2(0x4)

    ChrTalk(    #9
        0xFE,
        "And that's a launch, folks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Time to party like it's 1499!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DA0")

    label("loc_D6E")


    ChrTalk(    #11
        0xFE,
        "Classes start up again tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    label("loc_DA0")

    TalkEnd(0xE)
    Return()

    # Function_7_D19 end

    def Function_8_DA4(): pass

    label("Function_8_DA4")

    TalkBegin(0xF)

    ChrTalk(    #13
        0xFE,
        "The festival's over, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "So, why's everyone making\x01",
            "so much noise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "I just want to go home, already...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_8_DA4 end

    def Function_9_E22(): pass

    label("Function_9_E22")

    TalkBegin(0x10)

    ChrTalk(    #16
        0xFE,
        (
            "I feel like we've really accomplished\x01",
            "something today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I had the most fun while we\x01",
            "were still setting up.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_9_E22 end

    def Function_10_E9D(): pass

    label("Function_10_E9D")

    TalkBegin(0x11)

    ChrTalk(    #18
        0xFE,
        "Hee hee...I love launch parties!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Return()

    # Function_10_E9D end

    def Function_11_ECA(): pass

    label("Function_11_ECA")

    TalkBegin(0x12)

    ChrTalk(    #19
        0xFE,
        (
            "We really didn't have much time,\x01",
            "but we just barely squeaked by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "All the guests seemed to enjoy\x01",
            "it, though, so I had fun.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_11_ECA end

    def Function_12_F55(): pass

    label("Function_12_F55")

    TalkBegin(0x13)

    ChrTalk(    #21
        0xFE,
        (
            "I've been SO busy lately, but I've\x01",
            "managed to pull it all off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "I feel pretty good about it.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_12_F55 end

    def Function_13_FC2(): pass

    label("Function_13_FC2")

    TalkBegin(0x14)

    ChrTalk(    #23
        0xFE,
        (
            "I look forward to going back\x01",
            "home to Ruan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "...but days like today make\x01",
            "the wait easier.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_13_FC2 end

    def Function_14_102D(): pass

    label("Function_14_102D")

    TalkBegin(0x15)

    ChrTalk(    #25
        0xFE,
        (
            "Everything turned out okay...darn.\x01",
            "I was really hoping for a tragic\x01",
            "ending...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Return()

    # Function_14_102D end

    def Function_15_1087(): pass

    label("Function_15_1087")

    TalkBegin(0x16)

    ChrTalk(    #26
        0xFE,
        (
            "The ice cream shop was super popular.\x01",
            "I had no idea people would love the\x01",
            "Pom-shaped scoops so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "I'm glad those little kids had fun.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_15_1087 end

    def Function_16_1121(): pass

    label("Function_16_1121")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121F")
    OP_A2(0xD)

    ChrTalk(    #28
        0xFE,
        "Ahh, that was the best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I think the festival is enjoyable because\x01",
            "it only happens once a year and everyone\x01",
            "puts so much work into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "If we tried to keep up that pace\x01",
            "throughout the year, we'd all\x01",
            "get seriously burnt out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1239")

    label("loc_121F")


    ChrTalk(    #31
        0xFE,
        "Ahh, that was great!\x02",
    )

    CloseMessageWindow()

    label("loc_1239")

    TalkEnd(0x17)
    Return()

    # Function_16_1121 end

    def Function_17_123D(): pass

    label("Function_17_123D")

    TalkBegin(0x18)

    ChrTalk(    #32
        0xFE,
        (
            "Ha ha...there's nothing quite like\x01",
            "participating in a big event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "The important thing is to be\x01",
            "there for everyone else.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_17_123D end

    def Function_18_12C5(): pass

    label("Function_18_12C5")

    TalkBegin(0x19)

    ChrTalk(    #34
        0xFE,
        "Oh, hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "The play and the ice cream shop\x01",
            "were big hits. I'm so happy!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_18_12C5 end

    def Function_19_131B(): pass

    label("Function_19_131B")

    TalkBegin(0x1A)

    ChrTalk(    #36
        0xFE,
        "Ha ha...and that makes me happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "The play was great. Thanks to all\x01",
            "of you for your help.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_19_131B end

    def Function_20_1385(): pass

    label("Function_20_1385")

    TalkBegin(0x1B)

    ChrTalk(    #38
        0xFE,
        "*sigh* Man, I'm beat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "I can't wait to get home and sleep.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1B)
    Return()

    # Function_20_1385 end

    def Function_21_13D0(): pass

    label("Function_21_13D0")

    TalkBegin(0x1C)

    ChrTalk(    #40
        0xFE,
        (
            "I wonder if it's okay to take a\x01",
            "break from studying for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "It just has a tendency to pile\x01",
            "up on me...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1C)
    Return()

    # Function_21_13D0 end

    def Function_22_144D(): pass

    label("Function_22_144D")

    TalkBegin(0x1D)

    ChrTalk(    #42
        0xFE,
        "I swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Gerome is goofing off again...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1D)
    Return()

    # Function_22_144D end

    def Function_23_1488(): pass

    label("Function_23_1488")

    TalkBegin(0x1E)
    OP_4A(0x1F, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D2")
    OP_A2(0x14)
    OP_A2(0x15)

    ChrTalk(    #44
        0x1E,
        (
            "It's because of you that I practically\x01",
            "worked myself to death!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x1E,
        (
            "I should send you off to the old\x01",
            "man, or someone equally scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x1F,
        (
            "Ha ha...I'm honored by your\x01",
            "kind words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x1F,
        (
            "You know I only pushed you because I knew\x01",
            "you could handle it, right? And that it\x01",
            "would make you a better person!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    Jump("loc_166A")

    label("loc_15D2")


    ChrTalk(    #48
        0x1E,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x1F,
        (
            "What's with the sigh? If you need\x01",
            "someone to talk to, you know I'm\x01",
            "here for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #50
        0x1E,
        "Someone, shoot me...\x02",
    )

    CloseMessageWindow()

    label("loc_166A")

    OP_4B(0x1F, 255)
    TalkEnd(0x1E)
    Return()

    # Function_23_1488 end

    def Function_24_1672(): pass

    label("Function_24_1672")

    TalkBegin(0x1F)
    OP_4A(0x1E, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BC")
    OP_A2(0x14)
    OP_A2(0x15)

    ChrTalk(    #51
        0x1E,
        (
            "It's because of you that I practically\x01",
            "worked myself to death!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x1E,
        (
            "I should send you off to the old man,\x01",
            "or someone equally scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x1F,
        (
            "Ha ha...I'm honored by your\x01",
            "kind words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x1F,
        (
            "You know I only pushed you because I knew\x01",
            "you could handle it, right? And that it\x01",
            "would make you a better person!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    Jump("loc_17E7")

    label("loc_17BC")


    ChrTalk(    #55
        0xFE,
        (
            "Ha ha ha...\x01",
            "(I love torturing her...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E7")

    OP_4B(0x1E, 255)
    TalkEnd(0x1F)
    Return()

    # Function_24_1672 end

    def Function_25_17EF(): pass

    label("Function_25_17EF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1886")
    OP_A2(0x16)

    ChrTalk(    #56
        0xFE,
        (
            "#640FOh...I didn't know you were\x01",
            "still here.\x02\x03",

            "Don't you have to go back\x01",
            "to Ruan?\x02\x03",

            "You're more than welcome to\x01",
            "join in, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E3")

    label("loc_1886")


    ChrTalk(    #57
        0xFE,
        (
            "#640FDon't you have to go back\x01",
            "to Ruan?\x02\x03",

            "You're more than welcome to\x01",
            "join in, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E3")

    TalkEnd(0x8)
    Return()

    # Function_25_17EF end

    def Function_26_18E7(): pass

    label("Function_26_18E7")

    TalkBegin(0x9)

    ChrTalk(    #58
        0xFE,
        (
            "#730FOh...are you planning to participate\x01",
            "in the launch?\x02\x03",

            "The teachers are paying for all\x01",
            "of it, so you might as well pinch\x01",
            "'em for what they're worth! Heh...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_26_18E7 end

    def Function_27_1992(): pass

    label("Function_27_1992")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1A2C")

    ChrTalk(    #59
        0xFE,
        (
            "My job is taking care of the\x01",
            "academy's equipment and\x01",
            "facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "It's especially important now,\x01",
            "before the campus festival\x01",
            "starts up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2C")

    TalkEnd(0x20)
    Return()

    # Function_27_1992 end

    def Function_28_1A30(): pass

    label("Function_28_1A30")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_6D(-410, 4000, -4600, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(3720, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 850, 1000, 14010, 270)
    SetChrPos(0x105, -960, 1000, 14000, 90)
    SetChrPos(0x8, -80, 1000, 13250, 0)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x105, 15)
    SetChrChipByIndex(0x102, 16)
    FadeToBright(1000, 0)
    SetPlaceName(0x5F)
    OP_6D(910, 2000, 12490, 4000)
    Fade(500)
    OP_6D(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x101, 61000, 1000, 14250, 225)
    SetChrPos(0x105, 59080, 1000, 14210, 135)
    SetChrPos(0x8, 60000, 1000, 13140, 45)
    SetChrPos(0x102, 67180, 1000, 16860, 270)
    SetChrPos(0x9, 67180, 1000, 16860, 270)
    OP_0D()

    ChrTalk(    #61
        0x101,
        (
            "#340F#2PSo...these are our costumes?\x02\x03",

            "I figured that if we're playing\x01",
            "knights, we'd be all armored up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#644F#5PWell, armor and a helmet won't\x01",
            "work so well if we want people\x01",
            "to see you ACT.\x02\x03",

            "That's why I decided to arrange\x01",
            "things so you'd be dressed more\x01",
            "like the Royal Guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#340F#2POhhh, I got it.\x02\x03",

            "#341FIt's perfect for Kloe.\x01",
            "She's petite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x105,
        (
            "#351F#1PHa ha. Thank you so much.\x02\x03",

            "I think it suits you, also.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#348F#2PHa ha... Really?\x02\x03",

            "Say, why are we dressed\x01",
            "in different colors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x105,
        (
            "#350F#1PBecause I'm playing the\x01",
            "Azure Knight, Oscar.\x02\x03",

            "You're playing the Ruby\x01",
            "Knight, Julius.\x02\x03",

            "It makes the play more colorful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#340F#2PAhh, okay then...\x02\x03",

            "So what about Joshua...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#1PThe object of your affection\x01",
            "is the fair Princess Cecilia.\x02\x03",

            "Come on, Princess. This way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        (
            "#1PW-Wait...\x01",
            "I'm not in the moment yet!\x02",
        )
    )

    CloseMessageWindow()
    OP_66(0x0)

    def lambda_1ECC():
        OP_6D(61500, 2310, 14620, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1ECC)

    def lambda_1EE4():
        OP_6B(850, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1EE4)

    def lambda_1EF4():

        label("loc_1EF4")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1EF4")

    QueueWorkItem2(0x101, 1, lambda_1EF4)

    def lambda_1F05():

        label("loc_1F05")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1F05")

    QueueWorkItem2(0x105, 1, lambda_1F05)

    def lambda_1F16():

        label("loc_1F16")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1F16")

    QueueWorkItem2(0x8, 1, lambda_1F16)

    def lambda_1F27():

        label("loc_1F27")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1F27")

    QueueWorkItem2(0x9, 1, lambda_1F27)

    def lambda_1F38():
        OP_8F(0xFE, 0xF582, 0x3E8, 0x3B10, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1F38)
    Sleep(800)

    def lambda_1F58():
        OP_8F(0xFE, 0xF71C, 0x3E8, 0x3DFE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F58)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 0)
    WaitChrThread(0x9, 0x2)
    Sleep(200)
    OP_8F(0x9, 0xF85C, 0x3E8, 0x378C, 0x7D0, 0x0)
    OP_44(0x9, 0xFF)
    OP_8C(0x9, 315, 0)

    ChrTalk(    #70
        0x102,
        "#363F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#344F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x105,
        "#354F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "#643F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#367F#2PIf you're going to say\x01",
            "something, say it...\x02\x03",

            "Don't leave me in suspense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#340FWell, how should I put it...?\x02\x03",

            "#341FI think it looks perfect. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x105,
        (
            "#351FI'm shocked.\x02\x03",

            "#358FYou look beautiful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "#731FIndeed. Such poise.\x02\x03",

            "Why, if I didn't know what's really\x01",
            "going on under there, I'd be smitten\x01",
            "at the very sight of you. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #78
        0x102,
        (
            "#368F#2PWell, thank you for being so\x01",
            "honest about it, at least.\x01",
            "I'M not so thrilled, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#659FHeh heh...\x01",
            "This is just as I'd hoped...\x02\x03",

            "I think everyone will be pretty\x01",
            "pleased with the casting.\x02\x03",

            "#641FCome on, everyone! Let's make\x01",
            "this play one to remember!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#341F#6P#1KYeeeeaahh!\x02",
    )


    ChrTalk(    #81
        0x105,
        "#351F#1P#1KAll right!\x02",
    )


    ChrTalk(    #82
        0x9,
        "#731F#2P#1KMmm-hmmm...\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(    #83
        0x102,
        "#367F#2PBoo hoo... *sniffle*\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)

    AnonymousTalk(    #84
        "\x07\x05Afterward, Estelle and Joshua each slept in their respective dormitories.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_66(0x1)
    OP_28(0x3D, 0x1, 0x80)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2512   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_28_1A30 end

    def Function_29_2357(): pass

    label("Function_29_2357")

    EventBegin(0x0)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_6D(60480, 1000, 9080, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(19000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x101, 60900, 1000, 12690, 270)
    SetChrPos(0x105, 59100, 1000, 12780, 90)
    SetChrPos(0x102, 63020, 1000, 16920, 225)
    SetChrPos(0x8, 58340, 1000, 14950, 0)
    SetChrPos(0x9, 61530, 1000, 15270, 45)
    OP_43(0x102, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x102, 16)
    SetChrChipByIndex(0x101, 23)
    SetChrChipByIndex(0x105, 24)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    FadeToBright(1000, 0)

    def lambda_244B():
        OP_6D(60970, 1000, 14570, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_244B)

    def lambda_2463():
        OP_6C(30000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2463)
    OP_0D()
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x105, 0x1000)

    def lambda_2488():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2488)
    OP_99(0x101, 0x1, 0x2, 0x5DC)
    WaitChrThread(0x101, 0x1)

    def lambda_24B1():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24B1)
    WaitChrThread(0x105, 0x1)
    Sleep(150)

    def lambda_24D6():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24D6)
    OP_99(0x101, 0x1, 0x2, 0x5DC)
    WaitChrThread(0x101, 0x1)

    def lambda_24FF():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24FF)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0)

    def lambda_2529():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2529)
    OP_99(0x105, 0x1, 0x2, 0x5DC)
    WaitChrThread(0x105, 0x1)

    def lambda_2552():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2552)
    WaitChrThread(0x101, 0x1)
    Sleep(150)

    def lambda_2577():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2577)
    OP_99(0x105, 0x1, 0x2, 0x5DC)
    WaitChrThread(0x105, 0x1)

    def lambda_25A0():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25A0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    SetChrSubChip(0x105, 0)

    def lambda_25CA():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25CA)
    OP_99(0x101, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x101, 0x1)

    def lambda_25F3():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_25F3)
    WaitChrThread(0x105, 0x1)
    Sleep(120)

    def lambda_2618():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2618)
    OP_99(0x101, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x101, 0x1)

    def lambda_2641():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2641)
    WaitChrThread(0x105, 0x1)
    Sleep(120)

    def lambda_2666():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2666)
    OP_99(0x101, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x101, 0x1)

    def lambda_268F():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_268F)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0)
    FadeToDark(1500, 0, -1)

    def lambda_26C3():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_26C3)
    OP_99(0x105, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x105, 0x1)

    def lambda_26EC():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26EC)
    WaitChrThread(0x101, 0x1)
    Sleep(120)

    def lambda_2711():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2711)
    OP_99(0x105, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x105, 0x1)

    def lambda_273A():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_273A)
    WaitChrThread(0x101, 0x1)
    Sleep(120)

    def lambda_275F():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_275F)
    OP_99(0x105, 0x1, 0x2, 0x7D0)
    WaitChrThread(0x105, 0x1)

    def lambda_2788():
        OP_91(0xFE, 0x258, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2788)
    WaitChrThread(0x101, 0x1)
    OP_0D()

    AnonymousTalk(    #85
        "\x07\x05School was followed by rigorous rehearsals that lasted late into the night.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #86
        "\x07\x05Everyone was having such fun that time seemed to fly by.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2533   ._SN", 100, 0, 0)
    IdleLoop()
    OP_6D(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 610, 0, -360, 0)
    SetChrPos(0x102, -400, 0, 430, 0)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x105, 15)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    SetChrPos(0x101, 62000, 1000, 14000, 270)
    SetChrPos(0x105, 58000, 1000, 14000, 90)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_1D(0x61)
    OP_0D()
    Sleep(1000)

    NpcTalk(    #87
        0x101,
        "Ruby Knight Julius",
        (
            "#424F#2PMy friend...I fear that\x01",
            "this was inevitable.\x02\x03",

            "Perhaps fate always intended\x01",
            "for us to meet in so base a\x01",
            "fashion.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x16, 0x0, 0x64)
    SetChrChipByIndex(0x101, 23)
    SetChrSubChip(0x101, 5)
    OP_0D()
    Sleep(500)

    NpcTalk(    #88
        0x101,
        "Ruby Knight Julius",
        (
            "#421F#2PSpeak, that we may\x01",
            "both be unburdened!\x02\x03",

            "If nothing else, for\x01",
            "our beloved princess!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #89
        0x105,
        "Azure Knight Oscar",
        (
            "#359F#1PWe would cleave a path through\x01",
            "fate with our own hands...\x02\x03",

            "But at this moment, my words\x01",
            "and her smile seem lost...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #90
        0x101,
        "Ruby Knight Julius",
        (
            "#422F#2PHas fear clutched your heart,\x01",
            "Oscar?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #91
        0x105,
        "Azure Knight Oscar",
        (
            "#357F#1PBut what is this passion that\x01",
            "pierces me to the quick?\x02\x03",

            "Though I have no wish to fight\x01",
            "you again, it would seem that\x01",
            "I am left with little choice.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x16, 0x0, 0x64)
    SetChrChipByIndex(0x105, 24)
    SetChrSubChip(0x105, 8)
    OP_0D()
    Sleep(500)

    NpcTalk(    #92
        0x105,
        "Azure Knight Oscar",
        (
            "#352F#1PBefore this storm, by the\x01",
            "name of revolution, should\x01",
            "claim us both...\x02\x03",

            "Take up your sword, and\x01",
            "we shall let fate decide!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #93
        0x101,
        "Ruby Knight Julius",
        (
            "#420F#2PYes! And may the Goddess\x01",
            "above see our spirits as they\x01",
            "truly are!\x02\x03",

            "Come, then!\x01",
            "Let it be done!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #94
        0x105,
        "Azure Knight Oscar",
        "#356F#1PIndeed!\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x105)
    OP_21()

    ChrTalk(    #95
        0x101,
        "#347F#2PWhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x105,
        "#357F#1PWhew...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x16, 0x0, 0x64)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x105, 15)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    OP_0D()
    OP_1D(0xE)
    Sleep(500)

    ChrTalk(    #97
        0x101,
        (
            "#341F#2PWoohoo! ㈱\x02\x03",

            "I finally got through the\x01",
            "scene with no mistakes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x105,
        (
            "#351F#1PHa ha. And a convincing\x01",
            "performance it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#346F#2PHa ha ha. I've got nothing\x01",
            "on you, though.\x02\x03",

            "I don't think you've\x01",
            "flubbed a single line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x105,
        (
            "#350F#1PWell, I've been familiar with\x01",
            "this script for a long time.\x02\x03",

            "I think I learned it at about\x01",
            "the same rate you're going.\x02\x03",

            "#351FI really appreciate you taking\x01",
            "the trouble to rehearse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#340F#2PIt's no big deal. You've kinda\x01",
            "been my guide through it all.\x02\x03",

            "I think you would make a great\x01",
            "bracer, personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x105,
        "#355F#1PHa ha... You flatter me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x105,
        (
            "#040FWe finally do this for real\x01",
            "tomorrow.\x02\x03",

            "I hope Matron Theresa and the\x01",
            "children will enjoy it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#000FHa ha... They really mean\x01",
            "a lot to you, don't they?\x02\x03",

            "They're like your family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x105,
        "#040F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#000FI'm sorry. Did I say\x01",
            "something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x105,
        (
            "#040FNo... You're exactly right.\x02\x03",

            "They're the ones who taught me\x01",
            "the real value of family...\x02\x03",

            "Both of my parents died\x01",
            "shortly after I was born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#000FWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x105,
        (
            "#040FI was left in the care of an\x01",
            "affluent relative. I never\x01",
            "wanted for anything...\x02\x03",

            "But I really had no idea what\x01",
            "having a family was like.\x02\x03",

            "It was ten years ago that\x01",
            "I met the matron...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#000FTen years ago...\x02\x03",

            "Was that during the Hundred\x01",
            "Days War?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x105,
        (
            "#040FYes... That was when I came\x01",
            "to Ruan.\x02\x03",

            "Everyone I knew had scattered\x01",
            "trying to escape the Imperial\x01",
            "forces...\x02\x03",

            "Matron Theresa and her\x01",
            "husband, Joseph, took me in\x01",
            "and cared for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#000FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x105,
        (
            "#040FAfter the war ended, we\x01",
            "waited several months for\x01",
            "word to come of my relatives...\x02\x03",

            "She and Joseph were so kind\x01",
            "to me...\x02\x03",

            "That was when I first\x01",
            "understood...\x02\x03",

            "...what it must be like to\x01",
            "have a mother and father.\x02\x03",

            "And how it must be to have\x01",
            "a family to be with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#000FKloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x105,
        (
            "#040FI-I'm sorry...\x02\x03",

            "I've been rambling... You\x01",
            "must be bored to tears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#000FNo...not at all.\x02\x03",

            "Let's really show everyone\x01",
            "tomorrow how it's done!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x105,
        "#040FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#000FI was worried before, but\x01",
            "I'm really excited now.\x02\x03",

            "Jill and Hans sure have worked\x01",
            "hard on this, haven't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x105,
        (
            "#040FHa ha... Yes, indeed.\x02\x03",

            "But I think Joshua has really\x01",
            "been the biggest help.\x02\x03",

            "I never expected him to\x01",
            "be such a good actor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#000FY-Yeah...\x02\x03",

            "He acted all uninterested, but\x01",
            "he sure plays the role of the\x01",
            "spoiled princess well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x105,
        (
            "#040FHe definitely nailed the mannerisms.\x01",
            "I've seen professionals turn in\x01",
            "worse performances.\x02\x03",

            "Does he have any experience\x01",
            "in theater?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#000FHmm...\x02\x03",

            "I don't really know much about\x01",
            "his life before I met him...\x02\x03",

            "Whatever went on back then,\x01",
            "he's never wanted to talk\x01",
            "about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x105,
        (
            "#040FOh...\x02\x03",

            "I'm sorry... I don't mean to pry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#000FHa ha ha...\x01",
            "Don't sweat it.\x02\x03",

            "He's always been the type\x01",
            "to be good at whatever\x01",
            "he does.\x02\x03",

            "He's always so calm and collected.\x02\x03",

            "Sometimes he gets flustered,\x01",
            "though, and that's when he's\x01",
            "really cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x105,
        (
            "#040F*giggle*\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#000FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x105,
        (
            "#040FPerhaps our roles should\x01",
            "have been reversed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#000FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x105,
        (
            "#040FJulius and Oscar.\x02\x03",

            "Somehow I think you would have\x01",
            "preferred to play Oscar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#000FUh, how come?\x02\x03",

            "Well, maybe. I mean, Julius is\x01",
            "the son of a noble, and I sure\x01",
            "don't know anything about that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x105,
        (
            "#040FThat's not what I mean.\x02\x03",

            "It's more about...umm,\x01",
            "you know...the ending...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#000FOh...\x01",
            "You mean how Oscar gets...\x02\x03",

            "But that's just on the cheek,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x105,
        "#040FWell, that's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#000FW-Well, at least it's just\x01",
            "Joshua...\x02\x03",

            "And hey, do you mean you\x01",
            "wouldn't like kissing Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x105,
        (
            "#040FD-Don't be ridiculous!\x02\x03",

            "Still, it does seem rather risque...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#000FC-Come on. You're starting\x01",
            "to sound like Jill.\x02\x03",

            "And besides, Joshua just sees\x01",
            "me like a little sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x105,
        "#040FDoes he...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        (
            "#000FHe's always treated me like a\x01",
            "little kid, especially with my\x01",
            "dad around.\x02\x03",

            "It drives me nuts...\x02\x03",

            "Anyway, there's absolutely\x01",
            "nothing like that going on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x105,
        "#040FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        "#010F...Ah, here you are.\x02",
    )

    CloseMessageWindow()

    def lambda_3CE0():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CE0)

    def lambda_3CEE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CEE)

    def lambda_3CFC():
        OP_6D(-150, 1000, 11520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CFC)

    def lambda_3D14():
        OP_8E(0xFE, 0xDC, 0x0, 0x2030, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D14)
    OP_8E(0x102, 0x514, 0x0, 0x21A2, 0xBB8, 0x0)

    ChrTalk(    #141
        0x101,
        "#000FJ-Joshua?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x105,
        "#040FHans...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x9,
        (
            "#730FRehearsal's over, and you're\x01",
            "still practicing.\x02\x03",

            "That's some dedication you\x01",
            "two have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        "#010FReady for the big duel scene?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#000FJ-Just leave it to us!\x01",
            "It'll be flawless!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x102,
        (
            "#010FReally...? I look forward to\x01",
            "seeing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x105,
        "#040FAnyway...were you looking for us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x9,
        (
            "#730FYeah...today's the last day\x01",
            "that you two will be staying\x01",
            "with us in the dorms, right?\x02\x03",

            "I was thinking we could\x01",
            "have a big dinner to pump \x01",
            "ourselves up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#000FHmm... Maybe...\x02\x03",

            "Yeah, let's do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x105,
        (
            "#040FI think it sounds like\x01",
            "a great idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        "#010FBy the way...wasn't Jill with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x105,
        (
            "#040FShe was called away by the\x01",
            "dean some time ago...\x02\x03",

            "I'll go check on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#000FI'll come with you!\x02\x03",

            "You guys can go on ahead\x01",
            "to the cafeteria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x102,
        (
            "#010FOkay.\x02\x03",

            "Let's go, Hans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x9,
        "#730FAs you wish, boss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        "#010FDon't call me that...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_40AE():
        OP_8E(0xFE, 0x140, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_40AE)
    Sleep(500)
    OP_8E(0x102, 0x140, 0x0, 0x140, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_6D(-410, 1000, 15230, 1000)
    OP_67(0, 9500, -10000, 0)

    ChrTalk(    #157
        0x101,
        (
            "#000FHa ha... Looks like they've\x01",
            "really hit it off.\x02\x03",

            "Sometimes it worries me that\x01",
            "he doesn't really let people\x01",
            "get close...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x105,
        "#040F*chuckle*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #159
        0x101,
        "#000FWhat?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #160
        0x105,
        "#040FOh, it's nothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#000FOkay, then.\x01",
            "Let's go get changed.\x02\x03",

            "It'd be kind of embarrassing\x01",
            "to walk around like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x105,
        "#040FI have to agree.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(-35450, 1000, 8010, 0)
    OP_6C(45000, 0)
    RemoveParty(0x1, 0xFF)
    SetChrPos(0x105, -36670, 1000, 6980, 0)
    SetChrPos(0x101, -36420, 1000, 8500, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(    #163
        0x101,
        (
            "#000FThat should do it...\x02\x03",

            "Want to go meet up with Jill\x01",
            "in the dean's office?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x105,
        "#040FAll right.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_29_2357 end

    def Function_30_430D(): pass

    label("Function_30_430D")

    EventBegin(0x0)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_6D(-63840, 1000, 10070, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -64190, 1000, 9630, 225)
    SetChrPos(0x105, -63900, 1000, 8550, 270)
    SetChrPos(0x102, -65269, 1000, 9930, 180)
    SetChrPos(0x9, -66110, 1000, 8290, 45)
    SetChrPos(0x8, -65560, 1000, 7740, 45)
    OP_44(0x28, 0xFF)
    OP_44(0x2A, 0xFF)
    OP_44(0x2B, 0xFF)
    OP_44(0x29, 0xFF)
    OP_44(0x27, 0xFF)
    OP_44(0x2C, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrPos(0x28, -66100, 0, 1150, 0)
    SetChrPos(0x2A, -66100, 0, 1150, 0)
    SetChrPos(0x2B, -66100, 0, 1150, 0)
    SetChrPos(0x29, -66100, 0, 1150, 0)
    SetChrPos(0x27, -66100, 0, 1150, 0)
    SetChrPos(0x2C, -66100, 0, 1150, 0)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x2C, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #165
        0x8,
        (
            "#641FAhhh... Brilliant! Just brilliant!\x02\x03",

            "That was one fine play,\x01",
            "if the director's allowed\x01",
            "to say so!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x105,
        (
            "#041F#4PAt first, I thought people would\x01",
            "make fun of us with the roles\x01",
            "switched like that...\x02\x03",

            "I'm so glad they took it\x01",
            "seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x102,
        (
            "#010F#3PAgreed. The costumes worked\x01",
            "out pretty well.\x02\x03",

            "#017FI wouldn't want to have to wear\x01",
            "mine again, though. Corsets are\x01",
            "like some form of torture...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        (
            "#731F#1PHa ha... No kidding. Well,\x01",
            "it was all for a good cause.\x02\x03",

            "And just wait till you see how\x01",
            "many pictures the Photography\x01",
            "Club took...\x02\x03",

            "The ones of you ought to be\x01",
            "particularly popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x102,
        "#018F#3P*sigh*... Give it a rest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        (
            "#649FThe ones of Estelle and Kloe\x01",
            "won't exactly drive people\x01",
            "away, either.\x02\x03",

            "The guys always go nuts\x01",
            "for the junior girls.\x02\x03",

            "#641FWe're really gonna rake in the mira! ㈱\x01",
            "I mean...uh, all proceeds will go to a\x01",
            "good cause!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x105,
        "#045F#4PJill...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        "#503F#6P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #173
        0x102,
        (
            "#014F#3PHm...?\x02\x03",

            "Estelle? What's wrong?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #174
        0x101,
        "#004F#6P#3S...\x02",
    )

    OP_9E(0x101, 0x32, 0x0, 0x12C, 0x1770)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #175
        0x101,
        (
            "#008F#6PHuh, what, where?! What\x01",
            "are you talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        (
            "#013F#3PNothing important, really...\x02\x03",

            "You've been spacing out ever\x01",
            "since the play finished. Are\x01",
            "you okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x9,
        (
            "#730F#1PWell, that fight scene was\x01",
            "pretty hard work. It's no\x01",
            "surprise that you're tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        (
            "#642FDo you feel sick? We can take\x01",
            "you to the nurse's office...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 300)

    ChrTalk(    #179
        0x101,
        (
            "#008F#6PI'm fine, really!\x02\x03",

            "I deal with fatigue every\x01",
            "day as a bracer.\x02\x03",

            "#503FI'm just trying to get my head\x01",
            "back in order is all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x105,
        (
            "#043F#4POh...\x02\x03",

            "Estelle... You don't mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#503F#6PN-No...\x01",
            "Nothing like that at all...\x02\x03",

            "#504FAaaagh! I promise, I am\x01",
            "perfectly all right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        "#014F#3P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x28,
        (
            "#1PHa ha... I trust we're\x01",
            "not interrupting?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_4B9B():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4B9B)

    def lambda_4BA9():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4BA9)

    def lambda_4BB7():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BB7)

    def lambda_4BC5():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BC5)

    def lambda_4BD3():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4BD3)
    Sleep(400)

    def lambda_4BE6():

        label("loc_4BE6")

        TurnDirection(0xFE, 0x2A, 0)
        OP_48()
        Jump("loc_4BE6")

    QueueWorkItem2(0x101, 1, lambda_4BE6)

    def lambda_4BF7():

        label("loc_4BF7")

        TurnDirection(0xFE, 0x29, 0)
        OP_48()
        Jump("loc_4BF7")

    QueueWorkItem2(0x102, 1, lambda_4BF7)

    def lambda_4C08():

        label("loc_4C08")

        TurnDirection(0xFE, 0x2B, 0)
        OP_48()
        Jump("loc_4C08")

    QueueWorkItem2(0x105, 1, lambda_4C08)

    def lambda_4C19():

        label("loc_4C19")

        TurnDirection(0xFE, 0x2B, 0)
        OP_48()
        Jump("loc_4C19")

    QueueWorkItem2(0x8, 1, lambda_4C19)

    def lambda_4C2A():

        label("loc_4C2A")

        TurnDirection(0xFE, 0x2B, 0)
        OP_48()
        Jump("loc_4C2A")

    QueueWorkItem2(0x9, 1, lambda_4C2A)

    def lambda_4C3B():
        OP_6D(-64769, 1000, 9050, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C3B)
    OP_43(0x2B, 0x1, 0x0, 0x20)
    OP_43(0x2A, 0x1, 0x0, 0x21)
    OP_43(0x27, 0x1, 0x0, 0x22)
    OP_43(0x29, 0x1, 0x0, 0x23)
    OP_43(0x28, 0x1, 0x0, 0x1F)
    Sleep(2000)
    OP_44(0x8, 0xFF)

    def lambda_4C7F():
        OP_8E(0xFE, 0xFFFF0268, 0x3E8, 0x19BE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4C7F)
    OP_44(0x9, 0xFF)

    def lambda_4C9E():
        OP_8E(0xFE, 0xFFFEFDE0, 0x3E8, 0x1932, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4C9E)
    WaitChrThread(0x8, 0x2)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x9, 0x2)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x27, 0x1)

    ChrTalk(    #184
        0x2B,
        (
            "#771F#3PMiss Kloe! Oscar was so cool!\x02\x03",

            "I wanna be that cool when\x01",
            "I grow up!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x2B, 0)

    ChrTalk(    #185
        0x105,
        "#041FHa ha. Thank you...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x2A, 0x1)

    ChrTalk(    #186
        0x2A,
        (
            "#6PYou were really great, too,\x01",
            "Miss Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x2A,
        "#6P*siiiigh* Sir Julius... ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        "#008FH-Hey, now... Mary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x27,
        "#3PAn' Joshua wuz sooo cute! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x29,
        "#6PYeah! I couldn't stop looking. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x102,
        "#019FUm...ha ha... Thank you...\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    WaitChrThread(0x28, 0x1)

    ChrTalk(    #192
        0x28,
        (
            "#750F#1PIt was great fun for us all.\x02\x03",

            "A play about love and friendship\x01",
            "buffeted by the winds of a \x01",
            "tumultuous era... It was so moving!\x02\x03",

            "The fight scene was intense,\x01",
            "and though one could only\x01",
            "expect it to end in tragedy...\x02\x03",

            "...it had such a heart-warming\x01",
            "conclusion.\x02\x03",

            "#751FI thought it was splendid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        (
            "#641FWell...with praise like that,\x01",
            "I'd have to say it was worth\x01",
            "the effort.\x02\x03",

            "#644FOh yeah... Hans?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #194
        0x9,
        "#730F#5P...Oh, right! Almost forgot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#501F#6PHuh? What's up?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    ChrTalk(    #196
        0x8,
        (
            "#648FIt's...nothing bad, don't worry.\x02\x03",

            "I'll be right back, so just...\x01",
            "keep doing what you're doing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        "#505F#6PUm, okay...?\x02",
    )

    CloseMessageWindow()

    def lambda_50C3():

        label("loc_50C3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50C3")

    QueueWorkItem2(0x28, 1, lambda_50C3)

    def lambda_50D4():

        label("loc_50D4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50D4")

    QueueWorkItem2(0x101, 1, lambda_50D4)

    def lambda_50E5():

        label("loc_50E5")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50E5")

    QueueWorkItem2(0x102, 1, lambda_50E5)

    def lambda_50F6():

        label("loc_50F6")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50F6")

    QueueWorkItem2(0x105, 1, lambda_50F6)
    OP_8C(0x8, 90, 400)

    def lambda_510E():
        OP_8E(0xFE, 0xFFFF0F42, 0x3E8, 0x193C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_510E)
    Sleep(500)

    def lambda_512E():
        OP_8E(0xFE, 0xFFFF0F42, 0x3E8, 0x193C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_512E)
    WaitChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x9, 0x2)
    SetChrFlags(0x9, 0x80)
    Sleep(500)
    OP_8E(0x28, 0xFFFEFE26, 0x3E8, 0x1F04, 0x7D0, 0x0)

    ChrTalk(    #198
        0x28,
        (
            "#750F#6PThose were...Jill and Hans, no?\x02\x03",

            "Kloe... Your friends are on\x01",
            "the Student Council, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x28, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    def lambda_51EB():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51EB)

    def lambda_51F9():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51F9)
    TurnDirection(0x105, 0x28, 400)

    ChrTalk(    #199
        0x105,
        (
            "#040FYes, they were in charge of\x01",
            "the production of the play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x28,
        (
            "#750F#6PI see... I must thank them, then.\x02\x03",

            "#754FThe children will have many\x01",
            "fond memories of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x105,
        "#043FMatron...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x101, 0)
    Sleep(400)

    ChrTalk(    #203
        0x28,
        (
            "#750F#6PI've made up my mind... I will\x01",
            "tell them my decision when we\x01",
            "return to Manoria.\x02\x03",

            "And then tomorrow...we'll\x01",
            "take the first steps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#004FWhoa... So soon?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x28, 400)

    ChrTalk(    #205
        0x2B,
        "#770F#4PHey, what'cha talking about?\x02",
    )

    CloseMessageWindow()

    def lambda_53C1():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_53C1)

    def lambda_53CF():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_53CF)
    TurnDirection(0x2A, 0x2B, 400)

    ChrTalk(    #206
        0x2A,
        (
            "#1PClem! You shouldn't listen\x01",
            "in on grownups' talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x28,
        (
            "#751F#6PIt's okay, Mary.\x02\x03",

            "But I think we should probably\x01",
            "return to the inn.\x02\x03",

            "#750FWe can have dinner, and\x01",
            "continue our discussion\x01",
            "over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x2B,
        "#774F#4PO-Okay...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x28,
        (
            "#750F#6PNow, then, Kloe...and you\x01",
            "too, Estelle and Joshua.\x02\x03",

            "I'm afraid we'll be taking\x01",
            "our leave.\x02\x03",

            "#751FThank you for today.\x01",
            "It was a lovely play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#003FOh, hold on a sec. Jill's coming\x01",
            "back any moment, and she'll probably\x01",
            "want to say goodbye before you go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x2C,
        "#1PPardon me.\x02",
    )

    CloseMessageWindow()

    def lambda_55E8():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_55E8)

    def lambda_55F6():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55F6)

    def lambda_5604():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5604)

    def lambda_5612():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5612)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x4)
    OP_8E(0x2C, 0xFFFEFDB8, 0x0, 0xEE2, 0x7D0, 0x0)

    def lambda_563E():

        label("loc_563E")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_563E")

    QueueWorkItem2(0x28, 1, lambda_563E)

    def lambda_564F():

        label("loc_564F")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_564F")

    QueueWorkItem2(0x101, 1, lambda_564F)

    def lambda_5660():

        label("loc_5660")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_5660")

    QueueWorkItem2(0x102, 1, lambda_5660)

    def lambda_5671():

        label("loc_5671")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_5671")

    QueueWorkItem2(0x105, 1, lambda_5671)

    def lambda_5682():

        label("loc_5682")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_5682")

    QueueWorkItem2(0x2A, 1, lambda_5682)

    def lambda_5693():

        label("loc_5693")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_5693")

    QueueWorkItem2(0x29, 1, lambda_5693)

    def lambda_56A4():

        label("loc_56A4")

        TurnDirection(0xFE, 0x2C, 0)
        OP_48()
        Jump("loc_56A4")

    QueueWorkItem2(0x27, 1, lambda_56A4)
    ClearChrFlags(0x2C, 0x4)
    OP_8E(0x2C, 0xFFFEF5DE, 0x0, 0x1130, 0x7D0, 0x0)
    OP_43(0x8, 0x1, 0x0, 0x24)
    OP_43(0x9, 0x1, 0x0, 0x25)
    OP_8E(0x2C, 0xFFFEF688, 0x3E8, 0x1E64, 0x7D0, 0x0)
    OP_8E(0x2C, 0xFFFEF976, 0x3E8, 0x1EB4, 0x7D0, 0x0)

    ChrTalk(    #212
        0x28,
        "#753F#2POh, Dean Collins...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x2C,
        (
            "#780FIt's a pleasure to see you\x01",
            "again, Matron Theresa.\x02\x03",

            "I must apologize for not coming\x01",
            "by earlier, to thank you for\x01",
            "taking the time to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x28,
        (
            "#750F#2PYou needn't thank me...\x02\x03",

            "#751FThe festival was magnificent.\x01",
            "I'm grateful for the invitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x2C,
        (
            "#780FYes, the students were magnificent,\x01",
            "weren't they?\x02\x03",

            "...Kloe told me of your current\x01",
            "situation. Truly dreadful.\x02\x03",

            "I was trying to think of a\x01",
            "way that we could help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x28,
        "#753F#2PI...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x2C,
        "#781FJill.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x8,
        "#644FYes, sir.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFEFE26, 0x3E8, 0x1BF8, 0x3E8, 0x0)
    OP_44(0x28, 0xFF)

    def lambda_591F():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_591F)

    def lambda_592D():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_592D)

    def lambda_593B():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_593B)

    def lambda_5949():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5949)

    def lambda_5957():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_5957)

    def lambda_5965():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5965)

    def lambda_5973():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_5973)

    def lambda_5981():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5981)

    def lambda_598F():
        TurnDirection(0xFE, 0x28, 400)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_598F)
    TurnDirection(0x28, 0x8, 400)
    Sleep(500)

    ChrTalk(    #219
        0x8,
        "#640FPlease, take this...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #220
        (
            "\x07\x05Jill handed Matron Theresa a bulky envelope, sealed with the royal academy's\x01",
            "crest.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x8, 0xFFFEFDF4, 0x3E8, 0x1A54, 0x3E8, 0x0)

    ChrTalk(    #221
        0x28,
        "#753F#1PWhat's this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x8,
        (
            "#640FWe took up a collection\x01",
            "for you. It's one million\x01",
            "mira.\x02\x03",

            "Please use it to help\x01",
            "rebuild the orphanage.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x28, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #223
        0x101,
        "#004FO-O-One million mira?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        "#014FThat's impressive...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x28,
        "#756F#1PBut how...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x2C,
        (
            "#781FWell, we have the duke, as well\x01",
            "as the mayor of Bose...so there\x01",
            "are some celebrities here.\x02\x03",

            "Thanks to them, we were able\x01",
            "to collect far more than we\x01",
            "would have, otherwise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x105,
        "#048FDean...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x2C, 400)

    ChrTalk(    #228
        0x28,
        (
            "#755F#2PNo, I couldn't!\x02\x03",

            "I can't accept this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x9,
        (
            "#730FI don't see why not.\x02\x03",

            "The festival collects donations\x01",
            "for charity every year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x8,
        (
            "#641FPeople donated specifically\x01",
            "to help rebuild the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x28,
        (
            "#757F#2PBut... I...\x02\x03",

            "It's too much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x105,
        "#049FPlease accept it, Matron...\x02",
    )

    CloseMessageWindow()
    OP_44(0x28, 0xFF)
    TurnDirection(0x28, 0x105, 400)

    ChrTalk(    #233
        0x28,
        "#756F#3PBut... Kloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x105,
        (
            "#049FI realize that you're overwhelmed.\x02\x03",

            "#047FBut think about it...\x02\x03",

            "With that much mira, the\x01",
            "rebuilding could start, and you\x01",
            "wouldn't need to go to Grancel.\x02\x03",

            "#043FYou wouldn't have to give\x01",
            "up your herb garden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x28,
        "#757F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x2C,
        (
            "#780FShe speaks the truth.\x02\x03",

            "Joseph would want you to accept\x01",
            "this...for the children.\x02\x03",

            "You needn't focus on the amount...\x01",
            "just what can be done with it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x2C, 400)
    Sleep(500)

    ChrTalk(    #237
        0x28,
        (
            "#754F#2PYou're right...\x02\x03",

            "I... I don't know how to\x01",
            "show my appreciation...\x02\x03",

            "#758FThank you...\x01",
            "Thank you all so very much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        "#003F*sniffle* That's awesome...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x102,
        "#019FYes, that should settle that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x2B,
        (
            "#775F#4PH-Hey...\x01",
            "What's this about going to Grancel?\x02\x03",

            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x2B, 400)

    ChrTalk(    #241
        0x28,
        (
            "#758F#3PIt's okay...\x01",
            "There's no need to worry.\x02\x03",

            "You've all been through\x01",
            "so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x2B,
        (
            "#775F#4PI-It's really not that big a deal...\x02\x03",

            "But...why are you crying, Matron?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 400)

    ChrTalk(    #243
        0x2A,
        "#1PDon't be silly, Clem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x2A,
        "#1PThose are happy tears.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(    #245
        "\x07\x05After the matron and the children left to return to Manoria...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #246
        (
            "\x07\x05...Estelle and Joshua joined the other students in cleaning up after the\x01",
            "festival.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #247
        "\x07\x05By the time everything was done, the day had given way to evening.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_430D end

    def Function_31_6264(): pass

    label("Function_31_6264")

    Sleep(2000)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_31_6264 end

    def Function_32_62BC(): pass

    label("Function_32_62BC")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF02E0, 0x3E8, 0x203A, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x105, 0)
    Return()

    # Function_32_62BC end

    def Function_33_6323(): pass

    label("Function_33_6323")

    Sleep(500)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF02D6, 0x3E8, 0x2350, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_33_6323 end

    def Function_34_638F(): pass

    label("Function_34_638F")

    Sleep(1500)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEFE3A, 0x3E8, 0x2558, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x102, 400)
    Return()

    # Function_34_638F end

    def Function_35_63FB(): pass

    label("Function_35_63FB")

    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEFDB8, 0x0, 0xEE2, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFEF5DE, 0x0, 0x1130, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEF688, 0x3E8, 0x1E64, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF001A, 0x3E8, 0x23F0, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x102, 400)
    Return()

    # Function_35_63FB end

    def Function_36_6467(): pass

    label("Function_36_6467")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFEFDE0, 0x3E8, 0x1932, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_36_6467 end

    def Function_37_6488(): pass

    label("Function_37_6488")

    Sleep(700)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF0268, 0x3E8, 0x19BE, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_37_6488 end

    SaveToFile()

Try(main)
