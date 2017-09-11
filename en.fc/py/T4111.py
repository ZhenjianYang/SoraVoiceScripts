from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4111   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4111.x',
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
        'Helmuth',                              # 9
        'Norche',                               # 10
        'Martin',                               # 11
        'Marian',                               # 12
        'Helena',                               # 13
        'Katrina',                              # 14
        'Dalia',                                # 15
        'Rianne',                               # 16
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01230 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH02490 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01350 ._CH',             # 06
        'ED6_DT07/CH01480 ._CH',             # 07
        'ED6_DT07/CH01023 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01230P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH02490P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01350P._CP',             # 06
        'ED6_DT07/CH01480P._CP',             # 07
        'ED6_DT07/CH01023P._CP',             # 08
    )

    DeclNpc(
        X                   = 60450,
        Z                   = 0,
        Y                   = 62340,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 60030,
        Z                   = 0,
        Y                   = 1650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 6600,
        Z                   = 0,
        Y                   = -55590,
        Direction           = 83,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -4760,
        Z                   = 0,
        Y                   = 1910,
        Direction           = 150,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 0,
        Y                   = 61070,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_70C",          # 01, 1
        "Function_2_759",          # 02, 2
        "Function_3_76F",          # 03, 3
        "Function_4_793",          # 04, 4
        "Function_5_7B7",          # 05, 5
        "Function_6_7DB",          # 06, 6
        "Function_7_7FF",          # 07, 7
        "Function_8_823",          # 08, 8
        "Function_9_847",          # 09, 9
        "Function_10_86B",         # 0A, 10
        "Function_11_D3B",         # 0B, 11
        "Function_12_1427",        # 0C, 12
        "Function_13_2153",        # 0D, 13
        "Function_14_29DD",        # 0E, 14
        "Function_15_307C",        # 0F, 15
        "Function_16_37BE",        # 10, 16
        "Function_17_3EF9",        # 11, 17
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_223")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 60480, 0, 62200, 17)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    Jump("loc_70B")

    label("loc_223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2D2")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 59640, 0, 2040, 163)
    OP_43(0x8, 0x0, 0x0, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 60480, 0, 62200, 17)
    SetChrChipByIndex(0xA, 8)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 122730, 250, 64200, 278)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x4)
    OP_44(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    Jump("loc_70B")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_347")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x5)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    SetChrFlags(0xF, 0x80)
    Jump("loc_70B")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3C6")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115920, 0, 69500, 343)
    SetChrFlags(0xA, 0x10)
    TurnDirection(0xB, 0xA, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    Jump("loc_70B")

    label("loc_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_44F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 58250, 0, 60130, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x6)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 126360, 0, 1830, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 126360, 0, 740, 270)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    SetChrFlags(0xF, 0x80)
    Jump("loc_70B")

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4BF")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x5)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 121030, 0, -58010, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 116840, 0, -55210, 90)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrPos(0xD, -3010, 0, -54540, 0)
    Jump("loc_70B")

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_537")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 123980, 0, 1080, 90)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 126360, 0, 1830, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 126360, 0, 740, 270)
    SetChrPos(0xD, -960, 0, -55790, 0)
    Jump("loc_70B")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_59B")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x5)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    Jump("loc_70B")

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 123980, 0, 1080, 90)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 126360, 0, 1830, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 126360, 0, 740, 270)
    SetChrPos(0xD, 2380, 0, -55230, 0)
    Jump("loc_70B")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_699")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xA, 8)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 122730, 250, 64200, 278)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x4)
    OP_44(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 113680, 0, -55940, 266)
    OP_43(0xB, 0x0, 0x0, 0x7)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 115850, 0, 60880, 45)
    SetChrPos(0xD, -960, 0, -55790, 0)
    Jump("loc_70B")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_70B")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 115780, 0, 61020, 228)
    OP_43(0xA, 0x0, 0x0, 0x5)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 123540, 0, 68800, 3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 113680, 0, -55940, 266)
    OP_43(0xC, 0x0, 0x0, 0x7)
    SetChrPos(0xD, 6320, 0, -55580, 91)

    label("loc_70B")

    Return()

    # Function_0_1F2 end

    def Function_1_70C(): pass

    label("Function_1_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73F")
    OP_B1("t4111_y")
    Jump("loc_748")

    label("loc_73F")

    OP_B1("t4111_n")

    label("loc_748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_758")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_758")

    Return()

    # Function_1_70C end

    def Function_2_759(): pass

    label("Function_2_759")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_759")

    label("loc_76E")

    Return()

    # Function_2_759 end

    def Function_3_76F(): pass

    label("Function_3_76F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_792")
    OP_8D(0xFE, 59200, 2620, 64319, 1410, 2500)
    Jump("Function_3_76F")

    label("loc_792")

    Return()

    # Function_3_76F end

    def Function_4_793(): pass

    label("Function_4_793")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B6")
    OP_8D(0xFE, 56200, 3180, 64330, 1570, 2500)
    Jump("Function_4_793")

    label("loc_7B6")

    Return()

    # Function_4_793 end

    def Function_5_7B7(): pass

    label("Function_5_7B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DA")
    OP_8D(0xFE, 113710, 62230, 117600, 58990, 3000)
    Jump("Function_5_7B7")

    label("loc_7DA")

    Return()

    # Function_5_7B7 end

    def Function_6_7DB(): pass

    label("Function_6_7DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FE")
    OP_8D(0xFE, 113710, 62230, 117600, 58990, 6000)
    Jump("Function_6_7DB")

    label("loc_7FE")

    Return()

    # Function_6_7DB end

    def Function_7_7FF(): pass

    label("Function_7_7FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_822")
    OP_8D(0xFE, 113410, -55340, 116360, -56940, 3000)
    Jump("Function_7_7FF")

    label("loc_822")

    Return()

    # Function_7_7FF end

    def Function_8_823(): pass

    label("Function_8_823")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_846")
    OP_8D(0xFE, -6280, 2250, 4250, -530, 3000)
    Jump("Function_8_823")

    label("loc_846")

    Return()

    # Function_8_823 end

    def Function_9_847(): pass

    label("Function_9_847")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86A")
    OP_8D(0xFE, -4570, 58630, -30, 63950, 3000)
    Jump("Function_9_847")

    label("loc_86A")

    Return()

    # Function_9_847 end

    def Function_10_86B(): pass

    label("Function_10_86B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8C2")
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #0
        0xFE,
        "Hey, it's Estelle the bracer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Let's play sometime, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D37")

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_8CC")
    Jump("loc_D37")

    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8D6")
    Jump("loc_D37")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8E0")
    Jump("loc_D37")

    label("loc_8E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_981")

    ChrTalk(    #2
        0xFE,
        (
            "This year Grandpa said he's\x01",
            "not gonna fight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "What a boring old man. He should\x01",
            "fight for my amusement! I'm gonna\x01",
            "go play outside, dejected!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D37")

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9C9")

    ChrTalk(    #4
        0xFE,
        "Grandma's not feeling so well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "I hope she's okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D37")

    label("loc_9C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A52")

    ChrTalk(    #6
        0xFE,
        (
            "I hope I can meet up with all\x01",
            "my friends at the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I wanna meet the princess, too...\x01",
            "and I wanna see Grandpa!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D37")

    label("loc_A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_AD7")

    ChrTalk(    #8
        0xFE,
        (
            "Went to the castle with Grandma\x01",
            "for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I didn't get to meet the princess,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5A")

    label("loc_AD7")

    OP_A2(0x7)

    ChrTalk(    #10
        0xFE,
        (
            "Went to the castle with Grandma\x01",
            "for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I didn't get to meet the princess,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    label("loc_B5A")

    Jump("loc_D37")

    label("loc_B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BA5")

    ChrTalk(    #13
        0xFE,
        (
            "The princess is my friend, you\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "I'm not lyin'!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D37")

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_C03")

    ChrTalk(    #15
        0xFE,
        "*sniffle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Grandpa said he doesn't know if\x01",
            "he can come home any time soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D37")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_C96")

    ChrTalk(    #17
        0xFE,
        "Yaay! Grandpa's comin' home!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I hope he gets here riiiiight...\x01",
            "NOW! ...No? How abooooout...NOW!\x01",
            "...Still no? Aww, boo...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D37")

    label("loc_C96")

    OP_A2(0x7)

    ChrTalk(    #19
        0xFE,
        "Yaay! Grandpa's comin' home!\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0xFE,
        (
            "I hope he gets here riiiiight...\x01",
            "NOW! ...No? How abooooout...NOW!\x01",
            "...Still no? Aww, boo...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D37")

    TalkEnd(0xFE)
    Return()

    # Function_10_86B end

    def Function_11_D3B(): pass

    label("Function_11_D3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_DD1")

    ChrTalk(    #21
        0xFE,
        (
            "Colonel Richard's been here\x01",
            "many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "And every time, he always flatters\x01",
            "us with praise. He's so very polite\x01",
            "and upstanding!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1423")

    label("loc_DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_E15")

    ChrTalk(    #23
        0xFE,
        "Looks like Rianne's been found.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Thank goodness!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1423")

    label("loc_E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_E85")

    ChrTalk(    #25
        0xFE,
        (
            "Madam put in a request with\x01",
            "the Royal Army to find little\x01",
            "Rianne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "But there's been no word.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1423")

    label("loc_E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_E8F")
    Jump("loc_1423")

    label("loc_E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_F20")

    ChrTalk(    #27
        0xFE,
        (
            "The master of the house has not\x01",
            "even contacted us, which seems\x01",
            "exceptionally strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "I hope there are no...complications...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1423")

    label("loc_F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_FEE")

    ChrTalk(    #29
        0xFE,
        (
            "Madam and Rianne always look forward\x01",
            "to the Queen's Birthday Celebration\x01",
            "and the master's homecoming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "He is only able to return home\x01",
            "for a very short time during\x01",
            "this season, you see...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1423")

    label("loc_FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_10B2")

    ChrTalk(    #31
        0xFE,
        (
            "Each and every year, the master is\x01",
            "personally invited by Her Majesty\x01",
            "to attend the celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "So after the war, every year at\x01",
            "around this time, he has always\x01",
            "come back home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1423")

    label("loc_10B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_11BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1123")

    ChrTalk(    #33
        0xFE,
        (
            "Just between you and me...the\x01",
            "so-called master of this house\x01",
            "is simply no match for Madam!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B7")

    label("loc_1123")

    OP_A2(0x6)

    ChrTalk(    #34
        0xFE,
        (
            "The master is a scary individual,\x01",
            "to be sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "But just between you and me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "...he is simply no match for\x01",
            "Madam. Ooh hoo hoo hoo!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B7")

    Jump("loc_1423")

    label("loc_11BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_133E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1252")

    ChrTalk(    #37
        0xFE,
        (
            "I lost both of my parents in\x01",
            "the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "But Sir and Madam took me in,\x01",
            "simply out of the goodness of\x01",
            "their hearts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133B")

    label("loc_1252")

    OP_A2(0x6)

    ChrTalk(    #39
        0xFE,
        (
            "I lost both of my parents in\x01",
            "the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "But Sir and Madam took me in,\x01",
            "simply out of the goodness of\x01",
            "their hearts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Now, I work as a maid at this house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I owe them both a tremendous\x01",
            "debt of gratitude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133B")

    Jump("loc_1423")

    label("loc_133E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_13E4")

    ChrTalk(    #43
        0xFE,
        (
            "As the Birthday Celebration draws\x01",
            "ever nearer, I thought for certain\x01",
            "the master would be coming home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Perhaps his work is keeping him\x01",
            "occupied...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1423")

    label("loc_13E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1423")

    ChrTalk(    #45
        0xFE,
        (
            "I must clean the house before\x01",
            "the master's return!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1423")

    TalkEnd(0xFE)
    Return()

    # Function_11_D3B end

    def Function_12_1427(): pass

    label("Function_12_1427")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_16B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1524")

    ChrTalk(    #46
        0xFE,
        (
            "Some troops fight for their country\x01",
            "because they truly love it. And I\x01",
            "always took him to be such a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Somehow, that love must have become\x01",
            "twisted. Perhaps he convinced himself he\x01",
            "was serving the country's best interests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B1")

    label("loc_1524")

    OP_A2(0x5)

    ChrTalk(    #48
        0xFE,
        (
            "That Richard could even dream of\x01",
            "a coup d'etat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Some troops fight for their country\x01",
            "because they truly love it. And I\x01",
            "always took him to be such a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Somehow, that love must have become\x01",
            "twisted. Perhaps he convinced himself he\x01",
            "was serving the country's best interests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "I have to believe that. I can't imagine\x01",
            "he would ever incriminate himself for\x01",
            "any less noble reason!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B1")

    Jump("loc_214F")

    label("loc_16B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_18DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1797")

    ChrTalk(    #52
        0xFE,
        (
            "Thank the Goddess! A worker at\x01",
            "the Bracer Guild named Elnan\x01",
            "contacted me a short while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Apparently, Rianne has been found\x01",
            "at the Erbe Royal Villa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I'm so grateful to hear that she\x01",
            "is safe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D7")

    label("loc_1797")

    OP_A2(0x5)

    ChrTalk(    #55
        0xFE,
        (
            "Thank the Goddess! A worker at\x01",
            "the Bracer Guild named Elnan\x01",
            "contacted me a short while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Apparently, Rianne has been found\x01",
            "at the Erbe Royal Villa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I'm so grateful to hear that she\x01",
            "is safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "If something should have happened to her,\x01",
            "I don't think I'd ever be able to face\x01",
            "her parents again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D7")

    Jump("loc_214F")

    label("loc_18DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1A8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_195F")

    ChrTalk(    #59
        0xFE,
        (
            "Both as a wife and as a grandmother,\x01",
            "I must remain ever vigilant. Familial\x01",
            "relations are not be taken lightly!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8B")

    label("loc_195F")

    OP_A2(0x5)

    ChrTalk(    #60
        0xFE,
        (
            "My granddaughter Rianne has\x01",
            "not come home since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "And I've received no contact\x01",
            "from my husband, either...as\x01",
            "usual...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Ohh, what to do, what to do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Both as a wife and as a grandmother,\x01",
            "I must remain ever vigilant. Familial\x01",
            "relations are not be taken lightly!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8B")

    Jump("loc_214F")

    label("loc_1A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1AD1")

    ChrTalk(    #65
        0xFE,
        (
            "Oh dear, where has Rianne gotten\x01",
            "herself off to...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_1AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1BAE")

    ChrTalk(    #66
        0xFE,
        (
            "Aaand I seem to have lost all contact with\x01",
            "my husband--which is no surprise, I suppose,\x01",
            "what with Her Majesty having fallen ill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I just can't shake this feeling that\x01",
            "something terrible is happening...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_1BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1C32")

    ChrTalk(    #68
        0xFE,
        (
            "I've heard not a peep from my \x01",
            "husband, who's stationed at the \x01",
            "Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "What ever is going on here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D08")

    label("loc_1C32")

    OP_A2(0x5)

    ChrTalk(    #70
        0xFE,
        (
            "I've heard not a peep from my \x01",
            "husband, who's stationed on the \x01",
            "Bose side of the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "This is the first time I've been\x01",
            "so cut off from him since the war\x01",
            "ended!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "What ever is going on here?!\x02",
    )

    CloseMessageWindow()

    label("loc_1D08")

    Jump("loc_214F")

    label("loc_1D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1DD6")

    ChrTalk(    #73
        0xFE,
        (
            "I wonder if he'll even attend the Birthday\x01",
            "Celebration at all this year...to say nothing\x01",
            "of the tournament!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I'll have to try to get in touch\x01",
            "with him again before the day is\x01",
            "through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E73")

    ChrTalk(    #75
        0xFE,
        (
            "I've never been turned away from\x01",
            "a visit with Her Majesty before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "It's quite worrisome. Could her\x01",
            "illness really be that serious?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F89")

    label("loc_1E73")

    OP_A2(0x5)

    ChrTalk(    #77
        0xFE,
        (
            "When I went to visit Her Majesty\x01",
            "today, I was turned away by the\x01",
            "guards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "I've gone to see her when she was\x01",
            "sick before, countless times...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "And never once have I been turned\x01",
            "away at the gate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "It's quite worrisome. Could her\x01",
            "illness really be that serious?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F89")

    Jump("loc_214F")

    label("loc_1F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2020")

    ChrTalk(    #81
        0xFE,
        (
            "Today I plan on visiting Her\x01",
            "Majesty at the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "Though I've so much else to do,\x01",
            "I don't know how I'll have the\x01",
            "time for it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_2020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_20C8")

    ChrTalk(    #83
        0xFE,
        (
            "I wonder why he's decided not\x01",
            "to participate in the tournament\x01",
            "this year...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "There must be other, more pressing\x01",
            "circumstances for him to attend to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214F")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_214F")

    ChrTalk(    #85
        0xFE,
        "Ah, hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Please, forgive my appearance. You\x01",
            "caught me in the midst of cooking\x01",
            "beef stew for my granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214F")

    TalkEnd(0xFE)
    Return()

    # Function_12_1427 end

    def Function_13_2153(): pass

    label("Function_13_2153")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2160")
    Jump("loc_29D9")

    label("loc_2160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2176")

    ChrTalk(    #87
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_2176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_221E")

    ChrTalk(    #88
        0xFE,
        (
            "At this rate, what will become\x01",
            "of this Birthday Celebration?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "It's such a monumental event\x01",
            "every year...to cancel it would\x01",
            "be the shamest of shames!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_221E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2296")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_225B")

    ChrTalk(    #90
        0xFE,
        (
            "Ha, ha, ha! What a beautiful\x01",
            "sunset...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2293")

    label("loc_225B")

    OP_A2(0x2)

    ChrTalk(    #91
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Ha, ha, ha! What a beautiful\x01",
            "sunset...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2293")

    Jump("loc_29D9")

    label("loc_2296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_23CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_232B")

    ChrTalk(    #93
        0xFE,
        (
            "...Why the hell is the sun so high\x01",
            "in the sky? Why didn't anyone wake\x01",
            "me earlier?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Am I that undesirable to have\x01",
            "around?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C9")

    label("loc_232B")

    OP_A2(0x2)

    ChrTalk(    #95
        0xFE,
        "Un. Freaking. Believable!\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #96
        0xFE,
        (
            "How could I OVERSLEEP on the day of\x01",
            "the championship?! And oversleep so\x01",
            "SPECTACULARLY, no less!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C9")

    Jump("loc_29D9")

    label("loc_23CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_259B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2473")

    ChrTalk(    #97
        0xFE,
        (
            "If I'm right, the Special Ops team\x01",
            "is gonna win it all. I'd stake my\x01",
            "reputation on it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Ha, ha, ha! I'm looking forward\x01",
            "to tomorrow's match!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2598")

    label("loc_2473")

    OP_A2(0x2)

    ChrTalk(    #99
        0xFE,
        (
            "Ha, ha, ha! Tomorrow's the final\x01",
            "match, at long last!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "If I'm right, the Special Ops team\x01",
            "is gonna win it all. I'd stake my\x01",
            "reputation on it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#009F(Grrr...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Tomorrow we meet at the door,\x01",
            "at o-nine-hundred hours sharp!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Ha, ha, ha! I need to make sure\x01",
            "everyone knows.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2598")

    Jump("loc_29D9")

    label("loc_259B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_260A")

    ChrTalk(    #104
        0xFE,
        (
            "Ha, ha, ha! Looks like everybody's\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Time for my favorite part...\x01",
            "ROOOOOLL CAAAAALL!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_260A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26D8")

    ChrTalk(    #106
        0xFE,
        (
            "Man... What an amazing match!\x01",
            "I was on the edge of my seat\x01",
            "the whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "Tomorrow we meet at the door,\x01",
            "at ten-hundred hours sharp!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Ha, ha, ha! I need to make sure\x01",
            "everyone knows.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_26D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2726")

    ChrTalk(    #109
        0xFE,
        "Sooo, is everyone here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "Time to go over the time table...\x02",
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_2726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_293C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27BD")

    ChrTalk(    #111
        0xFE,
        (
            "We're to meet at the door at\x01",
            "ten-hundred hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Now, if I could just get everyone\x01",
            "to walk single-file to the Grand\x01",
            "Arena...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2939")

    label("loc_27BD")

    OP_A2(0x2)

    ChrTalk(    #113
        0xFE,
        "Hrmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "We're to meet at the door at\x01",
            "ten-hundred hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "After the main event, then, we can\x01",
            "all head to the coffee house or\x01",
            "something for a nice, light dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Now, if I could just get everyone\x01",
            "to walk single-file to the Grand\x01",
            "Arena...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #117
        0xFE,
        (
            "Oooookay! Tomorrow shall be a\x01",
            "family outing to the tournament!\x01",
            "Sound good? Of course it does!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2939")

    Jump("loc_29D9")

    label("loc_293C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_29D9")

    ChrTalk(    #118
        0xFE,
        (
            "Ha, ha, ha! The Martial Arts\x01",
            "Competition is underway, at\x01",
            "long last!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "An event of this scale should\x01",
            "only be experienced as a family\x01",
            "unit, no?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D9")

    TalkEnd(0xFE)
    Return()

    # Function_13_2153 end

    def Function_14_29DD(): pass

    label("Function_14_29DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_29EA")
    Jump("loc_3078")

    label("loc_29EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2A68")

    ChrTalk(    #120
        0xFE,
        (
            "Something about the town just\x01",
            "seems...off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "The regular soldiers aren't\x01",
            "around...only those ones in\x01",
            "black.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2AEF")

    ChrTalk(    #122
        0xFE,
        (
            "I swear, that man is far more concerned with\x01",
            "what's to become of the Birthday Celebration\x01",
            "than any grown man SHOULD be!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2B61")

    ChrTalk(    #123
        0xFE,
        (
            "Whenever he gets like this, we have\x01",
            "to fill him up with food or he\x01",
            "basically...explodes. Mentally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2C1A")

    ChrTalk(    #124
        0xFE,
        (
            "Doesn't he realize that getting\x01",
            "all worked up about it won't\x01",
            "actually HELP anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Would it kill him to calm down\x01",
            "a little, and just see which way\x01",
            "the wind blows?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2CD7")

    ChrTalk(    #126
        0xFE,
        (
            "Honestly, I can't imagine WHERE\x01",
            "he gets all his energy from...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "He's been this way for as long\x01",
            "as I've known him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "You'd think he'd've calmed down\x01",
            "as he got older...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2D3F")

    ChrTalk(    #129
        0xFE,
        (
            "...But you know the worst part?\x01",
            "It's that high energy that I love\x01",
            "most about my husband!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2DB0")

    ChrTalk(    #130
        0xFE,
        (
            "Okay! My daughter's clearly pretty\x01",
            "exhausted...so I should probably\x01",
            "go help her get dinner ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2E12")

    ChrTalk(    #131
        0xFE,
        "I swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "I was WONDERING what he was doing\x01",
            "staying up so late last night...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2ED4")

    ChrTalk(    #133
        0xFE,
        (
            "I hope Norche has worked out her\x01",
            "differences with her husband...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Seems those two lovebirds are having\x01",
            "some problems. She told me all about\x01",
            "it during our trip to Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC4")

    label("loc_2ED4")

    OP_A2(0x3)

    ChrTalk(    #135
        0xFE,
        (
            "I hope Norche has worked out her\x01",
            "differences with her husband...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Seems those two lovebirds are having\x01",
            "some problems. She told me all about\x01",
            "it during our trip to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "And I mean ALL about it. She had...\x01",
            "a lot on her mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC4")

    Jump("loc_3078")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3078")

    ChrTalk(    #138
        0xFE,
        (
            "My husband... Well, he's crazy\x01",
            "for big, public events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "During the Martial Arts Competition\x01",
            "and the Queen's Birthday Celebration,\x01",
            "he's pretty much inconsolable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3078")

    TalkEnd(0xFE)
    Return()

    # Function_14_29DD end

    def Function_15_307C(): pass

    label("Function_15_307C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3089")
    Jump("loc_37BA")

    label("loc_3089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_317A")

    ChrTalk(    #140
        0xFE,
        (
            "I wonder how depressed Dad'd\x01",
            "be if they canceled the festival\x01",
            "this year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "It makes me nervous to see him sitting\x01",
            "there so quiet. He's pretty much a ticking\x01",
            "time bomb...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Though I guess I'm kinda the\x01",
            "same way. Kinda.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_317A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_31BE")

    ChrTalk(    #143
        0xFE,
        (
            "Finally... A moment of peace\x01",
            "in my home, sweet home!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_31BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_32EE")

    ChrTalk(    #144
        0xFE,
        (
            "The team Dad was rooting for lost in the finals,\x01",
            "so we're going to have a 'good hustle' dinner in\x01",
            "their honor tonight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "...to console him, pretty much.\x01",
            "Keep him from drifting into a\x01",
            "total slump.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "We always have to walk on eggshells\x01",
            "around that man. It's really, really\x01",
            "annoying!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_32EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_339C")

    ChrTalk(    #147
        0xFE,
        (
            "Actually, I've been fiddling with the arms of\x01",
            "Dad's alarm clock orbment. Figure he could use\x01",
            "some more sleep...for his sake AND ours...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "...Crap. He's up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_339C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_344C")

    ChrTalk(    #149
        0xFE,
        (
            "*sigh* I am SOOO tired of putting up\x01",
            "with my dad these past three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Isn't just knowing who won good\x01",
            "enough? Do we really have to go\x01",
            "watch the matches?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_344C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3522")

    ChrTalk(    #151
        0xFE,
        (
            "Why does he have to be up by 9 for a 10 o'clock\x01",
            "get-together, anyway? All he does is walk around\x01",
            "and wake everybody ELSE up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "What's my dad's problem? Why is he\x01",
            "so MENTAL about these matches?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_3522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_35D0")

    ChrTalk(    #153
        0xFE,
        (
            "If my mom or I don't join him on his\x01",
            "little trips, he'll just sulk the\x01",
            "whole day and make us feel bad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Being a daughter is seriously\x01",
            "hard work sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_35D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3656")

    ChrTalk(    #155
        0xFE,
        (
            "My dad needs a new hobby. He's\x01",
            "just...nuts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "He's going to rupture a blood\x01",
            "vessel if he doesn't just chill!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3704")

    label("loc_3656")

    OP_A2(0x4)

    ChrTalk(    #157
        0xFE,
        (
            "'Everybody,' he says. All three\x01",
            "of us, you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "My dad needs a new hobby. He's\x01",
            "just...nuts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "He's going to rupture a blood\x01",
            "vessel if he doesn't just chill!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3704")

    Jump("loc_37BA")

    label("loc_3707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_373E")

    ChrTalk(    #160
        0xFE,
        (
            "*sigh* It's that time of year,\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_373E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_37BA")

    ChrTalk(    #161
        0xFE,
        "It's always the same old story...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "I'm going to make dinner today\x01",
            "in place of my mom. She deserves\x01",
            "a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37BA")

    TalkEnd(0xFE)
    Return()

    # Function_15_307C end

    def Function_16_37BE(): pass

    label("Function_16_37BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3982")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_389A")

    ChrTalk(    #163
        0xFE,
        (
            "I did it! I passed the entrance\x01",
            "exam for the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "My husband's gone back to work now, so it's\x01",
            "totally my time to shine. He thinks HE'S the\x01",
            "master fisherman? Ha! I'LL SHOW HIM!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397F")

    label("loc_389A")

    OP_A2(0x1)

    ChrTalk(    #165
        0xFE,
        "Ohhh ho ho ho ho ho!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "I did it! I passed the entrance\x01",
            "exam for the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "My husband's gone back to work now, so it's\x01",
            "totally my time to shine. He thinks HE'S the\x01",
            "master fisherman? Ha! I'LL SHOW HIM!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_397F")

    Jump("loc_3EF5")

    label("loc_3982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3AEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_39F3")

    ChrTalk(    #168
        0xFE,
        (
            "I decided on a whim to try my\x01",
            "hand at fishing recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "And it was ever so enjoyable!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AEC")

    label("loc_39F3")

    OP_A2(0x1)

    ChrTalk(    #170
        0xFE,
        "Ohhh ho ho ho ho ho!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "My husband is so wrapped up in\x01",
            "his fishing that I decided to\x01",
            "try my hand at it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "I could hardly believe how much\x01",
            "I enjoyed it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "I just completely lost track of\x01",
            "time, I was so wrapped up in the\x01",
            "moment...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AEC")

    Jump("loc_3EF5")

    label("loc_3AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3AF9")
    Jump("loc_3EF5")

    label("loc_3AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3B03")
    Jump("loc_3EF5")

    label("loc_3B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3B0D")
    Jump("loc_3EF5")

    label("loc_3B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3B17")
    Jump("loc_3EF5")

    label("loc_3B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3BB4")

    ChrTalk(    #174
        0xFE,
        "That man just drives me crazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "Well, if that's the way it's going to be,\x01",
            "then I'll just have to take matters into\x01",
            "my own hands...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C83")

    label("loc_3BB4")

    OP_A2(0x1)

    ChrTalk(    #176
        0xFE,
        (
            "My husband left the house early\x01",
            "this morning to fish.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #177
        0xFE,
        "...Again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "Well, if that's the way it's going to be,\x01",
            "then I'll just have to take matters into\x01",
            "my own hands!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C83")

    Jump("loc_3EF5")

    label("loc_3C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3CE3")

    ChrTalk(    #179
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "Lately he hasn't even bothered to\x01",
            "talk to me when he gets home...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EF5")

    label("loc_3CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3D65")

    ChrTalk(    #181
        0xFE,
        (
            "My husband left again, without\x01",
            "saying a word...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "And he won't listen to me at all\x01",
            "when I criticize him for it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EF5")

    label("loc_3D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3E22")

    ChrTalk(    #183
        0xFE,
        (
            "Since my husband has been so busy with\x01",
            "his work and his hobbies, I've taken it\x01",
            "upon myself to do a bit of traveling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Yesterday I went to Bose with my\x01",
            "neighbor Marian.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EF5")

    label("loc_3E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3EF5")

    ChrTalk(    #185
        0xFE,
        (
            "Even when he IS home, all he ever\x01",
            "talks about are HIS hobbies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "What kind of a relationship is it when the two\x01",
            "of us hardly ever see one another...and only\x01",
            "ever engage in small talk when we do?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EF5")

    TalkEnd(0xFE)
    Return()

    # Function_16_37BE end

    def Function_17_3EF9(): pass

    label("Function_17_3EF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3F06")
    Jump("loc_4847")

    label("loc_3F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_40C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F80")

    ChrTalk(    #187
        0xFE,
        (
            "I know it's all very complicated, but\x01",
            "honestly, I just don't understand what\x01",
            "I've been doing wrong!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40C3")

    label("loc_3F80")

    OP_A2(0x0)

    ChrTalk(    #188
        0xFE,
        (
            "Hear me out, will you? My wife,\x01",
            "who's been missing for some time,\x01",
            "has finally come back home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "She said she's been off practicing\x01",
            "her FISHING these past few days,\x01",
            "if you can believe it!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #190
        0xFE,
        (
            "And even though she's only just\x01",
            "started, she's apparently already\x01",
            "gotten better at it than I am!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40C3")

    Jump("loc_4847")

    label("loc_40C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4126")

    ChrTalk(    #191
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "I'd give up fishing altogether...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "...if you'd just come home...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4847")

    label("loc_4126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_42F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_41DC")

    ChrTalk(    #194
        0xFE,
        (
            "I put in a request with the Bracer\x01",
            "Guild to find my missing wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "But they just told me not to\x01",
            "worry...said I should wait for\x01",
            "her to come home on her own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F4")

    label("loc_41DC")

    OP_A2(0x0)

    ChrTalk(    #196
        0xFE,
        (
            "I put in a request with the Bracer\x01",
            "Guild to find my missing wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "But they just told me not to\x01",
            "worry...said I should wait for\x01",
            "her to come home on her own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "I wonder if they even bothered writing\x01",
            "down my request, or if they basically\x01",
            "just dismissed it outright...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F4")

    Jump("loc_4847")

    label("loc_42F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4392")

    ChrTalk(    #199
        0xFE,
        "Bad tidings! BAD TIDINGS!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "My wife hasn't been home since\x01",
            "yesterday afternoon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "What if...the terrorists kidnapped\x01",
            "her? What then?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4847")

    label("loc_4392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_454C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4457")

    ChrTalk(    #202
        0xFE,
        (
            "I failed the entrance exam for\x01",
            "the Fisherman's Guild. Ugh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "...On top of everything else,\x01",
            "I haven't seen my wife since\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "It's been a really rotten day!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4549")

    label("loc_4457")

    OP_A2(0x0)

    ChrTalk(    #205
        0xFE,
        (
            "I failed the entrance exam for\x01",
            "the Fisherman's Guild. Ugh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "I'm going to have to practice\x01",
            "harder and try again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "...On top of everything else,\x01",
            "I haven't seen my wife since\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "It's been a really rotten day!\x02",
    )

    CloseMessageWindow()

    label("loc_4549")

    Jump("loc_4847")

    label("loc_454C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4556")
    Jump("loc_4847")

    label("loc_4556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_45E3")

    ChrTalk(    #209
        0xFE,
        (
            "You know that rumored entrance exam for\x01",
            "getting into the Fisherman's Guild?\x01",
            "Well, it actually exists!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "And I'm taking it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4847")

    label("loc_45E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_45ED")
    Jump("loc_4847")

    label("loc_45ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_477F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_46B1")

    ChrTalk(    #211
        0xFE,
        (
            "I hear that there's a group in\x01",
            "the city who call themselves\x01",
            "the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "It sounds right up my alley!\x01",
            "When I have some free time I\x01",
            "think I'll go check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477C")

    label("loc_46B1")

    OP_A2(0x0)

    ChrTalk(    #213
        0xFE,
        (
            "I hear that there's a group in\x01",
            "the city who call themselves\x01",
            "the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "Intriguing, no?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "It sounds right up my alley!\x01",
            "When I have some free time I\x01",
            "think I'll go check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477C")

    Jump("loc_4847")

    label("loc_477F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4847")

    ChrTalk(    #216
        0xFE,
        (
            "I'd normally be at work in the castle,\x01",
            "but the duke suddenly thrust a mandatory\x01",
            "vacation on me all of a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "Well, I don't have anything better\x01",
            "to do...so, I've just been fishing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4847")

    TalkEnd(0xFE)
    Return()

    # Function_17_3EF9 end

    SaveToFile()

Try(main)
