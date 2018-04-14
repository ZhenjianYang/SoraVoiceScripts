from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4401   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4401.x',
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
        '丹克',                                 # 9
        '歌德',                                 # 10
        '罗布',                                 # 11
        '工人',                                 # 12
        '工人',                                 # 13
        '工人',                                 # 14
        '工人',                                 # 15
        '工人',                                 # 16
        '工人',                                 # 17
        '围观者',                               # 18
        '围观者',                               # 19
        '围观者',                               # 20
        '围观者',                               # 21
        '围观者',                               # 22
        '围观者',                               # 23
        '围观者',                               # 24
        '围观者',                               # 25
        '围观者',                               # 26
        '王都格兰赛尔·码头南',                 # 27
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
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH01530 ._CH',             # 01
        'ED6_DT07/CH01450 ._CH',             # 02
        'ED6_DT07/CH01530 ._CH',             # 03
        'ED6_DT07/CH01500 ._CH',             # 04
        'ED6_DT07/CH01500 ._CH',             # 05
        'ED6_DT07/CH01500 ._CH',             # 06
        'ED6_DT07/CH01530 ._CH',             # 07
        'ED6_DT07/CH01550 ._CH',             # 08
        'ED6_DT07/CH01200 ._CH',             # 09
        'ED6_DT07/CH01690 ._CH',             # 0A
        'ED6_DT07/CH01000 ._CH',             # 0B
        'ED6_DT07/CH01130 ._CH',             # 0C
        'ED6_DT07/CH01140 ._CH',             # 0D
        'ED6_DT07/CH01150 ._CH',             # 0E
        'ED6_DT07/CH01020 ._CH',             # 0F
        'ED6_DT07/CH01030 ._CH',             # 10
        'ED6_DT07/CH01170 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH01530P._CP',             # 01
        'ED6_DT07/CH01450P._CP',             # 02
        'ED6_DT07/CH01530P._CP',             # 03
        'ED6_DT07/CH01500P._CP',             # 04
        'ED6_DT07/CH01500P._CP',             # 05
        'ED6_DT07/CH01500P._CP',             # 06
        'ED6_DT07/CH01530P._CP',             # 07
        'ED6_DT07/CH01550P._CP',             # 08
        'ED6_DT07/CH01200P._CP',             # 09
        'ED6_DT07/CH01690P._CP',             # 0A
        'ED6_DT07/CH01000P._CP',             # 0B
        'ED6_DT07/CH01130P._CP',             # 0C
        'ED6_DT07/CH01140P._CP',             # 0D
        'ED6_DT07/CH01150P._CP',             # 0E
        'ED6_DT07/CH01020P._CP',             # 0F
        'ED6_DT07/CH01030P._CP',             # 10
        'ED6_DT07/CH01170P._CP',             # 11
    )

    DeclNpc(
        X                   = 4280,
        Z                   = 1500,
        Y                   = 93750,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 14220,
        Z                   = 0,
        Y                   = 57490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 14850,
        Z                   = 0,
        Y                   = 104990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -3760,
        Z                   = 0,
        Y                   = 30260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 45200,
        Z                   = 0,
        Y                   = 48610,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -5140,
        Z                   = 0,
        Y                   = 76620,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -6530,
        Z                   = 0,
        Y                   = 109060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 2760,
        Z                   = 5500,
        Y                   = 110270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 3210,
        Z                   = 1500,
        Y                   = 106100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -14940,
        Z                   = 0,
        Y                   = 109290,
        Direction           = 331,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -16290,
        Z                   = 0,
        Y                   = 109480,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 13900,
        Z                   = 0,
        Y                   = 123350,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 17930,
        Z                   = 0,
        Y                   = 122800,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 22520,
        Z                   = 0,
        Y                   = 123430,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -19490,
        Z                   = 0,
        Y                   = 106510,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -13780,
        Z                   = 0,
        Y                   = 109360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -12350,
        Z                   = 0,
        Y                   = 109360,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 23190,
        Z                   = 0,
        Y                   = 120570,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -880,
        Z                   = 0,
        Y                   = -32689,
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


    DeclActor(
        TriggerX            = 40210,
        TriggerZ            = 800,
        TriggerY            = 54960,
        TriggerRange        = 800,
        ActorX              = 40410,
        ActorZ              = 2200,
        ActorY              = 54960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3110,
        TriggerZ            = 2450,
        TriggerY            = 121430,
        TriggerRange        = 1000,
        ActorX              = 3230,
        ActorZ              = -1500,
        ActorY              = 127300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19490,
        TriggerZ            = 0,
        TriggerY            = 109370,
        TriggerRange        = 1700,
        ActorX              = -19490,
        ActorZ              = 0,
        ActorY              = 109370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_406",          # 00, 0
        "Function_1_669",          # 01, 1
        "Function_2_6B6",          # 02, 2
        "Function_3_833",          # 03, 3
        "Function_4_857",          # 04, 4
        "Function_5_E95",          # 05, 5
        "Function_6_139E",         # 06, 6
        "Function_7_1899",         # 07, 7
        "Function_8_1A26",         # 08, 8
        "Function_9_1C50",         # 09, 9
        "Function_10_1DBB",        # 0A, 10
        "Function_11_1F1E",        # 0B, 11
        "Function_12_2066",        # 0C, 12
        "Function_13_21D3",        # 0D, 13
        "Function_14_221F",        # 0E, 14
        "Function_15_22AA",        # 0F, 15
        "Function_16_2362",        # 10, 16
        "Function_17_2419",        # 11, 17
        "Function_18_2571",        # 12, 18
        "Function_19_2629",        # 13, 19
        "Function_20_271A",        # 14, 20
        "Function_21_288E",        # 15, 21
        "Function_22_2928",        # 16, 22
        "Function_23_2949",        # 17, 23
        "Function_24_29C7",        # 18, 24
        "Function_25_2A11",        # 19, 25
        "Function_26_2AFC",        # 1A, 26
    )


    def Function_0_406(): pass

    label("Function_0_406")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_461")
    SetChrPos(0xA, 18510, 0, 111750, 320)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x18, 0x10)

    label("loc_461")

    Jump("loc_668")

    label("loc_464")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_47A")
    Jump("loc_668")

    label("loc_47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4DC")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, 13720, 0, 54670, 18)
    SetChrPos(0x12, 9200, 0, 81310, 348)
    SetChrPos(0x13, 23080, 0, 91150, 85)
    SetChrPos(0x14, 12070, 0, 38910, 281)
    Jump("loc_668")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_567")
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x15, -22340, 0, 78050, 271)
    SetChrPos(0x16, 19180, 0, 114150, 252)
    SetChrPos(0x17, 18930, 0, 113030, 217)
    SetChrPos(0x18, -29540, 0, 75460, 360)
    SetChrPos(0x19, -29540, 0, 76300, 180)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x19, 0x10)
    Jump("loc_668")

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5E9")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x15, -12470, 0, 82840, 332)
    SetChrPos(0x16, 19180, 0, 114150, 252)
    SetChrPos(0x17, 18930, 0, 113030, 217)
    SetChrPos(0x18, 26840, 0, 72510, 179)
    SetChrPos(0x19, 27510, 0, 60850, 12)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x19, 0x10)
    Jump("loc_668")

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_668")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x15, -12470, 0, 82840, 332)
    SetChrPos(0x16, 19180, 0, 114150, 252)
    SetChrPos(0x17, 18930, 0, 113030, 217)
    SetChrPos(0x18, 26170, 0, 60420, 37)
    SetChrPos(0x19, -1210, 0, 67700, 180)

    label("loc_668")

    Return()

    # Function_0_406 end

    def Function_1_669(): pass

    label("Function_1_669")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFEE2D8, 0x23006E)
    OP_22(0x1C5, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A0")
    OP_B1("t4401_y")
    Jump("loc_6A9")

    label("loc_6A0")

    OP_B1("t4401_n")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B5")
    OP_64(0x2, 0x1)

    label("loc_6B5")

    Return()

    # Function_1_669 end

    def Function_2_6B6(): pass

    label("Function_2_6B6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DB")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_81D")

    label("loc_6DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F4")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_81D")

    label("loc_6F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70D")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_81D")

    label("loc_70D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_726")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_81D")

    label("loc_726")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73F")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_81D")

    label("loc_73F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_758")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_81D")

    label("loc_758")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_771")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_81D")

    label("loc_771")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_81D")

    label("loc_78A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A3")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_81D")

    label("loc_7A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BC")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_81D")

    label("loc_7BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D5")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_81D")

    label("loc_7D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EE")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_81D")

    label("loc_7EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_807")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_81D")

    label("loc_807")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81D")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_81D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_832")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_81D")

    label("loc_832")

    Return()

    # Function_2_6B6 end

    def Function_3_833(): pass

    label("Function_3_833")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_856")
    OP_8D(0xFE, 21480, 122570, 23470, 120150, 2000)
    Jump("Function_3_833")

    label("loc_856")

    Return()

    # Function_3_833 end

    def Function_4_857(): pass

    label("Function_4_857")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8BF")

    ChrTalk(    #0
        0xFE,
        (
            "导力停止之后，\x01",
            "船不来也没法工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "这下坦白说\x01",
            "真是束手无策啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_960")

    label("loc_8BF")


    ChrTalk(    #2
        0xFE,
        (
            "来参观那个螺一样的物体\x01",
            "的人越来越多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "要是平时会阻碍工作\x01",
            "会把他们赶走……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "导力停止之后，\x01",
            "船不来也没法工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "这下坦白说\x01",
            "真是束手无策啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_960")

    Jump("loc_E91")

    label("loc_963")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_A96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 3)), scpexpr(EXPR_END)), "loc_9DE")

    ChrTalk(    #6
        0xFE,
        (
            "偷走引擎的家伙们，\x01",
            "企图做什么不得了的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "如果你们没来，\x01",
            "现在还不知道会变成怎样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A93")

    label("loc_9DE")


    ChrTalk(    #8
        0xFE,
        (
            "哦，你们不是\x01",
            "那天晚上的游击士吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "偷走引擎的家伙们，\x01",
            "企图做什么不得了的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "如果你们没来，\x01",
            "现在还不知道会变成怎样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "不管怎样，谢谢你们了。\x01",
            "让我再次道谢吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1653)

    label("loc_A93")

    Jump("loc_E91")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AF3")

    ChrTalk(    #12
        0xFE,
        (
            "诺曼新市长\x01",
            "也不会对港口使坏的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "致力于旅游事业\x01",
            "我想是很不错的啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAF")

    label("loc_AF3")


    ChrTalk(    #14
        0xFE,
        (
            "看来卢安的市长\x01",
            "决定是诺曼氏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "我们是觉得，参与港湾事业\x01",
            "的波尔多斯氏当选\x01",
            "会有更多利益……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "不过诺曼氏也不会\x01",
            "完全不考虑港口的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "嗯，暂时用温和的目光\x01",
            "观察一下情况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_BAF")

    Jump("loc_E91")

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C0F")

    ChrTalk(    #18
        0xFE,
        (
            "对了对了，卢安\x01",
            "正在举行市长选举呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "卢安市民到底\x01",
            "会选哪边呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB6")

    label("loc_C0F")


    ChrTalk(    #20
        0xFE,
        (
            "对了对了，卢安\x01",
            "正在举行市长选举呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "卢安市民到底\x01",
            "会选哪边呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "因为同样在港口工作\x01",
            "很想支援波尔多斯氏……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "不过候选人诺曼氏\x01",
            "说的话也很有说服力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_CB6")

    Jump("loc_E91")

    label("loc_CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_DAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D23")

    ChrTalk(    #24
        0xFE,
        (
            "解决了１个问题\x01",
            "后面的问题又紧接而来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "工作就是这样反复不断,\x01",
            "总是无法随人愿啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAC")

    label("loc_D23")


    ChrTalk(    #26
        0xFE,
        (
            "解决了１个问题\x01",
            "后面的问题又紧接而来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "工作就是这样反复不断,\x01",
            "总是无法随人愿啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "正因如此，有费心的价值\x01",
            "才有趣也说不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_DAC")

    Jump("loc_E91")

    label("loc_DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E0A")

    ChrTalk(    #29
        0xFE,
        (
            "因为卢安市长不在\x01",
            "船的通过审查推迟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "害得我们的工作\x01",
            "好难计划。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E91")

    label("loc_E0A")


    ChrTalk(    #31
        0xFE,
        (
            "王都进港的船全部\x01",
            "都要通过卢安的卢比诺川\x01",
            "才能过来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "因为卢安市长不在\x01",
            "船的通过审查推迟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "害得我们的工作\x01",
            "好难计划。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E91")

    TalkEnd(0x8)
    Return()

    # Function_4_857 end

    def Function_5_E95(): pass

    label("Function_5_E95")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F03")

    ChrTalk(    #34
        0xFE,
        (
            "自从导力船被导入后\x01",
            "也没造过帆船之类的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "哈……\x01",
            "不能想点办法吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F80")

    label("loc_F03")


    ChrTalk(    #36
        0xFE,
        (
            "我们的工作\x01",
            "要是没有船\x01",
            "就根本没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "自从导力船被导入后\x01",
            "也没造过帆船之类的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "哈……\x01",
            "不能想点办法吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F80")

    Jump("loc_139A")

    label("loc_F83")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FF1")

    ChrTalk(    #39
        0xFE,
        (
            "被破坏的仓库门\x01",
            "和港口设施似乎会有补偿金。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "国家的对应够快真是帮大忙了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1065")

    label("loc_FF1")


    ChrTalk(    #41
        0xFE,
        (
            "仓库的借主好像\x01",
            "是情报部的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "难道保管了\x01",
            "开发中的导力战车之类的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "大吃一惊眼珠子\x01",
            "都差点跳出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1065")

    Jump("loc_139A")

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_113B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10BF")

    ChrTalk(    #44
        0xFE,
        (
            "和借仓库的人\x01",
            "联络不上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "差不多该进行\x01",
            "更新合同的手续了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1138")

    label("loc_10BF")


    ChrTalk(    #46
        0xFE,
        (
            "半年前开始\x01",
            "就有人借了\x01",
            "里头的仓库。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "使用费是预付的\x01",
            "倒是没有问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "不知为何，这数个月间，\x01",
            "联络不上啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1138")

    Jump("loc_139A")

    label("loc_113B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11AB")

    ChrTalk(    #49
        0xFE,
        "……已经完全到傍晚了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "埋头工作总让人感觉\x01",
            "时间过得真快啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "我就这样\x01",
            "慢慢老了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139A")

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_12C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_120C")

    ChrTalk(    #52
        0xFE,
        (
            "仓库空着\x01",
            "就只是浪费维修费而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "所以大家商量着\x01",
            "开始了借出仓库的业务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C1")

    label("loc_120C")


    ChrTalk(    #54
        0xFE,
        (
            "最近物资的搬运\x01",
            "也用飞船进行了,\x01",
            "空空的仓库很受欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "仓库空着\x01",
            "就只是浪费维修费而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "所以大家商量着\x01",
            "开始了借出仓库的业务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "不用说普通人，连王国军\x01",
            "也来借了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_12C1")

    Jump("loc_139A")

    label("loc_12C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_139A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_131B")

    ChrTalk(    #58
        0xFE,
        (
            "港口营运重开之后\x01",
            "那个忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "真正安定下来，\x01",
            "还是这几天以后。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139A")

    label("loc_131B")


    ChrTalk(    #60
        0xFE,
        (
            "政变的时候，这个港口\x01",
            "被情报部封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "结果为了卸货\x01",
            "进港的船\x01",
            "要在湖上等好几天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "港口营运重开之后\x01",
            "那个忙啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_139A")

    TalkEnd(0x9)
    Return()

    # Function_5_E95 end

    def Function_6_139E(): pass

    label("Function_6_139E")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_143B")

    ChrTalk(    #63
        0xFE,
        (
            "港口跃出的黑色巨人，\x01",
            "出现在柏斯的古代龙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "就算再出来什么\x01",
            "我都不会再惊讶了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "什么啊，那是……\x01",
            "出来那么奇怪的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143B")

    Jump("loc_1895")

    label("loc_143E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_14B1")

    ChrTalk(    #66
        0xFE,
        (
            "那天夜晚，港口飞起的\x01",
            "巨大黑影我确实看到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "好像是人的样子，\x01",
            "到底那是什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1533")

    label("loc_14B1")


    ChrTalk(    #68
        0xFE,
        (
            "那天夜晚，港口飞起的\x01",
            "巨大黑影我确实看到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "好像是人的样子，\x01",
            "到底那是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "还以为是看错了，\x01",
            "但军队也骚动不断。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1533")

    Jump("loc_1895")

    label("loc_1536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1655")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_15A6")

    ChrTalk(    #71
        0xFE,
        (
            "因为晕船\x01",
            "有些人说不喜欢船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "要我说的话，\x01",
            "不知何时会落下的\x01",
            "浮在空中的东西更加讨厌。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1652")

    label("loc_15A6")


    ChrTalk(    #73
        0xFE,
        (
            "因为晕船\x01",
            "有些人说不喜欢船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "要我说的话，\x01",
            "不知何时会落下的\x01",
            "浮在空中的东西更加讨厌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "船又不会坠落\x01",
            "比飞船安全多了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "……嗯，虽然也有\x01",
            "沉没的可能性。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1652")

    Jump("loc_1895")

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_172F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_16BF")

    ChrTalk(    #77
        0xFE,
        (
            "要说船和飞船，\x01",
            "我还是会毫不犹豫地选船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "要问为什么，我是属于大海的男人嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_172C")

    label("loc_16BF")


    ChrTalk(    #79
        0xFE,
        "浮在夕照海面的船……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "还有那前面\x01",
            "毅然伫立的我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "怎样，属于大海的男人\x01",
            "那种哀愁感受得到吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_172C")

    Jump("loc_1895")

    label("loc_172F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1845")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_17AB")

    ChrTalk(    #82
        0xFE,
        (
            "飞船确实很便利，\x01",
            "不过以现在的性能\x01",
            "能堆积的货物也很有限。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "要是大型货物的搬运\x01",
            "现在船也是很重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1842")

    label("loc_17AB")


    ChrTalk(    #84
        0xFE,
        (
            "船的优点怎么说\x01",
            "都是货物的装载量嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "飞船确实很便利，\x01",
            "不过以现在的性能\x01",
            "能堆积的货物也很有限。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "要是大型货物的搬运\x01",
            "现在船也是很重要的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1842")

    Jump("loc_1895")

    label("loc_1845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1895")

    ChrTalk(    #87
        0xFE,
        "嗯～还是船好～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "在大海上驰骋的浪漫\x01",
            "只有属于海的男人才能品味啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1895")

    TalkEnd(0xA)
    Return()

    # Function_6_139E end

    def Function_7_1899(): pass

    label("Function_7_1899")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_18F7")

    ChrTalk(    #89
        0xFE,
        (
            "嗯啊？　对了，你们也是\x01",
            "来参观那个的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "去到码头\x01",
            "就能看到啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F7")

    Jump("loc_1A22")

    label("loc_18FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1910")
    Jump("loc_1A22")

    label("loc_1910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_195B")

    ChrTalk(    #91
        0xFE,
        "嗯啊？　白衣服的女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "不，那样的孩子\x01",
            "没来过这里哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A22")

    label("loc_195B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19B9")

    ChrTalk(    #93
        0xFE,
        (
            "嗯啊？　这种时候\x01",
            "到底怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "差不多工作也快结束了。\x01",
            "赶快回家回家！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A22")

    label("loc_19B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_19DE")

    ChrTalk(    #95
        0xFE,
        (
            "嗯……\x01",
            "今天真是累啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A22")

    label("loc_19DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1A22")

    ChrTalk(    #96
        0xFE,
        "啊？有事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "要是出租仓库的合同\x01",
            "得先通过事务所哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A22")

    TalkEnd(0xFE)
    Return()

    # Function_7_1899 end

    def Function_8_1A26(): pass

    label("Function_8_1A26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A8A")

    ChrTalk(    #98
        0xFE,
        (
            "呼，到底怎么回事。\x01",
            "那是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "反正也不能工作，\x01",
            "就在这里平静一下心情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8A")

    Jump("loc_1C4C")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1AA3")
    Jump("loc_1C4C")

    label("loc_1AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1ACD")

    ChrTalk(    #100
        0xFE,
        "好，差不多该回去工作了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C4C")

    label("loc_1ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B0C")

    ChrTalk(    #101
        0xFE,
        "呼，出汗了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "真想就这样\x01",
            "跳进湖里啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4C")

    label("loc_1B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1B57")

    ChrTalk(    #103
        0xFE,
        (
            "不开心的时候\x01",
            "来到这里就镇定了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "你也有这样的地方吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C4C")

    label("loc_1B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1BA7")

    ChrTalk(    #105
        0xFE,
        "不、不是偷懒哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "是为了防范可疑的人\x01",
            "而在、在巡逻啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4C")

    label("loc_1BA7")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 300)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0x1388)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #107
        0xFE,
        "你、你们，是什么人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "不、不是偷懒哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "是为了防范可疑的人\x01",
            "而在、在巡逻啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1C4C")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A26 end

    def Function_9_1C50(): pass

    label("Function_9_1C50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CB4")

    ChrTalk(    #110
        0xFE,
        (
            "港口营运终于上了轨道\x01",
            "却在这时出这麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "空之女神\x01",
            "弃我们不顾了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB4")

    Jump("loc_1DB7")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1CCD")
    Jump("loc_1DB7")

    label("loc_1CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1CF3")

    ChrTalk(    #112
        0xFE,
        "今天的便当吃什么呢～⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DB7")

    label("loc_1CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D28")

    ChrTalk(    #113
        0xFE,
        (
            "好，还有一点\x01",
            "今天的工作也完成了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB7")

    label("loc_1D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1D69")

    ChrTalk(    #114
        0xFE,
        (
            "呜呜……肚子好涨………\x01",
            "中午的便当吃１个就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB7")

    label("loc_1D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1DB7")

    ChrTalk(    #115
        0xFE,
        "难道是来港口参观的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "到处转转看看是可以，\x01",
            "可别妨碍工作哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB7")

    TalkEnd(0xFE)
    Return()

    # Function_9_1C50 end

    def Function_10_1DBB(): pass

    label("Function_10_1DBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1E16")

    ChrTalk(    #117
        0xFE,
        (
            "搬运车也不能用，\x01",
            "重要的船也动不了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "到底我们做错了什么？\x02",
    )

    CloseMessageWindow()

    label("loc_1E16")

    Jump("loc_1F1A")

    label("loc_1E19")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1E2F")
    Jump("loc_1F1A")

    label("loc_1E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1E6C")

    ChrTalk(    #119
        0xFE,
        (
            "嘿嘿，今天也是个令人陶醉\x01",
            "适合工作的好天气啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F1A")

    label("loc_1E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E98")

    ChrTalk(    #120
        0xFE,
        "呼～今天也出了一身汗啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F1A")

    label("loc_1E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1EE4")

    ChrTalk(    #121
        0xFE,
        (
            "我们的工作\x01",
            "全年都得站着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "没有结实的腰腿\x01",
            "可没法胜任哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F1A")

    label("loc_1EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1F1A")

    ChrTalk(    #123
        0xFE,
        (
            "竟然来到这么深处的地方。\x01",
            "来看我们工作吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1A")

    TalkEnd(0xFE)
    Return()

    # Function_10_1DBB end

    def Function_11_1F1E(): pass

    label("Function_11_1F1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1F58")

    ChrTalk(    #124
        0xFE,
        "这个状况要持续到什么时候啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1F58")

    Jump("loc_2062")

    label("loc_1F5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2062")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1F71")
    Jump("loc_2062")

    label("loc_1F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1F9C")

    ChrTalk(    #125
        0xFE,
        (
            "嗯～湖上\x01",
            "吹来好凉爽的风啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2062")

    label("loc_1F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FCF")

    ChrTalk(    #126
        0xFE,
        (
            "真想向着那夕阳\x01",
            "让船飞驰而去……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2062")

    label("loc_1FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2020")

    ChrTalk(    #127
        0xFE,
        "我可喜欢这个工作岗位了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "因为全年都能\x01",
            "看到这个瓦雷利亚湖啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2062")

    label("loc_2020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2062")

    ChrTalk(    #129
        0xFE,
        (
            "这蓝天多么赏心悦目。\x01",
            "今天也能清楚地看到古罗尼峰峦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2062")

    TalkEnd(0xFE)
    Return()

    # Function_11_1F1E end

    def Function_12_2066(): pass

    label("Function_12_2066")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20B5")

    ChrTalk(    #130
        0xFE,
        (
            "没想到导力器\x01",
            "都动不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "……唉，真担心未来。\x02",
    )

    CloseMessageWindow()

    label("loc_20B5")

    Jump("loc_21CF")

    label("loc_20B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_20CE")
    Jump("loc_21CF")

    label("loc_20CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_20FD")

    ChrTalk(    #132
        0xFE,
        (
            "哈哈哈，今天\x01",
            "船的情形也非常好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_20FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2140")

    ChrTalk(    #133
        0xFE,
        (
            "黄昏之时真不可思议……\x01",
            "不知为何心情会变得难过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_2140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2191")

    ChrTalk(    #134
        0xFE,
        "这艘船何时都非常精神哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "因为是我倾注深情\x01",
            "整备出来的东西嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_2191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_21CF")

    ChrTalk(    #136
        0xFE,
        "是来参观导力船的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "呵呵，好啊。\x01",
            "尽情地看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CF")

    TalkEnd(0xFE)
    Return()

    # Function_12_2066 end

    def Function_13_21D3(): pass

    label("Function_13_21D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2203")

    ChrTalk(    #138
        0xFE,
        (
            "唔唔，越看越觉得\x01",
            "不可思议啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_221B")

    label("loc_2203")


    ChrTalk(    #139
        0xFE,
        "哦哦，好多货物啊。\x02",
    )

    CloseMessageWindow()

    label("loc_221B")

    TalkEnd(0xFE)
    Return()

    # Function_13_21D3 end

    def Function_14_221F(): pass

    label("Function_14_221F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2271")

    ChrTalk(    #140
        0xFE,
        "想想真是不可思议啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "导力又不能使用\x01",
            "那个到底怎么浮起来？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A6")

    label("loc_2271")


    ChrTalk(    #142
        0xFE,
        (
            "导力船也相当有震撼力呢。\x01",
            "要是带了照相机就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A6")

    TalkEnd(0xFE)
    Return()

    # Function_14_221F end

    def Function_15_22AA(): pass

    label("Function_15_22AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2339")

    ChrTalk(    #143
        0xFE,
        (
            "我活了这么久，\x01",
            "看过各种各样的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "那样不可思议的东西\x01",
            "还是第一次见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "由于那个而\x01",
            "不能使用导力器\x01",
            "的传闻是真的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235E")

    label("loc_2339")


    ChrTalk(    #146
        0xFE,
        (
            "哎呀，王都的美丽\x01",
            "可喻为珍珠呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235E")

    TalkEnd(0xFE)
    Return()

    # Function_15_22AA end

    def Function_16_2362(): pass

    label("Function_16_2362")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_23EE")

    ChrTalk(    #147
        0xFE,
        (
            "那个物体出现之后\x01",
            "导力器就一齐停了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "亲卫队不能用『埃尔赛尤』\x01",
            "把它击落吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "唔，『埃尔赛尤』\x01",
            "一定也动不了了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_23EE")


    ChrTalk(    #150
        0xFE,
        (
            "哦……确实是\x01",
            "气氛不错的仓库街呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2415")

    TalkEnd(0xFE)
    Return()

    # Function_16_2362 end

    def Function_17_2419(): pass

    label("Function_17_2419")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_246F")

    ChrTalk(    #151
        0xFE,
        "我，我什么都看不见！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "那样奇怪又令人毛骨悚然\x01",
            "的东西我才不相信！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256D")

    label("loc_246F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2479")
    Jump("loc_256D")

    label("loc_2479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24D5")

    ChrTalk(    #153
        0xFE,
        (
            "哦哦，那对亲子\x01",
            "不觉得是很棒的画面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "不知道为什么，\x01",
            "都快流眼泪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256D")

    label("loc_24D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_252E")

    ChrTalk(    #155
        0xFE,
        (
            "只是这样待在这里\x01",
            "就能感觉到成为属于海的男人的心情哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "怎样，有效吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_256D")

    label("loc_252E")


    ChrTalk(    #157
        0xFE,
        "港口气氛真好啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "如果要向她告白\x01",
            "真希望能在这种地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256D")

    TalkEnd(0xFE)
    Return()

    # Function_17_2419 end

    def Function_18_2571(): pass

    label("Function_18_2571")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_259B")

    ChrTalk(    #159
        0xFE,
        (
            "今天更加\x01",
            "看得清楚了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2625")

    label("loc_259B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_25A5")
    Jump("loc_2625")

    label("loc_25A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25CF")

    ChrTalk(    #160
        0xFE,
        "哇啊，好漂亮的景色啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2625")

    label("loc_25CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2606")

    ChrTalk(    #161
        0xFE,
        (
            "飞船也不错，\x01",
            "但船也相当令人心情舒畅呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2625")

    label("loc_2606")


    ChrTalk(    #162
        0xFE,
        (
            "船上能装\x01",
            "这么多货物啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2625")

    TalkEnd(0xFE)
    Return()

    # Function_18_2571 end

    def Function_19_2629(): pass

    label("Function_19_2629")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_266A")

    ChrTalk(    #163
        0xFE,
        "别、别说这么可怕的事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "你、你说谁在乘！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2716")

    label("loc_266A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2674")
    Jump("loc_2716")

    label("loc_2674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26A0")

    ChrTalk(    #165
        0xFE,
        "嗬，这真是漂亮的晚霞啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2716")

    label("loc_26A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_26DD")

    ChrTalk(    #166
        0xFE,
        (
            "话说回来拂过瓦雷利亚湖\x01",
            "的风真令人心情舒畅啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2716")

    label("loc_26DD")


    ChrTalk(    #167
        0xFE,
        "嗬，导力船吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "真是惭愧，\x01",
            "我还是第一次看到。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2716")

    TalkEnd(0xFE)
    Return()

    # Function_19_2629 end

    def Function_20_271A(): pass

    label("Function_20_271A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2742")

    ChrTalk(    #169
        0xFE,
        (
            "那里面\x01",
            "是谁在乘坐呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288A")

    label("loc_2742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_274C")
    Jump("loc_288A")

    label("loc_274C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_278A")

    ChrTalk(    #170
        0xFE,
        "啊啊，总算碰到你了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "再也不分开了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_288A")

    label("loc_278A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_27EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_27BC")

    ChrTalk(    #172
        0xFE,
        (
            "为什么港口会有\x01",
            "这种装置……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E8")

    label("loc_27BC")


    ChrTalk(    #173
        0xFE,
        (
            "我现在就去那边\x01",
            "待在那里别动──哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_27E8")

    Jump("loc_288A")

    label("loc_27EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_280D")

    ChrTalk(    #174
        0xFE,
        "我、我女儿去哪里？\x02",
    )

    CloseMessageWindow()
    Jump("loc_288A")

    label("loc_280D")


    ChrTalk(    #175
        0xFE,
        (
            "这个砖瓦仓库\x01",
            "气氛真好啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #176
        0xFE,
        "哎呀……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #177
        0xFE,
        "我、我女儿去哪里？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_288A")

    TalkEnd(0xFE)
    Return()

    # Function_20_271A end

    def Function_21_288E(): pass

    label("Function_21_288E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28B6")

    ChrTalk(    #178
        0xFE,
        "好大的贝壳在飞～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_2924")

    label("loc_28B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_28C0")
    Jump("loc_2924")

    label("loc_28C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E2")

    ChrTalk(    #179
        0xFE,
        "呜哇～妈妈～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2924")

    label("loc_28E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_290A")

    ChrTalk(    #180
        0xFE,
        "妈妈～！我在这里哦～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2924")

    label("loc_290A")


    ChrTalk(    #181
        0xFE,
        "妈妈～！你在哪里～？\x02",
    )

    CloseMessageWindow()

    label("loc_2924")

    TalkEnd(0xFE)
    Return()

    # Function_21_288E end

    def Function_22_2928(): pass

    label("Function_22_2928")

    TalkBegin(0xFE)

    ChrTalk(    #182
        0xFE,
        "消息未作成 给根田确认\x02",
    )

    TalkEnd(0xFE)
    Return()

    # Function_22_2928 end

    def Function_23_2949(): pass

    label("Function_23_2949")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2960")
    OP_6F(0x4, 0)
    OP_A3(0x0)
    Jump("loc_29C3")

    label("loc_2960")

    OP_A2(0x0)
    LoadEffect(0x0, "map\\\\snddst1.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 15080, 0, 56290, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x1E)
    OP_CA(0x4, 0x1, 0x1F4)
    OP_73(0x4)

    label("loc_29C3")

    TalkEnd(0xFF)
    Return()

    # Function_23_2949 end

    def Function_24_29C7(): pass

    label("Function_24_29C7")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #183
        "\x07\x05门紧紧地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_29C7 end

    def Function_25_2A11(): pass

    label("Function_25_2A11")

    EventBegin(0x1)

    ChrTalk(    #184
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_2A3D():
        OP_6D(3250, 0, 123500, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2A3D)

    def lambda_2A55():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2A55)

    def lambda_2A65():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2A65)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #185
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AEC")
    OP_C0(0xE, 0x2C, 0xC6C, 0x992, 0x1DA88, 0x0, 0xC9E, 0xFFFFF8F8, 0x1F144)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_2AFB")

    label("loc_2AEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AFB")
    EventEnd(0x1)

    label("loc_2AFB")

    Return()

    # Function_25_2A11 end

    def Function_26_2AFC(): pass

    label("Function_26_2AFC")

    OP_8C(0x0, 315, 0)
    OP_8C(0x1, 315, 0)
    OP_8C(0x2, 315, 0)
    OP_8C(0x3, 315, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400CE, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_26_2AFC end

    SaveToFile()

Try(main)
