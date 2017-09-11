from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3104   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Dorothy',                              # 9
        'Factory Chief Murdock',                # 10
        'Supervisor Travis',                    # 11
        'Hazel',                                # 12
        'Sotiria',                              # 13
        'Elise',                                # 14
        'Muriel',                               # 15
        'Stain',                                # 16
        'Vince',                                # 17
        'Elwyn',                                # 18
        'Wong',                                 # 19
        'Lane',                                 # 20
        'Cosimo',                               # 21
        'Monika',                               # 22
        'Bruno',                                # 23
        'Igor',                                 # 24
        'Priam',                                # 25
        'Irene',                                # 26
        'Rehmann',                              # 27
        'Rudi',                                 # 28
        'Faye',                                 # 29
        'Erick',                                # 30
        'Constance',                            # 31
        'Hugo',                                 # 32
        'Antoine',                              # 33
        'Prometheus',                           # 34
        'Ray',                                  # 35
        'Terry',                                # 36
        'Dr. Miriam',                           # 37
        'Wilmont',                              # 38
        'Maintenance Chief Gustav',             # 39
        ' ',                                    # 40
        'Zeiss Landing Port',                   # 41
        'Zeiss - City Block',                   # 42
    )

    DeclEntryPoint(
        Unknown_00              = -32000,
        Unknown_04              = 10000,
        Unknown_08              = 58000,
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02620 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01620 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01100 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01530 ._CH',             # 0E
        'ED6_DT07/CH01250 ._CH',             # 0F
        'ED6_DT07/CH01140 ._CH',             # 10
        'ED6_DT07/CH01150 ._CH',             # 11
        'ED6_DT07/CH01450 ._CH',             # 12
        'ED6_DT07/CH01500 ._CH',             # 13
        'ED6_DT07/CH01550 ._CH',             # 14
        'ED6_DT07/CH01450 ._CH',             # 15
        'ED6_DT07/CH01230 ._CH',             # 16
        'ED6_DT07/CH01680 ._CH',             # 17
        'ED6_DT07/CH01700 ._CH',             # 18
        'ED6_DT07/CH01100 ._CH',             # 19
        'ED6_DT07/CH01220 ._CH',             # 1A
        'ED6_DT07/CH01660 ._CH',             # 1B
        'ED6_DT07/CH01430 ._CH',             # 1C
        'ED6_DT07/CH01450 ._CH',             # 1D
        'ED6_DT07/CH02440 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02620P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01620P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01100P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01530P._CP',             # 0E
        'ED6_DT07/CH01250P._CP',             # 0F
        'ED6_DT07/CH01140P._CP',             # 10
        'ED6_DT07/CH01150P._CP',             # 11
        'ED6_DT07/CH01450P._CP',             # 12
        'ED6_DT07/CH01500P._CP',             # 13
        'ED6_DT07/CH01550P._CP',             # 14
        'ED6_DT07/CH01450P._CP',             # 15
        'ED6_DT07/CH01230P._CP',             # 16
        'ED6_DT07/CH01680P._CP',             # 17
        'ED6_DT07/CH01700P._CP',             # 18
        'ED6_DT07/CH01100P._CP',             # 19
        'ED6_DT07/CH01220P._CP',             # 1A
        'ED6_DT07/CH01660P._CP',             # 1B
        'ED6_DT07/CH01430P._CP',             # 1C
        'ED6_DT07/CH01450P._CP',             # 1D
        'ED6_DT07/CH02440P._CP',             # 1E
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
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
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
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
        TalkScenaIndex      = 37,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = -23030,
        Z                   = 8000,
        Y                   = 86970,
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
        X                   = 28060,
        Z                   = 8000,
        Y                   = 58980,
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
        X                   = -35690,
        Y                   = 9750,
        Z                   = 58940,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = -23010,
        Y                   = 7750,
        Z                   = 74850,
        Range               = 1500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = -50430,
        Y                   = 24000,
        Z                   = 53980,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 44,
    )


    ScpFunction(
        "Function_0_642",          # 00, 0
        "Function_1_BFC",          # 01, 1
        "Function_2_C40",          # 02, 2
        "Function_3_C76",          # 03, 3
        "Function_4_DF3",          # 04, 4
        "Function_5_E17",          # 05, 5
        "Function_6_E3B",          # 06, 6
        "Function_7_E5F",          # 07, 7
        "Function_8_E83",          # 08, 8
        "Function_9_EA7",          # 09, 9
        "Function_10_ECB",         # 0A, 10
        "Function_11_EEF",         # 0B, 11
        "Function_12_F54",         # 0C, 12
        "Function_13_FB9",         # 0D, 13
        "Function_14_101F",        # 0E, 14
        "Function_15_1066",        # 0F, 15
        "Function_16_10C0",        # 10, 16
        "Function_17_1164",        # 11, 17
        "Function_18_11EA",        # 12, 18
        "Function_19_136C",        # 13, 19
        "Function_20_1424",        # 14, 20
        "Function_21_1445",        # 15, 21
        "Function_22_149E",        # 16, 22
        "Function_23_1542",        # 17, 23
        "Function_24_15B4",        # 18, 24
        "Function_25_1615",        # 19, 25
        "Function_26_1692",        # 1A, 26
        "Function_27_16B9",        # 1B, 27
        "Function_28_1721",        # 1C, 28
        "Function_29_18FF",        # 1D, 29
        "Function_30_21FE",        # 1E, 30
        "Function_31_2663",        # 1F, 31
        "Function_32_270C",        # 20, 32
        "Function_33_284E",        # 21, 33
        "Function_34_2855",        # 22, 34
        "Function_35_285C",        # 23, 35
        "Function_36_2914",        # 24, 36
        "Function_37_2CF6",        # 25, 37
        "Function_38_2DCF",        # 26, 38
        "Function_39_2E23",        # 27, 39
        "Function_40_3039",        # 28, 40
        "Function_41_33AE",        # 29, 41
        "Function_42_3769",        # 2A, 42
        "Function_43_376D",        # 2B, 43
        "Function_44_3771",        # 2C, 44
    )


    def Function_0_642(): pass

    label("Function_0_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_69A")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_734")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -15510, 8000, 54720, 275)
    SetChrPos(0xD, -16920, 8000, 54780, 91)
    SetChrPos(0x10, -16950, 8000, 55940, 148)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -15680, 8000, 55990, 243)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -30230, 10000, 47900, 298)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_76A")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_7A0")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -25190, 8000, 66790, 275)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -17150, 8000, 63800, 358)
    Jump("loc_BE7")

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_879")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -34110, 10000, 62990, 166)
    OP_43(0x11, 0x0, 0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -23170, 8000, 59080, 91)
    OP_43(0x12, 0x0, 0x0, 0x5)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -25200, 8000, 67400, 272)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -31870, 10000, 49240, 326)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -33120, 10000, 50470, 135)
    SetChrFlags(0x17, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    Jump("loc_BE7")

    label("loc_879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_A7B")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -30660, 9000, 60810, 69)
    OP_43(0xA, 0x0, 0x0, 0x3)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, -24500, 8750, 51360, 18)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -34110, 10000, 62990, 166)
    OP_43(0x11, 0x0, 0x0, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -27110, 8000, 60420, 69)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -27070, 8000, 59620, 359)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -33870, 10000, 57010, 292)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -30810, 10000, 48800, 320)
    OP_43(0x1D, 0x0, 0x0, 0x7)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32630, 10000, 58920, 255)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -26600, 8000, 55790, 279)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -23180, 8000, 58380, 82)
    OP_43(0x1F, 0x0, 0x0, 0x8)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -29430, 8000, 57220, 85)
    SetChrFlags(0x17, 0x10)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -22660, 8000, 61960, 82)
    OP_43(0x21, 0x0, 0x0, 0xA)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -33530, 10000, 52430, 296)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -33770, 10000, 51140, 330)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -25860, 8000, 60310, 263)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, -21670, 8000, 66490, 242)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -23200, 10000, 47850, 272)
    OP_43(0x20, 0x0, 0x0, 0x9)
    Jump("loc_BE7")

    label("loc_A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_ACE")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    Jump("loc_BE7")

    label("loc_ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_B04")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_B3A")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_B92")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BE7")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)

    label("loc_BE7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_BF3"),
        (SWITCH_DEFAULT, "loc_BFB"),
    )


    label("loc_BF3")

    OP_22(0xE, 0x0, 0x64)
    Jump("loc_BFB")

    label("loc_BFB")

    Return()

    # Function_0_642 end

    def Function_1_BFC(): pass

    label("Function_1_BFC")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFEF278, 0x30052)
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x9C40, 0x64, 0x0)
    OP_43(0x27, 0x0, 0x0, 0x2)
    Return()

    # Function_1_BFC end

    def Function_2_C40(): pass

    label("Function_2_C40")

    OP_72(0x5, 0x20)
    OP_72(0x4, 0x20)

    label("loc_C4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C75")
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x28)
    OP_73(0x5)
    Jump("loc_C4A")

    label("loc_C75")

    Return()

    # Function_2_C40 end

    def Function_3_C76(): pass

    label("Function_3_C76")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_DDD")

    label("loc_C9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB4")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_DDD")

    label("loc_CB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCD")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_DDD")

    label("loc_CCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_DDD")

    label("loc_CE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_DDD")

    label("loc_CFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D18")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_DDD")

    label("loc_D18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D31")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_DDD")

    label("loc_D31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_DDD")

    label("loc_D4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D63")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_DDD")

    label("loc_D63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_DDD")

    label("loc_D7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D95")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_DDD")

    label("loc_D95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAE")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_DDD")

    label("loc_DAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC7")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_DDD")

    label("loc_DC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDD")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_DDD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_DDD")

    label("loc_DF2")

    Return()

    # Function_3_C76 end

    def Function_4_DF3(): pass

    label("Function_4_DF3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E16")
    OP_8D(0xFE, -35270, 61360, -33040, 64150, 3000)
    Jump("Function_4_DF3")

    label("loc_E16")

    Return()

    # Function_4_DF3 end

    def Function_5_E17(): pass

    label("Function_5_E17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E3A")
    OP_8D(0xFE, -26390, 55950, -19770, 61950, 3000)
    Jump("Function_5_E17")

    label("loc_E3A")

    Return()

    # Function_5_E17 end

    def Function_6_E3B(): pass

    label("Function_6_E3B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E5E")
    OP_8D(0xFE, -25190, 68440, -20920, 71850, 3000)
    Jump("Function_6_E3B")

    label("loc_E5E")

    Return()

    # Function_6_E3B end

    def Function_7_E5F(): pass

    label("Function_7_E5F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E82")
    OP_8D(0xFE, -32689, 46510, -30620, 50700, 3000)
    Jump("Function_7_E5F")

    label("loc_E82")

    Return()

    # Function_7_E5F end

    def Function_8_E83(): pass

    label("Function_8_E83")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EA6")
    OP_8D(0xFE, -25190, 54660, -20780, 60740, 3000)
    Jump("Function_8_E83")

    label("loc_EA6")

    Return()

    # Function_8_E83 end

    def Function_9_EA7(): pass

    label("Function_9_EA7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ECA")
    OP_8D(0xFE, -26510, 46520, -19100, 49060, 3000)
    Jump("Function_9_EA7")

    label("loc_ECA")

    Return()

    # Function_9_EA7 end

    def Function_10_ECB(): pass

    label("Function_10_ECB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEE")
    OP_8D(0xFE, -23960, 59250, -21170, 66410, 3000)
    Jump("Function_10_ECB")

    label("loc_EEE")

    Return()

    # Function_10_ECB end

    def Function_11_EEF(): pass

    label("Function_11_EEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_F50")

    ChrTalk(    #0
        0xFE,
        (
            "#690FThat is a LOT of smoke.\x02\x03",

            "If the central factory's fans\x01",
            "can't catch it all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F50")

    TalkEnd(0xFE)
    Return()

    # Function_11_EEF end

    def Function_12_F54(): pass

    label("Function_12_F54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_FB5")

    ChrTalk(    #1
        0xFE,
        (
            "I haven't run that hard in I don't\x01",
            "know how long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Ugh, I don't feel right...\x02",
    )

    CloseMessageWindow()

    label("loc_FB5")

    TalkEnd(0xFE)
    Return()

    # Function_12_F54 end

    def Function_13_FB9(): pass

    label("Function_13_FB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_101B")

    ChrTalk(    #3
        0xFE,
        "Back there is all smoke now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "*gasp* *pant* I really thought\x01",
            "I was done for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101B")

    TalkEnd(0xFE)
    Return()

    # Function_13_FB9 end

    def Function_14_101F(): pass

    label("Function_14_101F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1062")

    ChrTalk(    #5
        0xFE,
        "Is anyone injured?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "Please speak up if you are.\x02",
    )

    CloseMessageWindow()

    label("loc_1062")

    TalkEnd(0xFE)
    Return()

    # Function_14_101F end

    def Function_15_1066(): pass

    label("Function_15_1066")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_10BC")

    ChrTalk(    #7
        0xFE,
        "Wh-What do we do?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "If there's a fire, we'll lose all\x01",
            "of our data!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BC")

    TalkEnd(0xFE)
    Return()

    # Function_15_1066 end

    def Function_16_10C0(): pass

    label("Function_16_10C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1160")

    ChrTalk(    #9
        0xFE,
        "...Strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "That isn't smoke from a fire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "And there are no explosive\x01",
            "experiments going on right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "So what's making that smoke?\x02",
    )

    CloseMessageWindow()

    label("loc_1160")

    TalkEnd(0xFE)
    Return()

    # Function_16_10C0 end

    def Function_17_1164(): pass

    label("Function_17_1164")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_11E6")

    ChrTalk(    #13
        0xFE,
        "It seems everyone got out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "For a moment I flashed back\x01",
            "to the sky bandits' attack,\x01",
            "and my legs just froze. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E6")

    TalkEnd(0xFE)
    Return()

    # Function_17_1164 end

    def Function_18_11EA(): pass

    label("Function_18_11EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_131E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1295")

    ChrTalk(    #15
        0xFE,
        (
            "Now that I think about it,\x01",
            "I haven't seen Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "No matter though. He's probably\x01",
            "just shut himself up in the lab\x01",
            "and lost himself in work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131B")

    label("loc_1295")

    OP_A2(0xA)

    ChrTalk(    #17
        0xFE,
        (
            "Going up and down those stairs?\x01",
            "No problem at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "If it weren't for them, what\x01",
            "would we do? Jump off the\x01",
            "damn terrace?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131B")

    Jump("loc_1368")

    label("loc_131E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1368")

    ChrTalk(    #19
        0xFE,
        "Owowowow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I threw out my back on those\x01",
            "blasted stairs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1368")

    TalkEnd(0xFE)
    Return()

    # Function_18_11EA end

    def Function_19_136C(): pass

    label("Function_19_136C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1420")

    ChrTalk(    #21
        0xFE,
        (
            "We were in the middle of a\x01",
            "meeting when the place\x01",
            "filled up with smoke...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "It was all I could do to get\x01",
            "myself out of there safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "I hope nobody got left.\x02",
    )

    CloseMessageWindow()

    label("loc_1420")

    TalkEnd(0xFE)
    Return()

    # Function_19_136C end

    def Function_20_1424(): pass

    label("Function_20_1424")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1441")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #24
        0xFE,
        "NIIYAAO!\x02",
    )

    CloseMessageWindow()

    label("loc_1441")

    TalkEnd(0xFE)
    Return()

    # Function_20_1424 end

    def Function_21_1445(): pass

    label("Function_21_1445")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(    #25
        0xFE,
        (
            "How many years has it been\x01",
            "since I've moved that fast...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    label("loc_149A")

    TalkEnd(0xFE)
    Return()

    # Function_21_1445 end

    def Function_22_149E(): pass

    label("Function_22_149E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_153E")

    ChrTalk(    #27
        0x9,
        (
            "#800FIf the professor is here, he'll\x01",
            "be in the workshop up on 3.\x02\x03",

            "Check there first. And make sure\x01",
            "you get out at the slightest sign\x01",
            "of trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153E")

    TalkEnd(0xFE)
    Return()

    # Function_22_149E end

    def Function_23_1542(): pass

    label("Function_23_1542")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(    #28
        0x110,
        (
            "#150FI really want to go with you all,\x01",
            "but I guess that's out...\x02\x03",

            "Estelle, you all be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B0")

    TalkEnd(0xFE)
    Return()

    # Function_23_1542 end

    def Function_24_15B4(): pass

    label("Function_24_15B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1611")

    ChrTalk(    #29
        0xFE,
        (
            "H-Have all the guests been\x01",
            "properly evacuated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "This smoke is incredible.\x02",
    )

    CloseMessageWindow()

    label("loc_1611")

    TalkEnd(0xFE)
    Return()

    # Function_24_15B4 end

    def Function_25_1615(): pass

    label("Function_25_1615")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_168E")

    ChrTalk(    #31
        0xFE,
        (
            "I can't find Professor Russell\x01",
            "anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "He wouldn't still be inside...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Oh, what should I do?!\x02",
    )

    CloseMessageWindow()

    label("loc_168E")

    TalkEnd(0xFE)
    Return()

    # Function_25_1615 end

    def Function_26_1692(): pass

    label("Function_26_1692")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_16B5")

    ChrTalk(    #34
        0xFE,
        "Rudi, are you okay?\x02",
    )

    CloseMessageWindow()

    label("loc_16B5")

    TalkEnd(0xFE)
    Return()

    # Function_26_1692 end

    def Function_27_16B9(): pass

    label("Function_27_16B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_171D")

    ChrTalk(    #35
        0xFE,
        "*cough* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "Sm-smoke... *hack* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "...in...lungs... *cough* *hack*\x02",
    )

    CloseMessageWindow()

    label("loc_171D")

    TalkEnd(0xFE)
    Return()

    # Function_27_16B9 end

    def Function_28_1721(): pass

    label("Function_28_1721")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_180C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_17A7")

    ChrTalk(    #38
        0xFE,
        (
            "Did you see how many soldiers\x01",
            "came out of there? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "They didn't seem to have any\x01",
            "problems with the smoke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1809")

    label("loc_17A7")

    OP_A2(0xD)

    ChrTalk(    #40
        0xFE,
        (
            "This is some mess, all this\x01",
            "smoke in the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "My throat's all dried out!\x02",
    )

    CloseMessageWindow()

    label("loc_1809")

    Jump("loc_18FB")

    label("loc_180C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_184B")

    ChrTalk(    #42
        0xFE,
        "Aaahh, man!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "What is going ON around here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_18FB")

    label("loc_184B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_18FB")

    ChrTalk(    #44
        0xFE,
        (
            "I've got to be the only pilot in\x01",
            "the kingdom who flies an orbalship\x01",
            "while wearing a maintenance uniform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "It's not about looks though,\x01",
            "right? It's about SKILL.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FB")

    TalkEnd(0xFE)
    Return()

    # Function_28_1721 end

    def Function_29_18FF(): pass

    label("Function_29_18FF")

    TalkBegin(0x18)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_195F")
    OP_0D()
    OP_A9(0x4D)
    OP_56(0x0)
    TalkEnd(0x18)
    Return()

    label("loc_195F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1970")
    TalkEnd(0x18)
    Return()

    label("loc_1970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_19EC")

    ChrTalk(    #46
        0x18,
        (
            "Looks like the Royal Army\x01",
            "fleet is coming into port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x18,
        (
            "That's funny, there ain't nothing\x01",
            "going on here...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_19EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1AE1")

    ChrTalk(    #48
        0x18,
        (
            "Workin' hard, or hardly\x01",
            "workin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x18,
        (
            "I tell ya', the factory ship's sure been\x01",
            "getting a workout lately. Been in and out\x01",
            "of port a lot, and on really short notice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x18,
        (
            "The boarding pad has been pretty\x01",
            "quiet this morning, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_1AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1BC0")

    ChrTalk(    #51
        0x18,
        "Looks like another busy day!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x18,
        (
            "Speaking of busy, Rehmann just\x01",
            "came running up here like a\x01",
            "madman a little bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x18,
        (
            "Seems he had to get a factory\x01",
            "ship out of here in a hurry.\x01",
            "That must've been a pain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_1BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1C2D")

    ChrTalk(    #54
        0x18,
        "Morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x18,
        (
            "There ain't nothing like one of\x01",
            "these energy drinks first thing\x01",
            "in the morning!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_1C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1CE4")

    ChrTalk(    #56
        0x18,
        "Thanks for working so late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x18,
        (
            "Geez, what a busy day.\x01",
            "I'm completely exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x18,
        (
            "I'm closing up shop soon, so\x01",
            "if there's something you want,\x01",
            "you better speak up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_1CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1D70")

    ChrTalk(    #59
        0x18,
        (
            "I saw a bunch of guys in blue \x01",
            "military uniforms come out of\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x18,
        "What were they doing in there?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DF5")

    label("loc_1D70")

    OP_A2(0xB)

    ChrTalk(    #61
        0x18,
        (
            "Whew. Looks like the big\x01",
            "fuss is finally over with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x18,
        (
            "What were those military guys\x01",
            "doing under all that smoke,\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF5")

    Jump("loc_21FA")

    label("loc_1DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1E60")

    ChrTalk(    #63
        0x18,
        "O-Okay, everybody, just relax!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x18,
        (
            "Here, everyone just have a\x01",
            "cold drink and calm down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_1E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1F7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1EF8")

    ChrTalk(    #65
        0x18,
        (
            "Yeah, that guy Rehmann over\x01",
            "there? He's a pilot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x18,
        (
            "Of course, he only flies the\x01",
            "factory ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x18,
        "But flying's flying, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F7C")

    label("loc_1EF8")

    OP_A2(0xB)

    ChrTalk(    #68
        0x18,
        (
            "That guy Rehmann over there\x01",
            "looks like a mechanic, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x18,
        "Really, the guy's a pilot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x18,
        "Books and covers, right? Ha!\x02",
    )

    CloseMessageWindow()

    label("loc_1F7C")

    Jump("loc_21FA")

    label("loc_1F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_20C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2038")

    ChrTalk(    #71
        0x18,
        (
            "I can't just think about sales. I have\x01",
            "to worry about management, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x18,
        (
            "Having a 'down home, friendly'\x01",
            "store is an easy thing to say,\x01",
            "but hard to actually do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BE")

    label("loc_2038")

    OP_A2(0xB)

    ChrTalk(    #73
        0x18,
        (
            "Our dream is to have at least\x01",
            "one store of our own some day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x18,
        (
            "I'd love to have a warm little\x01",
            "store like the Bell Station.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BE")

    Jump("loc_21FA")

    label("loc_20C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_213C")

    ChrTalk(    #75
        0x18,
        (
            "The girl selling flowers over\x01",
            "there? Irene? She's my sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x18,
        (
            "Go on and take a look at her\x01",
            "flower shop!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_213C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_21A7")

    ChrTalk(    #77
        0x18,
        "How about a nice, cold drink?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x18,
        (
            "We carry all kinds of good\x01",
            "and healthy stuff!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_21A7")

    OP_A2(0xB)

    ChrTalk(    #79
        0x18,
        (
            "You look like you've been\x01",
            "working hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x18,
        "How about a nice, cold drink?\x02",
    )

    CloseMessageWindow()

    label("loc_21FA")

    TalkEnd(0x18)
    Return()

    # Function_29_18FF end

    def Function_30_21FE(): pass

    label("Function_30_21FE")

    TalkBegin(0x19)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_225E")
    OP_0D()
    OP_A9(0x4E)
    OP_56(0x0)
    TalkEnd(0x19)
    Return()

    label("loc_225E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_226F")
    TalkEnd(0x19)
    Return()

    label("loc_226F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_22CF")

    ChrTalk(    #81
        0x19,
        (
            "I heard a siren coming from\x01",
            "the boarding area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x19,
        "...I wonder what happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_265F")

    label("loc_22CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_234F")

    ChrTalk(    #83
        0x19,
        (
            "I have all kinds of beautiful\x01",
            "flowers! Please have a look!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x19,
        (
            "How about a flower to help\x01",
            "forget your troubles?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265F")

    label("loc_234F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_23E0")

    ChrTalk(    #85
        0x19,
        (
            "*sigh* All the people are too\x01",
            "busy talking to even LOOK\x01",
            "at my flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x19,
        (
            "Oh well. It's to be expected.\x01",
            "It was quite an ordeal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265F")

    label("loc_23E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_241F")

    ChrTalk(    #87
        0x19,
        "Good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x19,
        "Don't my flowers smell nice?\x02",
    )

    CloseMessageWindow()
    Jump("loc_265F")

    label("loc_241F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_246A")

    ChrTalk(    #89
        0x19,
        "Good evening!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x19,
        (
            "There's still time before\x01",
            "I close today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265F")

    label("loc_246A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_24FA")

    ChrTalk(    #91
        0x19,
        (
            "Just when the smoke stopped,\x01",
            "all of those soldiers came out\x01",
            "of the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x19,
        (
            "Do you think they were the\x01",
            "ones who stopped it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265F")

    label("loc_24FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2519")

    ChrTalk(    #93
        0x19,
        "Oh my goodness!\x02",
    )

    CloseMessageWindow()
    Jump("loc_265F")

    label("loc_2519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2588")

    ChrTalk(    #94
        0x19,
        "Zeiss has so few trees.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x19,
        (
            "I'd love to take a trip to see the\x01",
            "flowers in the town of Manoria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265F")

    label("loc_2588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2606")

    ChrTalk(    #96
        0x19,
        (
            "That's my brother over there\x01",
            "selling drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x19,
        (
            "Our dream is to make enough\x01",
            "money to open our own store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265F")

    label("loc_2606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_265F")

    ChrTalk(    #98
        0x19,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x19,
        (
            "I have all kinds of beautiful\x01",
            "flowers! Please have a look!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_265F")

    TalkEnd(0x19)
    Return()

    # Function_30_21FE end

    def Function_31_2663(): pass

    label("Function_31_2663")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2708")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_26B9")

    ChrTalk(    #100
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Think I'll have a drink to calm\x01",
            "my nerves a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2708")

    label("loc_26B9")

    OP_A2(0x6)

    ChrTalk(    #102
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "I can't believe this. I don't think\x01",
            "I can go back to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2708")

    TalkEnd(0xFE)
    Return()

    # Function_31_2663 end

    def Function_32_270C(): pass

    label("Function_32_270C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_284A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_27B5")

    ChrTalk(    #104
        0xFE,
        (
            "I'm glad to see you're okay, \x01",
            "but I haven't seen Russell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "He's probably okay, though.\x01",
            "I'm pretty sore over here,\x01",
            "but I'm sure he's fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284A")

    label("loc_27B5")

    OP_A2(0x7)

    ChrTalk(    #106
        0xFE,
        (
            "Look at you, Igor. How did you\x01",
            "manage not to get hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "You really barreled down the\x01",
            "emergency stairs. That must\x01",
            "have been tough on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_284A")

    TalkEnd(0xFE)
    Return()

    # Function_32_270C end

    def Function_33_284E(): pass

    label("Function_33_284E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_33_284E end

    def Function_34_2855(): pass

    label("Function_34_2855")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_34_2855 end

    def Function_35_285C(): pass

    label("Function_35_285C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_28AC")

    ChrTalk(    #108
        0xFE,
        (
            "Royal Guard uniforms...\x01",
            "That is troubling news indeed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2910")

    label("loc_28AC")

    OP_A2(0x0)

    ChrTalk(    #109
        0xFE,
        "What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Do you think the people\x01",
            "responsible for the attack\x01",
            "were really Royal Guardsmen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2910")

    TalkEnd(0xFE)
    Return()

    # Function_35_285C end

    def Function_36_2914(): pass

    label("Function_36_2914")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2A2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2981")

    ChrTalk(    #111
        0xFE,
        "I just can't calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Maybe some nice flowers will \x01",
            "help me clear my head...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A28")

    label("loc_2981")

    OP_A2(0x1)

    ChrTalk(    #113
        0xFE,
        "Still though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "They still haven't found the ones who\x01",
            "attacked the central factory yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Are the Royal Army and the\x01",
            "Bracer Guild even doing\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A28")

    Jump("loc_2CF2")

    label("loc_2A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2AD6")

    ChrTalk(    #116
        0xFE,
        (
            "I've asked lots of people and\x01",
            "they all say they saw soldiers\x01",
            "in blue at the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Vince saw them, too. I never did\x01",
            "trust those puffed up guardsmen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2C7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B61")

    ChrTalk(    #118
        0xFE,
        (
            "Every time I go shopping, \x01",
            "Vince starts to complain\x01",
            "about every little thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "He can be so difficult sometimes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C78")

    label("loc_2B61")

    OP_A2(0x1)

    ChrTalk(    #120
        0xFE,
        (
            "Hello, Tita. Showing some\x01",
            "guests around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x107,
        (
            "#060FOh, hello, Elise.\x02\x03",

            "Looking for some new flowers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Yes, that's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Every time I go shopping, \x01",
            "Vince starts to complain\x01",
            "about every little thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "He's as particular as certain\x01",
            "other people I could name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C78")

    Jump("loc_2CF2")

    label("loc_2C7B")


    ChrTalk(    #125
        0xFE,
        "Ooh, look at these flowers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I'd love to plant these on the\x01",
            "veranda, but I'm afraid the\x01",
            "colors might clash...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF2")

    TalkEnd(0xFE)
    Return()

    # Function_36_2914 end

    def Function_37_2CF6(): pass

    label("Function_37_2CF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2DCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2D94")

    ChrTalk(    #127
        0xFE,
        (
            "Even the Royal Guardsmen were\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "Jackpot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Okay, that's it. I am SO going\x01",
            "to be a receptionist at the\x01",
            "central factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCB")

    label("loc_2D94")

    OP_A2(0x2)

    ChrTalk(    #130
        0xFE,
        (
            "What?!\x01",
            "The Royal Guard were here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "Score!\x02",
    )

    CloseMessageWindow()

    label("loc_2DCB")

    TalkEnd(0xFE)
    Return()

    # Function_37_2CF6 end

    def Function_38_2DCF(): pass

    label("Function_38_2DCF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2E1F")

    ChrTalk(    #132
        0xFE,
        "I don't think it's a fire...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "So what's all that smoke then?\x02",
    )

    CloseMessageWindow()

    label("loc_2E1F")

    TalkEnd(0xFE)
    Return()

    # Function_38_2DCF end

    def Function_39_2E23(): pass

    label("Function_39_2E23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2EAE")

    ChrTalk(    #134
        0xFE,
        (
            "No one knows if the people \x01",
            "in the blue uniforms were \x01",
            "really soldiers or not yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "Who could they have been?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F2A")

    label("loc_2EAE")

    OP_A2(0x3)

    ChrTalk(    #136
        0xFE,
        (
            "I'm sure both the Royal Guardsmen\x01",
            "and the Bracer Guild are doing the\x01",
            "best they can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "We just aren't hearing it.\x02",
    )

    CloseMessageWindow()

    label("loc_2F2A")

    Jump("loc_3035")

    label("loc_2F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2F99")

    ChrTalk(    #138
        0xFE,
        (
            "What I said I saw were, 'Men\x01",
            "in blue soldiers' uniforms.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "I didn't say Royal Guardsmen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3035")

    label("loc_2F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2FEA")

    ChrTalk(    #140
        0xFE,
        (
            "I'm not obsessive, it's just that\x01",
            "Mother can be so obtuse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFC")

    label("loc_2FEA")


    ChrTalk(    #141
        0xFE,
        "Hello, Tita.\x02",
    )

    CloseMessageWindow()

    label("loc_2FFC")

    Jump("loc_3035")

    label("loc_2FFF")


    ChrTalk(    #142
        0xFE,
        (
            "Mother, there are enough flowers\x01",
            "on the veranda.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3035")

    TalkEnd(0xFE)
    Return()

    # Function_39_2E23 end

    def Function_40_3039(): pass

    label("Function_40_3039")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_31F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_311B")

    ChrTalk(    #143
        0xFE,
        (
            "I guess I better be getting\x01",
            "back to the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "Here I am giving stuff away for\x01",
            "free... I'm sure my wife'll have a\x01",
            "field day with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "But I was able to help some\x01",
            "people out, so that's good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_311B")

    OP_A2(0x4)

    ChrTalk(    #146
        0xFE,
        "Finally...the smoke's cleared.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I'm glad to hear there were\x01",
            "no injuries at the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "I heard some stuff was stolen,\x01",
            "but they can just build more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I guess I better be getting\x01",
            "back to the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F5")

    Jump("loc_33AA")

    label("loc_31F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_33AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3247")

    ChrTalk(    #150
        0xFE,
        "Try to help wherever you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "Be careful out there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_33AA")

    label("loc_3247")

    OP_A2(0x4)

    ChrTalk(    #152
        0xFE,
        "Hey, are you guys all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I'm Elwyn, from the general\x01",
            "goods store. I heard something\x01",
            "happened and ran over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I brought some stuff from \x01",
            "my store, too, so if you need\x01",
            "anything just let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "This is an emergency!\x01",
            "Don't worry about the money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "There you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "Try to help wherever you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "Be careful out there!\x02",
    )

    CloseMessageWindow()

    label("loc_33AA")

    TalkEnd(0xFE)
    Return()

    # Function_40_3039 end

    def Function_41_33AE(): pass

    label("Function_41_33AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3465")

    ChrTalk(    #159
        0xFE,
        (
            "I can't believe something like\x01",
            "this would happen while I\x01",
            "wasn't around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "I'll never be able to look Gundolf\x01",
            "in the eye... He left me in charge\x01",
            "of things!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3765")

    label("loc_3465")

    OP_A2(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_36E0")

    ChrTalk(    #161
        0xFE,
        "It's you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#000FWong...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "I...I just got back to Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "What in the Goddess' name\x01",
            "is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#000FWell, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x106,
        (
            "#050FHey, what are you doing?\x02\x03",

            "Get your butts back to the guild!\x01",
            "We've got no time for chit-chat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#000FGrrr...\x02\x03",

            "I hate it when Agate's right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x102,
        "#010FI don't know why...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x12, 400)

    ChrTalk(    #169
        0x106,
        (
            "#050FI'm talking to you, TOO!\x02\x03",

            "You're a bracer, aren't you?\x01",
            "Get out there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "Sorry, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x106,
        (
            "#050FHmph.\x02\x03",

            "Our job's to worry about what\x01",
            "to do next, not what's already\x01",
            "said and done.\x02\x03",

            "Let's get moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#000FBye, Wong...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "Okay. See you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x102,
        "#010FLet's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3765")

    label("loc_36E0")


    ChrTalk(    #176
        0xFE,
        (
            "The central factory was\x01",
            "attacked...inconceivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "I need to get back to the guild and\x01",
            "check in on the current situation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3765")

    TalkEnd(0xFE)
    Return()

    # Function_41_33AE end

    def Function_42_3769(): pass

    label("Function_42_3769")

    SetPlaceName(0x85)
    Return()

    # Function_42_3769 end

    def Function_43_376D(): pass

    label("Function_43_376D")

    SetPlaceName(0x81)
    Return()

    # Function_43_376D end

    def Function_44_3771(): pass

    label("Function_44_3771")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A3(0x546)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A2(0x546)
    Return()

    # Function_44_3771 end

    SaveToFile()

Try(main)
