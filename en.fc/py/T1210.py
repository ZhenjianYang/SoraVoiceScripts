from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1210   ._SN',
        MapName             = 'Bose',
        Location            = 'T1210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1210   ._SN',
            'ED6_DT01/T1210_1 ._SN',
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
        'Orange',                               # 9
        'Gray',                                 # 10
        'Elder Reisen',                         # 11
        'Birnette',                             # 12
        'Lewey',                                # 13
        'Figaro',                               # 14
        'Lore',                                 # 15
        'Pesca',                                # 16
        'Gray',                                 # 17
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
        'ED6_DT07/CH01010 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01490 ._CH',             # 02
        'ED6_DT07/CH01180 ._CH',             # 03
        'ED6_DT07/CH01470 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01123 ._CH',             # 06
        'ED6_DT07/CH01143 ._CH',             # 07
        'ED6_DT07/CH00003 ._CH',             # 08
        'ED6_DT07/CH00013 ._CH',             # 09
        'ED6_DT07/CH00023 ._CH',             # 0A
        'ED6_DT07/CH01003 ._CH',             # 0B
        'ED6_DT07/CH01493 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01010P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01490P._CP',             # 02
        'ED6_DT07/CH01180P._CP',             # 03
        'ED6_DT07/CH01470P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01123P._CP',             # 06
        'ED6_DT07/CH01143P._CP',             # 07
        'ED6_DT07/CH00003P._CP',             # 08
        'ED6_DT07/CH00013P._CP',             # 09
        'ED6_DT07/CH00023P._CP',             # 0A
        'ED6_DT07/CH01003P._CP',             # 0B
        'ED6_DT07/CH01493P._CP',             # 0C
    )

    DeclNpc(
        X                   = -31600,
        Z                   = 0,
        Y                   = 2900,
        Direction           = 270,
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
        X                   = -25500,
        Z                   = 0,
        Y                   = 8700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -1880,
        Z                   = 0,
        Y                   = 48500,
        Direction           = 0,
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
        X                   = 7500,
        Z                   = 0,
        Y                   = 46200,
        Direction           = 90,
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
        X                   = -1430,
        Z                   = 0,
        Y                   = 3310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 360,
        Z                   = 0,
        Y                   = 6440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4650,
        Z                   = 100,
        Y                   = 45830,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 3300,
        Z                   = 200,
        Y                   = 48070,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 3430,
        Z                   = 150,
        Y                   = 45650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    ScpFunction(
        "Function_0_232",          # 00, 0
        "Function_1_338",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_34F",          # 03, 3
        "Function_4_373",          # 04, 4
        "Function_5_C02",          # 05, 5
        "Function_6_D94",          # 06, 6
        "Function_7_22DC",         # 07, 7
        "Function_8_2B45",         # 08, 8
        "Function_9_2F2B",         # 09, 9
        "Function_10_36BE",        # 0A, 10
        "Function_11_3791",        # 0B, 11
        "Function_12_38FC",        # 0C, 12
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_27C")
    SetChrPos(0x9, 3300, -1000, 45700, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 6180, 0, 49500, 0)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_318")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2A1")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -780, 0, 5750, 0)
    Jump("loc_318")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2C6")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -780, 0, 5750, 0)
    Jump("loc_318")

    label("loc_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2E6")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -780, 0, 5750, 0)
    Jump("loc_318")

    label("loc_2E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_318")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -1820, 0, 47460, 0)
    SetChrPos(0xA, -1880, 0, 48500, 180)

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_329")
    SetChrFlags(0xA, 0x80)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_337")
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_337")

    Return()

    # Function_0_232 end

    def Function_1_338(): pass

    label("Function_1_338")

    Return()

    # Function_1_338 end

    def Function_2_339(): pass

    label("Function_2_339")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_339")

    label("loc_34E")

    Return()

    # Function_2_339 end

    def Function_3_34F(): pass

    label("Function_3_34F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_372")
    OP_8D(0xFE, -2590, 3920, 2730, 920, 1500)
    Jump("Function_3_34F")

    label("loc_372")

    Return()

    # Function_3_34F end

    def Function_4_373(): pass

    label("Function_4_373")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3F4")

    ChrTalk(    #0
        0xFE,
        "Are you here to buy some fruit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If you're looking for my husband, he's\x01",
            "over at the village elder's house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFE")

    label("loc_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_54F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F7")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "It might be a good time for him to\x01",
            "sit down and speak with the other\x01",
            "villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Then again, he's always been a stubborn\x01",
            "one, ever since his younger years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I hope there's someone who can be\x01",
            "a good mediator between them all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54C")

    label("loc_4F7")


    ChrTalk(    #5
        0xFE,
        (
            "It might be a good time for him to\x01",
            "sit down and speak with the other\x01",
            "villagers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C")

    Jump("loc_BFE")

    label("loc_54F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_6FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_650")
    OP_A2(0x0)

    ChrTalk(    #6
        0xFE,
        (
            "It looks like the army came back and\x01",
            "was looking for something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "These new soldiers are a lot more\x01",
            "energetic about their work than\x01",
            "the last ones who came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I'm sure that probably has something\x01",
            "to do with their leader.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F9")

    label("loc_650")


    ChrTalk(    #9
        0xFE,
        (
            "It looks like the army came back and\x01",
            "was looking for something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "These new soldiers are a lot more\x01",
            "energetic about their work than\x01",
            "the last ones who came.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F9")

    Jump("loc_BFE")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_84F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F4")
    OP_A2(0x0)

    ChrTalk(    #11
        0xFE,
        (
            "I don't think my husband is\x01",
            "wrong in his opinions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Because the fact is, he grows the\x01",
            "most delicious fruit in the entire\x01",
            "village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "That said, I don't think it would\x01",
            "hurt to try accepting new ways\x01",
            "of growing fruit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84C")

    label("loc_7F4")


    ChrTalk(    #14
        0xFE,
        (
            "That said, I don't think it would\x01",
            "hurt to try accepting new ways\x01",
            "of growing fruit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84C")

    Jump("loc_BFE")

    label("loc_84F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_9F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95D")
    OP_A2(0x0)

    ChrTalk(    #15
        0xFE,
        (
            "My husband is as stiff as a board\x01",
            "and stuck in his ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "In fact, he may just be stuck in his\x01",
            "old ways until the day he dies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "It seems like recently my husband\x01",
            "has had a difference of opinion with\x01",
            "one of the young men in the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9ED")

    label("loc_95D")


    ChrTalk(    #18
        0xFE,
        (
            "My husband is as stiff as a board\x01",
            "and stuck in his ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I hope he doesn't get on the bad\x01",
            "side of all the young people\x01",
            "because of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9ED")

    Jump("loc_BFE")

    label("loc_9F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_B4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABF")
    OP_A2(0x0)

    ChrTalk(    #20
        0xFE,
        (
            "If you're looking for my husband,\x01",
            "he's always in the orchard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Even when I call him for meals,\x01",
            "he ends up coming an hour later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "And by that time, his meal is\x01",
            "already cold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B48")

    label("loc_ABF")


    ChrTalk(    #23
        0xFE,
        (
            "If you're looking for my husband,\x01",
            "he's always in the orchard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Even when I call him for meals,\x01",
            "he ends up coming an hour later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B48")

    Jump("loc_BFE")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_BFE")

    ChrTalk(    #25
        0xFE,
        (
            "So let me guess, are you here\x01",
            "to buy fruit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I'm sorry to say this, but my husband\x01",
            "is outside. If you need to speak with him,\x01",
            "would you mind going to the orchard?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFE")

    TalkEnd(0x8)
    Return()

    # Function_4_373 end

    def Function_5_C02(): pass

    label("Function_5_C02")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_C6F")

    ChrTalk(    #27
        0xFE,
        (
            "I want to grow delicious fruit in\x01",
            "my own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I can't agree with the use of\x01",
            "machines.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D90")

    label("loc_C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_CDC")

    ChrTalk(    #29
        0xFE,
        (
            "I'm going to have to keep my eye on\x01",
            "these young upstarts and their ways\x01",
            "of cultivating fruit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D90")

    label("loc_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_D90")

    ChrTalk(    #30
        0xFE,
        (
            "Raising fruit naturally on trees one\x01",
            "by one is the best way as far as\x01",
            "I'm concerned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "And it's because I take so much care\x01",
            "and time that the fruit is so delicious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D90")

    TalkEnd(0x9)
    Return()

    # Function_5_C02 end

    def Function_6_D94(): pass

    label("Function_6_D94")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_DE0")

    ChrTalk(    #32
        0xFE,
        (
            "Goodness, we can't seem to get\x01",
            "anywhere with these talks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D8")

    label("loc_DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB4")
    OP_A2(0x2)

    ChrTalk(    #33
        0xFE,
        (
            "This village may seem peaceful at\x01",
            "first glance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "But we're actually dealing with a\x01",
            "number of problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Well, I guess the only thing we\x01",
            "can do is deal with them one at\x01",
            "a time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F26")

    label("loc_EB4")


    ChrTalk(    #36
        0xFE,
        (
            "This village may seem peaceful at\x01",
            "first glance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "But we're actually dealing with a\x01",
            "number of problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F26")

    Jump("loc_22D8")

    label("loc_F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_106A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAF")
    OP_A2(0x2)

    ChrTalk(    #38
        0xFE,
        "Oh, you bracers are back...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I was really worried after I saw\x01",
            "you all being led away by the\x01",
            "Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1067")

    label("loc_FAF")


    ChrTalk(    #40
        0xFE,
        (
            "It's almost unbelievable to think that\x01",
            "the airliner was hidden there in the\x01",
            "mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "The army is now watching the place\x01",
            "in the event that the sky bandits\x01",
            "decide to come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1067")

    Jump("loc_22D8")

    label("loc_106A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_10EC")
    OP_4A(0xFE, 255)

    ChrTalk(    #42
        0xFE,
        (
            "I hope you manage to find what\x01",
            "you're looking for in the mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Please let me know if you find\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D8")

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_11F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A7")
    OP_A2(0x2)

    ChrTalk(    #44
        0xFE,
        (
            "The silhouette that Lewey saw\x01",
            "flying in the sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "I wonder if it could be 'him'...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "No, it couldn't be... It's been\x01",
            "decades since anyone last saw\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11EF")

    label("loc_11A7")


    ChrTalk(    #47
        0xFE,
        (
            "No, it couldn't be... It's been\x01",
            "decades since anyone last saw\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EF")

    Jump("loc_22D8")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1DFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D67")
    OP_A2(0x31B)
    OP_28(0x36, 0x1, 0x4)
    EventBegin(0x0)
    OP_69(0xFE, 0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1600")

    ChrTalk(    #48
        0xFE,
        "I see you're all together.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "What brings you all up here today?\x01",
            "Are you here for a visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#020FNo, not exactly. We're actually here\x01",
            "on business.\x02\x03",

            "Although, if it's possible, I'd really\x01",
            "like a glass of your fruit wine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Ho ho ho. Things in the world never\x01",
            "go like you expect, do they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "By the way, I never got a chance to\x01",
            "ask you until now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "You don't happen to be one of\x01",
            "Agate's companions, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        (
            "#020FWell, we're all members of the same\x01",
            "guild, but we're not companions\x01",
            "exactly.\x02\x03",

            "We know him by face, and that's\x01",
            "probably about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "So he's traveling by himself as\x01",
            "usual, huh?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #57
        (
            "\x07\x05The village elder closed his eyes for a moment as a look of sadness passed\x01",
            "over his aged features.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #58
        0x101,
        (
            "#501F???\x02\x03",

            "What's wrong, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "It's nothing, really. Please pardon\x01",
            "my expression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Anyway, what brings you to this\x01",
            "rural village of ours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Don't tell me that another dangerous monster\x01",
            "showed up in the area.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1977")

    label("loc_1600")


    ChrTalk(    #62
        0xFE,
        (
            "I haven't seen the likes of you\x01",
            "around here before. So tell me, are\x01",
            "you here to buy some fruit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#020FNo, we're not merchants. We're here\x01",
            "with the Bracer Guild.\x02\x03",

            "So are you the elder of this village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "I guess you could say I'm\x01",
            "something like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "You don't happen to be one of\x01",
            "Agate's companions, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#020FWell, we're all members of the same\x01",
            "guild, but we're not companions\x01",
            "exactly.\x02\x03",

            "We know him by face, and that's\x01",
            "probably about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "So he's traveling by himself as\x01",
            "usual, huh?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #69
        (
            "\x07\x05The village elder closed his eyes for a moment\x01",
            "as a look of sadness passed over his aged\x01",
            "features.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #70
        0x101,
        (
            "#501F???\x02\x03",

            "What's wrong, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "It's nothing, really. Please pardon\x01",
            "my expression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Anyway, what brings you to this\x01",
            "rural village of ours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Don't tell me that another dangerous monster\x01",
            "showed up in the area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1977")


    ChrTalk(    #74
        0x102,
        (
            "#010FNo, actually we're in the middle of\x01",
            "an investigation concerning the\x01",
            "missing airliner.\x02\x03",

            "We came here because we heard\x01",
            "there was a report of some kind\x01",
            "of sighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Ah, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "The Royal Army came here and\x01",
            "investigated that the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "However, they searched around the area\x01",
            "and ended up leaving empty-handed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#000FReally, is that so...?\x02\x03",

            "Well, what about the person who saw\x01",
            "the flying silhouette in the sky?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "It was one of the children in the\x01",
            "village here. A boy named Lewey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "He apparently saw some suspicious\x01",
            "shadow making its way across the\x01",
            "sky on the night of the incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "But he's a kid any way you think about it,\x01",
            "so he may have just imagined the whole\x01",
            "thing while he was half-asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#002FImagined it, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#010FI guess the best thing we can do\x01",
            "then is ask him directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#006FYou're probably right about\x01",
            "that.\x02\x03",

            "Thank you for your time, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Don't mention it. If there's anything else\x01",
            "I can help you with, don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_1DF9")

    label("loc_1D67")


    ChrTalk(    #86
        0xFE,
        (
            "Lewey should be here somewhere\x01",
            "in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "The village is rather small, so I'm sure\x01",
            "you'll be able to find him without any\x01",
            "trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF9")

    Jump("loc_22D8")

    label("loc_1DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_22D8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E1D")
    Call(1, 0)
    Jump("loc_22D8")

    label("loc_1E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200E")
    OP_28(0xE, 0x1, 0x800)
    OP_A2(0x3)

    ChrTalk(    #88
        0xFE,
        (
            "Oh, it's you young bracers again, is it?\x01",
            "I've heard the news!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "You exterminated that monster on\x01",
            "the trail behind the village, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#000FYes, we did it somehow, I guess.\x01",
            "It was pretty tough in the end.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #91
        0xFE,
        (
            "Now it looks like we'll be able to\x01",
            "plant our saplings this year without\x01",
            "any more worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "I'm really grateful to you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "We may not have much to offer,\x01",
            "but please know you're always\x01",
            "welcome here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#001FWe appreciate that, sir.\x02",
    )

    CloseMessageWindow()
    Jump("loc_22D8")

    label("loc_200E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_208D")

    ChrTalk(    #95
        0xFE,
        "I'm really grateful to you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "We may not have much to offer,\x01",
            "but please know you're always\x01",
            "welcome here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D8")

    label("loc_208D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2220")
    OP_A2(0x2)

    ChrTalk(    #97
        0xFE,
        (
            "Oh, it's you young bracers again,\x01",
            "is it? Thank you for exterminating\x01",
            "the monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "Please make yourself at home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "You probably can't imagine it from\x01",
            "the way the village looks now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "But we suffered an incredible amount\x01",
            "of damage in the war 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "When I think about the aftermath of the\x01",
            "war, it's amazing that we were able to\x01",
            "rebuild this town to what it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D8")

    label("loc_2220")


    ChrTalk(    #102
        0xFE,
        (
            "When I think about the aftermath of the\x01",
            "war, it's amazing that we were able to\x01",
            "rebuild this town to what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "This is because of the hard work\x01",
            "and effort of the villagers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D8")

    TalkEnd(0xA)
    Return()

    # Function_6_D94 end

    def Function_7_22DC(): pass

    label("Function_7_22DC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_23AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2360")
    OP_A2(0x4)

    ChrTalk(    #104
        0xFE,
        "The village meeting is over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Things always end up like this\x01",
            "whenever those two come\x01",
            "face-to-face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23AA")

    label("loc_2360")


    ChrTalk(    #106
        0xFE,
        (
            "Things always end up like this\x01",
            "whenever those two come\x01",
            "face-to-face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23AA")

    Jump("loc_2B41")

    label("loc_23AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2543")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A3")
    OP_A2(0x4)

    ChrTalk(    #107
        0xFE,
        (
            "I know it's painful, but we shouldn't\x01",
            "forget about what happened here\x01",
            "10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "In order to prevent such a tragedy\x01",
            "from ever happening again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "We need to tell our own children\x01",
            "about the events of the war.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2540")

    label("loc_24A3")


    ChrTalk(    #110
        0xFE,
        (
            "I know it's painful, but we shouldn't\x01",
            "forget about what happened here\x01",
            "10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "We need to prevent such a tragedy\x01",
            "from ever happening again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2540")

    Jump("loc_2B41")

    label("loc_2543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_267D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2606")
    OP_A2(0x4)

    ChrTalk(    #112
        0xFE,
        (
            "Whenever I see a soldier, it causes my\x01",
            "heart to skip a beat and reminds me of\x01",
            "what happened here 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "I really don't like them coming\x01",
            "here to our village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267A")

    label("loc_2606")


    ChrTalk(    #114
        0xFE,
        (
            "Whenever I see a soldier, it causes my\x01",
            "heart to skip a beat and reminds me of\x01",
            "what happened here 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_267A")

    Jump("loc_2B41")

    label("loc_267D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_END)), "loc_2798")

    ChrTalk(    #115
        0xFE,
        (
            "When the mine was in use the village\x01",
            "enjoyed a period of economic growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "In fact, this place was so lively with miners\x01",
            "and merchants you could have almost called\x01",
            "it a small city instead of a town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "However, following the war, this\x01",
            "place became quite lonely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B41")

    label("loc_2798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_281D")

    ChrTalk(    #118
        0xFE,
        "Are you looking for my husband?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Since it's this time of the day,\x01",
            "I'm sure he's up at the grave\x01",
            "site on the hill.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B41")

    label("loc_281D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_28E5")

    ChrTalk(    #120
        0xFE,
        (
            "It's a daily routine for me and my\x01",
            "husband to pay our respects to\x01",
            "the deceased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "We don't ever want those who lost\x01",
            "their lives during the war to feel\x01",
            "that they have been forgotten.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B41")

    label("loc_28E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2A9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F7")
    OP_A2(0x4)

    ChrTalk(    #122
        0xFE,
        (
            "The heat of flames burning flesh\x01",
            "and the charred smell of blackened\x01",
            "bones...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Amidst the screams and cries of\x01",
            "the villagers and their children...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "No matter how many years pass,\x01",
            "the terrible events of the war\x01",
            "remain ingrained in my mind...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A9A")

    label("loc_29F7")


    ChrTalk(    #125
        0xFE,
        (
            "Speaking of the war, I saw that young\x01",
            "man for the first time in years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "If he'd let me know he was coming,\x01",
            "I could have cleaned up the house\x01",
            "for him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9A")

    Jump("loc_2B41")

    label("loc_2A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2B41")

    ChrTalk(    #127
        0xFE,
        (
            "The people left in this village are\x01",
            "those who managed to live through\x01",
            "the flames of war 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "I hope we can all continue to\x01",
            "work together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B41")

    TalkEnd(0xB)
    Return()

    # Function_7_22DC end

    def Function_8_2B45(): pass

    label("Function_8_2B45")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2F27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 6)), scpexpr(EXPR_END)), "loc_2BC8")

    ChrTalk(    #129
        0xFE,
        (
            "Those guys from the army are still\x01",
            "standing guard outside the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "Looks like they're investigating\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F27")

    label("loc_2BC8")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x38E)

    ChrTalk(    #131
        0xFE,
        "Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#001FHi, Lewey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "I was shocked to see the army\x01",
            "haul you guys off after you went\x01",
            "up to the abandoned mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Especially, after you didn't do\x01",
            "anything wrong either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Are you guys okay? Did those\x01",
            "soldiers do anything bad to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#506FI'm sorry if we had you worried\x01",
            "there...\x02\x03",

            "#006FBut we're okay. As you can see\x01",
            "we're alive and kicking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "I am glad you guys are all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "So what I saw was actually an\x01",
            "airship then, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "Thanks for proving that I wasn't\x01",
            "just telling a tall tale!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#505FSure...\x02\x03",

            "But I'm sure the Royal Army would have\x01",
            "proved your story sooner or later, so I've\x01",
            "got mixed feelings about the whole ordeal...\x02\x03",

            "Considering that we were mistaken\x01",
            "for sky bandits and then arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x102,
        (
            "#010FWell, even if you didn't go out in style\x01",
            "at least you kept your promise...\x02\x03",

            "And isn't that enough?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F27")

    TalkEnd(0xC)
    Return()

    # Function_8_2B45 end

    def Function_9_2F2B(): pass

    label("Function_9_2F2B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2F9A")

    ChrTalk(    #142
        0xFE,
        "Whew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Now that we've got the saplings planted,\x01",
            "we'll finally be able to take a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36BA")

    label("loc_2F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3176")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AD")
    OP_A2(0x6)

    ChrTalk(    #144
        0xFE,
        (
            "The entire village oversees all the\x01",
            "orchards in Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Originally everyone operated on\x01",
            "their own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "But since the orchard farmers were shorthanded,\x01",
            "the village decided to manage the cultivation of\x01",
            "orchards together with everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3173")

    label("loc_30AD")


    ChrTalk(    #147
        0xFE,
        (
            "The entire village oversees all the\x01",
            "orchards in the Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Orchard farmers were shorthanded so the\x01",
            "village decided to manage the cultivation\x01",
            "of orchards together with everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3173")

    Jump("loc_36BA")

    label("loc_3176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3207")

    ChrTalk(    #149
        0xFE,
        (
            "Lewey was born after the war had\x01",
            "already ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "I hope that you will never have to\x01",
            "experience something as horrible\x01",
            "as that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36BA")

    label("loc_3207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_3252")

    ChrTalk(    #151
        0xFE,
        "Lewey seems to be rather upset.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "I wonder what's wrong.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36BA")

    label("loc_3252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_33DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3346")
    OP_A2(0x6)

    ChrTalk(    #153
        0xFE,
        (
            "I wonder if Lewey is still off crying\x01",
            "somewhere by himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I know he told me he saw a shadow\x01",
            "flying through the air the other night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "But any normal person would think he\x01",
            "mistook an animal for what he saw.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D8")

    label("loc_3346")


    ChrTalk(    #156
        0xFE,
        (
            "I wonder if Lewey is still off crying\x01",
            "somewhere by himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "I know he told me he saw a shadow\x01",
            "flying through the air the other night...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D8")

    Jump("loc_36BA")

    label("loc_33DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_35AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3517")
    OP_A2(0x6)

    ChrTalk(    #158
        0xFE,
        (
            "Have you visited the grave site\x01",
            "here in the village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "That large tombstone is dedicated\x01",
            "to the victims who died in the\x01",
            "Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "10 years ago this village suffered\x01",
            "greatly because of the fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "And even today I still see that horrific\x01",
            "scene sometimes in my dreams.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35A8")

    label("loc_3517")


    ChrTalk(    #162
        0xFE,
        (
            "Have you visited the grave site\x01",
            "here in the village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "That large tombstone is dedicated\x01",
            "to the victims who died in the\x01",
            "Hundred Day War.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A8")

    Jump("loc_36BA")

    label("loc_35AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_36BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x1000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3648")
    OP_A2(0x6)

    ChrTalk(    #164
        0xFE,
        "Good work, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I already let the village elder know\x01",
            "you were successful in exterminating\x01",
            "the monster.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36BA")

    label("loc_3648")


    ChrTalk(    #166
        0xFE,
        (
            "Well, now that the monster's taken\x01",
            "care of...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "We'll need to start sorting through\x01",
            "the various saplings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36BA")

    TalkEnd(0xD)
    Return()

    # Function_9_2F2B end

    def Function_10_36BE(): pass

    label("Function_10_36BE")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_378D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3742")
    OP_A2(0x7)

    ChrTalk(    #168
        0xFE,
        "Man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "If those two could just learn to get\x01",
            "along, I could head to Bose without\x01",
            "any reservations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_378D")

    label("loc_3742")


    ChrTalk(    #170
        0xFE,
        (
            "I want to see my wife and son who\x01",
            "are already waiting for me in Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_378D")

    TalkEnd(0xE)
    Return()

    # Function_10_36BE end

    def Function_11_3791(): pass

    label("Function_11_3791")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_38F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_386D")
    OP_A2(0x8)

    ChrTalk(    #171
        0xFE,
        (
            "I'm not saying that we should sacrifice\x01",
            "the taste of the fruit in favor of shipping\x01",
            "volume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "I'm just saying that we should learn\x01",
            "to make the same quality of fruit,\x01",
            "but more effectively.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F8")

    label("loc_386D")


    ChrTalk(    #173
        0xFE,
        (
            "I wonder why I can't get him to\x01",
            "understand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "If we could get Gray's cooperation,\x01",
            "I'm sure that things would work out\x01",
            "just fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F8")

    TalkEnd(0xF)
    Return()

    # Function_11_3791 end

    def Function_12_38FC(): pass

    label("Function_12_38FC")

    OP_A2(0x31E)
    OP_28(0x36, 0x1, 0x80)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(5700, 0, 48496, 0)
    OP_67(0, 7080, -10000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xA, 12)
    SetChrSubChip(0xA, 0)
    OP_4A(0xA, 255)
    SetChrPos(0xB, 1450, 0, 41600, 90)
    SetChrPos(0xA, 5990, 200, 46960, 270)
    SetChrPos(0x101, 4561, 200, 48200, 180)
    SetChrPos(0x102, 3391, 200, 48200, 180)
    SetChrPos(0x103, 4561, 200, 45845, 0)
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x103, 10)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x102, 1)
    SetChrSubChip(0x103, 2)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #175
        0xA,
        (
            "#2PSo you say there might be\x01",
            "some clues in that old mine, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        (
            "#2PI know for certain that the soldiers\x01",
            "didn't check inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#000F#6PAfter I heard Lewey's story, it\x01",
            "really got me thinking...\x02\x03",

            "We'd like to check the place out just\x01",
            "in case, so would you mind lending\x01",
            "us the key to the entrance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "#2PThe key for that padlock, huh?\x01",
            "Give me a minute here...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 2)
    SetChrPos(0xA, 5660, 0, 46450, 180)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    OP_0D()

    def lambda_3B87():
        OP_6D(4094, 2000, 41516, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3B87)
    OP_8E(0xA, 0x1F3A, 0x0, 0xA998, 0xBB8, 0x0)
    ClearChrFlags(0xA, 0x4)
    OP_8E(0xA, 0x1F3A, 0x7D0, 0x9CA2, 0xBB8, 0x0)
    OP_8E(0xA, 0x10CA, 0x7D0, 0x9EDB, 0xBB8, 0x0)
    OP_8C(0xA, 0, 400)

    ChrTalk(    #179
        0xA,
        "I'm sure I put it in this drawer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xA,
        "Oh, right. Here it is.\x02",
    )

    CloseMessageWindow()

    def lambda_3C2C():
        OP_6D(5700, 0, 48496, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3C2C)
    OP_8E(0xA, 0x1F3A, 0x7D0, 0x9CA2, 0xBB8, 0x0)
    OP_8E(0xA, 0x1F3A, 0x0, 0xA998, 0xBB8, 0x0)
    OP_8E(0xA, 0x161C, 0x0, 0xB572, 0xBB8, 0x0)
    Fade(1000)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x102, 1)
    SetChrSubChip(0x103, 2)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 5990, 200, 46960, 270)
    SetChrChipByIndex(0xA, 12)
    SetChrSubChip(0xA, 0)
    OP_44(0xA, 0xFF)
    OP_0D()

    ChrTalk(    #181
        0xA,
        "#2POkay, this should get you inside.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x32E, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #182
        "\x07\x00Received \x07\x02Abandoned Mine Key\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #183
        0x101,
        (
            "#004F#6PWow, this key looks ancient...\x02\x03",

            "#001FMany thanks, Elder Reisen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x102,
        "#010F#1PThis will really help a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xA,
        (
            "#2PDon't mention it. We're always\x01",
            "indebted to the Bracer Guild\x01",
            "for their help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        (
            "#2PIt's only natural that we would\x01",
            "try and return the favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x103,
        (
            "#021F#5PThank you! If everyone we dealt\x01",
            "with were as cooperative as you, it\x01",
            "would make our lives a lot easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x102,
        (
            "#010F#1PWe'll be sure to let you know if\x01",
            "we find anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        "#2PI would appreciate that.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xA, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_6D(720, 0, 45250, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrPos(0x101, 720, 0, 45250, 180)
    SetChrPos(0x102, 720, 0, 45250, 180)
    SetChrPos(0x103, 720, 0, 45250, 180)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x102, 65535)
    OP_69(0x101, 0x0)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_12_38FC end

    SaveToFile()

Try(main)
