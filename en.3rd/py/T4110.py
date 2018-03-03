from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4110   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4110.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Seagaro',                              # 9
        'Patty',                                # 10
        'Ralph',                                # 11
        'Bill',                                 # 12
        'Ilene',                                # 13
        'Duncan',                               # 14
        'Melony',                               # 15
        'Pesca',                                # 16
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
        'ED6_DT07/CH01030 ._CH',             # 00
        'ED6_DT07/CH01043 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01490 ._CH',             # 03
        'ED6_DT07/CH01180 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01030P._CP',             # 00
        'ED6_DT07/CH01043P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01490P._CP',             # 03
        'ED6_DT07/CH01180P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
    )

    DeclNpc(
        X                   = 7220,
        Z                   = 200,
        Y                   = 53570,
        Direction           = 269,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -29600,
        Z                   = 4000,
        Y                   = 1830,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -27310,
        Z                   = 0,
        Y                   = -4370,
        Direction           = 81,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 26900,
        Z                   = 4000,
        Y                   = -470,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 26830,
        Z                   = 4000,
        Y                   = -1620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 91740,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 23,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 51810,
        Z                   = 0,
        Y                   = 56250,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 51250,
        Z                   = 0,
        Y                   = 55180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1F9",          # 01, 1
        "Function_2_203",          # 02, 2
        "Function_3_227",          # 03, 3
        "Function_4_4DD",          # 04, 4
        "Function_5_810",          # 05, 5
        "Function_6_915",          # 06, 6
        "Function_7_A9B",          # 07, 7
        "Function_8_BBB",          # 08, 8
        "Function_9_D3F",          # 09, 9
        "Function_10_EA5",         # 0A, 10
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8")
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)

    label("loc_1F8")

    Return()

    # Function_0_1E2 end

    def Function_1_1F9(): pass

    label("Function_1_1F9")

    OP_B1("t4110_n")
    Return()

    # Function_1_1F9 end

    def Function_2_203(): pass

    label("Function_2_203")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_226")
    OP_8D(0xFE, -30880, 4000, -29430, 0, 2000)
    Jump("Function_2_203")

    label("loc_226")

    Return()

    # Function_2_203 end

    def Function_3_227(): pass

    label("Function_3_227")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_234")
    Jump("loc_4D9")

    label("loc_234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_3B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D4")

    ChrTalk(    #0
        0xFE,
        (
            "I can't believe he actually bought us a house\x01",
            "here after I said I wanted to live in the city!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "He must really love me, mustn't he? ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B6")

    label("loc_2D4")


    ChrTalk(    #2
        0xFE,
        (
            "I was the one who first said I wanted to live\x01",
            "in the city, but I don't regret it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I mean, if we're going to buy ourselves a new\x01",
            "house, it's best to try and get as much of what\x01",
            "you want as possible from it, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3B6")

    Jump("loc_4D9")

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_3C3")
    Jump("loc_4D9")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_4D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_455")

    ChrTalk(    #4
        0xFE,
        "It sure is nice being able to live in a big city!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "It's especially convenient when I need to get\x01",
            "some shopping in, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9")

    label("loc_455")


    ChrTalk(    #6
        0xFE,
        (
            "Teehee. Begging my husband to buy us\x01",
            "a house here finally paid off. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "I've always wanted to live here in the capital.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4D9")

    TalkEnd(0xFE)
    Return()

    # Function_3_227 end

    def Function_4_4DD(): pass

    label("Function_4_4DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_80C")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_6CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5D6")

    ChrTalk(    #8
        0xFE,
        (
            "I can't help but feel like my wife's got me \x01",
            "wrapped around her little finger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Not only did I buy this house, but I'm the\x01",
            "one who's doing all of the chores, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Is this really how things should be...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CA")

    label("loc_5D6")


    ChrTalk(    #11
        0xFE,
        (
            "The price of property seems to be creeping\x01",
            "up and up lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "So on a logical level, this does seem like\x01",
            "a sound time to be buying a house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I can't help but feel like my wife's got me \x01",
            "wrapped around her little finger, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_6CA")

    Jump("loc_80C")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_6D7")
    Jump("loc_80C")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_80C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_75F")

    ChrTalk(    #14
        0xFE,
        (
            "I ended up buying this house in a moment\x01",
            "of great weakness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "...My poor wallet is still reeling from it, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_80C")

    label("loc_75F")


    ChrTalk(    #16
        0xFE,
        "What do you think? Pretty nice house, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I sure think so, which is just as well, seeing as\x01",
            "I'm the one who bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "...Against my own better judgment.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_80C")

    TalkEnd(0xFE)
    Return()

    # Function_4_4DD end

    def Function_5_810(): pass

    label("Function_5_810")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_81D")
    Jump("loc_911")

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_88F")

    ChrTalk(    #19
        0xFE,
        "Perhaps we should go over to the royal villa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "That area is perfect for a nice, relaxing walk.\x02",
    )

    CloseMessageWindow()
    Jump("loc_911")

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_899")
    Jump("loc_911")

    label("loc_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_911")

    ChrTalk(    #21
        0xFE,
        "It certainly is a fine day, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Here's hoping this is just another peaceful\x01",
            "day here in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_911")

    TalkEnd(0xFE)
    Return()

    # Function_5_810 end

    def Function_6_915(): pass

    label("Function_6_915")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_922")
    Jump("loc_A97")

    label("loc_922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_9B6")

    ChrTalk(    #23
        0xFE,
        "Oh, I quite agree! It really is stunning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Let me know if you start feeling tired, though.\x01",
            "We wouldn't want to strain your back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A97")

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_9C0")
    Jump("loc_A97")

    label("loc_9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_A97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_A66")

    ChrTalk(    #25
        0xFE,
        (
            "It's only thanks to Her Majesty that we were\x01",
            "able to pick ourselves up after that war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "As a nation, we truly owe a precious amount\x01",
            "to her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A97")

    label("loc_A66")


    ChrTalk(    #27
        0xFE,
        "I completely agree. Nothing beats peace.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_A97")

    TalkEnd(0xFE)
    Return()

    # Function_6_915 end

    def Function_7_A9B(): pass

    label("Function_7_A9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B38")

    ChrTalk(    #28
        0xFE,
        "I work over at the port. You ever been by there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Today's weather is so nice, we might even get to\x01",
            "see some mirages over there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B99")

    label("loc_B38")

    OP_8C(0xFE, 23, 0)

    ChrTalk(    #30
        0xFE,
        "Phew! That's the leak all fixed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Now to head out and do a good day's work!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_B99")

    Jump("loc_BB7")

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_BA6")
    Jump("loc_BB7")

    label("loc_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_BB0")
    Jump("loc_BB7")

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_BB7")

    label("loc_BB7")

    TalkEnd(0xFE)
    Return()

    # Function_7_A9B end

    def Function_8_BBB(): pass

    label("Function_8_BBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C9C")

    ChrTalk(    #32
        0xFE,
        (
            "It's almost time for the archbishop's sermon\x01",
            "to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "His sermons're always worth listening to.\x01",
            "He says some real thought-provoking things\x01",
            "in them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "Why don't you two come along and listen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D1D")

    label("loc_C9C")


    ChrTalk(    #35
        0xFE,
        (
            "Hey. Did you know it's almost time for the \x01",
            "archbishop's sermon to begin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "I should get going over to the cathedral.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_D1D")

    Jump("loc_D3B")

    label("loc_D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_D2A")
    Jump("loc_D3B")

    label("loc_D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_D34")
    Jump("loc_D3B")

    label("loc_D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_D3B")

    label("loc_D3B")

    TalkEnd(0xFE)
    Return()

    # Function_8_BBB end

    def Function_9_D3F(): pass

    label("Function_9_D3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_DE7")

    ChrTalk(    #37
        0xFE,
        (
            "See, look at this cultivar. Pretty promising,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I'd love to be able to loan a proper farm from\x01",
            "someone to test out all of my research.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_DE7")


    ChrTalk(    #39
        0xFE,
        (
            "I do research on the cultivation of crops,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "It's not a full-time occupation or anything,\x01",
            "though. It's just something I do as a hobby.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_E83")

    Jump("loc_EA1")

    label("loc_E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_E90")
    Jump("loc_EA1")

    label("loc_E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_E9A")
    Jump("loc_EA1")

    label("loc_E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_EA1")

    label("loc_EA1")

    TalkEnd(0xFE)
    Return()

    # Function_9_D3F end

    def Function_10_EA5(): pass

    label("Function_10_EA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_F40")

    ChrTalk(    #41
        0xFE,
        (
            "If you ask me, being able to spend time surrounded\x01",
            "by natural greenery is the definition of bliss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "...I'm so glad I met him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1010")

    label("loc_F40")


    ChrTalk(    #43
        0xFE,
        (
            "Heehee. My husband's hobby is quite an unusual\x01",
            "one, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "I think it's lovely, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "If you ask me, being able to spend time surrounded\x01",
            "by natural greenery is the definition of bliss.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1010")

    Jump("loc_102E")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_101D")
    Jump("loc_102E")

    label("loc_101D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1027")
    Jump("loc_102E")

    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_102E")

    label("loc_102E")

    TalkEnd(0xFE)
    Return()

    # Function_10_EA5 end

    SaveToFile()

Try(main)
