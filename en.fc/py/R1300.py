from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1300   ._SN',
        MapName             = 'Bose',
        Location            = 'R1300.x',
        MapIndex            = 57,
        MapDefaultBGM       = "ed60022",
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
        'Royal Army Soldier',                   # 9
        'Royal Army Soldier',                   # 10
        'East Bose Highway',                    # 11
        'Haken Gate',                           # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
    )

    DeclEntryPoint(
        Unknown_00              = -207000,
        Unknown_04              = 0,
        Unknown_08              = -154000,
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
        Unknown_30              = 312,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 57,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT09/CH10370 ._CH',             # 01
        'ED6_DT09/CH10371 ._CH',             # 02
        'ED6_DT09/CH10360 ._CH',             # 03
        'ED6_DT09/CH10361 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT09/CH10370P._CP',             # 01
        'ED6_DT09/CH10371P._CP',             # 02
        'ED6_DT09/CH10360P._CP',             # 03
        'ED6_DT09/CH10361P._CP',             # 04
    )

    DeclNpc(
        X                   = -209600,
        Z                   = 20,
        Y                   = -150000,
        Direction           = 180,
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
        X                   = -206360,
        Z                   = 10,
        Y                   = -150000,
        Direction           = 180,
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
        X                   = -207930,
        Z                   = -20,
        Y                   = -167750,
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
        X                   = -204120,
        Z                   = -200,
        Y                   = 1430,
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


    DeclMonster(
        X                   = -218580,
        Z                   = -40,
        Y                   = -112680,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x107,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -226560,
        Z                   = -30,
        Y                   = -88140,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x108,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -200780,
        Z                   = -20,
        Y                   = -50350,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x108,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -194620,
        Z                   = -30,
        Y                   = -34740,
        Unknown_0C          = 0,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x10B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -211700,
        Y                   = -2000,
        Z                   = -151630,
        Range               = -202854,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFDAA58,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_218",          # 02, 2
        "Function_3_22E",          # 03, 3
        "Function_4_2A1",          # 04, 4
        "Function_5_321",          # 05, 5
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1F3")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_1F3")

    Return()

    # Function_0_1E2 end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    OP_16(0x2, 0xFA0, 0xFFFADF80, 0xFFFCCBB0, 0x30013)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_217")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)

    label("loc_217")

    Return()

    # Function_1_1F4 end

    def Function_2_218(): pass

    label("Function_2_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_218")

    label("loc_22D")

    Return()

    # Function_2_218 end

    def Function_3_22E(): pass

    label("Function_3_22E")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        (
            "Well, if it's a request from the mayor,\x01",
            "then that's a different story. Be quick\x01",
            "about your business.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_22E end

    def Function_4_2A1(): pass

    label("Function_4_2A1")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        (
            "The Haken Gate sits on the international\x01",
            "border we share with the Empire. Make\x01",
            "sure you don't cause any problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_2A1 end

    def Function_5_321(): pass

    label("Function_5_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_32B")
    Jump("loc_E55")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_8C9")
    EventBegin(0x0)
    OP_4A(0x8, 0)
    OP_4A(0x9, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x9, 0x101, 400)
    OP_A2(0x30C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")

    ChrTalk(    #2
        0x8,
        "Hold it right there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "The Haken Gate is currently not\x01",
            "permitting civilian passage through\x01",
            "the checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "Unauthorized personnel are not\x01",
            "allowed past this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#006FSorry to make you waste your breath,\x01",
            "but we ARE authorized to be here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_521")

    label("loc_48C")


    ChrTalk(    #6
        0x8,
        "And you are?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "Wait...weren't you with the Bracer\x01",
            "Guild...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#006FHeh heh...\x01",
            "Too bad, not today.\x02\x03",

            "Today we're here on official business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_521")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Estelle produced Mayor Maybelle's Letter with a flourish.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #10
        0x8,
        "This is Mayor Maybelle's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#010FThe mayor has requested that we come\x01",
            "and speak with General Morgan about\x01",
            "the status of the search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x103,
        (
            "#020FAs you can see, this document is\x01",
            "official.\x02\x03",

            "But if you don't want to let us through,\x01",
            "I'm sure you'll be hating life later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "I guess there's nothing we can do\x01",
            "but let you through.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #15
        0x9,
        "Are you serious about this?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #16
        0x8,
        (
            "Don't you know? Mayor Maybelle is\x01",
            "the one in charge over the entire\x01",
            "region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "You can't just ignore that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        "I guess you're right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 400)

    ChrTalk(    #19
        0x9,
        "...All right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #20
        0x9,
        (
            "We'll grant you permission to pass,\x01",
            "but make sure you don't cause any\x01",
            "problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "Whatever happens, never forget that\x01",
            "we share a border with the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#006FYeah, yeah, we got it already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        "#020FAll right then, let us through.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 0)
    OP_8C(0x9, 180, 400)
    OP_4B(0x9, 0)
    EventEnd(0x1)
    Jump("loc_E55")

    label("loc_8C9")

    EventBegin(0x0)

    def lambda_8D1():
        OP_6D(-207880, 40, -151960, 1000)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8D1)
    OP_4A(0x8, 0)
    OP_4A(0x9, 0)
    OP_8B(0x0, 0xFFFCD3F8, 0xFFFDAE68, 0x0)
    OP_8B(0x1, 0xFFFCD3F8, 0xFFFDAE68, 0x0)
    OP_8B(0x2, 0xFFFCD3F8, 0xFFFDAE68, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D92")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 400)
    TurnDirection(0x9, 0x0, 400)
    OP_A2(0x306)

    ChrTalk(    #24
        0x8,
        "Hold it right there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "The Haken Gate is currently not\x01",
            "permitting civilian passage through\x01",
            "the checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        (
            "Unauthorized personnel are not\x01",
            "allowed past this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#009FCome on, it'll be all right if you\x01",
            "let us through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        "No, it's not all right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "The border garrison is putting all\x01",
            "of its efforts into searching for\x01",
            "the missing airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "We will not allow anything or ANYONE\x01",
            "to hinder the search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        (
            "#020FWe've no intention to do anything\x01",
            "of the sort.\x02\x03",

            "We're bracers. So are you trying to\x01",
            "tell us we can't pass either?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        "Bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "I can see that you're a bracer...\x01",
            "but are you trying to tell me that\x01",
            "these kids are, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#502FHeh heh heh, that's right! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#010FSee the emblems?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        "I-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "But I'm sorry to inform you that\x01",
            "even bracers are no exception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "You heard the man. Now how\x01",
            "about you move on out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#009FGrrrr...\x01",
            "I bet I could change their tune\x01",
            "with a little help from my staff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#010FForget it, Estelle. They wouldn't be\x01",
            "much use to us unconscious either.\x02\x03",

            "Anyway, let's hurry to Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E24")

    label("loc_D92")

    TurnDirection(0x8, 0x0, 400)
    TurnDirection(0x9, 0x0, 400)

    ChrTalk(    #41
        0x9,
        (
            "Look, how many times do I have\x01",
            "to tell you? You can't pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "Sorry, but you're going to have\x01",
            "to try again some other time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E24")

    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 0)
    OP_8C(0x9, 180, 0)
    OP_4B(0x9, 0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_E55")

    Return()

    # Function_5_321 end

    SaveToFile()

Try(main)
