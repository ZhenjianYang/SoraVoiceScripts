from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4262   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4262.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Mayor Klaus',                          # 9
        'Lila',                                 # 10
        'Mayor Maybelle',                       # 11
        'Dean Collins',                         # 12
        'Shea',                                 # 13
        'Zin',                                  # 14
        'Libra',                                # 15
        'Primrose',                             # 16
        'Agate',                                # 17
        'Olivier',                              # 18
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
        'ED6_DT07/CH02353 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH02363 ._CH',             # 02
        'ED6_DT07/CH02603 ._CH',             # 03
        'ED6_DT07/CH02623 ._CH',             # 04
        'ED6_DT07/CH02540 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH02460 ._CH',             # 07
        'ED6_DT07/CH02230 ._CH',             # 08
        'ED6_DT07/CH02240 ._CH',             # 09
        'ED6_DT07/CH01100 ._CH',             # 0A
        'ED6_DT07/CH01350 ._CH',             # 0B
        'ED6_DT07/CH00050 ._CH',             # 0C
        'ED6_DT07/CH00030 ._CH',             # 0D
        'ED6_DT07/CH00073 ._CH',             # 0E
        'ED6_DT07/CH02350 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02353P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH02363P._CP',             # 02
        'ED6_DT07/CH02603P._CP',             # 03
        'ED6_DT07/CH02623P._CP',             # 04
        'ED6_DT07/CH02540P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH02460P._CP',             # 07
        'ED6_DT07/CH02230P._CP',             # 08
        'ED6_DT07/CH02240P._CP',             # 09
        'ED6_DT07/CH01100P._CP',             # 0A
        'ED6_DT07/CH01350P._CP',             # 0B
        'ED6_DT07/CH00050P._CP',             # 0C
        'ED6_DT07/CH00030P._CP',             # 0D
        'ED6_DT07/CH00073P._CP',             # 0E
        'ED6_DT07/CH02350P._CP',             # 0F
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -139520,
        Z                   = 4000,
        Y                   = 9500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -78950,
        Z                   = 0,
        Y                   = 5960,
        Direction           = 359,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -81130,
        Z                   = 0,
        Y                   = 61160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -77050,
        Z                   = 0,
        Y                   = 55320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_654",          # 01, 1
        "Function_2_677",          # 02, 2
        "Function_3_68D",          # 03, 3
        "Function_4_85B",          # 04, 4
        "Function_5_8F1",          # 05, 5
        "Function_6_DFA",          # 06, 6
        "Function_7_E5B",          # 07, 7
        "Function_8_101A",         # 08, 8
        "Function_9_1620",         # 09, 9
        "Function_10_23E3",        # 0A, 10
        "Function_11_25F6",        # 0B, 11
        "Function_12_37BE",        # 0C, 12
        "Function_13_4527",        # 0D, 13
        "Function_14_4562",        # 0E, 14
        "Function_15_501E",        # 0F, 15
        "Function_16_5696",        # 10, 16
        "Function_17_586C",        # 11, 17
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_278")
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_289")
    OP_A3(0x3FB)
    OP_A2(0x63F)
    Event(0, 15)

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_297")
    OP_A3(0x3FC)
    Event(0, 17)

    label("loc_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FB")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -28870, 200, 53540, 270)
    SetChrPos(0x9, -28040, 0, 54950, 211)
    SetChrPos(0xB, -83970, 200, -52980, 270)
    SetChrPos(0x8, -86020, 200, -52980, 90)

    label("loc_2FB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_30B"),
        (101, "loc_32A"),
        (SWITCH_DEFAULT, "loc_340"),
    )


    label("loc_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_327")
    Event(0, 14)

    label("loc_327")

    Jump("loc_340")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33D")
    OP_A2(0x640)
    Event(0, 16)

    label("loc_33D")

    Jump("loc_340")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36A")
    SetChrChipByIndex(0x0, 7)
    SetChrChipByIndex(0x1, 8)
    SetChrChipByIndex(0x138, 9)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_36A")

    OP_A2(0x639)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_42D")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 14)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x800)
    SetChrPos(0xD, -85910, 200, 59730, 270)
    SetChrChipByIndex(0x8, 15)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -25510, 0, -57090, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -84730, 250, -53560, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -28700, 250, 53020, 270)
    SetChrPos(0x9, -29640, 0, 51490, 0)
    Jump("loc_653")

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_43C")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_653")

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_44B")
    SetChrFlags(0xE, 0x80)
    Jump("loc_653")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_4FC")
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 14)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x800)
    SetChrPos(0xD, -85910, 200, 59730, 270)
    SetChrChipByIndex(0x8, 15)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -25510, 0, -57090, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -84730, 250, -53560, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -28700, 250, 53020, 270)
    SetChrPos(0x9, -29640, 0, 51490, 0)
    Jump("loc_653")

    label("loc_4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_END)), "loc_5AC")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -80180, 0, 61190, 0)
    OP_43(0xD, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x8, 15)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -25510, 0, -57090, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -84730, 250, -53560, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -28700, 250, 53020, 270)
    SetChrPos(0x9, -29640, 0, 51490, 0)
    SetChrPos(0xE, -138810, 0, 7070, 0)
    Jump("loc_653")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_653")
    SetChrChipByIndex(0xD, 14)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x800)
    SetChrPos(0xD, -85910, 200, 59730, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -87350, 300, -53560, 90)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -84730, 250, -53560, 270)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -28700, 250, 53020, 270)
    SetChrPos(0x9, -29640, 0, 51490, 0)

    label("loc_653")

    Return()

    # Function_0_26A end

    def Function_1_654(): pass

    label("Function_1_654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66D")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_654 end

    def Function_2_677(): pass

    label("Function_2_677")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_677")

    label("loc_68C")

    Return()

    # Function_2_677 end

    def Function_3_68D(): pass

    label("Function_3_68D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6FE")

    ChrTalk(    #0
        0x11,
        (
            "#035FI knew it would be, but I'm\x01",
            "still extremely impressed with\x01",
            "his performance. Bravo! Bravo!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_857")

    label("loc_6FE")

    OP_A2(0x7)

    ChrTalk(    #1
        0x11,
        (
            "#033F...Hmm?\x02\x03",

            "I do believe that's a harmonica\x01",
            "I hear!\x02\x03",

            "#030FAnd playing the same melody\x01",
            "darling Joshua did on the\x01",
            "shores of the lake in Bose!\x02\x03",

            "#035FI knew it would be, but I'm\x01",
            "still extremely impressed with\x01",
            "his performance. Bravo! Bravo!\x02\x03",

            "I am unfamiliar with the original\x01",
            "piece...but I doubt it's as sad\x01",
            "and mournful as this rendition!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_857")

    TalkEnd(0xFE)
    Return()

    # Function_3_68D end

    def Function_4_85B(): pass

    label("Function_4_85B")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0x10,
        (
            "#050F...\x02\x03",

            "Whatever. I've still got a\x01",
            "score to settle with that\x01",
            "guy in the red mask.\x02\x03",

            "#057FI'm not about to leave things\x01",
            "the way they are!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_85B end

    def Function_5_8F1(): pass

    label("Function_5_8F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_9E7")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_91D")
    SetChrSubChip(0xFE, 2)
    Jump("loc_94E")

    label("loc_91D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_933")
    SetChrSubChip(0xFE, 1)
    Jump("loc_94E")

    label("loc_933")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_949")
    SetChrSubChip(0xFE, 0)
    Jump("loc_94E")

    label("loc_949")

    SetChrSubChip(0xFE, 2)

    label("loc_94E")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #3
        0xD,
        (
            "#070FI must admit, I didn't think I'd\x01",
            "get quite so full at the castle.\x02\x03",

            "Peace truly does make the spirits\x01",
            "sweeter, does it not?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_DF6")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9F1")
    Jump("loc_DF6")

    label("loc_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_9FB")
    Jump("loc_DF6")

    label("loc_9FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_BE2")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x102, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A24")
    SetChrSubChip(0xFE, 2)
    Jump("loc_A55")

    label("loc_A24")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A3A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_A55")

    label("loc_A3A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A50")
    SetChrSubChip(0xFE, 0)
    Jump("loc_A55")

    label("loc_A50")

    SetChrSubChip(0xFE, 2)

    label("loc_A55")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B12")

    ChrTalk(    #4
        0xD,
        (
            "#070FWhat magnificent architecture! What\x01",
            "fantastic design! ...And the castle's\x01",
            "not bad either.\x02\x03",

            "Miss, I think I shall have to request\x01",
            "a room cleaning post haste.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDA")

    label("loc_B12")

    OP_A2(0x2)

    ChrTalk(    #5
        0xD,
        (
            "#073F...What's this...?\x02\x03",

            "#070F...\x02\x03",

            "What magnificent architecture! What\x01",
            "fantastic design! ...And the castle's\x01",
            "not bad either.\x02\x03",

            "Miss, I think I shall have to request\x01",
            "a room cleaning post haste.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDA")

    SetChrSubChip(0xFE, 0)
    Jump("loc_DF6")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 7)), scpexpr(EXPR_END)), "loc_C91")

    ChrTalk(    #6
        0xD,
        (
            "#070FThe food was amazing, but the\x01",
            "conversation and flow of wine\x01",
            "were much...less so.\x02\x03",

            "So if you'll excuse me, I have\x01",
            "some lost drinking time to make\x01",
            "up for...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF6")

    label("loc_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_DF6")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CBA")
    SetChrSubChip(0xFE, 1)
    Jump("loc_CBF")

    label("loc_CBA")

    SetChrSubChip(0xFE, 0)

    label("loc_CBF")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D36")

    ChrTalk(    #7
        0xD,
        (
            "#070FIt still bugs me, about Olivier.\x02\x03",

            "Not that there's anything I\x01",
            "could've done for him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1")

    label("loc_D36")

    OP_A2(0x2)

    ChrTalk(    #8
        0xD,
        (
            "#070FI'm so hungry! Usually by this\x01",
            "time I'm already in some bar,\x01",
            "stuffing my face...\x02\x03",

            "Isn't our food ready yet? I'm\x01",
            "literally salivating thinking \x01",
            "about this full-course dinner!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF1")

    SetChrSubChip(0xFE, 0)

    label("loc_DF6")

    TalkEnd(0xFE)
    Return()

    # Function_5_8F1 end

    def Function_6_DFA(): pass

    label("Function_6_DFA")

    TalkBegin(0xFE)

    ChrTalk(    #9
        0xFE,
        "Time to clean the rooms.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "It's been hectic preparing\x01",
            "for so many guests tonight!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_DFA end

    def Function_7_E5B(): pass

    label("Function_7_E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_E68")
    Jump("loc_1016")

    label("loc_E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_F15")

    ChrTalk(    #11
        0xFE,
        (
            "Castle Blueprints... The\x01",
            "Sept-Terrions... Chronicles\x01",
            "of the Hundred Days War...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "The Intelligence Division\x01",
            "finally sent back all the\x01",
            "books they borrowed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1016")

    label("loc_F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_F1F")
    Jump("loc_1016")

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_F29")
    Jump("loc_1016")

    label("loc_F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_F90")

    ChrTalk(    #13
        0xFE,
        (
            "Hmm? Seems the castle blueprints\x01",
            "are missing too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "What do they need with those?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1016")

    label("loc_F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_1016")

    ChrTalk(    #15
        0xFE,
        (
            "What are those people at the \x01",
            "Intelligence Division up to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Taking important documents\x01",
            "without official permission...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1016")

    TalkEnd(0xFE)
    Return()

    # Function_7_E5B end

    def Function_8_101A(): pass

    label("Function_8_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1029")
    Call(0, 9)
    Jump("loc_161F")

    label("loc_1029")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1126")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1055")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1086")

    label("loc_1055")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_106B")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1086")

    label("loc_106B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1081")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1086")

    label("loc_1081")

    SetChrSubChip(0xFE, 2)

    label("loc_1086")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #17
        0xB,
        (
            "#780FWhat a nice, cool night.\x02\x03",

            "#780FThanks to you all, the kingdom\x01",
            "is at peace once more.\x02\x03",

            "Cassius has raised some wonderful\x01",
            "children.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_161C")

    label("loc_1126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1130")
    Jump("loc_161C")

    label("loc_1130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_113A")
    Jump("loc_161C")

    label("loc_113A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1219")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1163")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1194")

    label("loc_1163")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1179")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1194")

    label("loc_1179")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_118F")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1194")

    label("loc_118F")

    SetChrSubChip(0xFE, 2)

    label("loc_1194")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #18
        0xB,
        (
            "#780FOh! A private visit from\x01",
            "Mistress Hilda herself!\x02\x03",

            "A trainee maid inspection, is it?\x01",
            "All right, then...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_161C")

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_133B")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1242")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1273")

    label("loc_1242")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1258")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1273")

    label("loc_1258")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_126E")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1273")

    label("loc_126E")

    SetChrSubChip(0xFE, 2)

    label("loc_1273")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #19
        0xB,
        (
            "#780FThe colonel's points are all\x01",
            "very logical and rational...\x02\x03",

            "But I believe it would be best to get\x01",
            "the particulars from Her Majesty and\x01",
            "Her Highness the Princess directly.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_161C")

    label("loc_133B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_161C")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1364")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1395")

    label("loc_1364")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_137A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1395")

    label("loc_137A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1390")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1395")

    label("loc_1390")

    SetChrSubChip(0xFE, 2)

    label("loc_1395")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1457")

    ChrTalk(    #20
        0xB,
        (
            "#782FIt does bother me that no one's\x01",
            "heard from Kloe yet...\x02\x03",

            "She probably just dropped by to check\x01",
            "on the orphanage before setting off\x01",
            "for the capital, but even so...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1617")

    label("loc_1457")

    OP_A2(0x6)

    ChrTalk(    #21
        0xB,
        (
            "#780FOh yes...were you able to meet\x01",
            "with Kloe?\x02\x03",

            "I'd heard you made some kind of promise\x01",
            "to meet at the capital, but I wasn't\x01",
            "sure if you'd actually done so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#007FNo, even the guild has yet to\x01",
            "hear from her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#014FBut she should be at the capital\x01",
            "by now, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "#782FShe should be...\x02\x03",

            "#783FStill, though...it bothers me.\x02\x03",

            "She probably just dropped by to check\x01",
            "on the orphanage before setting off\x01",
            "for the capital, but even so...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1617")

    SetChrSubChip(0xFE, 0)

    label("loc_161C")

    TalkEnd(0xFE)

    label("loc_161F")

    Return()

    # Function_8_101A end

    def Function_9_1620(): pass

    label("Function_9_1620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8A")
    OP_A2(0x63B)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -85750, 0, -55050, 0)
    SetChrPos(0x102, -86740, 0, -55050, 0)
    OP_6D(-85810, 0, -53740, 0)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0x8, 2)
    OP_0D()

    ChrTalk(    #25
        0x8,
        (
            "#601F#3PAh, Joshua. Estelle. You made\x01",
            "it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        "#780FIt's been quite a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#004F...Dean Collins?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#4P#010FYou were invited to the banquet\x01",
            "as well, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "#780FI just arrived today via\x01",
            "airship from Ruan.\x02\x03",

            "...A little mayoral birdie told\x01",
            "me you two won the tournament.\x02\x03",

            "Jill and everyone else will be\x01",
            "so happy to hear it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#506FHeh heh...thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#4P#010FI had no idea we'd be seeing you\x01",
            "here, Dean Collins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#603F#3PDean Collins is a member of the\x01",
            "Royal Assembly, and a man of\x01",
            "great respect in Liberl.\x02\x03",

            "It's only fitting he be given\x01",
            "a seat at this banquet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        (
            "#780FA man of great respect, he says...\x01",
            "You flatter me, Mayor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#505F...What's the Royal Assembly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#4P#010FIt's a meeting held once per year\x01",
            "to address matters affecting the\x01",
            "kingdom.\x02\x03",

            "The queen, mayors of every city and other \x01",
            "representatives all come together to try\x01",
            "solving various problems of state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#501FWow. Sounds big.\x02\x03",

            "So all of those guys have been\x01",
            "invited here tonight, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        (
            "#783FNo... I'd say only about half.\x02\x03",

            "Her Majesty is still ill and\x01",
            "General Morgan is away on\x01",
            "official military business.\x02\x03",

            "And Mayor Dalmore of Ruan was\x01",
            "arrested in that nasty affair.\x02\x03",

            "And Professor Russell...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(    #38
        0x8,
        (
            "#603FHe is a bit too entrenched in\x01",
            "too many unknowns right now.\x02\x03",

            "We don't know how true all this talk is of\x01",
            "the Royal Guardsmen being involved in some\x01",
            "underground terrorist organization.\x02\x03",

            "#602F...It's hardly the time to be\x01",
            "holding a feast at all, if you\x01",
            "ask me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        "#4P#015F...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(300)

    ChrTalk(    #41
        0xB,
        (
            "#780FWell, we can use this chance\x01",
            "to see where Duke Dunan stands\x01",
            "on all of these issues.\x02\x03",

            "We need his permission to have\x01",
            "an audience with Her Majesty,\x01",
            "regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#603FYes. That's the biggest issue\x01",
            "here, without a doubt.\x02\x03",

            "#602FBarring us from seeing Her Majesty\x01",
            "is the height of idiocy and mis-\x01",
            "management!\x02\x03",

            "#601FI would like to pay my respects\x01",
            "to Princess Klaudia, as well,\x01",
            "but it's the same story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#501FPrincess Klaudia's...the queen's\x01",
            "granddaughter...right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        "#4P#014FDoes she live here in the castle?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 1)
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(200)

    ChrTalk(    #45
        0x8,
        (
            "#604F#3PNo, it's my understanding her\x01",
            "actual residence is elsewhere.\x02\x03",

            "But I'm told she's come to the\x01",
            "capital, as of a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#501FShe's...here, then?\x02\x03",

            "#502FI'd really love to meet her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        "#781FI'm sure you'll have a chance.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0x8, 0)
    EventEnd(0x0)
    Jump("loc_23E2")

    label("loc_1F8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_2146")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1FF7")

    ChrTalk(    #48
        0x8,
        (
            "#600FWe've got to do the best we\x01",
            "can to support the queen \x01",
            "during this tragic time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2143")

    label("loc_1FF7")

    OP_A2(0x3)

    ChrTalk(    #49
        0x8,
        (
            "#600FTo have one's daughter taken hostage...\x01",
            "I can't even imagine how painful an\x01",
            "experience that must be!\x02\x03",

            "Colonel Richard said he cherished this country,\x01",
            "and wished to protect it...but was it all a lie,\x01",
            "or did he simply choose the wrong path?\x02\x03",

            "We've got to do the best we\x01",
            "can to support the queen \x01",
            "during this tragic time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2143")

    Jump("loc_23DF")

    label("loc_2146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2150")
    Jump("loc_23DF")

    label("loc_2150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_215A")
    Jump("loc_23DF")

    label("loc_215A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_21A0")

    ChrTalk(    #50
        0x8,
        (
            "#600FMadame Hilda...What brings\x01",
            "you here at this hour?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DF")

    label("loc_21A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_22CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_21F9")

    ChrTalk(    #51
        0x8,
        (
            "#600FEvents are unfolding so quickly,\x01",
            "I hardly have time to react!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C8")

    label("loc_21F9")

    OP_A2(0x3)

    ChrTalk(    #52
        0x8,
        (
            "#602FI can't believe the queen's\x01",
            "so worried she's considering\x01",
            "abdication...\x02\x03",

            "And Princess Klaudia choosing\x01",
            "a husband, at her age?!\x02\x03",

            "#603FEvents are unfolding so quickly,\x01",
            "I hardly have time to react!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C8")

    Jump("loc_23DF")

    label("loc_22CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_23DF")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22F4")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2325")

    label("loc_22F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_230A")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2325")

    label("loc_230A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2320")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2325")

    label("loc_2320")

    SetChrSubChip(0xFE, 1)

    label("loc_2325")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #53
        0x8,
        (
            "#603FHonestly, why would we be holding\x01",
            "a banquet now, under these circum-\x01",
            "stances?\x02\x03",

            "I can't fathom why the duke\x01",
            "would allow this. It's in\x01",
            "poor taste, at the least!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_23DF")

    TalkEnd(0xFE)

    label("loc_23E2")

    Return()

    # Function_9_1620 end

    def Function_10_23E3(): pass

    label("Function_10_23E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F2")
    Call(0, 11)
    Jump("loc_25F5")

    label("loc_23F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_24A5")

    ChrTalk(    #54
        0x9,
        (
            "#620FI had wondered what would become\x01",
            "of us were we to be caught up in\x01",
            "events...\x02\x03",

            "But at least Her Majesty is able\x01",
            "to take some much-needed respite\x01",
            "as a result.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F2")

    label("loc_24A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_24AF")
    Jump("loc_25F2")

    label("loc_24AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_24B9")
    Jump("loc_25F2")

    label("loc_24B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_24F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_24D8")

    ChrTalk(    #55
        0x9,
        "#620F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F4")

    label("loc_24D8")

    OP_A2(0x4)

    ChrTalk(    #56
        0x9,
        (
            "#620F...!\x02\x03",

            "#621F...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F4")

    Jump("loc_25F2")

    label("loc_24F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_2573")

    ChrTalk(    #57
        0x9,
        (
            "#620FSeems it was a banquet to remember...\x02\x03",

            "And now my mistress has yet another\x01",
            "worry to wrinkle her brow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F2")

    label("loc_2573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_25F2")

    ChrTalk(    #58
        0x9,
        (
            "#621FMy mistress has been looking\x01",
            "forward to seeing you again.\x02\x03",

            "Please come visit her in\x01",
            "Bose again sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F2")

    TalkEnd(0xFE)

    label("loc_25F5")

    Return()

    # Function_10_23E3 end

    def Function_11_25F6(): pass

    label("Function_11_25F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB4")
    OP_A2(0x63A)
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -28930, 0, 54500, 180)
    SetChrPos(0x102, -29780, 0, 54500, 180)
    OP_6D(-29260, 0, 53440, 0)
    SetChrSubChip(0xA, 2)
    OP_8C(0x9, 0, 0)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(    #59
        0x101,
        "#501FMayor Maybelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        "#010FAnd Lila!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        "#621FJoshua! Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        (
            "#611FAh, here at last!\x02\x03",

            "I kept wondering when you'd get\x01",
            "here. I was practically counting\x01",
            "the seconds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#001FSo you were invited here too, Mayor?\x02\x03",

            "#004F...H-Hey, wait... You were waiting\x01",
            "for us? How did you know we were\x01",
            "coming?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "#610FI heard from Mayor Klaus.\x02\x03",

            "I heard about a pair of children who entered the\x01",
            "tournament, won its championship, and were \x01",
            "invited to a grand royal banquet in the castle.\x02\x03",

            "#617FIf I'd known, I would have\x01",
            "canceled my appointments and\x01",
            "come to cheer you on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "#623FBegging your pardon, ma'am...\x02\x03",

            "But that would have been quite\x01",
            "impossible, given the circum-\x01",
            "stances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#612FYes, yes, I'm aware. I'm trying\x01",
            "to be polite!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#506FHa ha ha! Don't worry. I know\x01",
            "how busy you must be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "#615FI'm sure the queen has no time to waste\x01",
            "at a banquet, what with everything else\x01",
            "going on. What is Duke Dunan thinking?!\x02\x03",

            "That captain was so stubborn about\x01",
            "inviting me, too... I had no real\x01",
            "choice but to accept!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        "#012FDo you mean Captain Amalthea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "#612FYes, that's her.\x02\x03",

            "Her words were polite enough, but she\x01",
            "gave me an evil eye while she spoke\x01",
            "them. I dared not refuse her request!\x02\x03",

            "I haven't heard from General\x01",
            "Morgan in quite some time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#002FWait, does that mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#012F...You haven't heard any word\x01",
            "from the Haken Gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "#615F'The general is unavailable'\x01",
            "is the longest message I've\x01",
            "been able to wring from them.\x02\x03",

            "It would seem he's busy with \x01",
            "these 'anti-terrorist counter-\x01",
            "measures,' or what-have-you.\x02\x03",

            "#610FI had hoped he'd be in attendance\x01",
            "at this banquet tonight...\x02\x03",

            "But I guess he couldn't pull\x01",
            "himself away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#003FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#012FWhat do you think about all of\x01",
            "this, Mayor?\x02\x03",

            "Putting mayors from every city\x01",
            "in the same place, at a time\x01",
            "like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "#613FWell...\x02\x03",

            "If the queen were to be in attendance,\x01",
            "I would expect some announcement of no\x01",
            "small importance...\x02\x03",

            "#611FBut as it is, this feels like\x01",
            "the duke has too much time\x01",
            "on his greasy, chubby hands.\x02\x03",

            "He's letting this position of\x01",
            "royal proxy go to his head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#509FThat sounds about right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#015FBut there might still be some\x01",
            "kind of official announcement,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "#611FWell, whatever may come of the\x01",
            "night, the grand chef here is\x01",
            "the best in all the kingdom.\x02\x03",

            "I plan to enjoy the dinner, pay\x01",
            "my respects to Her Majesty, and\x01",
            "return to Bose post-haste.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    SetChrSubChip(0xA, 0)
    EventEnd(0x0)
    Jump("loc_37BD")

    label("loc_2FB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_317F")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FE0")
    SetChrSubChip(0xFE, 2)
    Jump("loc_3011")

    label("loc_2FE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FF6")
    SetChrSubChip(0xFE, 1)
    Jump("loc_3011")

    label("loc_2FF6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_300C")
    SetChrSubChip(0xFE, 0)
    Jump("loc_3011")

    label("loc_300C")

    SetChrSubChip(0xFE, 2)

    label("loc_3011")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_30B4")

    ChrTalk(    #80
        0xA,
        (
            "#610FEstelle, tomorrow we're planning to\x01",
            "take the first airship to Bose.\x02\x03",

            "#611FIf you have a chance, please\x01",
            "come by and visit us again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3177")

    label("loc_30B4")

    OP_A2(0x5)

    ChrTalk(    #81
        0xA,
        (
            "#610FEstelle, tomorrow we're planning to\x01",
            "take the first airship to Bose.\x02\x03",

            "#611FIf you have a chance, please\x01",
            "come by and visit us again.\x02\x03",

            "We can have another chat over\x01",
            "dinner at Anterose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3177")

    SetChrSubChip(0xFE, 0)
    Jump("loc_37BA")

    label("loc_317F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3189")
    Jump("loc_37BA")

    label("loc_3189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_3193")
    Jump("loc_37BA")

    label("loc_3193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_347F")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31BC")
    SetChrSubChip(0xFE, 2)
    Jump("loc_31ED")

    label("loc_31BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31D2")
    SetChrSubChip(0xFE, 1)
    Jump("loc_31ED")

    label("loc_31D2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31E8")
    SetChrSubChip(0xFE, 0)
    Jump("loc_31ED")

    label("loc_31E8")

    SetChrSubChip(0xFE, 2)

    label("loc_31ED")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3262")

    ChrTalk(    #82
        0xA,
        (
            "#610FAre these all students of yours?\x02\x03",

            "It reminds me of when Lila\x01",
            "first came to my house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3477")

    label("loc_3262")

    OP_A2(0x5)

    ChrTalk(    #83
        0xA,
        (
            "#610FMadame Hilda... What a \x01",
            "long time it's been!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x0,
        "Head Maid Hilda",
        "#712FWhy, Mayor, you look simply exhausted!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "#617FHo ho... There's no hiding\x01",
            "anything from you, Madame.\x02\x03",

            "#610FI had some pressing business\x01",
            "to finish before I left Bose,\x01",
            "so I haven't yet slept.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #86
        0x0,
        "Head Maid Hilda",
        (
            "#710FThat won't do at all!\x02\x03",

            "I'll have some incense sent to\x01",
            "you right away. Good stuff that\x01",
            "should have you out in no time!\x02\x03",

            "I believe we just got some in from\x01",
            "the East only a very short while\x01",
            "ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "#610FThank you for your kindness.\x02",
    )

    CloseMessageWindow()

    label("loc_3477")

    SetChrSubChip(0xFE, 0)
    Jump("loc_37BA")

    label("loc_347F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_3602")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34A8")
    SetChrSubChip(0xFE, 2)
    Jump("loc_34D9")

    label("loc_34A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34BE")
    SetChrSubChip(0xFE, 1)
    Jump("loc_34D9")

    label("loc_34BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34D4")
    SetChrSubChip(0xFE, 0)
    Jump("loc_34D9")

    label("loc_34D4")

    SetChrSubChip(0xFE, 2)

    label("loc_34D9")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_355E")

    ChrTalk(    #88
        0xA,
        (
            "#612FDuke Dunan as official successor\x01",
            "to the throne...\x02\x03",

            "If anything could bring on a migraine,\x01",
            "it's that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FA")

    label("loc_355E")

    OP_A2(0x5)

    ChrTalk(    #89
        0xA,
        (
            "#612FWhat a shock this banquet\x01",
            "has been.\x02\x03",

            "Duke Dunan as official successor\x01",
            "to the throne...\x02\x03",

            "#617FIf anything could bring on a migraine,\x01",
            "it's that!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FA")

    SetChrSubChip(0xFE, 0)
    Jump("loc_37BA")

    label("loc_3602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_37BA")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_362B")
    SetChrSubChip(0xFE, 2)
    Jump("loc_365C")

    label("loc_362B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3641")
    SetChrSubChip(0xFE, 1)
    Jump("loc_365C")

    label("loc_3641")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3657")
    SetChrSubChip(0xFE, 0)
    Jump("loc_365C")

    label("loc_3657")

    SetChrSubChip(0xFE, 2)

    label("loc_365C")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3702")

    ChrTalk(    #90
        0xA,
        (
            "#615FWhen the duke came to Bose\x01",
            "before, he acted like a\x01",
            "spoiled child...\x02\x03",

            "#617FI received so many complaints\x01",
            "from the citizens he angered!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B5")

    label("loc_3702")

    OP_A2(0x5)

    ChrTalk(    #91
        0xA,
        (
            "#615FDuke Dunan is such a nuisance.\x02\x03",

            "When the duke came to Bose\x01",
            "before, he acted like a\x01",
            "spoiled child...\x02\x03",

            "#617FI received so many complaints\x01",
            "from the citizens he angered!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B5")

    SetChrSubChip(0xFE, 0)

    label("loc_37BA")

    TalkEnd(0xFE)

    label("loc_37BD")

    Return()

    # Function_11_25F6 end

    def Function_12_37BE(): pass

    label("Function_12_37BE")

    EventBegin(0x0)
    SetChrPos(0x102, -52050, 0, 2040, 0)
    SetChrPos(0x101, -52050, 0, 2040, 0)
    SetChrPos(0x108, -52050, 0, 2040, 0)
    SetChrPos(0xC, -52050, 0, 2040, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    OP_69(0xC, 0x0)
    OP_6A(0xC)

    def lambda_382D():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_382D)
    Sleep(500)

    def lambda_384D():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_384D)
    Sleep(500)

    def lambda_386D():

        label("loc_386D")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_386D")

    QueueWorkItem2(0x102, 2, lambda_386D)

    def lambda_387E():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_387E)
    Sleep(500)

    def lambda_389E():
        OP_8E(0xFE, 0xFFFECE9C, 0x0, 0x884, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_389E)
    WaitChrThread(0xC, 0x1)

    def lambda_38BE():
        OP_8E(0xFE, 0xFFFECB86, 0x0, 0x1CDE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_38BE)
    WaitChrThread(0x101, 0x1)

    def lambda_38DE():
        OP_8E(0xFE, 0xFFFEC7F8, 0x0, 0x159A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38DE)
    WaitChrThread(0x102, 0x1)

    def lambda_38FE():
        OP_8E(0xFE, 0xFFFECD2A, 0x0, 0x1554, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38FE)
    WaitChrThread(0x108, 0x1)

    def lambda_391E():
        OP_8E(0xFE, 0xFFFECA50, 0x0, 0x1162, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_391E)
    WaitChrThread(0xC, 0x1)
    Sleep(200)
    OP_6F(0x1D, 0)
    OP_70(0x1D, 0x3C)
    Sleep(400)
    OP_8E(0xC, 0xFFFEC668, 0x0, 0x1C52, 0x7D0, 0x0)
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #92
        0xC,
        (
            "#3PThis is the room where\x01",
            "you'll be staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xC,
        "#3PPlease, go on in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#501FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        "#010FPardon us...\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_44(0x102, 0x2)
    OP_43(0x102, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x108, 0x1, 0x0, 0xD)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(-89640, 0, 57110, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xC, -80040, 0, 50510, 0)
    SetChrPos(0x101, -80880, 0, 53000, 270)
    SetChrPos(0x102, -79650, 0, 53710, 270)
    SetChrPos(0x108, -78830, 0, 52390, 270)
    SetChrFlags(0xD, 0x80)
    OP_6D(-79120, 0, 55910, 5000)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)

    ChrTalk(    #96
        0x101,
        "#004F#2PHoly Stregas!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#010F#2PI never imagined we'd ever stay\x01",
            "in a place like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x108,
        (
            "#071F#2PNiiiice. This will make a good\x01",
            "story for later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xC,
        (
            "#2PI believe there is still some\x01",
            "time before the party.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BC2():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BC2)

    def lambda_3BD0():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BD0)

    def lambda_3BDE():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3BDE)
    OP_6D(-79790, 0, 52600, 1200)

    ChrTalk(    #100
        0xC,
        (
            "#4PYou are free to explore the\x01",
            "castle, but the security areas\x01",
            "are off limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xC,
        (
            "I ask that you refrain from\x01",
            "entering those areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#505FUmm...can you be a little\x01",
            "more specific?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        (
            "Most significantly, the Royal\x01",
            "Keep, where the queen resides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xC,
        (
            "It is a small palace of sorts,\x01",
            "built on the Garden Terrace\x01",
            "on the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#008FGarden Terrace...?\x01",
            "That sounds nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xC,
        (
            "#4PHa ha... The terrace is where Her\x01",
            "Majesty greets the people of Grancel\x01",
            "from during the birthday festivities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xC,
        (
            "So, you cannot go into the Royal\x01",
            "Keep itself, but you may visit the\x01",
            "Garden Terrace if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xC,
        "As for the other restricted areas...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xC,
        (
            "There's the Royal Guard Room\x01",
            "and also the Treasury, I believe.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    ChrTalk(    #110
        0x102,
        "#012FThe Royal Guard Room...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x108,
        (
            "#072FI guess they're still wanted\x01",
            "for questioning about all that\x01",
            "terrorist stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xC,
        "Y-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xC,
        (
            "The Intelligence Division is\x01",
            "currently occupying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "Entrance is restricted, so\x01",
            "please abide by the rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#015FUnderstood.\x02\x03",

            "#010FBy the way, what are the others\x01",
            "who were invited doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        "They've already arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        (
            "I imagine they're relaxing\x01",
            "in their respective rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x102,
        "#010FAll right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#501FSo Mayor Klaus is here, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        (
            "Oh, yes.\x01",
            "He arrived some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        (
            "Now, if you'll excuse me,\x01",
            "I'll be off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "If you need anything else, please\x01",
            "contact the first floor waiting room.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    def lambda_4160():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4160)
    OP_8E(0xC, 0xFFFEC6F4, 0x0, 0xBC3E, 0x7D0, 0x0)
    SetChrFlags(0xC, 0x4)

    ChrTalk(    #123
        0x101,
        "#500FNow, then...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x102, 0x101, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #124
        "\x07\x05Estelle and Joshua exchanged a look that went unnoticed by Zin.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_421E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_421E)
    Sleep(400)
    TurnDirection(0x102, 0x108, 400)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #125
        0x101,
        (
            "#006F...Hey, Zin?\x02\x03",

            "We want to go and walk around\x01",
            "the castle for a little bit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        (
            "#010FWe'll be back in time for\x01",
            "the party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x108,
        (
            "#075FHuh... It must be nice to be so young.\x01",
            "I'm worn out after the tournament.\x02\x03",

            "#070FNo problem. Have fun.\x02\x03",

            "Me, I'm going to kick back and relax\x01",
            "in this oh-so-luxurious room.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-79060, 0, 5600, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -79060, 0, 9840, 0)
    SetChrPos(0x102, -79060, 0, 9840, 0)
    OP_6F(0x1D, 60)

    def lambda_43BE():
        OP_8E(0xFE, 0xFFFECB2C, 0x0, 0x157C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43BE)
    Sleep(600)

    def lambda_43DE():
        OP_8E(0xFE, 0xFFFECB2C, 0x0, 0x1900, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43DE)
    WaitChrThread(0x101, 0x1)

    def lambda_43FE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43FE)
    WaitChrThread(0x102, 0x1)

    def lambda_4411():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4411)
    OP_72(0x1D, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1D, 0x0)
    OP_73(0x1D)
    OP_71(0x1D, 0x800)

    ChrTalk(    #128
        0x101,
        (
            "#006F#4PWe need to get as much done as\x01",
            "we can before the party starts.\x02\x03",

            "First, Julia told us that we have\x01",
            "to talk to the head maid, Hilda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x102,
        (
            "#010FI'd like to say hello to the\x01",
            "other invitees, too.\x02\x03",

            "We likely know most of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_6A(0x0)
    ClearMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_12_37BE end

    def Function_13_4527(): pass

    label("Function_13_4527")

    OP_8E(0xFE, 0xFFFECB5E, 0x0, 0x1CA2, 0xBB8, 0x0)

    def lambda_4541():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4541)
    OP_8E(0xFE, 0xFFFECB68, 0x0, 0x2602, 0xBB8, 0x0)
    Return()

    # Function_13_4527 end

    def Function_14_4562(): pass

    label("Function_14_4562")

    EventBegin(0x0)
    OP_6D(-80000, 0, 52700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0xD, 0x80)
    AddParty(0x7, 0xFF)
    SetChrPos(0x101, -79490, 0, 51290, 0)
    SetChrPos(0x102, -80530, 0, 51090, 0)
    SetChrPos(0x108, -80180, 0, 61190, 0)

    def lambda_45E2():
        OP_6D(-79580, 0, 57340, 2000)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_45E2)
    Sleep(1000)
    OP_8C(0x108, 180, 400)
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #130
        0x108,
        (
            "#070FHey, guys.\x01",
            "Talk about being late.\x02\x03",

            "The party's about to start,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_465E():
        OP_6D(-80100, 0, 60780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_465E)

    def lambda_4676():
        OP_8E(0xFE, 0xFFFEC884, 0x0, 0xE98E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4676)
    Sleep(300)

    def lambda_4696():
        OP_8E(0xFE, 0xFFFEC49C, 0x0, 0xE948, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4696)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #131
        0x101,
        (
            "#506FSorry...\x02\x03",

            "We got so caught up in sightseeing\x01",
            "that we lost track of time.\x02\x03",

            "#006FPlus, we also talked to all\x01",
            "of the mayors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x108,
        (
            "#073FHuh...\x01",
            "Well, aren't we well-connected?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        (
            "#010FWe're close friends with the\x01",
            "mayor of Rolent.\x02\x03",

            "Plus, we've met the other mayors\x01",
            "in the course of our travels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x108,
        (
            "#074FAhh, I see.\x02\x03",

            "I guess your work as bracers has\x01",
            "caused you to meet quite a few\x01",
            "big shots.\x02\x03",

            "#070FYou two sure get around\x01",
            "for Junior Bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#506FHeh heh...\x01",
            "Yeah, you might say that.\x02\x03",

            "#501FHave you done any bracer assignments\x01",
            "since we came to Grancel?\x02\x03",

            "I guess it's not all that different\x01",
            "in other countries, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x108,
        (
            "#070FRight. For a full-fledged bracer,\x01",
            "nationality isn't an issue when\x01",
            "it comes to your work.\x02\x03",

            "The prelim fights and legal procedures\x01",
            "at the embassy kept me too busy to get\x01",
            "any actual work done, though.\x02\x03",

            "#075FBut hey, there are four other bracers\x01",
            "on duty, too, which isn't so bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#010FNormally, that would be enough\x01",
            "to handle most cases, I'd imagine.\x02\x03",

            "But with all of them concentrated in\x01",
            "Grancel, that must make it tough to\x01",
            "handle any cases in other regions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x108,
        (
            "#071FHa ha ha...\x01",
            "Yeah, could be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#007FUgh... I feel like a goose just\x01",
            "walked over my grave...\x02\x03",

            "#505FI wonder what's going on with\x01",
            "Schera, back in Rolent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x108,
        (
            "#073FNow, that name rings a bell...\x02\x03",

            "You wouldn't happen to be talking\x01",
            "about Scherazard, would you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #141
        0x101,
        "#004F...You know her?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        (
            "#014FShe's our mentor, and she's\x01",
            "been a close friend for ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x108,
        (
            "#071FOhh, okay. Makes sense.\x02\x03",

            "I met her a long time ago, when a\x01",
            "case brought her to Calvard.\x02\x03",

            "She was fortunate to have a good\x01",
            "master working with her from such\x01",
            "a young age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        "#008F(Her master...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        "#019F(Yeah, probably Dad.)\x02",
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0xC, -80290, 0, 50310, 0)
    SetChrFlags(0xC, 0x80)

    def lambda_4DF2():
        OP_6D(-80130, 0, 59550, 1500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_4DF2)

    def lambda_4E0A():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E0A)

    def lambda_4E18():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4E18)

    def lambda_4E26():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E26)
    OP_22(0x6, 0x0, 0x64)
    ClearChrFlags(0xC, 0x80)
    OP_8E(0xC, 0xFFFEC5E6, 0x0, 0xD1B0, 0x7D0, 0x0)
    WaitChrThread(0x108, 0x2)

    ChrTalk(    #146
        0xC,
        (
            "#2P...Please, pardon me. The table\x01",
            "for the dinner party has been set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xC,
        "#2PMay I show you the way?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x108,
        (
            "#070F#6PSure. I was getting bored\x01",
            "with waiting anyhow.\x02\x03",

            "#071FAll right...\x01",
            "Wanna go and eat fancy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#006F#6PSure.\x01",
            "That fight left me starving.\x02\x03",

            "#001FLet's go dig in! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x102, 45, 400)

    ChrTalk(    #150
        0x102,
        (
            "#019F#6PCome on, you two...\x02\x03",

            "It would be nice if you two\x01",
            "didn't completely forget your\x01",
            "table manners for once...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4251   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_4562 end

    def Function_15_501E(): pass

    label("Function_15_501E")

    EventBegin(0x0)
    RemoveParty(0x7, 0xFF)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0xD, 6)
    OP_4A(0xD, 255)
    SetChrPos(0xD, -80180, 0, 61190, 180)
    SetChrPos(0x101, -79740, 0, 59790, 0)
    SetChrPos(0x102, -80740, 0, 59720, 0)
    OP_6D(-80100, 0, 60780, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #151
        0xD,
        (
            "#070FMan, I've heard some pretty unbelievable\x01",
            "conversations in my time, but that was\x01",
            "something else.\x02\x03",

            "I mean, I'm a foreigner, after all, so it's\x01",
            "not that big of a deal for me. I bet that\x01",
            "was huge news for you guys, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#005FO-Of course it was!\x02\x03",

            "I can't believe things have\x01",
            "gone this far already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xD,
        "#073FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#506FErr...n-never mind.\x02\x03",

            "#505FBut really...what a shame.\x02\x03",

            "That food was so amazing, and it practically\x01",
            "melted in the mouth... Couldn't tell what\x01",
            "that last flavor was, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #155
        0x102,
        (
            "#019FHa ha... Understandable enough.\x02\x03",

            "#010FBut anyway... Did you want to go\x01",
            "for a walk to work off some of\x01",
            "that rich food, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #156
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #157
        0x101,
        (
            "#006FOh! Yeah, sure!\x02\x03",

            "Yeah, I could go for a little\x01",
            "bit of fresh air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xD,
        (
            "#073F*sigh* You just played tourist a\x01",
            "little while ago, and now you want\x01",
            "to take an after-dinner walk...?\x02\x03",

            "#075FI sure don't get it.\x01",
            "Must be a local thing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #159
        0x101,
        (
            "#001FHa ha... I think you're exaggerating\x01",
            "a little bit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(    #160
        0x102,
        (
            "#010FYou haven't gone out to\x01",
            "take in the sights?\x02\x03",

            "There is a lot of historic architecture\x01",
            "around here, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        (
            "#070FIf the mood hits me, I may\x01",
            "still give it a shot.\x02\x03",

            "On the other hand, the kitchen may\x01",
            "still have some food left over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#509FYou've gotta be kidding.\x01",
            "You're still hungry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xD,
        (
            "#071FIf you had a blade to my throat,\x01",
            "my dying wish would be for some\x01",
            "liquor and a snack.\x02\x03",

            "I might go and hunt up a bar\x01",
            "or something in a little bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x4, 0x2)
    OP_28(0x4A, 0x4, 0x4)
    OP_28(0x4A, 0x1, 0x1)
    OP_28(0x4A, 0x1, 0x2)
    OP_28(0x4A, 0x1, 0x4)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    Return()

    # Function_15_501E end

    def Function_16_5696(): pass

    label("Function_16_5696")

    EventBegin(0x0)
    OP_6D(-79060, 0, 5600, 0)
    RemoveParty(0x7, 0xFF)
    SetChrPos(0x101, -79060, 0, 9840, 0)
    SetChrPos(0x102, -79060, 0, 9840, 0)
    OP_6F(0x1D, 60)

    def lambda_56DB():
        OP_8E(0xFE, 0xFFFECB2C, 0x0, 0x157C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56DB)
    Sleep(600)

    def lambda_56FB():
        OP_8E(0xFE, 0xFFFECB2C, 0x0, 0x1900, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56FB)
    WaitChrThread(0x101, 0x1)

    def lambda_571B():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_571B)
    WaitChrThread(0x102, 0x1)

    def lambda_572E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_572E)
    OP_72(0x1D, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1D, 0x0)
    OP_73(0x1D)
    OP_71(0x1D, 0x800)

    ChrTalk(    #164
        0x101,
        (
            "#007F#4P*sigh*\x01",
            "Things have gotten serious.\x02\x03",

            "We really have to find a way to\x01",
            "get in to see Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x102,
        (
            "#012FFirst things first: We go talk to the\x01",
            "head maid, Hilda, like we promised.\x02\x03",

            "She probably knows a way for us\x01",
            "to speak directly to the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#006F#4PFine by me.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_5696 end

    def Function_17_586C(): pass

    label("Function_17_586C")

    EventBegin(0x0)
    OP_6D(-79390, 0, 54420, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(1680, 0)
    OP_6C(38000, 0)
    OP_6E(509, 0)
    SetChrPos(0x101, -80040, 0, 48610, 0)
    SetChrPos(0x102, -80040, 0, 48610, 0)
    SetChrPos(0x108, -80040, 0, 48610, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1500, 0)

    def lambda_590E():
        OP_6D(-79660, 0, 55810, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_590E)

    def lambda_5926():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_5926)

    def lambda_5938():
        OP_8E(0xFE, 0xFFFEC762, 0x0, 0xDA52, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_5938)
    Sleep(800)

    def lambda_5958():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5958)

    def lambda_596A():
        OP_8E(0xFE, 0xFFFEC640, 0x0, 0xD426, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_596A)
    Sleep(500)

    def lambda_598A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_598A)

    def lambda_599C():
        OP_8E(0xFE, 0xFFFECAC8, 0x0, 0xD3CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_599C)
    WaitChrThread(0x108, 0x1)
    OP_8C(0x108, 180, 400)

    ChrTalk(    #167
        0x108,
        (
            "#074F#6P*sigh*...\x02\x03",

            "Looks like we managed to convince her,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #168
        0x101,
        (
            "#004F#6PWha...!\x02\x03",

            "Zin, aren't you drunk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x108,
        (
            "#070F#6PI was ACTING drunk...\x02\x03",

            "I haven't had a single drop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#009F#6PNo way! Your face had\x01",
            "even gone all red...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        (
            "#015FHe focused on making his blood \x01",
            "circulate better, which made it\x01",
            "look like he was intoxicated...\x02\x03",

            "#010FIt's done with some kind of \x01",
            "Eastern martial arts breathing\x01",
            "exercise, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x108,
        (
            "#073F#6PHuh! I'm surprised you're\x01",
            "familiar with it.\x02\x03",

            "#071FBut hey, you seemed to be in a\x01",
            "tight spot, so I figured I'd\x01",
            "distract everyone.\x02\x03",

            "Nice, huh? Saved your bacon,\x01",
            "as the saying goes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#007F#6PHmph...\x01",
            "You are an evil, evil man, Zin.\x02\x03",

            "#509FOkay, sure, you did help us out,\x01",
            "but you also surprised the hell\x01",
            "out of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x108,
        (
            "#071F#6PHa ha... Sorry about that.\x02\x03",

            "#070FSo, what's the story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#505F#6P???\x02\x03",

            "What story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x108,
        (
            "#070F#6PI would've thought it'd be obvious.\x02\x03",

            "The 'story' of you meeting\x01",
            "with the queen.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #177
        0x101,
        "#005F#3S#6PWhoa, wait, WHAT?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#580F#6PH-H-How did you--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        (
            "#014FDid Elnan tell you something\x01",
            "about this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x108,
        (
            "#070F#6PActually, I couldn't get him\x01",
            "to tell me anything.\x02\x03",

            "#071FBut now I know anyway,\x01",
            "don't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#509F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        (
            "#015FWithout prior knowledge, there's no\x01",
            "way you could have just guessed...\x02\x03",

            "#012FSo how much do you really know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x108,
        (
            "#074F#6PHa ha...\x02\x03",

            "I guess it's finally time to\x01",
            "show you this.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x108, 0x101, 0x320, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #184
        "\x07\x05Zin produced a letter from his pocket and handed it to Estelle and Joshua.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x108, 0xFFFEC762, 0x0, 0xDA52, 0x7D0, 0x0)

    ChrTalk(    #185
        0x101,
        "#004F#6PWhat's this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x102,
        "#014FI know this handwriting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x108,
        (
            "#070F#6PWell, don't just stand there.\x01",
            "Read it.\x02\x03",

            "It'll explain a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        "#505F#6PO-Okay...\x02",
    )

    CloseMessageWindow()
    OP_1F(0x50, 0x1F4)
    FadeToDark(300, 0, 100)
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #189
        (
            "\x07\x05'Dear Zin Vathek,\x01",
            "I hope this letter finds you well.\x01",
            "I know I've been out of touch.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #190
        (
            "\x07\x05'I'm in a hurry, so I hope you'll\x01",
            "pardon my bluntness.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #191
        (
            "\x07\x05'My work concerning the jaegers\x01",
            "is leading me into Imperial territory.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #192
        (
            "\x07\x05'However, due to the fact that unusual forces\x01",
            "seem to be influencing matters inside Liberl,\x01",
            "I feel uneasy being absent for so long.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #193
        "\x07\x05'This is why I must ask a favor of you.'\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #194
        (
            "\x07\x05'Could I persuade you to come to Liberl\x01",
            "and help out, if they need it?'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #195
        (
            "\x07\x05'Since you haven't been to Liberl before, perhaps\x01",
            "you could think of it as recreational trip.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #196
        (
            "\x07\x05'There is a Martial Arts Competition before the\x01",
            "Queen's Birthday Celebration, and foreigners\x01",
            "can participate. It would make fine camouflage.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #197
        (
            "\x07\x05'I realize that this is sudden, but if you can\x01",
            "do it, I would be most grateful.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #198
        (
            "\x07\x05'I'm intending to return to Liberl before the\x01",
            "festival, so hopefully we'll be able to have\x01",
            "a drink together when I return.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #199
        "\x07\x05                 ' -Cassius Bright '\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #200
        (
            "\x07\x05'P.S. You may have the chance to meet\x01",
            "my son and daughter!'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #201
        (
            "\x07\x05'They're currently apprentices at the guild,\x01",
            "so if you happen to meet them, feel free to\x01",
            "test the extent of their training.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #202
        (
            "\x07\x05'Try not to bail them out too much, unless it\x01",
            "seems like they really need it.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_1F(0x64, 0x1F4)
    Sleep(500)

    ChrTalk(    #203
        0x101,
        "#580F#6PI...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x102,
        (
            "#015FSo, Dad actually asked you to\x01",
            "come to Liberl...\x02\x03",

            "#010FWhich means he's in Erebonia now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x108,
        "#074F#6PThat's the long and short of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#509F#6P'The long and short of it'...?\x02\x03",

            "What it means is that you were\x01",
            "in cahoots with him all along!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x108,
        (
            "#070F#6PThat's kind of a nasty way to\x01",
            "put it, don't you think?\x02\x03",

            "I owed Master Cassius a favor, from\x01",
            "the time he spent in Calvard.\x02\x03",

            "This letter just gave me the\x01",
            "chance to make us square again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        "#007F#6PI suppose...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        (
            "#010FWhen did you realize that\x01",
            "we were his kids?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x108,
        (
            "#070F#6PI had a feeling from the outset, \x01",
            "once I saw Estelle's techniques\x01",
            "with a bo staff.\x02\x03",

            "I asked Kilika about it,\x01",
            "and that confirmed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        (
            "#009F#6PIt would have been nice if you'd\x01",
            "said something about it at ALL...\x02\x03",

            "We've been worried sick,\x01",
            "wondering where Dad's been.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x108,
        (
            "#075F#6PI know, and I'm sorry I haven't\x01",
            "said anything.\x02\x03",

            "But I got the impression from the\x01",
            "letter that he was trying to keep\x01",
            "his whereabouts a secret.\x02\x03",

            "#070FStill, you're definitely his kids, all right,\x01",
            "if you can pull off a job as big as sneaking an\x01",
            "audience with the queen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#004F#6PI-I suppose so...\x02\x03",

            "#006F...He knows this much, it wouldn't hurt to tell\x01",
            "him everything, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x102,
        (
            "#010FI agree, it'd probably be best to fill Zin in\x01",
            "on everything.\x02\x03",

            "It is a bit far-fetched to say that\x01",
            "we could put an end to this whole\x01",
            "situation on our own, after all.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #215
        (
            "\x07\x05Estelle and Joshua told of how they had managed to speak directly with the\x01",
            "queen...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #216
        "\x07\x05...as well as the queen's request to safely rescue Princess Klaudia.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #217
        0x108,
        (
            "#074F#6PI see...\x02\x03",

            "I thought something seemed a\x01",
            "little 'off' when everyone was\x01",
            "talking at the party...\x02\x03",

            "#070FAll right, then. I'll help you\x01",
            "out with that little request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        "#004F#6PWha... You will?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x108,
        (
            "#070F#6PYep. I think this is the ideal\x01",
            "opportunity to settle my debt\x01",
            "to Master Cassius.\x02\x03",

            "Please, let me help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#008F#6PWe... We'd be glad to!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x102,
        "#010FThank you, once again.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FA)
    ClearMapFlags(0x800)
    NewScene("ED6_DT01/C4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_586C end

    SaveToFile()

Try(main)
