from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Mayor Maybelle',                       # 9
        'Lila',                                 # 10
        'Sister Rosa',                          # 11
        'Sarah',                                # 12
        'Butler Mayner',                        # 13
        'Meissen',                              # 14
        'Hardt',                                # 15
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
        "Function_5_1FF9",         # 05, 5
        "Function_6_200A",         # 06, 6
        "Function_7_2EDB",         # 07, 7
        "Function_8_369D",         # 08, 8
        "Function_9_3A4D",         # 09, 9
        "Function_10_4500",        # 0A, 10
        "Function_11_492B",        # 0B, 11
        "Function_12_4A4C",        # 0C, 12
        "Function_13_4C3E",        # 0D, 13
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD7")

    ChrTalk(    #0
        0x8,
        (
            "#613FHello again, Estelle.\x01",
            "And... Oh, hello, Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1000FHi, Mayor Maybelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1040F...It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#611FIt has indeed...\x02\x03",

            "You two look busy again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1016FNo kidding. I heard it's been really hard\x01",
            "on you, too, though.\x02\x03",

            "Lugran was telling us about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1035FI was a little worried when I heard\x01",
            "some citizens broke in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#615F*sigh* Yes, I had to spend the better part\x01",
            "of the evening talking them down, and even\x01",
            "then I only barely got them to return home.\x02\x03",

            "#612FI didn't really do anything to actually\x01",
            "assuage their fears, though. I couldn't.\x01",
            "Even I'M half-scared out of my wits.\x02\x03",

            "If this keeps up, I'm afraid there will be\x01",
            "another uprising. A much more violent\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1043FIt could happen, yes...\x02\x03",

            "So long as the real problem remains\x01",
            "unresolved, people will be on edge\x01",
            "and looking for someone to blame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006FRight now, though, we just need to do\x01",
            "what we can.\x02\x03",

            "Staring at the floor and fretting won't\x01",
            "solve anything!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B92")

    ChrTalk(    #9
        0x106,
        (
            "#051FYou got that right.\x02\x03",

            "No matter what comes,\x01",
            "we'll do our duty as bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7F")

    label("loc_B92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF5")

    ChrTalk(    #10
        0x103,
        (
            "#020FYes, exactly.\x02\x03",

            "No matter what may come,\x01",
            "we will do our duty as bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7F")

    label("loc_BF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7F")

    ChrTalk(    #11
        0x108,
        (
            "#070FHm. As you say.\x02\x03",

            "'Do your best, and let heaven decide\x01",
            "the rest'... All we can do is continue\x01",
            "our duty as bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7F")


    ChrTalk(    #12
        0x8,
        (
            "#610FI feel pretty much the same way\x01",
            "about being a mayor.\x02\x03",

            "No matter how dark and hopeless the\x01",
            "situation may seem, a mayor must\x01",
            "remain with her city and protect it.\x02\x03",

            "Of course, I believe you will resolve\x01",
            "things in the end, mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1008FAh...haha... Well, no pressure there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#1049FWe'll take those as words of encouragement.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2090)
    Jump("loc_F07")

    label("loc_DD7")


    ChrTalk(    #15
        0x8,
        (
            "#610FRight now, all each and every one\x01",
            "of us can do is our best.\x02\x03",

            "I believe that by combining all of our\x01",
            "efforts we can overcome this crisis.\x02\x03",

            "For my part, I intend to have a long\x01",
            "talk with all our major merchants.\x02\x03",

            "Their support in making sure prices remain\x01",
            "stable during all this will be crucial.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F07")

    Jump("loc_1FF0")

    label("loc_F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1944")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15F6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_F9F")

    ChrTalk(    #16
        0x8,
        (
            "#610FI know it won't be very long,\x01",
            "but do enjoy your holiday!\x02\x03",

            "Staying rested is part of the\x01",
            "job too, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F3")

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 2)), scpexpr(EXPR_END)), "loc_12FB")

    ChrTalk(    #17
        0x8,
        (
            "#610FOh, hello again!\x02\x03",

            "And thank you again with your\x01",
            "help with Lila.\x02\x03",

            "#617FThat was kind of a surprise for\x01",
            "everyone, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1016FA surprise? Yeah, that's one way to\x01",
            "put it.\x02\x03",

            "#1000FIt all really turned out for the best,\x01",
            "though, so I'm super glad we could\x01",
            "be a part of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#610FYes, you were a great help.\x02\x03",

            "Honestly, I feel guilty. It seems like\x01",
            "I cause nothing but trouble for you\x01",
            "whenever we meet.\x02\x03",

            "I hope you can get some rest at the\x01",
            "Kingfisher Inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1001FHeehee. Don't worry, I think we can\x01",
            "call it even.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121D")

    ChrTalk(    #21
        0x103,
        (
            "#020FIt's our first vacation in a while,\x01",
            "so if anything, I think we owe YOU.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A9")

    label("loc_121D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_126D")

    ChrTalk(    #22
        0x106,
        (
            "#051FYeah, I am lookin' forward to\x01",
            "kickin' back for once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A9")

    label("loc_126D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A9")

    ChrTalk(    #23
        0x104,
        "#031FHeh. You need not tell me to relax.\x02",
    )

    CloseMessageWindow()

    label("loc_12A9")


    ChrTalk(    #24
        0x8,
        (
            "#611FHaha. Please, enjoy yourselves.\x02\x03",

            "I hope you all have a nice holiday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15ED")

    label("loc_12FB")


    ChrTalk(    #25
        0x8,
        (
            "#610FAh, hey there!\x02\x03",

            "Thank you so much for your help with Lila.\x02\x03",

            "And don't worry, I'm going to use the\x01",
            "crystal Ragnard entrusted me with very\x01",
            "carefully.\x02\x03",

            "By the way, I don't suppose you've heard\x01",
            "about a certain little something I arranged?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1018FYeah, Lugran just told us.\x02\x03",

            "We'll be glad to, uh, abuse your\x01",
            "hospitality, if you don't mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#610FHaha. Please, abuse it to your heart's content.\x02\x03",

            "It's not the holiday you deserve,\x01",
            "but please try to get some rest.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1503")

    ChrTalk(    #28
        0x103,
        "#020FOh, we intend to.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_1503")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1539")

    ChrTalk(    #29
        0x106,
        "#051FDon't gotta tell us twice.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_1539")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1562")

    ChrTalk(    #30
        0x104,
        "#031FWe shall indeed!\x02",
    )

    CloseMessageWindow()

    label("loc_1562")


    ChrTalk(    #31
        0x101,
        "#1000FYeah. Don't worry, we'll take it easy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#611FThey do say resting is part\x01",
            "of a bracer's job.\x02\x03",

            "Have a good holiday, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15ED")

    OP_28(0x79, 0x1, 0x2000)

    label("loc_15F3")

    Jump("loc_1941")

    label("loc_15F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 2)), scpexpr(EXPR_END)), "loc_1676")

    ChrTalk(    #33
        0x8,
        (
            "#610FIt may not be for very long,\x01",
            "but please enjoy your holiday.\x02\x03",

            "They do say resting is part\x01",
            "of a bracer's job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1941")

    label("loc_1676")


    ChrTalk(    #34
        0x8,
        (
            "#610FHello again, everyone.\x01",
            "Thank you for all your hard work.\x02\x03",

            "If you're wondering about the goldia\x01",
            "crystal, don't worry; I'll use it very\x01",
            "carefully.\x02\x03",

            "#613FBy the way, has Lugran told you about\x01",
            "the arrangements I made?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1018FYeah, he just told us.\x02\x03",

            "We'll be glad to, uh, abuse your\x01",
            "hospitality, if you don't mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#611FAbuse it to your heart's content.\x02\x03",

            "I know it isn't much of a holiday,\x01",
            "but do try to get some rest.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1854")

    ChrTalk(    #37
        0x103,
        "#021FOh, we intend to.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18B3")

    label("loc_1854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188A")

    ChrTalk(    #38
        0x106,
        "#051FDon't gotta tell us twice.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18B3")

    label("loc_188A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B3")

    ChrTalk(    #39
        0x104,
        "#031FWe shall indeed!\x02",
    )

    CloseMessageWindow()

    label("loc_18B3")


    ChrTalk(    #40
        0x101,
        "#1001FYeah! Don't worry, we'll take it easy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "#610FThey do say resting is part\x01",
            "of a bracer's job.\x02\x03",

            "Have a good holiday, everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A52)

    label("loc_1941")

    Jump("loc_1FF0")

    label("loc_1944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1A39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19D0")
    TurnDirection(0x8, 0x0, 0)

    ChrTalk(    #42
        0x8,
        (
            "#611FThis is also thanks for saving Lila.\x02\x03",

            "From the bottom of my heart...\x01",
            "thank you. Thank you so much.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 0)
    Jump("loc_1A36")

    label("loc_19D0")

    TurnDirection(0x8, 0x0, 0)

    ChrTalk(    #43
        0x8,
        (
            "#611FEstelle, Lila's awake! She's all right!\x02\x03",

            "Oh, thank Aidios... Thank YOU...!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 0)
    OP_A2(0x0)

    label("loc_1A36")

    Jump("loc_1FF0")

    label("loc_1A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1C80")
    SetChrSubChip(0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AA1")

    ChrTalk(    #44
        0x8,
        (
            "#618FI have a mountain of work to do.\x02\x03",

            "I can't waste time being depressed...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C7D")

    label("loc_1AA1")


    ChrTalk(    #45
        0x8,
        (
            "#615FI've contacted all of the shops people\x01",
            "have evacuated to.\x02\x03",

            "Now I need to arrange a full investigation\x01",
            "of the damage to the market, and put together\x01",
            "a plan to rebuild it and order materials...\x02\x03",

            "#618FAfter that I need to...to arrange to have\x01",
            "aid and repair materials sent to...to...\x02\x03",

            "...\x01",
            "Lila...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #46
        0x8,
        (
            "#616FGet it together, Maybelle!\x01",
            "You have a mountain of work to do!\x02\x03",

            "How is the city supposed to function\x01",
            "if you sit around moping?!\x01",
            "Father would DIE of shame!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1C7D")

    Jump("loc_1FF0")

    label("loc_1C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D0E")

    ChrTalk(    #47
        0x8,
        (
            "#610FEnsuring the safety of the roads and\x01",
            "traffic is key to a trade city's survival.\x02\x03",

            "Good luck against those monsters!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF0")

    label("loc_1D0E")


    ChrTalk(    #48
        0x8,
        (
            "#610FHello, everyone.\x02\x03",

            "Already on business, I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1000FUh-huh. We just wanted to let you\x01",
            "know what we were doing.\x02\x03",

            "#1015FWe're going to start by helping with\x01",
            "the wanted monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x106,
        "#050FThat's just what we're doing for now, mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#617FNo, trust me, the city of Bose, and I,\x01",
            "thank you for your service.\x02\x03",

            "There have been so many of them as of\x01",
            "late. They've really been wreaking havoc.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1016FSo they're causing you trouble, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#615FYes, ensuring the roads are safe and\x01",
            "passable is vital to keeping the city\x01",
            "alive.\x02\x03",

            "#610FI know it seems like a simple mission,\x01",
            "but its completion means more to this\x01",
            "city than you may think.\x02\x03",

            "We're ALL counting on you to defeat\x01",
            "those monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1006FLeave it to us!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1FF0")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_4_644 end

    def Function_5_1FF9(): pass

    label("Function_5_1FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2009")
    Call(0, 6)

    label("loc_2009")

    Return()

    # Function_5_1FF9 end

    def Function_6_200A(): pass

    label("Function_6_200A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_202A")
    Call(1, 2)
    Return()

    label("loc_202A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_213A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E4")

    ChrTalk(    #55
        0x9,
        (
            "#620FThank you for the other day.\x02\x03",

            "Miss Maybelle is currently as busy as\x01",
            "humanly possible...\x02\x03",

            "Please, if you can aid her in some way,\x01",
            "I would ask you do so.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2137")

    label("loc_20E4")


    ChrTalk(    #56
        0x9,
        (
            "#620FPlease, if you can aid Miss Maybelle in\x01",
            "some way, I would ask you do so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2137")

    Jump("loc_2ED7")

    label("loc_213A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2911")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_264D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_21CA")

    ChrTalk(    #57
        0x9,
        (
            "#620FYou will be heading to the Kingfisher Inn,\x01",
            "then?\x02\x03",

            "Please, rest and enjoy your holiday\x01",
            "as best you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264A")

    label("loc_21CA")


    ChrTalk(    #58
        0x9,
        (
            "#620FI'm sorry...\x02\x03",

            "You went through so much trouble,\x01",
            "simply on my account...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1017FIt wasn't really any trouble. I'm glad we could\x01",
            "help!\x02\x03",

            "After all...seeing two people who were once\x01",
            "strangers, and were a little afraid to admit how\x01",
            "close they'd become, accepting their feelings...\x02\x03",

            "That was something I think I needed to see, too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2347")

    ChrTalk(    #60
        0x103,
        "#020FWell, well...\x02",
    )

    CloseMessageWindow()
    Jump("loc_238B")

    label("loc_2347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2368")

    ChrTalk(    #61
        0x107,
        "#060FYeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_238B")

    label("loc_2368")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_238B")

    ChrTalk(    #62
        0x105,
        "#040FEstelle...\x02",
    )

    CloseMessageWindow()

    label("loc_238B")

    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #63
        0x9,
        (
            "#621FI see.\x02\x03",

            "Estelle, you are one of a kind in your\x01",
            "kindness. Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1000FSpeaking of finding people, when are\x01",
            "you going to visit your family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "#620FWe have not yet set a date.\x01",
            "It will depend on Miss Maybelle.\x02\x03",

            "It has been decided that she will\x01",
            "accompany me, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1018FHey, yeah, that sounds cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#623FIt is nice, but it means we will not be\x01",
            "leaving immediately.\x02\x03",

            "Miss Maybelle tends to bury herself in\x01",
            "her work. Getting her out of the house\x01",
            "can be...difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1016FOooooh, yeeeeeah, that might be a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "#620FWell, even if it is not happening\x01",
            "immediately, I do intend to visit.\x02\x03",

            "I will simply have to wait patiently for\x01",
            "an opportunity.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x79, 0x1, 0x4000)

    label("loc_264A")

    Jump("loc_290E")

    label("loc_264D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26C2")

    ChrTalk(    #70
        0x9,
        (
            "#620FYou have my most sincere thanks for\x01",
            "helping Miss Maybelle.\x02\x03",

            "Please, enjoy your visit to the inn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290E")

    label("loc_26C2")


    ChrTalk(    #71
        0x9,
        (
            "#620FHello, everyone.\x02\x03",

            "You have my most sincere thanks for\x01",
            "helping Miss Maybelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1007FUh, yeah...\x02\x03",

            "I kinda feel like YOU'RE the one who\x01",
            "suffered the most in all this.\x02\x03",

            "#1002FAre you sure you're okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#620FI am fine. Please do not worry on my account.\x02\x03",

            "More importantly, I believe you are heading\x01",
            "to the Kingfisher Inn on Miss Maybelle's\x01",
            "invitation?\x02\x03",

            "You have been working very hard, between\x01",
            "the dragon case and other things...\x02\x03",

            "#621FPlease, enjoy this chance to relax.\x01",
            "Miss Maybelle worries after you greatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1016FAww, thanks!\x02\x03",

            "We'll enjoy ourselves, trust me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_290E")

    Jump("loc_2ED7")

    label("loc_2911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 5)), scpexpr(EXPR_END)), "loc_2992")

    ChrTalk(    #75
        0x9,
        (
            "#621FIt seems I owe a debt to Mr. Vathek\x01",
            "and Mr. Lenheim.\x02\x03",

            "Thank you for helping me when\x01",
            "I was indisposed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D56")

    label("loc_2992")


    ChrTalk(    #76
        0x9,
        "#627FMiss Bright...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1004FLila! Are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "#620FI am well, yes. It seems I've\x01",
            "caused you all to worry...\x02\x03",

            "#627F...Please, forgive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1001FOh, Lila! What are you saying?\x02\x03",

            "You shielded Mayor Maybelle in the only way\x01",
            "you could! You probably saved her life!\x02\x03",

            "#1009FALL the fault goes to that silver-haired\x01",
            "maniac and his dragon!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B27")

    ChrTalk(    #80
        0x108,
        "#070FYes, do not blame yourself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BBE")

    label("loc_2B27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B81")

    ChrTalk(    #81
        0x104,
        (
            "#030FIndeed! Do not blame yourself for\x01",
            "injuries inflicted upon you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBE")

    label("loc_2B81")


    ChrTalk(    #82
        0x106,
        (
            "#053FEstelle's right.\x01",
            "You don't need to blame yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBE")


    ChrTalk(    #83
        0x9,
        (
            "#621FBy the way, I heard from Miss Maybelle.\x02\x03",

            "It seems I owe a debt to Mr. Vathek\x01",
            "and Mr. Lenheim.\x02\x03",

            "Thank you for helping me when\x01",
            "I was indisposed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CD2")

    ChrTalk(    #84
        0x108,
        (
            "#070FThere's no need for thanks!\x02\x03",

            "The real hero there was you.\x01",
            "I was simply honored to carry a hero.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D53")

    label("loc_2CD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D1C")

    ChrTalk(    #85
        0x104,
        (
            "#031FIt was a pleasure to help one as\x01",
            "brave as you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D53")

    label("loc_2D1C")


    ChrTalk(    #86
        0x101,
        "#1001FHaha. I'll be sure and pass on your thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_2D53")

    OP_A2(0x1A75)

    label("loc_2D56")

    Jump("loc_2ED7")

    label("loc_2D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2D71")

    ChrTalk(    #87
        0x9,
        "#620F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED7")

    label("loc_2D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2D89")

    ChrTalk(    #88
        0x9,
        "#620F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED7")

    label("loc_2D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2ED7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E2F")

    ChrTalk(    #89
        0x9,
        (
            "#620FMiss Maybelle is in her study next door.\x02\x03",

            "If you have business with her, you may\x01",
            "find her there. Please do not disturb\x01",
            "her if you do not.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    Jump("loc_2ED7")

    label("loc_2E2F")


    ChrTalk(    #90
        0x9,
        (
            "#620FBracers, hello.\x02\x03",

            "Miss Maybelle is in her study next door.\x02\x03",

            "If you have business with her, you may\x01",
            "find her there. Please do not disturb\x01",
            "her if you do not.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2ED7")

    TalkEnd(0x9)
    Return()

    # Function_6_200A end

    def Function_7_2EDB(): pass

    label("Function_7_2EDB")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F71")

    ChrTalk(    #91
        0xFE,
        "Welcome, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "If you're looking for the mayor,\x01",
            "she's gone out with Lila.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "I think they went to the church.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2FD7")

    label("loc_2F71")


    ChrTalk(    #94
        0xFE,
        (
            "If you're looking for the mayor,\x01",
            "she's gone out with Lila.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "I think they went to the church.\x02",
    )

    CloseMessageWindow()

    label("loc_2FD7")

    Jump("loc_3699")

    label("loc_2FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3154")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F5")

    ChrTalk(    #96
        0xFE,
        "That riot last night was terrifying!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "So many people, storming into the mansion...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "They all looked and sounded so furious,\x01",
            "as though they were going to tear the\x01",
            "place down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Ahh, but Mayor Maybelle is truly amazing.\x01",
            "Calming a mob as she did...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3151")

    label("loc_30F5")


    ChrTalk(    #100
        0xFE,
        "That riot last night was terrifying!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "So many people, storming into the mansion...\x02",
    )

    CloseMessageWindow()

    label("loc_3151")

    Jump("loc_3699")

    label("loc_3154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_32D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3267")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_31D3")

    ChrTalk(    #102
        0xFE,
        (
            "There's no way you could have a\x01",
            "problem with that girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Hmm. I'm curious now, I'll admit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3264")

    label("loc_31D3")


    ChrTalk(    #104
        0xFE,
        "What business DO you have with Lila?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "There's no way you could have a\x01",
            "problem with that girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "Hmm. I'm curious now, I'll admit.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3264")

    Jump("loc_32D4")

    label("loc_3267")


    ChrTalk(    #107
        0xFE,
        (
            "The market has reopened, and yet Mayor\x01",
            "Maybelle is still so busy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "It's so difficult being mayor...\x02",
    )

    CloseMessageWindow()

    label("loc_32D4")

    Jump("loc_3699")

    label("loc_32D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3451")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3338")

    ChrTalk(    #109
        0xFE,
        "Lila has finally awoken!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Aidios be praised!\x01",
            "We were all so worried...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_344E")

    label("loc_3338")


    ChrTalk(    #111
        0xFE,
        "Oh, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "Lila's finally awoken! Thank Aidios!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "*sigh* Of course, she IMMEDIATELY returned to\x01",
            "work, which I swear is going to end up making\x01",
            "Sister Rosa bedridden...from worry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Ah, it's so like Lila. She really is unstoppable\x01",
            "when it comes to her work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_344E")

    Jump("loc_3699")

    label("loc_3451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_351E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_34AD")

    ChrTalk(    #115
        0xFE,
        (
            "I can't decide what we should do for\x01",
            "dinner without Lilaaaaa! Aaaaah!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351B")

    label("loc_34AD")


    ChrTalk(    #116
        0xFE,
        (
            "I can't decide what we should do for\x01",
            "dinner without Lilaaaaa! Aaaaah!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "Oh, please, Lila, wake up!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_351B")

    Jump("loc_3699")

    label("loc_351E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3699")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3599")

    ChrTalk(    #118
        0xFE,
        "Now, then! Time to prepare some tea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "We have to make sure the mayor\x01",
            "rests SOMETIMES, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3699")

    label("loc_3599")


    ChrTalk(    #120
        0xFE,
        "Now, then! Time to prepare some tea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "We have to make sure the mayor\x01",
            "rests SOMETIMES, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Mayor Maybelle has a bad habit of\x01",
            "letting her work take over her life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "That's why we make her tea, sometimes,\x01",
            "and make her take a break.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3699")

    TalkEnd(0xB)
    Return()

    # Function_7_2EDB end

    def Function_8_369D(): pass

    label("Function_8_369D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3754")

    ChrTalk(    #124
        0xFE,
        (
            "Goddess preserve us... Preserve ME!\x01",
            "Lila's only just woken up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "She's not well enough to be straining\x01",
            "herself so! Perhaps if I hog-tie her \x01",
            "to the bed...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3830")

    label("loc_3754")


    ChrTalk(    #126
        0xFE,
        (
            "Goddess preserve us... Preserve ME!\x01",
            "Lila's only just woken up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "And yet she insists on going right\x01",
            "back to work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "She's not well enough to be straining\x01",
            "herself so! Perhaps if I hog-tie her \x01",
            "to the bed...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3830")

    Jump("loc_3A49")

    label("loc_3833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_39C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_38EA")

    ChrTalk(    #129
        0xFE,
        (
            "Her condition is stable, but Lila still\x01",
            "isn't regaining consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "The medicine I received from Father Holstein\x01",
            "doesn't seem to be having any effect...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C1")

    label("loc_38EA")


    ChrTalk(    #131
        0xFE,
        (
            "Her condition is stable, but Lila still\x01",
            "isn't regaining consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "The medicine I received from Father Holstein\x01",
            "doesn't seem to be having any effect...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "All we can do now is pray for Her mercy.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_39C1")

    Jump("loc_3A49")

    label("loc_39C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3A49")

    ChrTalk(    #134
        0xFE,
        "Lila remains unconscious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "I do not think her life is in danger,\x01",
            "but for now, all we can do is pray\x01",
            "for Her mercy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A49")

    TalkEnd(0xA)
    Return()

    # Function_8_369D end

    def Function_9_3A4D(): pass

    label("Function_9_3A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3A59")
    Call(1, 4)
    Return()

    label("loc_3A59")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B27")

    ChrTalk(    #136
        0xFE,
        "The market has regained its normal energy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Now, if only our orbments would function\x01",
            "once again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "From what I have heard, that may prove\x01",
            "to be our greatest challenge.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3B99")

    label("loc_3B27")


    ChrTalk(    #139
        0xFE,
        "The city is regaining its normal energy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "Our mistress' endless efforts have\x01",
            "borne fruit, it would seem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B99")

    Jump("loc_44FC")

    label("loc_3B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3CCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C49")

    ChrTalk(    #141
        0xFE,
        "Oh, bracer friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "At the moment, we in Bose are facing\x01",
            "a terrible danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Please, give any aid you can to\x01",
            "Mayor Maybelle and our city.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3CC8")

    label("loc_3C49")


    ChrTalk(    #144
        0xFE,
        (
            "At the moment, we in Bose are facing\x01",
            "a terrible danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Please, give any aid you can to\x01",
            "Mayor Maybelle and our city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC8")

    Jump("loc_44FC")

    label("loc_3CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3E28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3D6D")

    ChrTalk(    #146
        0xFE,
        (
            "Thanks to you, good bracers, peace\x01",
            "has returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "The young mistress, however, remains\x01",
            "most busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "Perhaps it is simply her nature.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E25")

    label("loc_3D6D")


    ChrTalk(    #149
        0xFE,
        (
            "Thanks to you, good bracers, peace\x01",
            "has returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "My only remaining concern is the\x01",
            "young mistress' health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "We shall take care to ensure she does\x01",
            "not overwork herself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3E25")

    Jump("loc_44FC")

    label("loc_3E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3F32")

    ChrTalk(    #152
        0xFE,
        "Lila has regained consciousness at last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "The young mistress has been most worried\x01",
            "about Lila, despite being as busy as she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Lila can return to the duty she loves,\x01",
            "and the mistress' worries are soothed.\x01",
            "It is a bright day for both.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FEE")

    label("loc_3F32")


    ChrTalk(    #155
        0xFE,
        "Lila has regained consciousness at last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "In the darkest moments, I did fear that...\x01",
            "ah, but it has not come to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "It lifts all our hearts to see her\x01",
            "healthy and well.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3FEE")

    Jump("loc_44FC")

    label("loc_3FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_40E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_40E2")

    ChrTalk(    #158
        0xFE,
        (
            "That chandelier is one of the items here\x01",
            "which passed through the war unscathed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Perhaps because of its history, the previous\x01",
            "master of the house, Mayor Maybelle's father,\x01",
            "spent a great deal of time staring at it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E6")

    label("loc_40E2")

    Call(0, 11)

    label("loc_40E6")

    Jump("loc_44FC")

    label("loc_40E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_4356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4194")

    ChrTalk(    #160
        0xFE,
        (
            "Even people fleeing disaster are still\x01",
            "guests when they come to this house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "It is only natural to provide them\x01",
            "with all the hospitality we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4353")

    label("loc_4194")


    ChrTalk(    #162
        0xFE,
        (
            "Even people fleeing disaster are still\x01",
            "guests when they come to this house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "It is only natural to provide them\x01",
            "with all the hospitality we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "Why, even during the war ten years ago,\x01",
            "citizens who evacuated to our home were\x01",
            "provided with tea and refreshments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "No matter the crisis, one must never\x01",
            "lose their grace and composure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "I am sure that Bose's swift recovery was\x01",
            "based on Mayor Maybelle's understanding\x01",
            "of this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_4353")

    Jump("loc_44FC")

    label("loc_4356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_44FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_43ED")

    ChrTalk(    #167
        0xFE,
        (
            "Mayor Maybelle is in the study on the\x01",
            "second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "She is quite busy, as always.\x01",
            "Please do not distract her for very long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44FC")

    label("loc_43ED")


    ChrTalk(    #169
        0xFE,
        "Welcome to our humble home, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "Allow me to thank you for your previous efforts.\x01",
            "I know the mistress appreciates them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "Mayor Maybelle is in the study on the\x01",
            "second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "She is quite busy, as always.\x01",
            "Please do not distract her for very long.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_44FC")

    TalkEnd(0xC)
    Return()

    # Function_9_3A4D end

    def Function_10_4500(): pass

    label("Function_10_4500")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_459F")

    ChrTalk(    #173
        0xFE,
        "That chandelier is quite the masterpiece!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Just what you'd expect from one of the\x01",
            "most distinguished families in Bose,\x01",
            "I suppose!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4665")

    label("loc_459F")


    ChrTalk(    #175
        0xFE,
        (
            "I only saw it for a moment yesterday,\x01",
            "but my word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "That chandelier is quite the masterpiece!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "Just what you'd expect from one of the\x01",
            "most distinguished families in Bose,\x01",
            "I suppose!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_4665")

    Jump("loc_4927")

    label("loc_4668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_475A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4753")

    ChrTalk(    #178
        0xFE,
        "Ahhh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "Always amazing to take a moment and realize\x01",
            "the scope of the history of things around us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "It's one of the things antiques can do for\x01",
            "you... Makes you think about your own history,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4757")

    label("loc_4753")

    Call(0, 11)

    label("loc_4757")

    Jump("loc_4927")

    label("loc_475A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_4927")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_47F4")

    ChrTalk(    #181
        0xFE,
        (
            "Offering tea to us hoodlums who just\x01",
            "barged in here without permission...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "Chokes you up a bit to see such kindness,\x01",
            "it does...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4927")

    label("loc_47F4")


    ChrTalk(    #183
        0xFE,
        (
            "Would you look at this!\x01",
            "Look at what this butler's doing for us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "I just pushed my way in here without thinking,\x01",
            "y'see. But the man's serving tea to all of us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "And this cup! Just look at it! It must\x01",
            "be worth more mira than m'house!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "Chokes you up a bit to see such kindness,\x01",
            "it does...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_4927")

    TalkEnd(0xD)
    Return()

    # Function_10_4500 end

    def Function_11_492B(): pass

    label("Function_11_492B")

    OP_4A(0xD, 255)
    OP_4A(0xC, 255)

    ChrTalk(    #187
        0xD,
        "Ahhh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xD,
        (
            "So the chandelier's originally of\x01",
            "Erebonian make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xD,
        (
            "And then the family modified it to use\x01",
            "orbal lights after those became popular?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xC,
        "Just as you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xC,
        (
            "It is one of the exceptional pieces left\x01",
            "behind by the previous mayor.\x02",
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

    # Function_11_492B end

    def Function_12_4A4C(): pass

    label("Function_12_4A4C")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_4C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4B2E")

    ChrTalk(    #192
        0xE,
        (
            "Of all the places I pick in a blind panic,\x01",
            "I pick the mayor's mansion, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xE,
        (
            "Talk about a mansion, though.\x01",
            "Look at this place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xE,
        (
            "Kinda wish I could've visited when it\x01",
            "was a bit more peaceful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C3A")

    label("loc_4B2E")


    ChrTalk(    #195
        0xE,
        (
            "Whew! Managed to get away in just\x01",
            "the nick of time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xE,
        (
            "Of all the places I pick in a blind panic,\x01",
            "I pick the mayor's mansion, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xE,
        (
            "Talk about a mansion, though.\x01",
            "Look at this place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xE,
        (
            "Kinda wish I could've visited when it\x01",
            "was a bit more peaceful...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4C3A")

    TalkEnd(0xE)
    Return()

    # Function_12_4A4C end

    def Function_13_4C3E(): pass

    label("Function_13_4C3E")

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

    def lambda_4D13():
        OP_6D(-116590, 0, -790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D13)
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

    # Function_13_4C3E end

    SaveToFile()

Try(main)
