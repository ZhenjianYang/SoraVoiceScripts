from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x1)
    OP_28(0xD, 0x4, 0x10)
    OP_3F(0x329, 1)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE6DC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_451")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6")
    Fade(1000)
    SetChrPos(0x101, 60600, 1000, 52500, 270)
    SetChrPos(0x102, 60600, 1000, 51300, 315)
    SetChrPos(0x103, 61600, 1000, 51500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE")
    SetChrPos(0x104, 61600, 1000, 50200, 315)
    Jump("loc_10D")

    label("loc_EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D")
    SetChrPos(0x134, 61600, 1000, 50200, 315)

    label("loc_10D")

    TurnDirection(0x101, 0x8, 0)
    OP_69(0x101, 0x7D0)

    ChrTalk(    #0
        0x101,
        "#000FUm, excuse me.\x02",
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(    #1
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#000FYou're Father Holstein, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "Ho ho ho.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Indeed I am, but how may I help\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44E")

    label("loc_1A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F")
    Fade(1000)
    SetChrPos(0x102, 60600, 1000, 52500, 270)
    SetChrPos(0x101, 60600, 1000, 51300, 315)
    SetChrPos(0x103, 61600, 1000, 51500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C")
    SetChrPos(0x104, 61600, 1000, 50200, 315)
    Jump("loc_22B")

    label("loc_20C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B")
    SetChrPos(0x134, 61600, 1000, 50200, 315)

    label("loc_22B")

    TurnDirection(0x102, 0x8, 0)
    OP_69(0x102, 0x7D0)

    ChrTalk(    #5
        0x102,
        (
            "#010FExcuse us, Father, but could we\x01",
            "have a minute of your time?\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(    #6
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_44E")

    label("loc_28F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D")
    Fade(1000)
    SetChrPos(0x103, 60600, 1000, 52500, 270)
    SetChrPos(0x101, 60600, 1000, 51300, 315)
    SetChrPos(0x102, 61600, 1000, 51500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F5")
    SetChrPos(0x104, 61600, 1000, 50200, 315)
    Jump("loc_314")

    label("loc_2F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_314")
    SetChrPos(0x134, 61600, 1000, 50200, 315)

    label("loc_314")

    TurnDirection(0x103, 0x8, 0)
    OP_69(0x103, 0x7D0)

    ChrTalk(    #7
        0x103,
        (
            "#020FAre you free to talk to us for a\x01",
            "moment, Father?\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(    #8
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_44E")

    label("loc_36D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E")
    Fade(1000)
    SetChrPos(0x104, 60600, 1000, 52500, 270)
    SetChrPos(0x101, 60600, 1000, 51300, 315)
    SetChrPos(0x103, 61600, 1000, 50200, 315)
    SetChrPos(0x102, 61600, 1000, 51500, 270)
    TurnDirection(0x104, 0x8, 0)
    OP_69(0x104, 0x7D0)

    ChrTalk(    #9
        0x104,
        (
            "#030FHello there and good day, Father.\x02\x03",

            "Forgive our intrusion, but we need\x01",
            "to borrow a minute of your time.\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(    #10
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    label("loc_44E")

    Jump("loc_817")

    label("loc_451")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F")
    Fade(1000)
    SetChrPos(0x101, 57400, 1000, 52500, 90)
    SetChrPos(0x102, 57400, 1000, 51300, 45)
    SetChrPos(0x103, 56400, 1000, 51500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B7")
    SetChrPos(0x104, 56400, 1000, 50200, 45)
    Jump("loc_4D6")

    label("loc_4B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D6")
    SetChrPos(0x134, 56400, 1000, 50200, 45)

    label("loc_4D6")

    TurnDirection(0x101, 0x8, 0)
    OP_69(0x101, 0x7D0)

    ChrTalk(    #11
        0x101,
        "#000FUm, excuse me.\x02",
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(    #12
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#000FYou're Father Holstein, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "Ho ho ho.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "Indeed I am, but how may I help\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_817")

    label("loc_56F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_658")
    Fade(1000)
    SetChrPos(0x102, 57400, 1000, 52500, 90)
    SetChrPos(0x101, 57400, 1000, 51300, 45)
    SetChrPos(0x103, 56400, 1000, 51500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D5")
    SetChrPos(0x104, 56400, 1000, 50200, 45)
    Jump("loc_5F4")

    label("loc_5D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F4")
    SetChrPos(0x134, 56400, 1000, 50200, 45)

    label("loc_5F4")

    TurnDirection(0x102, 0x8, 0)
    OP_69(0x102, 0x7D0)

    ChrTalk(    #16
        0x102,
        (
            "#010FExcuse us, Father, but could we\x01",
            "have a minute of your time?\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(    #17
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_817")

    label("loc_658")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_736")
    Fade(1000)
    SetChrPos(0x103, 57400, 1000, 52500, 90)
    SetChrPos(0x101, 57400, 1000, 51300, 45)
    SetChrPos(0x102, 56400, 1000, 51500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BE")
    SetChrPos(0x104, 56400, 1000, 50200, 45)
    Jump("loc_6DD")

    label("loc_6BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DD")
    SetChrPos(0x134, 56400, 1000, 50200, 45)

    label("loc_6DD")

    TurnDirection(0x103, 0x8, 0)
    OP_69(0x103, 0x7D0)

    ChrTalk(    #18
        0x103,
        (
            "#020FAre you free to talk to us for a\x01",
            "moment, Father?\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(    #19
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_817")

    label("loc_736")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_817")
    Fade(1000)
    SetChrPos(0x104, 57400, 1000, 52500, 90)
    SetChrPos(0x101, 57400, 1000, 51300, 45)
    SetChrPos(0x103, 56400, 1000, 50200, 45)
    SetChrPos(0x102, 56400, 1000, 51500, 90)
    TurnDirection(0x104, 0x8, 0)
    OP_69(0x104, 0x7D0)

    ChrTalk(    #20
        0x104,
        (
            "#030FHello there and good day, Father.\x02\x03",

            "Forgive our intrusion, but we need\x01",
            "to borrow a minute of your time.\x02",
        )
    )

    CloseMessageWindow()
    TalkBegin(0x8)

    ChrTalk(    #21
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    label("loc_817")


    ChrTalk(    #22
        0x101,
        (
            "#000FThis is for you.\x02\x03",

            "It's a letter from Father Divine in\x01",
            "Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x00Handed over \x07\x02Father Divine's Letter\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C8")
    OP_28(0xD, 0x1, 0x4000)

    label("loc_8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_939")
    OP_28(0xD, 0x1, 0x2000)
    OP_28(0xD, 0x1, 0x2)

    ChrTalk(    #24
        0x101,
        (
            "#000FI'm really sorry to deliver it this\x01",
            "late, but we had a number of things\x01",
            "come up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93F")

    label("loc_939")

    OP_28(0xD, 0x1, 0x4)

    label("loc_93F")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #25
        0x8,
        "Ho ho ho. Is this for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "Thank you very much for delivering\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "However, a letter from Father Divine\x01",
            "could only mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "Ah yes, he's come up with a new\x01",
            "formula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#501FEh...?\x02\x03",

            "A new formula for what?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #30
        0x8,
        (
            "Ho ho ho. Don't tell me you didn't\x01",
            "know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "Father Divine is a master of medicine,\x01",
            "known throughout Liberl for his skills\x01",
            "in the healing arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "In fact, he was well-known for this\x01",
            "even back when he was at Grancel\x01",
            "Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #33
        0x101,
        "#004FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "Even after he took up his new post as\x01",
            "a father in Rolent, he has continued\x01",
            "his research without fail...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "And when he discovers an effective\x01",
            "medicine, he shares his knowledge\x01",
            "with the rest of us.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC2")

    ChrTalk(    #36
        0x103,
        (
            "#020FWe bracers also use the medicine\x01",
            "created by Father Divine on a\x01",
            "daily basis.\x02\x03",

            "So in a way, we're being supported\x01",
            "in our work from behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC2")


    ChrTalk(    #37
        0x101,
        (
            "#004FI had no idea...\x02\x03",

            "It would have been nice if he had\x01",
            "at least mentioned it to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#010FBut it's just like him not to.\x02\x03",

            "Since he never talks about himself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #39
        0x101,
        "#000FAin't THAT the truth!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E95")
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #40
        0x101,
        (
            "#509FUnlike someone I know who rambles\x01",
            "on about stuff that nobody cares\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #41
        0x104,
        (
            "#035FEstelle...\x02\x03",

            "Why are you looking at me like\x01",
            "that? \x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x101,
        (
            "#007FNo reason.\x01",
            "No reason at all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E95")


    ChrTalk(    #43
        0x8,
        (
            "Father Divine is very strict with\x01",
            "himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "Whenever he admonishes someone,\x01",
            "he is always admonishing himself\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "This is one attitude I think all young\x01",
            "children these days should learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "Although it'd be a bit difficult\x01",
            "for me to learn at this ripe age.\x01",
            "Ho ho ho.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FBA():
        TurnDirection(0x104, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FBA)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #47
        0x101,
        "#506FYeah. Har har har or whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#6PWell, how about we just try to work\x01",
            "hard without overreaching ourselves.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 0)

    ChrTalk(    #49
        0x8,
        (
            "I appreciate you coming all the\x01",
            "way up from Rolent to deliver\x01",
            "this letter today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "Oh, Aidios, goddess of the\x01",
            "firmament...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "Please protect these souls as you\x01",
            "guide them in their daily lives...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #52
        "\x07\x00Quest \x07\x02[Letter Carrier] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x8, 180, 0)
    EventEnd(0x0)
    TalkEnd(0x8)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
