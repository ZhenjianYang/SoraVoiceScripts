from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0110   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0110.x',
        MapIndex            = 11,
        MapDefaultBGM       = "ed60010",
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
        'Rhett',                                # 9
        'Serra',                                # 10
        'Maggy',                                # 11
        'Luke',                                 # 12
        'Pat',                                  # 13
        'Diary',                                # 14
    )

    DeclEntryPoint(
        Unknown_00              = 52000,
        Unknown_04              = 0,
        Unknown_08              = 164000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 83000,
        Unknown_04              = 0,
        Unknown_08              = 116000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01120 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH01110 ._CH',             # 02
        'ED6_DT07/CH01160 ._CH',             # 03
        'ED6_DT07/CH01060 ._CH',             # 04
        'ED6_DT06/CH20021 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01120P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH01110P._CP',             # 02
        'ED6_DT07/CH01160P._CP',             # 03
        'ED6_DT07/CH01060P._CP',             # 04
        'ED6_DT06/CH20021P._CP',             # 05
    )

    DeclNpc(
        X                   = 93326,
        Z                   = 0,
        Y                   = 162898,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 58084,
        Z                   = 0,
        Y                   = 198250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 51750,
        Z                   = 0,
        Y                   = 163200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 55045,
        Z                   = 0,
        Y                   = 164193,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 88798,
        Z                   = 0,
        Y                   = 163093,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 52700,
        Z                   = 700,
        Y                   = 161650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 52860,
        TriggerZ            = 0,
        TriggerY            = 161440,
        TriggerRange        = 800,
        ActorX              = 52700,
        ActorZ              = 700,
        ActorY              = 161650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_24A",          # 02, 2
        "Function_3_260",          # 03, 3
        "Function_4_284",          # 04, 4
        "Function_5_2A8",          # 05, 5
        "Function_6_2CC",          # 06, 6
        "Function_7_FE3",          # 07, 7
        "Function_8_1900",         # 08, 8
        "Function_9_1B1C",         # 09, 9
        "Function_10_233A",        # 0A, 10
        "Function_11_244E",        # 0B, 11
    )


    def Function_0_202(): pass

    label("Function_0_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_211")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_227")

    label("loc_211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_227")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    label("loc_227")

    Return()

    # Function_0_202 end

    def Function_1_228(): pass

    label("Function_1_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_240")
    OP_B1("t0110_y")
    Jump("loc_249")

    label("loc_240")

    OP_B1("t0110_n")

    label("loc_249")

    Return()

    # Function_1_228 end

    def Function_2_24A(): pass

    label("Function_2_24A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_24A")

    label("loc_25F")

    Return()

    # Function_2_24A end

    def Function_3_260(): pass

    label("Function_3_260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_283")
    OP_8D(0xFE, 51000, 165000, 56500, 163300, 2500)
    Jump("Function_3_260")

    label("loc_283")

    Return()

    # Function_3_260 end

    def Function_4_284(): pass

    label("Function_4_284")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A7")
    OP_8D(0xFE, 52766, 165023, 56498, 163482, 3000)
    Jump("Function_4_284")

    label("loc_2A7")

    Return()

    # Function_4_284 end

    def Function_5_2A8(): pass

    label("Function_5_2A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CB")
    OP_8D(0xFE, 87700, 161023, 91100, 164700, 3000)
    Jump("Function_5_2A8")

    label("loc_2CB")

    Return()

    # Function_5_2A8 end

    def Function_6_2CC(): pass

    label("Function_6_2CC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_43D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        (
            "I read in the Liberl News that Bose\x01",
            "has been hit by a recent string of\x01",
            "burglaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Speaking of Bose, it's the economic\x01",
            "center of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "There sure are a lot of people with\x01",
            "criminal minds these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A")

    label("loc_3BB")


    ChrTalk(    #3
        0xFE,
        (
            "Speaking of Bose, it's the economic\x01",
            "center of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "There sure are a lot of people with\x01",
            "criminal minds these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A")

    Jump("loc_FDF")

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4E1")

    ChrTalk(    #5
        0xFE,
        (
            "You know, Liberl News is selling\x01",
            "like hotcakes lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Up until just recently, it was a\x01",
            "minor magazine circulated in and\x01",
            "around the Royal City.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDF")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_67A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD")
    OP_A2(0x0)

    ChrTalk(    #7
        0xFE,
        (
            "The Liberl Kingdom is sandwiched in\x01",
            "between two powerful nations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "The Erebonian Empire to the north\x01",
            "and the Calvard Republic to the east.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "But it has proudly maintained its\x01",
            "independence since the country\x01",
            "was founded.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677")

    label("loc_5DD")


    ChrTalk(    #10
        0xFE,
        (
            "The Liberl Kingdom is sandwiched in\x01",
            "between two powerful nations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "But it has proudly maintained its\x01",
            "independence since the country\x01",
            "was founded.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_677")

    Jump("loc_FDF")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_87A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A8")
    OP_A2(0x0)

    ChrTalk(    #12
        0xFE,
        (
            "Our nation is divided up into 5 regions\x01",
            "with a central city in each.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Mayor Klaus has been given charge\x01",
            "of Rolent, which is one of these cities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Although he's called 'Ol' Man Klaus' because\x01",
            "he likes to potter about in his garden, he's\x01",
            "actually a very capable leader.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_877")

    label("loc_7A8")


    ChrTalk(    #15
        0xFE,
        (
            "Mayor Klaus has been given charge\x01",
            "of Rolent, which is one of these cities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Although he's called 'Ol' Man Klaus' because\x01",
            "he likes to potter about in his garden, he's\x01",
            "actually a very capable leader.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_877")

    Jump("loc_FDF")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_992")
    OP_A2(0x0)

    ChrTalk(    #17
        0xFE,
        (
            "I was shocked when I heard the\x01",
            "news that Pat had gone to the\x01",
            "Esmelas Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "He's an obedient kid, but like any\x01",
            "child, it seems he has a strong\x01",
            "sense of curiosity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "It's not a bad thing, but I sure\x01",
            "scolded him something fierce\x01",
            "over it this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3F")

    label("loc_992")


    ChrTalk(    #20
        0xFE,
        (
            "I was shocked when I heard the\x01",
            "news that Pat had gone to the\x01",
            "Esmelas Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "He's an obedient kid, but like any\x01",
            "child, it seems he has a strong\x01",
            "sense of curiosity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3F")

    Jump("loc_FDF")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_C38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AA4")

    ChrTalk(    #22
        0x8,
        (
            "Things from ancient civilizations\x01",
            "sure do grab the imagination,\x01",
            "don't they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BC7")
    OP_A2(0x1)

    ChrTalk(    #23
        0x8,
        (
            "Do you know about the four massive\x01",
            "towers that exist in the Liberl\x01",
            "Kingdom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "They're really old and it was written\x01",
            "in a book that they might be somehow\x01",
            "related to an ancient civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "Things from ancient civilizations\x01",
            "sure do grab the imagination,\x01",
            "don't they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_BC7")

    OP_A2(0x0)

    ChrTalk(    #26
        0x8,
        (
            "Phew...I finally found the book\x01",
            "I was looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "I wonder why it was shelved with\x01",
            "Pat's books.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C35")

    Jump("loc_FDF")

    label("loc_C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_E53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1D")
    OP_A2(0x29B)

    ChrTalk(    #28
        0x8,
        (
            "Thanks to the airliners in recent\x01",
            "days, even Rolent has been able\x01",
            "to get a good selection of books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "And thanks to that, I find myself\x01",
            "compelled to buy a new one each\x01",
            "time I head to the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "But I get yelled at by my wife for\x01",
            "gettin' so many...so maybe I should\x01",
            "cut back a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "I've only got the first chapter of this\x01",
            "novel, so if you want I'll give it to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x212, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #32
        "\x07\x00Received \x07\x02Carnelia - Chapter 1\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_E50")

    label("loc_E1D")


    ChrTalk(    #33
        0x8,
        (
            "I just can't find the book\x01",
            "I'm looking for...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E50")

    Jump("loc_FDF")

    label("loc_E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7B")
    OP_A2(0x0)

    ChrTalk(    #34
        0x8,
        (
            "'Glory of the Kingdom'...'Compendium of Orbment\x01",
            "Technology'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "'Guide to the Rolent Region'...'The Septian Church and\x01",
            "the Bracer Guild'...\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "I wonder where that book I just bought the\x01",
            "other day went...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "It looks like I'm going to have to put these\x01",
            "books in order.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDF")

    label("loc_F7B")


    ChrTalk(    #38
        0x8,
        (
            "And, what do we have here...\x01",
            "'The Joy of Cooking Monsters'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        "Hmm... Did I really buy this?\x02",
    )

    CloseMessageWindow()

    label("loc_FDF")

    TalkEnd(0x8)
    Return()

    # Function_6_2CC end

    def Function_7_FE3(): pass

    label("Function_7_FE3")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_106B")

    ChrTalk(    #40
        0xFE,
        (
            "Recently, even my husband has been\x01",
            "talking with Pat about a lot of things. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "We've finally become a close family.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18FC")

    label("loc_106B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_11EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1197")
    OP_A2(0x2)

    ChrTalk(    #42
        0xFE,
        (
            "The bracers who helped Pat seem\x01",
            "to be active recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I heard they were a pair of young\x01",
            "bracers, a boy and a girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "That boy is especially well spoken\x01",
            "of by the wives' circle as being quite\x01",
            "the cutie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#009F(Joshua's a hunk to all these\x01",
            "desperate housewives?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11EB")

    label("loc_1197")


    ChrTalk(    #46
        0xFE,
        (
            "Thanks to a number of well-known\x01",
            "bracers in Rolent, we can live free\x01",
            "of worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EB")

    Jump("loc_18FC")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D2")
    OP_A2(0x2)

    ChrTalk(    #47
        0xFE,
        (
            "Pat is good friends with a girl\x01",
            "named Yuni...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Her father always comes to see her\x01",
            "off and pick her up from Sunday\x01",
            "School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I'm a bit jealous of their good relationship\x01",
            "between parent and child.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1321")

    label("loc_12D2")


    ChrTalk(    #50
        0xFE,
        "Maybe I should go pick up Pat, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "But, I wonder if he'd hate it...\x02",
    )

    CloseMessageWindow()

    label("loc_1321")

    Jump("loc_18FC")

    label("loc_1324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CC")
    OP_A2(0x2)

    ChrTalk(    #52
        0xFE,
        (
            "I wonder what my son, Pat, wants\x01",
            "to be in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Unlike Luke, who wants to be a bracer,\x01",
            "I want him to pick a safe and stable job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FE")

    label("loc_13CC")


    ChrTalk(    #54
        0xFE,
        (
            "I want my son to pick a safe\x01",
            "and stable job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FE")

    Jump("loc_18FC")

    label("loc_1401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_155A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1522")
    OP_A2(0x2)

    ChrTalk(    #55
        0xFE,
        (
            "Yesterday, my husband, Pat and I,\x01",
            "managed to hold a conversation\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "My husband gave Pat a good\x01",
            "scolding and well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Pat's always been a reasonable child,\x01",
            "so he saw the error of his ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I wonder if it was a great opportunity\x01",
            "for all of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1557")

    label("loc_1522")


    ChrTalk(    #59
        0xFE,
        (
            "Our family has finally taken one \x01",
            "step forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1557")

    Jump("loc_18FC")

    label("loc_155A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_16A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1658")
    OP_A2(0x2)

    ChrTalk(    #60
        0x9,
        (
            "Of all the things Pat could have done,\x01",
            "he ran off outside of town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "Even after I told him so many times\x01",
            "how dangerous it is because of\x01",
            "roaming monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "I'm going to have to have my husband\x01",
            "give him a talking to later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169D")

    label("loc_1658")


    ChrTalk(    #63
        0x9,
        (
            "Maybe this family really needs to\x01",
            "sit down and talk things out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_169D")

    Jump("loc_18FC")

    label("loc_16A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_17F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174C")
    OP_A2(0x2)

    ChrTalk(    #64
        0x9,
        (
            "My son, Pat, has been gone\x01",
            "since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "I hope he's not getting into any\x01",
            "trouble with Luke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        "I'm worried about what he's up to...\x02",
    )

    CloseMessageWindow()
    Jump("loc_17F2")

    label("loc_174C")


    ChrTalk(    #67
        0x9,
        (
            "In any case, what is my husband\x01",
            "doing up in his room without giving\x01",
            "any attention to his own son...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "Oh, Aidios...our family is in danger\x01",
            "of falling apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F2")

    Jump("loc_18FC")

    label("loc_17F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1889")
    OP_A2(0x2)

    ChrTalk(    #69
        0x9,
        "*cough cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "Unbelievable! My husband knocked over his\x01",
            "bookshelves again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "The room is now so dusty I can't\x01",
            "go inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18FC")

    label("loc_1889")


    ChrTalk(    #72
        0x9,
        (
            "Unbelievable! My husband knocked over his\x01",
            "bookshelves again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "The room is now so dusty I can't\x01",
            "go inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FC")

    TalkEnd(0x9)
    Return()

    # Function_7_FE3 end

    def Function_8_1900(): pass

    label("Function_8_1900")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_196D")

    ChrTalk(    #74
        0xFE,
        (
            "I didn't realize it until now, but\x01",
            "my dad knows a lot of stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Adults are amazing...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B18")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A88")
    OP_A2(0x5)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #76
        0xC,
        (
            "Thanks for saving us today,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xC,
        (
            "I wonder what would have happened\x01",
            "to us if you and Joshua hadn't come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        (
            "Luke might grumble and say some,\x01",
            "mean things, but I'm sure he's really\x01",
            "grateful to you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xC,
        (
            "Please don't get too angry\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B18")

    label("loc_1A88")


    ChrTalk(    #80
        0xC,
        (
            "Luke might grumble and say some,\x01",
            "mean things, but I'm sure he's really\x01",
            "grateful to you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xC,
        (
            "Please don't get too angry\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B18")

    TalkEnd(0xC)
    Return()

    # Function_8_1900 end

    def Function_9_1B1C(): pass

    label("Function_9_1B1C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1BEB")

    ChrTalk(    #82
        0xFE,
        (
            "My son, Ashton, hardly ever comes\x01",
            "home from his job at the checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "And my grandson, Luke, is always\x01",
            "off playing somewhere, every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "It all makes me feel a tad bit lonely...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_1BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1C9D")

    ChrTalk(    #85
        0xFE,
        (
            "Though they're complete opposites,\x01",
            "my grandson, Luke, appears to get\x01",
            "along well with his neighbor, Pat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "I wish Luke would pick up a few\x01",
            "good things from Pat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_1C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1D4F")

    ChrTalk(    #87
        0xFE,
        (
            "It's rather unusual for Luke, but it seems\x01",
            "that he went to Sunday School like he\x01",
            "was supposed to the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "I wonder if there was something\x01",
            "fun going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_1D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E45")
    OP_A2(0x3)

    ChrTalk(    #89
        0xFE,
        "My boy is a soldier in the Royal Army.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "He was posted in the Royal City before,\x01",
            "but now he's assigned to security at the\x01",
            "Verte Checkpoint to the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "When he gets back, I want him to give\x01",
            "Luke a good scolding.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E8A")

    label("loc_1E45")


    ChrTalk(    #92
        0xFE,
        (
            "When my son gets back, I want him\x01",
            "to give Luke a good scolding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E8A")

    Jump("loc_2336")

    label("loc_1E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1F01")

    ChrTalk(    #93
        0xFE,
        "Luke took off today in a big rush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I wonder if he's really learned his\x01",
            "lesson from last time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_1F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_20B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2010")
    OP_A2(0x3)

    ChrTalk(    #95
        0xA,
        (
            "Luke is naughty as all get out\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "Just when I thought he was late\x01",
            "getting home, it turns out he ran\x01",
            "off to the Esmelas Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "It's a good thing those bracers went\x01",
            "after him like they did or who knows\x01",
            "what might have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20AF")

    label("loc_2010")


    ChrTalk(    #98
        0xA,
        (
            "I wonder if this is my punishment\x01",
            "for spoiling the boy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "After you leave, I think it'd be\x01",
            "best if I sat down and had a\x01",
            "good, long talk with my son.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AF")

    Jump("loc_2336")

    label("loc_20B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B9")
    OP_A2(0x3)

    ChrTalk(    #100
        0xA,
        (
            "Just when I thought Luke had come\x01",
            "home, he took off out the door again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "I told the boy that dinner was almost\x01",
            "ready, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "That boy is always running around\x01",
            "like his pants are on fire! He just\x01",
            "can't sit still for two minutes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2272")

    label("loc_21B9")


    ChrTalk(    #103
        0xA,
        (
            "Just when I thought Luke had come\x01",
            "home, he took off out the door again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "That boy is always running around\x01",
            "like his pants are on fire! He just\x01",
            "can't sit still for two minutes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2272")

    Jump("loc_2336")

    label("loc_2275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E5")
    OP_A2(0x3)

    ChrTalk(    #105
        0xA,
        "That boy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        "Where could Luke have gone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        (
            "He took off without a bite\x01",
            "of breakfast...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_22E5")


    ChrTalk(    #108
        0xA,
        "Where could Luke have gone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "He took off without a bite\x01",
            "of breakfast...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2336")

    TalkEnd(0xA)
    Return()

    # Function_9_1B1C end

    def Function_10_233A(): pass

    label("Function_10_233A")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240E")
    OP_A2(0x4)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #110
        0xB,
        "H-Hmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "I just wanted to say I'm grateful\x01",
            "that you saved us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xB,
        "And...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        (
            "I hate to admit it, but...you were\x01",
            "pretty cool, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xB,
        "Not as cool as your dad, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_244A")

    label("loc_240E")


    ChrTalk(    #115
        0xB,
        "I've made up my mind!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xB,
        "I'm gonna be a bracer, too!\x02",
    )

    CloseMessageWindow()

    label("loc_244A")

    TalkEnd(0xB)
    Return()

    # Function_10_233A end

    def Function_11_244E(): pass

    label("Function_11_244E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #117
        (
            "\x07\x05There's a notebook sitting on top\x01",
            "of the desk.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read]\x01",       # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2501")
    OP_B9(0x376, 0x0)

    label("loc_2501")

    TalkEnd(0xFF)
    Return()

    # Function_11_244E end

    SaveToFile()

Try(main)
