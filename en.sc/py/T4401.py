from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Duncan',                               # 9
        'Gotti',                                # 10
        'Rob',                                  # 11
        'Worker',                               # 12
        'Worker',                               # 13
        'Worker',                               # 14
        'Worker',                               # 15
        'Worker',                               # 16
        'Worker',                               # 17
        'Sightseer',                            # 18
        'Sightseer',                            # 19
        'Sightseer',                            # 20
        'Sightseer',                            # 21
        'Sightseer',                            # 22
        'Sightseer',                            # 23
        'Sightseer',                            # 24
        'Sightseer',                            # 25
        'Sightseer',                            # 26
        'Grancel - S Warehouse District',       # 27
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
        "Function_5_129B",         # 05, 5
        "Function_6_1B7A",         # 06, 6
        "Function_7_23BD",         # 07, 7
        "Function_8_2593",         # 08, 8
        "Function_9_2885",         # 09, 9
        "Function_10_2A7B",        # 0A, 10
        "Function_11_2C33",        # 0B, 11
        "Function_12_2DF2",        # 0C, 12
        "Function_13_3009",        # 0D, 13
        "Function_14_3079",        # 0E, 14
        "Function_15_3140",        # 0F, 15
        "Function_16_323A",        # 10, 16
        "Function_17_333F",        # 11, 17
        "Function_18_3549",        # 12, 18
        "Function_19_3669",        # 13, 19
        "Function_20_379E",        # 14, 20
        "Function_21_39AC",        # 15, 21
        "Function_22_3A4E",        # 16, 22
        "Function_23_3A76",        # 17, 23
        "Function_24_3AF4",        # 18, 24
        "Function_25_3B4B",        # 19, 25
        "Function_26_3C55",        # 1A, 26
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8FD")

    ChrTalk(    #0
        0xFE,
        (
            "With orbal energy stopped,\x01",
            "no ships are coming, so there's\x01",
            "no work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Honestly, standing around's\x01",
            "pretty much all you can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0B")

    label("loc_8FD")


    ChrTalk(    #2
        0xFE,
        (
            "More people are coming to\x01",
            "see that weird floating thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I'd normally kick 'em out for\x01",
            "getting in the way of work,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "With orbal energy stopped,\x01",
            "no ships are coming, so there\x01",
            "IS no work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Honestly, standing around's\x01",
            "pretty much all you can do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A0B")

    Jump("loc_1297")

    label("loc_A0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1297")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 3)), scpexpr(EXPR_END)), "loc_AB9")

    ChrTalk(    #6
        0xFE,
        (
            "My gut tells me those guys\x01",
            "who stole the engine were up\x01",
            "to something nasty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "If you hadn't come, who knows\x01",
            "what would've happened...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA0")

    label("loc_AB9")


    ChrTalk(    #8
        0xFE,
        (
            "Oh, you're those bracers\x01",
            "from before! Hey there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "My gut tells me those guys\x01",
            "who stole the engine were up\x01",
            "to something nasty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "If you hadn't come, who knows\x01",
            "what would've happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "Anyway, thanks. Seriously.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1653)

    label("loc_BA0")

    Jump("loc_1297")

    label("loc_BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C47")

    ChrTalk(    #12
        0xFE,
        (
            "I'm sure the new mayor\x01",
            "won't treat the harbor too\x01",
            "badly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Personally, I don't see the\x01",
            "problem with putting focus\x01",
            "on the tourist industry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D70")

    label("loc_C47")


    ChrTalk(    #14
        0xFE,
        "Mister Norman won the election.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Woulda been nice for us\x01",
            "if a fellow man of the harbor \x01",
            "like Portos had won, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "It's not like Mister Norman's\x01",
            "a bad guy or anything. I don't\x01",
            "think he'll neglect the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Guess the only thing we\x01",
            "can do is sit back and see\x01",
            "how things go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D70")

    Jump("loc_1297")

    label("loc_D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E0E")

    ChrTalk(    #18
        0xFE,
        (
            "You've heard about the\x01",
            "election going on in Ruan,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I wonder who everyone\x01",
            "in Ruan's gonna choose for\x01",
            "their next mayor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F41")

    label("loc_E0E")


    ChrTalk(    #20
        0xFE,
        (
            "You've heard about the\x01",
            "election going on in Ruan,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I wonder who everyone\x01",
            "in Ruan's gonna choose for\x01",
            "their next mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I've got a soft spot for the harbor\x01",
            "myself, so I like the idea of a\x01",
            "man like Portos taking on the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "That Mister Norman's a pretty\x01",
            "persuasive fellow, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F41")

    Jump("loc_1297")

    label("loc_F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1104")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FFB")

    ChrTalk(    #24
        0xFE,
        (
            "Once one problem's solved,\x01",
            "the next one crops right up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "It's the same thing again and again\x01",
            "at my job. With any job, really.\x01",
            "Never quite goes how you want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1101")

    label("loc_FFB")


    ChrTalk(    #26
        0xFE,
        (
            "Once one problem's solved,\x01",
            "the next one crops right up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "It's the same thing again and again\x01",
            "at my job. With any job, really.\x01",
            "Never quite goes how you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I like to think of each new problem\x01",
            "as a new puzzle to solve. Keeps my\x01",
            "job interesting.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1101")

    Jump("loc_1297")

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1297")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11A4")

    ChrTalk(    #29
        0xFE,
        (
            "With Ruan missing a mayor,\x01",
            "ship traffic inspection's getting\x01",
            "delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Thanks to that, our work's\x01",
            "a heck of a lot harder than\x01",
            "normal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1297")

    label("loc_11A4")


    ChrTalk(    #31
        0xFE,
        (
            "All ships that come into the\x01",
            "capital port have to pass through\x01",
            "Ruan's Roubine River, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "With Ruan missing a mayor,\x01",
            "ship traffic inspection's getting\x01",
            "delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Thanks to that, our work's\x01",
            "a heck of a lot harder than\x01",
            "normal.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1297")

    TalkEnd(0x8)
    Return()

    # Function_4_857 end

    def Function_5_129B(): pass

    label("Function_5_129B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1338")

    ChrTalk(    #34
        0xFE,
        (
            "Ever since orbal ships were\x01",
            "introduced, sailing ships have\x01",
            "been on the decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "*sigh*\x01",
            "Can't something be done...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F2")

    label("loc_1338")


    ChrTalk(    #36
        0xFE,
        (
            "Our job's kind of at a dead\x01",
            "end if no ships come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Ever since orbal ships were\x01",
            "introduced, sailing ships have\x01",
            "been on the decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "*sigh*\x01",
            "Can't something be done...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_13F2")

    Jump("loc_1B76")

    label("loc_13F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_157E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14A7")

    ChrTalk(    #39
        0xFE,
        (
            "I was told we'd be compensated\x01",
            "for the damages to the warehouse\x01",
            "doors and harbor facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Our country sure works fast\x01",
            "in a crisis, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157B")

    label("loc_14A7")


    ChrTalk(    #41
        0xFE,
        (
            "I can't believe the renter of\x01",
            "that warehouse was with the\x01",
            "Intelligence Division!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Never would've thought there\x01",
            "was a friggin' TANK in it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I was so shocked, I thought\x01",
            "my eyeballs would fly out!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_157B")

    Jump("loc_1B76")

    label("loc_157E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1621")

    ChrTalk(    #44
        0xFE,
        (
            "We can't get in contact with\x01",
            "the renter for this warehouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Their contract's about to expire,\x01",
            "so if we can't get a hold of them\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1722")

    label("loc_1621")


    ChrTalk(    #46
        0xFE,
        (
            "About half a year ago,\x01",
            "someone came and rented\x01",
            "out this warehouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "They paid in advance, so it's not\x01",
            "like we've ever had to worry about\x01",
            "money with them or anything, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "...we haven't been able to get\x01",
            "a hold of 'em for a few months now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1722")

    Jump("loc_1B76")

    label("loc_1725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D5")

    ChrTalk(    #49
        0xFE,
        "...Already pretty late, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Whenever I get immersed\x01",
            "in my work, time just goes\x01",
            "by so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "And every day, I grow a little\x01",
            "bit older and wiser.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B76")

    label("loc_17D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_19F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_188A")

    ChrTalk(    #52
        0xFE,
        (
            "Leaving the warehouses\x01",
            "empty was just a waste of\x01",
            "space and maintenance fees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "So we put our heads together\x01",
            "and came up with the warehouse\x01",
            "rental business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19EE")

    label("loc_188A")


    ChrTalk(    #54
        0xFE,
        (
            "Goods are all being transported\x01",
            "by airship these days, so the number\x01",
            "of empty warehouses kept adding up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "And having nothing but empty\x01",
            "warehouses is a waste of space\x01",
            "and maintenance fees, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "So we put our heads together\x01",
            "and came up with the warehouse\x01",
            "rental business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "We rent out to civilians, of course,\x01",
            "but also the Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_19EE")

    Jump("loc_1B76")

    label("loc_19F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A83")

    ChrTalk(    #58
        0xFE,
        (
            "Once the harbor was re-opened,\x01",
            "we got real busy, let me tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "It's only really calmed down\x01",
            "over the last few days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B76")

    label("loc_1A83")


    ChrTalk(    #60
        0xFE,
        (
            "During the coup d'etat, the harbor\x01",
            "was closed by the Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Thanks to that, ships that'd come in for\x01",
            "loading had to wait on the lake for days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Once the harbor was re-opened,\x01",
            "we got real busy, let me tell you!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1B76")

    TalkEnd(0x9)
    Return()

    # Function_5_129B end

    def Function_6_1B7A(): pass

    label("Function_6_1B7A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C86")

    ChrTalk(    #63
        0xFE,
        (
            "The giant orbal construct that flew\x01",
            "away from the harbor, the ancient\x01",
            "dragon that appeared in Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "I didn't think I'd be surprised at\x01",
            "anythin' that showed up anymore,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "What is that weird thing that\x01",
            "appeared in the sky...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C86")

    Jump("loc_23B9")

    label("loc_1C89")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1D3D")

    ChrTalk(    #66
        0xFE,
        (
            "That night, I saw a giant shadow\x01",
            "fly off from the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "It was shaped like a person,\x01",
            "but that's impossible, right?\x01",
            "What on earth WAS that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E22")

    label("loc_1D3D")


    ChrTalk(    #68
        0xFE,
        (
            "That night, I saw a giant shadow\x01",
            "fly off from the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "It was shaped like a person,\x01",
            "but that's impossible, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I was sure I was just imagining\x01",
            "things, but with the army as worked\x01",
            "up as it is, maybe not...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1E22")

    Jump("loc_23B9")

    label("loc_1E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1EDA")

    ChrTalk(    #71
        0xFE,
        (
            "Some people say they don't\x01",
            "like boats because they get\x01",
            "sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "If you ask me, bein' in the air\x01",
            "and knowin' you could fall at\x01",
            "any time is a whole lot worse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2006")

    label("loc_1EDA")


    ChrTalk(    #73
        0xFE,
        (
            "Some people say they don't\x01",
            "like boats because they get\x01",
            "sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "If you ask me, bein' in the air\x01",
            "and knowin' you could fall at\x01",
            "any time is a whole lot worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Boats don't exactly fall, so\x01",
            "they're a lot safer than airships,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "... \x01",
            "Well, I guess you could still drown.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2006")

    Jump("loc_23B9")

    label("loc_2009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_216A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_20B3")

    ChrTalk(    #77
        0xFE,
        (
            "If I had to pick between an airship\x01",
            "or a boat, hands down, I'd pick\x01",
            "the damn boat every time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "That's the only choice for a man\x01",
            "of the sea!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2167")

    label("loc_20B3")


    ChrTalk(    #79
        0xFE,
        (
            "A boat gliding across the\x01",
            "evening sea...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "And me, standing stoically\x01",
            "upon its prow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "How about it? Doesn't that paint\x01",
            "a melancholy picture? A romantic\x01",
            "one, even?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2167")

    Jump("loc_23B9")

    label("loc_216A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2322")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2231")

    ChrTalk(    #82
        0xFE,
        (
            "Airships may be convenient, but there's\x01",
            "a limit to how many goods you can put\x01",
            "on 'em with their current performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "For mass transport of goods,\x01",
            "boats are still the best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231F")

    label("loc_2231")


    ChrTalk(    #84
        0xFE,
        (
            "Simply put, boats're better because\x01",
            "you can fit more stuff in 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Airships may be convenient, but there's\x01",
            "a limit to how many goods you can put\x01",
            "on 'em with their current performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "You just can't go wrong with boats.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_231F")

    Jump("loc_23B9")

    label("loc_2322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_23B9")

    ChrTalk(    #87
        0xFE,
        "Hmm, ships really are great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "The romance of the open sea is\x01",
            "something you can only understand\x01",
            "if you've seen it on a boat first-hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B9")

    TalkEnd(0xA)
    Return()

    # Function_6_1B7A end

    def Function_7_23BD(): pass

    label("Function_7_23BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_242B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2428")

    ChrTalk(    #89
        0xFE,
        (
            "Eh? Lemme guess,\x01",
            "you're here to see THAT.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "You can see it over at the dock.\x02",
    )

    CloseMessageWindow()

    label("loc_2428")

    Jump("loc_258F")

    label("loc_242B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_258F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2441")
    Jump("loc_258F")

    label("loc_2441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2496")

    ChrTalk(    #91
        0xFE,
        "Eh? A girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Nah, no girl like that's come here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_258F")

    label("loc_2496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2500")

    ChrTalk(    #93
        0xFE,
        "Eh? What do you want at this hour?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Work's almost over.\x01",
            "I'm ready to head on home!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_258F")

    label("loc_2500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2521")

    ChrTalk(    #95
        0xFE,
        "Phew! What a day.\x02",
    )

    CloseMessageWindow()
    Jump("loc_258F")

    label("loc_2521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_258F")

    ChrTalk(    #96
        0xFE,
        "Eh? You want somethin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "If you're lookin' to rent one\x01",
            "of the warehouses, talk to\x01",
            "the office.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258F")

    TalkEnd(0xFE)
    Return()

    # Function_7_23BD end

    def Function_8_2593(): pass

    label("Function_8_2593")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_260D")

    ChrTalk(    #98
        0xFE,
        "What the heck is that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Not like I can get any work\x01",
            "done anyway. Might as well\x01",
            "relax here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260D")

    Jump("loc_2881")

    label("loc_2610")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2626")
    Jump("loc_2881")

    label("loc_2626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_265A")

    ChrTalk(    #100
        0xFE,
        "All right, time to get back to work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2881")

    label("loc_265A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26C4")

    ChrTalk(    #101
        0xFE,
        "*sigh* I am super sweaty right now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I just wanna dive head-first into\x01",
            "the lake!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2881")

    label("loc_26C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_273A")

    ChrTalk(    #103
        0xFE,
        (
            "When something bad happens,\x01",
            "I like to come here and relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "You have a place like that too,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2881")

    label("loc_273A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_27AB")

    ChrTalk(    #105
        0xFE,
        "I-I'm not skipping work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "I'm p-patrolling to see if there's\x01",
            "anyone suspicious around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2881")

    label("loc_27AB")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 300)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0x1388)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #107
        0xFE,
        "Wh-What do you guys want?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "I-I'm not skipping work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "I'm p-patrolling to see if there's\x01",
            "anyone suspicious around.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_8C(0xFE, 180, 0)
    OP_A2(0x4)

    label("loc_2881")

    TalkEnd(0xFE)
    Return()

    # Function_8_2593 end

    def Function_9_2885(): pass

    label("Function_9_2885")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2916")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2913")

    ChrTalk(    #110
        0xFE,
        (
            "Just as harbor business was\x01",
            "starting to get back on track,\x01",
            "this mess happens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "Has the Goddess abandoned us?\x02",
    )

    CloseMessageWindow()

    label("loc_2913")

    Jump("loc_2A77")

    label("loc_2916")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_292C")
    Jump("loc_2A77")

    label("loc_292C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2960")

    ChrTalk(    #112
        0xFE,
        "I wonder what today's lunch is... ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A77")

    label("loc_2960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29B0")

    ChrTalk(    #113
        0xFE,
        (
            "All right, gonna get a bit more\x01",
            "done and then call it a day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A77")

    label("loc_29B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2A08")

    ChrTalk(    #114
        0xFE,
        (
            "Uuughhh... My stomach's so full...\x01",
            "I shoulda left it at one lunch today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A77")

    label("loc_2A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2A77")

    ChrTalk(    #115
        0xFE,
        "Come to sightsee in the harbor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "You're free to look around,\x01",
            "but don't get in the way of work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A77")

    TalkEnd(0xFE)
    Return()

    # Function_9_2885 end

    def Function_10_2A7B(): pass

    label("Function_10_2A7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B01")

    ChrTalk(    #117
        0xFE,
        (
            "Can't use transport trucks,\x01",
            "and the boats ain't movin' either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "What the heck are we\x01",
            "supposed to do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B01")

    Jump("loc_2C2F")

    label("loc_2B04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2B1A")
    Jump("loc_2C2F")

    label("loc_2B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2B49")

    ChrTalk(    #119
        0xFE,
        "Heh, what a great day for work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C2F")

    label("loc_2B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B80")

    ChrTalk(    #120
        0xFE,
        (
            "Phew!\x01",
            "Worked up a good sweat today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2F")

    label("loc_2B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2BED")

    ChrTalk(    #121
        0xFE,
        (
            "Our job involves standin'\x01",
            "up all year long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Can't really do it without\x01",
            "real strong hips.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2F")

    label("loc_2BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2C2F")

    ChrTalk(    #123
        0xFE,
        (
            "Welcome! Wanna see how\x01",
            "I do my job while you're here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2F")

    TalkEnd(0xFE)
    Return()

    # Function_10_2A7B end

    def Function_11_2C33(): pass

    label("Function_11_2C33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C7F")

    ChrTalk(    #124
        0xFE,
        (
            "I wonder how long this\x01",
            "is gonna keep goin' on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C7F")

    Jump("loc_2DEE")

    label("loc_2C82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2C98")
    Jump("loc_2DEE")

    label("loc_2C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2CDA")

    ChrTalk(    #125
        0xFE,
        (
            "Mmmmm, that's a great\x01",
            "wind comin' in off the lake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEE")

    label("loc_2CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D30")

    ChrTalk(    #126
        0xFE,
        (
            "There's something about\x01",
            "sending off a boat into the\x01",
            "evenin' sun...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEE")

    label("loc_2D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2D99")

    ChrTalk(    #127
        0xFE,
        "I love this work place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Who wouldn't want to stare\x01",
            "out into Valleria Lake every day?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DEE")

    label("loc_2D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2DEE")

    ChrTalk(    #129
        0xFE,
        (
            "Man, what a gorgeous blue sky!\x01",
            "You can see the Krone peaks clear\x01",
            "as day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DEE")

    TalkEnd(0xFE)
    Return()

    # Function_11_2C33 end

    def Function_12_2DF2(): pass

    label("Function_12_2DF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2E62")

    ChrTalk(    #130
        0xFE,
        (
            "To think orbments would\x01",
            "just stop working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "*sigh*\x01",
            "I'm worried about the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E62")

    Jump("loc_3005")

    label("loc_2E65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2E7B")
    Jump("loc_3005")

    label("loc_2E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2EB2")

    ChrTalk(    #132
        0xFE,
        (
            "Ahaha, the boats are doing\x01",
            "great today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3005")

    label("loc_2EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F23")

    ChrTalk(    #133
        0xFE,
        (
            "Twilight always works this\x01",
            "mysterious magic on me. It feels\x01",
            "bittersweet...or lonely, perhaps.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3005")

    label("loc_2F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2FA7")

    ChrTalk(    #134
        0xFE,
        "This boat's always in great shape.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Just as it should be! No one puts\x01",
            "their heart into these boats more\x01",
            "than me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3005")

    label("loc_2FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3005")

    ChrTalk(    #136
        0xFE,
        "Come to see an orbal boat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Heh, go ahead.\x01",
            "Look around as much as\x01",
            "you'd like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3005")

    TalkEnd(0xFE)
    Return()

    # Function_12_2DF2 end

    def Function_13_3009(): pass

    label("Function_13_3009")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3045")

    ChrTalk(    #138
        0xFE,
        (
            "Hmm, the more I look,\x01",
            "the stranger it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3075")

    label("loc_3045")


    ChrTalk(    #139
        0xFE,
        (
            "My goodness, this is quite\x01",
            "a lot of cargo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3075")

    TalkEnd(0xFE)
    Return()

    # Function_13_3009 end

    def Function_14_3079(): pass

    label("Function_14_3079")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_30D7")

    ChrTalk(    #140
        0xFE,
        "Very curious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "How is that thing floating if\x01",
            "orbments aren't working?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313C")

    label("loc_30D7")


    ChrTalk(    #142
        0xFE,
        (
            "Orbal boats just look stunning\x01",
            "framed by the blue sky and waters.\x01",
            "I wish I'd brought my camera.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313C")

    TalkEnd(0xFE)
    Return()

    # Function_14_3079 end

    def Function_15_3140(): pass

    label("Function_15_3140")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_31E6")

    ChrTalk(    #143
        0xFE,
        "I've seen a lot in my long life, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "I've never seen anything that odd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Is the rumor that orbments aren't\x01",
            "working thanks to that true?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3236")

    label("loc_31E6")


    ChrTalk(    #146
        0xFE,
        (
            "Oh, yes, I can see why the capital's\x01",
            "beauty is likened to that of a pearl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3236")

    TalkEnd(0xFE)
    Return()

    # Function_15_3140 end

    def Function_16_323A(): pass

    label("Function_16_323A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3307")

    ChrTalk(    #147
        0xFE,
        (
            "Ever since that object appeared,\x01",
            "orbments have stopped working!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Can't the Royal Guard shoot it\x01",
            "down in the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I suppose the Arseille can't move\x01",
            "either, though, can it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333B")

    label("loc_3307")


    ChrTalk(    #150
        0xFE,
        (
            "My, what a pleasant little\x01",
            "warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_333B")

    TalkEnd(0xFE)
    Return()

    # Function_16_323A end

    def Function_17_333F(): pass

    label("Function_17_333F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_33B4")

    ChrTalk(    #151
        0xFE,
        "I-I didn't see anything!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "No way a freaky thing like that's\x01",
            "real! I disbelieve! I disbelieve!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3545")

    label("loc_33B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_33BE")
    Jump("loc_3545")

    label("loc_33BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3457")

    ChrTalk(    #153
        0xFE,
        (
            "Ohh, don't you think that little\x01",
            "family over there makes for a\x01",
            "pretty picture?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I don't know why, but it brings\x01",
            "tears to my eyes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3545")

    label("loc_3457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_34D0")

    ChrTalk(    #155
        0xFE,
        (
            "Just being here makes me\x01",
            "feel like I've become a man\x01",
            "of the sea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "How about it, pretty handsome,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3545")

    label("loc_34D0")


    ChrTalk(    #157
        0xFE,
        "Harbors have a great atmosphere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "I'd really love to confess my love to\x01",
            "my girlfriend in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3545")

    TalkEnd(0xFE)
    Return()

    # Function_17_333F end

    def Function_18_3549(): pass

    label("Function_18_3549")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3588")

    ChrTalk(    #159
        0xFE,
        (
            "You can see it all the more\x01",
            "clearly today...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3665")

    label("loc_3588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3592")
    Jump("loc_3665")

    label("loc_3592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35C7")

    ChrTalk(    #160
        0xFE,
        "My, what a lovely bit of scenery!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3665")

    label("loc_35C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3619")

    ChrTalk(    #161
        0xFE,
        (
            "Airships are nice, but boats just\x01",
            "exude a special sense of wonder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3665")

    label("loc_3619")


    ChrTalk(    #162
        0xFE,
        (
            "Huh. Didn't realize you could pile\x01",
            "this much stuff onto an orbal boat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3665")

    TalkEnd(0xFE)
    Return()

    # Function_18_3549 end

    def Function_19_3669(): pass

    label("Function_19_3669")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_36BC")

    ChrTalk(    #163
        0xFE,
        "P-Please don't say something so scary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "Wh-Who's riding it?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_379A")

    label("loc_36BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_36C6")
    Jump("loc_379A")

    label("loc_36C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36F7")

    ChrTalk(    #165
        0xFE,
        "Oh, this is quite the sunset.\x02",
    )

    CloseMessageWindow()
    Jump("loc_379A")

    label("loc_36F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_373A")

    ChrTalk(    #166
        0xFE,
        (
            "Mmmm, the wind off Valleria Lake is\x01",
            "quite pleasant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_379A")

    label("loc_373A")


    ChrTalk(    #167
        0xFE,
        "Oh, an orbal boat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "Kinda embarrassing to admit,\x01",
            "but this is my first time seeing\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_379A")

    TalkEnd(0xFE)
    Return()

    # Function_19_3669 end

    def Function_20_379E(): pass

    label("Function_20_379E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_37DC")

    ChrTalk(    #169
        0xFE,
        (
            "I wonder if someone's riding that\x01",
            "object...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39A8")

    label("loc_37DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_37E6")
    Jump("loc_39A8")

    label("loc_37E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3845")

    ChrTalk(    #170
        0xFE,
        "Oh, finally!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "You gave me a real scare.\x01",
            "I'm never letting you go again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39A8")

    label("loc_3845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_38C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3883")

    ChrTalk(    #172
        0xFE,
        (
            "Why is this harbor so busy,\x01",
            "I wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C1")

    label("loc_3883")


    ChrTalk(    #173
        0xFE,
        (
            "I'm coming right now, so just\x01",
            "wait there! Don't move!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_38C1")

    Jump("loc_39A8")

    label("loc_38C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_38FD")

    ChrTalk(    #174
        0xFE,
        (
            "Wh-Where's my daughter\x01",
            "gotten off to now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39A8")

    label("loc_38FD")


    ChrTalk(    #175
        0xFE,
        (
            "This warehouse has a\x01",
            "nice, peaceful atmosphere...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #176
        0xFE,
        "Oh, my...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #177
        0xFE,
        (
            "Wh-Where's my daughter\x01",
            "gotten off to now?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_39A8")

    TalkEnd(0xFE)
    Return()

    # Function_20_379E end

    def Function_21_39AC(): pass

    label("Function_21_39AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_39E0")

    ChrTalk(    #178
        0xFE,
        "There's a biiig flying island!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_3A4A")

    label("loc_39E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_39EA")
    Jump("loc_3A4A")

    label("loc_39EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A0B")

    ChrTalk(    #179
        0xFE,
        "Waaaah, Mama!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A4A")

    label("loc_3A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3A30")

    ChrTalk(    #180
        0xFE,
        "Mama! I'm over here!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A4A")

    label("loc_3A30")


    ChrTalk(    #181
        0xFE,
        "Mama! Where are you?\x02",
    )

    CloseMessageWindow()

    label("loc_3A4A")

    TalkEnd(0xFE)
    Return()

    # Function_21_39AC end

    def Function_22_3A4E(): pass

    label("Function_22_3A4E")

    TalkBegin(0xFE)

    ChrTalk(    #182
        0xFE,
        "メッセージ未作成　根田に確認\x02",
    )

    TalkEnd(0xFE)
    Return()

    # Function_22_3A4E end

    def Function_23_3A76(): pass

    label("Function_23_3A76")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A8D")
    OP_6F(0x4, 0)
    OP_A3(0x0)
    Jump("loc_3AF0")

    label("loc_3A8D")

    OP_A2(0x0)
    LoadEffect(0x0, "map\\\\snddst1.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 15080, 0, 56290, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x1E)
    OP_CA(0x4, 0x1, 0x1F4)
    OP_73(0x4)

    label("loc_3AF0")

    TalkEnd(0xFF)
    Return()

    # Function_23_3A76 end

    def Function_24_3AF4(): pass

    label("Function_24_3AF4")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #183
        "\x07\x05The door is tightly closed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_3AF4 end

    def Function_25_3B4B(): pass

    label("Function_25_3B4B")

    EventBegin(0x1)

    ChrTalk(    #184
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_3B77():
        OP_6D(3250, 0, 123500, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3B77)

    def lambda_3B8F():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3B8F)

    def lambda_3B9F():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3B9F)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #185
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C45")
    OP_C0(0xE, 0x2C, 0xC6C, 0x992, 0x1DA88, 0x0, 0xC9E, 0xFFFFF8F8, 0x1F144)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_3C54")

    label("loc_3C45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C54")
    EventEnd(0x1)

    label("loc_3C54")

    Return()

    # Function_25_3B4B end

    def Function_26_3C55(): pass

    label("Function_26_3C55")

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

    # Function_26_3C55 end

    SaveToFile()

Try(main)
