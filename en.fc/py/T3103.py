from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3103   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3103.x',
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
        'Sotiria',                              # 9
        'Elise',                                # 10
        'Muriel',                               # 11
        'Vince',                                # 12
        'Gary',                                 # 13
        'Knowles',                              # 14
        'Didi',                                 # 15
        'Lane',                                 # 16
        'Cosimo',                               # 17
        'Monika',                               # 18
        'Bruno',                                # 19
        'Igor',                                 # 20
        'Radmira',                              # 21
        'Charles',                              # 22
        ' ',                                    # 23
        'Zeiss Central Factory',                # 24
        'Tratt Plains Road',                    # 25
        'Ritter Roadway',                       # 26
    )

    DeclEntryPoint(
        Unknown_00              = 67000,
        Unknown_04              = 0,
        Unknown_08              = 53000,
        Unknown_0C              = 4,
        Unknown_0E              = 315,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01200 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01060 ._CH',             # 0A
        'ED6_DT07/CH01160 ._CH',             # 0B
        'ED6_DT07/CH01160 ._CH',             # 0C
        'ED6_DT07/CH01100 ._CH',             # 0D
        'ED6_DT07/CH02490 ._CH',             # 0E
        'ED6_DT07/CH01530 ._CH',             # 0F
        'ED6_DT07/CH01250 ._CH',             # 10
        'ED6_DT07/CH01690 ._CH',             # 11
        'ED6_DT07/CH02640 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01200P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01060P._CP',             # 0A
        'ED6_DT07/CH01160P._CP',             # 0B
        'ED6_DT07/CH01160P._CP',             # 0C
        'ED6_DT07/CH01100P._CP',             # 0D
        'ED6_DT07/CH02490P._CP',             # 0E
        'ED6_DT07/CH01530P._CP',             # 0F
        'ED6_DT07/CH01250P._CP',             # 10
        'ED6_DT07/CH01690P._CP',             # 11
        'ED6_DT07/CH02640P._CP',             # 12
    )

    DeclNpc(
        X                   = 17600,
        Z                   = 3500,
        Y                   = 53760,
        Direction           = 283,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 18000,
        Z                   = 3500,
        Y                   = 52580,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 24380,
        Z                   = 3500,
        Y                   = 53780,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 6,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 7,
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
        X                   = -17220,
        Z                   = 8000,
        Y                   = 59000,
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
        X                   = 81330,
        Z                   = 0,
        Y                   = 53110,
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
        X                   = 42990,
        Z                   = 0,
        Y                   = 104270,
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
        X                   = 39600,
        Y                   = -1000,
        Z                   = 90600,
        Range               = 46400,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x16828,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 69400,
        Y                   = -1000,
        Z                   = 56700,
        Range               = 71000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xB734,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 43700,
        Y                   = 0,
        Z                   = 63080,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 40200,
        Y                   = 0,
        Z                   = 66870,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 52230,
        Y                   = 0,
        Z                   = 54590,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 51500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 48500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 59950,
        Y                   = 0,
        Z                   = 25220,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 36000,
        Y                   = 0,
        Z                   = 54740,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 27020,
        Y                   = 0,
        Z                   = 63460,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 23130,
        Y                   = 0,
        Z                   = 82450,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 64030,
        Y                   = 0,
        Z                   = 69550,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )


    ScpFunction(
        "Function_0_502",          # 00, 0
        "Function_1_A43",          # 01, 1
        "Function_2_A87",          # 02, 2
        "Function_3_ABD",          # 03, 3
        "Function_4_C3A",          # 04, 4
        "Function_5_C5E",          # 05, 5
        "Function_6_C82",          # 06, 6
        "Function_7_DAA",          # 07, 7
        "Function_8_1147",         # 08, 8
        "Function_9_1257",         # 09, 9
        "Function_10_1A33",        # 0A, 10
        "Function_11_2182",        # 0B, 11
        "Function_12_26E3",        # 0C, 12
        "Function_13_2CD3",        # 0D, 13
        "Function_14_2D01",        # 0E, 14
        "Function_15_2F90",        # 0F, 15
        "Function_16_304A",        # 10, 16
        "Function_17_34DD",        # 11, 17
        "Function_18_36A8",        # 12, 18
        "Function_19_3E9C",        # 13, 19
        "Function_20_3FB2",        # 14, 20
        "Function_21_40FE",        # 15, 21
        "Function_22_424A",        # 16, 22
        "Function_23_424E",        # 17, 23
        "Function_24_4252",        # 18, 24
        "Function_25_4256",        # 19, 25
        "Function_26_425A",        # 1A, 26
        "Function_27_425E",        # 1B, 27
        "Function_28_4262",        # 1C, 28
    )


    def Function_0_502(): pass

    label("Function_0_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_57A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 47810, 0, 37590, 185)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_5E6")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 38910, 0, 69580, 177)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    Jump("loc_A42")

    label("loc_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_6B1")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16250, 3500, 71750, 39)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 38910, 0, 69580, 177)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 32970, 500, 85010, 175)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39900, 0, 67550, 4)
    Jump("loc_A42")

    label("loc_6B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_6BB")
    Jump("loc_A42")

    label("loc_6BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_6F1")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 22230, 0, 80520, 215)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_74C")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 20340, 0, 80730, 227)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 11290, 0, 64040, 258)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_7F7")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 8690, 0, 54740, 180)
    OP_43(0xC, 0x0, 0x0, 0x5)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 47290, 0, 54830, 275)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 45580, 0, 54810, 97)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_859")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    Jump("loc_A42")

    label("loc_859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_929")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 41900, 0, 61970, 17)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 46850, 0, 87800, 238)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 9770, 0, 59280, 277)
    Jump("loc_A42")

    label("loc_929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_9B7")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 8690, 0, 54740, 306)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 47810, 0, 37590, 185)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_A42")

    label("loc_9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A42")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 8690, 0, 54740, 306)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 47810, 0, 37590, 185)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 38650, 0, 46790, 258)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)

    label("loc_A42")

    Return()

    # Function_0_502 end

    def Function_1_A43(): pass

    label("Function_1_A43")

    OP_16(0x2, 0xFA0, 0xFFFE94B8, 0xFFFEF278, 0x30051)
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    SoundDistance(0xA0, 0x1CC, 0xADC, 0xE63C, 0x2710, 0x9C40, 0x64, 0x0)
    OP_43(0x16, 0x0, 0x0, 0x2)
    Return()

    # Function_1_A43 end

    def Function_2_A87(): pass

    label("Function_2_A87")

    OP_72(0x10, 0x20)
    OP_72(0xE, 0x20)

    label("loc_A91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ABC")
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x28)
    OP_73(0x10)
    Jump("loc_A91")

    label("loc_ABC")

    Return()

    # Function_2_A87 end

    def Function_3_ABD(): pass

    label("Function_3_ABD")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_C24")

    label("loc_AE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFB")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_C24")

    label("loc_AFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B14")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_C24")

    label("loc_B14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_C24")

    label("loc_B2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B46")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_C24")

    label("loc_B46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_C24")

    label("loc_B5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_C24")

    label("loc_B78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B91")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_C24")

    label("loc_B91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_C24")

    label("loc_BAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_C24")

    label("loc_BC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_C24")

    label("loc_BDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF5")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_C24")

    label("loc_BF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_C24")

    label("loc_C0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C24")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_C24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C39")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_C24")

    label("loc_C39")

    Return()

    # Function_3_ABD end

    def Function_4_C3A(): pass

    label("Function_4_C3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C5D")
    OP_8D(0xFE, 17510, 71160, 14830, 73220, 3000)
    Jump("Function_4_C3A")

    label("loc_C5D")

    Return()

    # Function_4_C3A end

    def Function_5_C5E(): pass

    label("Function_5_C5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C81")
    OP_8D(0xFE, 11460, 51180, 8590, 67130, 3000)
    Jump("Function_5_C5E")

    label("loc_C81")

    Return()

    # Function_5_C5E end

    def Function_6_C82(): pass

    label("Function_6_C82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_DA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(    #0
        0xFE,
        (
            "By the way, I'm pleased to hear\x01",
            "Randall's working so hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "But when did he start working\x01",
            "in a BAR?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA6")

    label("loc_D06")

    OP_A2(0xB)

    ChrTalk(    #2
        0xFE,
        (
            "Would you look at that...\x01",
            "the main clock IS slow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Guess that blackout's\x01",
            "responsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Well, I'll be sure t' take\x01",
            "a look at it in a little bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA6")

    TalkEnd(0xFE)
    Return()

    # Function_6_C82 end

    def Function_7_DAA(): pass

    label("Function_7_DAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1143")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C2")
    OP_A2(0x583)

    ChrTalk(    #5
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "Hey. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#014F...?\x02\x03",

            "#010FAh, hey.\x01",
            "It HAS been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#501FWho's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#010FYou remember that kid who was\x01",
            "looking for that piece of quartz in\x01",
            "Rolent, don't you?\x02\x03",

            "Remember? We took a request\x01",
            "to find it a while back.\x02\x03",

            "Are you headed back to\x01",
            "the Republic?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #10
        0xFE,
        (
            "Nah, the central factory. We\x01",
            "made some cash in Grancel and\x01",
            "have some shopping to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Mom said we're gonna take this\x01",
            "mira and stock up on orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "They say the eyes are the first\x01",
            "to go, but she can still spot a\x01",
            "good deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#506FI can see you're still an\x01",
            "obnoxious brat.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #14
        0xFE,
        (
            "What? I'm only saying what\x01",
            "everybody else is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "But yeah...did you check out\x01",
            "these crazy moving stairs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I'll never get tired of them!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1143")

    label("loc_10C2")


    ChrTalk(    #17
        0xFE,
        "These moving stairs are cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "It's true that walking up and\x01",
            "down stairs is a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "So make the stairs move.\x01",
            "Nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1143")

    TalkEnd(0xFE)
    Return()

    # Function_7_DAA end

    def Function_8_1147(): pass

    label("Function_8_1147")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_11A9")

    ChrTalk(    #20
        0xFE,
        "Now, where is Charles?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "That stupid boy is always\x01",
            "wandering off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1253")

    label("loc_11A9")

    OP_A2(0xC)

    ChrTalk(    #22
        0xFE,
        "Whew, Zeiss at last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I probably should go to the\x01",
            "central factory and see the\x01",
            "orbment selection...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "But first, a break. Let's find a\x01",
            "nice place to sit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1253")

    TalkEnd(0xFE)
    Return()

    # Function_8_1147 end

    def Function_9_1257(): pass

    label("Function_9_1257")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_13DF")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_131D")

    ChrTalk(    #25
        0xFE,
        (
            "Now we just remove the broken\x01",
            "quartz and we're finished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "*sigh* I just can't seem to get\x01",
            "into this like usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Maybe I should go to the chapel\x01",
            "again for prayer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DC")

    label("loc_131D")

    OP_A2(0x7)

    ChrTalk(    #28
        0xFE,
        (
            "Okay, all the size 8 screws together\x01",
            "in one case, along with two orbal\x01",
            "pressure indicators...CHECK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Feels like the same thing every\x01",
            "single week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Parts inventory is SO dull.\x02",
    )

    CloseMessageWindow()

    label("loc_13DC")

    Jump("loc_1A2F")

    label("loc_13DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(    #31
        0xFE,
        (
            "It...took a lot less time\x01",
            "than I expected to find the\x01",
            "box I was looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I'm going to pretend I'm still\x01",
            "searching when the boss comes\x01",
            "by. Have a little 'me' time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_149A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_152B")

    ChrTalk(    #33
        0xFE,
        (
            "All right! Starting today I will\x01",
            "be positive! POSITIVE, CURSE YOU\x01",
            "ALL!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Today I'm finishing the order\x01",
            "for Elkan's weapon box.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_152B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_157D")

    ChrTalk(    #35
        0xFE,
        "All the factory workers are...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "They've all been evacuated?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_157D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_16B2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1620")

    ChrTalk(    #37
        0xFE,
        (
            "I wanna just tell Elkan to finish\x01",
            "his own boxes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "But...*sigh* I can't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "And ratting him out to old man\x01",
            "Stain'd look bad, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AF")

    label("loc_1620")

    OP_A2(0x7)

    ChrTalk(    #40
        0xFE,
        (
            "Dang it, now the box with the\x01",
            "parts I need is gone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I wanna just tell Elkan to finish\x01",
            "his own boxes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "But...*sigh* I can't.\x02",
    )

    CloseMessageWindow()

    label("loc_16AF")

    Jump("loc_1A2F")

    label("loc_16B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1831")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1753")

    ChrTalk(    #43
        0xFE,
        (
            "Man...these boxes are\x01",
            "just a MESS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "It's going to take FOREVER to\x01",
            "find what I need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Progress demands sacrifice, \x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_182E")

    label("loc_1753")

    OP_A2(0x7)

    ChrTalk(    #46
        0xFE,
        "But still, what a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I was in total shock when the\x01",
            "lights went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "But I bet those guys up in the\x01",
            "engine room were even more\x01",
            "surprised, am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Progress demands sacrifice, \x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182E")

    Jump("loc_1A2F")

    label("loc_1831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_18BF")

    ChrTalk(    #50
        0xFE,
        (
            "Hey, Tita. Thanks again for\x01",
            "helping clean up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Tell your grandfather to place\x01",
            "his orders early when he starts\x01",
            "running low.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A2F")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1918")

    ChrTalk(    #52
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "All that's left now is collecting\x01",
            "the broken quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_1918")

    OP_A2(0x7)

    ChrTalk(    #54
        0xFE,
        (
            "Okay, all the size 8 screws together\x01",
            "in one case, along with two orbal\x01",
            "pressure indicators...CHECK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Parts inventory isn't easy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "That's because all the research\x01",
            "labs submit massive orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I'm pretty lucky that I've got the\x01",
            "Professor's grandkid to help me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2F")

    TalkEnd(0xFE)
    Return()

    # Function_9_1257 end

    def Function_10_1A33(): pass

    label("Function_10_1A33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1A99")

    ChrTalk(    #58
        0xFE,
        (
            "Looks like the clock decided\x01",
            "to work properly today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Gotta check it every day.\x02",
    )

    CloseMessageWindow()
    Jump("loc_217E")

    label("loc_1A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1B43")

    ChrTalk(    #60
        0xFE,
        "At last, it's keeping time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "As long as this old clock's tickin',\x01",
            "I reckon I will too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I mean, if I ain't around to\x01",
            "watch the old girl, who will?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217E")

    label("loc_1B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1B8D")

    ChrTalk(    #63
        0x13,
        "Very well, let's get this started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "Yes, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D55")

    label("loc_1B8D")

    OP_A2(0x8)

    ChrTalk(    #65
        0xFE,
        (
            "Thank you for making the time\x01",
            "to help us, Igor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x13,
        "Why, it's no trouble at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x13,
        (
            "An old, obsolete engineer like\x01",
            "me has plenty of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "Ha! 'Obsolete,' he says.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "He helps build the Arseille,\x01",
            "the greatest machine to ever\x01",
            "fly, and he's 'obsolete.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x13,
        "Okay, okay. Then just 'old'.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x13,
        (
            "My small part in the Arseille's\x01",
            "construction wore me out. I\x01",
            "couldn't keep up with Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x13,
        (
            "But I've got to serve as best\x01",
            "I can, even at my age.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D55")

    Jump("loc_217E")

    label("loc_1D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1D8D")

    ChrTalk(    #73
        0xFE,
        "Eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "What's that smoke, I wonder?\x02",
    )

    CloseMessageWindow()
    Jump("loc_217E")

    label("loc_1D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1E22")

    ChrTalk(    #75
        0xFE,
        (
            "Sorry, but I don't trust Randall\x01",
            "to work the machinery any more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Call on the experts to get the\x01",
            "job done right, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC0")

    label("loc_1E22")

    OP_A2(0x8)

    ChrTalk(    #77
        0xFE,
        (
            "Good ol' Igor. Full of spit and\x01",
            "vinegar, like usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Wonder if I could trouble you\x01",
            "to look at the clock. It's been\x01",
            "runnin' slow since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC0")

    Jump("loc_217E")

    label("loc_1EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1F5C")

    ChrTalk(    #79
        0xFE,
        (
            "I guess it's true... ALL the\x01",
            "orbments shut down last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Well, let's get this reset.\x01",
            "I suppose I should call\x01",
            "ol' Igor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC5")

    label("loc_1F5C")

    OP_A2(0x8)

    ChrTalk(    #81
        0xFE,
        "Look at that. The clock's slow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "I guess it's true... ALL the\x01",
            "orbments shut down last night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC5")

    Jump("loc_217E")

    label("loc_1FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_217E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_207A")

    ChrTalk(    #83
        0xFE,
        (
            "Orbments all started with the\x01",
            "technology we invented for\x01",
            "clocks, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "And now orbments are being\x01",
            "used to power clocks. Ain't\x01",
            "science grand?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217E")

    label("loc_207A")

    OP_A2(0x8)

    ChrTalk(    #85
        0xFE,
        "Ah, the memories.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "I helped Professor Russell build\x01",
            "this orbal clock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Orbments drive it, you know.\x01",
            "Long as the orbal power don't\x01",
            "stop, the clock'll keep running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Not many remember the old days\x01",
            "anymore, when Zeiss was 'that\x01",
            "clock town'...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_217E")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A33 end

    def Function_11_2182(): pass

    label("Function_11_2182")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2294")

    ChrTalk(    #89
        0xFE,
        (
            "*giggle* I've discovered a way\x01",
            "to shop without getting bogged\x01",
            "down by decisions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Whenever I don't know what\x01",
            "to buy, I just choose the one\x01",
            "furthest to the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "That way, I don't have to worry\x01",
            "about silly details and can get\x01",
            "on with my shopping!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_2294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_23B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_231F")

    ChrTalk(    #92
        0xFE,
        (
            "That said, doesn't this lack of\x01",
            "information bother you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "We consumers demand all kinds\x01",
            "of important information!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B1")

    label("loc_231F")

    OP_A2(0x9)

    ChrTalk(    #94
        0xFE,
        (
            "I came shopping for canned\x01",
            "goods today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "It's so much easier than bread.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "I mean, what's in the can is\x01",
            "right on the label, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B1")

    Jump("loc_26DF")

    label("loc_23B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2415")

    ChrTalk(    #97
        0xFE,
        (
            "Oh, thank goodness things\x01",
            "have finally calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "Now I can shop properly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_2415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2494")

    ChrTalk(    #99
        0xFE,
        (
            "The owner of the item shop's\x01",
            "run off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Maybe to the factory to see all\x01",
            "the commotion for himself?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_2494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2566")

    ChrTalk(    #101
        0xFE,
        (
            "My father's an orbal engineer.\x01",
            "I'm used to buying parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "*sigh* Parts' vital statistics are\x01",
            "clearly labeled. It's so easy to\x01",
            "make a choice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Why isn't this bread like that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_25E4")

    label("loc_2566")

    OP_A2(0x9)

    ChrTalk(    #104
        0xFE,
        "Wheat, white, rye, sourdough...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "What kind of bread is 'good\x01",
            "bread,' anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "Labels would be SO much easier.\x02",
    )

    CloseMessageWindow()

    label("loc_25E4")

    Jump("loc_26DF")

    label("loc_25E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2666")

    ChrTalk(    #107
        0xFE,
        (
            "This is my first time shopping\x01",
            "for food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "All this bread looks the same. \x01",
            "Which one do I choose?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_2666")

    OP_A2(0x9)

    ChrTalk(    #109
        0xFE,
        "What do I do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "Father told me to go buy bread...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "All this bread looks the same. \x01",
            "Which one do I choose?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DF")

    TalkEnd(0xFE)
    Return()

    # Function_11_2182 end

    def Function_12_26E3(): pass

    label("Function_12_26E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_27E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2769")

    ChrTalk(    #112
        0xFE,
        (
            "I'm tired, but being a bracer\x01",
            "has gotta be tough, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Wouldn't call it 'work' otherwise\x01",
            "though, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E6")

    label("loc_2769")

    OP_A2(0xA)

    ChrTalk(    #114
        0xFE,
        (
            "*sigh* I'm off to the Wolf Fort\x01",
            "this afternoon. Again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "How many orbments do those \x01",
            "Republican guys need anyway?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E6")

    Jump("loc_2CCF")

    label("loc_27E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_28E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2865")

    ChrTalk(    #116
        0xFE,
        "Oh well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Probably a bit early, but I'd\x01",
            "better go place a request for\x01",
            "guards at the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E6")

    label("loc_2865")

    OP_A2(0xA)

    ChrTalk(    #118
        0xFE,
        "Feels like I just got home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "And now I'm off to the\x01",
            "Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I can't even catch my breath\x01",
            "enough to complain!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E6")

    Jump("loc_2CCF")

    label("loc_28E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2A8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_29D7")

    ChrTalk(    #121
        0xFE,
        "I swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Everybody's all blah-blah-blah\x01",
            "about yesterday, instead of \x01",
            "getting some real work done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "And here I am trying to get\x01",
            "ready to leave for the Wolf\x01",
            "Fort!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "We working guys have got it\x01",
            "the worst.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A87")

    label("loc_29D7")

    OP_A2(0xA)

    ChrTalk(    #125
        0xFE,
        (
            "Looks like all the packing's in\x01",
            "order. Almost ready to go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Time for one final check.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Oh, hey, gotta remember to go request\x01",
            "a bracer escort. Time's a-wastin'!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A87")

    Jump("loc_2CCF")

    label("loc_2A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2BC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2B21")

    ChrTalk(    #128
        0xFE,
        (
            "I swear, I get paranoid about this\x01",
            "thing. Never satisfied that it'll\x01",
            "get me where I'm goin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "I worry that it'll break down.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BC4")

    label("loc_2B21")

    OP_A2(0xA)

    ChrTalk(    #130
        0xFE,
        (
            "And I need to be absolutely certain\x01",
            "it won't before I take it even one\x01",
            "selge out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I'd hate to break down in the\x01",
            "middle of a nest of monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC4")

    Jump("loc_2CCF")

    label("loc_2BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2C42")

    ChrTalk(    #132
        0xFE,
        (
            "Shame they don't use airships\x01",
            "for transporting goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Only royalty gets to fly to\x01",
            "the Republic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CCF")

    label("loc_2C42")

    OP_A2(0xA)

    ChrTalk(    #134
        0xFE,
        (
            "Just about time to check\x01",
            "our inventory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Once the order's assembled,\x01",
            "we'll take all the goods to the\x01",
            "Republic via the Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCF")

    TalkEnd(0xFE)
    Return()

    # Function_12_26E3 end

    def Function_13_2CD3(): pass

    label("Function_13_2CD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2CFD")

    ChrTalk(    #136
        0xFE,
        "What's causing that smoke?\x02",
    )

    CloseMessageWindow()

    label("loc_2CFD")

    TalkEnd(0xFE)
    Return()

    # Function_13_2CD3 end

    def Function_14_2D01(): pass

    label("Function_14_2D01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2DD9")

    ChrTalk(    #137
        0xFE,
        (
            "I heard the ones who attacked\x01",
            "the central factory were\x01",
            "members of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "My Vince said he saw soldiers\x01",
            "in blue uniforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "I couldn't believe it, but Vince\x01",
            "isn't one to tell lies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2E01")

    ChrTalk(    #140
        0xFE,
        "It's not a fire, is it?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2EBB")

    ChrTalk(    #141
        0xFE,
        (
            "My son's got a point... There's faaaar\x01",
            "too much planter space up here, and not\x01",
            "enough flowers to fill it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "I wonder if Sotiria would part\x01",
            "with a few flowers for me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F2C")

    ChrTalk(    #143
        0xFE,
        "Vince, dear, what do you think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "Isn't the color balance for this\x01",
            "flower bed nice?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2F2C")

    OP_A2(0x1)

    ChrTalk(    #145
        0xFE,
        (
            "My husband said all the orbments\x01",
            "stopped running yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "Is that even possible?\x02",
    )

    CloseMessageWindow()

    label("loc_2F8C")

    TalkEnd(0xFE)
    Return()

    # Function_14_2D01 end

    def Function_15_2F90(): pass

    label("Function_15_2F90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3046")

    ChrTalk(    #147
        0xFE,
        "I think my mom might be wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "I wanna be a receptionist in\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I should be able to get a position\x01",
            "easily enough. That Hazel's\x01",
            "getting old.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3046")

    TalkEnd(0xFE)
    Return()

    # Function_15_2F90 end

    def Function_16_304A(): pass

    label("Function_16_304A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_31C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30EB")

    ChrTalk(    #150
        0xFE,
        (
            "I wonder if the central factory\x01",
            "will tighten security after this\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "I don't know if I'd like it if\x01",
            "things get too strict...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C1")

    label("loc_30EB")

    OP_A2(0x3)

    ChrTalk(    #152
        0xFE,
        (
            "A group of soldiers wearing\x01",
            "blue uniforms ran past me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "Judging from the time of the\x01",
            "attack on the central factory,\x01",
            "I'm sure they were involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "It's too bad I didn't have an\x01",
            "orbal camera with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C1")

    Jump("loc_34D9")

    label("loc_31C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3246")

    ChrTalk(    #155
        0xFE,
        (
            "What is that smoke? It doesn't\x01",
            "look like it's from a fire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "Maybe some experimental device\x01",
            "is releasing gas?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D9")

    label("loc_3246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_33F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_333E")

    ChrTalk(    #157
        0xFE,
        (
            "If I had the chance, I'd love to\x01",
            "study the phenomenon using\x01",
            "the archives room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Of course, Constance from\x01",
            "Archives would need to finish\x01",
            "reorganizing everything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "It's going to take so long to\x01",
            "figure out the cause...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EE")

    label("loc_333E")

    OP_A2(0x3)

    ChrTalk(    #160
        0xFE,
        "Total orbal shutdown...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "I've never even seen any records\x01",
            "of such an event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "If some experiment was the cause,\x01",
            "I wonder exactly what kind of\x01",
            "experiment it was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EE")

    Jump("loc_34D9")

    label("loc_33F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3445")

    ChrTalk(    #163
        0xFE,
        "By the way, Mother...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "Did you change the flower bed?\x02",
    )

    CloseMessageWindow()
    Jump("loc_34D9")

    label("loc_3445")

    OP_A2(0x3)

    ChrTalk(    #165
        0xFE,
        "An orbal blackout...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "Something like that wasn't in\x01",
            "the first edition theses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "I suppose I need to find more\x01",
            "specialized documents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D9")

    TalkEnd(0xFE)
    Return()

    # Function_16_304A end

    def Function_17_34DD(): pass

    label("Function_17_34DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_361D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3588")

    ChrTalk(    #168
        0xFE,
        (
            "They have everything at that\x01",
            "Eastern-style hot springs resort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "I actually love everything\x01",
            "related to the Far East!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "Ooh, I'm so excited!\x02",
    )

    CloseMessageWindow()
    Jump("loc_361A")

    label("loc_3588")

    OP_A2(0x4)

    ChrTalk(    #171
        0xFE,
        (
            "I hear there's a hot springs\x01",
            "resort near here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "I wanna go see it! But I guess\x01",
            "I'll wait until we check this\x01",
            "place out a little more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_361A")

    Jump("loc_36A4")

    label("loc_361D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_366C")

    ChrTalk(    #173
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Can somebody get me on\x01",
            "this crazy thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A4")

    label("loc_366C")

    OP_A2(0x4)

    ChrTalk(    #175
        0xFE,
        "That's incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "A staircase that moves.\x02",
    )

    CloseMessageWindow()

    label("loc_36A4")

    TalkEnd(0xFE)
    Return()

    # Function_17_34DD end

    def Function_18_36A8(): pass

    label("Function_18_36A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_375E")

    ChrTalk(    #177
        0xFE,
        "Okay, let's arrange cans today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "First move all the unsold cans\x01",
            "to the front right. There.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "Make the goods you want to\x01",
            "sell easy to get at. Get it? \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3823")

    label("loc_375E")

    OP_A2(0x5)

    ChrTalk(    #180
        0xFE,
        (
            "I thought it might be time to\x01",
            "teach my brother Didi about\x01",
            "item display...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "But I guess it's too early.\x01",
            "He just gets bored and quits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "*sigh* I guess I'll have to do\x01",
            "it myself.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x10)

    label("loc_3823")

    Jump("loc_3E98")

    label("loc_3826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_389C")

    ChrTalk(    #183
        0xFE,
        "Didi, you're moving it too far!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "If you set it like that you'll\x01",
            "destroy the entire balance!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3923")

    label("loc_389C")

    OP_A2(0x5)

    ChrTalk(    #185
        0xFE,
        (
            "I think it'd look better if\x01",
            "you moved those cans over\x01",
            "there, a little to the left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "Didi! Set it up the way I told\x01",
            "you to!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3923")

    Jump("loc_3E98")

    label("loc_3926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_39B5")

    ChrTalk(    #187
        0xFE,
        (
            "I'm thinking it's time to get\x01",
            "my brother working in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "I want to teach him about all\x01",
            "the facets of item display!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A2B")

    label("loc_39B5")

    OP_A2(0x5)

    ChrTalk(    #189
        0xFE,
        "Listen up, Didi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "You have to put merchandise\x01",
            "the customers have moved\x01",
            "back to their original place.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_3A2B")

    Jump("loc_3E98")

    label("loc_3A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3C24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3AAA")

    ChrTalk(    #191
        0xFE,
        (
            "I'd forgotten how dark it\x01",
            "actually gets at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "It was kind of scary looking\x01",
            "out the window...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C21")

    label("loc_3AAA")

    OP_A2(0x5)

    ChrTalk(    #193
        0xFE,
        "Oh, Tita. It's you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "Yesterday sure was something\x01",
            "else, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "Did the orbments at your house \x01",
            "all suddenly stop, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x107,
        (
            "#060FEep...?!\x02\x03",

            "...Uh...y-y-yeah! They stopped!\x01",
            "Totally stopped!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "Yeah, they stopped all over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "It was scary, looking out and\x01",
            "seeing the whole town dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "It was scary, looking out and\x01",
            "seeing the whole town dark.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C21")

    Jump("loc_3E98")

    label("loc_3C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3C8F")

    ChrTalk(    #200
        0xFE,
        "Oh, that's just awful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "Let's move all those cans to\x01",
            "the left a little bit more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DCC")

    label("loc_3C8F")

    OP_A2(0x5)

    ChrTalk(    #202
        0xFE,
        (
            "No, no...\x01",
            "The balance is still all off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        "Huh? Oh, Tita, it's you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "Got work at the central factory\x01",
            "again today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x107,
        (
            "#060FUh, yeah.\x02\x03",

            "You're helping out here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "Yeah, I'm in charge of merchandise\x01",
            "display.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "Okay, next is the fruit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "See you at school on Sunday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x107,
        "#060FOkay. Have fun.\x02",
    )

    CloseMessageWindow()

    label("loc_3DCC")

    Jump("loc_3E98")

    label("loc_3DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3E36")

    ChrTalk(    #210
        0xFE,
        "What a mess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "We'll have to restack the cans\x01",
            "again, starting on the right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E98")

    label("loc_3E36")

    OP_A2(0x5)

    ChrTalk(    #212
        0xFE,
        "The balance is all off again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "Maybe if I moved that can on\x01",
            "the left a little more...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E98")

    TalkEnd(0xFE)
    Return()

    # Function_18_36A8 end

    def Function_19_3E9C(): pass

    label("Function_19_3E9C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3EFD")

    ChrTalk(    #214
        0xFE,
        "This is so BORING!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "I can't believe my brother\x01",
            "actually enjoys doing this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAE")

    label("loc_3EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3FAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3F76")
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #216
        0xFE,
        (
            "Activate Orbal Engines! \x01",
            "Can Transmogrification, GO!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        "Beeep, bweeeeep...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "Ka-chink!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FAE")

    label("loc_3F76")

    OP_A2(0x6)

    ChrTalk(    #219
        0xFE,
        "Okay, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "Message received, Dr. Knowles.\x02",
    )

    CloseMessageWindow()

    label("loc_3FAE")

    TalkEnd(0xFE)
    Return()

    # Function_19_3E9C end

    def Function_20_3FB2(): pass

    label("Function_20_3FB2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE8")

    ChrTalk(    #221
        0x101,
        "#002F(Wait, that goes outside.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_40E2")

    label("loc_3FE8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_403B")

    ChrTalk(    #222
        0x102,
        (
            "#012F(So here's the exit. Guess we\x01",
            "might as well get going...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E2")

    label("loc_403B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4070")

    ChrTalk(    #223
        0x107,
        "#062F(Wait, this is the exit...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_40E2")

    label("loc_4070")


    ChrTalk(    #224
        0x108,
        (
            "#070F(Hmm...the streets at night\x01",
            "seem so peaceful.)\x02\x03",

            "(I had hoped to do some more\x01",
            "training, but I can wait.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E2")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_20_3FB2 end

    def Function_21_40FE(): pass

    label("Function_21_40FE")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4134")

    ChrTalk(    #225
        0x101,
        "#002F(Wait, that goes outside.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_422E")

    label("loc_4134")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4187")

    ChrTalk(    #226
        0x102,
        (
            "#012F(So here's the exit. Guess we\x01",
            "might as well get going...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_422E")

    label("loc_4187")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41BC")

    ChrTalk(    #227
        0x107,
        "#062F(Wait, this is the exit...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_422E")

    label("loc_41BC")


    ChrTalk(    #228
        0x108,
        (
            "#070F(Hmm...the streets at night\x01",
            "seem so peaceful.)\x02\x03",

            "(I had hoped to do some more\x01",
            "training, but I can wait.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_422E")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_21_40FE end

    def Function_22_424A(): pass

    label("Function_22_424A")

    SetPlaceName(0x7D)
    Return()

    # Function_22_424A end

    def Function_23_424E(): pass

    label("Function_23_424E")

    SetPlaceName(0x7F)
    Return()

    # Function_23_424E end

    def Function_24_4252(): pass

    label("Function_24_4252")

    SetPlaceName(0x82)
    Return()

    # Function_24_4252 end

    def Function_25_4256(): pass

    label("Function_25_4256")

    SetPlaceName(0x7C)
    Return()

    # Function_25_4256 end

    def Function_26_425A(): pass

    label("Function_26_425A")

    SetPlaceName(0x7A)
    Return()

    # Function_26_425A end

    def Function_27_425E(): pass

    label("Function_27_425E")

    SetPlaceName(0x7B)
    Return()

    # Function_27_425E end

    def Function_28_4262(): pass

    label("Function_28_4262")

    SetPlaceName(0x80)
    Return()

    # Function_28_4262 end

    SaveToFile()

Try(main)
