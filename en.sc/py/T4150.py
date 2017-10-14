from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4150   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4150.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Sieg',                                 # 9
        'Royal Army Soldier',                   # 10
        'Royal Army Soldier',                   # 11
        'Royal Army Soldier',                   # 12
        'Royal Army Soldier',                   # 13
        'Middle-Aged Man',                      # 14
        'Aristocrat',                           # 15
        'Sailor',                               # 16
        'Middle-Aged Woman',                    # 17
        'Middle-Aged Man',                      # 18
        'Middle-Aged Woman',                    # 19
        'Middle-Aged Man',                      # 20
        'Young Woman',                          # 21
        'Berden',                               # 22
        'Royal Army Soldier',                   # 23
        'Royal Army Soldier',                   # 24
        'Grancel - North Block',                # 25
        'Royal Avenue',                         # 26
        'Grancel - East Block',                 # 27
        'Grancel - West Block',                 # 28
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
        'ED6_DT07/CH02320 ._CH',             # 00
        'ED6_DT26/CH20238 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01690 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01150 ._CH',             # 0A
        'ED6_DT26/CH20254 ._CH',             # 0B
        'ED6_DT07/CH01200 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02320P._CP',             # 00
        'ED6_DT26/CH20238P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01690P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01150P._CP',             # 0A
        'ED6_DT26/CH20254P._CP',             # 0B
        'ED6_DT07/CH01200P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6280,
        Z                   = 0,
        Y                   = 2180,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -6430,
        Z                   = 0,
        Y                   = -22020,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -6250,
        Z                   = 0,
        Y                   = -870,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -6250,
        Z                   = 0,
        Y                   = -1920,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -8540,
        Z                   = 250,
        Y                   = 6040,
        Direction           = 172,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -8540,
        Z                   = 250,
        Y                   = 4630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -5690,
        Z                   = 0,
        Y                   = -7580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 13060,
        Z                   = 250,
        Y                   = 4130,
        Direction           = 51,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -8230,
        Z                   = 250,
        Y                   = -31580,
        Direction           = 90,
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
        X                   = 7330,
        Z                   = 250,
        Y                   = -27330,
        Direction           = 37,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 5760,
        Z                   = 0,
        Y                   = -46060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 10,
        Z                   = 250,
        Y                   = 36990,
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
        X                   = -50,
        Z                   = 0,
        Y                   = -90220,
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
        X                   = 54990,
        Z                   = 0,
        Y                   = -1130,
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
        X                   = -44420,
        Z                   = 0,
        Y                   = -19990,
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
        X                   = -5000,
        Y                   = -2000,
        Z                   = -65600,
        Range               = 5000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF0344,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 35,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 38,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 39,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_4C7",          # 01, 1
        "Function_2_536",          # 02, 2
        "Function_3_6B3",          # 03, 3
        "Function_4_722",          # 04, 4
        "Function_5_791",          # 05, 5
        "Function_6_7B5",          # 06, 6
        "Function_7_824",          # 07, 7
        "Function_8_893",          # 08, 8
        "Function_9_8AE",          # 09, 9
        "Function_10_8C9",         # 0A, 10
        "Function_11_8E4",         # 0B, 11
        "Function_12_8FF",         # 0C, 12
        "Function_13_91A",         # 0D, 13
        "Function_14_935",         # 0E, 14
        "Function_15_950",         # 0F, 15
        "Function_16_96B",         # 10, 16
        "Function_17_986",         # 11, 17
        "Function_18_9A1",         # 12, 18
        "Function_19_9BC",         # 13, 19
        "Function_20_9D7",         # 14, 20
        "Function_21_A8E",         # 15, 21
        "Function_22_BD3",         # 16, 22
        "Function_23_D18",         # 17, 23
        "Function_24_168C",        # 18, 24
        "Function_25_19BE",        # 19, 25
        "Function_26_1CB6",        # 1A, 26
        "Function_27_2004",        # 1B, 27
        "Function_28_2352",        # 1C, 28
        "Function_29_264A",        # 1D, 29
        "Function_30_270E",        # 1E, 30
        "Function_31_3160",        # 1F, 31
        "Function_32_31AF",        # 20, 32
        "Function_33_31FE",        # 21, 33
        "Function_34_324D",        # 22, 34
        "Function_35_32D3",        # 23, 35
        "Function_36_32D7",        # 24, 36
        "Function_37_32DB",        # 25, 37
        "Function_38_32DF",        # 26, 38
        "Function_39_32E3",        # 27, 39
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_488")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_4B5")

    label("loc_488")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_494"),
        (SWITCH_DEFAULT, "loc_4B5"),
    )


    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_4B2")

    Jump("loc_4B5")

    label("loc_4B5")

    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_472 end

    def Function_1_4C7(): pass

    label("Function_1_4C7")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x23005B)
    OP_71(0x2, 0x10)
    OP_71(0x0, 0x10)
    OP_71(0x3, 0x10)
    OP_71(0xD, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_503")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_524")
    OP_1B(0xA, 0x0, 0x1C)
    OP_1B(0xB, 0x0, 0x19)
    OP_1B(0xC, 0x0, 0x1A)
    OP_1B(0xD, 0x0, 0x19)
    OP_1B(0xE, 0x0, 0x1B)

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_535")
    OP_1B(0x9, 0x0, 0x1D)

    label("loc_535")

    Return()

    # Function_1_4C7 end

    def Function_2_536(): pass

    label("Function_2_536")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_69D")

    label("loc_55B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_69D")

    label("loc_574")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58D")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_69D")

    label("loc_58D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_69D")

    label("loc_5A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_69D")

    label("loc_5BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D8")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_69D")

    label("loc_5D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F1")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_69D")

    label("loc_5F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_69D")

    label("loc_60A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_623")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_69D")

    label("loc_623")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_69D")

    label("loc_63C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_655")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_69D")

    label("loc_655")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_69D")

    label("loc_66E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_687")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_69D")

    label("loc_687")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69D")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_69D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_69D")

    label("loc_6B2")

    Return()

    # Function_2_536 end

    def Function_3_6B3(): pass

    label("Function_3_6B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_721")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_3_6B3")

    label("loc_721")

    Return()

    # Function_3_6B3 end

    def Function_4_722(): pass

    label("Function_4_722")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_790")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_4_722")

    label("loc_790")

    Return()

    # Function_4_722 end

    def Function_5_791(): pass

    label("Function_5_791")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B4")
    OP_8D(0xFE, 3700, -42040, 10110, -50100, 2000)
    Jump("Function_5_791")

    label("loc_7B4")

    Return()

    # Function_5_791 end

    def Function_6_7B5(): pass

    label("Function_6_7B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_823")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_6_7B5")

    label("loc_823")

    Return()

    # Function_6_7B5 end

    def Function_7_824(): pass

    label("Function_7_824")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_892")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_7_824")

    label("loc_892")

    Return()

    # Function_7_824 end

    def Function_8_893(): pass

    label("Function_8_893")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_893 end

    def Function_9_8AE(): pass

    label("Function_9_8AE")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_8AE end

    def Function_10_8C9(): pass

    label("Function_10_8C9")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_8C9 end

    def Function_11_8E4(): pass

    label("Function_11_8E4")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_8E4 end

    def Function_12_8FF(): pass

    label("Function_12_8FF")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_8FF end

    def Function_13_91A(): pass

    label("Function_13_91A")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_91A end

    def Function_14_935(): pass

    label("Function_14_935")

    TalkBegin(0xFE)

    ChrTalk(    #6
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_935 end

    def Function_15_950(): pass

    label("Function_15_950")

    TalkBegin(0xFE)

    ChrTalk(    #7
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_950 end

    def Function_16_96B(): pass

    label("Function_16_96B")

    TalkBegin(0xFE)

    ChrTalk(    #8
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_96B end

    def Function_17_986(): pass

    label("Function_17_986")

    TalkBegin(0xFE)

    ChrTalk(    #9
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_986 end

    def Function_18_9A1(): pass

    label("Function_18_9A1")

    TalkBegin(0xFE)

    ChrTalk(    #10
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_9A1 end

    def Function_19_9BC(): pass

    label("Function_19_9BC")

    TalkBegin(0xFE)

    ChrTalk(    #11
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_9BC end

    def Function_20_9D7(): pass

    label("Function_20_9D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_A0E")

    ChrTalk(    #12
        0xFE,
        "Did a bird just fly off to the west?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A8A")

    label("loc_A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_A8A")

    ChrTalk(    #13
        0xFE,
        (
            "Mmm, the chill of the night feels\x01",
            "really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Walking around at night's weirdly\x01",
            "calming, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8A")

    TalkEnd(0xFE)
    Return()

    # Function_20_9D7 end

    def Function_21_A8E(): pass

    label("Function_21_A8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_AE5")

    ChrTalk(    #15
        0xFE,
        (
            "Where are you going this late\x01",
            "at night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Be careful on your way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCF")

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_BCF")

    ChrTalk(    #17
        0xFE,
        (
            "There've been reports of an armed\x01",
            "group sighted in the region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "By Colonel Cid's orders, we've\x01",
            "stationed a squadron in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I don't know who they are, but I doubt\x01",
            "they could lay a hand on the capital now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCF")

    TalkEnd(0xFE)
    Return()

    # Function_21_A8E end

    def Function_22_BD3(): pass

    label("Function_22_BD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_C44")

    ChrTalk(    #20
        0xFE,
        "I think the city's probably safe, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Take care not to go anywhere too\x01",
            "empty or quiet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D14")

    label("loc_C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_D14")

    ChrTalk(    #22
        0xFE,
        "I've heard a few things about the society.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I guess their goal's interfering with the\x01",
            "signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "They must be idiots to try to cause\x01",
            "problems in the capital region with\x01",
            "us around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D14")

    TalkEnd(0xFE)
    Return()

    # Function_22_BD3 end

    def Function_23_D18(): pass

    label("Function_23_D18")

    EventBegin(0x0)
    OP_DB()
    AddParty(0x42, 0xFF, 0xFF)
    SetChrFlags(0x143, 0x80)
    OP_6D(-1140, 0, -63570, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(0, 0)
    OP_6E(580, 0)
    SetChrPos(0x101, 630, 0, -64819, 0)
    SetChrPos(0x109, -700, 0, -65820, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x109, 0x80)
    FadeToBright(2000, 0)

    def lambda_D9C():
        OP_6D(50, 0, 5920, 14000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9C)

    def lambda_DB4():
        OP_6C(320000, 16000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB4)

    def lambda_DC4():
        OP_67(0, 14750, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DC4)
    WaitChrThread(0x101, 0x3)
    Fade(1000)
    OP_6D(110, 0, -61800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(134000, 0)
    OP_6E(200, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x109, 0x80)

    def lambda_E2D():
        OP_8E(0xFE, 0x276, 0x0, 0xFFFF0FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E2D)

    def lambda_E48():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0xFFFF0F38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E48)
    WaitChrThread(0x109, 0x1)
    OP_DC()

    ChrTalk(    #25
        0x101,
        (
            "#1002F#6PMan, sun's down already.\x02\x03",

            "I hope things are okay at the villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1060F#4PWell, they might've contacted the guild.\x01",
            "C'mon, let's go check in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1015F#6PRight...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)
    Sleep(500)

    ChrTalk(    #28
        0x101,
        (
            "#1007F#6PErm. Kevin?\x02\x03",

            "Sorry about some of the things I said\x01",
            "back there. I was kinda out of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #29
        0x109,
        (
            "#1061F#4PHeeey, it's cool.\x02\x03",

            "You were a bit messed up because you were\x01",
            "thinkin' of your boyfriend. I get it.\x02\x03",

            "#1060FI'm not worried about it, so relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1017F#6PThanks...\x02\x03",

            "#1015FBut...I'm sorry. I still can't fully trust you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1068F#4PKa-zing. Can't win, can I?\x02\x03",

            "#1060FWell, I should be able to convince you that\x01",
            "I'm not an Ouroboros death merchant or\x01",
            "whatever at your guildhouse. Y'see--\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x143, 0x80)
    SetChrPos(0x143, 30, 300, -49360, 180)

    NpcTalk(    #32
        0x143,
        "Man's Voice",
        "#2PMiss Estelle!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_11B4():
        OP_6D(220, 0, -60300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11B4)

    def lambda_11CC():
        OP_67(0, 7890, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_11CC)

    def lambda_11E4():
        OP_6E(217, 2000)
        ExitThread()

    QueueWorkItem(0x143, 1, lambda_11E4)

    def lambda_11F4():
        TurnDirection(0xFE, 0x143, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11F4)
    Sleep(50)

    def lambda_1207():
        TurnDirection(0xFE, 0x143, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1207)
    OP_8E(0x143, 0x1E, 0x0, 0xFFFF1A96, 0xBB8, 0x0)
    WaitChrThread(0x143, 0x1)

    ChrTalk(    #33
        0x101,
        "#1004FHuh? Phillip?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x143,
        (
            "#722F#6PH-Hello. Pardon me for imposing upon you.\x02\x03",

            "But, Miss Estelle, I must ask...\x02\x03",

            "Have you seen the duke?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1004FDuke Dunan? Uh, we met him this morning...\x02\x03",

            "#1015FHas something happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x143,
        (
            "#722F#6PI would like to know!\x01",
            "He left at around noon and has yet\x01",
            "to return or even contact us.\x02\x03",

            "I've searched all the places His Highness\x01",
            "might have gone, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1007FOh, for... What's he doing?\x01",
            "We're busy enough as it is!\x02\x03",

            "#1006FY'know what? Phillip, come with us. We're\x01",
            "going back to the guildhouse.\x02\x03",

            "If the duke's in trouble, someone might've\x01",
            "contacted the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x143,
        (
            "#722F#6PThat is true...\x01",
            "Allow me to accompany you, then.\x02\x03",

            "#721FAnd...who are you, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        (
            "#1062FKevin Graham, traveling priest of\x01",
            "the Septian Church.\x02\x03",

            "#1061FA pleasure, sir!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x143,
        (
            "#720F#6PHow very polite.\x02\x03",

            "I am the butler to Duke Dunan von Auslese,\x01",
            "Phillip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1007FC'mon, we can do big introductions later.\x02\x03",

            "#1006FLet's get back to the guildhouse!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(290, 0, -61590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 290, 0, -61590, 0)
    SetChrPos(0x109, 290, 0, -61590, 0)
    SetChrPos(0x143, 290, 0, -61590, 0)
    OP_A2(0x1639)
    OP_1B(0xA, 0x0, 0x1C)
    OP_1B(0xB, 0x0, 0x19)
    OP_1B(0xC, 0x0, 0x1A)
    OP_1B(0xD, 0x0, 0x19)
    OP_1B(0xE, 0x0, 0x1B)
    OP_1B(0x9, 0x0, 0x1D)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_23_D18 end

    def Function_24_168C(): pass

    label("Function_24_168C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1779")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_16FE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B7")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_16BE")

    label("loc_16B7")

    TurnDirection(0x103, 0x0, 400)

    label("loc_16BE")


    ChrTalk(    #42
        0x103,
        (
            "#022FWe don't have much time.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175B")

    label("loc_16FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1714")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_171B")

    label("loc_1714")

    TurnDirection(0x106, 0x0, 400)

    label("loc_171B")


    ChrTalk(    #43
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175B")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_19BD")

    label("loc_1779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18F6")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DD")

    ChrTalk(    #44
        0x101,
        (
            "#1002FWe don't have time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D8")

    label("loc_17DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182E")

    ChrTalk(    #45
        0x109,
        (
            "#1063FWe don't got much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D8")

    label("loc_182E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1887")

    ChrTalk(    #46
        0x103,
        (
            "#022FI don't think we have much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D8")

    label("loc_1887")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D8")

    ChrTalk(    #47
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D8")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_19BD")

    label("loc_18F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19BD")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1954")

    ChrTalk(    #48
        0x101,
        (
            "#1000F...It's pretty late out.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199D")

    label("loc_1954")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_199D")

    ChrTalk(    #49
        0x109,
        (
            "#1060F...Gettin' pretty late.\x01",
            "Let's hurry to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_199D")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_19BD")

    Return()

    # Function_24_168C end

    def Function_25_19BE(): pass

    label("Function_25_19BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A90")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1A30")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E9")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_19F0")

    label("loc_19E9")

    TurnDirection(0x103, 0x0, 400)

    label("loc_19F0")


    ChrTalk(    #50
        0x103,
        (
            "#022FWe don't have much time.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8D")

    label("loc_1A30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A46")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_1A4D")

    label("loc_1A46")

    TurnDirection(0x106, 0x0, 400)

    label("loc_1A4D")


    ChrTalk(    #51
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8D")

    Jump("loc_1C95")

    label("loc_1A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BF2")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF4")

    ChrTalk(    #52
        0x101,
        (
            "#1002FWe don't have time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEF")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B45")

    ChrTalk(    #53
        0x109,
        (
            "#1063FWe don't got much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEF")

    label("loc_1B45")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9E")

    ChrTalk(    #54
        0x103,
        (
            "#022FI don't think we have much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEF")

    label("loc_1B9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BEF")

    ChrTalk(    #55
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEF")

    Jump("loc_1C95")

    label("loc_1BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C95")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4C")

    ChrTalk(    #56
        0x101,
        (
            "#1000F...It's pretty late out.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C95")

    label("loc_1C4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C95")

    ChrTalk(    #57
        0x109,
        (
            "#1060F...Gettin' pretty late.\x01",
            "Let's hurry to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C95")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_25_19BE end

    def Function_26_1CB6(): pass

    label("Function_26_1CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D88")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1D28")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE1")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1CE8")

    label("loc_1CE1")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1CE8")


    ChrTalk(    #58
        0x103,
        (
            "#022FWe don't have much time.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D85")

    label("loc_1D28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3E")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_1D45")

    label("loc_1D3E")

    TurnDirection(0x106, 0x0, 400)

    label("loc_1D45")


    ChrTalk(    #59
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D85")

    Jump("loc_1F8D")

    label("loc_1D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EEA")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DEC")

    ChrTalk(    #60
        0x101,
        (
            "#1002FWe don't have time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE7")

    label("loc_1DEC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3D")

    ChrTalk(    #61
        0x109,
        (
            "#1063FWe don't got much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE7")

    label("loc_1E3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E96")

    ChrTalk(    #62
        0x103,
        (
            "#022FI don't think we have much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE7")

    label("loc_1E96")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE7")

    ChrTalk(    #63
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE7")

    Jump("loc_1F8D")

    label("loc_1EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8D")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F44")

    ChrTalk(    #64
        0x101,
        (
            "#1000F...It's pretty late out.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F8D")

    label("loc_1F44")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8D")

    ChrTalk(    #65
        0x109,
        (
            "#1060F...Gettin' pretty late.\x01",
            "Let's hurry to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8D")

    OP_59()

    def lambda_1F94():
        OP_6D(-3370, 0, 11000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F94)
    Fade(1000)
    SetChrPos(0x0, -3370, 0, 12430, 180)
    SetChrPos(0x1, -3370, 0, 12430, 180)
    SetChrPos(0x2, -3370, 0, 12430, 180)
    SetChrPos(0x143, -3370, 0, 12430, 180)
    OP_0D()
    OP_8C(0x0, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_26_1CB6 end

    def Function_27_2004(): pass

    label("Function_27_2004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20D6")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2076")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202F")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2036")

    label("loc_202F")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2036")


    ChrTalk(    #66
        0x103,
        (
            "#022FWe don't have much time.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D3")

    label("loc_2076")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_208C")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_2093")

    label("loc_208C")

    TurnDirection(0x106, 0x0, 400)

    label("loc_2093")


    ChrTalk(    #67
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D3")

    Jump("loc_22DB")

    label("loc_20D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2238")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213A")

    ChrTalk(    #68
        0x101,
        (
            "#1002FWe don't have time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2235")

    label("loc_213A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218B")

    ChrTalk(    #69
        0x109,
        (
            "#1063FWe don't got much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2235")

    label("loc_218B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E4")

    ChrTalk(    #70
        0x103,
        (
            "#022FI don't think we have much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2235")

    label("loc_21E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2235")

    ChrTalk(    #71
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2235")

    Jump("loc_22DB")

    label("loc_2238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DB")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2292")

    ChrTalk(    #72
        0x101,
        (
            "#1000F...It's pretty late out.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DB")

    label("loc_2292")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22DB")

    ChrTalk(    #73
        0x109,
        (
            "#1060F...Gettin' pretty late.\x01",
            "Let's hurry to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DB")

    OP_59()

    def lambda_22E2():
        OP_6D(3370, 0, 11000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_22E2)
    Fade(1000)
    SetChrPos(0x0, 3370, 0, 12430, 180)
    SetChrPos(0x1, 3370, 0, 12430, 180)
    SetChrPos(0x2, 3370, 0, 12430, 180)
    SetChrPos(0x143, 3370, 0, 12430, 180)
    OP_0D()
    OP_8C(0x0, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_27_2004 end

    def Function_28_2352(): pass

    label("Function_28_2352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2424")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_23C4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_237D")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2384")

    label("loc_237D")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2384")


    ChrTalk(    #74
        0x103,
        (
            "#022FWe don't have much time.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_23C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23DA")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_23E1")

    label("loc_23DA")

    TurnDirection(0x106, 0x0, 400)

    label("loc_23E1")


    ChrTalk(    #75
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the docks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2421")

    Jump("loc_2629")

    label("loc_2424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2586")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2488")

    ChrTalk(    #76
        0x101,
        (
            "#1002FWe don't have time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_2488")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D9")

    ChrTalk(    #77
        0x109,
        (
            "#1063FWe don't got much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_24D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2532")

    ChrTalk(    #78
        0x103,
        (
            "#022FI don't think we have much time.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_2532")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2583")

    ChrTalk(    #79
        0x106,
        (
            "#050FWe ain't got time to waste.\x01",
            "Let's hurry to the West Block.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2583")

    Jump("loc_2629")

    label("loc_2586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2629")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E0")

    ChrTalk(    #80
        0x101,
        (
            "#1000F...It's pretty late out.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2629")

    label("loc_25E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2629")

    ChrTalk(    #81
        0x109,
        (
            "#1060F...Gettin' pretty late.\x01",
            "Let's hurry to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2629")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_28_2352 end

    def Function_29_264A(): pass

    label("Function_29_264A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270D")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A4")

    ChrTalk(    #82
        0x101,
        (
            "#1000F...It's pretty late out.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26ED")

    label("loc_26A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26ED")

    ChrTalk(    #83
        0x109,
        (
            "#1060F...Gettin' pretty late.\x01",
            "Let's hurry to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26ED")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_270D")

    Return()

    # Function_29_264A end

    def Function_30_270E(): pass

    label("Function_30_270E")

    EventBegin(0x0)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_272D")
    Call(0, 34)

    label("loc_272D")

    RemoveParty(0x42, 0xFF)
    RemoveParty(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_274B")
    AddParty(0x2, 0xF7, 0xFF)
    OP_31(0x2, 0x0, 0x38)
    OP_31(0x2, 0xFE, 0x0)
    Jump("loc_2759")

    label("loc_274B")

    AddParty(0x5, 0xF7, 0xFF)
    OP_31(0x5, 0x0, 0x38)
    OP_31(0x5, 0xFE, 0x0)

    label("loc_2759")

    AddParty(0x8, 0xF8, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x109, 0x80)
    OP_6D(8150, 250, -13250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    Sleep(500)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x1F)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x20)
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0x21)
    Sleep(500)

    def lambda_282E():
        OP_6D(5120, 0, -13430, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_282E)
    OP_72(0x1, 0x800)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x10)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    OP_71(0x1, 0x800)

    ChrTalk(    #84
        0x101,
        "#1002F#6PSo where the heck could this tea party BE?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_297F")

    ChrTalk(    #85
        0x106,
        (
            "#053F#4PThe obvious answer would be Grancel Castle.\x02\x03",

            "#050FBut...I dunno, it's got a lot of guards and\x01",
            "is well-fortified.\x02\x03",

            "I think they're gonna start elsewhere this time,\x01",
            "so let's look around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A50")

    label("loc_297F")


    ChrTalk(    #86
        0x103,
        (
            "#026F#4PThe most logical target is Grancel Castle.\x01",
            "However...\x02\x03",

            "#020FIt's well-staffed with guards and fortified.\x02\x03",

            "I think they'll, ah, pour the first cup\x01",
            "somewhere else. We should look\x01",
            "beyond the castle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A50")


    ChrTalk(    #87
        0x109,
        (
            "#1067FProblem is, though...this town is a huge,\x01",
            "crowded place.\x02\x03",

            "We can't just go groping around in the dark.\x01",
            "We'd be lucky to stumble on a single black\x01",
            "helmet.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, -14000, 6000, -18050, 90)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #88
        0x101,
        "#1011F#6PAh!\x02",
    )

    CloseMessageWindow()
    OP_22(0x8C, 0x0, 0x64)
    OP_43(0x8, 0x0, 0x0, 0x2)

    def lambda_2B61():
        OP_6D(-1390, 0, -15440, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B61)

    def lambda_2B79():
        OP_67(0, 12610, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B79)

    def lambda_2B91():
        OP_6B(1940, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B91)

    def lambda_2BA1():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2BA1)

    def lambda_2BB1():
        OP_6E(362, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2BB1)

    def lambda_2BC1():

        label("loc_2BC1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2BC1")

    QueueWorkItem2(0x109, 0, lambda_2BC1)

    def lambda_2BD2():

        label("loc_2BD2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2BD2")

    QueueWorkItem2(0xF7, 0, lambda_2BD2)
    WaitChrThread(0x101, 0x1)
    OP_8E(0x8, 0x0, 0x7D0, 0xFFFFB1E0, 0x2710, 0x0)
    OP_44(0x101, 0x0)

    def lambda_2C00():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C00)

    def lambda_2C0E():
        OP_6D(4980, 0, -13500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C0E)

    def lambda_2C26():
        OP_67(0, 11320, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C26)

    def lambda_2C3E():
        OP_6B(1800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2C3E)
    OP_44(0x109, 0x0)
    OP_97(0x8, 0x7D0, 0xFFFFC180, 0xFFFD8F00, 0x1770, 0x1)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 225, 400)
    OP_44(0xF7, 0x0)

    def lambda_2C7C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2C7C)

    def lambda_2C8A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C8A)
    OP_8F(0x8, 0x10CC, 0x12C, 0xFFFFCA18, 0x3E8, 0x0)
    Fade(500)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x101, 1)

    ChrTalk(    #89
        0x101,
        "#1018F#1PSieg!\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #90
        0x109,
        "#1064FWaaaa-aaaah! What the heck?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(    #91
        0x106,
        "#051F#2PYeah, here we go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D7E")

    label("loc_2D48")


    ChrTalk(    #92
        0x103,
        (
            "#021F#2PAnd now we've got the\x01",
            "perfect assistant!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7E")


    ChrTalk(    #93
        0x8,
        (
            "#310F#2PScreee-screee!\x02\x03",

            "Screeeee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1006F#1PUh, I don't really understand, but...\x02\x03",

            "You want to show us the way to something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        "#311F#2PScreee! ♪\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x8, 4300, 300, -13800, 225)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x8, 0x80)
    OP_0D()
    OP_22(0x8C, 0x0, 0x64)

    def lambda_2E52():
        OP_6D(4980, 2000, -13500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2E52)

    def lambda_2E6A():
        OP_8F(0xFE, 0x1194, 0xFA0, 0xFFFFC950, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2E6A)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0x101, 0x3)
    OP_8C(0x8, 270, 400)
    Sleep(300)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)

    def lambda_2EA5():
        OP_8E(0xFE, 0xFFFFA25E, 0x1770, 0xFFFFB1CC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2EA5)
    Sleep(500)

    def lambda_2EC5():

        label("loc_2EC5")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2EC5")

    QueueWorkItem2(0x101, 0, lambda_2EC5)

    def lambda_2ED6():

        label("loc_2ED6")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2ED6")

    QueueWorkItem2(0x109, 0, lambda_2ED6)

    def lambda_2EE7():

        label("loc_2EE7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2EE7")

    QueueWorkItem2(0xF7, 0, lambda_2EE7)

    def lambda_2EF8():
        OP_6D(-30650, 0, -19610, 5000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_2EF8)

    def lambda_2F10():
        OP_6B(2530, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F10)

    def lambda_2F20():
        OP_6C(279000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2F20)
    WaitChrThread(0x8, 0x2)
    OP_44(0x8, 0x1)
    OP_8E(0x8, 0xFFFF737E, 0x1F40, 0xFFFFB1CC, 0x1770, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x109, 0x0)
    OP_44(0xF7, 0x0)
    SetChrPos(0x101, -15970, 0, -20020, 270)
    SetChrPos(0xF7, -15260, 0, -19020, 270)
    SetChrPos(0x109, -15170, 0, -21220, 270)

    def lambda_2F8C():
        OP_8E(0xFE, 0xFFFF92BE, 0x0, 0xFFFFB1CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F8C)
    Sleep(50)

    def lambda_2FAC():
        OP_8E(0xFE, 0xFFFF9584, 0x0, 0xFFFFB5B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2FAC)
    Sleep(50)

    def lambda_2FCC():
        OP_8E(0xFE, 0xFFFF95DE, 0x0, 0xFFFFAD1C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2FCC)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3024")

    ChrTalk(    #96
        0x106,
        "#555F#2PToward the West Block, eh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3049")

    label("loc_3024")


    ChrTalk(    #97
        0x103,
        "#027F#2PAh, the western blocks.\x02",
    )

    CloseMessageWindow()

    label("loc_3049")


    ChrTalk(    #98
        0x101,
        "#1006F#5PLet's go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x109,
        (
            "#1068F#5POoo-kaaay...\x01",
            "You guys are, uh, kind of amazing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    Sleep(200)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    Fade(1000)
    OP_6D(-27270, 0, -19880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -27970, 0, -20020, 270)
    SetChrPos(0x1, -27970, 0, -20020, 270)
    SetChrPos(0x2, -27970, 0, -20020, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x163A)
    OP_A3(0x10F1)
    OP_1B(0x9, 0xFF, 0xFFFF)
    OP_28(0x8E, 0x4, 0x2)
    OP_28(0x8E, 0x4, 0x8)
    OP_28(0x8E, 0x1, 0x1)
    EventEnd(0x0)
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    Return()

    # Function_30_270E end

    def Function_31_3160(): pass

    label("Function_31_3160")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)

    def lambda_3187():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3187)
    OP_8E(0xFE, 0xF28, 0x0, 0xFFFFCA5E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_31_3160 end

    def Function_32_31AF(): pass

    label("Function_32_31AF")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)

    def lambda_31D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31D6)
    OP_8E(0xFE, 0x1590, 0x28, 0xFFFFC7DE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_32_31AF end

    def Function_33_31FE(): pass

    label("Function_33_31FE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)

    def lambda_3225():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3225)
    OP_8E(0xFE, 0x15AE, 0x0, 0xFFFFCC52, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_33_31FE end

    def Function_34_324D(): pass

    label("Function_34_324D")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_32C6"),
        (1, "loc_32CC"),
        (SWITCH_DEFAULT, "loc_32D2"),
    )


    label("loc_32C6")

    OP_A2(0x1200)
    Jump("loc_32D2")

    label("loc_32CC")

    OP_A2(0x1201)
    Jump("loc_32D2")

    label("loc_32D2")

    Return()

    # Function_34_324D end

    def Function_35_32D3(): pass

    label("Function_35_32D3")

    SetPlaceName(0xB9)
    Return()

    # Function_35_32D3 end

    def Function_36_32D7(): pass

    label("Function_36_32D7")

    SetPlaceName(0xB0)
    Return()

    # Function_36_32D7 end

    def Function_37_32DB(): pass

    label("Function_37_32DB")

    SetPlaceName(0xB2)
    Return()

    # Function_37_32DB end

    def Function_38_32DF(): pass

    label("Function_38_32DF")

    SetPlaceName(0xAE)
    Return()

    # Function_38_32DF end

    def Function_39_32E3(): pass

    label("Function_39_32E3")

    SetPlaceName(0xB3)
    Return()

    # Function_39_32E3 end

    SaveToFile()

Try(main)
