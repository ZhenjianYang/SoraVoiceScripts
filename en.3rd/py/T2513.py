from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2513   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2513.x',
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
        'Clara',                                # 9
        'Rhody',                                # 10
        'Lechter',                              # 11
        'Book',                                 # 12
        'Jill',                                 # 13
        'Mickey',                               # 14
        'Mickey',                               # 15
        'Rigel',                                # 16
        'Anton',                                # 17
        'Target Camera',                        # 18
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
        'ED6_DT07/CH01090 ._CH',             # 00
        'ED6_DT07/CH01360 ._CH',             # 01
        'ED6_DT07/CH02670 ._CH',             # 02
        'ED6_DT06/CH20021 ._CH',             # 03
        'ED6_DT07/CH02390 ._CH',             # 04
        'ED6_DT07/CH01080 ._CH',             # 05
        'ED6_DT07/CH02910 ._CH',             # 06
        'ED6_DT07/CH02910 ._CH',             # 07
        'ED6_DT07/CH02900 ._CH',             # 08
        'ED6_DT26/CH20778 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01090P._CP',             # 00
        'ED6_DT07/CH01360P._CP',             # 01
        'ED6_DT07/CH02670P._CP',             # 02
        'ED6_DT06/CH20021P._CP',             # 03
        'ED6_DT07/CH02390P._CP',             # 04
        'ED6_DT07/CH01080P._CP',             # 05
        'ED6_DT07/CH02910P._CP',             # 06
        'ED6_DT07/CH02910P._CP',             # 07
        'ED6_DT07/CH02900P._CP',             # 08
        'ED6_DT26/CH20778P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C7,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0xFC,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2330,
        Z                   = 0,
        Y                   = 4680,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 56700,
        Z                   = 1000,
        Y                   = 19000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 6330,
        Y                   = 4000,
        Z                   = -1250,
        Range               = 9800,
        Unknown_10          = 0x1B58,
        Unknown_14          = 0xA0,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_3A2",          # 01, 1
        "Function_2_3E6",          # 02, 2
        "Function_3_563",          # 03, 3
        "Function_4_85D",          # 04, 4
        "Function_5_9D8",          # 05, 5
        "Function_6_A27",          # 06, 6
        "Function_7_B5E",          # 07, 7
        "Function_8_F34",          # 08, 8
        "Function_9_10BC",         # 09, 9
        "Function_10_10E3",        # 0A, 10
        "Function_11_1BE0",        # 0B, 11
        "Function_12_2712",        # 0C, 12
        "Function_13_2D12",        # 0D, 13
        "Function_14_2DA5",        # 0E, 14
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_346")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_END)), "loc_2A0")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -37060, 1000, 7700, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -35280, 1000, 7780, 270)

    label("loc_2A0")

    Jump("loc_346")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0x18, 0x80)
    Jump("loc_346")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_30E")
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 9)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 8600, 4200, 9370, 90)
    OP_62(0x12, 0x64, 1600, 0x18, 0x1B, 0x12C, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8160, 4400, 9200, 0)
    SetChrSubChip(0x13, 29)
    Jump("loc_346")

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_346")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -66600, 1000, 9600, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -65140, 1000, 9600, 270)
    ClearChrFlags(0x17, 0x80)

    label("loc_346")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_37B")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_369"),
        (107, "loc_369"),
        (SWITCH_DEFAULT, "loc_378"),
    )


    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375")
    Event(0, 14)

    label("loc_375")

    Jump("loc_378")

    label("loc_378")

    Jump("loc_3A1")

    label("loc_37B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3A1")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_392"),
        (106, "loc_392"),
        (SWITCH_DEFAULT, "loc_3A1"),
    )


    label("loc_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E")
    Event(0, 9)

    label("loc_39E")

    Jump("loc_3A1")

    label("loc_3A1")

    Return()

    # Function_0_25A end

    def Function_1_3A2(): pass

    label("Function_1_3A2")

    OP_B1("t2513_n")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E5")
    OP_B2(0x1, 0x0, 0x80)
    OP_62(0x12, 0x64, 1600, 0x18, 0x1B, 0x12C, 0x0)

    label("loc_3E5")

    Return()

    # Function_1_3A2 end

    def Function_2_3E6(): pass

    label("Function_2_3E6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_54D")

    label("loc_40B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_54D")

    label("loc_424")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_54D")

    label("loc_43D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_456")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_54D")

    label("loc_456")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46F")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_54D")

    label("loc_46F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_488")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_54D")

    label("loc_488")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A1")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_54D")

    label("loc_4A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BA")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_54D")

    label("loc_4BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D3")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_54D")

    label("loc_4D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EC")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_54D")

    label("loc_4EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_505")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_54D")

    label("loc_505")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_54D")

    label("loc_51E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_54D")

    label("loc_537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_54D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_562")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_54D")

    label("loc_562")

    Return()

    # Function_2_3E6 end

    def Function_3_563(): pass

    label("Function_3_563")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_570")
    Jump("loc_859")

    label("loc_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_57A")
    Jump("loc_859")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_584")
    Jump("loc_859")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_58E")
    Jump("loc_859")

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 6)), scpexpr(EXPR_END)), "loc_63F")

    ChrTalk(    #0
        0x17,
        (
            "It's about time for the other members of the\x01",
            "club to come in and start practice. \x02\x03",

            "So if you're at all interested in fencing, by all\x01",
            "means stay and watch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_859")

    label("loc_63F")


    ChrTalk(    #1
        0x17,
        "Oh, I recognize you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x17,
        (
            "You're the new first-year transfer student,\x01",
            "Kloe Rinz, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#044FYes, I am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x17,
        (
            "I'm Rigel, a third-year humanities student.\x01",
            "I also serve as the captain of the Fencing\x01",
            "Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x17,
        (
            "If you're at all interested in what we do,\x01",
            "you'd be welcome to stay and watch us\x01",
            "practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x105,
        (
            "#542F...I wish I could, but I'm afraid I'm a little too\x01",
            "busy at the moment. Thank you for your offer,\x01",
            "though.\x02\x03",

            "#543F(Hmm...)\x02\x03",

            "#048F(Heehee. Just the thought of joining reminds\x01",
            "me of my training sessions with Julia.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F7E)

    label("loc_859")

    TalkEnd(0xFE)
    Return()

    # Function_3_563 end

    def Function_4_85D(): pass

    label("Function_4_85D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_9AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_915")

    ChrTalk(    #7
        0xFE,
        (
            "I can't believe that guy is the\x01",
            "Student Council's president...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I think I'd be better at the job than him,\x01",
            "and I thought I was the biggest slacker\x01",
            "around!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AC")

    label("loc_915")


    ChrTalk(    #9
        0xFE,
        "I can't believe what I'm hearing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "THAT guy is the Student Council president?!\x01",
            "Seriously?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "There is something wrong with this world.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9AC")

    Jump("loc_9D4")

    label("loc_9AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_9B9")
    Jump("loc_9D4")

    label("loc_9B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_9C3")
    Jump("loc_9D4")

    label("loc_9C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_9CD")
    Jump("loc_9D4")

    label("loc_9CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_9D4")

    label("loc_9D4")

    TalkEnd(0xFE)
    Return()

    # Function_4_85D end

    def Function_5_9D8(): pass

    label("Function_5_9D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_A23")

    ChrTalk(    #12
        0xFE,
        (
            "I'm going to be born again as a new man. \x01",
            "Yes! Yes, I will!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A23")

    TalkEnd(0xFE)
    Return()

    # Function_5_9D8 end

    def Function_6_A27(): pass

    label("Function_6_A27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_B5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_AA6")

    ChrTalk(    #13
        0xFE,
        "Monika sure is taking her time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I wonder if she's still busy getting changed\x01",
            "into her uniform.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5A")

    label("loc_AA6")


    ChrTalk(    #15
        0xFE,
        (
            "Oh! Did you decide to stay and watch\x01",
            "club practice after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "You'll be more than welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "We've got another member coming soon,\x01",
            "though, so just sit tight, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_B5A")

    TalkEnd(0xFE)
    Return()

    # Function_6_A27 end

    def Function_7_B5E(): pass

    label("Function_7_B5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 2)), scpexpr(EXPR_END)), "loc_CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C17")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #18
        0x14,
        (
            "#646FListen to what I'm saying, Mickey.\x02\x03",

            "It's because you're always focused on nothing\x01",
            "but slacking that this happened to you in the\x01",
            "first place!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDC")

    label("loc_C17")


    ChrTalk(    #19
        0x14,
        (
            "#644FI'm gonna keep lecturing Mickey for a while\x01",
            "longer.\x02\x03",

            "#646FHis slacktitude always remind me of Lechter,\x01",
            "and anything that reminds me of him makes\x01",
            "me mad, mad, mad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x105,
        "#045FA-Ahaha...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_CDC")

    Jump("loc_F30")

    label("loc_CDF")

    OP_8C(0xFE, 90, 0)

    ChrTalk(    #21
        0x14,
        (
            "#646FListen to what I'm saying, Mickey.\x02\x03",

            "I should probably have told you this a long\x01",
            "time ago, but I'm going to take this golden\x01",
            "chance to give you a good lecturing now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x105,
        "#044FUmm... Jill?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #23
        0x14,
        (
            "#643FOh, Kloe.\x02\x03",

            "#1890FSorry, but I'm gonna stay and give Mickey\x01",
            "a good lecturing for a while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        (
            "#040FOh, that's all right. You can leave looking\x01",
            "for Lechter to me.\x02\x03",

            "I think I might have an idea where he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x14,
        (
            "#643FYou do?\x02\x03",

            "#644FAww, but why am I even surprised? You're like\x01",
            "a metal detector for Lechter at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x105,
        "#045FI-I wouldn't go quite that far.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F82)

    label("loc_F30")

    TalkEnd(0xFE)
    Return()

    # Function_7_B5E end

    def Function_8_F34(): pass

    label("Function_8_F34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_10B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1009")

    ChrTalk(    #27
        0xFE,
        (
            "As soon as Monika arrives, we're going to\x01",
            "be getting right to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "If you do want to stay and see what we get\x01",
            "up to, this is probably the perfect chance.\x01",
            "You'd be more than welcome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B8")

    label("loc_1009")


    ChrTalk(    #29
        0xFE,
        "You're not currently in any clubs, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "If you do want to stay and see what we get\x01",
            "up to, you'd be welcome to. This is probably\x01",
            "the perfect time to get a look!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_10B8")

    TalkEnd(0xFE)
    Return()

    # Function_8_F34 end

    def Function_9_10BC(): pass

    label("Function_9_10BC")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_10D4"),
        (106, "loc_10DB"),
        (SWITCH_DEFAULT, "loc_10E2"),
    )


    label("loc_10D4")

    Call(0, 10)
    Jump("loc_10E2")

    label("loc_10DB")

    Call(0, 11)
    Jump("loc_10E2")

    label("loc_10E2")

    Return()

    # Function_9_10BC end

    def Function_10_10E3(): pass

    label("Function_10_10E3")

    OP_6D(-65500, 1000, 7440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -66100, 0, 1500, 0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1142():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1142)

    def lambda_1154():
        OP_8E(0xFE, 0xFFFEFDCC, 0x0, 0xF28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1154)
    WaitChrThread(0x105, 0x1)

    def lambda_1174():
        OP_8E(0xFE, 0xFFFEF5FC, 0x0, 0xF28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1174)
    WaitChrThread(0x105, 0x1)

    def lambda_1194():
        OP_8E(0xFE, 0xFFFEF5FC, 0x3E8, 0x1D10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1194)
    WaitChrThread(0x105, 0x1)
    TurnDirection(0x105, 0x10, 500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x10, 255)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x11, 255)
    Sleep(500)

    ChrTalk(    #31
        0x10,
        "Is that you, Monika?\x02",
    )

    CloseMessageWindow()

    def lambda_120B():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_120B)
    Sleep(100)

    def lambda_121E():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_121E)
    Sleep(300)

    ChrTalk(    #32
        0x10,
        "Finally! We've been waiting for you, you know!\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x105,
        (
            "#044F#6PUmm... I... I...\x02\x03",

            "#043FSorry... I didn't mean to confuse you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "What? You didn't do anything wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        "I was the one who made a mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x105,
        (
            "#045F#6POh, I suppose you're right...\x02\x03",

            "#540FI-I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        "Like I said, I was the one who made a mistake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        "#11POookay, stop right there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        (
            "#11PDon't mind her, Kloe. She's kind of...slow on\x01",
            "the uptake at times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#11PDid you need something from us, though?\x01",
            "We're gonna start practice soon,\x01",
            "so we can't hang around and talk long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x105,
        (
            "#044F#6POh, I see...\x02\x03",

            "#047F(Still, I'm relatively sure that Clara is a\x01",
            "social studies student...)\x02\x03",

            "#049F(This doesn't really seem like the best\x01",
            "time to be intruding on them...)\x02\x03",

            "(Maybe it would be best for me to excuse\x01",
            "myself now and come back later?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x10,
        "Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "Oh, I know! You came to watch us practice \x01",
            "because you're thinking of joining the club,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "AWESOME! We'd be stoked to have you as\x01",
            "a member!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 500)

    ChrTalk(    #45
        0x11,
        (
            "#11PYou might want to let her speak before\x01",
            "busting out the confetti and streamers...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x105, 500)

    ChrTalk(    #46
        0x11,
        (
            "#11PSeriously, just ignore her, Kloe. If you don't,\x01",
            "we'll be here all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#11PWe really do need to start soon, though,\x01",
            "so can you make whatever you need quick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#044F#6POh, sure. Sorry...\x02\x03",

            "#045FUmm... W-Well, I just came to deliver this,\x01",
            "that's all...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17ED():
        OP_8E(0xFE, 0xFFFEF7F0, 0x3E8, 0x2148, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_17ED)
    WaitChrThread(0x105, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        "\x07\x05Kloe handed Clara the printout.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #50
        0x10,
        (
            "Aww... This is all you were here for?\x01",
            "A credits list?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "I got my hopes up for nothing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        "Booooo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x105,
        (
            "#540F#6PI-I'm sorry about that.\x02\x03",

            "#543FBut yes, that was all I wanted, so I'll let\x01",
            "you go ahead and start practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        "O-Oh, thanks...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)

    def lambda_1955():

        label("loc_1955")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1955")

    QueueWorkItem2(0x10, 2, lambda_1955)

    def lambda_1966():

        label("loc_1966")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1966")

    QueueWorkItem2(0x11, 2, lambda_1966)

    def lambda_1977():
        OP_8E(0xFE, 0xFFFEF5FC, 0x3E8, 0x1EF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1977)
    WaitChrThread(0x105, 0x1)

    def lambda_1997():
        OP_8E(0xFE, 0xFFFEF5FC, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1997)
    WaitChrThread(0x105, 0x1)

    def lambda_19B7():
        OP_8E(0xFE, 0xFFFEFDCC, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_19B7)
    WaitChrThread(0x105, 0x1)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x105, 180, 500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_1A0C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1A0C)

    def lambda_1A1E():
        OP_8E(0xFE, 0xFFFEFDCC, 0x3E8, 0x5DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A1E)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(2000)
    OP_63(0x10)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #55
        0x10,
        "She's kinda weird, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        (
            "#5PShe's the mysterious transfer student everyone is \x01",
            "talking about. You wouldn't expect her to be TOO\x01",
            "normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "Ohhh... That's her, huh?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #58
        0x10,
        "I wish she'd stayed and joined the club.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-7000, 0, 11400, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -7000, 0, 11400, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_69(0x105, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F69)
    EventEnd(0x0)
    Return()

    # Function_10_10E3 end

    def Function_11_1BE0(): pass

    label("Function_11_1BE0")

    OP_6D(-64239, 1000, 8800, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -59740, 1000, 7660, 270)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x10, 255)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x11, 255)
    Sleep(500)

    ChrTalk(    #59
        0x10,
        "#6PIs that you, Monika?\x02",
    )

    CloseMessageWindow()

    def lambda_1C97():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1C97)
    Sleep(100)

    def lambda_1CAA():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1CAA)
    Sleep(300)

    ChrTalk(    #60
        0x10,
        "#6PFinally! We've been waiting for you, you know!\x02",
    )

    CloseMessageWindow()

    def lambda_1CF4():

        label("loc_1CF4")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1CF4")

    QueueWorkItem2(0x10, 2, lambda_1CF4)

    def lambda_1D05():

        label("loc_1D05")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1D05")

    QueueWorkItem2(0x11, 2, lambda_1D05)

    def lambda_1D16():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1D16)

    def lambda_1D28():
        OP_8E(0xFE, 0xFFFF07CC, 0x3E8, 0x1DEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D28)
    WaitChrThread(0x105, 0x1)
    TurnDirection(0x105, 0x10, 500)
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x105,
        (
            "#044FUmm... I... I...\x02\x03",

            "#043FSorry... I didn't mean to confuse you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        "#1PWhat? You didn't do anything wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        "#1PI was the one who made a mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x105,
        (
            "#045FOh, I suppose you're right...\x02\x03",

            "#540FI-I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        "#1PLike I said, I was the one who made a mistake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x11,
        "#5POookay, stop right there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "#5PDon't mind her, Kloe. She's kind of...slow on\x01",
            "the uptake at times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x11,
        (
            "#5PDid you need something from us, though?\x01",
            "We're gonna start practice soon,\x01",
            "so we can't hang around and talk long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x105,
        (
            "#044FOh, I see...\x02\x03",

            "#047F(Still, I'm relatively sure that Clara is a\x01",
            "social studies student...)\x02\x03",

            "#049F(This doesn't really seem like the best\x01",
            "time to be intruding on them...)\x02\x03",

            "(Maybe it would be best for me to excuse\x01",
            "myself now and come back later?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x10,
        "#1PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        (
            "#1POh, I know! You came to watch us practice \x01",
            "because you're thinking of joining the club,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#1PAWESOME! We'd be stoked to have you as\x01",
            "a member!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 500)

    ChrTalk(    #73
        0x11,
        (
            "#11PYou might want to let her speak before\x01",
            "busting out the confetti and streamers...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x105, 500)

    ChrTalk(    #74
        0x11,
        (
            "#5PSeriously, just ignore her, Kloe. If you don't,\x01",
            "we'll be here all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "#5PWe really do need to start soon, though,\x01",
            "so can you make whatever you need quick?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x105,
        (
            "#044FOh, sure. Sorry...\x02\x03",

            "#045FUmm... W-Well, I just came to deliver this,\x01",
            "that's all...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22E0():

        label("loc_22E0")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_22E0")

    QueueWorkItem2(0x10, 2, lambda_22E0)

    def lambda_22F1():

        label("loc_22F1")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_22F1")

    QueueWorkItem2(0x11, 2, lambda_22F1)

    def lambda_2302():
        OP_8E(0xFE, 0xFFFEFBD8, 0x3E8, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2302)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x05Kloe handed Clara the printout.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #78
        0x10,
        (
            "#1PAww... This is all you were here for?\x01",
            "A credits list?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        "#1PI got my hopes up for nothing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        "#1PBooooo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x105,
        (
            "#540F#6PI-I'm sorry about that.\x02\x03",

            "#543FBut yes, that was all I wanted, so I'll let\x01",
            "you go ahead and start practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        "#1PO-Oh, thanks...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 250, 400)

    def lambda_2485():

        label("loc_2485")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_2485")

    QueueWorkItem2(0x10, 2, lambda_2485)

    def lambda_2496():

        label("loc_2496")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_2496")

    QueueWorkItem2(0x11, 2, lambda_2496)

    def lambda_24A7():
        OP_8E(0xFE, 0xFFFEF5FC, 0x3E8, 0x1EF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24A7)
    WaitChrThread(0x105, 0x1)

    def lambda_24C7():
        OP_8E(0xFE, 0xFFFEF5FC, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24C7)
    WaitChrThread(0x105, 0x1)

    def lambda_24E7():
        OP_8E(0xFE, 0xFFFEFDCC, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24E7)
    WaitChrThread(0x105, 0x1)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x105, 180, 500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_253C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_253C)

    def lambda_254E():
        OP_8E(0xFE, 0xFFFEFDCC, 0x3E8, 0x5DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_254E)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(2000)
    OP_63(0x10)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #83
        0x10,
        "#1PShe's kinda weird, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x11,
        (
            "#5PShe's the mysterious transfer student everyone is \x01",
            "talking about. You wouldn't expect her to be TOO\x01",
            "normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10,
        "#1POhhh... That's her, huh?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #86
        0x10,
        "#1PI wish she'd stayed and joined the club.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-7000, 0, 11400, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -7000, 0, 11400, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F69)
    EventEnd(0x0)
    Return()

    # Function_11_1BE0 end

    def Function_12_2712(): pass

    label("Function_12_2712")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    OP_8C(0x105, 0, 0)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2743():
        OP_6D(9440, 4000, 9740, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2743)

    def lambda_275B():
        OP_67(0, 4640, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_275B)

    def lambda_2773():
        OP_6B(3160, 2000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_2773)
    WaitChrThread(0x19, 0x0)
    SetChrPos(0x105, 8000, 4000, -3540, 0)
    SetChrPos(0x13B, 8500, 4000, -2140, 0)
    SetChrPos(0x152, 7700, 4000, -2500, 0)

    def lambda_27BB():
        OP_8E(0xFE, 0x1E14, 0xFA0, 0x1D4C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x152, 1, lambda_27BB)
    Sleep(300)

    def lambda_27DB():
        OP_8E(0xFE, 0x2134, 0xFA0, 0x1BE4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_27DB)
    Sleep(100)
    SetChrFlags(0x105, 0x1000)

    def lambda_2800():
        OP_8E(0xFE, 0x1F40, 0xFA0, 0x1554, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2800)
    WaitChrThread(0x13B, 0x1)
    Sleep(500)

    ChrTalk(    #87
        0x13B,
        "#649F#60W#12PWe've fouuuuuund youuuuuu.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #88
        0x13B,
        "#1891F#3S#12PYou're not getting away this time!#2S\x02",
    )

    OP_7C(0x32, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #89
        0x152,
        "#732F#6PIt's time to come quietly.\x02",
    )

    CloseMessageWindow()
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #90
        0x12,
        (
            "#1774F#5PHmm... Hmm...\x02\x03",

            "Hmm... Hmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x64, 1500, 0x18, 0x1B, 0x12C, 0x0)
    Sleep(2000)
    OP_62(0x13B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x152, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #91
        0x105,
        "#542F#12PUmm... What exactly is that you're reading?\x02",
    )

    CloseMessageWindow()
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #92
        0x12,
        (
            "#1772F#5PIt's 'Kitty-Talk for Dummies.'\x02\x03",

            "#1771FNya-go.\x02\x03",

            "Nnyan. ☆\x02\x03",

            "Unyanya～n. ♪\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x152, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x13B, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #93
        0x152,
        (
            "#734F#6PH-Have you been sitting here reading that all\x01",
            "this time?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x12, 0x64, 1500, 0x8, 0x9, 0xC8, 0x0)
    Sleep(1000)
    OP_62(0x13B, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x13B, 0x3, 0x0, 0xD)
    Sleep(2000)
    FadeToDark(2000, 0, -96)
    OP_A2(0x5)
    OP_0D()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #94
        (
            "\x18\x07\x0CI just closed my eyes and kept running forward\x01",
            "through a vast, empty world, living the hardest\x01",
            "that I could.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #95
        (
            "\x18\x07\x0CIt wasn't that running would achieve anything,\x01",
            "and it wasn't as if I would suddenly be able to\x01",
            "leave the ground and fly by doing so.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #96
        (
            "\x18\x07\x0CIt was just that if I stood still, the small, perfectly\x01",
            "enclosed garden around me would suddenly feel\x01",
            "too uncomfortably vast.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0x13B, 0xFF)
    SetChrName("")

    AnonymousTalk(    #97
        "\x18\x07\x0C#40WLechter was right.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #98
        "\x18\x07\x0C#40WJust what HAD I come here to do...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    RemoveParty(0x3A, 0x0)
    RemoveParty(0x51, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2712 end

    def Function_13_2D12(): pass

    label("Function_13_2D12")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DA4")

    def lambda_2D21():
        OP_8F(0xFE, 0x2134, 0xFA0, 0x21C0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_2D21)
    WaitChrThread(0x13B, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D48")
    OP_22(0x8E, 0x0, 0x32)

    label("loc_2D48")


    def lambda_2D4E():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2D4E)

    def lambda_2D68():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_2D68)

    def lambda_2D82():
        OP_8F(0xFE, 0x2134, 0xFA0, 0x1BE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_2D82)
    WaitChrThread(0x13B, 0x1)
    Sleep(500)
    Jump("Function_13_2D12")

    label("loc_2DA4")

    Return()

    # Function_13_2D12 end

    def Function_14_2DA5(): pass

    label("Function_14_2DA5")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    OP_6D(-34930, 0, 5630, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    SetChrPos(0x14, -36120, 0, 3440, 0)
    SetChrFlags(0x14, 0x40)
    SetChrPos(0x15, -35750, 0, 5500, 0)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x20)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x15, 0x100)
    OP_51(0x15, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0xAFC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x91), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -36120, -800, 4800, 0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_2ED0"),
        (107, "loc_2EE4"),
        (SWITCH_DEFAULT, "loc_2EF8"),
    )


    label("loc_2ED0")

    SetChrPos(0x105, -36140, 0, 1500, 0)
    Jump("loc_2EF8")

    label("loc_2EE4")

    SetChrPos(0x105, -40500, 1000, 6540, 90)
    Jump("loc_2EF8")

    label("loc_2EF8")

    OP_0D()
    Sleep(1000)

    ChrTalk(    #99
        0x14,
        (
            "#649F#12PHeeheehee. I've got you now, you sorry excuse\x01",
            "for a president!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F51():
        OP_8E(0xFE, 0xFFFF72E8, 0x0, 0xF00, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2F51)
    WaitChrThread(0x14, 0x1)
    Sleep(300)

    ChrTalk(    #100
        0x14,
        "#1891F#12P#3STime to accept your fate!#2S\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x14, 0x4)

    def lambda_2FAA():
        OP_8E(0xFE, 0xFFFF72E8, 0x0, 0x11F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2FAA)
    WaitChrThread(0x14, 0x1)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(300)

    def lambda_2FD4():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2FD4)
    Sleep(1000)

    def lambda_2FF3():
        OP_8F(0xFE, 0xFFFF72E8, 0x0, 0xD70, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2FF3)

    def lambda_300E():
        OP_8F(0xFE, 0xFFFF745A, 0x0, 0x10CC, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_300E)
    WaitChrThread(0x14, 0x1)
    Sleep(1000)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #101
        0x14,
        (
            "#642FMickey?\x02\x03",

            "#645F...Whaaat were you doing under there?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x16, -36120, -1000, 4800, 0)
    SetChrPos(0x15, -35750, 0, 4300, 225)
    SetChrFlags(0x15, 0x800)
    OP_0D()
    Sleep(300)
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #102
        0x16,
        "#1PL-Let go of me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x16,
        "#1PI wasn't doing anything!\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_313A"),
        (107, "loc_319A"),
        (SWITCH_DEFAULT, "loc_321A"),
    )


    label("loc_313A")

    OP_22(0x6, 0x0, 0x64)

    def lambda_3145():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3145)
    WaitChrThread(0x105, 0x2)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1300)

    ChrTalk(    #104
        0x105,
        "#044FWhat's going on here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_321A")

    label("loc_319A")


    def lambda_31A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_31A0)

    def lambda_31B2():
        OP_8E(0xFE, 0xFFFF6870, 0x3E8, 0x198C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_31B2)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 135, 400)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1300)

    ChrTalk(    #105
        0x105,
        "#044F#5PWhat's going on here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_321A")

    label("loc_321A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-34850, 1000, 10060, 0)
    OP_67(0, 4400, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x15, -35330, 1000, 8510, 270)
    SetChrFlags(0x15, 0x40)
    ClearChrFlags(0x15, 0x800)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x20)
    SetChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x100)
    SetChrFlags(0x16, 0x80)
    OP_51(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x105, -37090, 1000, 7760, 90)
    SetChrPos(0x14, -37220, 1000, 8900, 90)
    ClearChrFlags(0x14, 0x4)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #106
        0x15,
        (
            "#11PI keep telling you, I wasn't doing anything weird!\x01",
            "I swear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x14,
        (
            "#646F#6PThen what were you doing down there, huh?\x02\x03",

            "I'm sorry, but crawling under there screams\x01",
            "'suspicious.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x15,
        (
            "#11PTh-That's what I thought, too! That's why \x01",
            "I crawled in there!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #109
        0x14,
        "#643F#6P...I'm not following you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x105,
        "#044F#6PUmm... Can you elaborate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x15,
        "#11PWell, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x15,
        (
            "#11PI was around the back of the school building\x01",
            "when I saw this guy who looked like he rolled\x01",
            "right out of a dumpster walking around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x15,
        (
            "#11PI don't think I've ever seen anyone so sloppy\x01",
            "looking in my life.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x105,
        (
            "#045F#6P(It's scary how I know just from that\x01",
            "who he's talking about...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x14,
        "#645F#6P(Yeah. Me, too...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x15,
        (
            "#11PHonestly, he made me so curious I had to see\x01",
            "what he was up to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x15,
        "#11P...so I ended up following him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x15,
        (
            "#11PAnyway, he looked around for a while, then he\x01",
            "wandered here into the auditorium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x15,
        "#11PPretty suspicious, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x14,
        "#647F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x15,
        (
            "#11PIt was when I followed him in here that he\x01",
            "noticed me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x15,
        (
            "#11PThe second he saw me, he seemed to panic\x01",
            "a little before crawling under there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x15,
        (
            "#11PI tried to follow him, but I ended up getting\x01",
            "stuck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x15,
        "#11PI was SO close, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x14,
        "#645F#6P*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        (
            "#045F#6PUmm... So, in other words...\x02\x03",

            "...he was toying with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x15,
        "#11PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x14,
        (
            "#647F#6PMaybe if you bothered thinking about things\x01",
            "other than how best to skip class you wouldn't\x01",
            "fall for such obvious tricks.\x02\x03",

            "#649FHe was deliberately trying to get your attention\x01",
            "by acting suspicious as all get-out. Like, he was\x01",
            "trying to set you up.\x02\x03",

            "Call it our Student Council president's specialty.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #129
        0x15,
        "#11PWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x15,
        "#11PTHAT guy is the Student Council president?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x15,
        (
            "#11PYou've gotta be kidding... He couldn't look any\x01",
            "less the part!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x105,
        (
            "#045F#6PA-Ahaha...\x02\x03",

            "(He's preaching to the choir...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-37200, 1000, 6860, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0x15, 0x40)
    SetChrPos(0x105, -37090, 1000, 7760, 90)
    SetChrPos(0x14, -37220, 1000, 8900, 90)
    SetChrPos(0x15, -35330, 1000, 8510, 270)
    OP_69(0x0, 0x0)
    OP_A2(0x2F71)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_14_2DA5 end

    SaveToFile()

Try(main)
