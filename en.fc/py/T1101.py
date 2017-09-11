from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1101   ._SN',
        MapName             = 'Bose',
        Location            = 'T1101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1101   ._SN',
            'ED6_DT01/T1101_1 ._SN',
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
        'Lucas',                                # 9
        'Elegia',                               # 10
        'Harry',                                # 11
        'Mina',                                 # 12
        'Jacob',                                # 13
        'Marco',                                # 14
        'Letta',                                # 15
        'Fannie',                               # 16
        'Mayor Maybelle',                       # 17
        'Nial',                                 # 18
        'Dorothy',                              # 19
        'Lila',                                 # 20
        'Hardt',                                # 21
        'West Bose Highway',                    # 22
        'East Bose Highway',                    # 23
        'Bose - South Block',                   # 24
        'Bose Landing Port',                    # 25
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01160 ._CH',             # 02
        'ED6_DT07/CH01170 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH01100 ._CH',             # 05
        'ED6_DT07/CH02360 ._CH',             # 06
        'ED6_DT07/CH02060 ._CH',             # 07
        'ED6_DT07/CH02070 ._CH',             # 08
        'ED6_DT07/CH02370 ._CH',             # 09
        'ED6_DT07/CH01120 ._CH',             # 0A
        'ED6_DT07/CH01040 ._CH',             # 0B
        'ED6_DT07/CH01053 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01160P._CP',             # 02
        'ED6_DT07/CH01170P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH01100P._CP',             # 05
        'ED6_DT07/CH02360P._CP',             # 06
        'ED6_DT07/CH02060P._CP',             # 07
        'ED6_DT07/CH02070P._CP',             # 08
        'ED6_DT07/CH02370P._CP',             # 09
        'ED6_DT07/CH01120P._CP',             # 0A
        'ED6_DT07/CH01040P._CP',             # 0B
        'ED6_DT07/CH01053P._CP',             # 0C
    )

    DeclNpc(
        X                   = 64280,
        Z                   = 0,
        Y                   = 52300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 63060,
        Z                   = 0,
        Y                   = 49000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 36520,
        Z                   = 0,
        Y                   = 52210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 36520,
        Z                   = 0,
        Y                   = 51220,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48310,
        Z                   = 0,
        Y                   = 46460,
        Direction           = 262,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 66100,
        Z                   = 0,
        Y                   = 62200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 67500,
        Z                   = 0,
        Y                   = 52540,
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
        X                   = 69170,
        Z                   = 0,
        Y                   = 52540,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
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
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 23100,
        Z                   = 0,
        Y                   = 47200,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 45190,
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
        X                   = 87650,
        Z                   = 0,
        Y                   = 60410,
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
        X                   = 47990,
        Z                   = -3000,
        Y                   = 29310,
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
        X                   = 47940,
        Z                   = 0,
        Y                   = 93220,
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
        X                   = 17000,
        Y                   = -1000,
        Z                   = 50100,
        Range               = 18000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x9D6C,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 27800,
        Y                   = -1000,
        Z                   = 57900,
        Range               = 2000,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 25200,
        Y                   = 0,
        Z                   = 57940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 18880,
        Y                   = 0,
        Z                   = 76030,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 36200,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 38540,
        Y                   = 0,
        Z                   = 59990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 48040,
        Y                   = 100,
        Z                   = 69500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 57480,
        Y                   = 0,
        Z                   = 60010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 48010,
        Y                   = 0,
        Z                   = 50550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 67340,
        Y                   = -500,
        Z                   = 73070,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 72240,
        Y                   = 0,
        Z                   = 44910,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = 47960,
        Y                   = 0,
        Z                   = 85570,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 33,
    )


    ScpFunction(
        "Function_0_4D2",          # 00, 0
        "Function_1_638",          # 01, 1
        "Function_2_65E",          # 02, 2
        "Function_3_7DB",          # 03, 3
        "Function_4_8D8",          # 04, 4
        "Function_5_9D5",          # 05, 5
        "Function_6_AD2",          # 06, 6
        "Function_7_12AB",         # 07, 7
        "Function_8_172A",         # 08, 8
        "Function_9_2292",         # 09, 9
        "Function_10_2DE7",        # 0A, 10
        "Function_11_38B7",        # 0B, 11
        "Function_12_3978",        # 0C, 12
        "Function_13_3B90",        # 0D, 13
        "Function_14_3E58",        # 0E, 14
        "Function_15_3EAF",        # 0F, 15
        "Function_16_3ED2",        # 10, 16
        "Function_17_3F3D",        # 11, 17
        "Function_18_4134",        # 12, 18
        "Function_19_438E",        # 13, 19
        "Function_20_486E",        # 14, 20
        "Function_21_4BE7",        # 15, 21
        "Function_22_5846",        # 16, 22
        "Function_23_6443",        # 17, 23
        "Function_24_6C47",        # 18, 24
        "Function_25_726D",        # 19, 25
        "Function_26_783D",        # 1A, 26
        "Function_27_7841",        # 1B, 27
        "Function_28_7845",        # 1C, 28
        "Function_29_7849",        # 1D, 29
        "Function_30_784D",        # 1E, 30
        "Function_31_7851",        # 1F, 31
        "Function_32_7855",        # 20, 32
        "Function_33_7859",        # 21, 33
    )


    def Function_0_4D2(): pass

    label("Function_0_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4E6")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_597")

    label("loc_4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4FA")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_597")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_51C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_519")
    ClearChrFlags(0x14, 0x80)

    label("loc_519")

    Jump("loc_597")

    label("loc_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_END)), "loc_53C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 66400, 0, 54570, 270)
    Jump("loc_597")

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_546")
    Jump("loc_597")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_550")
    Jump("loc_597")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_55A")
    Jump("loc_597")

    label("loc_55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_597")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, 69070, 0, 48400, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x13, 69060, 0, 49440, 180)

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_5A5")
    OP_A3(0x3FA)
    Event(0, 20)

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_5B3")
    OP_A3(0x3FB)
    Event(0, 23)

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_5C1")
    OP_A3(0x3FC)
    Event(0, 25)

    label("loc_5C1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (115, "loc_5D5"),
        (110, "loc_5FA"),
        (116, "loc_611"),
        (SWITCH_DEFAULT, "loc_637"),
    )


    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E4")
    OP_A2(0x307)
    Event(0, 19)

    label("loc_5E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F7")
    OP_A2(0x313)
    Event(0, 21)

    label("loc_5F7")

    Jump("loc_637")

    label("loc_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_611")
    OP_A2(0x315)
    Event(0, 24)

    label("loc_611")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_637")
    OP_28(0x10, 0x3, 0x8)
    RemoveParty(0x34, 0xFF)
    Event(1, 2)

    label("loc_637")

    Return()

    # Function_0_4D2 end

    def Function_1_638(): pass

    label("Function_1_638")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEF660, 0x30041)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65D")
    OP_1B(0xF, 0x0, 0x10)

    label("loc_65D")

    Return()

    # Function_1_638 end

    def Function_2_65E(): pass

    label("Function_2_65E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_683")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7C5")

    label("loc_683")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7C5")

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B5")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7C5")

    label("loc_6B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7C5")

    label("loc_6CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7C5")

    label("loc_6E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_700")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7C5")

    label("loc_700")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_719")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7C5")

    label("loc_719")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_732")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7C5")

    label("loc_732")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7C5")

    label("loc_74B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_764")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7C5")

    label("loc_764")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7C5")

    label("loc_77D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_796")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7C5")

    label("loc_796")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AF")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7C5")

    label("loc_7AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7C5")

    label("loc_7DA")

    Return()

    # Function_2_65E end

    def Function_3_7DB(): pass

    label("Function_3_7DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D7")
    OP_8E(0xFE, 0xFB18, 0x0, 0xAFFA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF6F4, 0x0, 0xAD0C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF15E, 0x0, 0xA99C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x85FC, 0x0, 0xA99C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7EDF, 0x0, 0xB13A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7BE8, 0x0, 0xBA4A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7AA8, 0x0, 0x1249E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x7EAE, 0x0, 0x128D6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x8480, 0x0, 0x12B74, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF596, 0x0, 0x12B74, 0xBB8, 0x0)
    OP_8E(0xFE, 0xF9CE, 0x0, 0x12700, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFB18, 0x0, 0x12340, 0xBB8, 0x0)
    Jump("Function_3_7DB")

    label("loc_8D7")

    Return()

    # Function_3_7DB end

    def Function_4_8D8(): pass

    label("Function_4_8D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D4")
    OP_8E(0xFE, 0xF654, 0x0, 0x119F4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF2A8, 0x0, 0x12214, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEF74, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8A16, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x839A, 0x0, 0x120A2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0x11E36, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0xBC66, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8264, 0x0, 0xB414, 0x9C4, 0x0)
    OP_8E(0xFE, 0x85E8, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEB96, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF122, 0x0, 0xB1C6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF654, 0x0, 0xB874, 0x9C4, 0x0)
    Jump("Function_4_8D8")

    label("loc_9D4")

    Return()

    # Function_4_8D8 end

    def Function_5_9D5(): pass

    label("Function_5_9D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AD1")
    OP_8E(0xFE, 0x8E44, 0x0, 0xB57C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88F4, 0x0, 0xB770, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0xB9DC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0x118D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88C2, 0x0, 0x11D00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8B1A, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEA06, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEE34, 0x0, 0x11CBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0x11A62, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0xBB44, 0x7D0, 0x0)
    OP_8E(0xFE, 0xED62, 0x0, 0xB6EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEB82, 0x0, 0xB57C, 0x7D0, 0x0)
    Jump("Function_5_9D5")

    label("loc_AD1")

    Return()

    # Function_5_9D5 end

    def Function_6_AD2(): pass

    label("Function_6_AD2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCB")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        (
            "Now that the incident has been resolved,\x01",
            "I can finally walk around town in high\x01",
            "spirits for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'm so happy that I just want\x01",
            "to greet everyone I meet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Bose forever!\x01",
            "Long live the mayor!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF3")

    label("loc_BCB")


    ChrTalk(    #3
        0xFE,
        (
            "Bose forever!\x01",
            "Long live the mayor!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF3")

    Jump("loc_12A7")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_D7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD1")
    OP_A2(0x0)

    ChrTalk(    #4
        0xFE,
        (
            "People have been saying that\x01",
            "the missing airliner is the\x01",
            "work of sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "And on top of that, I've heard they\x01",
            "demanded a ransom from the\x01",
            "Royal Family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "What an outrageous bunch.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D78")

    label("loc_CD1")


    ChrTalk(    #7
        0xFE,
        (
            "People have been saying that\x01",
            "the missing airliner is the\x01",
            "work of sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "And on top of that, I've heard they\x01",
            "demanded a ransom from the\x01",
            "Royal Family...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D78")

    Jump("loc_12A7")

    label("loc_D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_E1F")

    ChrTalk(    #9
        0xFE,
        (
            "I hope these burglaries and the missing\x01",
            "airliner incident get resolved soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Nothing good has happened around\x01",
            "here for the last several months.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_EEB")

    ChrTalk(    #11
        0xFE,
        (
            "I put in a notice that I'd be opening\x01",
            "up a shop in the Bose Market...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "But it turns out they're not accepting them\x01",
            "at the moment. It seems like there's been\x01",
            "a lot of problems recently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_F9A")

    ChrTalk(    #13
        0xFE,
        (
            "The Bose Market is like the gateway\x01",
            "to success for aspiring merchants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "If I'm going to begin any kind of\x01",
            "business, it'll have to start in\x01",
            "the Bose Market.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110A")
    OP_A2(0x0)

    ChrTalk(    #15
        0xFE,
        "This city has all kinds of merchants.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "First, there are the ones who open\x01",
            "up shops in the Bose Market...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Then there are the merchants\x01",
            "who have their own places on\x01",
            "the south block avenue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "And then there are the trade merchants\x01",
            "like Trino and Borden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Oh, and I almost forgot to mention\x01",
            "that even the mayor is a merchant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1135")

    label("loc_110A")


    ChrTalk(    #20
        0xFE,
        "This city has all kinds of merchants.\x02",
    )

    CloseMessageWindow()

    label("loc_1135")

    Jump("loc_12A7")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_12A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1223")
    OP_A2(0x0)

    ChrTalk(    #21
        0xFE,
        (
            "Welcome to Bose, the\x01",
            "city of commerce!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "This is the most commercially active\x01",
            "city in all the kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "It's the place where merchants\x01",
            "who dream of success gather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "And of course, that includes me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_1223")


    ChrTalk(    #25
        0xFE,
        (
            "This is the most commercially active\x01",
            "city in all the kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "It's the place where merchants\x01",
            "who dream of success gather.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A7")

    TalkEnd(0x8)
    Return()

    # Function_6_AD2 end

    def Function_7_12AB(): pass

    label("Function_7_12AB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1322")

    ChrTalk(    #27
        0xFE,
        (
            "Every shop has finally got\x01",
            "their wares in again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Now I can go shopping\x01",
            "again as much as I like!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_1322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_13B1")

    ChrTalk(    #29
        0xFE,
        (
            "There's really not much good\x01",
            "to talk about these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Maybe I'll go shopping to keep my\x01",
            "mind off all the depressing news.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_13B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_148A")

    ChrTalk(    #31
        0xFE,
        (
            "With all the soldiers flooding the\x01",
            "south block, there's not much\x01",
            "room to do any shopping there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I had planned to go see some orbment\x01",
            "engraving work, but I guess I'll go to\x01",
            "the Bose Market instead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_148A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(    #33
        0xFE,
        (
            "It seems like no matter which store\x01",
            "I go to recently, they're getting low\x01",
            "on their supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "It looks like the airliners being grounded is\x01",
            "to blame. They can't stock up on anything\x01",
            "with those being out of commission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "There's nothing I really want\x01",
            "to buy, so I'm bored.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_15B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_164E")

    ChrTalk(    #36
        0xFE,
        (
            "I really want to buy a pair of shoes to\x01",
            "match the dress I bought yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Maybe I'll go poke around the shops\x01",
            "and see what they've got.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_164E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_16BC")

    ChrTalk(    #38
        0xFE,
        (
            "Today I'm going to treat \x01",
            "myself to a new dress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I hope I can find something that\x01",
            "I like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1726")

    label("loc_16BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1726")

    ChrTalk(    #40
        0xFE,
        (
            "Hmm...I wonder what I'll buy\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I hope I can find some kind\x01",
            "of outfit that I like!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1726")

    TalkEnd(0x9)
    Return()

    # Function_7_12AB end

    def Function_8_172A(): pass

    label("Function_8_172A")

    TalkBegin(0xA)
    OP_4A(0xB, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192C")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #42
        0xA,
        "You know what, Mina?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #43
        0xB,
        "What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        "I'm gonna try real hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        (
            "Oh, you mean about your dream\x01",
            "of being a merchant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        "Yeah, that of course and...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        "And...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "If you've got something to say,\x01",
            "then spit it out already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        "Umm, a-all right then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        (
            "I-I hope that I can become the\x01",
            "man you want me to become.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0xB,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        "Oh, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        "Well then, I'm looking forward to it.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #54
        0xA,
        "Gr-great!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_196E")

    label("loc_192C")


    ChrTalk(    #55
        0xA,
        (
            "(All right then, now I'm really\x01",
            "going to have to work hard!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196E")

    Jump("loc_228A")

    label("loc_1971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1AA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A99")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #56
        0xA,
        "Umm, Mina...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #57
        0xB,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "Isn't there anything you want\x01",
            "to be in the future?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        "Sure there is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        "Really? Wh-What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        "Do you really want to know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        "Of course I do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        "A wife who's filthy rich.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0xA,
        "...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_1AA2")

    label("loc_1A99")


    ChrTalk(    #65
        0xA,
        "...\x02",
    )

    CloseMessageWindow()

    label("loc_1AA2")

    Jump("loc_228A")

    label("loc_1AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1CAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C56")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #66
        0xA,
        "Hey, Mina...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #67
        0xB,
        "What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "I'm thinking about becoming a\x01",
            "merchant and opening my own\x01",
            "shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xB,
        "Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        (
            "Well, I guess having a goal\x01",
            "is always a good thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        (
            "Now all you need to do is figure\x01",
            "out how to become one, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xA,
        "Y-You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xB,
        (
            "I'll see what I can do\x01",
            "to help you out.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0xA,
        "Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        "Yeah, as long as it's within reason.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_1CAB")

    label("loc_1C56")


    ChrTalk(    #76
        0xA,
        (
            "I feel like this is the first time you've\x01",
            "said anything kind like that to me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAB")

    Jump("loc_228A")

    label("loc_1CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E36")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #77
        0xA,
        "You know, Mina...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #78
        0xB,
        "Know what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        "Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        (
            "You know how you always\x01",
            "nitpick at me? Do you hate\x01",
            "me or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xB,
        (
            "If that was the case, I don't\x01",
            "think I'd be here right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        "What are you blushing about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xB,
        "I never said that I liked you either.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0xA,
        (
            "Ha ha, I should have figured as\x01",
            "much...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_1E82")

    label("loc_1E36")


    ChrTalk(    #86
        0xFE,
        "So I guess that means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "You neither like me nor dislike\x01",
            "me, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E82")

    Jump("loc_228A")

    label("loc_1E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE9")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #88
        0xA,
        "Man...I really want to be a merchant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "But I've never been good at arithmetic\x01",
            "so maybe I'm just not cut out for it,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #90
        0xB,
        "Who knows...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xB,
        (
            "But if you're already going to give up on\x01",
            "any possibility before you've begun, then\x01",
            "you're bound to fail at anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #92
        0xA,
        "...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_204E")

    label("loc_1FE9")

    TurnDirection(0x101, 0xA, 0)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #93
        0xA,
        "Is it okay if I just cry now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#501FS-Sure, maybe that's not a bad idea.\x02",
    )

    CloseMessageWindow()

    label("loc_204E")

    Jump("loc_228A")

    label("loc_2051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_215B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2146")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #95
        0xA,
        (
            "Umm, I wonder how I can\x01",
            "become a merchant.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #96
        0xB,
        "Beats me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xB,
        (
            "But I'll at least tell you this: anyone\x01",
            "who can't do Sunday School arithmetic\x01",
            "is bound to fail.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #98
        0xA,
        "...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_2158")

    label("loc_2146")


    ChrTalk(    #99
        0xA,
        "(Whimper...)\x02",
    )

    CloseMessageWindow()

    label("loc_2158")

    Jump("loc_228A")

    label("loc_215B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_228A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2256")
    OP_A2(0x1)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #100
        0xA,
        (
            "One day, I'm going to be a merchant\x01",
            "and live in a big mansion.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #101
        0xB,
        "Good luck with that one...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        (
            "If you haven't noticed, not every\x01",
            "merchant can live in a big home.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #103
        0xA,
        "...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    Jump("loc_228A")

    label("loc_2256")


    ChrTalk(    #104
        0xA,
        (
            "(I feel like I've just had my\x01",
            "hopes dashed...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228A")

    OP_4B(0xB, 255)
    TalkEnd(0xA)
    Return()

    # Function_8_172A end

    def Function_9_2292(): pass

    label("Function_9_2292")

    TalkBegin(0xB)
    OP_4A(0xA, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_24DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A0")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #105
        0xA,
        "You know what, Mina?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #106
        0xB,
        "What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        "I'm gonna try real hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xB,
        (
            "Oh, you mean about your dream\x01",
            "of being a merchant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        "Yeah, that of course and...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        "And...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "If you've got something to say,\x01",
            "then spit it out already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xA,
        "Umm, a-all right then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "I-I hope that I can become the\x01",
            "man you want me to become.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0xB,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        "Oh, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xB,
        "Well then, I'm looking forward to it.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #117
        0xA,
        "Gr-great!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_24D8")

    label("loc_24A0")


    ChrTalk(    #118
        0xB,
        (
            "No sense squashing his dream...\x01",
            "Not YET, anyway...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D8")

    Jump("loc_2DDF")

    label("loc_24DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2616")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260A")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #119
        0xA,
        "Umm, Mina...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #120
        0xB,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "Isn't there anything you want\x01",
            "to be in the future?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xB,
        "Sure there is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        "Really? Wh-What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        "Do you really want to know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        "Of course I do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xB,
        "A wife who's filthy rich.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #127
        0xA,
        "...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_2613")

    label("loc_260A")


    ChrTalk(    #128
        0xB,
        "...\x02",
    )

    CloseMessageWindow()

    label("loc_2613")

    Jump("loc_2DDF")

    label("loc_2616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_27F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CE")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #129
        0xA,
        "Hey, Mina...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #130
        0xB,
        "What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xA,
        (
            "I'm thinking about becoming a\x01",
            "merchant and opening my own\x01",
            "shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xB,
        "Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "Well, I guess having a goal\x01",
            "is always a good thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        (
            "Now all you need to do is figure\x01",
            "out how to become one, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xA,
        "Y-You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        (
            "I'll see what I can do\x01",
            "to help you out.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #137
        0xA,
        "Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        "Yeah, as long as it's within reason.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_27F0")

    label("loc_27CE")


    ChrTalk(    #139
        0xB,
        "It's not going to be easy...\x02",
    )

    CloseMessageWindow()

    label("loc_27F0")

    Jump("loc_2DDF")

    label("loc_27F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_29A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2982")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #140
        0xA,
        "You know, Mina...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #141
        0xB,
        "Know what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xA,
        "Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xA,
        (
            "You know how you always\x01",
            "nitpick at me? Do you hate\x01",
            "me or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        (
            "If that was the case, I don't\x01",
            "think I'd be here right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xA,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        "What are you blushing about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xB,
        "I never said that I liked you either.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #148
        0xA,
        (
            "Ha ha, I should have figured as\x01",
            "much...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_299E")

    label("loc_2982")


    ChrTalk(    #149
        0xFE,
        "You're unbelievable...\x02",
    )

    CloseMessageWindow()

    label("loc_299E")

    Jump("loc_2DDF")

    label("loc_29A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2B4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B0C")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #150
        0xA,
        "Man...I really want to be a merchant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xA,
        (
            "But I've never been good at arithmetic\x01",
            "so maybe I'm just not cut out for it,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #152
        0xB,
        "Who knows...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xB,
        (
            "But if you're already going to give up on\x01",
            "any possibility before you've begun, then\x01",
            "you're bound to fail at anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #154
        0xA,
        "...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_2B48")

    label("loc_2B0C")


    ChrTalk(    #155
        0xB,
        (
            "Harry, I hope you know you\x01",
            "act just like a little kid.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B48")

    Jump("loc_2DDF")

    label("loc_2B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C47")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #156
        0xA,
        (
            "Umm, I wonder how I can\x01",
            "become a merchant.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #157
        0xB,
        "Beats me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xB,
        (
            "But I'll at least tell you this: anyone\x01",
            "who can't do Sunday School arithmetic\x01",
            "is bound to fail.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #159
        0xA,
        "...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_2C8C")

    label("loc_2C47")


    ChrTalk(    #160
        0xB,
        (
            "Besides, I've never heard of a merchant\x01",
            "who's bad with numbers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C8C")

    Jump("loc_2DDF")

    label("loc_2C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2DDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D91")
    OP_A2(0x1)
    OP_8C(0xB, 270, 0)
    TurnDirection(0xA, 0xB, 0)

    ChrTalk(    #161
        0xA,
        (
            "One day, I'm going to be a merchant\x01",
            "and live in a big mansion.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #162
        0xB,
        "Good luck with that one...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xB,
        (
            "If you haven't noticed, not every\x01",
            "merchant can live in a big home.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #164
        0xA,
        "...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_2DDF")

    label("loc_2D91")


    ChrTalk(    #165
        0xB,
        "That's just not the reality of things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xB,
        "I told him for his own good.\x02",
    )

    CloseMessageWindow()

    label("loc_2DDF")

    OP_4B(0xA, 255)
    TalkEnd(0xB)
    Return()

    # Function_9_2292 end

    def Function_10_2DE7(): pass

    label("Function_10_2DE7")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2F95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EED")
    OP_A2(0x2)

    ChrTalk(    #167
        0xFE,
        (
            "The Krone ridge is the biggest choke-\x01",
            "point between Bose and Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "It's a series of peaks with difficult\x01",
            "terrain covered by bare rock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "It's one place no one should set foot\x01",
            "on without the proper equipment\x01",
            "and preparations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F92")

    label("loc_2EED")


    ChrTalk(    #170
        0xFE,
        (
            "The Krone ridge is the biggest choke-\x01",
            "point between Bose and Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "It's one place no one should set foot\x01",
            "on without the proper equipment\x01",
            "and preparations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F92")

    Jump("loc_38B3")

    label("loc_2F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3168")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AC")
    OP_A2(0x2)

    ChrTalk(    #172
        0xFE,
        (
            "There's a place called the Nebel Valley\x01",
            "in the northeast Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "It's a place where the fog never clears\x01",
            "throughout the entire year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Given its complex geography of mountains\x01",
            "and valleys, it's quite the strange\x01",
            "spectacle to get a look at.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3165")

    label("loc_30AC")


    ChrTalk(    #175
        0xFE,
        (
            "There's a place called the Nebel Valley\x01",
            "in the northeast Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "Given its complex geography of mountains\x01",
            "and valleys, it's quite the strange\x01",
            "spectacle to get a look at.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3165")

    Jump("loc_38B3")

    label("loc_3168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_321B")

    ChrTalk(    #177
        0xFE,
        (
            "It's odd to see the border garrison\x01",
            "directly involved instead of bracers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "I wonder if it has anything to do with the\x01",
            "recent burglaries and missing airliner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B3")

    label("loc_321B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_3411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333D")
    OP_A2(0x2)

    ChrTalk(    #179
        0xFE,
        (
            "The fruit coming from Ravennue\x01",
            "Village knows no equal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "We may lose to Rolent when it comes to\x01",
            "producing great vegetables, but Bose is\x01",
            "definitely the place to be for fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "Not to mention, it's one of the things we\x01",
            "pride ourselves on as citizens of Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_340E")

    label("loc_333D")


    ChrTalk(    #182
        0xFE,
        (
            "We may lose to Rolent when it comes to\x01",
            "producing great vegetables, but Bose is\x01",
            "definitely the place to be for fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Not to mention, it's one of the things we\x01",
            "pride ourselves on as citizens of Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_340E")

    Jump("loc_38B3")

    label("loc_3411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_35B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3516")
    OP_A2(0x2)

    ChrTalk(    #184
        0xFE,
        (
            "Ah, General Morgan... He's one\x01",
            "of the great men who fought in\x01",
            "the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "And the Haken Gate is one of the most\x01",
            "important of strategic military points...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "It's no surprise that he oversees\x01",
            "the border garrison there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B1")

    label("loc_3516")


    ChrTalk(    #187
        0xFE,
        (
            "Ah, General Morgan... He's one\x01",
            "of the great men who fought in\x01",
            "the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "It's no surprise that he oversees\x01",
            "the border garrison there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B1")

    Jump("loc_38B3")

    label("loc_35B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A8")
    OP_A2(0x2)

    ChrTalk(    #189
        0xFE,
        (
            "Mayor Maybelle may be young, but\x01",
            "she's quite the businesswoman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "Her political finesse is one of the things\x01",
            "we pride ourselves on as citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "Ho ho ho, and did I mention that\x01",
            "she's quite the eye-catcher too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3740")

    label("loc_36A8")


    ChrTalk(    #192
        0xFE,
        (
            "Mayor Maybelle may be young, but\x01",
            "she's quite the businesswoman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "Her political finesse is one of the things\x01",
            "we pride ourselves on as citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3740")

    Jump("loc_38B3")

    label("loc_3743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_38B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3861")
    OP_A2(0x2)

    ChrTalk(    #194
        0xFE,
        (
            "Bose is nearly, if not just as\x01",
            "lively as the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "We do a lot of trade with merchants from\x01",
            "the Empire. In other words, we're not in\x01",
            "short supply of much of anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "Ho ho ho, there's no place like the Bose\x01",
            "Market in Grancel, that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B3")

    label("loc_3861")


    ChrTalk(    #197
        0xFE,
        (
            "Ho ho ho, there's no place like the Bose\x01",
            "Market in Grancel, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B3")

    TalkEnd(0xC)
    Return()

    # Function_10_2DE7 end

    def Function_11_38B7(): pass

    label("Function_11_38B7")

    TalkBegin(0xD)

    ChrTalk(    #198
        0xFE,
        "Whew, I finally made it to Bose...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Man, I really got stuck at the\x01",
            "Haken Gate for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "How outrageous to make a merchant\x01",
            "from the Empire such as myself\x01",
            "wait like that.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_11_38B7 end

    def Function_12_3978(): pass

    label("Function_12_3978")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3A2A")

    ChrTalk(    #201
        0xFE,
        (
            "I've really got a thing for the clothes being\x01",
            "sold in the Bose Market recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "Their designs are trendy and unique,\x01",
            "but I wonder where the brand is from?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B8C")

    label("loc_3A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3AC7")

    ChrTalk(    #203
        0xFE,
        (
            "I'm looking for a part-time job\x01",
            "now so that I can eat at the\x01",
            "Anterose again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "I guess the Bose Market is probably\x01",
            "the best place to look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B8C")

    label("loc_3AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3B8C")

    ChrTalk(    #205
        0xFE,
        (
            "Fannie says she wants to dine\x01",
            "at the Anterose again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "But this just isn't a place we\x01",
            "can afford all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "I'm going to have to work a part-time\x01",
            "job and save up some money.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B8C")

    TalkEnd(0xE)
    Return()

    # Function_12_3978 end

    def Function_13_3B90(): pass

    label("Function_13_3B90")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3C63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C1F")
    OP_A2(0x4)

    ChrTalk(    #208
        0xFE,
        (
            "The cake shop in the Bose Market\x01",
            "is said to be pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "I wonder if I should go and\x01",
            "have a taste myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C60")

    label("loc_3C1F")


    ChrTalk(    #210
        0xFE,
        (
            "The cake shop in the Bose Market\x01",
            "is said to be pretty good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C60")

    Jump("loc_3E54")

    label("loc_3C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3CF9")

    ChrTalk(    #211
        0xFE,
        "I'm going to get a part-time job, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "I can work like nobody's business if\x01",
            "it means I can eat more delicious\x01",
            "food because of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E54")

    label("loc_3CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3E54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC9")
    OP_A2(0x4)

    ChrTalk(    #213
        0xFE,
        (
            "Whenever I eat good food,\x01",
            "I feel so happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "The much-praised food at the Anterose\x01",
            "was beyond my wildest expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "I'd love to indulge myself there\x01",
            "at least once a year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E54")

    label("loc_3DC9")


    ChrTalk(    #216
        0xFE,
        (
            "The much-praised food at the Anterose\x01",
            "was beyond my wildest expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "I'd love to indulge myself there\x01",
            "at least once a year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E54")

    TalkEnd(0xF)
    Return()

    # Function_13_3B90 end

    def Function_14_3E58(): pass

    label("Function_14_3E58")

    TalkBegin(0x10)

    NpcTalk(    #218
        0x10,
        "Young Woman",
        "Please, Lila.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #219
        0x10,
        "Young Woman",
        "This is my one and only chance!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_14_3E58 end

    def Function_15_3EAF(): pass

    label("Function_15_3EAF")

    TalkBegin(0x13)

    NpcTalk(    #220
        0x13,
        "Maid",
        "Not this again...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_15_3EAF end

    def Function_16_3ED2(): pass

    label("Function_16_3ED2")

    EventBegin(0x2)
    TurnDirection(0x134, 0x0, 400)

    ChrTalk(    #221
        0x134,
        (
            "#620FWhere are you all headed?\x02\x03",

            "The mayor is in the Bose Market.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_3ED2 end

    def Function_17_3F3D(): pass

    label("Function_17_3F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_END)), "loc_3F4B")
    Call(0, 18)
    Jump("loc_4133")

    label("loc_3F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FC6")
    EventBegin(0x2)
    TurnDirection(0x134, 0x0, 400)

    ChrTalk(    #222
        0x134,
        (
            "#620FWhere are you all headed?\x02\x03",

            "The mayor is in the Bose Market.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4133")

    label("loc_3FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4133")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4081")
    OP_A2(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF1")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3FF8")

    label("loc_3FF1")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3FF8")


    ChrTalk(    #223
        0x103,
        (
            "#020FLet's first stop by the guild and find\x01",
            "out about the ongoing situation.\x02\x03",

            "It's not too late to go somewhere\x01",
            "else after that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4118")

    label("loc_4081")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4097")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_409E")

    label("loc_4097")

    TurnDirection(0x103, 0x0, 400)

    label("loc_409E")


    ChrTalk(    #224
        0x103,
        (
            "#020FLet's first stop by the guild and find\x01",
            "out about the ongoing situation.\x02\x03",

            "The Bose branch is near the\x01",
            "east gate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4118")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4133")

    Return()

    # Function_17_3F3D end

    def Function_18_4134(): pass

    label("Function_18_4134")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_438D")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_41B1")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #225
        0x102,
        (
            "#010FBefore we leave, we need to\x01",
            "deliver Father Divine's letter\x01",
            "to the chapel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4372")

    label("loc_41B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4298")
    Sleep(100)
    OP_A2(0x5)

    ChrTalk(    #226
        0x102,
        (
            "#014FHold on, Estelle.\x02\x03",

            "We haven't delivered the letter\x01",
            "Father Divine gave us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #227
        0x101,
        (
            "#008FGood call. I completely forgot\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        (
            "#010FWe'd better deliver it to the\x01",
            "chapel before we leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4372")

    label("loc_4298")

    OP_A2(0x5)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #229
        0x102,
        (
            "#014FWait, I just remembered.\x02\x03",

            "We haven't delivered the letter\x01",
            "Father Divine gave us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        (
            "#008FGood call. I completely forgot\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x102,
        (
            "#010FWe'd better deliver it to the\x01",
            "chapel before we leave.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4372")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_438D")

    Return()

    # Function_18_4134 end

    def Function_19_438E(): pass

    label("Function_19_438E")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(48080, 5850, 59960, 0)
    OP_6C(225000, 0)
    OP_67(0, 5395, -10000, 0)
    OP_6B(5350, 0)
    SetChrPos(0x103, 69550, 0, 60780, 270)
    SetChrPos(0x101, 70210, 0, 59570, 270)
    SetChrPos(0x102, 71260, 0, 60540, 270)
    StopSound(0x9470, 0x30D40, 0x0)

    def lambda_440F():
        OP_6C(270000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_440F)
    Sleep(3000)

    def lambda_4424():
        OP_6D(69410, 0, 60250, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4424)

    def lambda_443C():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_443C)
    OP_6B(2800, 5000)
    StopSound(0x9470, 0x186A0, 0x1F40)

    ChrTalk(    #232
        0x103,
        (
            "#020FWe finally made it here.\x02\x03",

            "This is the commercial city of\x01",
            "Bose, which sits at the heart\x01",
            "of the Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#004FWow...this definitely looks like\x01",
            "a city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x102,
        (
            "#010FOf the five major cities in Liberl,\x01",
            "this one comes next after the\x01",
            "Royal City.\x02\x03",

            "Compared to Rolent, the buildings\x01",
            "are all made of stone and seem\x01",
            "a lot bigger.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #235
        0x101,
        (
            "#000FDoes anyone have any idea what\x01",
            "that huge building is over there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #236
        0x103,
        (
            "#020FThat's the Bose Market. It's an\x01",
            "indoor marketplace made up\x01",
            "of various shops.\x02\x03",

            "Food, clothing, sundry goods,\x01",
            "furniture, books, and so on...\x02\x03",

            "You can pretty much buy everything\x01",
            "here with the exception of weapons\x01",
            "and orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        (
            "#501FIt's not surprising that they call\x01",
            "this place a commercial city.\x02\x03",

            "#007FMan...I really wish this trip could\x01",
            "have been for shopping...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #238
        0x102,
        (
            "#010FMaybe some other time.\x02\x03",

            "Let's first stop by the guild and\x01",
            "find out what's going on\x01",
            "regarding the incident.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #239
        0x101,
        "#002FOh, all right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x103,
        (
            "#020FJust so you know, the Bracer Guild is\x01",
            "just right over there.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_19_438E end

    def Function_20_486E(): pass

    label("Function_20_486E")

    EventBegin(0x0)
    OP_6D(64470, 0, 73180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_44(0x10, 0xFF)
    OP_44(0x13, 0xFF)
    SetChrPos(0x103, 63280, 0, 74260, 180)
    SetChrPos(0x101, 64540, 0, 74600, 180)
    SetChrPos(0x102, 65730, 0, 74040, 225)
    SetChrPos(0x10, 64220, 0, 71730, 0)
    SetChrPos(0x13, 65120, 0, 70810, 0)
    TurnDirection(0x101, 0x10, 0)
    TurnDirection(0x102, 0x10, 0)
    TurnDirection(0x103, 0x10, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x13, 0x40)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #241
        0x10,
        (
            "#610F...All right everyone, I'm counting\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        (
            "#006FYou just leave everything to us.\x01",
            "If we find out anything, we'll\x01",
            "come and let you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x10,
        (
            "#611FI'll be looking forward to some\x01",
            "good news.\x02\x03",

            "Goodbye, and have a wonderful day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x13,
        "#620FGoodbye.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    def lambda_4A59():
        OP_8E(0x10, 0xFBA4, 0x0, 0xFBE9, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4A59)
    Sleep(500)
    OP_8C(0x13, 180, 400)
    OP_8E(0x13, 0xFBA4, 0x0, 0xFBE9, 0xBB8, 0x0)

    def lambda_4A94():
        OP_69(0x101, 0x5DC)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4A94)
    Sleep(1000)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #245
        0x103,
        (
            "#020FAll right, let's get going,\x01",
            "shall we?\x02\x03",

            "The Haken Gate is at the end of the\x01",
            "Eisen Road to the north of the East\x01",
            "Bose Highway.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #246
        0x102,
        (
            "#010FIn short, we need to head out the\x01",
            "east gate and then turn north\x01",
            "thereafter, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x101,
        (
            "#006FAll-righty then. Haken Gate here\x01",
            "we come!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)
    Return()

    # Function_20_486E end

    def Function_21_4BE7(): pass

    label("Function_21_4BE7")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_44(0x104, 0xFF)
    OP_6D(70630, 0, 62020, 0)
    OP_6C(315000, 0)
    SetChrPos(0x104, 70660, 0, 60750, 270)
    SetChrPos(0x103, 72300, 0, 59880, 270)
    SetChrPos(0x101, 71730, 0, 61730, 270)
    SetChrPos(0x102, 73360, 0, 61130, 270)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #248
        0x104,
        (
            "#030F#3PHmm... So this is Bose, is it?\x01",
            "It's more urban than I'd imagined.\x02\x03",

            "That building over there...\x01",
            "is Bose Market, no?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #249
        0x101,
        (
            "#000FWell, you seem to be quite knowledgeable.\x01",
            "Are you sure this is really your first\x01",
            "time in Liberl?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 0)
    TurnDirection(0x104, 0x102, 400)

    ChrTalk(    #250
        0x104,
        (
            "#035FHa, I was smart enough to buy a\x01",
            "tourist guidebook before I left.\x02\x03",

            "One published by your very\x01",
            "own Liberl News, no less!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x101,
        (
            "#004FA guidebook? Do they really\x01",
            "sell such things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x102,
        (
            "#010FI don't know how to say it...but we\x01",
            "live in a really convenient age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x103,
        (
            "#020FSo do you intend to go shopping\x01",
            "at the Bose Market now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x104,
        (
            "#030FYep. And after doing a bit of window\x01",
            "shopping, I planned to dress up and\x01",
            "dine out.\x02\x03",

            "According to the guide, there's\x01",
            "supposed to be a three-star\x01",
            "restaurant in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x101,
        (
            "#000FRight, the place we ate at with\x01",
            "the mayor. Er...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #256
        0x101,
        (
            "#000FWhat I mean to say is...I guess\x01",
            "this is the place.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FE8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FE8)

    def lambda_4FF6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4FF6)

    def lambda_5004():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5004)

    def lambda_5012():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5012)
    OP_6D(67520, 260, 72190, 3000)
    Sleep(500)

    ChrTalk(    #257
        0x102,
        (
            "#010FThe Anterose. Authentic Liberl\x01",
            "cuisine...or so they say.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(70630, 0, 62020, 0)
    OP_6C(315000, 0)
    OP_0D()

    ChrTalk(    #258
        0x104,
        (
            "#031FIndeed, no doubt this is the place.\x02\x03",

            "I'm quite looking forward to it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0x102, 0x104, 400)
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #259
        0x103,
        (
            "#020FBut it's supposed to cost a pretty\x01",
            "mira if you decide to go with a\x01",
            "full-course meal.\x02\x03",

            "I'd have to recommend a normal\x01",
            "bar any day over this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 400)

    ChrTalk(    #260
        0x104,
        (
            "#030FWorry not, my fair lady. I've brought\x01",
            "sufficient travel expenses.\x02\x03",

            "And if that's not enough, I'll earn\x01",
            "more with my superb skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x102,
        (
            "#014FSuperb skills...? You're not talking\x01",
            "about your songs and musical, uh,\x01",
            "renditions, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#009FCan you actually earn mira\x01",
            "with that crap?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x104,
        (
            "#035FHa! I've starred as the main opera\x01",
            "singer at the Great Theater in the\x01",
            "Erebonian Capital before.\x02\x03",

            "If I remember right, I once earned\x01",
            "1,000,000 mira in a single night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        "#007F(Big fat liar...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x104,
        (
            "#030FAll right, everyone, good work.\x02\x03",

            "I guess this is farewell until fate\x01",
            "brings us together once more.\x02\x03",

            "#031FAdios, amigos!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 270, 400)
    Sleep(250)

    def lambda_5426():

        label("loc_5426")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5426")

    QueueWorkItem2(0x101, 1, lambda_5426)

    def lambda_5437():

        label("loc_5437")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5437")

    QueueWorkItem2(0x102, 1, lambda_5437)

    def lambda_5448():

        label("loc_5448")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5448")

    QueueWorkItem2(0x103, 1, lambda_5448)
    OP_62(0x104, 0x0, 2300, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_8E(0x104, 0xEF34, 0x0, 0xECE0, 0x1770, 0x0)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)

    def lambda_5495():
        OP_6D(72130, 0, 62020, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5495)
    OP_8C(0x101, 135, 400)
    OP_8C(0x103, 45, 400)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #266
        0x101,
        (
            "#008FWhat horror have we unleashed\x01",
            "upon this poor, innocent city?!\x02\x03",

            "Is everyone from Erebonia\x01",
            "a weirdo like that?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #267
        0x102,
        (
            "#018F#2PI-I don't think I like the idea of\x01",
            "THAT being the Empire stereotype...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x101,
        "#501FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x102,
        (
            "#015F#2PWhat I'm trying to say is that I\x01",
            "think the majority of the people\x01",
            "there are quite serious.\x02\x03",

            "I read in a book that their ethos\x01",
            "respects the strong, silent type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        (
            "#000FHmm...\x02\x03",

            "So what you're saying is that\x01",
            "he's simply a weirdo because\x01",
            "he's an artist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x103,
        (
            "#021FNow just hold up there, Estelle. If\x01",
            "the artists of this world heard that,\x01",
            "they'd be less than pleased.\x02\x03",

            "#020FLet's see...we need to report the\x01",
            "information we got out of the\x01",
            "general to Lugran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x102,
        (
            "#010F#2PAnd it would be best if we let\x01",
            "Mayor Maybelle know after\x01",
            "that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        (
            "#006FSo first we visit the guild and\x01",
            "then the mayor's residence.\x02\x03",

            "Okay, let's get going.\x02",
        )
    )

    CloseMessageWindow()
    RemoveParty(0x3, 0xFF)
    OP_B8(0x3)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_21_4BE7 end

    def Function_22_5846(): pass

    label("Function_22_5846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6442")
    OP_A2(0x316)
    OP_44(0x13, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 24359, 500, 57973, 90)
    SetChrPos(0x11, 25364, 0, 57280, 270)
    SetChrPos(0x12, 25497, 0, 58710, 270)
    TurnDirection(0x11, 0x13, 800)
    TurnDirection(0x12, 0x13, 800)

    def lambda_58B6():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_58B6)
    OP_6D(24400, 0, 57655, 3000)

    ChrTalk(    #274
        0x11,
        (
            "#141FCome on, missy. I'm begging you.\x01",
            "Please let us in.\x02\x03",

            "If I could just get a comment from\x01",
            "the mayor, I'd be on my merry\x01",
            "little way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x12,
        (
            "#151FYep, that's right. And of course I'd\x01",
            "need a photograph, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x13,
        (
            "#620F#6PI'm sure the mayor would be flattered,\x01",
            "but she's extremely busy.\x02\x03",

            "I'm going to have to ask all those\x01",
            "without an appointment to leave.\x02\x03",

            "I hope you can understand the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x11,
        (
            "#144FCome on! Please!\x02\x03",

            "For an incident this huge, we\x01",
            "hardly know anything about the\x01",
            "circumstances surrounding it...\x02\x03",

            "And I have an obligation to\x01",
            "inform the readers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x13,
        "#623F#6PBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x12,
        (
            "#151FYeah, what about the readers?\x02\x03",

            "We can probably reach double the number\x01",
            "if we have the mayor grace the cover!\x01",
            "She's said to be very beautiful, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x13,
        "#620F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    def lambda_5BF4():
        TurnDirection(0xFE, 0x12, 0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5BF4)

    ChrTalk(    #281
        0x11,
        (
            "#144FD-Dorothy! Why did you have to go\x01",
            "and say something like that?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C4B():
        TurnDirection(0xFE, 0x11, 0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5C4B)

    ChrTalk(    #282
        0x12,
        (
            "#153FHuh? But it was you who was saying\x01",
            "the same thing, remember?\x02\x03",

            "You said if we didn't have any news to go on,\x01",
            "we could lure customers to buy the magazine\x01",
            "by featuring the sexy mayor on the cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x11,
        "#144FY-You idiot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x13,
        "#620F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x11, 0x13, 0)
    Sleep(500)

    ChrTalk(    #285
        0x11,
        (
            "#143FAh...ha...ha...\x01",
            "U-Umm, miss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x13,
        (
            "#620F#6PWell, aren't you two a couple\x01",
            "of interesting visitors...\x02\x03",

            "I'll make sure to tell Mayor Maybelle\x01",
            "about the details of our conversation.\x02\x03",

            "At the moment, however, I am going\x01",
            "to have to ask you to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x11,
        "#144FW-Wait! This is a misunderstanding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x13,
        "#624F#6PP-L-E-A-S-E L-E-A-V-E.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x11,
        "#145FFine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x12,
        (
            "#153FSo are we going to be okay not\x01",
            "getting a photograph of the mayor\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x11,
        (
            "#145FPlease...for the love of Aidios and\x01",
            "my sanity...just keep your mouth\x01",
            "shut...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 45, 400)

    def lambda_5F6D():
        OP_8E(0xFE, 0x7B09, 0x0, 0xE22C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5F6D)
    Sleep(300)

    def lambda_5F8D():

        label("loc_5F8D")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_5F8D")

    QueueWorkItem2(0x12, 1, lambda_5F8D)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #292
        0x12,
        "#153FN-Nial! Wait for me!\x02",
    )

    CloseMessageWindow()
    OP_44(0x12, 0xFF)
    OP_8E(0x12, 0x7B09, 0x0, 0xE22C, 0xBB8, 0x0)

    ChrTalk(    #293
        0x13,
        "#620F#6PWhew...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #294
        0x13,
        "#622F#6PHuh...?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, 33497, 0, 57400, 0)
    SetChrPos(0x102, 33497, 0, 58550, 0)
    SetChrPos(0x103, 33497, 0, 57890, 0)

    def lambda_607E():
        OP_6D(25400, 0, 57800, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_607E)

    def lambda_6096():
        OP_8E(0xFE, 0x6CCA, 0x0, 0xE038, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6096)
    Sleep(500)

    def lambda_60B6():
        OP_8E(0xFE, 0x6D60, 0x0, 0xE4B6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60B6)
    Sleep(500)

    def lambda_60D6():
        OP_8E(0xFE, 0x72B0, 0x0, 0xE222, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_60D6)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #295
        0x101,
        "#000FGood afternoon, Lila.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x13,
        (
            "#620F#6POh, it's you bracers again.\x02\x03",

            "Did you just return from the\x01",
            "Haken Gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#000FUh yeah, something like that.\x02\x03",

            "So, uh, those two you just\x01",
            "turned away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x13,
        "#620F#6PA bunch of unscrupulous individuals.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#501FReally...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x13,
        (
            "#620F#6PThose miscreants said they planned\x01",
            "to use the mayor to make some\x01",
            "quick mira.\x02\x03",

            "But as long as I'm here to protect\x01",
            "my mistress, I won't allow that to\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #301
        0x101,
        "#008FAh...ha ha...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x102,
        (
            "#019FY-You're really serious about\x01",
            "your job, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x13,
        (
            "#621F#6PDeadly serious.\x01",
            "That's because it's my duty.\x02\x03",

            "Anyway, why don't you all come inside.\x01",
            "The mayor is waiting for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3C)
    OP_73(0x6)
    SetChrFlags(0x13, 0x40)
    OP_8E(0x13, 0x5B4F, 0x1F4, 0xE2C2, 0xBB8, 0x0)

    def lambda_63EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_63EC)
    SetChrFlags(0x13, 0x4)
    OP_94(0x0, 0x13, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_72(0x6, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_73(0x6)
    OP_71(0x6, 0x800)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    EventEnd(0x0)

    label("loc_6442")

    Return()

    # Function_22_5846 end

    def Function_23_6443(): pass

    label("Function_23_6443")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 28680, 0, 57870, 90)
    SetChrPos(0x102, 29950, 0, 59190, 180)
    SetChrPos(0x103, 30030, 0, 56790, 0)
    OP_6D(28840, 0, 57170, 0)
    OP_6C(225000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #304
        0x101,
        (
            "#002F#4PUm...I wonder what's up with\x01",
            "the mayor.\x02\x03",

            "As soon as we mentioned Dad's\x01",
            "name she got all surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x102,
        (
            "#015FYou're right...but I guess I can imagine\x01",
            "where she's coming from.\x02\x03",

            "The mayor and the general\x01",
            "have known one another for\x01",
            "a long time, after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x101,
        "#501F#4P???\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669C")

    ChrTalk(    #307
        0x103,
        (
            "#020FWell, let's not worry about that\x01",
            "right now.\x02\x03",

            "We've given the mayor a brief\x01",
            "rundown of everything, so let's\x01",
            "head to the guild.\x02\x03",

            "I'm sure Lugran is waiting for\x01",
            "a report from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        "#006F#2PRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C3F")

    label("loc_669C")

    OP_A2(0x315)

    ChrTalk(    #309
        0x103,
        (
            "#020FWell, let's not worry about that\x01",
            "right now.\x02\x03",

            "The real question is, where\x01",
            "do we go from here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x101,
        (
            "#002F#4PHmm...\x02\x03",

            "Just searching around blindly for\x01",
            "the airliner or sky bandits probably\x01",
            "won't amount to anything, right?\x02\x03",

            "I mean, if that's all it'd take,\x01",
            "then the army would have found\x01",
            "them a long time ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #311
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(    #312
        0x103,
        "#023F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(200)
    TurnDirection(0x101, 0x103, 400)
    Sleep(200)
    OP_8C(0x101, 90, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #313
        0x101,
        (
            "#000F#4PHuh? What's the matter with\x01",
            "you two?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x102,
        (
            "#014FEstelle, you've matured...\x02\x03",

            "If it had been the same you as before,\x01",
            "you probably would have said something\x01",
            "like, 'Let's just comb the entire region!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x103,
        (
            "#021FI never thought I'd see the day\x01",
            "when those words would come\x01",
            "out of your mouth either...\x02\x03",

            "My heart's too full of emotions\x01",
            "for words...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #316
        0x101,
        (
            "#009F#4PSo what are you two trying to say?\x01",
            "You can be so rude sometimes,\x01",
            "I hope you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x102,
        (
            "#019FHa ha. We were complimenting\x01",
            "you, Estelle. Seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x103,
        (
            "#020FUnfortunately, unlike Rolent, the\x01",
            "Bose region is...enormous.\x02\x03",

            "I'm really hoping for a clue\x01",
            "right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        (
            "#003F#4PA clue, huh...?\x02\x03",

            "#006FOh, right. Wasn't that Nial and\x01",
            "Dorothy we saw in front of the\x01",
            "mayor's place earlier?\x02\x03",

            "He seemed pretty starved for a\x01",
            "story...but he's gotta know\x01",
            "SOMETHING by now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x102,
        (
            "#010FIt's true he arrived in Bose\x01",
            "a little before we did...\x02\x03",

            "So I think it may be worth\x01",
            "talking to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        "#000F#4PI wonder where they went.\x02",
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x800)
    OP_28(0x35, 0x1, 0x1000)

    label("loc_6C3F")

    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_23_6443 end

    def Function_24_6C47(): pass

    label("Function_24_6C47")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_6D(58940, 0, 77210, 0)
    SetChrPos(0x101, 58890, 0, 78180, 180)
    SetChrPos(0x102, 57570, 0, 76880, 90)
    SetChrPos(0x103, 59990, 0, 77000, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #322
        0x103,
        (
            "#020F#4PLet's see...now that we've reported\x01",
            "to the guild and the mayor...\x02\x03",

            "We need to think about what\x01",
            "to do next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        (
            "#002F#3PHmm...\x02\x03",

            "Just searching around blindly for\x01",
            "the airliner or sky bandits probably\x01",
            "won't amount to anything, right?\x02\x03",

            "If it had, then the army would have\x01",
            "found them a long time ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #324
        0x102,
        "#014F#3P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(    #325
        0x103,
        "#023F#4P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(200)
    TurnDirection(0x101, 0x103, 400)
    Sleep(200)
    OP_8C(0x101, 180, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #326
        0x101,
        (
            "#000F#3PHuh? What's the matter with\x01",
            "you two?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x102,
        (
            "#014F#3PEstelle, you've matured...\x02\x03",

            "If it had been the same you as before,\x01",
            "you probably would have said something\x01",
            "like, 'Let's just comb the entire region!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x103,
        (
            "#021F#4PI never thought I'd see the day\x01",
            "when those words would come\x01",
            "out of your mouth either...\x02\x03",

            "My heart's too full of emotions\x01",
            "for words...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #329
        0x101,
        (
            "#009F#3PSo what are you two trying to say?\x01",
            "You can be so rude sometimes,\x01",
            "I hope you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x102,
        (
            "#019F#3PHa ha. We were complimenting\x01",
            "you, Estelle. Seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x103,
        (
            "#020F#4PUnfortunately, unlike Rolent, the\x01",
            "Bose region is certainly much\x01",
            "vaster.\x02\x03",

            "I'm really hoping for a clue\x01",
            "right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x101,
        (
            "#003F#3PA clue, huh...?\x02\x03",

            "#006FOh, right. Wasn't that Nial and\x01",
            "Dorothy we saw in front of the\x01",
            "mayor's place earlier?\x02\x03",

            "He seemed pretty starved for a\x01",
            "story...but I wonder if he knows\x01",
            "anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x102,
        (
            "#010F#3PIt's true he arrived in Bose\x01",
            "a little before we did...\x02\x03",

            "So I think it may be worth\x01",
            "talking to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x101,
        "#000F#3PI wonder where they went.\x02",
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x800)
    OP_28(0x35, 0x1, 0x1000)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_24_6C47 end

    def Function_25_726D(): pass

    label("Function_25_726D")

    EventBegin(0x0)
    OP_6D(49570, 0, 86360, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_B8(0x2)
    OP_B8(0x3)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    SetChrPos(0x101, 47600, 3000, 91910, 180)
    SetChrPos(0x102, 48600, 3000, 92500, 180)

    def lambda_72EA():
        OP_8E(0xFE, 0xB9F0, 0x0, 0x13F10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72EA)

    def lambda_7305():
        OP_8E(0xFE, 0xBDD8, 0x0, 0x14406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7305)
    FadeToBright(2000, 0)
    Sleep(3500)
    Fade(500)
    OP_6D(48040, 0, 83320, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(261, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 45, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 400)

    ChrTalk(    #335
        0x101,
        (
            "#000FLet's see...if we're going to travel around\x01",
            "the entire kingdom, then our next destination\x01",
            "is the Ruan region.\x02\x03",

            "I wonder which route we should\x01",
            "take to get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x102,
        (
            "#014F#4PAbout that...so you're really not\x01",
            "planning on using an airliner?\x02\x03",

            "I think it's going to be quite the\x01",
            "detour if we head there on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        (
            "#006FYou remember what Schera\x01",
            "said, right?\x02\x03",

            "We need to walk and actually\x01",
            "see the places we protect first.\x02\x03",

            "Or was it Dad who said that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x102,
        (
            "#010F#4PWell, I guess since we have some\x01",
            "time on our hands, it wouldn't be a\x01",
            "bad thing to head there on foot.\x02\x03",

            "We could save the money it\x01",
            "would cost to use an airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x101,
        (
            "#001FGreat idea! We can use the money\x01",
            "we save to go shopping at the\x01",
            "Bose Market!\x02\x03",

            "After all, we didn't have the time to\x01",
            "spend shopping around leisurely\x01",
            "during the whole sky bandit mess.\x02\x03",

            "#501FAnd then we could leave after that.\x01",
            "So what do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x102,
        (
            "#017F#4PI don't care either way...but try\x01",
            "not to waste too much money.\x02\x03",

            "#010FJust so you know, in order to enter\x01",
            "the Ruan region, we'll need to go\x01",
            "through the Krone Pass to the west.\x02\x03",

            "Once you're done shopping,\x01",
            "let's leave through the west\x01",
            "gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        "#006FOkay. The west gate, right?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x35D)
    OP_A2(0x35E)
    OP_A2(0x400)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_25_726D end

    def Function_26_783D(): pass

    label("Function_26_783D")

    SetPlaceName(0x2A)
    Return()

    # Function_26_783D end

    def Function_27_7841(): pass

    label("Function_27_7841")

    SetPlaceName(0x26)
    Return()

    # Function_27_7841 end

    def Function_28_7845(): pass

    label("Function_28_7845")

    SetPlaceName(0x25)
    Return()

    # Function_28_7845 end

    def Function_29_7849(): pass

    label("Function_29_7849")

    SetPlaceName(0x20)
    Return()

    # Function_29_7849 end

    def Function_30_784D(): pass

    label("Function_30_784D")

    SetPlaceName(0x28)
    Return()

    # Function_30_784D end

    def Function_31_7851(): pass

    label("Function_31_7851")

    SetPlaceName(0x2B)
    Return()

    # Function_31_7851 end

    def Function_32_7855(): pass

    label("Function_32_7855")

    SetPlaceName(0x21)
    Return()

    # Function_32_7855 end

    def Function_33_7859(): pass

    label("Function_33_7859")

    SetPlaceName(0x27)
    Return()

    # Function_33_7859 end

    SaveToFile()

Try(main)
