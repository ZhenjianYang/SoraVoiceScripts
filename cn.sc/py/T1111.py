from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1111   ._SN',
        MapName             = 'Bose',
        Location            = 'T1111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 0,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1111_1 ._SN',
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
        '梅贝尔市长',                           # 9
        '莉拉',                                 # 10
        '修女萝萨',                             # 11
        '萨拉',                                 # 12
        '管家门特斯',                           # 13
        '玛依森老人',                           # 14
        '哈尔德',                               # 15
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
        'ED6_DT07/CH02360 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH01410 ._CH',             # 02
        'ED6_DT07/CH01350 ._CH',             # 03
        'ED6_DT07/CH02363 ._CH',             # 04
        'ED6_DT07/CH01560 ._CH',             # 05
        'ED6_DT07/CH01200 ._CH',             # 06
        'ED6_DT07/CH01123 ._CH',             # 07
        'ED6_DT26/CH20361 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02360P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH01410P._CP',             # 02
        'ED6_DT07/CH01350P._CP',             # 03
        'ED6_DT07/CH02363P._CP',             # 04
        'ED6_DT07/CH01560P._CP',             # 05
        'ED6_DT07/CH01200P._CP',             # 06
        'ED6_DT07/CH01123P._CP',             # 07
        'ED6_DT26/CH20361P._CP',             # 08
    )

    DeclNpc(
        X                   = -120710,
        Z                   = 200,
        Y                   = 68600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -121000,
        Z                   = 0,
        Y                   = -1300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -117100,
        Z                   = 0,
        Y                   = -2170,
        Direction           = 90,
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
        X                   = -64200,
        Z                   = -3000,
        Y                   = 66350,
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
        X                   = 4000,
        Z                   = 500,
        Y                   = -870,
        Direction           = 180,
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
        X                   = -1860,
        Z                   = 500,
        Y                   = -3840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 6790,
        Z                   = 700,
        Y                   = 1130,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )


    DeclActor(
        TriggerX            = -117140,
        TriggerZ            = 0,
        TriggerY            = -1120,
        TriggerRange        = 400,
        ActorX              = -114920,
        ActorZ              = 1500,
        ActorY              = -1340,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_40D",          # 01, 1
        "Function_2_4A3",          # 02, 2
        "Function_3_620",          # 03, 3
        "Function_4_644",          # 04, 4
        "Function_5_1723",         # 05, 5
        "Function_6_1734",         # 06, 6
        "Function_7_20B2",         # 07, 7
        "Function_8_2589",         # 08, 8
        "Function_9_2745",         # 09, 9
        "Function_10_2D30",        # 0A, 10
        "Function_11_2F67",        # 0B, 11
        "Function_12_3015",        # 0C, 12
        "Function_13_3163",        # 0D, 13
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_209")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_269")
    SetChrPos(0xC, -760, 500, -1050, 135)
    SetChrPos(0x9, -6170, 4500, 2730, 280)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244")
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_266")

    label("loc_244")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xB, -117020, 0, 66660, 90)
    OP_43(0xB, 0x0, 0x0, 0x3)

    label("loc_266")

    Jump("loc_40C")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_27A")
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_40C")

    label("loc_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2F6")
    SetChrPos(0x9, -115400, 0, -1540, 180)
    SetChrPos(0xC, 4160, 500, -950, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -121500, 0, -4140, 270)
    OP_4A(0x9, 255)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0x9, 1)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x8, -116800, 0, -2420, 45)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_40C")

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_37A")
    SetChrPos(0x9, -115400, 0, -1540, 180)
    SetChrPos(0xC, -210, 500, -880, 270)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -1550, 500, -880, 90)
    SetChrFlags(0xD, 0x10)
    OP_4A(0x9, 255)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0x9, 0)
    SetChrPos(0xA, -116810, 0, -1060, 90)
    Jump("loc_40C")

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3FE")
    SetChrChipByIndex(0x8, 4)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -120760, 200, 68570, 180)
    SetChrPos(0x9, -115400, 0, -1540, 180)
    SetChrPos(0xB, -117050, 0, -1280, 90)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xC, 570, 500, 1500, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_4A(0x9, 255)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0x9, 0)
    Jump("loc_40C")

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_40C")
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_40C")

    Return()

    # Function_0_1F6 end

    def Function_1_40D(): pass

    label("Function_1_40D")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_41B")
    Jump("loc_473")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_436")
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    OP_6F(0xD, 15)
    OP_65(0x0, 0x1)
    Jump("loc_473")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_451")
    OP_6F(0xD, 15)
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    OP_65(0x0, 0x1)
    Jump("loc_473")

    label("loc_451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_46C")
    OP_6F(0xD, 15)
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    OP_65(0x0, 0x1)
    Jump("loc_473")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_473")

    label("loc_473")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A2")
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)

    label("loc_4A2")

    Return()

    # Function_1_40D end

    def Function_2_4A3(): pass

    label("Function_2_4A3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_60A")

    label("loc_4C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_60A")

    label("loc_4E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_60A")

    label("loc_4FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_513")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_60A")

    label("loc_513")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_60A")

    label("loc_52C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_545")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_60A")

    label("loc_545")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_60A")

    label("loc_55E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_60A")

    label("loc_577")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_590")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_60A")

    label("loc_590")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_60A")

    label("loc_5A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_60A")

    label("loc_5C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_60A")

    label("loc_5DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_60A")

    label("loc_5F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_60A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_60A")

    label("loc_61F")

    Return()

    # Function_2_4A3 end

    def Function_3_620(): pass

    label("Function_3_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_643")
    OP_8D(0xFE, -118390, 67890, -115780, 64680, 1500)
    Jump("Function_3_620")

    label("loc_643")

    Return()

    # Function_3_620 end

    def Function_4_644(): pass

    label("Function_4_644")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_664")
    Call(1, 1)
    Return()

    label("loc_664")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F4")
    Jump("loc_736")

    label("loc_6F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_710")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_736")

    label("loc_710")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72C")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_736")

    label("loc_72C")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_736")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4B")

    ChrTalk(    #0
        0x8,
        (
            "#613F呀，艾丝蒂尔，\x01",
            "还有约修亚也来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1000F你好，梅贝尔市长。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1040F……好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#611F呵呵，真的是呢……\x02\x03",

            "看起来还是\x01",
            "那么忙碌呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1016F市长也\x01",
            "很辛苦的样子嘛。\x02\x03",

            "我听卢格兰爷爷说了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1035F好像这里也有市民\x01",
            "冲进来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#615F嗯嗯，一直说服到半夜\x01",
            "才总算让他们回去了。\x02\x03",

            "#612F不过，这样并不能\x01",
            "消除市民的不安。\x02\x03",

            "这个状况长久持续下去的话\x01",
            "恐怕还会引起骚乱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1043F的确是这样……\x02\x03",

            "因为结果还是\x01",
            "什么也没能解决。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006F不过，不管怎样\x01",
            "只能做力所能及的事了。\x02\x03",

            "就算低头烦恼，\x01",
            "导力器也不会动起来的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D9")

    ChrTalk(    #9
        0x106,
        (
            "#051F啊啊，说得对。\x02\x03",

            "不管结果怎样，\x01",
            "我们都只能尽游击士的本分。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A86")

    label("loc_9D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A30")

    ChrTalk(    #10
        0x103,
        (
            "#020F嗯嗯，说得对呢。\x02\x03",

            "无论结果如何，\x01",
            "我们都只能尽游击士的本分。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A86")

    label("loc_A30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A86")

    ChrTalk(    #11
        0x108,
        (
            "#070F唔，你说得对。\x02\x03",

            "尽人事听天命……\x01",
            "我们就尽游击士的本分就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A86")


    ChrTalk(    #12
        0x8,
        (
            "#610F呵呵，我也有同感。\x02\x03",

            "无论状况如何，\x01",
            "保护城市是市长的职责……\x02\x03",

            "当然，我相信各位\x01",
            "最后终能解决问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1008F啊、啊哈哈……\x01",
            "这可是责任重大哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#1049F我就当是\x01",
            "鼓励的话记下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2090)
    Jump("loc_C09")

    label("loc_B4B")


    ChrTalk(    #15
        0x8,
        (
            "#610F现在只有各自\x01",
            "尽力而为了吧。\x02\x03",

            "这些努力积累在一起，\x01",
            "我相信一定能成为\x01",
            "渡过危机的力量。\x02\x03",

            "我也打算先和有实力的商人\x01",
            "谈谈看。\x02\x03",

            "这种状况下一定要保持物价安定，\x01",
            "所以他们的协助是不可或缺的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C09")

    Jump("loc_171A")

    label("loc_C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_12B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1073")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_C6B")

    ChrTalk(    #16
        0x8,
        (
            "#610F虽然时间短暂，\x01",
            "还请尽情放松。\x02\x03",

            "休息也是为工作做准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 2)), scpexpr(EXPR_END)), "loc_E78")

    ChrTalk(    #17
        0x8,
        (
            "#610F啊，各位……\x02\x03",

            "刚才莉拉的事…\x01",
            "十分感谢。\x02\x03",

            "#617F很令人吃惊吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1016F嗯、嗯……\x01",
            "真是吓了一跳。\x02\x03",

            "#1000F不过，最后也妥善解决了，\x01",
            "能帮上忙真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#610F嗯嗯，真是帮了大忙。\x02\x03",

            "这次又是到了最后的最后\x01",
            "麻烦你们帮忙。\x02\x03",

            "去了瓦雷利亚湖畔\x01",
            "请务必好好休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1001F嘿嘿，我们会的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD3")

    ChrTalk(    #21
        0x103,
        (
            "#020F难得的休假，\x01",
            "就恭敬不如从命了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3E")

    label("loc_DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0C")

    ChrTalk(    #22
        0x106,
        (
            "#051F是啊，正打算\x01",
            "好好修养一下呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3E")

    label("loc_E0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E3E")

    ChrTalk(    #23
        0x104,
        (
            "#031F呼，不用说\x01",
            "我也会放松的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3E")


    ChrTalk(    #24
        0x8,
        (
            "#611F嗯嗯，请尽情享用。\x02\x03",

            "那么，祝各位休假愉快……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106A")

    label("loc_E78")


    ChrTalk(    #25
        0x8,
        (
            "#610F啊，各位……\x02\x03",

            "刚才莉拉的事…\x01",
            "十分感谢。\x02\x03",

            "还有那个金耀石结晶……\x01",
            "我会小心使用的。\x02\x03",

            "对了，关于票的事情\x01",
            "已经听说了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1018F啊，嗯。\x01",
            "就在刚才。\x02\x03",

            "难得市长一番好意，\x01",
            "我们就打算恭敬不如从命了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#610F嗯嗯，请务必要去。\x02\x03",

            "虽然时间短暂，\x01",
            "但请好好休息。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB0")

    ChrTalk(    #28
        0x103,
        "#020F嗯嗯，就轻松一下吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_FB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD8")

    ChrTalk(    #29
        0x106,
        "#051F啊啊，会的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_FD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1001")

    ChrTalk(    #30
        0x104,
        "#031F呼，就这样定了。\x02",
    )

    CloseMessageWindow()

    label("loc_1001")


    ChrTalk(    #31
        0x101,
        (
            "#1000F嗯，趁此机会\x01",
            "好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#611F休息也是为了更好地工作。\x02\x03",

            "那么各位。\x01",
            "祝你们休假愉快……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106A")

    OP_28(0x79, 0x1, 0x2000)

    label("loc_1070")

    Jump("loc_12B1")

    label("loc_1073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 2)), scpexpr(EXPR_END)), "loc_10BD")

    ChrTalk(    #33
        0x8,
        (
            "#610F虽然时间短暂，\x01",
            "请尽情放松。\x02\x03",

            "休息也是为了更好地工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B1")

    label("loc_10BD")


    ChrTalk(    #34
        0x8,
        (
            "#610F哎呀，各位。\x01",
            "这次真是辛苦了呢。\x02\x03",

            "那个金耀石结晶……\x01",
            "我会小心使用的。\x02\x03",

            "#613F对了，关于票的事情\x01",
            "已经听说了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1018F啊，嗯。\x01",
            "就在刚才。\x02\x03",

            "难得市长一番好意，\x01",
            "我们就打算恭敬不如从命了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#611F嗯嗯，请务必要去。\x02\x03",

            "虽然时间短暂，\x01",
            "但请好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F4")

    ChrTalk(    #37
        0x103,
        "#021F嗯嗯，就轻松一下吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1245")

    label("loc_11F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121C")

    ChrTalk(    #38
        0x106,
        "#051F啊啊，会的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1245")

    label("loc_121C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1245")

    ChrTalk(    #39
        0x104,
        "#031F呼，就这样定了。\x02",
    )

    CloseMessageWindow()

    label("loc_1245")


    ChrTalk(    #40
        0x101,
        (
            "#1001F嗯，趁此机会\x01",
            "好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "#610F休息也是为了更好地工作。\x02\x03",

            "那么各位。\x01",
            "祝你们休假愉快……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A52)

    label("loc_12B1")

    Jump("loc_171A")

    label("loc_12B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_134F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1305")
    TurnDirection(0x8, 0x0, 0)

    ChrTalk(    #42
        0x8,
        (
            "#611F多亏了各位\x01",
            "把莉拉救出来。\x02\x03",

            "我衷心感谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 0)
    Jump("loc_134C")

    label("loc_1305")

    TurnDirection(0x8, 0x0, 0)

    ChrTalk(    #43
        0x8,
        (
            "#611F艾丝蒂尔，\x01",
            "莉拉醒来了！\x02\x03",

            "太好了……真的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 0)
    OP_A2(0x0)

    label("loc_134C")

    Jump("loc_171A")

    label("loc_134F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_14D3")
    SetChrSubChip(0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_139F")

    ChrTalk(    #44
        0x8,
        (
            "#618F不得不做的\x01",
            "工作堆积如山……\x02\x03",

            "现在可不能泄气啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_139F")


    ChrTalk(    #45
        0x8,
        (
            "#615F给避难目的地各店铺的邀请\x01",
            "总算发完了……\x02\x03",

            "接下来是超市的受害调查\x01",
            "和修复工程的计划还有材料的定购……\x02\x03",

            "#618F还有送往拉文努村的\x01",
            "物资也必须进行准备……\x02\x03",

            "…………………………………\x01",
            "…………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #46
        0x8,
        (
            "#616F梅贝尔，振作点！\x01",
            "工作还堆积如山呢。\x02\x03",

            "身为市长的我\x01",
            "要是泄气了城市可怎么办？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_14D0")

    Jump("loc_171A")

    label("loc_14D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_171A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1535")

    ChrTalk(    #47
        0x8,
        (
            "#610F交通安全的确保\x01",
            "也是商业都市的重要工作。\x02\x03",

            "通缉魔兽的剿灭……\x01",
            "就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171A")

    label("loc_1535")


    ChrTalk(    #48
        0x8,
        (
            "#610F哎呀，各位……\x02\x03",

            "开门见山吧，有什么要事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1000F不，只是来\x01",
            "报告一下状况。\x02\x03",

            "#1015F首先从通缉魔兽的剿灭任务开始，\x01",
            "做帮忙的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x106,
        "#050F嗯，总之先做这个吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#617F哪里，这也是帮大忙了。\x02\x03",

            "最近实在很多，\x01",
            "一直是让人头痛的原因之一呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1016F啊，果然\x01",
            "市长也很困扰啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#615F嗯嗯，安全交通路线的确保\x01",
            "对商业都市来说是生死存亡的问题……\x02\x03",

            "#610F虽然或许这工作并不难，\x01",
            "但解决了这些可是有很大益处的哦。\x02\x03",

            "通缉魔兽的剿灭……\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1006F嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_171A")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_4_644 end

    def Function_5_1723(): pass

    label("Function_5_1723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1733")
    Call(0, 6)

    label("loc_1733")

    Return()

    # Function_5_1723 end

    def Function_6_1734(): pass

    label("Function_6_1734")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1754")
    Call(1, 2)
    Return()

    label("loc_1754")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_180F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DE")

    ChrTalk(    #55
        0x9,
        (
            "#620F各位……\x01",
            "前几天给你们添麻烦了。\x02\x03",

            "现在梅贝尔小姐\x01",
            "似乎忙得不可开交……\x02\x03",

            "能帮助小姐的\x01",
            "就只有你们了，拜托。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_180C")

    label("loc_17DE")


    ChrTalk(    #56
        0x9,
        (
            "#620F能帮助小姐的，\x01",
            "就只有你们了，拜托。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_180C")

    Jump("loc_20AE")

    label("loc_180F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1CFB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_186F")

    ChrTalk(    #57
        0x9,
        (
            "#620F各位现在\x01",
            "要去湖畔的旅馆吗。\x02\x03",

            "那么就请你们\x01",
            "好好静养吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B2E")

    label("loc_186F")


    ChrTalk(    #58
        0x9,
        (
            "#620F哎呀，各位……\x02\x03",

            "各位为我做这么多事\x01",
            "真是给你们添麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1017F没什么麻烦的啦。\x01",
            "能帮上忙真是太好了。\x02\x03",

            "因为，就算没有血缘关系\x01",
            "亲人就是亲人……\x02\x03",

            "只要能确定这个，\x01",
            "我就感觉受到了鼓舞。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_195C")

    ChrTalk(    #60
        0x103,
        "#020F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_19A5")

    label("loc_195C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1980")

    ChrTalk(    #61
        0x107,
        "#060F姐姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_19A5")

    label("loc_1980")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A5")

    ChrTalk(    #62
        0x105,
        "#040F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    label("loc_19A5")

    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #63
        0x9,
        (
            "#621F是吗……\x02\x03",

            "你能这么说\x01",
            "我也安心不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1000F对了，莉拉\x01",
            "打算几时回家乡？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "#620F日程还没定……\x01",
            "要看小姐的计划了。\x02\x03",

            "因为小姐\x01",
            "会一起去嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1018F啊，不错的主意嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#623F嗯嗯，但是\x01",
            "大概也不太可能吧。\x02\x03",

            "小姐还是这么忙碌……\x01",
            "时间估计空不出来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1016F啊、啊哈哈……的确是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "#620F嗯，虽然现在没办法\x01",
            "但总有一天一定会回去的。\x02\x03",

            "在此之前慢慢\x01",
            "等待机会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x79, 0x1, 0x4000)

    label("loc_1B2E")

    Jump("loc_1CF8")

    label("loc_1B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B94")

    ChrTalk(    #70
        0x9,
        (
            "#620F这次你们又帮了小姐不少忙，\x01",
            "实在是感激不尽。\x02\x03",

            "那么，请在湖畔的旅店\x01",
            "好好静养吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF8")

    label("loc_1B94")


    ChrTalk(    #71
        0x9,
        (
            "#620F哎呀，各位是……\x02\x03",

            "这次你们又帮了小姐不少忙，\x01",
            "实在是感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1007F嗯、嗯……\x02\x03",

            "觉得这次莉拉\x01",
            "才是最为辛苦的……\x02\x03",

            "#1002F……身体没事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#620F请不必\x01",
            "为莉拉担心。\x02\x03",

            "对了，听说各位现在\x01",
            "要去湖畔的旅店……\x02\x03",

            "从龙的骚动事件开始，\x01",
            "这次似乎又有很多事情要忙呢……\x02\x03",

            "#621F请趁此机会\x01",
            "好好静养吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1016F唔，嗯，谢谢。\x02\x03",

            "不用客气好好享受哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1CF8")

    Jump("loc_20AE")

    label("loc_1CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1FB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 5)), scpexpr(EXPR_END)), "loc_1D4A")

    ChrTalk(    #75
        0x9,
        (
            "#621F也给金先生和奥利维尔先生\x01",
            "添麻烦了。\x02\x03",

            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB1")

    label("loc_1D4A")


    ChrTalk(    #76
        0x9,
        "#627F艾丝蒂尔小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1004F莉拉，没事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "#620F是……让各位\x01",
            "担心了……\x02\x03",

            "#627F……真是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1001F说什么呢。\x02\x03",

            "莉拉拼命\x01",
            "保护了梅贝尔市长。\x02\x03",

            "#1009F错的都是\x01",
            "那头龙和银发男子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E38")

    ChrTalk(    #80
        0x108,
        "#070F呼，无需自责。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E99")

    label("loc_1E38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E6D")

    ChrTalk(    #81
        0x104,
        (
            "#030F呼，小姐没必要\x01",
            "责怪自己。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E99")

    label("loc_1E6D")


    ChrTalk(    #82
        0x106,
        (
            "#053F艾丝蒂尔说得对。\x01",
            "没必要责怪自己。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E99")


    ChrTalk(    #83
        0x9,
        (
            "#621F……我听小姐说了。\x02\x03",

            "也给金先生和奥利维尔先生\x01",
            "添麻烦了。\x02\x03",

            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F42")

    ChrTalk(    #84
        0x108,
        (
            "#070F哪里，区区小事不值得道谢。\x02\x03",

            "反倒是我们\x01",
            "被你的行为所感动了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAE")

    label("loc_1F42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F85")

    ChrTalk(    #85
        0x104,
        (
            "#031F哪里，能救到小姐，\x01",
            "可以说是我的荣幸呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAE")

    label("loc_1F85")


    ChrTalk(    #86
        0x101,
        (
            "#1001F嗯，我一定会\x01",
            "传达给他们俩的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAE")

    OP_A2(0x1A75)

    label("loc_1FB1")

    Jump("loc_20AE")

    label("loc_1FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1FDD")

    ChrTalk(    #87
        0x9,
        "#620F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AE")

    label("loc_1FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2006")

    ChrTalk(    #88
        0x9,
        "#620F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AE")

    label("loc_2006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_20AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2054")

    ChrTalk(    #89
        0x9,
        (
            "#620F小姐正在２楼的书房\x01",
            "办公。\x02\x03",

            "有事的话请去那找她吧。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    Jump("loc_20AE")

    label("loc_2054")


    ChrTalk(    #90
        0x9,
        (
            "#620F哎呀，各位游击士。\x02\x03",

            "小姐在２楼的书房\x01",
            "办公。\x02\x03",

            "有什么事情的话\x01",
            "请到那去找她吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_20AE")

    TalkEnd(0x9)
    Return()

    # Function_6_1734 end

    def Function_7_20B2(): pass

    label("Function_7_20B2")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2151")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2116")

    ChrTalk(    #91
        0xFE,
        "啊，欢迎各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "小姐和莉拉\x01",
            "出门去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "我想一定是\x01",
            "去做礼拜了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_214E")

    label("loc_2116")


    ChrTalk(    #94
        0xFE,
        (
            "小姐和莉拉\x01",
            "出门去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "我想一定是\x01",
            "去做礼拜了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214E")

    Jump("loc_2585")

    label("loc_2151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_224A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2212")

    ChrTalk(    #96
        0xFE,
        "晚上的骚乱真恐怖～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "好多人\x01",
            "涌来屋子这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "现在还觉得好像会有人要冲进来似的，\x01",
            "每个人都一脸怒气冲冲的凶像呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "不过，能把这些人\x01",
            "都说服，\x01",
            "真不愧是小姐呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2247")

    label("loc_2212")


    ChrTalk(    #100
        0xFE,
        "骚乱的时候好恐怖呢～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "好多人\x01",
            "涌来屋子这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2247")

    Jump("loc_2585")

    label("loc_224A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2342")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_22A1")

    ChrTalk(    #102
        0xFE,
        (
            "莉拉的话\x01",
            "不可能有人说坏话的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "嗯～真有点\x01",
            "在意呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22FB")

    label("loc_22A1")


    ChrTalk(    #104
        0xFE,
        (
            "刚才找莉拉\x01",
            "有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "莉拉的话\x01",
            "不可能有人说坏话的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "嗯～真有点\x01",
            "在意呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_22FB")

    Jump("loc_233F")

    label("loc_22FE")


    ChrTalk(    #107
        0xFE,
        (
            "超市也重新开门了，\x01",
            "小姐还有得忙呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "唉，市长可真辛苦～\x02",
    )

    CloseMessageWindow()

    label("loc_233F")

    Jump("loc_2585")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_241A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_238D")

    ChrTalk(    #109
        0xFE,
        (
            "莉拉终于\x01",
            "醒过来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "呼～太好了。\x01",
            "这下就放心了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2417")

    label("loc_238D")


    ChrTalk(    #111
        0xFE,
        "啊，各位！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "莉拉终于\x01",
            "醒过来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "莉拉刚醒来就开始工作，\x01",
            "惹得修女都生气了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "不过还真是莉拉的风格。\x01",
            "感觉就是工作狂～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2417")

    Jump("loc_2585")

    label("loc_241A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_24AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_245A")

    ChrTalk(    #115
        0xFE,
        (
            "没、没有莉拉，\x01",
            "连晚饭的菜单也定不下来啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24AA")

    label("loc_245A")


    ChrTalk(    #116
        0xFE,
        (
            "没、没有莉拉，\x01",
            "连晚饭的菜单也定不下来啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "拜，拜托你一定要醒过来～\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_24AA")

    Jump("loc_2585")

    label("loc_24AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2585")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_24FC")

    ChrTalk(    #118
        0xFE,
        (
            "好了，差不多该\x01",
            "准备茶点了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "小姐不休息一下\x01",
            "可不行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2585")

    label("loc_24FC")


    ChrTalk(    #120
        0xFE,
        (
            "好了，差不多该\x01",
            "准备茶点了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "小姐不休息一下\x01",
            "可不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "小姐经常会\x01",
            "工作到废寝忘食～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "所以要送些茶点，\x01",
            "逼着她休息一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2585")

    TalkEnd(0xB)
    Return()

    # Function_7_20B2 end

    def Function_8_2589(): pass

    label("Function_8_2589")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_261C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25CF")

    ChrTalk(    #124
        0xFE,
        (
            "莉拉才刚刚\x01",
            "醒过来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "还不方便\x01",
            "行动呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2619")

    label("loc_25CF")


    ChrTalk(    #126
        0xFE,
        (
            "莉拉才刚刚\x01",
            "醒过来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "就开始\x01",
            "工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "还不方便\x01",
            "行动呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2619")

    Jump("loc_2741")

    label("loc_261C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_26EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2679")

    ChrTalk(    #129
        0xFE,
        (
            "虽然状态是稳定了……\x01",
            "但意识还没恢复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "教区长给的药\x01",
            "还没有效果……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26EB")

    label("loc_2679")


    ChrTalk(    #131
        0xFE,
        (
            "虽然状态是稳定了……\x01",
            "但意识还没恢复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "教区长给的药\x01",
            "还没有效果……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "……接下来只有\x01",
            "向女神祈祷了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_26EB")

    Jump("loc_2741")

    label("loc_26EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2741")

    ChrTalk(    #134
        0xFE,
        (
            "莉拉的意识\x01",
            "还没有回复……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "虽然性命保住了，\x01",
            "但也只能再继续观察了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2741")

    TalkEnd(0xA)
    Return()

    # Function_8_2589 end

    def Function_9_2745(): pass

    label("Function_9_2745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2751")
    Call(1, 4)
    Return()

    label("loc_2751")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_282D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E0")

    ChrTalk(    #136
        0xFE,
        (
            "超市也恢复\x01",
            "往日的热闹了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "之后要是导力器能复原\x01",
            "就万事大吉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "从各方的说法看来，\x01",
            "这才是最大的难题呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_282A")

    label("loc_27E0")


    ChrTalk(    #139
        0xFE,
        (
            "城市里也恢复\x01",
            "往日的热闹了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "小姐连日连夜的努力\x01",
            "终于也有了回报。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282A")

    Jump("loc_2D2C")

    label("loc_282D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A9")

    ChrTalk(    #141
        0xFE,
        (
            "噢，这不是\x01",
            "各位游击士吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "现在，柏斯正在遭遇\x01",
            "不得了的危机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "为了小姐\x01",
            "请务必伸出援手。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_28EF")

    label("loc_28A9")


    ChrTalk(    #144
        0xFE,
        (
            "现在，柏斯正在遭遇\x01",
            "不得了的危机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "为了小姐\x01",
            "请务必伸出援手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EF")

    Jump("loc_2D2C")

    label("loc_28F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_29D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_295F")

    ChrTalk(    #146
        0xFE,
        (
            "多亏各位的帮忙\x01",
            "终于恢复了和平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "可是，小姐\x01",
            "还是忙得不可开交。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "这也是天性吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29CD")

    label("loc_295F")


    ChrTalk(    #149
        0xFE,
        (
            "多亏各位的帮忙\x01",
            "终于恢复了和平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "要说还有什么担心的，\x01",
            "也就是小姐的身体了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "我会妥善\x01",
            "管理的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_29CD")

    Jump("loc_2D2C")

    label("loc_29D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2AAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2A44")

    ChrTalk(    #152
        0xFE,
        (
            "女佣莉拉\x01",
            "终于恢复意识了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "忙于公务的小姐\x01",
            "也很担心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "呀，主从二人\x01",
            "心情都变开朗了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAC")

    label("loc_2A44")


    ChrTalk(    #155
        0xFE,
        (
            "女佣莉拉\x01",
            "终于恢复意识了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "万一无法恢复……\x01",
            "虽然这样担心过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "呀，总算\x01",
            "心情都变开朗了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2AAC")

    Jump("loc_2D2C")

    label("loc_2AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2B27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2B20")

    ChrTalk(    #158
        0xFE,
        (
            "那盏吊灯\x01",
            "也是逃过战火的东西之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "不知道是不是因为这样的过去，\x01",
            "前市长也经常注视着它。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B24")

    label("loc_2B20")

    Call(0, 11)

    label("loc_2B24")

    Jump("loc_2D2C")

    label("loc_2B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2B76")

    ChrTalk(    #160
        0xFE,
        (
            "避难而来的人\x01",
            "也是我家的客人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "好好招待\x01",
            "是当然的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C4F")

    label("loc_2B76")


    ChrTalk(    #162
        0xFE,
        (
            "避难而来的人\x01",
            "也是我家的客人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "好好招待\x01",
            "是当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "１０年前的战役中，\x01",
            "好像也给避难的市民\x01",
            "分发了茶点哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "无论是怎样的非常时刻\x01",
            "都不能丧失平常的从容。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "正因为这样的心态\x01",
            "才引导了柏斯的复兴吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2C4F")

    Jump("loc_2D2C")

    label("loc_2C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2CAB")

    ChrTalk(    #167
        0xFE,
        (
            "市长现在在２楼\x01",
            "办公。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "现在小姐也正如往常一样\x01",
            "忙着处理公务呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D2C")

    label("loc_2CAB")


    ChrTalk(    #169
        0xFE,
        (
            "各位不是……\x01",
            "欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "前阵子\x01",
            "真是承蒙照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "市长现在在２楼\x01",
            "办公。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "现在小姐也如往常一样\x01",
            "正忙着处理公务呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2D2C")

    TalkEnd(0xC)
    Return()

    # Function_9_2745 end

    def Function_10_2D30(): pass

    label("Function_10_2D30")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2D7B")

    ChrTalk(    #173
        0xFE,
        (
            "那盏吊灯\x01",
            "一定相当有名。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "不愧是柏斯的名家啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DE0")

    label("loc_2D7B")


    ChrTalk(    #175
        0xFE,
        (
            "昨天瞄了一眼，\x01",
            "觉得有点在意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "唔唔，那盏吊灯\x01",
            "一定相当有名。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "不愧是柏斯的名家啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2DE0")

    Jump("loc_2F63")

    label("loc_2DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2E67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2E60")

    ChrTalk(    #178
        0xFE,
        "唔，原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "果然出色的文物，\x01",
            "必然有很深的渊源啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "解开这些谜团\x01",
            "也可说是古董的乐趣所在呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E64")

    label("loc_2E60")

    Call(0, 11)

    label("loc_2E64")

    Jump("loc_2F63")

    label("loc_2E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2F63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2ECA")

    ChrTalk(    #181
        0xFE,
        (
            "我们没礼貌的闯进来，\x01",
            "竟然还招待茶点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "这种时候\x01",
            "温暖的人情真令人感动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F63")

    label("loc_2ECA")


    ChrTalk(    #183
        0xFE,
        (
            "虽然贸然\x01",
            "逃进这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "我们没礼貌的闯进来，\x01",
            "管家还拿出茶点来招待我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "这茶杯\x01",
            "也是精美的古董啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "太感动了……\x01",
            "都忍不住热泪盈眶了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2F63")

    TalkEnd(0xD)
    Return()

    # Function_10_2D30 end

    def Function_11_2F67(): pass

    label("Function_11_2F67")

    OP_4A(0xD, 255)
    OP_4A(0xC, 255)

    ChrTalk(    #187
        0xD,
        "唔，原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xD,
        (
            "原本是帝国制的\x01",
            "吊灯吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xD,
        (
            "之后才装入导力器\x01",
            "的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xC,
        "是的，正是如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xC,
        (
            "算是上代市长\x01",
            "留下来的上等品之一吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xD, 255)
    OP_4B(0xC, 255)
    OP_A2(0x6)
    OP_A2(0x4)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xC, 0x10)
    Return()

    # Function_11_2F67 end

    def Function_12_3015(): pass

    label("Function_12_3015")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_315F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_30B4")

    ChrTalk(    #192
        0xE,
        (
            "胡乱冲进去的地方\x01",
            "没想到竟是市长的宅邸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xE,
        (
            "不过，真不愧是市长官邸。\x01",
            "好气派的房子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xE,
        (
            "可以的话真希望\x01",
            "能在和平的时候来拜访啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_315F")

    label("loc_30B4")


    ChrTalk(    #195
        0xE,
        (
            "唉，总算\x01",
            "逃过一劫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xE,
        (
            "话虽如此……\x01",
            "胡乱冲进去的地方 \x01",
            "竟是市长的宅邸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xE,
        (
            "真不愧是市长官邸。\x01",
            "好气派的房子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xE,
        (
            "可以的话真希望\x01",
            "能在和平的时候来拜访啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_315F")

    TalkEnd(0xE)
    Return()

    # Function_12_3015 end

    def Function_13_3163(): pass

    label("Function_13_3163")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrFlags(0x5, 0x80)
    SetChrFlags(0x6, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_6D(-120360, 0, -6050, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -117150, 0, -1280, 90)
    SetChrPos(0x9, -115400, 0, -1540, 180)
    SetChrPos(0xA, -117100, 0, -2170, 90)
    SetChrChipByIndex(0x8, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_4A(0x9, 255)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0x9, 0)
    OP_6F(0xD, 15)

    def lambda_3238():
        OP_6D(-116590, 0, -790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3238)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_3163 end

    SaveToFile()

Try(main)
