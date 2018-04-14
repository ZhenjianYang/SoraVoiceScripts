from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3300   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        '士兵布拉姆',                           # 9
        '士兵赫宁',                             # 10
        '派斯队长',                             # 11
        '格温副队长',                           # 12
        '伦法',                                 # 13
        '王',                                   # 14
        '冈多夫',                               # 15
        '鸡',                                   # 16
        '鸡',                                   # 17
        '鸡',                                   # 18
        '鸡',                                   # 19
        '托兰特平原道方向',                     # 20
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01310 ._CH',             # 02
        'ED6_DT07/CH01300 ._CH',             # 03
        'ED6_DT07/CH01270 ._CH',             # 04
        'ED6_DT07/CH01530 ._CH',             # 05
        'ED6_DT07/CH01760 ._CH',             # 06
        'ED6_DT07/CH01720 ._CH',             # 07
        'ED6_DT07/CH01750 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01310P._CP',             # 02
        'ED6_DT07/CH01300P._CP',             # 03
        'ED6_DT07/CH01270P._CP',             # 04
        'ED6_DT07/CH01530P._CP',             # 05
        'ED6_DT07/CH01760P._CP',             # 06
        'ED6_DT07/CH01720P._CP',             # 07
        'ED6_DT07/CH01750P._CP',             # 08
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 0,
        Y                   = 48690,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -7370,
        Z                   = 5500,
        Y                   = 49600,
        Direction           = 74,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 13200,
        Z                   = 0,
        Y                   = 38690,
        Direction           = 0,
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
        X                   = 3900,
        Z                   = 0,
        Y                   = 40920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 1990,
        Z                   = -500,
        Y                   = -280,
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
        X                   = -2420,
        Y                   = -2000,
        Z                   = 9840,
        Range               = 6500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2AF8,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 6530,
        Y                   = -1000,
        Z                   = 50580,
        Range               = 1330,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xC260,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )


    DeclActor(
        TriggerX            = 8039,
        TriggerZ            = 0,
        TriggerY            = 21240,
        TriggerRange        = 1500,
        ActorX              = 8039,
        ActorZ              = 2000,
        ActorY              = 21240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_35E",          # 01, 1
        "Function_2_39D",          # 02, 2
        "Function_3_444",          # 03, 3
        "Function_4_468",          # 04, 4
        "Function_5_48C",          # 05, 5
        "Function_6_5DA",          # 06, 6
        "Function_7_728",          # 07, 7
        "Function_8_7AC",          # 08, 8
        "Function_9_7D2",          # 09, 9
        "Function_10_E5B",         # 0A, 10
        "Function_11_1018",        # 0B, 11
        "Function_12_101F",        # 0C, 12
        "Function_13_1646",        # 0D, 13
        "Function_14_164D",        # 0E, 14
        "Function_15_1DD7",        # 0F, 15
        "Function_16_2034",        # 10, 16
        "Function_17_2578",        # 11, 17
        "Function_18_25B9",        # 12, 18
        "Function_19_2708",        # 13, 19
        "Function_20_290A",        # 14, 20
        "Function_21_2A6F",        # 15, 21
        "Function_22_2FBB",        # 16, 22
        "Function_23_3054",        # 17, 23
        "Function_24_30B2",        # 18, 24
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_320")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 6760, 0, 48670, 315)
    SetChrPos(0x8, 1020, 0, 48670, 45)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D")
    ClearChrFlags(0xE, 0x80)

    label("loc_31D")

    Jump("loc_33B")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_334")
    SetChrFlags(0x8, 0x10)
    Jump("loc_33B")

    label("loc_334")

    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34C")
    ClearChrFlags(0xD, 0x80)

    label("loc_34C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_35D")

    Return()

    # Function_0_2D6 end

    def Function_1_35E(): pass

    label("Function_1_35E")

    OP_16(0x2, 0xFA0, 0xFFFE1BA0, 0xFFFEB7E0, 0x230055)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37F")
    Jump("loc_384")

    label("loc_37F")

    OP_71(0x4, 0x4)

    label("loc_384")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C")
    OP_72(0x3, 0x10)
    OP_6F(0x3, 420)

    label("loc_39C")

    Return()

    # Function_1_35E end

    def Function_2_39D(): pass

    label("Function_2_39D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3CE"),
        (1, "loc_3DA"),
        (2, "loc_3E6"),
        (3, "loc_3F2"),
        (4, "loc_3FE"),
        (5, "loc_40A"),
        (6, "loc_416"),
        (SWITCH_DEFAULT, "loc_422"),
    )


    label("loc_3CE")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_42E")

    label("loc_3DA")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_42E")

    label("loc_3E6")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_42E")

    label("loc_3F2")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_42E")

    label("loc_3FE")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_42E")

    label("loc_40A")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_42E")

    label("loc_416")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_42E")

    label("loc_422")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_42E")

    label("loc_42E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_443")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_42E")

    label("loc_443")

    Return()

    # Function_2_39D end

    def Function_3_444(): pass

    label("Function_3_444")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_467")
    OP_8D(0xFE, -9410, 54290, -4840, 47630, 2000)
    Jump("Function_3_444")

    label("loc_467")

    Return()

    # Function_3_444 end

    def Function_4_468(): pass

    label("Function_4_468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48B")
    OP_8D(0xFE, -3560, 41360, 11130, 38000, 2000)
    Jump("Function_4_468")

    label("loc_48B")

    Return()

    # Function_4_468 end

    def Function_5_48C(): pass

    label("Function_5_48C")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -4320, 30420, 16309, 38200, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D9")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59E")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x10E0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x76D4), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x3FB5), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x9538), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_573")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_560():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_560)
    Jump("loc_596")

    label("loc_573")


    def lambda_579():
        OP_8D(0xFE, -4320, 30420, 16309, 38200, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_579)
    Sleep(200)

    label("loc_596")

    Sleep(30)
    Jump("loc_5D6")

    label("loc_59E")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D6")
    OP_44(0xFE, 0x2)

    def lambda_5BE():
        OP_8D(0xFE, -4320, 30420, 16309, 38200, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BE)

    label("loc_5D6")

    Jump("loc_4B5")

    label("loc_5D9")

    Return()

    # Function_5_48C end

    def Function_6_5DA(): pass

    label("Function_6_5DA")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -780, 24910, 8900, 46240, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_603")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_727")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EC")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x30C), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x614E), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x22C4), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xB4A0), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C1")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_6AE():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AE)
    Jump("loc_6E4")

    label("loc_6C1")


    def lambda_6C7():
        OP_8D(0xFE, -780, 24910, 8900, 46240, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C7)
    Sleep(200)

    label("loc_6E4")

    Sleep(30)
    Jump("loc_724")

    label("loc_6EC")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724")
    OP_44(0xFE, 0x2)

    def lambda_70C():
        OP_8D(0xFE, -780, 24910, 8900, 46240, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_70C)

    label("loc_724")

    Jump("loc_603")

    label("loc_727")

    Return()

    # Function_6_5DA end

    def Function_7_728(): pass

    label("Function_7_728")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AB")
    OP_43(0xFE, 0x2, 0x0, 0x8)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_7AB")
    TalkBegin(0xFE)
    OP_A2(0x7)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x8B\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_7AB")

    Return()

    # Function_7_728 end

    def Function_8_7AC(): pass

    label("Function_8_7AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_8_7AC")

    label("loc_7C7")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_7AC end

    def Function_9_7D2(): pass

    label("Function_9_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E3")
    Call(0, 21)
    Return()

    label("loc_7E3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_912")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_802")
    OP_A2(0x8)

    label("loc_802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇前作『爱的使者』高评价完成】\x01",      # 0
            "【◇没有完成】\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_86E"),
        (1, "loc_874"),
        (SWITCH_DEFAULT, "loc_87A"),
    )


    label("loc_86E")

    OP_A2(0x8)
    Jump("loc_87A")

    label("loc_874")

    OP_A3(0x8)
    Jump("loc_87A")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C9")

    ChrTalk(    #1
        0xFE,
        "呼，呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "是太紧张了吧\x01",
            "感觉好疲倦呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "呼啊啊…\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_90F")

    label("loc_8C9")


    ChrTalk(    #4
        0xFE,
        (
            "果然是太紧张了，\x01",
            "完全睡不着觉…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "呼啊啊…\x01",
            "但却一直在打呵欠。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90F")

    Jump("loc_E57")

    label("loc_912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96F")

    ChrTalk(    #6
        0xFE,
        (
            "现在最头疼的事情\x01",
            "就是大门关不上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "这，这害得\x01",
            "我都睡不着觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_9C5")

    label("loc_96F")


    ChrTalk(    #8
        0xFE,
        (
            "不早点想办法\x01",
            "能早日恢复啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "大门关上再关不上的话，\x01",
            "我大概就要患上失眠症了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C5")

    Jump("loc_E57")

    label("loc_9C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A18")

    ChrTalk(    #10
        0xFE,
        (
            "虽然没有发生什么\x01",
            "大灾害，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "地震真是好可怕啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A5F")

    label("loc_A18")


    ChrTalk(    #12
        0xFE,
        (
            "听说连雷斯顿要塞\x01",
            "也遭受到地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "吃了一惊，\x01",
            "马上就醒了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A5F")

    Jump("loc_E57")

    label("loc_A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_C9B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7E")
    OP_A2(0x8)

    label("loc_A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF6")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇前作『爱的使者』高评价完成】\x01",      # 0
            "【◇没有完成】\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AEA"),
        (1, "loc_AF0"),
        (SWITCH_DEFAULT, "loc_AF6"),
    )


    label("loc_AEA")

    OP_A2(0x8)
    Jump("loc_AF6")

    label("loc_AF0")

    OP_A3(0x8)
    Jump("loc_AF6")

    label("loc_AF6")

    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B4A")

    ChrTalk(    #14
        0xFE,
        (
            "……哎～哎嘿嘿………\x01",
            "菲……不行啊…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDA")

    label("loc_B4A")

    SetChrName("士兵布拉姆")

    ChrTalk(    #15
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("士兵布拉姆")

    ChrTalk(    #16
        0xFE,
        "……哎～哎嘿嘿………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "菲……不行啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "不……不要…………\x01",
            "……不要抛弃我……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BDA")

    Jump("loc_C98")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C1C")
    SetChrName("士兵布拉姆")

    ChrTalk(    #19
        0xFE,
        (
            "……呜、呜呜～………\x01",
            "菲……原谅我…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C98")

    label("loc_C1C")


    ChrTalk(    #20
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "……呜、呜呜～………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "菲……原谅我吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "对……对不起…………\x01",
            "……是我不好………\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C98")

    Jump("loc_E57")

    label("loc_C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_D5F")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CFA")

    ChrTalk(    #24
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "呜～……呜～…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_D5C")

    label("loc_CFA")


    ChrTalk(    #26
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "……嗯～……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "异状……没有………\x01",
            "……发～生～…………\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D5C")

    Jump("loc_E57")

    label("loc_D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_END)), "loc_D9A")

    ChrTalk(    #29
        0xFE,
        "呼哇哇～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "嗯嗯嗯……\x01",
            "我又睡着了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E57")

    label("loc_D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_END)), "loc_DCE")

    ChrTalk(    #31
        0xFE,
        "呼哇哇～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "嗯？见过赫宁了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_E57")

    label("loc_DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_END)), "loc_E22")

    ChrTalk(    #33
        0xFE,
        (
            "赫宁那家伙现在\x01",
            "应该在休息所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "在那里的２楼偷懒\x01",
            "是他一贯的作法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E57")

    label("loc_E22")


    ChrTalk(    #35
        0xFE,
        "呼哇哇～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "嗯嗯嗯……\x01",
            "今天也是好天气啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E57")

    TalkEnd(0x8)
    Return()

    # Function_9_7D2 end

    def Function_10_E5B(): pass

    label("Function_10_E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE6")

    ChrTalk(    #37
        0xFE,
        (
            "布拉姆那小子\x01",
            "从刚才开始就一直呵欠不断。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "但是今天可\x01",
            "不能睡啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "像、像现在这种情况\x01",
            "可不能只靠一个人。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_F42")

    label("loc_EE6")


    ChrTalk(    #40
        0xFE,
        (
            "如果布拉姆睡觉的话\x01",
            "警备工作就只能靠我一个了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "要是他再敢睡觉，\x01",
            "我就用枪把他捅醒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F42")

    Jump("loc_1014")

    label("loc_F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBC")

    ChrTalk(    #42
        0xFE,
        (
            "对面是共和国，在安全方面\x01",
            "大概没什么问题，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "像这样毫无防备，\x01",
            "总还是让人不放心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1014")

    label("loc_FBC")


    ChrTalk(    #44
        0xFE,
        (
            "像这样毫无防备，\x01",
            "总还是让人不踏实啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "呼，难得空闲\x01",
            "现在的状况让人不得不紧张。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1014")

    TalkEnd(0xFE)
    Return()

    # Function_10_E5B end

    def Function_11_1018(): pass

    label("Function_11_1018")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_1018 end

    def Function_12_101F(): pass

    label("Function_12_101F")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_111C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_108B")

    ChrTalk(    #46
        0xFE,
        (
            "虽然地震已经停止了，\x01",
            "但还是不能放松。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "不久之后就是互不侵犯条约\x01",
            "的签字仪式了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1119")

    label("loc_108B")


    ChrTalk(    #48
        0xFE,
        (
            "中央工房好像做出了\x01",
            "地震停止的公开宣言…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "其实军队上层也发布了\x01",
            "类似的通知。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "呼，理由暂且不问，\x01",
            "不过总之地震确实是没再发生了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1119")

    Jump("loc_1642")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_11AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1170")

    ChrTalk(    #51
        0xFE,
        (
            "地震的发生场所\x01",
            "全都是重要设施所在地，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "这似乎不是偶然啊…\x02",
    )

    CloseMessageWindow()
    Jump("loc_11AA")

    label("loc_1170")


    ChrTalk(    #53
        0xFE,
        "这次是雷斯顿要塞吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "竟然专门挑选\x01",
            "军事基地…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_11AA")

    Jump("loc_1642")

    label("loc_11AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_1277")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_120C")

    ChrTalk(    #55
        0xFE,
        (
            "圣海姆门也\x01",
            "好像发生地震了啊，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "我们这里也不能大意，\x01",
            "一定要加强警备！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1274")

    label("loc_120C")


    ChrTalk(    #57
        0xFE,
        (
            "圣海姆门也\x01",
            "好像发生地震了啊，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "说不定这里也\x01",
            "会发生地震呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "从现在开始一定\x01",
            "要加强警备。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1274")

    Jump("loc_1642")

    label("loc_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_END)), "loc_1565")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_END)), "loc_12E8")

    ChrTalk(    #60
        0xFE,
        (
            "除了有地震之外\x01",
            "就没有别的奇怪现象了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "如果有什么可疑的发现\x01",
            "部下们应该会来报告给我的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_12E8")


    ChrTalk(    #62
        0xFE,
        "嗯？有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1002F啊，我们是游击士协会的人。\x02\x03",

            "希望您能配合我们\x01",
            "做个调查。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #64
        0xFE,
        (
            "可以是可以……\x01",
            "不过请尽量长话短说吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x07\x05询问对方是否在地震前后\x01",
            "发现了什么奇怪的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #66
        0xFE,
        (
            "地震……\x01",
            "是指三天前的那场地震吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "嗯，除了地震之外\x01",
            "就是很普通的一天了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "如果有什么可疑的发现\x01",
            "部下们应该会来报告给我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1015F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x104,
        (
            "#032F嗯，看来\x01",
            "白跑了一趟呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "还有别的要问吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_14DB")

    ChrTalk(    #72
        0x106,
        (
            "#050F啊，这些就可以啦。\x02\x03",

            "抱歉打扰您的工作了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_151F")

    label("loc_14DB")


    ChrTalk(    #73
        0x103,
        (
            "#027F嗯，这些就可以了。\x02\x03",

            "打扰您的工作啦，真是不好意思。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    label("loc_151F")


    ChrTalk(    #74
        0xFE,
        "哪里，不必客气。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "那我就先失陪了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x140E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1562")
    OP_28(0x85, 0x1, 0x800)
    Jump("loc_1562")

    label("loc_1562")

    Jump("loc_1642")

    label("loc_1565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1642")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15A2")

    ChrTalk(    #76
        0xFE,
        (
            "真是的……\x01",
            "这里的警备实在是太松懈了，\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1642")

    label("loc_15A2")


    ChrTalk(    #77
        0xFE,
        (
            "真是的……\x01",
            "这里的警备实在是太松懈了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "条约签字仪式的日子就快到了，\x01",
            "现在应该强化警备才对……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "像现在这种状态，\x01",
            "遇到紧急情况的话根本就无法应对。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1642")

    TalkEnd(0xB)
    Return()

    # Function_12_101F end

    def Function_13_1646(): pass

    label("Function_13_1646")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_1646 end

    def Function_14_164D(): pass

    label("Function_14_164D")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_165A")
    OP_A2(0x4)

    label("loc_165A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D0")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在前作中与王相识】\x01",      # 0
            "【◇在前作中不认识王】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16C4"),
        (1, "loc_16CA"),
        (SWITCH_DEFAULT, "loc_16D0"),
    )


    label("loc_16C4")

    OP_A2(0x4)
    Jump("loc_16D0")

    label("loc_16CA")

    OP_A3(0x4)
    Jump("loc_16D0")

    label("loc_16D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_189C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_185B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 4)), scpexpr(EXPR_END)), "loc_1729")

    ChrTalk(    #80
        0xFE,
        (
            "现在应该赶快去\x01",
            "亚尔摩村吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "总之请小心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_185B")

    label("loc_1729")


    ChrTalk(    #82
        0xFE,
        "呀，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "我现在正要\x01",
            "回蔡斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "现在的时间\x01",
            "应该很紧迫吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#1015F嗯，其实是这样……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x05将地震源是亚尔摩村告诉给维修长。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #87
        0xFE,
        (
            "那可真是\x01",
            "太诡异了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "不管怎么说，现在\x01",
            "还是抓紧时间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "那么，请小心注意吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1006F嗯，我们走了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1434)

    label("loc_185B")

    Jump("loc_1899")

    label("loc_185E")


    ChrTalk(    #91
        0xFE,
        (
            "不好意思，\x01",
            "很想帮到你们一些忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "大家一起加油吧！\x02",
    )

    CloseMessageWindow()

    label("loc_1899")

    Jump("loc_1DD3")

    label("loc_189C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1A5B")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A8")

    ChrTalk(    #93
        0xFE,
        "呀，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "还记得我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1001F当然记得啦！\x02\x03",

            "你不是蔡斯支部\x01",
            "的王吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "哈哈，谢谢，竟然还记得我。\x01",
            "能再次相遇真是高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "你终于顺利晋升为\x01",
            "正游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "恭喜！\x01",
            "凭你的实力，这也是理所当然的结果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A58")

    label("loc_19A8")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #99
        0xFE,
        "啊，这不是艾丝蒂尔吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1004F咦……？\x02\x03",

            "#1018F啊，我还说是谁，\x01",
            "这不是王吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "你终于顺利晋升为\x01",
            "正游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "恭喜！\x01",
            "凭你的实力，这也是理所当然的结果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A58")

    Jump("loc_1BA3")

    label("loc_1A5B")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #103
        0xFE,
        "…………哎呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "你不就是…\x01",
            "最近才转正的艾丝蒂尔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1004F哎哎，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "啊，失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "我是王。\x01",
            "蔡斯地区的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1000F啊～是吗。\x02\x03",

            "我是艾丝蒂尔·布莱特。\x01",
            "请多指教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "啊啊，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "你们的事情\x01",
            "我也早有耳闻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "真是立了大功啊，\x01",
            "升为正游击士也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA3")


    ChrTalk(    #112
        0x101,
        (
            "#1008F嘿嘿，谢谢夸奖。\x02\x03",

            "我们也还差得远呢，\x01",
            "还需要不断努力进步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "嗯…保持上进心，永不懈怠吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "这种谦虚的态度\x01",
            "我也要多多学习。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "对了，冈多夫\x01",
            "出去办事了，你们知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1011F啊，嗯。\x01",
            "从嘉恩那里听说了。\x02\x03",

            "我们就是为了增援\x01",
            "才特意来蔡斯的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "是这样吗。\x01",
            "谢啦，真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "真是不好意思，\x01",
            "很想帮到你们一些忙。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1D4B")
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #119
        0xFE,
        (
            "连阿加特前辈也\x01",
            "请多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x106,
        "#051F哪里，也请你们多关照了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D96")

    label("loc_1D4B")

    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #121
        0xFE,
        (
            "雪拉扎德前辈也\x01",
            "请多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        "#020F哪里的话，互相关照吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1D96")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #123
        0xFE,
        "我也竭尽全力哟。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "那么，大家都加油吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1427)
    OP_A2(0x5)

    label("loc_1DD3")

    TalkEnd(0xD)
    Return()

    # Function_14_164D end

    def Function_15_1DD7(): pass

    label("Function_15_1DD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2030")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD4")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #125
        0xFE,
        "哟，艾丝蒂尔你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "真是辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1011F啊，冈多夫先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        "#1040F好久不见了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E7D")

    ChrTalk(    #129
        0x106,
        "#050F在巡逻吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_1EDA")

    label("loc_1E7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAE")

    ChrTalk(    #130
        0x103,
        "#020F是在巡逻中吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_1EDA")

    label("loc_1EAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDA")

    ChrTalk(    #131
        0x107,
        "#064F是在巡逻吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    label("loc_1EDA")


    ChrTalk(    #132
        0xFE,
        "啊，正是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "不管怎么说，警戒工作\x01",
            "可是不能松懈的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "那，你们就集中精力\x01",
            "完成自己的任务吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "维持治安之类的事情\x01",
            "交给我们就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#1002F嗯……明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#1040F……那可太好了。\x02\x03",

            "那么，请当心。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #138
        0xFE,
        "喔，真周到啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20D1)
    Jump("loc_2030")

    label("loc_1FD4")


    ChrTalk(    #139
        0xFE,
        (
            "在现在这种形势下，\x01",
            "不管再发生什么我也不会惊奇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "我只要做好自己的\x01",
            "警戒就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2030")

    TalkEnd(0xFE)
    Return()

    # Function_15_1DD7 end

    def Function_16_2034(): pass

    label("Function_16_2034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2045")
    Call(0, 22)

    label("loc_2045")

    EventBegin(0x0)
    ClearMapFlags(0x10)
    SetChrPos(0x101, 3000, -500, 13740, 0)
    SetChrPos(0xF7, 1560, -500, 13250, 0)
    SetChrPos(0x105, 2600, -500, 11780, 0)
    SetChrPos(0x104, 1630, -500, 10970, 0)
    OP_6D(4030, 0, 48420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(6200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_20D3():
        OP_6D(3180, -500, 27340, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20D3)

    def lambda_20EB():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20EB)
    OP_C8(0x200, 0x46, "C_PLAC09._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    Sleep(1000)

    def lambda_2126():
        OP_8E(0xFE, 0xDC0, 0xFFFFFE0C, 0x4F9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2126)
    Sleep(200)

    def lambda_2146():
        OP_8E(0xFE, 0x87A, 0xFFFFFE0C, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2146)

    def lambda_2161():
        OP_8E(0xFE, 0x8DE, 0xFFFFFE0C, 0x4844, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2161)

    def lambda_217C():
        OP_8E(0xFE, 0xDE8, 0xFFFFFE0C, 0x49B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_217C)
    OP_0D()
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Fade(1000)
    OP_6D(3240, -500, 19880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #141
        0x101,
        (
            "#1011F沃尔费堡垒啊……\x02\x03",

            "虽然是和卡尔瓦德共和国之间的国境线，\x01",
            "但一直是个安宁平和的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x104,
        (
            "#033F#6P同为国境线，\x01",
            "这里和哈肯大门就完全不同啊。\x02\x03",

            "#035F呼～果然是利贝尔的友邦啊，\x01",
            "享受的待遇和我的祖国完全不同。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_22F9")

    ChrTalk(    #143
        0x106,
        (
            "#552F#5P真是……\x01",
            "就好像在说与己无关的事情一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232A")

    label("loc_22F9")


    ChrTalk(    #144
        0x103,
        (
            "#025F#5P唉……\x01",
            "说得就好像完全与己无关一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232A")


    ChrTalk(    #145
        0x105,
        (
            "#542F这里警备薄弱，虽然是有友邦\x01",
            "的因素在内，不过……\x02\x03",

            "更主要的原因是这里临接山道，\x01",
            "军队是很难通行的。\x02\x03",

            "大门建造得比较小\x01",
            "大概也是出于这种考虑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x104,
        (
            "#030F#6P原来如此，和面对广阔大道的\x01",
            "哈肯大门确实是有所不同啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_24A8")

    ChrTalk(    #147
        0x106,
        (
            "#053F#5P就算是这样，\x01",
            "在堡垒门口养鸡… \x01",
            "也还真是前所未闻了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #148
        0x106,
        (
            "#051F#6P好了，咱们还是马上去\x01",
            "调查『地震』的事吧，\x02\x03",

            "首先要去和守备队长打个招呼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_254A")

    label("loc_24A8")


    ChrTalk(    #149
        0x103,
        (
            "#021F#5P呵呵，即使如此…\x01",
            "在堡垒门口养鸡…\x01",
            "还样的国境线还真是够随便啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #150
        0x103,
        (
            "#020F#6P好了，还是快点开始\x01",
            "调查『地震』的事吧。\x02\x03",

            "先去和守备队长打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254A")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #151
        0x101,
        "#1006F嗯，了解！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x140B)
    OP_28(0x6D, 0x4, 0x40)
    OP_28(0x85, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_16_2034 end

    def Function_17_2578(): pass

    label("Function_17_2578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2587")
    Call(0, 18)
    Jump("loc_25B8")

    label("loc_2587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25A0")
    Call(0, 19)
    Jump("loc_25B8")

    label("loc_25A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25B8")
    Call(0, 20)

    label("loc_25B8")

    Return()

    # Function_17_2578 end

    def Function_18_25B9(): pass

    label("Function_18_25B9")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2614")

    ChrTalk(    #152
        0x101,
        (
            "#1000F现在要抓紧时间\x01",
            "调查地震的事……\x02\x03",

            "先去和这里的队长\x01",
            "打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26EC")

    label("loc_2614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2686")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2631")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_2638")

    label("loc_2631")

    TurnDirection(0x106, 0x0, 400)

    label("loc_2638")


    ChrTalk(    #153
        0x106,
        (
            "#050F现在要赶快进行\x01",
            "地震的调查。\x02\x03",

            "首先从守备队长\x01",
            "快要需要试着听话了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26EC")

    label("loc_2686")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_269C")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_26A3")

    label("loc_269C")

    TurnDirection(0x103, 0x0, 400)

    label("loc_26A3")


    ChrTalk(    #154
        0x103,
        (
            "#020F现在要赶快\x01",
            "去调查地震的事情哦。\x02\x03",

            "先去和这里的队长\x01",
            "打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EC")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_18_25B9 end

    def Function_19_2708(): pass

    label("Function_19_2708")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2774")

    ChrTalk(    #155
        0x101,
        (
            "#1006F（喂……\x01",
            "　调查还没结束啊。)\x02\x03",

            "(休息所的人也不要漏掉，\x01",
            "　要探听出全部情报才行。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EE")

    label("loc_2774")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D9")

    ChrTalk(    #156
        0x105,
        (
            "#047F（调查还没完哦……）\x02\x03",

            "#040F（休息所里的人也要问到，\x01",
            "　情报收集得越多越好。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EE")

    label("loc_27D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283E")

    ChrTalk(    #157
        0x104,
        (
            "#030F（嗯……\x01",
            "　调查还没结束哦。)\x02\x03",

            "(休息所里的人也不要忘记，\x01",
            "　所有人都要问到。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EE")

    label("loc_283E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_289C")

    ChrTalk(    #158
        0x106,
        (
            "#555F（调查还没完成啊。）\x02\x03",

            "(要收集足够多的情报才行，\x01",
            "　休息所里的人也要问到。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EE")

    label("loc_289C")


    ChrTalk(    #159
        0x103,
        (
            "#020F（调查还没完成哦，）\x02\x03",

            "(休息所的人也不要漏掉，\x01",
            "　继续去探听一下情报吧。)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EE")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_19_2708 end

    def Function_20_290A(): pass

    label("Function_20_290A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2970")

    ChrTalk(    #160
        0x101,
        (
            "#1015F……虽然情报已经收集完了，\x01",
            "但还没有向队长报告呢。\x02\x03",

            "报告完毕后再回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A53")

    label("loc_2970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_29E5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298D")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_2994")

    label("loc_298D")

    TurnDirection(0x106, 0x0, 400)

    label("loc_2994")


    ChrTalk(    #161
        0x106,
        (
            "#050F调查算是告一段落了，\x01",
            "但还没向守备队长报告啊，\x02\x03",

            "报告之后再回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A53")

    label("loc_29E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29FB")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2A02")

    label("loc_29FB")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2A02")


    ChrTalk(    #162
        0x103,
        (
            "#020F调查虽然结束了，\x01",
            "但还没有向队长报告呢。\x02\x03",

            "过去做个报告之后\x01",
            "再回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A53")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_20_290A end

    def Function_21_2A6F(): pass

    label("Function_21_2A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A80")
    Call(0, 22)

    label("loc_2A80")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Fade(1000)
    SetChrPos(0x105, 1860, 0, 46170, 0)
    SetChrPos(0x101, 1500, 0, 47410, 0)
    SetChrPos(0xF7, 300, 0, 47400, 0)
    SetChrPos(0x104, 700, 0, 46200, 0)
    OP_6D(1210, 0, 47890, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #163
        0x8,
        "#5P呜啊啊啊～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        "#5P嗯？有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#1011F#4P啊……\x01",
            "我是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x105,
        (
            "#040F可以耽误您一点时间\x01",
            "配合我们做一个调查吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        "#5P啊……嗯，没问题……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #168
        (
            "\x07\x05询问是否在３天前地震的前后\x01",
            "遇到了什么奇怪的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #169
        0x8,
        "#5P啊啊～那次的地震啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        (
            "#5P我当时正在打磕睡，忽然感觉有晃动，\x01",
            "还以为副队长在推我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        "#5P但睁眼一看，周围谁都没有……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x8,
        (
            "#5P虽然之后明白是发生地震了。\x01",
            "但一开始还以为是有人在戏弄我呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#1019F#4P那个算是奇怪的事情吗……\x01",
            "明明只是你自己的工作态度问题而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x104,
        (
            "#035F呼～能站着睡着\x01",
            "也算是个了不起的特技了呢。\x02\x03",

            "#030F不过我也可以\x01",
            "躺在沙发上就轻轻松松\x01",
            "吃光一整套全餐呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2DC0")

    ChrTalk(    #175
        0x106,
        "#551F#6P这种事有什么值得骄傲啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DE6")

    label("loc_2DC0")


    ChrTalk(    #176
        0x103,
        "#025F#6P那种事有什么可自豪的嘛。\x02",
    )

    CloseMessageWindow()

    label("loc_2DE6")


    ChrTalk(    #177
        0x105,
        (
            "#542F除、除了那个之外\x01",
            "就没有别的发现了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        "#5P……我想想。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        (
            "#5P啊，对了，赫宁\x01",
            "他倒是问过我一件怪事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        "#1015F#4P怪事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x8,
        (
            "#5P那是在地震发生\x01",
            "的前一天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x8,
        (
            "#5P同班的赫宁忽然过来问我\x01",
            "有没有人通过大门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        (
            "#5P我告诉他没有以后，\x01",
            "他好像就显得很困惑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x105,
        "#043F这是怎么回事呢？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 5)), scpexpr(EXPR_END)), "loc_2F69")

    ChrTalk(    #185
        0x101,
        (
            "#1006F#4P也许他有什么发现也说不定。\x02\x03",

            "去找那个叫赫宁的士兵\x01",
            "再问一次吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FAB")

    label("loc_2F69")


    ChrTalk(    #186
        0x101,
        (
            "#1006F#4P也许他有什么发现也说不定。\x02\x03",

            "向那个士兵\x01",
            "打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FAB")

    OP_A2(0x1410)
    OP_28(0x85, 0x1, 0x100)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_21_2A6F end

    def Function_22_2FBB(): pass

    label("Function_22_2FBB")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3035"),
        (1, "loc_303B"),
        (SWITCH_DEFAULT, "loc_3041"),
    )


    label("loc_3035")

    OP_A2(0x1200)
    Jump("loc_3041")

    label("loc_303B")

    OP_A2(0x1201)
    Jump("loc_3041")

    label("loc_3041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_304F")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3053")

    label("loc_304F")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3053")

    Return()

    # Function_22_2FBB end

    def Function_23_3054(): pass

    label("Function_23_3054")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #187
        (
            "\x07\x05东　卡尔瓦德共和国\x01",
            "西　蔡斯市　２８０塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_3054 end

    def Function_24_30B2(): pass

    label("Function_24_30B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30BF")
    Return()

    label("loc_30BF")

    EventBegin(0x1)
    TurnDirection(0x9, 0x0, 400)
    OP_4A(0x9, 255)

    ChrTalk(    #188
        0x9,
        (
            "喂喂！\x01",
            "那边是共和国的领土了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        (
            "这种非常时期\x01",
            "别乱走啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_8C(0x9, 315, 0)
    OP_4B(0x9, 255)
    Return()

    # Function_24_30B2 end

    SaveToFile()

Try(main)
