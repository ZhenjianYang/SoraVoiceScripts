from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2120_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        "Function_1_107",          # 01, 1
        "Function_2_3B9",          # 02, 2
        "Function_3_120D",         # 03, 3
        "Function_4_1503",         # 04, 4
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_8A")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0x1D, 0x1E, 0x1F, 0x20, 0x23, 0x25, 0xFFFF)
    Jump("loc_103")

    label("loc_8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_AB")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0x1D, 0x1E, 0x1F, 0x20, 0x23, 0x25, 0xFFFF)
    Jump("loc_103")

    label("loc_AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_CA")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0x1D, 0x1E, 0x1F, 0x20, 0x23, 0xFFFF)
    Jump("loc_103")

    label("loc_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_E9")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0x1D, 0x1E, 0x1F, 0x20, 0x23, 0xFFFF)
    Jump("loc_103")

    label("loc_E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_FE")
    OP_2A(0x24, 0x21, 0x22, 0x26, 0xFFFF)
    Jump("loc_103")

    label("loc_FE")

    OP_2A(0x24, 0xFFFF)

    label("loc_103")

    TalkEnd(0xFF)
    Return()

    # Function_0_66 end

    def Function_1_107(): pass

    label("Function_1_107")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_233")
    OP_A2(0xB)
    OP_28(0x1D, 0x1, 0x8000)

    ChrTalk(    #0
        0xB,
        (
            "Whoops... I guess you managed\x01",
            "okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#010FThe delivery went pretty smoothly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#001FAnd the old man was doing well.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #3
        0xB,
        "Ah, okay. Sounds good, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        (
            "Later, then. I'll be in touch if\x01",
            "anything comes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#010FTake care, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#001FSee you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B5")

    label("loc_233")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26D")

    ChrTalk(    #7
        0xB,
        "Is something wrong?\x02",
    )

    CloseMessageWindow()
    Call(1, 3)
    Jump("loc_3B5")

    label("loc_26D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_2EF")

    ChrTalk(    #8
        0xB,
        "Finished with your other work now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        (
            "I really need this Maintenance Kit\x01",
            "delivered. Are you ready to go?\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_3B5")

    label("loc_2EF")


    ChrTalk(    #10
        0x101,
        (
            "#000FUm, Mr. Tobias?\x02\x03",

            "We came here from the guild...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #11
        0xB,
        (
            "Oh, this is about the Maintenance Kit,\x01",
            "no? Your timing is exemplary!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xB,
        (
            "Will you be able to make the delivery\x01",
            "post haste?\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)

    label("loc_3B5")

    TalkEnd(0xB)
    Return()

    # Function_1_107 end

    def Function_2_3B9(): pass

    label("Function_2_3B9")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_415"),
        (1, "loc_111E"),
        (SWITCH_DEFAULT, "loc_1209"),
    )


    label("loc_415")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_5BB")
    OP_28(0x1D, 0x4, 0x8)

    ChrTalk(    #13
        0xB,
        (
            "Well, then... This brick of a\x01",
            "thing is all yours!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #14
        "\x07\x00Received \x07\x02Maintenance Kit\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x326, 1)

    ChrTalk(    #15
        0xB,
        (
            "Deliver it directly to Mr. Vogt\x01",
            "at the Varenne Lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xB,
        (
            "Its contents are quite valuable, so\x01",
            "please be as careful as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xB,
        (
            "The Varenne Lighthouse is on the\x01",
            "coast, just to the south of Manoria\x01",
            "Village in the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        "And, there you have it!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Jump("loc_111B")

    label("loc_5BB")

    OP_28(0x1D, 0x4, 0x4)
    OP_28(0x1D, 0x4, 0x8)
    OP_28(0x1D, 0x1, 0x1)
    OP_28(0x1D, 0x1, 0x2)

    ChrTalk(    #19
        0xB,
        (
            "This brick of a thing is all\x01",
            "yours now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#004FBrick...of a thing?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 400)

    ChrTalk(    #21
        0xB,
        (
            "Are you daft? I'm telling you it's\x01",
            "heavy! Very, very heavy! Here--\x01",
            "feel for yourself!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x00Received \x07\x02Maintenance Kit\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x326, 1)

    ChrTalk(    #23
        0xB,
        (
            "You okay with it? No bone fractures\x01",
            "forming, to your knowledge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "It's filled to the brim with replacement\x01",
            "parts and every tool you can imagine for\x01",
            "replacing an orbment light of that size.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#000FIt's no big deal at all. I'm stronger\x01",
            "than I look, believe me! We just need\x01",
            "to carry this to the lighthouse, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #26
        0xB,
        (
            "Indeed. To Vogt, the lighthouse keeper.\x01",
            "He's expecting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "Its contents are quite valuable, so\x01",
            "please be as careful as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xB,
        (
            "...I still can't believe it.\x01",
            "Such responsibility! Such strength!\x01",
            "Such grace! Ah, youth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#000FUh...what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        (
            "Jean told me about you two, but\x01",
            "seeing for myself just how peppy\x01",
            "you are lifts my spirits to the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#506FPeppy? No, no, we're just...uh...\x01",
            "professional?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "You're young, that's what you are! And naturally,\x01",
            "I was worried entrusting something so valuable to\x01",
            "potentially reckless youths...but I worry no more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#009FHmph...\x02\x03",

            "We may be young, but that doesn't\x01",
            "automatically mean we're reckless!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #34
        0xB,
        (
            "Oh...no, no! You've got it\x01",
            "all wrong!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xB,
        (
            "I just meant that I wasn't sure\x01",
            "how old man Vogt would take it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_C67")

    ChrTalk(    #36
        0x101,
        "#505FAhh, yeah, that's a good point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        "What, you know Vogt?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#506FYeah, we helped him out when he\x01",
            "was in a bit of a pickle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#017FLet's...just leave it at that,\x01",
            "yeah.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #40
        0xB,
        (
            "Ha ha ha. He leave the door open\x01",
            "again? Either way, you know what\x01",
            "I'm talking about, it seems!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D87")

    label("loc_C67")


    ChrTalk(    #41
        0x101,
        "#000FOh? Why do you say that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#010FIs there something we should\x01",
            "know about him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "Well...you might say he's a bit\x01",
            "of an eccentric.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xB,
        (
            "He can be a little abrasive when\x01",
            "it comes to younger people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#509F...So in other words, he's a\x01",
            "weirdo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xB,
        "That's one way to put it.\x02",
    )

    CloseMessageWindow()

    label("loc_D87")

    TurnDirection(0xB, 0x0, 400)

    ChrTalk(    #47
        0xB,
        (
            "Just try to understand where\x01",
            "he's coming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "Being a lighthouse keeper is lonely\x01",
            "work, so a little eccentricity is to\x01",
            "be expected.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #49
        0x105,
        (
            "#040FThe lighthouse is crucial for ships\x01",
            "to be able to navigate safely...\x02\x03",

            "So the keeper's work is a very\x01",
            "big responsibility.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #50
        0x101,
        "#003FGot'cha. So, really important work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xB,
        (
            "When he was a fisherman, he\x01",
            "used to down plenty of drinks\x01",
            "at Lavantar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        (
            "Now that he lives at the lighthouse,\x01",
            "though, he rarely gets a chance to\x01",
            "have his favorite drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        (
            "It's pretty sad. I'd really like to\x01",
            "go ahead with getting him what\x01",
            "he wants, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        "...well, I've probably said too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xB,
        (
            "Either way, don't let the old man's\x01",
            "unpleasantness get to you, okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #56
        0x101,
        (
            "#000FOkay, got it.\x02\x03",

            "Is there anything else before\x01",
            "we go?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #57
        0xB,
        (
            "Nothing in particular. Once you're\x01",
            "done, I'd like you to return here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        "Take care, and I'll see you later.\x02",
    )

    CloseMessageWindow()

    label("loc_111B")

    Jump("loc_1209")

    label("loc_111E")

    OP_28(0x1D, 0x1, 0x4000)

    ChrTalk(    #59
        0x101,
        (
            "#505FHmmm...well, right now is no\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #60
        0xB,
        (
            "All right. Once you've completed\x01",
            "your other errands, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        (
            "This is rather urgent business, after\x01",
            "all. If you want in, I'll need you\x01",
            "here as soon as you can manage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1209")

    label("loc_1209")

    TalkEnd(0xB)
    Return()

    # Function_2_3B9 end

    def Function_3_120D(): pass

    label("Function_3_120D")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Confirm job info]\x01",      # 0
            "[Cancel request]\x01",        # 1
            "[Never mind]\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1293"),
        (1, "loc_1353"),
        (2, "loc_14DE"),
        (SWITCH_DEFAULT, "loc_14FF"),
    )


    label("loc_1293")


    ChrTalk(    #62
        0xB,
        (
            "I just need you to take that\x01",
            "Maintenance Kit to Vogt at\x01",
            "the Varenne Lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "It's on the coast, just to the\x01",
            "south of Manoria Village in the\x01",
            "west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        "I'll be counting on you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14FF")

    label("loc_1353")

    OP_28(0x1D, 0x3, 0x8)
    OP_28(0x1D, 0x1, 0x4000)

    ChrTalk(    #65
        0x101,
        (
            "#007FI'm sorry, Tobias...\x01",
            "We've got so much going\x01",
            "on right now...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #66
        0xB,
        (
            "I understand. You can't help \x01",
            "it if you have other duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        (
            "If I could just get back my\x01",
            "property...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #68
        "\x07\x00Returned \x07\x02Maintenance Kit\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x326, 1)

    ChrTalk(    #69
        0xB,
        (
            "This is rather urgent business, after\x01",
            "all. If you want in, I'll need you\x01",
            "here as soon as you can manage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FF")

    label("loc_14DE")


    ChrTalk(    #70
        0xB,
        "I'll be counting on you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14FF")

    label("loc_14FF")

    TalkEnd(0xB)
    Return()

    # Function_3_120D end

    def Function_4_1503(): pass

    label("Function_4_1503")

    OP_28(0x22, 0x4, 0x10)
    OP_28(0x22, 0x1, 0x4)
    OP_A2(0x1)
    OP_3F(0x67, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1859")

    ChrTalk(    #71
        0x101,
        "#501FIs this the prototype gun?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #72
        "\x07\x00Handed over \x07\x020-Type Test Model\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(800)

    ChrTalk(    #73
        0xFE,
        "Whoa...! H-How...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "How did you get your hands\x01",
            "on this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#010FA monster near the Sapphirl\x01",
            "Tower had it.\x02\x03",

            "It probably wanted it for\x01",
            "the septium mechanism.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #76
        0xFE,
        (
            "In Aidios' name, thank you so\x01",
            "much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "Ohhh...thank goodness you found it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#000FAnd now we've fulfilled your\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        "#010FPardon us, but we must be going.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #80
        0xFE,
        "Wh-Why are you in such a hurry?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(    #81
        0xFE,
        "Please, at least take this with you.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #82
        "\x07\x00Received \x07\x02Attack 2\x07\x00 Quartz.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #83
        0xFE,
        "Just a token of my appreciation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I wish you luck on your future\x01",
            "endeavors!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#508FThanks!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FF4")

    label("loc_1859")


    ChrTalk(    #86
        0x101,
        (
            "#002FHey, do you think...\x02\x03",

            "Is this the prototype gun?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #87
        "\x07\x00Handed over \x07\x020-Type Test Model\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(800)

    ChrTalk(    #88
        0xFE,
        "Whoa...! H-How...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "How did you get your hands\x01",
            "on this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        (
            "#010FA monster near the Sapphirl\x01",
            "Tower had it.\x02\x03",

            "It probably wanted it for\x01",
            "the septium mechanism.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #91
        0xFE,
        (
            "In Aidios' name, thank you so\x01",
            "much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Ohhh...I don't have the words!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #93
        0xFE,
        (
            "I could give you each a huge hug\x01",
            "and a kiss!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #94
        0x101,
        (
            "#008FAck...\x02\x03",

            "I-I'm okay!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1AB5")
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #95
        0x105,
        "#045FA-As am I...\x02",
    )

    CloseMessageWindow()

    label("loc_1AB5")


    ChrTalk(    #96
        0x102,
        "#018FNo, but thank you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #97
        0xFE,
        (
            "Even the manly girl with pigtails\x01",
            "turned me down... *sniffle*\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #98
        0x102,
        (
            "#010FIs the prototype really that\x01",
            "important?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "Most certainly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "It's being actively worked on at\x01",
            "the Zeiss central lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "It's not ready for public sale\x01",
            "and distribution yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#004FWow, it must be really effective,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #103
        0xFE,
        "Are you interested in weaponry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Ha, I guess that's a stupid question.\x01",
            "As bracers, of course you'd be\x01",
            "interested in them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Well, then, let me give you this\x01",
            "quartz as a token of my appreciation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "I'm sure it should come in handy.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #107
        "\x07\x00Received \x07\x02Attack 2\x07\x00 Quartz.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #108
        0x102,
        (
            "#014FI'm sorry, but we can't accept\x01",
            "something this nice...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #109
        0xFE,
        "Oh, please. It's the least I can do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "And of course, the guild will pay\x01",
            "you for your time and effort, as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #111
        0x101,
        "#004FIn mira, I hope!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #112
        0xFE,
        "Certainly. You needn't worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Right from the central lab's\x01",
            "coffers to your wallets!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #114
        0x101,
        (
            "#509FI just meant, instead of hugs\x01",
            "and kisses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "It's quite all right. You should\x01",
            "simply accept your reward at\x01",
            "times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Again, thank you for what you've\x01",
            "done today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I'm sure you'll hear from me again,\x01",
            "should anything else come up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF4")

    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #118
        "\x07\x00Quest \x07\x02[Find the Prototype!] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_3E(0x25F, 1)
    OP_8C(0xFE, 0, 400)
    EventEnd(0x1)
    TalkEnd(0xC)
    Return()

    # Function_4_1503 end

    SaveToFile()

Try(main)
