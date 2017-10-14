from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4101_2 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4101.x',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AF",           # 01, 1
        "Function_2_1BEF",         # 02, 2
        "Function_3_2824",         # 03, 3
        "Function_4_2A7C",         # 04, 4
        "Function_5_2B77",         # 05, 5
        "Function_6_4080",         # 06, 6
        "Function_7_57BB",         # 07, 7
        "Function_8_5D12",         # 08, 8
        "Function_9_62AB",         # 09, 9
        "Function_10_6934",        # 0A, 10
        "Function_11_6D40",        # 0B, 11
        "Function_12_70DB",        # 0C, 12
        "Function_13_7E44",        # 0D, 13
        "Function_14_8495",        # 0E, 14
        "Function_15_8E0F",        # 0F, 15
        "Function_16_9111",        # 10, 16
        "Function_17_930E",        # 11, 17
        "Function_18_9E0B",        # 12, 18
        "Function_19_A108",        # 13, 19
        "Function_20_A862",        # 14, 20
        "Function_21_B017",        # 15, 21
        "Function_22_B4A5",        # 16, 22
        "Function_23_B718",        # 17, 23
        "Function_24_B9EF",        # 18, 24
        "Function_25_BCB2",        # 19, 25
        "Function_26_BD65",        # 1A, 26
        "Function_27_BE4F",        # 1B, 27
        "Function_28_BFC7",        # 1C, 28
        "Function_29_C00A",        # 1D, 29
        "Function_30_C069",        # 1E, 30
        "Function_31_C0A6",        # 1F, 31
        "Function_32_C0EB",        # 20, 32
        "Function_33_C15F",        # 21, 33
        "Function_34_C18B",        # 22, 34
        "Function_35_C1E1",        # 23, 35
        "Function_36_C20B",        # 24, 36
        "Function_37_C242",        # 25, 37
        "Function_38_C2F3",        # 26, 38
        "Function_39_C367",        # 27, 39
        "Function_40_C3B5",        # 28, 40
        "Function_41_C423",        # 29, 41
        "Function_42_C46F",        # 2A, 42
        "Function_43_C499",        # 2B, 43
        "Function_44_C553",        # 2C, 44
        "Function_45_C5E0",        # 2D, 45
        "Function_46_C69A",        # 2E, 46
        "Function_47_C6D6",        # 2F, 47
        "Function_48_C727",        # 30, 48
        "Function_49_C77B",        # 31, 49
        "Function_50_C7CF",        # 32, 50
        "Function_51_C837",        # 33, 51
        "Function_52_C915",        # 34, 52
        "Function_53_C93E",        # 35, 53
        "Function_54_C985",        # 36, 54
        "Function_55_CA37",        # 37, 55
        "Function_56_CABD",        # 38, 56
        "Function_57_CB0D",        # 39, 57
        "Function_58_CB34",        # 3A, 58
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Call(2, 1)
    Return()

    # Function_0_AA end

    def Function_1_AF(): pass

    label("Function_1_AF")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B13")
    OP_A2(0x61A)
    OP_28(0x47, 0x1, 0x4)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(108440, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x108, 107670, 1250, 24030, 135)
    SetChrPos(0x101, 107510, 1250, 23130, 90)
    SetChrPos(0x102, 107680, 1250, 22250, 45)
    SetChrPos(0x104, 106450, 1250, 22690, 90)
    TurnDirection(0xA, 0x108, 0)
    OP_0D()

    ChrTalk(    #0
        0x108,
        "#070FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        "#4POh, Zin! Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xA,
        (
            "#4PDo you feel ready for\x01",
            "the next match at noon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x108,
        (
            "#071FI do. And I'd like to\x01",
            "finish my registration,\x01",
            "if I may.\x02\x03",

            "Can you help me with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        "#4PAbsolutely, I can!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        (
            "#4PWhen I first heard the news, I'd\x01",
            "thought to myself, how is he going\x01",
            "to fight all by himself...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #6
        0xA,
        (
            "...Hey, wait a minute...\x01",
            "Aren't you the ones...\x01",
            "from yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#008FHeh. How's it going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#010FWe'd like to register for\x01",
            "the tournament, as auxiliary\x01",
            "members of Zin's team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        "Would you, now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "Then we'll need you to fill\x01",
            "out these forms, please.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05Estelle, Joshua and Olivier filled out the required paperwork. Next to his\x01",
            "signature, Olivier detailed a red rose--for 'flavor.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #12
        0xA,
        (
            "So, you two are members\x01",
            "of the Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "But...according to your \x01",
            "profile, sir...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        (
            "'Wandering lyric, troubadour\x01",
            "extraordinaire.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        (
            "'Ambassador of peace and\x01",
            "hearts most faire.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "...And there's a note under\x01",
            "it: 'Trill the extra e, and\x01",
            "don't spare the spittle'...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        (
            "#031FHa ha ha! My dear, you need\x01",
            "not bother with that post-script;\x01",
            "your diction sings!\x02\x03",

            "#030FIf you wish to know more, however,\x01",
            "I'd be happy to teach you the proper\x01",
            "reading...perhaps, over tea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#509FYeeeeah... That's enough of that,\x01",
            "thanks. You can just burn that\x01",
            "application. With fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#010FNot literally, of course.\x01",
            "Thank you for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xA,
        "You're very...welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "I've finalized your team \x01",
            "register for the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "I list Zin as team captain, with 3 auxiliary\x01",
            "members: Estelle, Joshua and Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "Please remember there can be\x01",
            "no changes or substitutions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x108,
        "#070FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#006FFeels like it's all about\x01",
            "to break loose, doesn't it?\x02\x03",

            "Oh yeah. Do we know who our\x01",
            "opponents are going to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        (
            "We have already determined the pairings, but to\x01",
            "discourage wagering, we do not announce them\x01",
            "until just before the match is to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "You can guess your opponents just prior\x01",
            "to the match, though, by taking note of\x01",
            "who else is sharing your ready room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#010FAh, so opposing teams are\x01",
            "kept in opposing rooms,\x01",
            "I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        "That's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "Here. This is for you\x01",
            "and your teammates.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x372, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #31
        (
            "\x07\x00You received the \x01",
            "\x07\x02Registry Card\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #32
        0xA,
        (
            "Please show that to\x01",
            "the staff before you \x01",
            "enter the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "And, that should just about cover\x01",
            "everything. Best of luck to you\x01",
            "all! Knock 'em dead!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1BEB")

    label("loc_B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 2)), scpexpr(EXPR_END)), "loc_C00")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(109490, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 107600, 1250, 23440, 90)
    SetChrPos(0x102, 107500, 1250, 22630, 90)
    TurnDirection(0xA, 0x101, 0)
    OP_6C(90000, 0)
    OP_0D()

    ChrTalk(    #34
        0xA,
        (
            "Welcome to the Grand Arena. \x01",
            "Would you like a ticket?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        "Tickets are 1000 mira per pair.\x02",
    )

    CloseMessageWindow()
    Jump("loc_102C")

    label("loc_C00")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(109490, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 107600, 1250, 23440, 90)
    SetChrPos(0x102, 107500, 1250, 22630, 90)
    TurnDirection(0xA, 0x101, 0)
    OP_6C(90000, 0)
    OP_0D()
    OP_A2(0x672)

    ChrTalk(    #36
        0xA,
        (
            "Welcome to the Grand Arena. \x01",
            "Would you like a ticket?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDF")

    ChrTalk(    #37
        0x101,
        "#006FYes. Two please.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CFB")

    label("loc_CDF")


    ChrTalk(    #38
        0x102,
        "#010FThank you, ma'am.\x02",
    )

    CloseMessageWindow()

    label("loc_CFB")


    ChrTalk(    #39
        0xA,
        (
            "Preliminaries are in progress right now,\x01",
            "but the main event will last for three\x01",
            "days, starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "For which day would you\x01",
            "like your ticket?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#505FUhh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#014FActually, we were hoping to catch\x01",
            "the preliminary matches, if we\x01",
            "could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        "Oh, all right, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        (
            "They're already more than\x01",
            "halfway finished, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        "Will that be a problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#006FNope, no problem at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "Okay. Bad value, but\x01",
            "hey, not my money!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xA,
        "That'll be 1000 mira.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#004FWow. That's a lot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x102,
        (
            "#014FI had heard that there was\x01",
            "some kind of discount for\x01",
            "the birthday celebration...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        "I'm sorry, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        (
            "This year there have been some...\x01",
            "complications...that have made it\x01",
            "impossible for us to offer discounts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#501FOh, okay. That's pretty sucky.\x01",
            "But, what can you do?\x02\x03",

            "Let's see... 900, 950...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102C")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Pay 1000 mira]\x01",      # 0
            "[Don't pay]\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1099"),
        (1, "loc_1205"),
        (SWITCH_DEFAULT, "loc_123E"),
    )


    label("loc_1099")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B3")
    OP_22(0x14, 0x0, 0x64)
    OP_4F(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #54
        0xA,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        "Here are your tickets.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #56
        "\x07\x00Received two \x07\x02Grand Arena Tickets\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x36B, 2)
    OP_A2(0x60C)
    OP_A2(0x60C)
    OP_28(0x45, 0x1, 0x800)

    ChrTalk(    #57
        0xA,
        (
            "The entrance to the arena is\x01",
            "directly to your left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        "Show your tickets at the gate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1200")

    label("loc_11B3")


    ChrTalk(    #59
        0x101,
        "#004F(Crap...I don't have enough.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        "#017F(We'll have to come back.)\x02",
    )

    CloseMessageWindow()

    label("loc_1200")

    EventEnd(0x0)
    Jump("loc_123E")

    label("loc_1205")


    ChrTalk(    #61
        0xA,
        (
            "Thank you. We look forward\x01",
            "to your next visit.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_123E")

    label("loc_123E")

    Jump("loc_1BEB")

    label("loc_1241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1380")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_12C2")

    ChrTalk(    #62
        0xA,
        (
            "Everyone looks so happy\x01",
            "out on the streets today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "The queen's charisma is quite\x01",
            "a positive influence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137D")

    label("loc_12C2")

    OP_A2(0x18)

    ChrTalk(    #64
        0xA,
        (
            "I'm so glad the birthday\x01",
            "celebration is off to such\x01",
            "a great start!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xA,
        (
            "Everyone looks so happy\x01",
            "out on the streets today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "The queen's charisma is quite\x01",
            "a positive influence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137D")

    Jump("loc_1BEB")

    label("loc_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1402")
    TurnDirection(0xA, 0x108, 400)

    ChrTalk(    #67
        0xA,
        (
            "Well, if it isn't Joshua and\x01",
            "Zin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "...What's the matter? You two\x01",
            "look troubled. Something on\x01",
            "your mind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_1402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_148C")

    ChrTalk(    #69
        0xA,
        (
            "Well, the Martial Arts Competition went off\x01",
            "without a hitch, but I'm still a bit worried\x01",
            "about the birthday celebration...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_148C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_160A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_1526")

    ChrTalk(    #70
        0xA,
        (
            "Congratulations on your stunning\x01",
            "victory! Goooo team!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "Hope you enjoy the dinner\x01",
            "party--it promises some\x01",
            "serious deliciousness!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1607")

    label("loc_1526")

    OP_A2(0x18)

    ChrTalk(    #72
        0xA,
        (
            "Congratulations on your stunning\x01",
            "victory! Goooo team!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "I wasn't able to see your match,\x01",
            "but I heard it was a heck of a\x01",
            "thing to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "Hope you enjoy the dinner\x01",
            "party--it promises some\x01",
            "serious deliciousness!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1607")

    Jump("loc_1BEB")

    label("loc_160A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_169D")

    ChrTalk(    #75
        0xA,
        (
            "It's almost time for the\x01",
            "championship match to start.\x01",
            "Are you nervous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "When you're ready, please\x01",
            "proceed to the entrance gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_169D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_1700")

    ChrTalk(    #77
        0xA,
        (
            "*giggle* It seems you've\x01",
            "amassed quite a following!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        "Good luck tomorrow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1794")

    label("loc_1700")

    OP_A2(0x18)

    ChrTalk(    #79
        0xA,
        (
            "Well, you guys, tomorrow is\x01",
            "the final match! You nervous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        (
            "*giggle* It seems you've\x01",
            "amassed quite a following!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        "Good luck tomorrow.\x02",
    )

    CloseMessageWindow()

    label("loc_1794")

    Jump("loc_1BEB")

    label("loc_1797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1806")
    TurnDirection(0xA, 0x108, 400)

    ChrTalk(    #82
        0xA,
        "Zin, it's time for Round 2.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "When you're ready, please\x01",
            "proceed to the entrance gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_1806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1893")

    ChrTalk(    #84
        0xA,
        (
            "Congratulations on clearing\x01",
            "Round 1!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        (
            "Tomorrow's match is in the\x01",
            "afternoon as well, so please\x01",
            "make sure you arrive early.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_1893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1923")

    ChrTalk(    #86
        0xA,
        (
            "If you show your Registry\x01",
            "Card at the entrance, the\x01",
            "staff will show you in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "That should cover everything.\x01",
            "Luck be with you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_1923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_19F3")

    ChrTalk(    #88
        0xA,
        (
            "The first round of the \x01",
            "competition will begin\x01",
            "tomorrow afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "There are no reserved seats, so please take\x01",
            "the first available seat you find, for the\x01",
            "convenience of the other patrons.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_19F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1BEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_END)), "loc_1A61")

    ChrTalk(    #90
        0xA,
        (
            "The entrance to the arena is\x01",
            "directly to your left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        "Show your tickets at the gate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_1A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_1AB6")

    ChrTalk(    #92
        0xA,
        (
            "If you have your ticket, \x01",
            "please make your way to\x01",
            "the front entrance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_1AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_1B43")

    ChrTalk(    #93
        0xA,
        (
            "There's still some time before\x01",
            "the match begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "Please feel free to wait in line\x01",
            "with the other spectators if you\x01",
            "wish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_1B43")

    OP_A2(0x18)

    ChrTalk(    #95
        0xA,
        "Welcome to the Grand Arena. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "There's still some time before\x01",
            "the match begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "Please feel free to wait in line\x01",
            "with the other spectators if you\x01",
            "wish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEB")

    TalkEnd(0xA)
    Return()

    # Function_1_AF end

    def Function_2_1BEF(): pass

    label("Function_2_1BEF")

    TalkBegin(0xB)
    OP_8C(0xB, 270, 0)
    SetChrSubChip(0xB, 0)
    EventBegin(0x0)
    Fade(1500)

    def lambda_1C0B():
        OP_6D(108230, 1250, 32820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C0B)

    def lambda_1C23():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C23)
    SetChrPos(0x101, 107830, 1250, 33580, 90)
    SetChrPos(0x102, 107750, 1250, 32470, 90)
    OP_8C(0xB, 270, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C75")
    SetChrPos(0x108, 106450, 1250, 32450, 90)

    label("loc_1C75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C94")
    SetChrPos(0x104, 106450, 1250, 33600, 90)

    label("loc_1C94")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F33")

    ChrTalk(    #98
        0xB,
        (
            "Welcome, everyone, \x01",
            "to the Grand Arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xB,
        (
            "Please note that tournament participants\x01",
            "are asked to remain within the arena's\x01",
            "walls until the end of the day's matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xB,
        (
            "Have you made all the necessary\x01",
            "preparations for a day of hot,\x01",
            "hot action?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Bring it on!]\x01",       # 0
            "[Not quite yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E0D"),
        (1, "loc_1EA9"),
        (SWITCH_DEFAULT, "loc_1F30"),
    )


    label("loc_1E0D")

    OP_A2(0x631)
    OP_28(0x49, 0x1, 0x4)

    ChrTalk(    #101
        0xB,
        "Excellent, excellent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        (
            "Your waiting room is the 'Blue\x01",
            "Team Room,' just inside the hall\x01",
            "on the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        "Fight well!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x3F5)
    NewScene("ED6_DT01/T4136   ._SN", 111, 0, 0)
    IdleLoop()
    Jump("loc_1F30")

    label("loc_1EA9")


    ChrTalk(    #104
        0xB,
        (
            "I understand. These things\x01",
            "take time, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xB,
        (
            "And there IS still time before\x01",
            "the match begins...so try to\x01",
            "relax, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F30")

    label("loc_1F30")

    Jump("loc_281E")

    label("loc_1F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21CE")

    ChrTalk(    #106
        0xB,
        (
            "Master Zin! Welcome\x01",
            "to the Grand Arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xB,
        (
            "Please note that tournament participants\x01",
            "are asked to remain within the arena's\x01",
            "walls until the end of the day's matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xB,
        (
            "Have you made all the necessary\x01",
            "preparations for a day of hot,\x01",
            "hot action?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Bring it on!]\x01",       # 0
            "[Not quite yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20AB"),
        (1, "loc_2144"),
        (SWITCH_DEFAULT, "loc_21CB"),
    )


    label("loc_20AB")

    OP_A2(0x623)
    OP_28(0x48, 0x1, 0x4)

    ChrTalk(    #109
        0xB,
        "Excellent, excellent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xB,
        (
            "Your waiting room is the 'Blue\x01",
            "Team Room,' just inside the hall\x01",
            "on the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        "Fight well!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_21CB")

    label("loc_2144")


    ChrTalk(    #112
        0xB,
        (
            "I understand. These things\x01",
            "take time, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        (
            "And there IS still time before\x01",
            "the match begins...so try to\x01",
            "relax, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CB")

    label("loc_21CB")

    Jump("loc_281E")

    label("loc_21CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2479")

    ChrTalk(    #114
        0xB,
        (
            "Your card, please... Ah, part\x01",
            "of the tournament, I see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        (
            "Please note that tournament participants\x01",
            "are asked to remain within the arena's\x01",
            "walls until the end of the day's matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xB,
        (
            "Have you made all the necessary\x01",
            "preparations for a day of hot,\x01",
            "hot action?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Bring it on!]\x01",       # 0
            "[Not quite yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2356"),
        (1, "loc_23EF"),
        (SWITCH_DEFAULT, "loc_2476"),
    )


    label("loc_2356")

    OP_A2(0x61B)
    OP_28(0x47, 0x1, 0x8)

    ChrTalk(    #117
        0xB,
        "Excellent, excellent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xB,
        (
            "Your waiting room is the 'Blue\x01",
            "Team Room,' just inside the hall\x01",
            "on the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xB,
        "Fight well!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2476")

    label("loc_23EF")


    ChrTalk(    #120
        0xB,
        (
            "I understand. These things\x01",
            "take time, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xB,
        (
            "And there IS still time before\x01",
            "the match begins...so try to\x01",
            "relax, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2476")

    label("loc_2476")

    Jump("loc_281E")

    label("loc_2479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_256D")

    ChrTalk(    #122
        0xB,
        (
            "Currently at the arena\x01",
            "we're holding the royal\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xB,
        (
            "If you would like to\x01",
            "participate, you'll\x01",
            "need to register first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "Registration is being handled\x01",
            "at the ticket counter on the\x01",
            "right-hand side.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_281E")

    label("loc_256D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_277A")

    ChrTalk(    #125
        0xB,
        (
            "Currently at the arena we're\x01",
            "holding the preliminary matches\x01",
            "of the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xB,
        "May I see your tickets?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Show tickets]\x01",      # 0
            "[Don't show]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2666"),
        (1, "loc_272A"),
        (SWITCH_DEFAULT, "loc_2777"),
    )


    label("loc_2666")

    OP_A2(0x60D)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #127
        "\x07\x00Handed over \x07\x02Grand Arena Tickets\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x36B, 2)

    ChrTalk(    #128
        0xB,
        (
            "Thanks! Everything seems to be\x01",
            "in order. You may enter at your\x01",
            "discretion.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2777")

    label("loc_272A")


    ChrTalk(    #129
        0xB,
        "Are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xB,
        (
            "This ticket is only usable\x01",
            "for today's matches...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2777")

    label("loc_2777")

    Jump("loc_281E")

    label("loc_277A")


    ChrTalk(    #131
        0xB,
        (
            "Currently at the arena we're\x01",
            "holding the preliminary matches\x01",
            "of the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xB,
        "May I see your tickets?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        "Ticket sales are to the right.\x02",
    )

    CloseMessageWindow()

    label("loc_281E")

    EventEnd(0x0)
    TalkEnd(0xB)
    Return()

    # Function_2_1BEF end

    def Function_3_2824(): pass

    label("Function_3_2824")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2831")
    Jump("loc_2A78")

    label("loc_2831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_283B")
    Jump("loc_2A78")

    label("loc_283B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2845")
    Jump("loc_2A78")

    label("loc_2845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_284F")
    Jump("loc_2A78")

    label("loc_284F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2859")
    Jump("loc_2A78")

    label("loc_2859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2863")
    Jump("loc_2A78")

    label("loc_2863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_286D")
    Jump("loc_2A78")

    label("loc_286D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2951")

    ChrTalk(    #134
        0xFE,
        (
            "#819FThis morning at work I got\x01",
            "all tangled up with group of\x01",
            "army guys. What a mess...\x02\x03",

            "All because the terrorists were posing as\x01",
            "Bracer Guild members! Hard to believe all\x01",
            "the backlash that stunt caused...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5A")

    label("loc_2951")

    OP_A2(0x0)

    ChrTalk(    #135
        0xFE,
        (
            "#810FThis morning I had to go out\x01",
            "near the Erbe Royal Villa\x01",
            "for work...\x02\x03",

            "#819FAnd as soon as they recognized\x01",
            "us as bracers, they were all\x01",
            "over us. It was terrible!\x02\x03",

            "Hard to believe all the backlash\x01",
            "those terrorists caused by posing\x01",
            "as Bracer Guild members.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5A")

    Jump("loc_2A78")

    label("loc_2A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2A67")
    Jump("loc_2A78")

    label("loc_2A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2A71")
    Jump("loc_2A78")

    label("loc_2A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2A78")

    label("loc_2A78")

    TalkEnd(0xFE)
    Return()

    # Function_3_2824 end

    def Function_4_2A7C(): pass

    label("Function_4_2A7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2A89")
    Jump("loc_2B73")

    label("loc_2A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2A93")
    Jump("loc_2B73")

    label("loc_2A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2A9D")
    Jump("loc_2B73")

    label("loc_2A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2AA7")
    Jump("loc_2B73")

    label("loc_2AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2AB1")
    Jump("loc_2B73")

    label("loc_2AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2B44")

    ChrTalk(    #136
        0xFE,
        (
            "I want to get good seats for\x01",
            "my wife and I, so I'm camping\x01",
            "out at the front of the line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "I'm such a lovestruck son-of-a-gun...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B73")

    label("loc_2B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2B4E")
    Jump("loc_2B73")

    label("loc_2B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B58")
    Jump("loc_2B73")

    label("loc_2B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2B62")
    Jump("loc_2B73")

    label("loc_2B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2B6C")
    Jump("loc_2B73")

    label("loc_2B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2B73")

    label("loc_2B73")

    TalkEnd(0xFE)
    Return()

    # Function_4_2A7C end

    def Function_5_2B77(): pass

    label("Function_5_2B77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2E5B")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2C24")

    ChrTalk(    #138
        0xFE,
        (
            "The Erebonian embassy is just\x01",
            "up ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E58")

    label("loc_2C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D08")

    ChrTalk(    #140
        0xFE,
        (
            "Leave it to the Queen's Birthday\x01",
            "Celebration to bring out all the\x01",
            "crazies, weirdos and heroes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "And this is still just a small fraction\x01",
            "of the people you'll find in the Empire's\x01",
            "capital city. Crazy, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E58")

    label("loc_2D08")

    OP_A2(0x1)

    ChrTalk(    #142
        0xFE,
        (
            "Leave it to the Queen's Birthday\x01",
            "Celebration to bring out all the\x01",
            "crazies, weirdos and heroes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "And this is still just a small fraction\x01",
            "of the people you'll find in the Empire's\x01",
            "capital city. Crazy, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "I just can't imagine so many people\x01",
            "milling about, every single day. How\x01",
            "can a city like that even function?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E58")

    Jump("loc_407C")

    label("loc_2E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2FC5")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2F02")

    ChrTalk(    #145
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC2")

    label("loc_2F02")


    ChrTalk(    #147
        0xFE,
        (
            "Seems all the other guardsmen\x01",
            "have withdrawn from the embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "But I haven't gotten any direct\x01",
            "orders to leave my post...so\x01",
            "here I shall stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "That is my sworn duty, after all!\x02",
    )

    CloseMessageWindow()

    label("loc_2FC2")

    Jump("loc_407C")

    label("loc_2FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3119")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_306C")

    ChrTalk(    #150
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3116")

    label("loc_306C")


    ChrTalk(    #152
        0xFE,
        (
            "I've been instructed to keep\x01",
            "Olivier from leaving the\x01",
            "embassy premises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I would probably refrain from\x01",
            "acting on his behalf, too...\x01",
            "at least for the time being.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3116")

    Jump("loc_407C")

    label("loc_3119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_338A")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_31C0")

    ChrTalk(    #154
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3387")

    label("loc_31C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3273")

    ChrTalk(    #156
        0xFE,
        (
            "Mueller is the most recent\x01",
            "Imperial officer in residence\x01",
            "at the Erebonian embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "He's young, but he's a senior\x01",
            "officer with quite a bit of\x01",
            "rank and decorum.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3387")

    label("loc_3273")

    OP_A2(0x1)

    ChrTalk(    #158
        0xFE,
        (
            "Mueller is the most recent\x01",
            "Imperial officer in residence\x01",
            "at the Erebonian embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "He's young, but he's a senior\x01",
            "officer with quite a bit of\x01",
            "rank and decorum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "Olivier is, hopefully, behaving\x01",
            "himself at the embassy right now.\x01",
            "If he knows what's good for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3387")

    Jump("loc_407C")

    label("loc_338A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3609")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3431")

    ChrTalk(    #161
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3606")

    label("loc_3431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3506")
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #163
        0xFE,
        (
            "Olivier, you know that no one is\x01",
            "covering for you and all these\x01",
            "little 'walks' of yours, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "I've been ordered to report \x01",
            "you in the event of you doing\x01",
            "anything particularly asinine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3606")

    label("loc_3506")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #165
        0xFE,
        (
            "'Stepping out' again today,\x01",
            "are we, Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "Olivier, you know that no one is\x01",
            "covering for you and all these\x01",
            "little 'walks' of yours, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "I've been ordered to report \x01",
            "you in the event of you doing\x01",
            "anything particularly asinine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3606")

    Jump("loc_407C")

    label("loc_3609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_376D")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_36B0")

    ChrTalk(    #168
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_376A")

    label("loc_36B0")


    ChrTalk(    #170
        0xFE,
        (
            "I wish they'd keep people like Olivier and\x01",
            "all those embassy folks under lock and key,\x01",
            "so we could all breathe a little easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "How does he keep getting out,\x01",
            "anyway? Honestly!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376A")

    Jump("loc_407C")

    label("loc_376D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_39B8")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3814")

    ChrTalk(    #172
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B5")

    label("loc_3814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_38CF")
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #174
        0xFE,
        (
            "Olivier, please try to stop\x01",
            "doing things we have to issue\x01",
            "formal apologies for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "All of the others at your \x01",
            "embassy at least TRY to be a\x01",
            "little conscientious...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B5")

    label("loc_38CF")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #176
        0xFE,
        (
            "'Stepping out' again today,\x01",
            "are we, Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "Olivier, please try to stop\x01",
            "doing things we have to issue\x01",
            "formal apologies for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "All of the others at your \x01",
            "embassy at least TRY to be a\x01",
            "little conscientious...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B5")

    Jump("loc_407C")

    label("loc_39B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3AFB")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3A5F")

    ChrTalk(    #179
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF8")

    label("loc_3A5F")


    ChrTalk(    #181
        0xFE,
        (
            "As a Royal Army private, being in\x01",
            "the Martial Arts Competition would\x01",
            "be a tremendous honor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "If only I were given the chance \x01",
            "to participate...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF8")

    Jump("loc_407C")

    label("loc_3AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3DC9")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3BA2")

    ChrTalk(    #183
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC6")

    label("loc_3BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3C32")
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #185
        0xFE,
        (
            "Olivier... Please try to show\x01",
            "a little restraint out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "I'm sick of getting pulled into\x01",
            "your filth all the time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC6")

    label("loc_3C32")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #187
        0xFE,
        (
            "Olivier, are you headed\x01",
            "back to the embassy now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x104,
        (
            "#035FHmph. Don't be absurd!\x02\x03",

            "Look around you, at these decorated\x01",
            "villas! These smiling visages! These\x01",
            "enticing...victuals!\x02\x03",

            "#030FIt would be a crime fouler\x01",
            "than murder were I not to go\x01",
            "and partake in the merriment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "...Yes, well, please try to\x01",
            "show a little restraint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "I'm sick of getting pulled into\x01",
            "your filth all the time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC6")

    Jump("loc_407C")

    label("loc_3DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3FE1")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3E70")

    ChrTalk(    #191
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FDE")

    label("loc_3E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3EFC")

    ChrTalk(    #193
        0xFE,
        (
            "The people at the Erebonian\x01",
            "embassy are all very upscale,\x01",
            "upstanding people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "With one...notable exception,\x01",
            "of course...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FDE")

    label("loc_3EFC")

    OP_A2(0x1)

    ChrTalk(    #195
        0xFE,
        (
            "The people at the Erebonian\x01",
            "embassy are all very upscale,\x01",
            "upstanding people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "With one...notable exception,\x01",
            "of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "Every time he goes and causes\x01",
            "trouble, the parties involved\x01",
            "all come complaining to ME.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FDE")

    Jump("loc_407C")

    label("loc_3FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_407C")

    ChrTalk(    #198
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_407C")

    TalkEnd(0xFE)
    Return()

    # Function_5_2B77 end

    def Function_6_4080(): pass

    label("Function_6_4080")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_482A")
    EventBegin(0x0)
    OP_69(0x23, 0x3E8)
    OP_A2(0x612)
    OP_28(0x46, 0x1, 0x8)
    OP_28(0x46, 0x1, 0x10)

    ChrTalk(    #200
        0x23,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x23,
        "What's your business here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#000FWe're looking for a person\x01",
            "named Zin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x102,
        "#010FMay we see him, please?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x23,
        (
            "Oh, you're here to see Zin,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x23,
        (
            "Have you actually met the man?\x01",
            "First time I did, I almost peed\x01",
            "myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x23,
        (
            "I was like, holy crap! He\x01",
            "ain't a man, he's a grizzly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#001FHeh. He is a pretty big fella,\x01",
            "that's for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x23,
        (
            "But he's real friendly once\x01",
            "you start talking with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x23,
        (
            "He even gave me a meat-bun \x01",
            "when I told him I was hungry\x01",
            "during my shift one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#502FYeah, he's the kind of guy\x01",
            "you can really count on.\x01",
            "Like a big brother!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x102,
        (
            "#015FAhem! Indeed.\x02\x03",

            "#010FSo, may we see him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x23,
        "Oh, yes, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x23,
        (
            "He actually stepped out again shortly\x01",
            "after returning. Said he had some\x01",
            "business to take care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x23,
        (
            "Looking for a place to 'meditate and \x01",
            "prepare for the tournament,' or some\x01",
            "such thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        (
            "#004FMeditate, huh? Man, he's\x01",
            "not kidding around!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x102,
        (
            "#010FWhere do you think such a\x01",
            "place might be found?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x23,
        (
            "Well, when he left here,\x01",
            "he was headed for the Erbe\x01",
            "Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x23,
        (
            "That old forest path has a feeling to it\x01",
            "not unlike a park...and it being monster-\x01",
            "infested makes it a good training ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x102,
        (
            "#010FThe Erbe Scenic Route? Okay,\x01",
            "got it. Come on, Estelle,\x01",
            "let's go find him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#006FRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x23,
        (
            "Hang on. If you're going to\x01",
            "the Erbe Scenic Route, there's\x01",
            "one thing you need to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x23,
        (
            "There's a place nearby called\x01",
            "the Erbe Royal Villa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        "#002FOh, we heard about that place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        (
            "#012F...I assume you're going to tell us that\x01",
            "it's been commandeered for the anti-terror\x01",
            "division, so it's totally locked down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x23,
        "...Good guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x23,
        (
            "They can raise quite a ruckus\x01",
            "over there. Watch your backs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x23,
        (
            "Or better yet, just avoid it\x01",
            "altogether.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#505FSo they're strict, huh? Strict\x01",
            "is starting to get real old...\x02\x03",

            "#501FAvoidance sounds good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x102,
        "#010FThank you for the information.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_57B7")

    label("loc_482A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_497F")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_48B9")

    ChrTalk(    #230
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_497C")

    label("loc_48B9")


    ChrTalk(    #232
        0xFE,
        (
            "I swear, more people turn out\x01",
            "for the festivities every year.\x01",
            "It's crazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "In crowds like this I have to really\x01",
            "keep an eye out for mischief-makers,\x01",
            "and shake the fun-lovin' out of 'em.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_497C")

    Jump("loc_57B7")

    label("loc_497F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4AE2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4A0E")

    ChrTalk(    #234
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ADF")

    label("loc_4A0E")


    ChrTalk(    #236
        0xFE,
        (
            "All of the regular troops have \x01",
            "been ordered out and replaced\x01",
            "with Special Ops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "All of them but me, that is. I'm staying\x01",
            "here until I'm directly ordered to with-\x01",
            "draw. Because that's what heroes do!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ADF")

    Jump("loc_57B7")

    label("loc_4AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4C41")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4B71")

    ChrTalk(    #238
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C3E")

    label("loc_4B71")


    ChrTalk(    #240
        0xFE,
        (
            "What'll I be doing for the queen's\x01",
            "Birthday Celebration, you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "Sadly, I can't say. The ambassador can't\x01",
            "decide on his schedule, and until he does,\x01",
            "I've got to keep mine open as well. Le sigh!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C3E")

    Jump("loc_57B7")

    label("loc_4C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4EE6")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4CD0")

    ChrTalk(    #242
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EE3")

    label("loc_4CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4D59")
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #244
        0xFE,
        "Congratulations, Zin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "I was rooting for you, but even\x01",
            "I couldn't have predicted you'd \x01",
            "end up winning it all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EE3")

    label("loc_4D59")

    OP_A2(0x2)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #246
        0xFE,
        "Congratulations, Zin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "I was rooting for you, but even\x01",
            "I couldn't have predicted you'd \x01",
            "end up winning it all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "You've made us all very proud\x01",
            "here at the embassy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x108,
        (
            "#070FThank you. I actually have\x01",
            "some news for the ambassador..\x02\x03",

            "Tonight I've been invited to\x01",
            "stay at the castle, so I won't\x01",
            "be back until tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        "I'll pass along the message.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "Enjoy yourself!\x02",
    )

    CloseMessageWindow()

    label("loc_4EE3")

    Jump("loc_57B7")

    label("loc_4EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4FD4")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4F75")

    ChrTalk(    #252
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FD1")

    label("loc_4F75")


    ChrTalk(    #254
        0xFE,
        "Final round today. At long last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "I believe in you guys. Knock\x01",
            "'em dead out there!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD1")

    Jump("loc_57B7")

    label("loc_4FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_50F4")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5063")

    ChrTalk(    #256
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50F1")

    label("loc_5063")


    ChrTalk(    #258
        0xFE,
        (
            "If I didn't have to work,\x01",
            "I'd've loved to participate\x01",
            "in the tournament with Zin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "So you guys'll have to fight\x01",
            "extra hard...for me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50F1")

    Jump("loc_57B7")

    label("loc_50F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5213")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5183")

    ChrTalk(    #260
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5210")

    label("loc_5183")

    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #262
        0xFE,
        (
            "Zin, congratulations on \x01",
            "making it to day two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "I'll be cheering the loudest\x01",
            "for you, big guy, so show 'em\x01",
            "all what you got!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5210")

    Jump("loc_57B7")

    label("loc_5213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5369")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_52A2")

    ChrTalk(    #264
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5366")

    label("loc_52A2")


    ChrTalk(    #266
        0xFE,
        (
            "Zin's such a lovable bear of\x01",
            "a man, he's become something of\x01",
            "an icon at the embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "If he's got one weakness, though,\x01",
            "its his chivalry. He kinda goes\x01",
            "a bit overboard with it sometimes!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5366")

    Jump("loc_57B7")

    label("loc_5369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_55AF")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_53F8")

    ChrTalk(    #268
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55AC")

    label("loc_53F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_548B")
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #270
        0xFE,
        (
            "So, the tournament's finally\x01",
            "starting today, eh Zin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "I can't go watch, sadly, but\x01",
            "I'll be cheering you on from\x01",
            "my post!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55AC")

    label("loc_548B")

    OP_A2(0x2)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #272
        0xFE,
        (
            "So, the tournament's finally\x01",
            "starting today, eh Zin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "I can't go watch, sadly, but\x01",
            "I'll be cheering you on from\x01",
            "my post!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x108,
        (
            "#070FMuch obliged. With all the\x01",
            "helping hands I've got, I aim\x01",
            "to come out on top.\x02\x03",

            "But regardless of the outcome,\x01",
            "I shall fight without regret!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55AC")

    Jump("loc_57B7")

    label("loc_55AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5734")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_563E")

    ChrTalk(    #275
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5731")

    label("loc_563E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_END)), "loc_56B5")

    ChrTalk(    #277
        0xFE,
        (
            "I think Zin went out to the\x01",
            "Erbe Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "But if you go, be careful to\x01",
            "avoid the Royal Villa!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5731")

    label("loc_56B5")


    ChrTalk(    #279
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5731")

    Jump("loc_57B7")

    label("loc_5734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_57B7")

    ChrTalk(    #281
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57B7")

    TalkEnd(0xFE)
    Return()

    # Function_6_4080 end

    def Function_7_57BB(): pass

    label("Function_7_57BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5814")

    ChrTalk(    #283
        0xFE,
        (
            "Princess Klaudia looks\x01",
            "so beautiful today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "I wish I could be her!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_5814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5881")

    ChrTalk(    #285
        0xFE,
        (
            "Those soldiers in black sure\x01",
            "seem to be all over the place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "Is there some kind of drill?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_5881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_590C")

    ChrTalk(    #287
        0xFE,
        (
            "Hurray! Now that the Martial\x01",
            "Arts Competition is over, the\x01",
            "birthday festivities can begin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "It's going to be super-fun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_590C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_59B5")

    ChrTalk(    #289
        0xFE,
        (
            "I cheered so much, my throat's\x01",
            "all sore and bloody! Gross,\x01",
            "but AWESOME! ...Ow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "The tournament is just SO exciting!\x01",
            "I can't wait for next year's now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_59B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5A38")

    ChrTalk(    #291
        0xFE,
        (
            "Yay! The final round! Who will\x01",
            "win, and who will lose? I don't\x01",
            "even really care--just YAAAY!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        "Violence is cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_5A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5AC3")

    ChrTalk(    #293
        0xFE,
        (
            "Wow, I didn't think we'd see\x01",
            "a dark horse entry make it all\x01",
            "the way to the championship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "I can hardly believe my eyes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_5AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5B49")

    ChrTalk(    #295
        0xFE,
        (
            "No matter who's fighting whom, both matches\x01",
            "today are sure to be must-sees. Have I died\x01",
            "and gone to gladiator heaven?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_5B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5B99")

    ChrTalk(    #296
        0xFE,
        (
            "All the matches today have been\x01",
            "must-sees. It's so invigorating!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_5B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5C22")

    ChrTalk(    #297
        0xFE,
        (
            "I'm going to cheer so hard my voice will\x01",
            "ride out on the hoarse it rode in on! Makes\x01",
            "no sense? I don't care! Just YAAAAY!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_5C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5C98")

    ChrTalk(    #298
        0xFE,
        (
            "After watching the prelims, I'm totally\x01",
            "thinking that team of bracers has this\x01",
            "competition in the bag!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D0E")

    label("loc_5C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5D0E")

    ChrTalk(    #299
        0xFE,
        (
            "So, let's see... Who should I cheer for\x01",
            "this year? Maybe I'll just cheer for\x01",
            "blood! Doesn't matter whose!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D0E")

    TalkEnd(0xFE)
    Return()

    # Function_7_57BB end

    def Function_8_5D12(): pass

    label("Function_8_5D12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5D1F")
    Jump("loc_62A7")

    label("loc_5D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5D29")
    Jump("loc_62A7")

    label("loc_5D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5DAC")

    ChrTalk(    #300
        0xFE,
        (
            "Ugh. I drank way too much\x01",
            "yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "I don't even remember who\x01",
            "I was drinking with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        "Ooooh, my head...\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A7")

    label("loc_5DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5DB6")
    Jump("loc_62A7")

    label("loc_5DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5E88")

    ChrTalk(    #303
        0xFE,
        (
            "Look at all these people! I got up\x01",
            "early specifically to avoid the\x01",
            "crowds... Lot of good THAT did!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "These are the final match-ups,\x01",
            "though, so I guess I shouldn't\x01",
            "be surprised by the turnout.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62A7")

    label("loc_5E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_606E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5F29")

    ChrTalk(    #305
        0xFE,
        (
            "I don't think there were too\x01",
            "many people cheering for that\x01",
            "team of sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "Have to admit, though, they\x01",
            "put up a heck of a fight!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_606B")

    label("loc_5F29")

    OP_A2(0x4)

    ChrTalk(    #307
        0xFE,
        (
            "I don't think there were too\x01",
            "many people cheering for that\x01",
            "team of sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "Plenty of people cheering\x01",
            "AGAINST them, though, judging\x01",
            "by the din when they lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "Have to admit, though, they\x01",
            "put up a heck of a fight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "Here's hoping they rethink\x01",
            "their lives a bit, 'cause\x01",
            "they could really go places!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_606B")

    Jump("loc_62A7")

    label("loc_606E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_60BA")

    ChrTalk(    #311
        0xFE,
        "The finals continue today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        "I wonder who'll make it...\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A7")

    label("loc_60BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6153")

    ChrTalk(    #313
        0xFE,
        (
            "There's something...unsettling\x01",
            "about the sky bandit team\x01",
            "beating the Royal Army...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "I really wanted to see them\x01",
            "get a little farther!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62A7")

    label("loc_6153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_61D2")

    ChrTalk(    #315
        0xFE,
        "When's it gonna start, already?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "The real matches are always\x01",
            "so much more exciting than\x01",
            "the preliminaries!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62A7")

    label("loc_61D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_624A")

    ChrTalk(    #317
        0xFE,
        (
            "Are they seriously doing\x01",
            "TEAM battles this year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        (
            "I've always preferred one-on-\x01",
            "one matches, myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62A7")

    label("loc_624A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_62A7")

    ChrTalk(    #319
        0xFE,
        (
            "If looks like they changed\x01",
            "around a lot of the rules\x01",
            "this year, for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62A7")

    TalkEnd(0xFE)
    Return()

    # Function_8_5D12 end

    def Function_9_62AB(): pass

    label("Function_9_62AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_62B8")
    Jump("loc_6930")

    label("loc_62B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_62C2")
    Jump("loc_6930")

    label("loc_62C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_62CC")
    Jump("loc_6930")

    label("loc_62CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_62D6")
    Jump("loc_6930")

    label("loc_62D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_651A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_640A")

    ChrTalk(    #320
        0xFE,
        "That tears it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "I'm cheering for that big\x01",
            "guy from the Republic, Zin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xFE,
        (
            "...Though that Special Ops\x01",
            "team is nothing to sneeze\x01",
            "at, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "...Or maybe the bracers, as a team, have what\x01",
            "it takes. I'm just not sure! Maybe I'll just\x01",
            "cheer for the Specia...racer...ane! Yeah!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6517")

    label("loc_640A")

    OP_A2(0x5)

    ChrTalk(    #324
        0xFE,
        "Hmm... Who shall I cheer for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "It seems that whoever I end\x01",
            "up cheering for always loses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        (
            "So, maybe I should cheer for\x01",
            "the team I DON'T want to win!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xFE,
        (
            "Good ol' reverse psychology... You\x01",
            "haven't failed me yet! Er...I mean,\x01",
            "you have! You TOTALLY have!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6517")

    Jump("loc_6930")

    label("loc_651A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6586")

    ChrTalk(    #328
        0xFE,
        (
            "Aww, man! The team I was\x01",
            "cheering for lost again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        "I must be cursed or something!\x02",
    )

    CloseMessageWindow()
    Jump("loc_663D")

    label("loc_6586")

    OP_A2(0x5)

    ChrTalk(    #330
        0xFE,
        (
            "Aww, man! The team I was\x01",
            "cheering for lost again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        "I must be cursed or something!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        (
            "...There sure are a lot of\x01",
            "soldiers walking the streets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        "Did something happen?\x02",
    )

    CloseMessageWindow()

    label("loc_663D")

    Jump("loc_6930")

    label("loc_6640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6692")

    ChrTalk(    #334
        0xFE,
        (
            "Today I'm going to cheer for\x01",
            "that bracer team from Grancel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6726")

    label("loc_6692")

    OP_A2(0x5)

    ChrTalk(    #335
        0xFE,
        (
            "Today I'm going to cheer for\x01",
            "that bracer team from Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xFE,
        "I keep betting on losers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        (
            "But today'll be different!\x01",
            "I can feel it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6726")

    Jump("loc_6930")

    label("loc_6729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6774")

    ChrTalk(    #338
        0xFE,
        "Awww, the Ravens lost, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        "All my teams are losing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6930")

    label("loc_6774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_685F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_67D4")

    ChrTalk(    #340
        0xFE,
        (
            "The tournament is so much\x01",
            "more exciting when you pick\x01",
            "a team to root for!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_685C")

    label("loc_67D4")

    OP_A2(0x5)

    ChrTalk(    #341
        0xFE,
        (
            "When I was younger I acted like\x01",
            "a big-shot punk all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        (
            "So maybe I'll cheer for the \x01",
            "Ravens...or that nameless\x01",
            "team.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_685C")

    Jump("loc_6930")

    label("loc_685F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_68E5")

    ChrTalk(    #343
        0xFE,
        (
            "The border garrison team I'd \x01",
            "been cheering for lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        (
            "I can't believe General\x01",
            "Morgan's not participating\x01",
            "in this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6930")

    label("loc_68E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6930")

    ChrTalk(    #345
        0xFE,
        (
            "The border garrison team is\x01",
            "totally gonna win again\x01",
            "this year!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6930")

    TalkEnd(0xFE)
    Return()

    # Function_9_62AB end

    def Function_10_6934(): pass

    label("Function_10_6934")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6977")

    ChrTalk(    #346
        0xFE,
        (
            "I wonder what it's like to live\x01",
            "in the castle...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D3C")

    label("loc_6977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6981")
    Jump("loc_6D3C")

    label("loc_6981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_698B")
    Jump("loc_6D3C")

    label("loc_698B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_6995")
    Jump("loc_6D3C")

    label("loc_6995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6A4E")

    ChrTalk(    #347
        0xFE,
        (
            "I keep thinking about all\x01",
            "the different teams...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #348
        0xFE,
        (
            "And I've decided that, in the\x01",
            "end, I'm just going to cheer\x01",
            "for Joshua! My one and only!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D3C")

    label("loc_6A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6B8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6AE5")

    ChrTalk(    #349
        0xFE,
        (
            "That silky black hair and cool\x01",
            "gaze of his... It totally melts\x01",
            "my heart! He's simply DARLING!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        "I just want to hug him tight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B87")

    label("loc_6AE5")

    OP_A2(0x6)

    ChrTalk(    #351
        0xFE,
        (
            "Isn't that black-haired boy\x01",
            "out there amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        (
            "He's cute, but he has this\x01",
            "cool composure about him too,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        "I just want to hug him tight!\x02",
    )

    CloseMessageWindow()

    label("loc_6B87")

    Jump("loc_6D3C")

    label("loc_6B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6BC7")

    ChrTalk(    #354
        0xFE,
        (
            "Yeah, this is all that \x01",
            "DUKE's fault, I hear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D3C")

    label("loc_6BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6BF6")

    ChrTalk(    #355
        0xFE,
        "Yeah, Red Mask Man is DREAMY...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D3C")

    label("loc_6BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6C40")

    ChrTalk(    #356
        0xFE,
        (
            "Wow, those guys in the black\x01",
            "armor look pretty tough, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D3C")

    label("loc_6C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6CC5")

    ChrTalk(    #357
        0xFE,
        (
            "That Zin guy looks like an\x01",
            "immovable iron weight out\x01",
            "there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        (
            "He's fighting alone? What a\x01",
            "hulking specimen of man!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D3C")

    label("loc_6CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6D3C")

    ChrTalk(    #359
        0xFE,
        (
            "I can't believe the Royal\x01",
            "Guardsmen aren't fighting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xFE,
        (
            "I wanted to see Lieutenant\x01",
            "Schwarz do her thing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D3C")

    TalkEnd(0xFE)
    Return()

    # Function_10_6934 end

    def Function_11_6D40(): pass

    label("Function_11_6D40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6D9A")

    ChrTalk(    #361
        0xFE,
        "I dunno...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        (
            "Rumors might be rumors, but\x01",
            "it still sounds good to me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70D7")

    label("loc_6D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6DA4")
    Jump("loc_70D7")

    label("loc_6DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6DAE")
    Jump("loc_70D7")

    label("loc_6DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_6DB8")
    Jump("loc_70D7")

    label("loc_6DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6DFE")

    ChrTalk(    #363
        0xFE,
        (
            "What? Why are you going to \x01",
            "cheer for just one person?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70D7")

    label("loc_6DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6EC1")

    ChrTalk(    #364
        0xFE,
        (
            "Isn't Phoebe just AWFUL? I guess I'm \x01",
            "not one to talk, though, as I feel the\x01",
            "same way about that black-haired boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        (
            "That boy seriously looks like\x01",
            "he needs some of mama's love.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70D7")

    label("loc_6EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6F06")

    ChrTalk(    #366
        0xFE,
        (
            "But, aren't those sky bandit\x01",
            "guys just the creepiest?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70D7")

    label("loc_6F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6F9B")

    ChrTalk(    #367
        0xFE,
        (
            "That guy in the red mask? \x01",
            "Doesn't he just have the\x01",
            "SEXIEST set of lips?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x28, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #368
        0xFE,
        "His arms aren't bad either.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70D7")

    label("loc_6F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7021")

    ChrTalk(    #369
        0xFE,
        (
            "Yeah, those Royal Special...\x01",
            "Army Ops dudes, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        (
            "That matching black on black is\x01",
            "SO not doing them any favors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70D7")

    label("loc_7021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_709B")

    ChrTalk(    #371
        0xFE,
        (
            "I guess he looks ripped \x01",
            "enough, but he's...\x01",
            "He's OLD!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        (
            "You gotta have the look\x01",
            "to go with the skills.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70D7")

    label("loc_709B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_70D7")

    ChrTalk(    #373
        0xFE,
        (
            "Why did I even bother buying\x01",
            "an advance ticket?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70D7")

    TalkEnd(0xFE)
    Return()

    # Function_11_6D40 end

    def Function_12_70DB(): pass

    label("Function_12_70DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7143")

    ChrTalk(    #374
        0xFE,
        (
            "Everyone looks like they're\x01",
            "having so much fun at the\x01",
            "Queen's Birthday Celebration...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E40")

    label("loc_7143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_71A6")

    ChrTalk(    #375
        0xFE,
        (
            "Ricky acts like such a slacker\x01",
            "sometimes. Doesn't he have\x01",
            "any kind of drive at all?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E40")

    label("loc_71A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_722A")

    ChrTalk(    #376
        0xFE,
        (
            "Someone like Ricky would never\x01",
            "be able to understand the passion\x01",
            "that wells deep within me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        "Somebody save me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E40")

    label("loc_722A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_73E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_73A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7280")

    ChrTalk(    #378
        0xFE,
        (
            "He's going to sap all the \x01",
            "motivation out of me again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73A5")

    label("loc_7280")


    ChrTalk(    #379
        0xFE,
        (
            "I just tried talking \x01",
            "to that pretty girl who \x01",
            "kept walking by here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        "You know what she said?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "She told me that 'a leering\x01",
            "scumbag like me would never\x01",
            "stand a chance' with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        (
            "I was like, wow. You could\x01",
            "have just said no!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xFE,
        (
            "I just want to go curl up\x01",
            "somewhere and die...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73A5")

    Jump("loc_73DE")

    label("loc_73A8")


    ChrTalk(    #384
        0xFE,
        "Ugh. Another uneventful day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        "My life sucks.\x02",
    )

    CloseMessageWindow()

    label("loc_73DE")

    Jump("loc_7E40")

    label("loc_73E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_792F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_742C")

    ChrTalk(    #386
        0xFE,
        (
            "All right, I am so going to\x01",
            "talk to that lady today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_792C")

    label("loc_742C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_75A0")
    OP_A2(0x6EB)

    ChrTalk(    #387
        0xFE,
        (
            "YES! That makes three! I've\x01",
            "seen her three times now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xFE,
        (
            "I feel like I need to\x01",
            "thank someone upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xFE,
        "Thank you! Thank you Goddess!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        (
            "Thank you too, you guys!\x01",
            "Here, take this! As a token\x01",
            "of my appreciation!\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x21C, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #391
        "\x07\x00Received \x07\x02Carnelia - Finale\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #392
        0xFE,
        (
            "All right! Time to man up\x01",
            "and say something to her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_792C")

    label("loc_75A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_7657")

    ChrTalk(    #393
        0xFE,
        "One more time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0xFE,
        (
            "If I see that girl one more\x01",
            "time, I'll say hello to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xFE,
        (
            "She's like a goddess to me...\x01",
            "celestial and untenable, but\x01",
            "captivating in her beauty!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_792C")

    label("loc_7657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_775E")

    ChrTalk(    #396
        0xFE,
        (
            "Heh heh, that girl just\x01",
            "walked by here again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xFE,
        "Two more times...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0xFE,
        (
            "If that girl walks by \x01",
            "here two more times, it \x01",
            "means she's the one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0xFE,
        (
            "...But, what if she doesn't\x01",
            "walk by again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xFE,
        (
            "Oh, man...will she? Won't she?\x01",
            "Will she? Won't she?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_792C")

    label("loc_775E")

    OP_A2(0x9)

    ChrTalk(    #401
        0xFE,
        (
            "There's this beautiful girl\x01",
            "who walks by here all the\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xFE,
        (
            "Some days, counting how many times I see her\x01",
            "is the only way I can keep myself sane...\x01",
            "IF YOU CAN CALL THAT SANE. Ha...haha...ha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0xFE,
        "All right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xFE,
        (
            "If that girl walks by here\x01",
            "three times today, I'm going\x01",
            "to go up to her and say hi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0xFE,
        (
            "Now I just need that book, so I can pretend to be\x01",
            "reading it while I wait for her...because girls\x01",
            "like smart, bookish men, right? RIGHT? RIIIGHT?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_792C")

    Jump("loc_7E40")

    label("loc_792F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7AF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_79EE")

    ChrTalk(    #406
        0xFE,
        (
            "Everyplace I go around here, they're\x01",
            "all caught up in the festival, and no\x01",
            "one's even thinking about hiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0xFE,
        (
            "Maybe it's a sign from above\x01",
            "telling me not to work...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AEF")

    label("loc_79EE")

    OP_A2(0x8)

    ChrTalk(    #408
        0xFE,
        (
            "And I went to all the trouble of\x01",
            "coming out here to search for a\x01",
            "job, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0xFE,
        (
            "Everyplace I go around here, they're\x01",
            "all caught up in the festival, and no\x01",
            "one's even thinking about hiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xFE,
        (
            "Maybe it's a sign from above\x01",
            "telling me not to work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AEF")

    Jump("loc_7E40")

    label("loc_7AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7B40")

    ChrTalk(    #411
        0xFE,
        (
            "I don't get how Ricky can\x01",
            "be so laid-back all the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BD0")

    label("loc_7B40")

    OP_A2(0x8)

    ChrTalk(    #412
        0xFE,
        (
            "I've been feeling oddly\x01",
            "motivated these last couple\x01",
            "of days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xFE,
        (
            "As a matter of fact, I'm about\x01",
            "to go out and start looking\x01",
            "for a job!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BD0")

    Jump("loc_7E40")

    label("loc_7BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7C74")

    ChrTalk(    #414
        0xFE,
        (
            "Another day of doing nothing,\x01",
            "gone like dust in the wind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0xFE,
        (
            "I know everything'll change\x01",
            "if I can just find a good\x01",
            "job...but where do I look?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E40")

    label("loc_7C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7CEE")

    ChrTalk(    #416
        0xFE,
        (
            "*sigh* Another day of doing\x01",
            "nothing at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0xFE,
        (
            "At this rate I'm never going\x01",
            "to go anywhere with my life!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E40")

    label("loc_7CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_7D9A")

    ChrTalk(    #418
        0xFE,
        (
            "Aaaaand, there's another day\x01",
            "of my life completely wasted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xFE,
        (
            "I just don't want to DO anything\x01",
            "anymore... All I want to do is\x01",
            "stay home and waste my time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E40")

    label("loc_7D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7E40")

    ChrTalk(    #420
        0xFE,
        (
            "At least if I had a girlfriend,\x01",
            "I might go to the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xFE,
        (
            "...There's this beautiful girl\x01",
            "who comes by here all the time. \x01",
            "She's totally my type.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E40")

    TalkEnd(0xFE)
    Return()

    # Function_12_70DB end

    def Function_13_7E44(): pass

    label("Function_13_7E44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7ED2")

    ChrTalk(    #422
        0xFE,
        "Whoa, sure is busy out here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0xFE,
        (
            "Doesn't look like I'll get that\x01",
            "nap I've been wanting; may as\x01",
            "well just hang out instead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8491")

    label("loc_7ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7F4E")

    ChrTalk(    #424
        0xFE,
        "What do I want to do...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0xFE,
        (
            "Well...I guess it'd be cool \x01",
            "to have a nap in Grancel\x01",
            "Castle's Garden Terrace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8491")

    label("loc_7F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7FC6")

    ChrTalk(    #426
        0xFE,
        (
            "Right now, Anton's not talking\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        (
            "But, we all go through patches\x01",
            "like this sometimes, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8491")

    label("loc_7FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_8027")

    ChrTalk(    #428
        0xFE,
        (
            "...Watching Anton over there\x01",
            "never gets old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0xFE,
        "Hmm... What to do now...\x02",
    )

    CloseMessageWindow()
    Jump("loc_805E")

    label("loc_8027")


    ChrTalk(    #430
        0xFE,
        (
            "Man, I'm good with just not\x01",
            "doing ANYTHING today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_805E")

    Jump("loc_8491")

    label("loc_8061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_81A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_80E0")

    ChrTalk(    #431
        0xFE,
        (
            "I think Anton's a pretty happy\x01",
            "guy, sort of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0xFE,
        (
            "I can't figure out what's got\x01",
            "him so stoked, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81A0")

    label("loc_80E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8127")

    ChrTalk(    #433
        0xFE,
        (
            "Anton gets some weird ideas\x01",
            "in his head sometimes, man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81A0")

    label("loc_8127")


    ChrTalk(    #434
        0xFE,
        (
            "The final round of the tournament?\x01",
            "Was that today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xFE,
        (
            "It's all good to me, man. I'll\x01",
            "just be hanging out here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81A0")

    Jump("loc_8491")

    label("loc_81A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_8236")

    ChrTalk(    #436
        0xFE,
        (
            "Anton's starting up his old\x01",
            "habits again, man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xFE,
        (
            "He says he's looking for work...\x01",
            "but what he's actually looking\x01",
            "for is HIMSELF.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8491")

    label("loc_8236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8269")

    ChrTalk(    #438
        0xFE,
        "Maaaaan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0xFE,
        "Nice weather today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8491")

    label("loc_8269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_82F1")

    ChrTalk(    #440
        0xFE,
        (
            "My buddy's got something\x01",
            "on his mind again, man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0xFE,
        (
            "But he ain't gonna find\x01",
            "purpose in life just\x01",
            "by scoring some work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8491")

    label("loc_82F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_83A0")

    ChrTalk(    #442
        0xFE,
        (
            "Man, Anton's got himself all\x01",
            "worked up over something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0xFE,
        (
            "If he's got something on his mind,\x01",
            "he should take action, rather than\x01",
            "just stewing over it all day!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8491")

    label("loc_83A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_83EF")

    ChrTalk(    #444
        0xFE,
        (
            "Better go get some food before\x01",
            "it gets too crowded around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8491")

    label("loc_83EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8491")

    ChrTalk(    #445
        0xFE,
        (
            "Man, I ain't interested in\x01",
            "the tournament. Not at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xFE,
        (
            "All that stuff just happens,\x01",
            "man. It happens and it ends.\x01",
            "And the world keeps on turnin'.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8491")

    TalkEnd(0xFE)
    Return()

    # Function_13_7E44 end

    def Function_14_8495(): pass

    label("Function_14_8495")

    TalkBegin(0xFE)
    OP_A3(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_84A5")
    Jump("loc_8521")

    label("loc_84A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_84B2")
    OP_A2(0x19)
    Jump("loc_8521")

    label("loc_84B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_84BF")
    OP_A2(0x19)
    Jump("loc_8521")

    label("loc_84BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_84CC")
    OP_A2(0x19)
    Jump("loc_8521")

    label("loc_84CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_84D9")
    OP_A2(0x19)
    Jump("loc_8521")

    label("loc_84D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_84E6")
    OP_A2(0x19)
    Jump("loc_8521")

    label("loc_84E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_84F0")
    Jump("loc_8521")

    label("loc_84F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_84FD")
    OP_A2(0x19)
    Jump("loc_8521")

    label("loc_84FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_850A")
    OP_A2(0x19)
    Jump("loc_8521")

    label("loc_850A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_8517")
    OP_A2(0x19)
    Jump("loc_8521")

    label("loc_8517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8521")
    OP_A2(0x19)

    label("loc_8521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_8596")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8585")
    OP_0D()
    OP_A9(0x74)
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_8585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8596")
    TalkEnd(0xFE)
    Return()

    label("loc_8596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8633")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_85DD")

    ChrTalk(    #447
        0xFE,
        (
            "Busy, busy, busy! Just as I\x01",
            "assumed it would be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8630")

    label("loc_85DD")

    OP_A2(0xE)

    ChrTalk(    #448
        0xFE,
        (
            "One double chocolate mint,\x01",
            "coming right up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0xFE,
        "Thank you very much!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_8630")

    Jump("loc_8E0B")

    label("loc_8633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_8693")

    ChrTalk(    #450
        0xFE,
        (
            "All these soldiers sure seem\x01",
            "busy with something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0xFE,
        "I wonder what happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E0B")

    label("loc_8693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_86F4")

    ChrTalk(    #452
        0xFE,
        (
            "What ever happened to those\x01",
            "Royal Guardsmen people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xFE,
        "Have you heard anything?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E0B")

    label("loc_86F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_88DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_87D2")

    ChrTalk(    #454
        0xFE,
        (
            "Today's special is our \x01",
            "chocolate, strawberry, mint\x01",
            "and lemon sundae.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0xFE,
        (
            "Each scoop represents one of our champions:\x01",
            "Zin is chocolate, Estelle is strawberry,\x01",
            "Joshua is mint...and Olivier's a lemon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88DB")

    label("loc_87D2")

    OP_A2(0xE)

    ChrTalk(    #456
        0xFE,
        (
            "Hello! Would you like to\x01",
            "try our special sundae?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0xFE,
        (
            "It's one scoop each of \x01",
            "chocolate, strawberry, mint\x01",
            "and lemon ice cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0xFE,
        (
            "Each scoop represents one of our champions:\x01",
            "Zin is chocolate, Estelle is strawberry,\x01",
            "Joshua is mint...and Olivier's a lemon!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88DB")

    Jump("loc_8E0B")

    label("loc_88DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8972")

    ChrTalk(    #459
        0xFE,
        "Welcome! Step right up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0xFE,
        (
            "Today, after the final match,\x01",
            "I'll be selling my special \x01",
            "championship sundae!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xFE,
        "Come buy one later!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E0B")

    label("loc_8972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_89D7")

    ChrTalk(    #462
        0xFE,
        "So, tomorrow's the championship!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xFE,
        (
            "I'm already planning a \x01",
            "special edition sundae.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E0B")

    label("loc_89D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_8A6F")

    ChrTalk(    #464
        0xFE,
        (
            "During the tournament and the\x01",
            "Birthday Celebration, we're \x01",
            "running a special discount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xFE,
        (
            "Deal of a lifetime, so don't\x01",
            "miss it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B16")

    label("loc_8A6F")

    OP_A2(0xE)

    ChrTalk(    #466
        0xFE,
        "Welcome! Step right up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xFE,
        (
            "During the tournament and the\x01",
            "Birthday Celebration, we're \x01",
            "running a special discount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0xFE,
        (
            "Deal of a lifetime, so don't\x01",
            "miss it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B16")

    Jump("loc_8E0B")

    label("loc_8B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8C2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_8B9B")

    ChrTalk(    #469
        0xFE,
        (
            "My store doesn't have tons\x01",
            "of flavors, but they're\x01",
            "all home-made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0xFE,
        "Step on up and try one out for size!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C28")

    label("loc_8B9B")

    OP_A2(0xE)

    ChrTalk(    #471
        0xFE,
        "Coooome and get it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0xFE,
        (
            "My store doesn't have tons\x01",
            "of flavors, but they're\x01",
            "all home-made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0xFE,
        "Step on up and try one out for size!\x02",
    )

    CloseMessageWindow()

    label("loc_8C28")

    Jump("loc_8E0B")

    label("loc_8C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_8D45")

    ChrTalk(    #474
        0xFE,
        (
            "I hear the nobles associated with the royal\x01",
            "family are fans of my ice cream...but it's\x01",
            "probably just a rumor. Although...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0xFE,
        (
            "*giggle* Nobles are always sneaking into town\x01",
            "incognito, and if Princess Klaudia has done the\x01",
            "same, maybe she's tried some of my ice cream!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E0B")

    label("loc_8D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_8DB2")

    ChrTalk(    #476
        0xFE,
        (
            "You look tired from \x01",
            "all that cheering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0xFE,
        (
            "You know what'll freshen\x01",
            "you up? Some ice cream!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E0B")

    label("loc_8DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8E0B")

    ChrTalk(    #478
        0xFE,
        "Coooome and get it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0xFE,
        (
            "Who wants some cold and\x01",
            "creamy home-made ice cream?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E0B")

    TalkEnd(0xFE)
    Return()

    # Function_14_8495 end

    def Function_15_8E0F(): pass

    label("Function_15_8E0F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8ECA")

    ChrTalk(    #480
        0xFE,
        (
            "Working from home means,\x01",
            "ironically enough, I can't \x01",
            "spend time with my kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0xFE,
        (
            "But, she seems to understand.\x01",
            "And it's not like I can't make\x01",
            "time, if the need arises.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_910D")

    label("loc_8ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_8F76")

    ChrTalk(    #482
        0xFE,
        (
            "We're here in the capital for the\x01",
            "Queen's Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0xFE,
        (
            "But I'm worried about being so\x01",
            "far from home, with the airships\x01",
            "being held up so often.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_910D")

    label("loc_8F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8FA1")

    ChrTalk(    #484
        0xFE,
        "Boys are so full of energy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_910D")

    label("loc_8FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_9048")

    ChrTalk(    #485
        0xFE,
        (
            "This woman is an attendant\x01",
            "for one of the airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0xFE,
        (
            "We're both working mothers, so\x01",
            "we hit it off pretty quickly,\x01",
            "comparing 'war stories' and such.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_910D")

    label("loc_9048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_90D4")

    ChrTalk(    #487
        0xFE,
        (
            "The ice cream they sell\x01",
            "here is really good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0xFE,
        (
            "I'll bet it's probably one \x01",
            "of the more famous stores\x01",
            "here in the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_910D")

    label("loc_90D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_90DE")
    Jump("loc_910D")

    label("loc_90DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_90E8")
    Jump("loc_910D")

    label("loc_90E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_90F2")
    Jump("loc_910D")

    label("loc_90F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_90FC")
    Jump("loc_910D")

    label("loc_90FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_9106")
    Jump("loc_910D")

    label("loc_9106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_910D")

    label("loc_910D")

    TalkEnd(0xFE)
    Return()

    # Function_15_8E0F end

    def Function_16_9111(): pass

    label("Function_16_9111")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9178")

    ChrTalk(    #489
        0xFE,
        (
            "Mommy said she'd buy me more\x01",
            "ice cream if I would leave\x01",
            "her alone to talk some more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_930A")

    label("loc_9178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_919E")

    ChrTalk(    #490
        0xFE,
        "I want more ice cream!\x02",
    )

    CloseMessageWindow()
    Jump("loc_930A")

    label("loc_919E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_9243")

    ChrTalk(    #491
        0xFE,
        (
            "I come from a village by the\x01",
            "sea, where there are lots and\x01",
            "lots of pretty white flowers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0xFE,
        (
            "And my best friend Polly and\x01",
            "all my friends live there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_930A")

    label("loc_9243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_9295")

    ChrTalk(    #493
        0xFE,
        "I want to go see the castle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0xFE,
        "But they said I'm not allowed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_930A")

    label("loc_9295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_92D1")

    ChrTalk(    #495
        0xFE,
        "I love ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0xFE,
        "Mommy bought me some.\x02",
    )

    CloseMessageWindow()
    Jump("loc_930A")

    label("loc_92D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_92DB")
    Jump("loc_930A")

    label("loc_92DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_92E5")
    Jump("loc_930A")

    label("loc_92E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_92EF")
    Jump("loc_930A")

    label("loc_92EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_92F9")
    Jump("loc_930A")

    label("loc_92F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_9303")
    Jump("loc_930A")

    label("loc_9303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_930A")

    label("loc_930A")

    TalkEnd(0xFE)
    Return()

    # Function_16_9111 end

    def Function_17_930E(): pass

    label("Function_17_930E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9407")

    ChrTalk(    #497
        0xFE,
        (
            "I didn't have work today, so\x01",
            "I got to play with my kid and\x01",
            "meet some lovely new people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0xFE,
        (
            "What's sad, though, is I keep thinking about\x01",
            "work. I figured this would be a much-needed\x01",
            "break, but I just can't get away from it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_954E")

    label("loc_9407")

    OP_A2(0x11)

    ChrTalk(    #499
        0xFE,
        (
            "I've got to catch a flight\x01",
            "on the next Cecilia. Off-duty,\x01",
            "of course--the ONLY way to fly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0xFE,
        (
            "I didn't have work today, so\x01",
            "I got to play with my kid and\x01",
            "meet some lovely new people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0xFE,
        (
            "What's sad, though, is I keep thinking about\x01",
            "work. I figured this would be a much-needed\x01",
            "break, but I just can't get away from it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_954E")

    Jump("loc_9E07")

    label("loc_9551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_961A")

    ChrTalk(    #502
        0xFE,
        (
            "I was supposed to work today,\x01",
            "but the boarding platform\x01",
            "was closed and locked down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0xFE,
        (
            "It might be an anti-terrorist\x01",
            "thing... I have no idea. There's\x01",
            "just been so much of that lately!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E07")

    label("loc_961A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_9665")

    ChrTalk(    #504
        0xFE,
        (
            "Seeing Carla's daughter makes\x01",
            "me really want one of my own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E07")

    label("loc_9665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_97B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_96E7")

    ChrTalk(    #505
        0xFE,
        (
            "This woman here works at\x01",
            "an inn, with her husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0xFE,
        (
            "It sounds like harder work\x01",
            "than you might expect...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97B0")

    label("loc_96E7")

    OP_A2(0x11)

    ChrTalk(    #507
        0xFE,
        (
            "When your kids become friends,\x01",
            "you wind up becoming friends\x01",
            "with their parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xFE,
        (
            "This woman here works at\x01",
            "an inn, with her husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0xFE,
        (
            "It sounds like harder work\x01",
            "than you might expect...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97B0")

    Jump("loc_9E07")

    label("loc_97B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_988D")

    ChrTalk(    #510
        0xFE,
        (
            "This ice cream is pretty\x01",
            "popular throughout the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0xFE,
        (
            "There was a big rumor that Princess Klaudia snuck\x01",
            "here and ate some, and then her attendants came\x01",
            "to get her, and made a whole scene out of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E07")

    label("loc_988D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9920")

    ChrTalk(    #512
        0xFE,
        (
            "Before we go home I think \x01",
            "we'll stop in the park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0xFE,
        (
            "I could use a rest; it's been\x01",
            "a while since I played that\x01",
            "long with my kid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E07")

    label("loc_9920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_998B")

    ChrTalk(    #514
        0xFE,
        (
            "He's just crazy about the\x01",
            "Martial Arts Competition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0xFE,
        "Boys will be boys, though...right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E07")

    label("loc_998B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9B64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9A5C")

    ChrTalk(    #516
        0xFE,
        (
            "Sure was a shocker, I must admit...\x01",
            "To think the sky bandits who kid-\x01",
            "napped us were out in the arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0xFE,
        (
            "I'm sure it was a good show\x01",
            "for everyone else, but it\x01",
            "made me...uncomfortable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B61")

    label("loc_9A5C")

    OP_A2(0x11)

    ChrTalk(    #518
        0xFE,
        (
            "Sure was a shocker, I must admit... Why\x01",
            "would the sky bandits who kidnapped us be\x01",
            "allowed to fight in the competition?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0xFE,
        (
            "What in the world was Duke\x01",
            "Dunan thinking?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0xFE,
        (
            "I'm sure it was a good show\x01",
            "for everyone else, but it\x01",
            "made me...uncomfortable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B61")

    Jump("loc_9E07")

    label("loc_9B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9BE3")

    ChrTalk(    #521
        0xFE,
        (
            "We're going to the tournament\x01",
            "today, but only because my\x01",
            "boy begged me to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0xFE,
        "I hope I'm not spoiling him!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E07")

    label("loc_9BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_9D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9C71")

    ChrTalk(    #523
        0xFE,
        (
            "People are coming from all \x01",
            "over to see the tournament; \x01",
            "the airships must be packed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0xFE,
        "I hope the company's okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D4B")

    label("loc_9C71")

    OP_A2(0x11)

    ChrTalk(    #525
        0xFE,
        (
            "People are coming from all \x01",
            "over to see the tournament; \x01",
            "the airships must be packed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0xFE,
        (
            "Getting a vacation at times like\x01",
            "this is almost more of a hassle\x01",
            "than anything else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0xFE,
        "I hope the company's okay...\x02",
    )

    CloseMessageWindow()

    label("loc_9D4B")

    Jump("loc_9E07")

    label("loc_9D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9E07")

    ChrTalk(    #528
        0xFE,
        (
            "Since I was locked up during the Sky\x01",
            "Bandit incident, the company gave me\x01",
            "a long paid vacation as compensation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0xFE,
        (
            "I'm grateful to be able to spend\x01",
            "this time with my son.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E07")

    TalkEnd(0xFE)
    Return()

    # Function_17_930E end

    def Function_18_9E0B(): pass

    label("Function_18_9E0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9E5D")

    ChrTalk(    #530
        0xFE,
        "This ice cream is the best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0xFE,
        "Mint chocolate is my favorite.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_9E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_9E88")

    ChrTalk(    #532
        0xFE,
        "How long is Mom gonna talk?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_9E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_9EB4")

    ChrTalk(    #533
        0xFE,
        "I wanna go to Lucia's house!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_9EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_9F03")

    ChrTalk(    #534
        0xFE,
        (
            "Heh, you know what? I've been\x01",
            "inside the castle before! Really!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_9F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_9F4D")

    ChrTalk(    #535
        0xFE,
        "Ice cream?! Luuucky...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0xFE,
        "That ice cream is really good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_9F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9F8D")

    ChrTalk(    #537
        0xFE,
        "Mom sure gets tired quick!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0xFE,
        "She's so lazy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_9F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9FBB")

    ChrTalk(    #539
        0xFE,
        "I'm going to watch the fights!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_9FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A01F")

    ChrTalk(    #540
        0xFE,
        "That fight was AWESOME!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #541
        0xFE,
        (
            "I was so surprised, I jumped\x01",
            "THIS high out of my chair!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_A01F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A062")

    ChrTalk(    #542
        0xFE,
        (
            "I get to go and see the fights\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #543
        0xFE,
        "Jealous?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_A062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A0C4")

    ChrTalk(    #544
        0xFE,
        "Mom is always on the airships.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #545
        0xFE,
        (
            "When I grow up, I wanna \x01",
            "work on airships too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_A0C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A104")

    ChrTalk(    #546
        0xFE,
        (
            "Today Mom said she's gonna\x01",
            "play with me aaaall day!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A104")

    TalkEnd(0xFE)
    Return()

    # Function_18_9E0B end

    def Function_19_A108(): pass

    label("Function_19_A108")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A22C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_A175")

    ChrTalk(    #547
        0xFE,
        (
            "I trusted them. I was so sure\x01",
            "the Royal Guardsmen would \x01",
            "never betray Her Highness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A229")

    label("loc_A175")

    OP_A2(0x13)

    ChrTalk(    #548
        0xFE,
        (
            "I trusted them. I was so sure\x01",
            "the Royal Guardsmen would \x01",
            "never betray Her Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #549
        0xFE,
        (
            "And then Colonel Richard \x01",
            "staged a coup d'etat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0xFE,
        "I just don't understand it.\x02",
    )

    CloseMessageWindow()

    label("loc_A229")

    Jump("loc_A85E")

    label("loc_A22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A294")

    ChrTalk(    #551
        0xFE,
        (
            "The Royal Garrison have all\x01",
            "pulled back in a real hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #552
        0xFE,
        "That does not bode well...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A85E")

    label("loc_A294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A344")

    ChrTalk(    #553
        0xFE,
        (
            "The Birthday Celebration is only\x01",
            "a few days away, but there's been\x01",
            "no word from the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #554
        0xFE,
        (
            "I wonder how the Royal Guard's\x01",
            "investigation is coming along...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85E")

    label("loc_A344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A402")

    ChrTalk(    #555
        0xFE,
        (
            "I assumed Colonel Richard and Lt.\x01",
            "Schwarz working together meant that\x01",
            "we'd be safe, pretty much forevermore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #556
        0xFE,
        (
            "But...I never thought they'd be \x01",
            "working together like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85E")

    label("loc_A402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_A4B8")

    ChrTalk(    #557
        0xFE,
        (
            "I don't care that those Special Ops guys are\x01",
            "Colonel Richard's troops. I don't trust them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0xFE,
        (
            "That we would even HAVE \x01",
            "stormtroopers like that,\x01",
            "serving in Liberl...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85E")

    label("loc_A4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_A54C")

    ChrTalk(    #559
        0xFE,
        (
            "Come to think of it, 1st Lt.\x01",
            "Schwarz was always a very\x01",
            "devout member of the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #560
        0xFE,
        (
            "I saw her there numerous times\x01",
            "during mass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85E")

    label("loc_A54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A5F1")

    ChrTalk(    #561
        0xFE,
        (
            "You used to see 1st Lt. Schwarz\x01",
            "patrolling this area quite\x01",
            "often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #562
        0xFE,
        (
            "She was so friendly. She even\x01",
            "made small talk, asking about\x01",
            "my sore back once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85E")

    label("loc_A5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A685")

    ChrTalk(    #563
        0xFE,
        (
            "The Arseille is being held\x01",
            "in port by the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #564
        0xFE,
        (
            "But the Royal Guard are still\x01",
            "showing up in Zeiss, and\x01",
            "attacking the capital...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85E")

    label("loc_A685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A73F")

    ChrTalk(    #565
        0xFE,
        (
            "The Royal Guard used to be\x01",
            "quite popular with the common\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #566
        0xFE,
        (
            "Every year, they'd participate in the\x01",
            "Martial Arts Competition, and the\x01",
            "Birthday Celebration as well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85E")

    label("loc_A73F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A811")

    ChrTalk(    #567
        0xFE,
        (
            "The terrorists' actions are all the\x01",
            "more shocking when you consider the\x01",
            "season. It's the queen's birthday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #568
        0xFE,
        (
            "You would think that they'd\x01",
            "show at least some respect,\x01",
            "even if they're rebelling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85E")

    label("loc_A811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A85E")

    ChrTalk(    #569
        0xFE,
        "Oh, hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #570
        0xFE,
        (
            "Are you here to watch the\x01",
            "Martial Arts Competition?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A85E")

    TalkEnd(0xFE)
    Return()

    # Function_19_A108 end

    def Function_20_A862(): pass

    label("Function_20_A862")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A8F6")

    ChrTalk(    #571
        0xFE,
        (
            "The queen imprisoned, the\x01",
            "princess kidnapped...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #572
        0xFE,
        (
            "I don't care about the ends;\x01",
            "the means Colonel Richard \x01",
            "used are disgusting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B013")

    label("loc_A8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A99C")

    ChrTalk(    #573
        0xFE,
        (
            "I'm supposed to be shopping,\x01",
            "but something feels...off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #574
        0xFE,
        (
            "It's too quiet, even with all\x01",
            "these people around. And all \x01",
            "these guards make me nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B013")

    label("loc_A99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_AA13")

    ChrTalk(    #575
        0xFE,
        (
            "The castle is still closed\x01",
            "to visitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #576
        0xFE,
        (
            "I feel bad for the people who\x01",
            "came all this way to see it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B013")

    label("loc_AA13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_AAD4")

    ChrTalk(    #577
        0xFE,
        (
            "Hey, aren't you the guys who\x01",
            "won the championship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #578
        0xFE,
        (
            "Congratulations! That was an\x01",
            "absolutely incredible match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #579
        0xFE,
        (
            "I'm so glad you won it instead\x01",
            "of that Special Ops team...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B013")

    label("loc_AAD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_AE37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_AB35")

    ChrTalk(    #580
        0xFE,
        (
            "Standing around all day,\x01",
            "ogling people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #581
        0xFE,
        "That's just rude, you know?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE34")

    label("loc_AB35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_AB8F")

    ChrTalk(    #582
        0xFE,
        (
            "Standing around all day,\x01",
            "ogling people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #583
        0xFE,
        "That's just rude, you know?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE34")

    label("loc_AB8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_ACAC")
    OP_63(0x31)

    ChrTalk(    #584
        0xFE,
        (
            "That guy over there is staring\x01",
            "at me. I can feel his eyes on\x01",
            "me, all the time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #585
        0xFE,
        (
            "It's just so creepy... I don't\x01",
            "want to get anywhere near him!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x31, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #586
        0xFE,
        "Oh, are you bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #587
        0xFE,
        (
            "What a relief! I feel a lot\x01",
            "safer with bracers around.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x15)
    OP_4B(0x31, 255)
    Jump("loc_AE34")

    label("loc_ACAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AD3A")

    ChrTalk(    #588
        0xFE,
        (
            "I saw that guy over there\x01",
            "looking at me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #589
        0xFE,
        (
            "*shudder* Maybe I'll find \x01",
            "another route to take for\x01",
            "running my errands...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE34")

    label("loc_AD3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_ADC8")

    ChrTalk(    #590
        0xFE,
        (
            "That guy standing in front of\x01",
            "the market has been staring at\x01",
            "me for quite some time now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #591
        0xFE,
        "Makes me VERY uncomfortable...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE34")

    label("loc_ADC8")


    ChrTalk(    #592
        0xFE,
        (
            "All these soldiers showed\x01",
            "up in town yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #593
        0xFE,
        (
            "I wonder if they found those\x01",
            "Royal Guardsmen yet?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE34")

    Jump("loc_B013")

    label("loc_AE37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_AECF")

    ChrTalk(    #594
        0xFE,
        (
            "The Royal Guardsmen were chased\x01",
            "out of the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #595
        0xFE,
        (
            "I'll just bet it was because\x01",
            "Duke Dunan was getting jealous\x01",
            "of their popularity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B013")

    label("loc_AECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_AF27")

    ChrTalk(    #596
        0xFE,
        "Mmmm... What a nice morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #597
        0xFE,
        (
            "The sun feels so wonderful\x01",
            "on my skin!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B013")

    label("loc_AF27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AF5D")

    ChrTalk(    #598
        0xFE,
        (
            "I wonder how the day's matches\x01",
            "went...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B013")

    label("loc_AF5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_AF81")

    ChrTalk(    #599
        0xFE,
        "Today's the big day!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B013")

    label("loc_AF81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_AFB9")

    ChrTalk(    #600
        0xFE,
        (
            "The city sure is full of life\x01",
            "today, no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B013")

    label("loc_AFB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B013")

    ChrTalk(    #601
        0xFE,
        (
            "There's this ice cream shop\x01",
            "here in the East Block that\x01",
            "is simply to DIE for!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B013")

    TalkEnd(0xFE)
    Return()

    # Function_20_A862 end

    def Function_21_B017(): pass

    label("Function_21_B017")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B05F")

    ChrTalk(    #602
        0xFE,
        (
            "I was so happy to finally\x01",
            "see the queen's face again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B05F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_B0C8")

    ChrTalk(    #603
        0xFE,
        (
            "Haven't seen the usual soldiers\x01",
            "around lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #604
        0xFE,
        (
            "Did something happen at the\x01",
            "castle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B0C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_B169")

    ChrTalk(    #605
        0xFE,
        (
            "The Birthday Celebration isn't\x01",
            "quite the same with Duke Dunan\x01",
            "instead of the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #606
        0xFE,
        (
            "I hope she gets better by the\x01",
            "time it officially starts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B1DE")

    ChrTalk(    #607
        0xFE,
        (
            "That was some match, wasn't it?\x01",
            "Had me all aflutter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #608
        0xFE,
        (
            "Well, time to go home and get\x01",
            "dinner ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B250")

    ChrTalk(    #609
        0xFE,
        (
            "Saw this nun I'd never seen before\x01",
            "at the cathedral recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #610
        0xFE,
        "I wonder when she started...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B2A9")

    ChrTalk(    #611
        0xFE,
        (
            "I want to get some shopping\x01",
            "done at Edel's, then get the\x01",
            "heck outta here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B2A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B31E")

    ChrTalk(    #612
        0xFE,
        (
            "Some good matches this afternoon. I really\x01",
            "want to make sure I get everything done\x01",
            "before they start.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B36E")

    ChrTalk(    #613
        0xFE,
        (
            "Ahhh... Nothin' like a tourney\x01",
            "to soothe one's shattered nerves!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B3E1")

    ChrTalk(    #614
        0xFE,
        (
            "Today's match-ups should set\x01",
            "a few new records, yesiree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #615
        0xFE,
        (
            "This afteroon can't come soon\x01",
            "enough!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B3E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B443")

    ChrTalk(    #616
        0xFE,
        (
            "Heh heh. There've been a lot\x01",
            "of good matches this year,\x01",
            "even in the preliminaries!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4A1")

    label("loc_B443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B4A1")

    ChrTalk(    #617
        0xFE,
        (
            "Everyone in the city always looks\x01",
            "forward to the annual Martial Arts\x01",
            "Competition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4A1")

    TalkEnd(0xFE)
    Return()

    # Function_21_B017 end

    def Function_22_B4A5(): pass

    label("Function_22_B4A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B527")

    ChrTalk(    #618
        0xFE,
        (
            "During the Birthday Celebration,\x01",
            "nobody really comes here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #619
        0xFE,
        (
            "But we still need to stand guard,\x01",
            "just in case!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B714")

    label("loc_B527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_B531")
    Jump("loc_B714")

    label("loc_B531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_B574")

    ChrTalk(    #620
        0xFE,
        (
            "After the tournament, this\x01",
            "place gets pretty quiet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B714")

    label("loc_B574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B629")

    ChrTalk(    #621
        0xFE,
        "So...the bracers won it, I hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #622
        0xFE,
        (
            "I kind of thought the Special\x01",
            "Ops Team'd have an edge..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #623
        0xFE,
        (
            "Oh well. The bracers won, fair\x01",
            "and square. No getting around\x01",
            "that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B714")

    label("loc_B629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B683")

    ChrTalk(    #624
        0xFE,
        "So, the championship's today, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #625
        0xFE,
        "I look forward to a quiet shift.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B714")

    label("loc_B683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B6E5")

    ChrTalk(    #626
        0xFE,
        (
            "It's tough being on guard duty\x01",
            "during the tournament, what\x01",
            "with people EVERYWHERE.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B714")

    label("loc_B6E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B6EF")
    Jump("loc_B714")

    label("loc_B6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B6F9")
    Jump("loc_B714")

    label("loc_B6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B703")
    Jump("loc_B714")

    label("loc_B703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B70D")
    Jump("loc_B714")

    label("loc_B70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B714")

    label("loc_B714")

    TalkEnd(0xFE)
    Return()

    # Function_22_B4A5 end

    def Function_23_B718(): pass

    label("Function_23_B718")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B7AC")

    ChrTalk(    #627
        0xFE,
        (
            "Word is they're going to start\x01",
            "restructuring the royal military's\x01",
            "chain of command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #628
        0xFE,
        (
            "I hope they put the right\x01",
            "people on top!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9EB")

    label("loc_B7AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_B7B6")
    Jump("loc_B9EB")

    label("loc_B7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_B854")

    ChrTalk(    #629
        0xFE,
        (
            "Those terrorists still\x01",
            "haven't been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #630
        0xFE,
        (
            "That's probably why I'm\x01",
            "still standing guard here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #631
        0xFE,
        (
            "But we're all...frankly,\x01",
            "exhausted!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9EB")

    label("loc_B854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B8EE")

    ChrTalk(    #632
        0xFE,
        (
            "I was up late last night on\x01",
            "patrol, so I need to get\x01",
            "some proper rest tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #633
        0xFE,
        (
            "With the tournament over,\x01",
            "I hope I can get some leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9EB")

    label("loc_B8EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B947")

    ChrTalk(    #634
        0xFE,
        (
            "I was up late last night,\x01",
            "on patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #635
        0xFE,
        "So I didn't get a lot of sleep.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9EB")

    label("loc_B947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B9BC")

    ChrTalk(    #636
        0xFE,
        (
            "We've got to really keep a close\x01",
            "eye on the city, to ensure there\x01",
            "are no further terrorist incidents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9EB")

    label("loc_B9BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B9C6")
    Jump("loc_B9EB")

    label("loc_B9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B9D0")
    Jump("loc_B9EB")

    label("loc_B9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B9DA")
    Jump("loc_B9EB")

    label("loc_B9DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B9E4")
    Jump("loc_B9EB")

    label("loc_B9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B9EB")

    label("loc_B9EB")

    TalkEnd(0xFE)
    Return()

    # Function_23_B718 end

    def Function_24_B9EF(): pass

    label("Function_24_B9EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BA91")

    ChrTalk(    #637
        0xFE,
        (
            "Word is they're going to start\x01",
            "restructuring the royal military's\x01",
            "chain of command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #638
        0xFE,
        (
            "I hope they put someone with\x01",
            "some brains in command...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCAE")

    label("loc_BA91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BA9B")
    Jump("loc_BCAE")

    label("loc_BA9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BB25")

    ChrTalk(    #639
        0xFE,
        (
            "We're patrolling endlessly, and\x01",
            "keeping all the access gates shut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #640
        0xFE,
        (
            "Finding those terrorists is\x01",
            "just a matter of time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCAE")

    label("loc_BB25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BB83")

    ChrTalk(    #641
        0xFE,
        (
            "I'll be patrolling inside the\x01",
            "department store later. That's\x01",
            "my favorite beat!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCAE")

    label("loc_BB83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BBEE")

    ChrTalk(    #642
        0xFE,
        (
            "If you see any Royal Guardsmen,\x01",
            "or anyone else who seems suspi-\x01",
            "cious, please, let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCAE")

    label("loc_BBEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BC7F")

    ChrTalk(    #643
        0xFE,
        (
            "I can't believe the sky bandits\x01",
            "got permission to fight in the\x01",
            "competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #644
        0xFE,
        (
            "What the hell is going through\x01",
            "the duke's head?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCAE")

    label("loc_BC7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BC89")
    Jump("loc_BCAE")

    label("loc_BC89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BC93")
    Jump("loc_BCAE")

    label("loc_BC93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BC9D")
    Jump("loc_BCAE")

    label("loc_BC9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BCA7")
    Jump("loc_BCAE")

    label("loc_BCA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BCAE")

    label("loc_BCAE")

    TalkEnd(0xFE)
    Return()

    # Function_24_B9EF end

    def Function_25_BCB2(): pass

    label("Function_25_BCB2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BCBF")
    Jump("loc_BD61")

    label("loc_BCBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BD0A")

    ChrTalk(    #645
        0xFE,
        "Yeah? What do you want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #646
        0xFE,
        "Stop makin' googly-eyes at me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD61")

    label("loc_BD0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BD14")
    Jump("loc_BD61")

    label("loc_BD14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BD1E")
    Jump("loc_BD61")

    label("loc_BD1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BD28")
    Jump("loc_BD61")

    label("loc_BD28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BD32")
    Jump("loc_BD61")

    label("loc_BD32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BD3C")
    Jump("loc_BD61")

    label("loc_BD3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BD46")
    Jump("loc_BD61")

    label("loc_BD46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BD50")
    Jump("loc_BD61")

    label("loc_BD50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BD5A")
    Jump("loc_BD61")

    label("loc_BD5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BD61")

    label("loc_BD61")

    TalkEnd(0xFE)
    Return()

    # Function_25_BCB2 end

    def Function_26_BD65(): pass

    label("Function_26_BD65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BD72")
    Jump("loc_BE4B")

    label("loc_BD72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BDF4")

    ChrTalk(    #647
        0xFE,
        (
            "People haven't seen Colonel\x01",
            "Richard anywhere--not even\x01",
            "inside the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #648
        0xFE,
        "Where the heck could he have gone?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE4B")

    label("loc_BDF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BDFE")
    Jump("loc_BE4B")

    label("loc_BDFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BE08")
    Jump("loc_BE4B")

    label("loc_BE08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BE12")
    Jump("loc_BE4B")

    label("loc_BE12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BE1C")
    Jump("loc_BE4B")

    label("loc_BE1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BE26")
    Jump("loc_BE4B")

    label("loc_BE26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BE30")
    Jump("loc_BE4B")

    label("loc_BE30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BE3A")
    Jump("loc_BE4B")

    label("loc_BE3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BE44")
    Jump("loc_BE4B")

    label("loc_BE44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BE4B")

    label("loc_BE4B")

    TalkEnd(0xFE)
    Return()

    # Function_26_BD65 end

    def Function_27_BE4F(): pass

    label("Function_27_BE4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BE5C")
    Jump("loc_BFC3")

    label("loc_BE5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BF6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_BED2")

    ChrTalk(    #649
        0xFE,
        (
            "Commander Lorence really\x01",
            "fought hard in the finals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #650
        0xFE,
        (
            "He's a real force to be\x01",
            "reckoned with!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF69")

    label("loc_BED2")

    OP_A2(0x17)

    ChrTalk(    #651
        0xFE,
        (
            "You guys really earned\x01",
            "that championship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #652
        0xFE,
        (
            "Commander Lorence really\x01",
            "fought hard in the finals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #653
        0xFE,
        (
            "He's a real force to be\x01",
            "reckoned with!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF69")

    Jump("loc_BFC3")

    label("loc_BF6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BF76")
    Jump("loc_BFC3")

    label("loc_BF76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BF80")
    Jump("loc_BFC3")

    label("loc_BF80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BF8A")
    Jump("loc_BFC3")

    label("loc_BF8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BF94")
    Jump("loc_BFC3")

    label("loc_BF94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BF9E")
    Jump("loc_BFC3")

    label("loc_BF9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BFA8")
    Jump("loc_BFC3")

    label("loc_BFA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BFB2")
    Jump("loc_BFC3")

    label("loc_BFB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BFBC")
    Jump("loc_BFC3")

    label("loc_BFBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BFC3")

    label("loc_BFC3")

    TalkEnd(0xFE)
    Return()

    # Function_27_BE4F end

    def Function_28_BFC7(): pass

    label("Function_28_BFC7")

    TalkBegin(0xFE)

    ChrTalk(    #654
        0xFE,
        (
            "Allllllll right, time to hit\x01",
            "up that department store!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_BFC7 end

    def Function_29_C00A(): pass

    label("Function_29_C00A")

    TalkBegin(0xFE)

    ChrTalk(    #655
        0xFE,
        (
            "May as well pick up some of\x01",
            "the latest fashions after\x01",
            "coming all this way, y'know?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_C00A end

    def Function_30_C069(): pass

    label("Function_30_C069")

    TalkBegin(0xFE)

    ChrTalk(    #656
        0xFE,
        "Will you look at this line?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #657
        0xFE,
        "What's it for?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_C069 end

    def Function_31_C0A6(): pass

    label("Function_31_C0A6")

    TalkBegin(0xFE)

    ChrTalk(    #658
        0xFE,
        (
            "Who do you think I am, a kid?\x01",
            "I'm not going to eat that!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_C0A6 end

    def Function_32_C0EB(): pass

    label("Function_32_C0EB")

    TalkBegin(0xFE)

    ChrTalk(    #659
        0xFE,
        "Oh, you're not, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #660
        0xFE,
        (
            "Well, then I guess you don't\x01",
            "mind your old man eating it.\x01",
            "Ha ha ha ha ha!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_C0EB end

    def Function_33_C15F(): pass

    label("Function_33_C15F")

    TalkBegin(0xFE)

    ChrTalk(    #661
        0xFE,
        "This crowd is something else...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_C15F end

    def Function_34_C18B(): pass

    label("Function_34_C18B")

    TalkBegin(0xFE)

    ChrTalk(    #662
        0xFE,
        (
            "It's a lot hotter today than\x01",
            "it's been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #663
        0xFE,
        "Ice cold refreshment time!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_C18B end

    def Function_35_C1E1(): pass

    label("Function_35_C1E1")

    TalkBegin(0xFE)

    ChrTalk(    #664
        0xFE,
        "HEY!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #665
        0xFE,
        "No cutting in line!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_C1E1 end

    def Function_36_C20B(): pass

    label("Function_36_C20B")

    TalkBegin(0xFE)

    ChrTalk(    #666
        0xFE,
        (
            "This line sure is taking its\x01",
            "sweet time...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_C20B end

    def Function_37_C242(): pass

    label("Function_37_C242")

    TalkBegin(0xFE)

    ChrTalk(    #667
        0xFE,
        (
            "You hear about that coup d'etat? Was\x01",
            "pretty serious, but the Royal Guard\x01",
            "and the bracers put a stop to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #668
        0xFE,
        (
            "Can't help wondering about the\x01",
            "Royal Army, though...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_C242 end

    def Function_38_C2F3(): pass

    label("Function_38_C2F3")

    TalkBegin(0xFE)

    ChrTalk(    #669
        0xFE,
        (
            "So this is the famous Museum\x01",
            "of History, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #670
        0xFE,
        (
            "...Birthday Celebration first.\x01",
            "THEN it's museum time!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_C2F3 end

    def Function_39_C367(): pass

    label("Function_39_C367")

    TalkBegin(0xFE)

    ChrTalk(    #671
        0xFE,
        (
            "Never too old to learn more\x01",
            "about the world around you,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_C367 end

    def Function_40_C3B5(): pass

    label("Function_40_C3B5")

    TalkBegin(0xFE)

    ChrTalk(    #672
        0xFE,
        "Oogh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #673
        0xFE,
        (
            "I got a blister on my feet from\x01",
            "all this walking!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #674
        0xFE,
        "It really, really hurts, too!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_C3B5 end

    def Function_41_C423(): pass

    label("Function_41_C423")

    TalkBegin(0xFE)

    ChrTalk(    #675
        0xFE,
        (
            "That's what you get for not\x01",
            "breaking in those shoes,\x01",
            "I guess...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_C423 end

    def Function_42_C46F(): pass

    label("Function_42_C46F")

    TalkBegin(0xFE)

    ChrTalk(    #676
        0xFE,
        "Daad, that is sooooo laaaame!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_C46F end

    def Function_43_C499(): pass

    label("Function_43_C499")

    TalkBegin(0xFE)

    ChrTalk(    #677
        0xFE,
        (
            "I'm getting chills from the\x01",
            "sheer lameness of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #678
        0xFE,
        (
            "If the coup d'etat had \x01",
            "succeeded, would Duke Dunan \x01",
            "have taken over the throne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #679
        0xFE,
        "We'd be goners if that happened!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_C499 end

    def Function_44_C553(): pass

    label("Function_44_C553")

    TalkBegin(0xFE)

    ChrTalk(    #680
        0xFE,
        (
            "I heard the Intelligence\x01",
            "Division was behind the\x01",
            "so-called 'terrorists.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #681
        0xFE,
        (
            "I'm glad it didn't turn out\x01",
            "to be the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_C553 end

    def Function_45_C5E0(): pass

    label("Function_45_C5E0")

    TalkBegin(0xFE)

    ChrTalk(    #682
        0xFE,
        (
            "Apparently, the department store's\x01",
            "holding a big sale for the queen's\x01",
            "Birthday Celebration!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #683
        0xFE,
        (
            "All the latest brands and\x01",
            "fashions are on sale--but\x01",
            "only for a limited time!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_C5E0 end

    def Function_46_C69A(): pass

    label("Function_46_C69A")

    TalkBegin(0xFE)

    ChrTalk(    #684
        0xFE,
        "Are you SERIOUS?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #685
        0xFE,
        "We gotta get over there!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_46_C69A end

    def Function_47_C6D6(): pass

    label("Function_47_C6D6")

    TalkBegin(0xFE)

    ChrTalk(    #686
        0xFE,
        (
            "It sure is calm, considering\x01",
            "there was a coup d'etat not\x01",
            "long ago...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_47_C6D6 end

    def Function_48_C727(): pass

    label("Function_48_C727")

    TalkBegin(0xFE)

    ChrTalk(    #687
        0xFE,
        "So, this is Calvard's embassy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #688
        0xFE,
        "I'd love to see the inside of it.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_48_C727 end

    def Function_49_C77B(): pass

    label("Function_49_C77B")

    TalkBegin(0xFE)

    ChrTalk(    #689
        0xFE,
        (
            "This is my first time\x01",
            "visiting the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #690
        0xFE,
        "The roads are so wide!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_C77B end

    def Function_50_C7CF(): pass

    label("Function_50_C7CF")

    TalkBegin(0xFE)

    ChrTalk(    #691
        0xFE,
        "Hey! Don't wander off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #692
        0xFE,
        (
            "...I'm worried my daughter will\x01",
            "get lost in all this craziness.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_50_C7CF end

    def Function_51_C837(): pass

    label("Function_51_C837")

    TalkBegin(0xFE)

    ChrTalk(    #693
        0xFE,
        (
            "This year the airships were\x01",
            "a mess, so we missed the\x01",
            "competition altogether.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #694
        0xFE,
        (
            "I heard it was because of\x01",
            "Colonel Richard's coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #695
        0xFE,
        (
            "I liked that guy, too! Sucks\x01",
            "when someone turns out to be\x01",
            "a backstabber.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_51_C837 end

    def Function_52_C915(): pass

    label("Function_52_C915")

    TalkBegin(0xFE)

    ChrTalk(    #696
        0xFE,
        "I'm gonna get a toy airship!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_52_C915 end

    def Function_53_C93E(): pass

    label("Function_53_C93E")

    TalkBegin(0xFE)

    ChrTalk(    #697
        0xFE,
        (
            "My grandson begged me to take\x01",
            "him to the department store.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_53_C93E end

    def Function_54_C985(): pass

    label("Function_54_C985")

    TalkBegin(0xFE)

    ChrTalk(    #698
        0xFE,
        (
            "Now that the coup's been\x01",
            "thwarted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #699
        0xFE,
        (
            "...it's finally sunk in that the\x01",
            "ones who thwarted it were the\x01",
            "tournament champions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #700
        0xFE,
        "Crazy times call for crazy riots!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_54_C985 end

    def Function_55_CA37(): pass

    label("Function_55_CA37")

    TalkBegin(0xFE)

    ChrTalk(    #701
        0xFE,
        (
            "It makes me kind of nervous,\x01",
            "dancing around like this in\x01",
            "front of the Erebonian embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #702
        0xFE,
        "It's an intimidating place!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_55_CA37 end

    def Function_56_CABD(): pass

    label("Function_56_CABD")

    TalkBegin(0xFE)

    ChrTalk(    #703
        0xFE,
        (
            "I think you're big enough to\x01",
            "walk by yourself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #704
        0xFE,
        "But whatever!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_56_CABD end

    def Function_57_CB0D(): pass

    label("Function_57_CB0D")

    TalkBegin(0xFE)

    ChrTalk(    #705
        0xFE,
        "Sis! Give me a piggy-back!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_57_CB0D end

    def Function_58_CB34(): pass

    label("Function_58_CB34")

    TalkBegin(0xFE)

    ChrTalk(    #706
        0xFE,
        (
            "The reception is over, so I'm\x01",
            "gonna go look around the city.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_58_CB34 end

    SaveToFile()

Try(main)
