from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Private Brahm',                        # 9
        'Private Henning',                      # 10
        'CWO Pace',                             # 11
        'Warrant Officer Gerwin',               # 12
        'Rufus',                                # 13
        'Wong',                                 # 14
        'Gundolf',                              # 15
        'Chicken',                              # 16
        'Chicken',                              # 17
        'Chicken',                              # 18
        'Chicken',                              # 19
        'Tratt Plains Road',                    # 20
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
        "Function_8_7AE",          # 08, 8
        "Function_9_7D4",          # 09, 9
        "Function_10_F2B",         # 0A, 10
        "Function_11_1185",        # 0B, 11
        "Function_12_118C",        # 0C, 12
        "Function_13_1AAE",        # 0D, 13
        "Function_14_1AB5",        # 0E, 14
        "Function_15_2482",        # 0F, 15
        "Function_16_27A9",        # 10, 16
        "Function_17_2E4C",        # 11, 17
        "Function_18_2E8D",        # 12, 18
        "Function_19_30AB",        # 13, 19
        "Function_20_33A4",        # 14, 20
        "Function_21_35CF",        # 15, 21
        "Function_22_3D17",        # 16, 22
        "Function_23_3DAF",        # 17, 23
        "Function_24_3E18",        # 18, 24
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD")
    OP_43(0xFE, 0x2, 0x0, 0x8)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_7AD")
    TalkBegin(0xFE)
    OP_A2(0x7)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00Received #907i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_7AD")

    Return()

    # Function_7_728 end

    def Function_8_7AE(): pass

    label("Function_8_7AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_8_7AE")

    label("loc_7C9")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_7AE end

    def Function_9_7D4(): pass

    label("Function_9_7D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E5")
    Call(0, 21)
    Return()

    label("loc_7E5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_96E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_804")
    OP_A2(0x8)

    label("loc_804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_890")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared 'Messenger of Love' in past chapter with high score\x01",      # 0
            "Did not\x01",                                                          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_884"),
        (1, "loc_88A"),
        (SWITCH_DEFAULT, "loc_890"),
    )


    label("loc_884")

    OP_A2(0x8)
    Jump("loc_890")

    label("loc_88A")

    OP_A3(0x8)
    Jump("loc_890")

    label("loc_890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F2")

    ChrTalk(    #1
        0xFE,
        "Phew!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I've been so on edge lately\x01",
            "that I'm getting tired...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "*yaaawn*\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_96B")

    label("loc_8F2")


    ChrTalk(    #4
        0xFE,
        (
            "I guess I've been so on edge lately\x01",
            "that it's wearing me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "*yaaawn* I can't stop...*yaaaaaawn*...yawning...\x02",
    )

    CloseMessageWindow()

    label("loc_96B")

    Jump("loc_F27")

    label("loc_96E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EA")

    ChrTalk(    #6
        0xFE,
        (
            "Th-This gate being stuck open is kind\x01",
            "of a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "I admit, this kills any desire to sleep.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_A69")

    label("loc_9EA")


    ChrTalk(    #8
        0xFE,
        "I-I hope the gate goes back to normal soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "With it stuck open like this I really\x01",
            "can't relax and snooze on the job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A69")

    Jump("loc_F27")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_B47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AD0")

    ChrTalk(    #10
        0xFE,
        (
            "Apparently there's almost no damage,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "Earthquakes are still scary.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B44")

    label("loc_AD0")


    ChrTalk(    #12
        0xFE,
        (
            "Apparently even Leiston Fortress got\x01",
            "hit by a quake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "I was so surprised that I'm completely awake now.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B44")

    Jump("loc_F27")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_D72")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B63")
    OP_A2(0x8)

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEF")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared 'Messenger of Love' in past chapter with high score\x01",      # 0
            "Did not\x01",                                                          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BE3"),
        (1, "loc_BE9"),
        (SWITCH_DEFAULT, "loc_BEF"),
    )


    label("loc_BE3")

    OP_A2(0x8)
    Jump("loc_BEF")

    label("loc_BE9")

    OP_A3(0x8)
    Jump("loc_BEF")

    label("loc_BEF")

    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_CC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C41")

    ChrTalk(    #14
        0xFE,
        "...Heehee... Faye... No, don't...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC2")

    label("loc_C41")

    SetChrName("Private Brahm")

    ChrTalk(    #15
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    SetChrName("Private Brahm")

    ChrTalk(    #16
        0xFE,
        "...Ehehe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Faye... No, don't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "People are...watching us...\x01",
            "Aaaaaah...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_CC2")

    Jump("loc_D6F")

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D09")
    SetChrName("Private Brahm")

    ChrTalk(    #19
        0xFE,
        "... *sniffle*... Faye...forgive me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D6F")

    label("loc_D09")


    ChrTalk(    #20
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "... *sniffle*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "Faye...forgive me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "I... I'm sorry... It was my fault...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D6F")

    Jump("loc_F27")

    label("loc_D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_DF5")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DB8")

    ChrTalk(    #24
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "Zzz...zzz...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF2")

    label("loc_DB8")


    ChrTalk(    #26
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "...Nnn...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Nothing...to re...port...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_DF2")

    Jump("loc_F27")

    label("loc_DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_END)), "loc_E3E")

    ChrTalk(    #29
        0xFE,
        "*yaaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Mmm... Nnmm... Maybe I'll take a nap here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F27")

    label("loc_E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_END)), "loc_E71")

    ChrTalk(    #31
        0xFE,
        "*yaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Did you meet Henning?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F27")

    label("loc_E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_END)), "loc_EE8")

    ChrTalk(    #33
        0xFE,
        "Henning will be in the break area, I bet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Slacking off on the second floor there\x01",
            "is his specialty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F27")

    label("loc_EE8")


    ChrTalk(    #35
        0xFE,
        "*yaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Mmm Nnmm...\x01",
            "Great weather again today, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F27")

    TalkEnd(0x8)
    Return()

    # Function_9_7D4 end

    def Function_10_F2B(): pass

    label("Function_10_F2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1070")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF0")

    ChrTalk(    #37
        0xFE,
        "Brahm's been yawning like crazy for a while now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "However, today at least, I'm not letting him\x01",
            "fall asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I-I don't wanna be alone in a situation\x01",
            "like this!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_106D")

    label("loc_FF0")


    ChrTalk(    #40
        0xFE,
        (
            "If Brahm falls asleep, I'll be the\x01",
            "only one on guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "If he falls asleep, I'm poking him with\x01",
            "my freakin' bayonet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106D")

    Jump("loc_1181")

    label("loc_1070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1115")

    ChrTalk(    #42
        0xFE,
        (
            "The Republic's on the other side over there, so\x01",
            "I doubt they'll do anything, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "B-Being this defenseless makes me REALLY nervous.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1181")

    label("loc_1115")


    ChrTalk(    #44
        0xFE,
        "B-Being this defenseless makes me REALLY nervous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "Phew! Haven't been this on edge in a long time.\x02",
    )

    CloseMessageWindow()

    label("loc_1181")

    TalkEnd(0xFE)
    Return()

    # Function_10_F2B end

    def Function_11_1185(): pass

    label("Function_11_1185")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_1185 end

    def Function_12_118C(): pass

    label("Function_12_118C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_132A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_123A")

    ChrTalk(    #46
        0xFE,
        (
            "Even with the earthquakes quieted down,\x01",
            "we still can't let our guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "The non-aggression pact signing ceremony\x01",
            "is scheduled to occur soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1327")

    label("loc_123A")


    ChrTalk(    #48
        0xFE,
        (
            "According to the central factory, the\x01",
            "earthquakes are over with, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I actually received a similar report from\x01",
            "army command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Regardless of the reasons, it does seem to\x01",
            "be true that the earthquakes have quieted down.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1327")

    Jump("loc_1AAA")

    label("loc_132A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_143F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(    #51
        0xFE,
        (
            "The earthquakes have been striking\x01",
            "as if aiming for critical facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "It's hard to think it's a coincidence...\x02",
    )

    CloseMessageWindow()
    Jump("loc_143C")

    label("loc_13B7")


    ChrTalk(    #53
        0xFE,
        "Leiston Fortress, this time, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "It's amazing how they can happen as if\x01",
            "they're aimed right for military facilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_143C")

    Jump("loc_1AAA")

    label("loc_143F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_157C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14DA")

    ChrTalk(    #55
        0xFE,
        (
            "Seems there was an earthquake even\x01",
            "at the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "We need to be sure to not let our\x01",
            "guard down and strengthen security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1579")

    label("loc_14DA")


    ChrTalk(    #57
        0xFE,
        (
            "Seems there was an earthquake\x01",
            "even at the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "There might be another one here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "We'll have to ensure we don't let our guard down.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1579")

    Jump("loc_1AAA")

    label("loc_157C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_END)), "loc_1992")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_END)), "loc_1621")

    ChrTalk(    #60
        0xFE,
        (
            "Putting aside the earthquake,\x01",
            "I don't think anything else's happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "If anything suspicious had happened,\x01",
            "I'd have reported it long ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_198F")

    label("loc_1621")


    ChrTalk(    #62
        0xFE,
        "What, do you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1002FYeah, we're with the Bracer Guild.\x02\x03",

            "We'd like you to help with our investigation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #64
        0xFE,
        "I don't mind, but...please keep it short.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x07\x05Estelle asked if anything suspicious had happened before\x01",
            "or after the earthquake.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #66
        0xFE,
        "Earthquake...? You mean the one three days ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "The day the earthquake happened\x01",
            "was just a normal day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "If anything suspicious had happened,\x01",
            "I'd have reported it long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1015FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x104,
        "#032FSeems this was a swing and a miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "Is that all you needed?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_18BB")

    ChrTalk(    #72
        0x106,
        (
            "#050FYeah, that's plenty.\x02\x03",

            "Sorry to disturb your work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_1914")

    label("loc_18BB")


    ChrTalk(    #73
        0x103,
        (
            "#027FYes, that's plenty.\x02\x03",

            "We're sorry to have disturbed you\x01",
            "during your job.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    label("loc_1914")


    ChrTalk(    #74
        0xFE,
        (
            "No problem. We're both on the job,\x01",
            "after all, aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Well, then, if you'll excuse me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x140E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_198F")
    OP_28(0x85, 0x1, 0x800)
    Jump("loc_198F")

    label("loc_198F")

    Jump("loc_1AAA")

    label("loc_1992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19D5")

    ChrTalk(    #76
        0xFE,
        "Unbelievable. The security here's terrible!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AAA")

    label("loc_19D5")


    ChrTalk(    #77
        0xFE,
        "Unbelievable. The security here's terrible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Even though we need to be enhancing security\x01",
            "in preparation for the signing ceremony...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Layabouts like these won't be able\x01",
            "to respond to an emergency.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1AAA")

    TalkEnd(0xB)
    Return()

    # Function_12_118C end

    def Function_13_1AAE(): pass

    label("Function_13_1AAE")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_1AAE end

    def Function_14_1AB5(): pass

    label("Function_14_1AB5")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_1AC2")
    OP_A2(0x4)

    label("loc_1AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B47")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Met Wong in previous game\x01",               # 0
            "Did not meet Wong in previous game\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B3B"),
        (1, "loc_1B41"),
        (SWITCH_DEFAULT, "loc_1B47"),
    )


    label("loc_1B3B")

    OP_A2(0x4)
    Jump("loc_1B47")

    label("loc_1B41")

    OP_A3(0x4)
    Jump("loc_1B47")

    label("loc_1B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 4)), scpexpr(EXPR_END)), "loc_1BA6")

    ChrTalk(    #80
        0xFE,
        "Shouldn't you hurry to Elmo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Please, be careful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D37")

    label("loc_1BA6")


    ChrTalk(    #82
        0xFE,
        "Hey, good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "I'm just on my way back to Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "You guys sure seem in a hurry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#1015FYeah, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #86
        (
            "\x07\x05Estelle explained that the source of the earthquakes was\x01",
            "discovered to be in Elmo Village.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #87
        0xFE,
        "Well, that's kinda freaky...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "Anyway, seems like you should hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "Be careful out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1006FYeah, we're gonna go.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1434)

    label("loc_1D37")

    Jump("loc_1DA4")

    label("loc_1D3A")


    ChrTalk(    #91
        0xFE,
        (
            "Sorry, but I hope you'll help\x01",
            "out around for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Let's both work together and do our best.\x02",
    )

    CloseMessageWindow()

    label("loc_1DA4")

    Jump("loc_247E")

    label("loc_1DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1FCC")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EEA")

    ChrTalk(    #93
        0xFE,
        "Hey, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "Do you remember me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1001FOf course!\x02\x03",

            "You're Wong, with the Zeiss branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "Haha, thanks. Glad we got to meet again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Looks like you managed to get\x01",
            "promoted to a full bracer, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Congrats. With your skills I expected\x01",
            "nothing less.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC9")

    label("loc_1EEA")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #99
        0xFE,
        "Oh, hey, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1004FHuh...?\x02\x03",

            "#1018FAh, I was wondering who it was.\x01",
            "Hey, Wong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Looks like you managed to get\x01",
            "promoted to a full bracer, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Congrats. With your skills I expected\x01",
            "nothing less.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC9")

    Jump("loc_2164")

    label("loc_1FCC")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #103
        0xFE,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "Aren't you Estelle, that recently promoted senior?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1004FUh, yeah, that's me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "Ah, 'scuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "I'm Wong. I'm with the Zeiss branch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1000FAh, I see.\x02\x03",

            "I'm Estelle Bright. Nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "Yeah, same here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "I've heard about your work here and there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "After all the successes you've had, it's\x01",
            "only natural you're a full bracer already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2164")


    ChrTalk(    #112
        0x101,
        (
            "#1008FAhaha, thank you.\x02\x03",

            "But, I'm still in training.\x01",
            "I've got a lot to learn still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Never forget the attitude of a\x01",
            "beginner, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Pretty admirable sentiment.\x01",
            "I hope I can follow your example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Incidentally, did you know Gundolf\x01",
            "is out on a job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1011FAh, yeah, I heard from Jean.\x02\x03",

            "We came to Zeiss in part to help\x01",
            "pitch in while he's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "Ah, got'cha. Thanks, that'll be a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Sorry for the trouble, but I hope you'll\x01",
            "help out around here for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_23B6")
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #119
        0xFE,
        (
            "Agate, looking forward to working\x01",
            "with you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x106,
        "#051FYeah, same here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_23B6")

    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #121
        0xFE,
        (
            "Scherazard, looking forward to working\x01",
            "with you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        "#020FYes, same here.\x02",
    )

    CloseMessageWindow()

    label("loc_2415")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #123
        0xFE,
        "I'll help out as best I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Well, then, let's all work\x01",
            "together and do our best.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1427)
    OP_A2(0x5)

    label("loc_247E")

    TalkEnd(0xD)
    Return()

    # Function_14_1AB5 end

    def Function_15_2482(): pass

    label("Function_15_2482")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_27A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2705")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #125
        0xFE,
        "Yo, Estelle, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Must be hard having to come all the way out here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1011FHey, Gundolf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        "#1040FIt's been a while.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2552")

    ChrTalk(    #129
        0x106,
        "#050FOn patrol?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_25C9")

    label("loc_2552")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2587")

    ChrTalk(    #130
        0x103,
        "#020FMaking the rounds?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_25C9")

    label("loc_2587")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C9")

    ChrTalk(    #131
        0x107,
        "#064FAre you in the middle of a patrol?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    label("loc_25C9")


    ChrTalk(    #132
        0xFE,
        "Yeah, more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Thought I'd put my legs to work and keep\x01",
            "an eye on things around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "Well, you guys can focus on your own mission.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "Leave the general upkeep to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#1002FYeah, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#1040FMuch appreciated.\x02\x03",

            "Well, then, pardon us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #138
        0xFE,
        "Yeah, best of luck to you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20D1)
    Jump("loc_27A5")

    label("loc_2705")


    ChrTalk(    #139
        0xFE,
        (
            "In the current situation, anything could\x01",
            "happen anywhere, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "I'm putting my legs to work and trying to\x01",
            "keep things as safe as I can around here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27A5")

    TalkEnd(0xFE)
    Return()

    # Function_15_2482 end

    def Function_16_27A9(): pass

    label("Function_16_27A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27BA")
    Call(0, 22)

    label("loc_27BA")

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

    def lambda_2848():
        OP_6D(3180, -500, 27340, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2848)

    def lambda_2860():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2860)
    OP_C8(0x200, 0x46, "C_PLAC09._CH", 0x0, 0x3E8)
    OP_DE("Wolf Fort")
    FadeToBright(1000, 0)
    Sleep(1000)

    def lambda_28A6():
        OP_8E(0xFE, 0xDC0, 0xFFFFFE0C, 0x4F9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28A6)
    Sleep(200)

    def lambda_28C6():
        OP_8E(0xFE, 0x87A, 0xFFFFFE0C, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_28C6)

    def lambda_28E1():
        OP_8E(0xFE, 0x8DE, 0xFFFFFE0C, 0x4844, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_28E1)

    def lambda_28FC():
        OP_8E(0xFE, 0xDE8, 0xFFFFFE0C, 0x49B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_28FC)
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
            "#1011FAnd here's the Wolf Fort.\x02\x03",

            "It's really peaceful here. I guess we don't\x01",
            "need to worry about Calvard invading us and\x01",
            "stealing our puppies or something, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x104,
        (
            "#033FQuite a difference compared to the Haken Gate.\x02\x03",

            "#035FOf course, unlike my 'glorious fatherland,'\x01",
            "Calvard and Liberl are easy friends.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2AE8")

    ChrTalk(    #143
        0x106,
        (
            "#552F#6PAnd Erebonia's done nothin' to\x01",
            "deserve different? Tch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_2AE8")


    ChrTalk(    #144
        0x103,
        "#025F#6PThere are reasons for that, you realize.\x02",
    )

    CloseMessageWindow()

    label("loc_2B1E")


    ChrTalk(    #145
        0x105,
        (
            "#542FI imagine our relationship with Calvard\x01",
            "has something to do with it. Although...\x02\x03",

            "Beyond the gate is a mountain pass\x01",
            "that would be difficult for a full army to\x01",
            "pass through.\x02\x03",

            "That's why the gate is so\x01",
            "small as well, as I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x104,
        (
            "#030FAh, yes. Far different from the Haken Gate,\x01",
            "which faces onto a great, open road.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D39")

    ChrTalk(    #147
        0x106,
        (
            "#053F#6PThe hell's with the chickens,\x01",
            "though? It's embarrassing...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #148
        0x106,
        (
            "#051F#6PAh, whatever. Let's get to\x01",
            "askin' some questions.\x02\x03",

            "We should probably say hi to\x01",
            "whoever's in charge first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1F")

    label("loc_2D39")


    ChrTalk(    #149
        0x103,
        (
            "#021F#6PI'm still not quite sure about the\x01",
            "free-range poultry, either way, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #150
        0x103,
        (
            "#020F#6PAnyway. Let's start asking around\x01",
            "about the earthquake, hmm?\x02\x03",

            "We should probably check in\x01",
            "with the guard commander first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1F")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #151
        0x101,
        "#1006F#4PRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x140B)
    OP_28(0x6D, 0x4, 0x40)
    OP_28(0x85, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_16_27A9 end

    def Function_17_2E4C(): pass

    label("Function_17_2E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5B")
    Call(0, 18)
    Jump("loc_2E8C")

    label("loc_2E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E74")
    Call(0, 19)
    Jump("loc_2E8C")

    label("loc_2E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E8C")
    Call(0, 20)

    label("loc_2E8C")

    Return()

    # Function_17_2E4C end

    def Function_18_2E8D(): pass

    label("Function_18_2E8D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2A")

    ChrTalk(    #152
        0x101,
        (
            "#1000FAnyway, we need to ask about the\x01",
            "earthquake that happened here...\x02\x03",

            "First we should hear what the commander\x01",
            "in charge has to say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_2F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2FE7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F47")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_2F4E")

    label("loc_2F47")

    TurnDirection(0x106, 0x0, 400)

    label("loc_2F4E")


    ChrTalk(    #153
        0x106,
        (
            "#050FAnyway, we need to ask about the\x01",
            "earthquake that happened here...\x02\x03",

            "Seems we should first probably ask the\x01",
            "guy in charge here what happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_2FE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FFD")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3004")

    label("loc_2FFD")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3004")


    ChrTalk(    #154
        0x103,
        (
            "#020FAnyway, we need to ask about the\x01",
            "earthquake that happened here...\x02\x03",

            "First we should hear what the commander\x01",
            "in charge has to say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308F")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_18_2E8D end

    def Function_19_30AB(): pass

    label("Function_19_30AB")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3147")

    ChrTalk(    #155
        0x101,
        (
            "#1006F(Ah... We're still not done investigating, huh.)\x02\x03",

            "(We should question everyone around,\x01",
            "including the people in the break area.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3388")

    label("loc_3147")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E5")

    ChrTalk(    #156
        0x105,
        (
            "#047F(We still haven't checked everything out yet...)\x02\x03",

            "#040F(We should question everyone around,\x01",
            "including the people in the break area.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3388")

    label("loc_31E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327C")

    ChrTalk(    #157
        0x104,
        (
            "#030F(Hmm... Our investigation is not yet perfect.)\x02\x03",

            "(We should question everyone around,\x01",
            "including the people in the break area.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3388")

    label("loc_327C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3305")

    ChrTalk(    #158
        0x106,
        (
            "#555F(We ain't finished investigatin' yet.)\x02\x03",

            "(We should question everyone around,\x01",
            "including the folks in the break area.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3388")

    label("loc_3305")


    ChrTalk(    #159
        0x103,
        (
            "#020F(We still aren't finished investigating.)\x02\x03",

            "(We should question everyone around,\x01",
            "including the people in the break area.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3388")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_19_30AB end

    def Function_20_33A4(): pass

    label("Function_20_33A4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3442")

    ChrTalk(    #160
        0x101,
        (
            "#1015F...We're done investigating, but we need\x01",
            "to report to the commander here.\x02\x03",

            "We can return to the guild after we\x01",
            "check in with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B3")

    label("loc_3442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_34FE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_345F")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_3466")

    label("loc_345F")

    TurnDirection(0x106, 0x0, 400)

    label("loc_3466")


    ChrTalk(    #161
        0x106,
        (
            "#050FWe're done with questionin', but we\x01",
            "haven't reported to the commander\x01",
            "here yet.\x02\x03",

            "We'll return to the guild once we've\x01",
            "checked in with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B3")

    label("loc_34FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3514")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_351B")

    label("loc_3514")

    TurnDirection(0x103, 0x0, 400)

    label("loc_351B")


    ChrTalk(    #162
        0x103,
        (
            "#020FWe're done with our interviews, but we\x01",
            "haven't reported to the commander\x01",
            "here yet.\x02\x03",

            "We'll return to the guild once we've\x01",
            "checked in with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B3")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_20_33A4 end

    def Function_21_35CF(): pass

    label("Function_21_35CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35E0")
    Call(0, 22)

    label("loc_35E0")

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
        "#6P*yaaaaaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        "#6PHnnn? 'Sup?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1011F#4PUm... We're from the Bracer Guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x105,
        (
            "#2P#040FI hope we're not disturbing you, but\x01",
            "could you answer some questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        "#6POh, uh, sure...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #168
        (
            "\x07\x05Estelle asked the soldier about any odd things he\x01",
            "might have seen when the earthquake happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #169
        0x8,
        "#6POdd things? Hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        (
            "#6PI was...uh, checking the light-blocking abilities\x01",
            "of my hat when the quake hit. I thought the\x01",
            "chief was yelling at me at first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        "#6PBut, no, I didn't see anyone around...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x8,
        (
            "#6PI mean, I thought it was a prank\x01",
            "at first, not an earthquake.\x01",
            "Wasn't really all that strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#1019F#4PThis isn't so much a strange occurrence\x01",
            "as it is an admission that you're awful\x01",
            "at your job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x104,
        (
            "#035FAh, but to sleep standing?\x01",
            "That is a rare skill, Estelle.\x02\x03",

            "#030FI, however, can consume an entire\x01",
            "full-course meal while asleep on a sofa!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3A3E")

    ChrTalk(    #175
        0x106,
        (
            "#551F#6PWhy the hell are you trying\x01",
            "to brag about that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A78")

    label("loc_3A3E")


    ChrTalk(    #176
        0x103,
        (
            "#025F#6PThat's not something to brag about,\x01",
            "Lenheim.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A78")


    ChrTalk(    #177
        0x105,
        (
            "#2P#542FSo, um. Was there anything else\x01",
            "you can remember? At all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        "#6PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        (
            "#6PActually, Henning said he\x01",
            "saw somethin' weird, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        "#1015F#4PSomething weird?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x8,
        (
            "#6PWell, this was the day BEFORE\x01",
            "the earthquake, mind you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x8,
        (
            "#6POne of the other guards here,\x01",
            "Henning, asked if anyone'd\x01",
            "passed through the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        (
            "#6PWhen I told him I hadn't seen anyone,\x01",
            "he just shook his head...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x105,
        (
            "#2P#043FWell, that's curious.\x01",
            "I wonder what that was about.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 5)), scpexpr(EXPR_END)), "loc_3CAE")

    ChrTalk(    #185
        0x101,
        (
            "#1006F#4PHe might be able to tell us something.\x02\x03",

            "Let's go talk to Henning again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D07")

    label("loc_3CAE")


    ChrTalk(    #186
        0x101,
        (
            "#1006F#4PHe might be able to tell us something.\x02\x03",

            "Let's go talk to this Henning guy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D07")

    OP_A2(0x1410)
    OP_28(0x85, 0x1, 0x100)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_21_35CF end

    def Function_22_3D17(): pass

    label("Function_22_3D17")

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
        (0, "loc_3D90"),
        (1, "loc_3D96"),
        (SWITCH_DEFAULT, "loc_3D9C"),
    )


    label("loc_3D90")

    OP_A2(0x1200)
    Jump("loc_3D9C")

    label("loc_3D96")

    OP_A2(0x1201)
    Jump("loc_3D9C")

    label("loc_3D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3DAA")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3DAE")

    label("loc_3DAA")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3DAE")

    Return()

    # Function_22_3D17 end

    def Function_23_3DAF(): pass

    label("Function_23_3DAF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #187
        (
            "\x07\x05East: Calvard Republic\x01",
            "West: City of Zeiss - 280 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_3DAF end

    def Function_24_3E18(): pass

    label("Function_24_3E18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E25")
    Return()

    label("loc_3E25")

    EventBegin(0x1)
    TurnDirection(0x9, 0x0, 400)
    OP_4A(0x9, 255)

    ChrTalk(    #188
        0x9,
        "H-Hey! That way's Republican territory!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        (
            "Please don't do such careless things\x01",
            "in an emergency like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_8C(0x9, 315, 0)
    OP_4B(0x9, 255)
    Return()

    # Function_24_3E18 end

    SaveToFile()

Try(main)
