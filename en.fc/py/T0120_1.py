from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0120_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0120.x',
        MapIndex            = 1,
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_6CC",          # 01, 1
        "Function_2_112D",         # 02, 2
        "Function_3_157D",         # 03, 3
    )


    def Function_0_66(): pass

    label("Function_0_66")

    OP_A2(0x228)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266")

    ChrTalk(    #0
        0x8,
        (
            "Well, hey there!\x01",
            "You two new bracers seem to\x01",
            "be having some success lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "I've been hearing a lot about\x01",
            "your hard work recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#006FYeah, that's because we're\x01",
            "still new at this, so we have\x01",
            "to work extra hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "That's encouraging to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "You guys actually came at a good\x01",
            "time. I've got an urgent job that\x01",
            "needs to be taken care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "Do you think that you'd be up to the task\x01",
            "of replacing an Orbment Light in a road\x01",
            "lamp along the Milch Main Road?\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 1)
    Jump("loc_302")

    label("loc_266")


    def lambda_26C():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_26C)
    TurnDirection(0x1, 0x8, 400)

    ChrTalk(    #6
        0x8,
        "Hey there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "So, can I get you to replace the\x01",
            "Orbment Light in that road lamp\x01",
            "for me?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_2FE")
    Call(1, 2)
    Jump("loc_302")

    label("loc_2FE")

    Call(1, 1)

    label("loc_302")

    Jump("loc_6C1")

    label("loc_305")


    ChrTalk(    #8
        0x8,
        (
            "Can I help you with\x01",
            "something else?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BE")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Confirm the combination]\x01",      # 0
            "[Cancel the job]\x01",               # 1
            "[Never mind]\x01",                   # 2
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3BC"),
        (1, "loc_4FA"),
        (2, "loc_692"),
        (SWITCH_DEFAULT, "loc_692"),
    )


    label("loc_3BC")


    ChrTalk(    #9
        0x8,
        (
            "I want you to replace the Orbment\x01",
            "Light in road lamp no. 6 on the\x01",
            "Milch Main Road to the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "It's the 6th road lamp that\x01",
            "you'll come across counting\x01",
            "from Rolent's west entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "The maintenance panel combination\x01",
            "is 544818. Make sure you don't\x01",
            "forget it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "And good luck on the job.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6BB")

    label("loc_4FA")

    OP_28(0x6, 0x3, 0x8)
    OP_28(0x6, 0x1, 0x8000)

    ChrTalk(    #13
        0x101,
        (
            "#003FI'm really sorry, Freddy, but we\x01",
            "had something urgent come up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "Really? I guess there's nothing\x01",
            "you can do about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "Anyway, why don't you return\x01",
            "the replacement for now?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00Returned \x07\x02Orbment Light\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x327, 1)
    Sleep(100)

    ChrTalk(    #17
        0x8,
        (
            "Let me know as soon\x01",
            "as you're done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "The reason being,\x01",
            "this is pretty urgent as well.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6BB")

    label("loc_692")


    ChrTalk(    #19
        0x8,
        "I'll see you later.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6BB")

    label("loc_6BB")

    Jump("loc_32E")

    label("loc_6BE")

    OP_5F(0x0)

    label("loc_6C1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_66 end

    def Function_1_6CC(): pass

    label("Function_1_6CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1122")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_731"),
        (1, "loc_1024"),
        (SWITCH_DEFAULT, "loc_1024"),
    )


    label("loc_731")

    OP_28(0x6, 0x4, 0x8)
    OP_28(0x6, 0x4, 0x4)
    OP_28(0x6, 0x4, 0x2)
    OP_28(0x6, 0x1, 0x1)
    OP_28(0x6, 0x1, 0x2)

    ChrTalk(    #20
        0x101,
        "#006FYou just leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#010FIf you're fine with us doing the\x01",
            "job, then we'll gladly accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "Thanks, I really appreciate this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "I completely forgot it needed\x01",
            "to be replaced today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "First off, I'll need to give you\x01",
            "the replacement part.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x00Received \x07\x02Orbment Light\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x327, 1)
    Sleep(100)

    ChrTalk(    #26
        0x101,
        "#000FThis is the replacement orbment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "I want you to replace the Orbment\x01",
            "Light in road lamp no. 6 on the\x01",
            "Milch Main Road to the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "It's the 6th road lamp that\x01",
            "you'll come across counting\x01",
            "from Rolent's west entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "Make sure you get the right one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#000FI think I've got it.\x02\x03",

            "The 6th road lamp from Rolent's\x01",
            "west entrance, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "Once you've found the road lamp,\x01",
            "you'll need to open the maintenance\x01",
            "panel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "You'll need a 6-digit combination\x01",
            "to open it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#004FAre you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "Yep. The combination for the\x01",
            "6th road lamp is 544818.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #36
        0x101,
        (
            "#008FI'm sorry, but could you repeat\x01",
            "that again...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        "#010FIt's 544818.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "That's right.\x01",
            "Good memory, Joshua.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #39
        0x101,
        "#009FShow-off...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #40
        0x8,
        (
            "After the combination is entered the\x01",
            "panel will open. And after that, all\x01",
            "that's left is to replace the orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "It may seem like a simple task,\x01",
            "but make sure not to mess it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "The road lamp may have been\x01",
            "out of order for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#010FI see.\x02\x03",

            "#010FThe light of the orbments keep\x01",
            "the large monsters away, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #44
        0x8,
        (
            "It's not much more than an\x01",
            "unconscious dislike for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "But if they do go out, then we\x01",
            "run into real problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "Which is why I'm asking you\x01",
            "to do this job, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "These road lamps are placed just off\x01",
            "the roads in areas where monsters\x01",
            "are most likely to appear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#505FWell, you just leave those monsters\x01",
            "to me and I'll take care of them.\x02\x03",

            "But I'd better write down that\x01",
            "combination before I forget...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #49
        0x102,
        (
            "#010FThen, maybe you should let\x01",
            "me deal with the combination\x01",
            "instead.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #50
        0x8,
        (
            "I'll leave it up to you two to\x01",
            "divide up the work amongst\x01",
            "yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "That should be everything you\x01",
            "need to know, so good luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "If you need to double-check or\x01",
            "cancel the job, then come and\x01",
            "talk with me again.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_111C")

    label("loc_1024")

    OP_28(0x6, 0x1, 0x8000)

    ChrTalk(    #53
        0x101,
        (
            "#505FI'm really sorry, Freddy, but we\x01",
            "had something else come up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "Really? I guess there's nothing\x01",
            "you can do about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "Let me know as soon\x01",
            "as you're done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "The reason being, this is\x01",
            "pretty urgent as well.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_111C")

    label("loc_111C")

    OP_5F(0x0)
    Jump("Function_1_6CC")

    label("loc_1122")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_6CC end

    def Function_2_112D(): pass

    label("Function_2_112D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156F")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_1192"),
        (1, "loc_145B"),
        (SWITCH_DEFAULT, "loc_145B"),
    )


    label("loc_1192")

    OP_28(0x6, 0x4, 0x8)

    ChrTalk(    #57
        0x101,
        (
            "#006FWe finished with our other errand,\x01",
            "so we can take care of this now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "I've already explained everything\x01",
            "to you, so all you need is this.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x00Received \x07\x02Orbment Light\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x327, 1)
    Sleep(100)

    ChrTalk(    #60
        0x8,
        (
            "The key points I'd like to confirm\x01",
            "with you are as follows...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "I want you to replace the Orbment\x01",
            "Light in road lamp no. 6 on the\x01",
            "Milch Main Road to the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "It's the 6th road lamp that\x01",
            "you'll come across counting\x01",
            "from Rolent's west entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "The maintenance panel\x01",
            "combination is 544818.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "That's pretty much it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "Good luck on the job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "If you need to double-check or\x01",
            "cancel the job, then come and\x01",
            "talk with me again.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_156C")

    label("loc_145B")

    OP_28(0x6, 0x1, 0x8000)

    ChrTalk(    #67
        0x101,
        (
            "#003FI'm really sorry, Freddy, but we\x01",
            "had yet another errand come up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "You children are starting to break\x01",
            "my heart... But, I guess you have\x01",
            "your priorities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "Let me know as soon as\x01",
            "you're done, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        "This is pretty urgent as well.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_156C")

    label("loc_156C")

    Jump("Function_2_112D")

    label("loc_156F")

    OP_5F(0x0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_112D end

    def Function_3_157D(): pass

    label("Function_3_157D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1593")
    Jump("loc_15BB")

    label("loc_1593")


    ChrTalk(    #71
        0x8,
        "このメッセージを見てたらバグ有り。\x02",
    )

    CloseMessageWindow()

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3A")
    EventBegin(0x0)
    OP_28(0x6, 0x4, 0x10)
    OP_28(0x6, 0x1, 0x10)

    ChrTalk(    #72
        0x101,
        "#001FWe're back, Freddy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "Oh, hi, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "From the look on your face, it\x01",
            "seems like you finished the job.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        (
            "#006FYep. And we did a fine job, too.\x02\x03",

            "Although we did have a few\x01",
            "hang ups...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        (
            "#010FWe thought we'd report to you\x01",
            "as a matter of good measure.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #77
        (
            "\x07\x05Reported the events which occurred\x01",
            "on the Milch Main Road.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #78
        0x8,
        (
            "So it really was burnt out, huh?\x01",
            "I'm sure it happened because\x01",
            "we were late replacing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "Sorry, kids.\x01",
            "You were put in harm's\x01",
            "way because of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#000FThere's no need to apologize.\x02\x03",

            "#000FIt comes with the territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        (
            "#010FDealing with dangerous jobs\x01",
            "is a part of a bracer's work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        "I appreciate you saying that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #83
        0x8,
        (
            "Oh, I know. How about I give\x01",
            "you this to make amends?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x00Received \x07\x02Impede 2\x07\x00 quartz.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x2C2, 1)
    Sleep(100)

    ChrTalk(    #85
        0x101,
        "#004FThis is a quartz?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        "Yep. It's an Impede 2 quartz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        "It can prevent an enemy's arts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "It can be pretty useful if\x01",
            "you use it effectively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#001FThanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        "#010FWe appreciate it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #91
        0x8,
        (
            "No, thank you to the both\x01",
            "of you today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "If you need to discuss anything\x01",
            "about orbments, then stop by\x01",
            "any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "Don't forget to swing by if you\x01",
            "have any other business needs.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #94
        "\x07\x00Quest \x07\x02[Orbment Replacement] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)
    Jump("loc_1BCA")

    label("loc_1B3A")


    ChrTalk(    #95
        0x8,
        (
            "If you need to discuss anything\x01",
            "about orbments, then stop by\x01",
            "any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "Don't forget to swing by if you\x01",
            "have any other business needs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCA")

    Return()

    # Function_3_157D end

    SaveToFile()

Try(main)
