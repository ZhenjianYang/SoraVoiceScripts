from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4150   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4150.x',
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
        'Olivier',                              # 9
        'Soldier',                              # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Grancel - North Block',                # 18
        'Royal Avenue',                         # 19
        'Grancel - East Block',                 # 20
        'Grancel - West Block',                 # 21
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 4200,
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT07/CH00102 ._CH',             # 01
        'ED6_DT07/CH00133 ._CH',             # 02
        'ED6_DT07/CH00107 ._CH',             # 03
        'ED6_DT07/CH01650 ._CH',             # 04
        'ED6_DT07/CH01620 ._CH',             # 05
        'ED6_DT07/CH01490 ._CH',             # 06
        'ED6_DT07/CH01180 ._CH',             # 07
        'ED6_DT07/CH01270 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01150 ._CH',             # 0C
        'ED6_DT07/CH01160 ._CH',             # 0D
        'ED6_DT07/CH01470 ._CH',             # 0E
        'ED6_DT07/CH01060 ._CH',             # 0F
        'ED6_DT07/CH01200 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT07/CH01100 ._CH',             # 12
        'ED6_DT07/CH01320 ._CH',             # 13
        'ED6_DT07/CH01640 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH00102P._CP',             # 01
        'ED6_DT07/CH00133P._CP',             # 02
        'ED6_DT07/CH00107P._CP',             # 03
        'ED6_DT07/CH01650P._CP',             # 04
        'ED6_DT07/CH01620P._CP',             # 05
        'ED6_DT07/CH01490P._CP',             # 06
        'ED6_DT07/CH01180P._CP',             # 07
        'ED6_DT07/CH01270P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01150P._CP',             # 0C
        'ED6_DT07/CH01160P._CP',             # 0D
        'ED6_DT07/CH01470P._CP',             # 0E
        'ED6_DT07/CH01060P._CP',             # 0F
        'ED6_DT07/CH01200P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT07/CH01100P._CP',             # 12
        'ED6_DT07/CH01320P._CP',             # 13
        'ED6_DT07/CH01640P._CP',             # 14
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        X                   = 5270,
        Y                   = -1000,
        Z                   = -67700,
        Range               = -6090,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF0182,
        Unknown_18          = 0x0,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )


    ScpFunction(
        "Function_0_3D2",          # 00, 0
        "Function_1_44C",          # 01, 1
        "Function_2_606",          # 02, 2
        "Function_3_61C",          # 03, 3
        "Function_4_1070",         # 04, 4
        "Function_5_1137",         # 05, 5
        "Function_6_172C",         # 06, 6
        "Function_7_189A",         # 07, 7
        "Function_8_1B6B",         # 08, 8
        "Function_9_224D",         # 09, 9
        "Function_10_24B1",        # 0A, 10
        "Function_11_251F",        # 0B, 11
        "Function_12_258D",        # 0C, 12
        "Function_13_25D3",        # 0D, 13
        "Function_14_2619",        # 0E, 14
        "Function_15_265F",        # 0F, 15
        "Function_16_26CD",        # 10, 16
        "Function_17_2A7B",        # 11, 17
        "Function_18_2B1C",        # 12, 18
        "Function_19_2C71",        # 13, 19
        "Function_20_2D92",        # 14, 20
        "Function_21_2EC3",        # 15, 21
        "Function_22_3072",        # 16, 22
        "Function_23_3195",        # 17, 23
        "Function_24_32E0",        # 18, 24
        "Function_25_33E9",        # 19, 25
        "Function_26_3545",        # 1A, 26
        "Function_27_3630",        # 1B, 27
        "Function_28_364C",        # 1C, 28
        "Function_29_3650",        # 1D, 29
        "Function_30_3654",        # 1E, 30
        "Function_31_3658",        # 1F, 31
        "Function_32_365C",        # 20, 32
    )


    def Function_0_3D2(): pass

    label("Function_0_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3E0")
    OP_A3(0x3FA)
    Event(0, 5)

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3F3")
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 7)

    label("loc_3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_401")
    OP_A3(0x3FC)
    Event(0, 16)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_40F")
    OP_A3(0x3FD)
    Event(0, 17)

    label("loc_40F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_41F"),
        (103, "loc_435"),
        (SWITCH_DEFAULT, "loc_44B"),
    )


    label("loc_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_432")
    OP_A2(0x608)
    Event(0, 3)

    label("loc_432")

    Jump("loc_44B")

    label("loc_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448")
    OP_A2(0x629)
    Event(0, 8)

    label("loc_448")

    Jump("loc_44B")

    label("loc_44B")

    Return()

    # Function_0_3D2 end

    def Function_1_44C(): pass

    label("Function_1_44C")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x3005B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46F")
    OP_1C(0x10, 0x0, 0x4)

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47F")
    OP_1B(0x0, 0x0, 0x12)
    Jump("loc_51C")

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_498")
    OP_1B(0x0, 0x0, 0x6)
    Jump("loc_51C")

    label("loc_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AC")
    OP_1B(0x0, 0x0, 0x13)
    Jump("loc_51C")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C0")
    OP_1B(0x0, 0x0, 0x14)
    Jump("loc_51C")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D4")
    OP_1B(0x0, 0x0, 0x15)
    Jump("loc_51C")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E8")
    OP_1B(0x0, 0x0, 0x16)
    Jump("loc_51C")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FC")
    OP_1B(0x0, 0x0, 0x17)
    Jump("loc_51C")

    label("loc_4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_510")
    OP_1B(0x0, 0x0, 0x18)
    Jump("loc_51C")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_51C")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_51C")

    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_605")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_43(0xB, 0x1, 0x0, 0x9)
    OP_43(0xC, 0x1, 0x0, 0x9)
    OP_43(0xD, 0x1, 0x0, 0x9)
    OP_43(0xE, 0x1, 0x0, 0x9)
    OP_43(0xF, 0x1, 0x0, 0x9)
    OP_43(0x10, 0x1, 0x0, 0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_599")

    label("loc_599")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_5A4")

    label("loc_5A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_5C1")
    SetChrFlags(0xE, 0x80)
    OP_44(0xE, 0xFF)
    SetChrFlags(0xF, 0x80)
    OP_44(0xF, 0xFF)

    label("loc_5C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_5DE")
    SetChrFlags(0xB, 0x80)
    OP_44(0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    OP_44(0xC, 0xFF)

    label("loc_5DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_5F2")
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0xFF)

    label("loc_5F2")

    OP_6B(4200, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_605")

    Return()

    # Function_1_44C end

    def Function_2_606(): pass

    label("Function_2_606")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_606")

    label("loc_61B")

    Return()

    # Function_2_606 end

    def Function_3_61C(): pass

    label("Function_3_61C")

    EventBegin(0x0)
    OP_6D(600, 250, 1950, 0)
    OP_67(0, 17690, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(571, 0)
    SetChrPos(0x101, -340, 0, -51790, 0)
    SetChrPos(0x102, -1140, 0, -53240, 0)
    SetChrPos(0x10E, 710, 0, -53630, 0)

    def lambda_694():
        OP_6D(-450, 290, -49040, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_694)

    def lambda_6AC():
        OP_6B(3600, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6AC)

    def lambda_6BC():
        OP_67(0, 6190, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6BC)

    def lambda_6D4():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6D4)

    def lambda_6E4():
        OP_6E(262, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E4)
    Sleep(8500)

    ChrTalk(    #0
        0x101,
        (
            "#000FWow...\x01",
            "This city's freakin' HUGE.\x02\x03",

            "Dad used to take me here a long\x01",
            "time ago, but was it really this\x01",
            "big then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#010FWell, it is the biggest city\x01",
            "in the kingdom.\x02\x03",

            "Grancel Castle's just past the\x01",
            "main road. That's where the\x01",
            "queen lives.\x02\x03",

            "There's also the Grancel Cathedral, the\x01",
            "Grand Arena, and all the embassies\x01",
            "for the surrounding nations.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #2
        0x101,
        (
            "#000FHuh... You don't say.\x02\x03",

            "You sure know a lot\x01",
            "about this city.\x02\x03",

            "You must have been here\x01",
            "before, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #3
        0x102,
        (
            "#010FYes...\x01",
            "When I was little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10E,
        (
            "#130FMy... No matter how many times\x01",
            "I see it, this city still amazes\x01",
            "me with its beauty.\x02\x03",

            "Purely in terms of scale, I believe the\x01",
            "Imperial and Republican capitals are larger...\x02\x03",

            "...but neither feels as elegant\x01",
            "and refined as Grancel does.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EE():
        TurnDirection(0xFE, 0x10E, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9EE)
    TurnDirection(0x101, 0x10E, 400)

    ChrTalk(    #5
        0x101,
        (
            "#000FHa ha, I'm glad to hear it. It's nice to hear\x01",
            "a foreigner complimenting your home country.\x02\x03",

            "Which reminds me... What do you\x01",
            "plan to do now, Professor?\x02\x03",

            "Are you going to be okay with\x01",
            "staying in a hotel?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(    #6
        0x10E,
        (
            "#130FHa ha. I have something\x01",
            "else in mind.\x02\x03",

            "I intend to go bug the folks\x01",
            "at the History Museum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#000FOh, cool.\x01",
            "Grancel has one of those?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#010FThey find ancient artifacts and\x01",
            "put them on display there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10E,
        (
            "#130FYes, and I'll be staying there\x01",
            "as a guest associate member.\x02\x03",

            "You two should stop by to visit,\x01",
            "if you get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#000FEhhh... Museums are awfully\x01",
            "formal for my tastes...\x02\x03",

            "If we do come by, are you going\x01",
            "to give us a bunch of lessons?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10E,
        (
            "#130FHeh heh heh... If that is your \x01",
            "wish, then I shall certainly do\x01",
            "my best.\x02\x03",

            "Just kidding...though I do\x01",
            "think that checking out all\x01",
            "the exhibits would be fun.\x02\x03",

            "Now, if you'll excuse me...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D76():

        label("loc_D76")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_D76")

    QueueWorkItem2(0x101, 1, lambda_D76)

    def lambda_D87():

        label("loc_D87")

        TurnDirection(0xFE, 0x10E, 0)
        OP_48()
        Jump("loc_D87")

    QueueWorkItem2(0x102, 1, lambda_D87)
    OP_8E(0x10E, 0xF78, 0x0, 0xFFFF3D78, 0x7D0, 0x0)

    def lambda_DAC():
        OP_8E(0xFE, 0x1356, 0x0, 0xFFFF76E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_DAC)

    def lambda_DC7():
        OP_6D(-1030, 0, -52400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC7)
    Sleep(2000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(    #12
        0x101,
        (
            "#000F*sigh*... Well, he's just as\x01",
            "happy-go-lucky as ever...\x02\x03",

            "What's this 'guest associate' thing,\x01",
            "though...? Is he a famous scholar\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#010FYes, most likely.\x02\x03",

            "Now...we should probably stop in\x01",
            "at the local guild branch before\x01",
            "we do anything else.\x02\x03",

            "Not only do we need to change our branch\x01",
            "affiliation, but we can discuss there how to\x01",
            "approach delivering the professor's message.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #14
        0x101,
        (
            "#000FHmm...\x01",
            "Yeah, you're right.\x02\x03",

            "Thinking about it, how are we even going to get\x01",
            "an audience with Her Majesty, anyway?\x02\x03",

            "And there's no way that'll be as\x01",
            "simple as just walking up to the\x01",
            "castle and saying, 'Hi.'\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10E, -100, 0, -52250, 0)
    SetChrFlags(0x10E, 0x80)
    EventEnd(0x0)
    RemoveParty(0xD, 0xFF)
    Return()

    # Function_3_61C end

    def Function_4_1070(): pass

    label("Function_4_1070")

    EventBegin(0x0)
    OP_6D(16030, 500, 7220, 1000)

    ChrTalk(    #15
        0x101,
        (
            "#000FOh...\x02\x03",

            "Is that a piano...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#010FYes. Not just a record, either.\x01",
            "It sounds like someone's playing\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#000FI've got a bad feeling about this...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1070 end

    def Function_5_1137(): pass

    label("Function_5_1137")

    EventBegin(0x0)
    OP_6D(16020, 250, 7280, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x101, 15830, 740, 8470, 0)
    SetChrPos(0x102, 15830, 740, 8470, 0)
    SetChrPos(0x8, 15830, 740, 8470, 0)
    OP_0D()
    OP_70(0x10, 0x3C)
    OP_73(0x10)

    def lambda_1198():
        OP_8E(0xFE, 0x3B7E, 0xFA, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1198)
    Sleep(400)

    def lambda_11B8():
        OP_8E(0xFE, 0x4060, 0xFA, 0xE6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11B8)
    Sleep(500)

    def lambda_11D8():
        OP_8E(0xFE, 0x3E9E, 0xFA, 0x14FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11D8)
    OP_6D(16100, 250, 4400, 2000)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #18
        0x101,
        (
            "#000FHow is it 'a matter of course'\x01",
            "for you to come with us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#030FHa ha ha...\x01",
            "Please, don't be cruel.\x02\x03",

            "Beyond my uses as a traveling\x01",
            "companion, I also wish to\x01",
            "assist in the manhunt.\x02\x03",

            "Unless, of course...you two\x01",
            "want to be alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#000FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#030FOh, my...\x01",
            "Such an unsophisticated child.\x02\x03",

            "But when you blossom to your full\x01",
            "potential, you shall be a woman\x01",
            "to be reckoned with.\x02\x03",

            "...Ha ha. And quite a desirable\x01",
            "one, I'd wager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#010F???\x02\x03",

            "What are you trying to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "#030FHa ha ha, well...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 1)

    ChrTalk(    #25
        0x101,
        "#000FHi-YAH!\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x0, 0x7, 0x7D0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 2)

    ChrTalk(    #26 op#5
        0x8,
        "#030FAaaaiiiieeeee...!\x05\x02",
    )


    def lambda_1486():
        OP_8F(0xFE, 0x3DD6, 0x2E4, 0x2116, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1486)
    OP_99(0x101, 0x7, 0xC, 0x7D0)
    Sleep(1000)

    ChrTalk(    #27
        0x8,
        "Yow! What the--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "Sir! Speak to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "No good...\x01",
            "He's not waking up.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x102,
        (
            "#010FEstelle...\x02\x03",

            "You know, no matter how angry someone\x01",
            "makes you, you're not allowed to brain\x01",
            "them. Especially not in public...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 3)
    SetChrFlags(0x101, 0x2)
    OP_99(0x101, 0x0, 0x13, 0x7D0)

    ChrTalk(    #31
        0x101,
        (
            "#000F...It was all flash, no impact.\x02\x03",

            "I didn't do any real damage.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)

    ChrTalk(    #32
        0x8,
        (
            "#030FHa ha ha... It seems...that Estelle\x01",
            "is a very shy individual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#010FWell, he doesn't SEEM to be hurt...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D9")

    ChrTalk(    #34
        0x101,
        (
            "#000FOkay, let's get back to searching.\x02\x03",

            "Next stop is the embassy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1729")

    label("loc_16D9")


    ChrTalk(    #35
        0x101,
        (
            "#000FOkay, let's get back to searching.\x02\x03",

            "Next up is the Erbe Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1729")

    EventEnd(0x0)
    Return()

    # Function_5_1137 end

    def Function_6_172C(): pass

    label("Function_6_172C")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A2")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #36
        0x102,
        (
            "#010FWe still don't know where Zin is.\x02\x03",

            "I think we should go over to\x01",
            "the Calvardian embassy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1895")

    label("loc_17A2")

    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #37
        0x101,
        (
            "#000FOh, right...\x02\x03",

            "Didn't he say he'd probably\x01",
            "be out drinking?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #38
        0x102,
        (
            "#010FYes, I believe that's what\x01",
            "Elnan said.\x02\x03",

            "Just to make sure, let's check the\x01",
            "bar on the main street before we\x01",
            "head out to the Erbe Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1895")

    Call(0, 27)
    Return()

    # Function_6_172C end

    def Function_7_189A(): pass

    label("Function_7_189A")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(16020, 250, 7280, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, 15830, 740, 8470, 0)
    SetChrPos(0x102, 15830, 740, 8470, 0)
    OP_0D()
    OP_70(0xD, 0x3B)
    OP_73(0xD)

    def lambda_18E8():
        OP_8E(0xFE, 0x3B7E, 0xFA, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18E8)
    Sleep(400)

    def lambda_1908():
        OP_8E(0xFE, 0x4060, 0xFA, 0xE6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1908)
    OP_6D(16100, 250, 4400, 2000)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 270, 400)
    Fade(1000)
    OP_6B(3000, 0)
    OP_0D()

    ChrTalk(    #39
        0x101,
        (
            "#008FUuugh...\x01",
            "I think I'm gonna burst.\x02\x03",

            "#007FI can't believe those guys are\x01",
            "actually drinking after a meal\x01",
            "like that.\x02\x03",

            "They must fill up from the legs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#019FWell, Zin's got the constitution\x01",
            "for it, and Olivier's just kind\x01",
            "of a glutton.\x02\x03",

            "As long as it doesn't interfere with\x01",
            "Zin's performance in the tournament\x01",
            "tomorrow, I think it'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#006FYeah... I guess worrying about\x01",
            "it won't do any good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#010FYou want to go to the hotel\x01",
            "on the North Block?\x02\x03",

            "Our room should be ready\x01",
            "by now...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_189A end

    def Function_8_1B6B(): pass

    label("Function_8_1B6B")

    EventBegin(0x0)
    OP_6F(0x1, 60)
    SetChrPos(0x101, 8940, 250, -12710, 270)
    SetChrPos(0x102, 8980, 250, -13870, 270)
    SetChrPos(0x9, 1930, 0, -4430, 0)
    SetChrPos(0xA, 1040, 0, -5320, 0)
    SetChrChipByIndex(0x9, 20)
    SetChrChipByIndex(0xA, 20)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(9320, 440, -13270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToDark(0, 0, -1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1500)
    FadeToBright(1500, 0)
    OP_72(0x1, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x800)
    OP_0D()

    ChrTalk(    #43
        0x101,
        "#6P#004FWow, it's late...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#010FWe should probably get back\x01",
            "to the hotel.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #45
        0x9,
        "A man's voice",
        "#4PHey! You two!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1CED():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CED)

    def lambda_1CFB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CFB)

    def lambda_1D09():
        OP_6D(8710, 250, -11760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D09)

    def lambda_1D21():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D21)

    def lambda_1D31():
        OP_8E(0xFE, 0x1B76, 0xFA, 0xFFFFD724, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D31)
    Sleep(300)

    def lambda_1D51():
        OP_8E(0xFE, 0x1720, 0x0, 0xFFFFD314, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D51)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #46
        0x101,
        (
            "#004FHm? Oh...\x01",
            "What's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        "#1PWe're on patrol.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#1PNighttime patrols have been\x01",
            "increased as part of the\x01",
            "counter-terrorism measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "#1PSo it's best to avoid going out\x01",
            "after 9 o'clock, if at all possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        "#1PYou two should go on home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#509FDon't you think that's a little\x01",
            "obnoxious? What if you NEED to\x01",
            "go out after 9 o'clock?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        (
            "#1PIt's the higher-ups who make\x01",
            "the decisions, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#1PSorry to cause any trouble, but\x01",
            "everyone has to abide by the rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#1PBy the way, where is it that\x01",
            "you two live?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#010FWe're staying at the hotel on\x01",
            "the North Block.\x02\x03",

            "We'll be there for the duration\x01",
            "of the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        "#1PHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "#1PHold on a second... I could\x01",
            "swear I've seen you two\x01",
            "somewhere before...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0x9,
        "#3S#1PHey!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        "#1PThese kids are in the tournament!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        "#1PYou know, now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#501FOh! Were you guys in\x01",
            "the audience?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        (
            "#1PHa ha... Well, we were on\x01",
            "security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        "#1PThat match today was pretty incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        "#1PTomorrow's the championship, no?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "#1PWe'll escort you to the hotel, so\x01",
            "you can rest up for your big fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#008FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        "#010FVery well. We accept.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1B6B end

    def Function_9_224D(): pass

    label("Function_9_224D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B0")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2280")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_2280")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22A6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_22A6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22CC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_22CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22F3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_22F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2319")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_2319")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_233F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_233F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2364")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_2364")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2389")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239D")

    label("loc_2389")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_239D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24AD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249E")

    ChrTalk(    #68
        0xFE,
        "What do you think you're doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#580F(Ah, crap...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        "#017F(Caught already...)\x02",
    )

    CloseMessageWindow()

    label("loc_249E")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_24AD")

    Jump("Function_9_224D")

    label("loc_24B0")

    Return()

    # Function_9_224D end

    def Function_10_24B1(): pass

    label("Function_10_24B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_251E")
    SetChrPos(0xFE, -29750, 250, -16079, 270)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0x2EEA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE0B6, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF8BCA, 0xFA, 0xFFFFC131, 0xBB8, 0x0)
    Jump("Function_10_24B1")

    label("loc_251E")

    Return()

    # Function_10_24B1 end

    def Function_11_251F(): pass

    label("Function_11_251F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_258C")
    SetChrPos(0xFE, -29910, 250, -23870, 270)
    OP_8E(0xFE, 0xFFFFDF08, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDE2C, 0xFA, 0xFFFF7D88, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF08, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF8B2A, 0xFA, 0xFFFFA2C2, 0xBB8, 0x0)
    Jump("Function_11_251F")

    label("loc_258C")

    Return()

    # Function_11_251F end

    def Function_12_258D(): pass

    label("Function_12_258D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25D2")
    SetChrPos(0xFE, -6720, 0, -19860, 270)
    OP_8E(0xFE, 0xFFFF8620, 0x0, 0xFFFFB26C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFE5C0, 0x0, 0xFFFFB26C, 0xBB8, 0x0)
    Jump("Function_12_258D")

    label("loc_25D2")

    Return()

    # Function_12_258D end

    def Function_13_25D3(): pass

    label("Function_13_25D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2618")
    SetChrPos(0xFE, 3810, 0, 10100, 180)
    OP_8E(0xFE, 0xEE2, 0x0, 0xFFFF7518, 0xBB8, 0x0)
    OP_8E(0xFE, 0xEE2, 0x0, 0x2774, 0xBB8, 0x0)
    Jump("Function_13_25D3")

    label("loc_2618")

    Return()

    # Function_13_25D3 end

    def Function_14_2619(): pass

    label("Function_14_2619")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_265E")
    SetChrPos(0xFE, -3690, 0, -34890, 180)
    OP_8E(0xFE, 0xFFFFF196, 0x0, 0x25DA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF196, 0x0, 0xFFFF77B6, 0xBB8, 0x0)
    Jump("Function_14_2619")

    label("loc_265E")

    Return()

    # Function_14_2619 end

    def Function_15_265F(): pass

    label("Function_15_265F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26CC")
    SetChrPos(0xFE, -1740, 0, -6830, 180)
    OP_8E(0xFE, 0xFFFFF934, 0x0, 0xFFFFAF1A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7F8, 0x0, 0xFFFFAE66, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7F8, 0x0, 0xFFFFE4B2, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF934, 0x0, 0xFFFFE552, 0xBB8, 0x0)
    Jump("Function_15_265F")

    label("loc_26CC")

    Return()

    # Function_15_265F end

    def Function_16_26CD(): pass

    label("Function_16_26CD")

    EventBegin(0x0)
    RemoveParty(0x0, 0xFF)
    AddParty(0x3, 0xFF)
    FadeToBright(2000, 0)
    OP_6D(-90, 0, -64700, 0)
    OP_67(0, 6090, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(196000, 0)
    OP_6E(372, 0)
    SetChrPos(0x104, -190, 0, -63320, 197)
    SetChrPos(0x102, 560, 0, -64300, 200)
    SetChrPos(0x108, -890, 0, -64430, 197)

    def lambda_2754():
        OP_8E(0xFE, 0x96, 0x0, 0xFFFF2C8E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2754)

    def lambda_276F():
        OP_8E(0xFE, 0x3F2, 0x0, 0xFFFF2702, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_276F)

    def lambda_278A():
        OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0xFFFF25F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_278A)
    OP_6D(280, 0, -55900, 3000)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 0, 400)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #71
        0x102,
        (
            "#010F...No patrols, but there's still\x01",
            "a lot of tension in the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x108,
        (
            "#070FHm... It's certainly loud enough.\x02\x03",

            "The atmosphere's obviously\x01",
            "different from yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x104,
        (
            "#030FPerhaps I can help loosen them up\x01",
            "with the dulcet tones of my lute...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28C2():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_28C2)
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(    #74
        0x102,
        (
            "#010FYou do anything conspicuous and\x01",
            "that guy will be on you faster than\x01",
            "you can say, 'off-key.'\x02\x03",

            "'Mueller,' wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x104,
        (
            "#030FY-Yes, it was...\x02\x03",

            "Ah... We should definitely...MUST, rather,\x01",
            "NOT go near the Erebonian embassy. It could be\x01",
            "quite dangerous. Yes! Quite perilous, indeed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x108,
        (
            "#070FHa ha... Well, we don't have\x01",
            "time to just drop by there.\x02\x03",

            "Once preparations are complete,\x01",
            "we have to get inside the sewers.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_26CD end

    def Function_17_2A7B(): pass

    label("Function_17_2A7B")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-1140, 0, -63570, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(320000, 0)
    OP_6E(580, 0)

    def lambda_2ADD():
        OP_6D(-20, 250, 7140, 20000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2ADD)

    def lambda_2AF5():
        OP_6C(0, 20000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2AF5)
    Sleep(17000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2A7B end

    def Function_18_2B1C(): pass

    label("Function_18_2B1C")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDB")
    OP_A2(0x0)

    ChrTalk(    #77
        0x102,
        (
            "#010FFirst, we should stop in at\x01",
            "the local guild branch.\x02\x03",

            "We can start the registration\x01",
            "process and also see about\x01",
            "the professor's request.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #78
        0x101,
        "#000FOkay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C6C")

    label("loc_2BDB")


    ChrTalk(    #79
        0x102,
        (
            "#010FFirst, we should stop in at\x01",
            "the local guild branch.\x02\x03",

            "We can start the registration\x01",
            "process and also see about\x01",
            "the professor's request.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6C")

    Call(0, 27)
    Return()

    # Function_18_2B1C end

    def Function_19_2C71(): pass

    label("Function_19_2C71")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1D")
    OP_A2(0x0)

    ChrTalk(    #80
        0x102,
        (
            "#010FCome on, let's go to\x01",
            "the guild branch.\x02\x03",

            "If we waste too much time, it'll\x01",
            "be night before you know it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #81
        0x101,
        "#006FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D8D")

    label("loc_2D1D")


    ChrTalk(    #82
        0x102,
        (
            "#010FCome on, let's go to\x01",
            "the guild branch.\x02\x03",

            "If we waste too much time, it'll\x01",
            "be night before you know it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D8D")

    Call(0, 27)
    Return()

    # Function_19_2C71 end

    def Function_20_2D92(): pass

    label("Function_20_2D92")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E54")
    OP_A2(0x0)

    ChrTalk(    #83
        0x102,
        (
            "#010FIt's late... We should just\x01",
            "go back to the hotel.\x02\x03",

            "We really need to get what\x01",
            "rest we can.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #84
        0x101,
        (
            "#000FLet's see... The hotel is in\x01",
            "the North Block, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EBE")

    label("loc_2E54")


    ChrTalk(    #85
        0x102,
        (
            "#010FIt's late... We should just\x01",
            "go back to the hotel.\x02\x03",

            "We need to rest up for\x01",
            "tomorrow's big match.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBE")

    Call(0, 27)
    Return()

    # Function_20_2D92 end

    def Function_21_2EC3(): pass

    label("Function_21_2EC3")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF6")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F62")

    ChrTalk(    #86
        0x102,
        (
            "#010FNial must be waiting for us.\x02\x03",

            "He should be at the News Service\x01",
            "building in the West Block.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #87
        0x101,
        "#000FOkay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FF3")

    label("loc_2F62")


    ChrTalk(    #88
        0x102,
        (
            "#010FThat's the exit, Estelle...\x02\x03",

            "Nial's supposed to be at the News\x01",
            "Service building in the West Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#006FOkay, okay...\x01",
            "My mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF3")

    Jump("loc_306D")

    label("loc_2FF6")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #90
        0x102,
        (
            "#010FI'd imagine that Nial's waiting for us.\x02\x03",

            "He should be at the News Service\x01",
            "building in the West Block.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306D")

    Call(0, 27)
    Return()

    # Function_21_2EC3 end

    def Function_22_3072(): pass

    label("Function_22_3072")

    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311F")
    OP_A2(0x0)

    ChrTalk(    #91
        0x102,
        (
            "#010FFor now, let's report in at the guild.\x02\x03",

            "We ought to let them know what\x01",
            "Nial's investigation turned up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #92
        0x101,
        "#006FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3190")

    label("loc_311F")


    ChrTalk(    #93
        0x102,
        (
            "#010FFor now, let's report in at the guild.\x02\x03",

            "We ought to let them know what\x01",
            "Nial's investigation turned up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3190")

    Call(0, 27)
    Return()

    # Function_22_3072 end

    def Function_23_3195(): pass

    label("Function_23_3195")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3240")

    ChrTalk(    #94
        0x108,
        (
            "#070FWow... Night already. It feels\x01",
            "a little weird being outside\x01",
            "like this.\x02\x03",

            "Since we're done for today,\x01",
            "why don't we check in at that\x01",
            "dinner party?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32DB")

    label("loc_3240")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(    #95
        0x108,
        (
            "#070FHey... You're not thinking of\x01",
            "leaving already, are you?\x02\x03",

            "Your devotion to training is\x01",
            "admirable, but we do have a\x01",
            "dinner party to attend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DB")

    Call(0, 27)
    Return()

    # Function_23_3195 end

    def Function_24_32E0(): pass

    label("Function_24_32E0")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3367")

    ChrTalk(    #96
        0x108,
        (
            "#070FThis is no time to go on the road.\x02\x03",

            "If everything's set up, then\x01",
            "why don't we head for the \x01",
            "Grancel Sewers?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E4")

    label("loc_3367")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(    #97
        0x108,
        (
            "#070FThis is no time to go on the road.\x02\x03",

            "If everything's set up, then\x01",
            "why don't we head for the \x01",
            "Grancel Sewers?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E4")

    Call(0, 27)
    Return()

    # Function_24_32E0 end

    def Function_25_33E9(): pass

    label("Function_25_33E9")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B0")

    ChrTalk(    #98
        0x101,
        "#501FOh, this way leads outside...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #99
        0x101,
        (
            "#000FWhy don't we explore some more\x01",
            "of the city before we leave?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #100
        0x102,
        (
            "#010FYeah, you're right. There's\x01",
            "plenty more to see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3540")

    label("loc_34B0")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #101
        0x101,
        (
            "#000FHey...Joshua?\x02\x03",

            "Why don't we walk around\x01",
            "town a little longer?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #102
        0x102,
        (
            "#010FYeah, you're right. There's\x01",
            "plenty more to see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3540")

    Call(0, 27)
    Return()

    # Function_25_33E9 end

    def Function_26_3545(): pass

    label("Function_26_3545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_362F")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E3")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #103
        0x102,
        (
            "#012FWe've still got time before we\x01",
            "need to go, Estelle.\x02\x03",

            "For now, let's go to the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #104
        0x101,
        "#002FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_362B")

    label("loc_35E3")


    ChrTalk(    #105
        0x102,
        (
            "#012FIt's not time to go yet.\x02\x03",

            "For now, let's go to the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362B")

    Call(0, 27)

    label("loc_362F")

    Return()

    # Function_26_3545 end

    def Function_27_3630(): pass

    label("Function_27_3630")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_27_3630 end

    def Function_28_364C(): pass

    label("Function_28_364C")

    SetPlaceName(0xB9)
    Return()

    # Function_28_364C end

    def Function_29_3650(): pass

    label("Function_29_3650")

    SetPlaceName(0xB0)
    Return()

    # Function_29_3650 end

    def Function_30_3654(): pass

    label("Function_30_3654")

    SetPlaceName(0xB2)
    Return()

    # Function_30_3654 end

    def Function_31_3658(): pass

    label("Function_31_3658")

    SetPlaceName(0xAE)
    Return()

    # Function_31_3658 end

    def Function_32_365C(): pass

    label("Function_32_365C")

    SetPlaceName(0xB3)
    Return()

    # Function_32_365C end

    SaveToFile()

Try(main)
