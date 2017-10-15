from ED6SCScenarioHelper import *

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
        'Lakeisha',                             # 9
        'Phelio',                               # 10
        'Seagaro',                              # 11
        'Patty',                                # 12
        'Ralph',                                # 13
        'Bill',                                 # 14
        'Ilene',                                # 15
        'Duncan',                               # 16
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
    )

    AddCharChipPat(
        'ED6_DT07/CH01030P._CP',             # 00
        'ED6_DT07/CH01043P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01490P._CP',             # 03
        'ED6_DT07/CH01180P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
    )

    DeclNpc(
        X                   = 59570,
        Z                   = 0,
        Y                   = 58710,
        Direction           = 3,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 57660,
        Z                   = 0,
        Y                   = 58150,
        Direction           = 53,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 28110,
        Z                   = 0,
        Y                   = -950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 32189,
        Z                   = 0,
        Y                   = 6630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 91740,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 23,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_30B",          # 01, 1
        "Function_2_331",          # 02, 2
        "Function_3_355",          # 03, 3
        "Function_4_ACA",          # 04, 4
        "Function_5_110C",         # 05, 5
        "Function_6_1842",         # 06, 6
        "Function_7_20B5",         # 07, 7
        "Function_8_2638",         # 08, 8
        "Function_9_2E76",         # 09, 9
        "Function_10_2F35",        # 0A, 10
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FF")
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xE, 31320, 0, 100, 270)
    SetChrFlags(0xE, 0x10)
    Jump("loc_30A")

    label("loc_1FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_25E")
    SetChrPos(0xB, -27310, 0, -4370, 81)
    OP_43(0xB, 0x0, 0x6, 0x2)
    SetChrPos(0xC, -29600, 4000, 1830, 90)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xE, 31320, 0, 100, 270)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_30A")

    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_29D")
    SetChrPos(0xB, -27310, 0, -4370, 81)
    OP_43(0xB, 0x0, 0x6, 0x2)
    SetChrPos(0xC, -29600, 4000, 1830, 90)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrFlags(0xE, 0x10)
    Jump("loc_30A")

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2DC")
    SetChrPos(0xB, -27310, 0, -4370, 81)
    OP_43(0xB, 0x0, 0x6, 0x2)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xC, -29600, 4000, 1830, 90)
    OP_43(0xC, 0x0, 0x0, 0x2)
    Jump("loc_30A")

    label("loc_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA")
    Jump("loc_30A")

    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2F9")
    SetChrFlags(0xE, 0x10)
    Jump("loc_30A")

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_303")
    Jump("loc_30A")

    label("loc_303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_30A")

    label("loc_30A")

    Return()

    # Function_0_1DA end

    def Function_1_30B(): pass

    label("Function_1_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_327")
    OP_B1("t4110_y")
    Jump("loc_330")

    label("loc_327")

    OP_B1("t4110_n")

    label("loc_330")

    Return()

    # Function_1_30B end

    def Function_2_331(): pass

    label("Function_2_331")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_354")
    OP_8D(0xFE, -30880, 4000, -29430, 0, 2000)
    Jump("Function_2_331")

    label("loc_354")

    Return()

    # Function_2_331 end

    def Function_3_355(): pass

    label("Function_3_355")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_406")

    ChrTalk(    #0
        0xFE,
        (
            "My husband went off to the harbor\x01",
            "in order to defend the warehouses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I wonder if he's finally latched onto\x01",
            "something? All my hard work's paid\x01",
            "off!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD")

    label("loc_406")


    ChrTalk(    #2
        0xFE,
        (
            "I feel like I've seen that store owner\x01",
            "somewhere before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Whenever I try to get a good look at\x01",
            "his face, though, he hides in the back\x01",
            "of the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "Maybe he's shy?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_4BD")

    Jump("loc_AC6")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_633")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_59F")

    ChrTalk(    #5
        0xFE,
        (
            "That reminds me! You know how\x01",
            "the house next door has been on\x01",
            "the market for ages, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I heard they found someone who's\x01",
            "willing to rent the place. Haven't seen\x01",
            "them yet, but am I ever curious!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_630")

    label("loc_59F")


    ChrTalk(    #7
        0xFE,
        (
            "When I heard my husband had gotten\x01",
            "mixed up in that mess at the harbor,\x01",
            "I felt the life drained out of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "I'm so glad he's safe...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_630")

    Jump("loc_AC6")

    label("loc_633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_778")

    ChrTalk(    #9
        0xFE,
        (
            "I went and delivered a specially\x01",
            "packed lunch to my husband out\x01",
            "working at the harbor today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "He's more liable to give up than\x01",
            "keep trying if I'm too hard on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Sometimes you just have to use\x01",
            "the carrot AND stick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I'm basing it all on a book written\x01",
            "by the most amazing person from\x01",
            "the Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC6")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84B")

    ChrTalk(    #13
        0xFE,
        (
            "My husband wouldn't wake up, so I\x01",
            "dragged him outside in his pajamas\x01",
            "and sent him to work just like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "He may not like it now, but he'll\x01",
            "understand that it's for his own\x01",
            "good someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC6")

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_99C")

    ChrTalk(    #15
        0xFE,
        (
            "The more I think about it, the more\x01",
            "I realize that I'm the one at fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I could've taken a stand against my\x01",
            "husband's reckless behavior all this\x01",
            "time, but I kept letting it slide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "You know what? I don't care if they call\x01",
            "me the wife from hell--I'll put an end to his\x01",
            "ludicrous ways if it's the last thing I do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC6")

    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_AC6")

    ChrTalk(    #18
        0xFE,
        (
            "My husband's been working his butt off\x01",
            "at the harbor ever since he blew all our\x01",
            "savings at the casino in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I guess the shock of losing that much\x01",
            "finally made him see the error of his\x01",
            "ways...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "...Or not. I want to believe that,\x01",
            "but I won't take my eyes off of him\x01",
            "just yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC6")

    TalkEnd(0xFE)
    Return()

    # Function_3_355 end

    def Function_4_ACA(): pass

    label("Function_4_ACA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BC6")

    ChrTalk(    #21
        0xFE,
        (
            "At first, I was pretty down about all the\x01",
            "orbments not working, but at times like\x01",
            "these we've just gotta keep strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "My wife's been putting her all into her\x01",
            "work at the department store, and I don't\x01",
            "plan on doing anything less.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1108")

    label("loc_BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_C71")

    ChrTalk(    #23
        0xFE,
        (
            "A fair portion of the harbor facilities\x01",
            "were destroyed by the tank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "...And Duncan was captured by the\x01",
            "Special Ops, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "I hope he's not hurt...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1108")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_DF8")

    ChrTalk(    #26
        0xFE,
        (
            "One of the sisters at the Bose Chapel\x01",
            "was getting angry because folks\x01",
            "were praying for financial success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "True, Aidios isn't a goddess of wealth.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I HAVE heard about a deity of wealth\x01",
            "that's worshiped in certain parts of the\x01",
            "Republic, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "...Keep that nugget from Edel, okay?\x01",
            "I love my wife, but if she heard that,\x01",
            "she'd jump on the first flight to Calvard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1108")

    label("loc_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EDA")

    ChrTalk(    #30
        0xFE,
        (
            "The Rolent Chapel was simple, but\x01",
            "Father Divine left a strong impression\x01",
            "on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "He was calm, solemn, and very\x01",
            "knowledgeable about medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Exactly the kind of person a priest\x01",
            "should aspire to be!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1108")

    label("loc_EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1051")

    ChrTalk(    #33
        0xFE,
        (
            "A while back, my wife and I went on\x01",
            "a pilgrimage to all the chapels and\x01",
            "cathedrals in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "...Turns out she just wanted to shopping\x01",
            "for all the latest trends in every region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Anyway, Archbishop Currant suggested\x01",
            "that I put together a journal detailing my\x01",
            "pilgrimage, so here I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Not much of a writer, but what the hey.\x01",
            "I'll give it a shot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1108")

    label("loc_1051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1108")

    ChrTalk(    #37
        0xFE,
        (
            "My wife runs the department store\x01",
            "in the East Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "What about me, you ask? Hmm...\x01",
            "I guess I'm something of a priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I'm not a househusband. Nope.\x01",
            "Not at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1108")

    TalkEnd(0xFE)
    Return()

    # Function_4_ACA end

    def Function_5_110C(): pass

    label("Function_5_110C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11AF")

    ChrTalk(    #40
        0xFE,
        (
            "Aaaagh! This SUCKS. Not being able\x01",
            "to use orbments is such a hassle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I trust that Her Majesty will be able to\x01",
            "fix everything soon, however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_11AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_149D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E4")

    ChrTalk(    #42
        0xFE,
        (
            "My sweet hubby stayed up nearly the\x01",
            "whole night getting us the perfect seats\x01",
            "for the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I'll have to lay on the charm extra\x01",
            "thick come next year if I'm gonna get\x01",
            "him to do it again. What to do... ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "...Oh, don't give me that look!\x01",
            "I'm only kidding. Maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I work my hardest to keep this house\x01",
            "in shape for him. Everything I do, I do it\x01",
            "for love. I really, truly love that man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "The reason I'm so selfish all the time?\x01",
            "I want him to show him how much he\x01",
            "loves me. I want to see how far he'll go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_149A")

    label("loc_13E4")


    ChrTalk(    #47
        0xFE,
        (
            "Sure, I COULD do all the housework.\x01",
            "'Could' being the operative word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "But if I did that, I wouldn't get a chance\x01",
            "to see my hubby work so hard for me,\x01",
            "now, would I? Heehee.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149A")

    Jump("loc_183E")

    label("loc_149D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_14E1")

    ChrTalk(    #49
        0xFE,
        "Hmmhmmhmmmmm... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Time to start making dinner!\x02",
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_14E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_151F")

    ChrTalk(    #51
        0xFE,
        "Hmmhmmhmmmmm... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "Lalala la, la la... ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_151F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C7")

    ChrTalk(    #53
        0xFE,
        (
            "I wonder if this Colonel Cid\x01",
            "guy is as strong as they say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "He certainly doesn't look very\x01",
            "strong. At least, judging by the\x01",
            "photo, he doesn't.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_16E5")

    ChrTalk(    #55
        0xFE,
        (
            "I wonder who'd come out on top\x01",
            "in a match between Captain Schwarz\x01",
            "and Brigadier General Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Oooh, this is a toughie...\x01",
            "Time to so some research!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Naturally, all I'll have to do is sweet talk\x01",
            "my husband into scouting out one of the\x01",
            "army's training sessions. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_16E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_17D8")

    ChrTalk(    #58
        0xFE,
        (
            "Is Brigadier General Bright the same hero\x01",
            "from the Hundred Days War?\x01",
            "Like, is he THAT Cassius Bright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Oooh, I wonder how he'd do if he\x01",
            "were in the Martial Arts Competition.\x01",
            "That'd be so cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "Time to so some research!\x02",
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_183E")

    ChrTalk(    #61
        0xFE,
        "I can't waaait until next year!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I can't wait for the next Martial Arts\x01",
            "Competition! \x02",
        )
    )

    CloseMessageWindow()

    label("loc_183E")

    TalkEnd(0xFE)
    Return()

    # Function_5_110C end

    def Function_6_1842(): pass

    label("Function_6_1842")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_184F")
    Jump("loc_20B1")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_191C")

    ChrTalk(    #63
        0xFE,
        "Yeowch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Daytime's not so bad. At least it's\x01",
            "warm and I can see what I'm doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Cooking at night, however... Now,\x01",
            "that's a real pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "I just hope I don't set myself on fire...\x02",
    )

    CloseMessageWindow()
    Jump("loc_20B1")

    label("loc_191C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_19C3")

    ChrTalk(    #67
        0xFE,
        (
            "A-Am I dreaming? What's going on?!\x01",
            "Something must be terribly wrong!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Y-You there! You've got to help me!\x01",
            "It's my wife, she's...she's doing chores!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B1")

    label("loc_19C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1B43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9D")

    ChrTalk(    #69
        0xFE,
        "...Something must be terribly wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "My wife's been doing chores all day!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "I mean, yeah, I'm happy she's helping,\x01",
            "but knowing her... You don't think she's\x01",
            "plotting something, do you?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1B40")

    label("loc_1A9D")


    ChrTalk(    #72
        0xFE,
        (
            "If my wife by some miracle is doing\x01",
            "chores just to help, then I'm thrilled,\x01",
            "but knowing her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "*shiver* She's planning something.\x01",
            "Something nefarious...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B40")

    Jump("loc_20B1")

    label("loc_1B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1BD5")

    ChrTalk(    #74
        0xFE,
        (
            "Phew! Patty's actually doing the\x01",
            "cooking for once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Looks like I'll be able to kick back\x01",
            "and relax for the first time in ages.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B1")

    label("loc_1BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C4B")

    ChrTalk(    #76
        0xFE,
        "And with that, another day is done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Oh, Aidios... Am I content to have\x01",
            "this as my daily life?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B1")

    label("loc_1C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1D81")

    ChrTalk(    #78
        0xFE,
        (
            "I was up all night during the Martial Arts\x01",
            "Competition, all so I could score two of\x01",
            "the best seats for me and Patty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Part of me's happy to do something for\x01",
            "her, but I wonder if I'm just feeding into\x01",
            "her selfishness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I feel like I'm being pulled by the strings\x01",
            "more than ever before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B1")

    label("loc_1D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1FA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EEF")

    ChrTalk(    #81
        0xFE,
        (
            "She wants me to pick up special edition\x01",
            "books about the Martial Arts Competition\x01",
            "while I'm out shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "*sigh*\x01",
            "I wish her only vice was her eating out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "My wife apparently can't wait for the\x01",
            "next Martial Arts Competition. She's\x01",
            "already trying to predict the winner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "They haven't even decided who'll be\x01",
            "participating yet...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1FA3")

    label("loc_1EEF")


    ChrTalk(    #85
        0xFE,
        (
            "My wife apparently can't wait for the\x01",
            "next Martial Arts Competition. She's\x01",
            "already trying to predict the winner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "They haven't even decided who'll be\x01",
            "participating yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA3")

    Jump("loc_20B1")

    label("loc_1FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_20B1")

    ChrTalk(    #87
        0xFE,
        (
            "My wife can't stop thinking about the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "I don't mind her THINKING about the\x01",
            "Martial Arts Competition next year, sure,\x01",
            "but on the other hand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "...she could help out with a few of the\x01",
            "chores while she's thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B1")

    TalkEnd(0xFE)
    Return()

    # Function_6_1842 end

    def Function_7_20B5(): pass

    label("Function_7_20B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2182")

    ChrTalk(    #90
        0xFE,
        (
            "Pfft! Why, when I was a young lad,\x01",
            "we didn't even have orbments!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "There's not a darned thing inconvenient\x01",
            "about living without 'em, I say! If anything,\x01",
            "it brings me back to my youth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2634")

    label("loc_2182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_21EB")

    ChrTalk(    #92
        0xFE,
        "Now, my dear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "What do you believe is the most\x01",
            "important thing to live for in life?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2634")

    label("loc_21EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_229A")

    ChrTalk(    #94
        0xFE,
        (
            "I'd like to see our grandchild again,\x01",
            "I think. It's been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Old as I am, my greatest pleasure\x01",
            "is seeing my son, his wife, and my\x01",
            "beloved grandchild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2634")

    label("loc_229A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2308")

    ChrTalk(    #96
        0xFE,
        "Aaah, what wonderful weather today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Beautiful days like this lift this\x01",
            "old man's spirits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2634")

    label("loc_2308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_236C")

    ChrTalk(    #98
        0xFE,
        "Is it already this late?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Almighty Aidios, I thank you\x01",
            "for this day's peace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2634")

    label("loc_236C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2474")

    ChrTalk(    #100
        0xFE,
        (
            "That foul coup d'etat was unfortunate,\x01",
            "but thankfully awful nothing came of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I hope the non-aggression pact signing\x01",
            "ceremony ends on a high note.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I'm sure we'll be all right now\x01",
            "that Brigadier General Bright's back with\x01",
            "the Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2634")

    label("loc_2474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_25C0")

    ChrTalk(    #103
        0xFE,
        (
            "My! A non-aggression pact between not\x01",
            "two, but three countries? Countries that\x01",
            "are always at each other's throats, at that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Who else but Queen Alicia could manage to\x01",
            "have both the Empire and Republic agree to\x01",
            "set aside their weapons in favor of peace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Her Majesty is the reason Liberl thrives\x01",
            "as a country.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2634")

    label("loc_25C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2634")

    ChrTalk(    #106
        0xFE,
        "Today's weather is so good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "I think I'd like to go on a walk with my\x01",
            "beloved at the royal villa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2634")

    TalkEnd(0xFE)
    Return()

    # Function_7_20B5 end

    def Function_8_2638(): pass

    label("Function_8_2638")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2747")

    ChrTalk(    #108
        0xFE,
        (
            "Bringing it back to 'your youth' doesn't\x01",
            "stop all this from being inconvenient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "No matter how trying the circumstances,\x01",
            "I've never lost the strength to endure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "So long as we stay strong and endure,\x01",
            "Her Majesty will surely pull through for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_285F")

    ChrTalk(    #111
        0xFE,
        (
            "Why, the most important thing is\x01",
            "the strength to endure, of course!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "No matter how terrible the circumstances,\x01",
            "so long as we band together and endure,\x01",
            "we can overcome any obstacle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "As long as you have a strong,\x01",
            "steadfast heart, you'll be able to\x01",
            "be happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_285F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2916")

    ChrTalk(    #114
        0xFE,
        (
            "That reminds me--I saw the most adorable\x01",
            "girl in a white dress at the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I couldn't help but think of our grandchild.\x01",
            "I wonder how they're doing...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2A53")

    ChrTalk(    #116
        0xFE,
        (
            "As the signing ceremony edges closer,\x01",
            "the town's grown more and more into a\x01",
            "frenzy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "The city's most beautiful during times\x01",
            "like this. I love all the warmth and energy\x01",
            "in the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "This is the city where I met my darling\x01",
            "husband, after all. Where we've lived,\x01",
            "where we've grown old together...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF9")

    ChrTalk(    #119
        0xFE,
        (
            "I just hope the world keeps on moving\x01",
            "in the right direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I haven't a clue what's happening\x01",
            "in the modern world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "Things were much simpler back\x01",
            "when I was young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Ever since the revolution, the world's\x01",
            "just changed so rapidly... It makes\x01",
            "this old girl anxious, if I'm to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "I suppose as long as we don't forget\x01",
            "to be thankful to Her Majesty, we'll be\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2CD2")

    label("loc_2BF9")


    ChrTalk(    #124
        0xFE,
        (
            "Ever since the revolution, the world's\x01",
            "just changed so rapidly... It makes\x01",
            "this old girl anxious, if I'm to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I suppose as long as we don't forget\x01",
            "to be thankful to Her Majesty, we'll be\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD2")

    Jump("loc_2E72")

    label("loc_2CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2D5C")

    ChrTalk(    #126
        0xFE,
        (
            "Now, now! Your blood pressure\x01",
            "could start acting up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "You take a seat and wait--I'm going\x01",
            "to put on some tea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2DF4")

    ChrTalk(    #128
        0xFE,
        (
            "The reason my husband and I can\x01",
            "live without worry is because of Her\x01",
            "Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I always have--and always will--\x01",
            "be thankful for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2E72")

    ChrTalk(    #130
        0xFE,
        (
            "My husband and I used to take walks\x01",
            "to the villa quite often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "We haven't gone since the coup d'etat,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E72")

    TalkEnd(0xFE)
    Return()

    # Function_8_2638 end

    def Function_9_2E76(): pass

    label("Function_9_2E76")

    TalkBegin(0xFE)

    ChrTalk(    #132
        0xFE,
        "*sigh* The harbor's closed again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "I thought all the crap from the coup\x01",
            "would've been done and over with by\x01",
            "now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "If this keeps up, I might seriously be\x01",
            "out of a job!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_2E76 end

    def Function_10_2F35(): pass

    label("Function_10_2F35")

    TalkBegin(0xFE)

    ChrTalk(    #135
        0xFE,
        (
            "My wife's been really stressed lately,\x01",
            "and it's all because of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I think I'll try and help ease her workload\x01",
            "around the house on my next day off.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_2F35 end

    SaveToFile()

Try(main)
