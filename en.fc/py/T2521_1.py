from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2521_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        "Function_1_BF7",          # 01, 1
        "Function_2_105A",         # 02, 2
        "Function_3_10C7",         # 03, 3
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_16B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6")
    TalkBegin(0x15)
    OP_A2(0xC)

    ChrTalk(    #0
        0xFE,
        (
            "Thanks to you, I now have all \x01",
            "three volumes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Now, I can begin my research \x01",
            "without delay. Time is short.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_168")

    label("loc_F6")

    SetChrFlags(0x15, 0x10)
    TalkBegin(0x15)

    ChrTalk(    #2
        0xFE,
        "Hmm... Ahh, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Hmm... It appears that I shall \x01",
            "have to adjust my estimates\x01",
            "somewhat.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x10)

    label("loc_168")

    Jump("loc_BF3")

    label("loc_16B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1D6")
    TalkBegin(0x15)

    ChrTalk(    #4
        0xFE,
        (
            "I could finish my paper, if you'll just\x01",
            "find me the copy of 'Ruan Economics.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF3")

    label("loc_1D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B5")
    TalkBegin(0x15)
    OP_A2(0xB)

    ChrTalk(    #6
        0xFE,
        (
            "Hmm...as I suspected. This isn't\x01",
            "going to be sufficient for my\x01",
            "research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "You haven't found the remaining\x01",
            "volumes anywhere around, have\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40E")
    EventBegin(0x0)

    ChrTalk(    #8
        0x101,
        "#006FHeh heh... Yep, we found them.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_END)), "loc_329")
    OP_3F(0x33D, 1)
    OP_28(0x27, 0x1, 0x200)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00Handed over \x07\x02Ruan Economics I\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_329")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_END)), "loc_389")
    OP_3F(0x33E, 1)
    OP_28(0x27, 0x1, 0x400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00Handed over \x07\x02Ruan Economics II\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_389")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_END)), "loc_3EA")
    OP_3F(0x33F, 1)
    OP_28(0x27, 0x1, 0x800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00Handed over \x07\x02Ruan Economics III\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3EA")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #12
        0xFE,
        "Ahh, so you did.\x02",
    )

    CloseMessageWindow()
    Call(1, 1)
    Jump("loc_4B2")

    label("loc_40E")


    ChrTalk(    #13
        0x101,
        (
            "#003FUmm... Well, we haven't found\x01",
            "ALL of them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        "#040FThat's right, we haven't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "If you find the rest of them,\x01",
            "be sure to let me know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B2")

    Jump("loc_BF3")

    label("loc_4B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_57C")
    TalkBegin(0x15)

    ChrTalk(    #17
        0xFE,
        (
            "I simply must have the supporting\x01",
            "documents for my paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "The three volumes of the 'Ruan\x01",
            "Economics' series appear to be\x01",
            "missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "If you can find them,\x01",
            "please let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF3")

    label("loc_57C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_8D9")
    TalkBegin(0x15)
    OP_A2(0xB)

    ChrTalk(    #20
        0xFE,
        (
            "Hmm...as I suspected. This isn't\x01",
            "going to be sufficient for my\x01",
            "research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Have you seen any of the books\x01",
            "in the 'Ruan Economics' series\x01",
            "around, perchance?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_828")
    EventBegin(0x0)

    ChrTalk(    #22
        0x101,
        (
            "#000FUh... Well...\x02\x03",

            "(Kloe, is this what he's talking\x01",
            "about?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x105,
        (
            "#040FYes, I believe so.\x02\x03",

            "Logic, is this what you've\x01",
            "been looking for?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_END)), "loc_731")
    OP_3F(0x33D, 1)
    OP_28(0x27, 0x1, 0x200)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x00Handed over \x07\x02Ruan Economics I\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_END)), "loc_791")
    OP_3F(0x33E, 1)
    OP_28(0x27, 0x1, 0x400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x00Handed over \x07\x02Ruan Economics II\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_791")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_END)), "loc_7F2")
    OP_3F(0x33F, 1)
    OP_28(0x27, 0x1, 0x800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x00Handed over \x07\x02Ruan Economics III\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7F2")

    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #27
        0xFE,
        "Ahh, yes. Yes! You have my thanks!\x02",
    )

    CloseMessageWindow()
    Call(1, 1)
    Jump("loc_8D6")

    label("loc_828")


    ChrTalk(    #28
        0x101,
        "#002FHmm... No, we haven't seen them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        "#040FI'm sorry, Logic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "No, no. There's no need for you\x01",
            "to apologize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Pardon me. Come talk to me\x01",
            "when you find them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D6")

    Jump("loc_BF3")

    label("loc_8D9")

    OP_A2(0xA)
    OP_28(0x27, 0x1, 0x20)
    ClearChrFlags(0x15, 0x10)
    TalkBegin(0x15)
    EventBegin(0x0)
    TurnDirection(0x15, 0x105, 0)
    OP_4A(0x15, 255)

    ChrTalk(    #32
        0xFE,
        "Hmm? Kloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x105,
        (
            "#044FHello, Logic.\x02\x03",

            "Are you still working on the research for your\x01",
            "class' presentation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "Y-Yes... I'm almost finished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "But I'm missing a few research materials needed\x01",
            "to back up the points made in the presentation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x105,
        "#043FOh, my... That's terrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Specifically, I need all three volumes\x01",
            "of the 'Ruan Economics' series.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "It appears that some miscreant\x01",
            "has carried them out of the\x01",
            "reference section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I don't suppose you've seen\x01",
            "them anywhere around the\x01",
            "school, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#003FHmm... I don't think so.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #41
        0xFE,
        (
            "I see... Well, they must be\x01",
            "around here somewhere.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #42
        0xFE,
        (
            "If you should happen to find\x01",
            "them, please let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x105,
        (
            "#040FWe shall.\x02\x03",

            "If we find them, you will be\x01",
            "the first to know.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x10)
    EventEnd(0x1)
    OP_4B(0x15, 255)

    label("loc_BF3")

    TalkEnd(0x15)
    Return()

    # Function_0_66 end

    def Function_1_BF7(): pass

    label("Function_1_BF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED7")
    OP_28(0x27, 0x1, 0x1000)
    OP_28(0x3D, 0x1, 0x400)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)

    ChrTalk(    #44
        0xFE,
        (
            "Now I finally have all\x01",
            "of the books I need for my\x01",
            "research.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xFE, 400)

    ChrTalk(    #45
        0x105,
        (
            "#040FHa ha. I look forward to reading\x01",
            "your paper when it's done,\x01",
            "Logic.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #46
        0xFE,
        (
            "Yes, and I look forward to showing you\x01",
            "my results. You will be astounded!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Thanks to your help, I can\x01",
            "make this paper the best it\x01",
            "can possibly be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Now, I really should get\x01",
            "started. Time is short.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I wish you the best of luck\x01",
            "with your play, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x105,
        "#040FWe'll do our best.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #51
        0x105,
        "#040FIsn't that right, Estelle?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #52
        0x101,
        "#001FHa ha. You can count on it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #53
        0xFE,
        "Good to hear it.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x00Festival help quest \x07\x02[Research Materials Hunt] \x07\x00completed!\x02",
    )

    OP_83(0x2, 0x3)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(100)
    Jump("loc_1054")

    label("loc_ED7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F83")

    ChrTalk(    #55
        0xFE,
        (
            "There must be one more volume\x01",
            "somewhere on campus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Please, find it and bring it\x01",
            "back to me for my research.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1054")

    label("loc_F83")


    ChrTalk(    #57
        0xFE,
        (
            "The other two volumes must be\x01",
            "around somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "If I have the materials I need,\x01",
            "I can make sure that the research\x01",
            "paper is flawless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Please, find them and bring them\x01",
            "back to me for my research.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1054")

    EventEnd(0x1)
    TalkEnd(0x15)
    Return()

    # Function_1_BF7 end

    def Function_2_105A(): pass

    label("Function_2_105A")

    OP_A3(0xA)
    OP_A3(0xB)
    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x16, 0x80)
    OP_64(0x1, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #60
        "\x07\x00Found \x07\x02Ruan Economics I\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33D, 1)
    OP_28(0x27, 0x1, 0x40)
    TalkEnd(0xFF)
    Return()

    # Function_2_105A end

    def Function_3_10C7(): pass

    label("Function_3_10C7")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #61
        (
            "\x07\x05The bookshelf is empty. The reference material\x01",
            "has apparently been removed. On the shelf\x01",
            "someone has scratched ' I <3 JDK '.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1305")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Return Ruan Economics books]\x01",      # 0
            "[Cancel]\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11E8"),
        (1, "loc_1302"),
        (SWITCH_DEFAULT, "loc_1305"),
    )


    label("loc_11E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_END)), "loc_1244")
    OP_3F(0x33D, 1)
    OP_28(0x27, 0x1, 0x200)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #62
        "\x07\x00Returned \x07\x02Ruan Economics I\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1244")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_END)), "loc_12A1")
    OP_3F(0x33E, 1)
    OP_28(0x27, 0x1, 0x400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        "\x07\x00Returned \x07\x02Ruan Economics II\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_END)), "loc_12FF")
    OP_3F(0x33F, 1)
    OP_28(0x27, 0x1, 0x800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #64
        "\x07\x00Returned \x07\x02Ruan Economics III\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12FF")

    Jump("loc_1305")

    label("loc_1302")

    Jump("loc_1305")

    label("loc_1305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1324")
    OP_64(0x3, 0x1)

    label("loc_1324")

    TalkEnd(0xFF)
    Return()

    # Function_3_10C7 end

    SaveToFile()

Try(main)
