from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_67",           # 01, 1
        "Function_2_68",           # 02, 2
        "Function_3_305",          # 03, 3
        "Function_4_A87",          # 04, 4
        "Function_5_DFC",          # 05, 5
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Return()

    # Function_0_66 end

    def Function_1_67(): pass

    label("Function_1_67")

    Return()

    # Function_1_67 end

    def Function_2_68(): pass

    label("Function_2_68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_75")
    Jump("loc_301")

    label("loc_75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7F")
    Jump("loc_301")

    label("loc_7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_113")

    ChrTalk(    #0
        0xFE,
        (
            "#812FLooks like you haven't had a\x01",
            "moment's rest since everything\x01",
            "started.\x02\x03",

            "Take a minute now and get\x01",
            "everything squared away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC")

    label("loc_113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_END)), "loc_1CC")

    ChrTalk(    #1
        0xFE,
        (
            "#854FUp until now things haven't\x01",
            "made much sense, but I think \x01",
            "I'm starting to get it...\x02\x03",

            "When this much is on the line,\x01",
            "you can't help but get a bit\x01",
            "nervous, right? Heh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC")

    Jump("loc_301")

    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D9")
    Jump("loc_301")

    label("loc_1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1E3")
    Jump("loc_301")

    label("loc_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1ED")
    Jump("loc_301")

    label("loc_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_239")

    ChrTalk(    #2
        0xFE,
        (
            "#850FLet's do what it is we need\x01",
            "to do, the best way we can!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_243")
    Jump("loc_301")

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_24D")
    Jump("loc_301")

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_28F")

    ChrTalk(    #3
        0xFE,
        (
            "#850FHey, new guys! Have you found\x01",
            "Zin yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7")

    label("loc_28F")


    ChrTalk(    #4
        0xFE,
        (
            "#850FHey, new guys! Have you found\x01",
            "Zin yet?\x02\x03",

            "#811FI can't wait for a chance\x01",
            "to spar with you guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F7")

    Jump("loc_301")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_301")

    label("loc_301")

    TalkEnd(0xFE)
    Return()

    # Function_2_68 end

    def Function_3_305(): pass

    label("Function_3_305")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_A83")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_31C")
    Jump("loc_A83")

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_391")

    ChrTalk(    #5
        0xFE,
        (
            "#830FI'll leave the breaking and\x01",
            "entering to you guys.\x02\x03",

            "...What? You guys can totally\x01",
            "do this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F8")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 3)), scpexpr(EXPR_END)), "loc_3F8")

    ChrTalk(    #6
        0xFE,
        (
            "#832FThis is the first time I've\x01",
            "had to handle a job this big.\x02\x03",

            "We have no room for error!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F8")

    Jump("loc_A83")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_49A")

    ChrTalk(    #7
        0xFE,
        (
            "#831FA big match like that is going\x01",
            "to be burned into my brain for\x01",
            "a long time to come!\x02\x03",

            "I hope I can work alongside\x01",
            "you guys one day...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53D")

    label("loc_49A")

    OP_A2(0x6)

    ChrTalk(    #8
        0xFE,
        (
            "#831FCongratulations!\x02\x03",

            "A big match like that is going\x01",
            "to be burned into my brain for\x01",
            "a long time to come!\x02\x03",

            "I hope I can work alongside\x01",
            "you guys one day...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D")

    Jump("loc_A83")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_54A")
    Jump("loc_A83")

    label("loc_54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5BD")

    ChrTalk(    #9
        0xFE,
        (
            "#830FTomorrow's the big match.\x02\x03",

            "Don't go out there and embarrass\x01",
            "the bracers, now, you hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_653")

    label("loc_5BD")

    OP_A2(0x6)

    ChrTalk(    #10
        0xFE,
        (
            "#830FTomorrow's the big match.\x02\x03",

            "Don't go out there and embarrass\x01",
            "the bracers, now, you hear?\x02\x03",

            "#835FNot that I think you guys will,\x01",
            "of course!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_653")

    Jump("loc_A83")

    label("loc_656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_690")

    ChrTalk(    #11
        0xFE,
        (
            "#831FAll righty, then.\x02\x03",

            "Let's do it to it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A83")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6FF")

    ChrTalk(    #12
        0xFE,
        (
            "#830FLooking forward to pitting my\x01",
            "own skills against you two in\x01",
            "the very near future...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E2")

    label("loc_6FF")

    OP_A2(0x6)

    ChrTalk(    #13
        0xFE,
        (
            "#831FHey, you. Congratulations on\x01",
            "finishing round one.\x02\x03",

            "Bet you weren't expecting to\x01",
            "meet up with the Ravens there,\x01",
            "were you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#505FIt was definitely a bit of a\x01",
            "surprise!\x02\x03",

            "#006FBut I think THEY were even MORE\x01",
            "surprised. Heh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#019FIf we keep this up, we might\x01",
            "even become bracers like Agate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#009FEw. No, one of him is plenty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "#833FHeh heh. They fought pretty\x01",
            "hard, but honestly, I was \x01",
            "surprised how well you did.\x02\x03",

            "#830FI heard all the stories about you at the\x01",
            "Ruan Branch, but you exceed your reputations\x01",
            "quite thoroughly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#008FReally?\x02\x03",

            "That's so sweet of you to say!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "#831FHeh heh. I can't wait to cross\x01",
            "swords with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#001FIt's a date!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#010FWe're looking forward to the\x01",
            "chance ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E2")

    Jump("loc_A83")

    label("loc_9E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A72")

    ChrTalk(    #22
        0xFE,
        "All righty, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Before the match, you guys should\x01",
            "warm up against a couple of monsters.\x01",
            "Get the ol' muscles stretched.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A83")

    label("loc_A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A7C")
    Jump("loc_A83")

    label("loc_A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A83")

    label("loc_A83")

    TalkEnd(0xFE)
    Return()

    # Function_3_305 end

    def Function_4_A87(): pass

    label("Function_4_A87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A94")
    Jump("loc_DF8")

    label("loc_A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A9E")
    Jump("loc_DF8")

    label("loc_A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_B23")

    ChrTalk(    #24
        0xFE,
        (
            "#824FIntelligence is resorting to\x01",
            "using hostages? That's just\x01",
            "disgusting...\x02\x03",

            "#822FLet's go save us a princess!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAF")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_END)), "loc_BAF")

    ChrTalk(    #25
        0xFE,
        (
            "#822FColonel Richard, staging a\x01",
            "coup d'etat? I'd've never\x01",
            "believed it before today.\x02\x03",

            "He's a pretty smooth liar, I\x01",
            "must admit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAF")

    Jump("loc_DF8")

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BBC")
    Jump("loc_DF8")

    label("loc_BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BC6")
    Jump("loc_DF8")

    label("loc_BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C33")

    ChrTalk(    #26
        0xFE,
        (
            "#820FWe lost, but we lost in a good\x01",
            "fight. No regrets.\x02\x03",

            "Go win the championship, guys!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA3")

    label("loc_C33")

    OP_A2(0x5)

    ChrTalk(    #27
        0xFE,
        (
            "#820FHey, everybody!\x02\x03",

            "We lost, but we lost in a good\x01",
            "fight. No regrets.\x02\x03",

            "Go win the championship, guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA3")

    Jump("loc_DF8")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_CB0")
    Jump("loc_DF8")

    label("loc_CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_D3E")

    ChrTalk(    #28
        0xFE,
        (
            "#821FTomorrow, it's all about fighting\x01",
            "the big boys... Makin' a big noise\x01",
            "with some big toys...\x02\x03",

            "You'd better bring it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDA")

    label("loc_D3E")

    OP_A2(0x5)

    ChrTalk(    #29
        0xFE,
        (
            "#821FGood work out there today.\x02\x03",

            "Tomorrow, it's all about fighting\x01",
            "the big boys... Makin' a big noise\x01",
            "with some big toys...\x02\x03",

            "You'd better bring it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDA")

    Jump("loc_DF8")

    label("loc_DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_DE7")
    Jump("loc_DF8")

    label("loc_DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_DF1")
    Jump("loc_DF8")

    label("loc_DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_DF8")

    label("loc_DF8")

    TalkEnd(0xFE)
    Return()

    # Function_4_A87 end

    def Function_5_DFC(): pass

    label("Function_5_DFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_E09")
    Jump("loc_10C3")

    label("loc_E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_E13")
    Jump("loc_10C3")

    label("loc_E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 0)), scpexpr(EXPR_END)), "loc_E79")

    ChrTalk(    #30
        0xFE,
        (
            "#840FWe're the only ones who can\x01",
            "possibly pull this off.\x02\x03",

            "So let's get pulling!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_END)), "loc_F13")

    ChrTalk(    #31
        0xFE,
        (
            "#845FWell, that was certainly embarrassing.\x02\x03",

            "I am bothered by my missing memories,\x01",
            "but right now, the queen's orders are\x01",
            "foremost on my mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F13")

    Jump("loc_10C3")

    label("loc_F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1080")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(    #32
        0xFE,
        (
            "#840FSeeing you young bracers in\x01",
            "action is a pretty big motivator\x01",
            "for the rest of us.\x02\x03",

            "I can't just let myself get\x01",
            "left behind, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107D")

    label("loc_FB6")

    OP_A2(0x4)

    ChrTalk(    #33
        0xFE,
        (
            "#840FHey, congratulations. That\x01",
            "was an impressive match.\x02\x03",

            "Seeing you young bracers in\x01",
            "action is a pretty big motivator\x01",
            "for the rest of us.\x02\x03",

            "I can't just let myself get\x01",
            "left behind, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107D")

    Jump("loc_10C3")

    label("loc_1080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_108A")
    Jump("loc_10C3")

    label("loc_108A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1094")
    Jump("loc_10C3")

    label("loc_1094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_109E")
    Jump("loc_10C3")

    label("loc_109E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_10A8")
    Jump("loc_10C3")

    label("loc_10A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_10B2")
    Jump("loc_10C3")

    label("loc_10B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_10BC")
    Jump("loc_10C3")

    label("loc_10BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_10C3")

    label("loc_10C3")

    TalkEnd(0xFE)
    Return()

    # Function_5_DFC end

    SaveToFile()

Try(main)
