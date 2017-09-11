from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0130.x',
        MapIndex            = 3,
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
        "Function_1_335",          # 01, 1
        "Function_2_95A",          # 02, 2
        "Function_3_E50",          # 03, 3
        "Function_4_130D",         # 04, 4
        "Function_5_17BD",         # 05, 5
        "Function_6_1D4E",         # 06, 6
        "Function_7_20F6",         # 07, 7
        "Function_8_2704",         # 08, 8
        "Function_9_272A",         # 09, 9
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7")
    OP_28(0x7, 0x1, 0x8000)

    ChrTalk(    #0
        0x8,
        (
            "Well, good morning, everyone. Are\x01",
            "you going on a journey somewhere?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #1
        0x101,
        "#000FYeah, just over to Bose.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #2
        0x8,
        "Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "Then in that case could I ask a\x01",
            "favor of you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "I had wanted to send Father Holstein\x01",
            "a letter, but the airliners are grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "So how about it? Can I get you to\x01",
            "deliver this letter while you're there\x01",
            "in Bose?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D")

    label("loc_1E7")


    ChrTalk(    #6
        0x8,
        (
            "By the way... You said you were\x01",
            "headed to Bose, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #7
        0x101,
        "#000FYeah, that's right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #8
        0x8,
        (
            "Then in that case could I ask a\x01",
            "favor of you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "I had wanted to send Father Holstein\x01",
            "a letter, but the airliners are grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "So how about it? Can I get you to\x01",
            "deliver this letter while you're there\x01",
            "in Bose?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D")

    Call(1, 3)
    TalkEnd(0x8)
    Return()

    # Function_0_66 end

    def Function_1_335(): pass

    label("Function_1_335")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE678), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_38C")
    SetChrPos(0x101, 60600, 1000, 52500, 270)
    SetChrPos(0x102, 60600, 1000, 51300, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_389")
    SetChrPos(0x103, 61600, 1000, 50200, 315)

    label("loc_389")

    Jump("loc_3C6")

    label("loc_38C")

    SetChrPos(0x101, 57400, 1000, 52500, 90)
    SetChrPos(0x102, 57400, 1000, 51300, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3C6")
    SetChrPos(0x103, 56400, 1000, 50200, 45)

    label("loc_3C6")

    OP_69(0x101, 0x7D0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7")
    OP_28(0x7, 0x1, 0x8000)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #11
        0x8,
        (
            "Well, good morning, everyone. Are\x01",
            "you going on a journey somewhere?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #12
        0x101,
        (
            "#000FYep.\x02\x03",

            "Just over to Bose, but before we\x01",
            "left there was something we\x01",
            "wanted to give you...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #13
        0x8,
        "To me...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_57A")

    label("loc_4B7")

    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #14
        0x8,
        (
            "Well, good morning, everyone.\x01",
            "I thought you'd have left by now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #15
        0x101,
        (
            "#000FWell...\x02\x03",

            "Actually, there was something we\x01",
            "wanted to give you before that...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #16
        0x8,
        "To me...?\x02",
    )

    CloseMessageWindow()

    label("loc_57A")

    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #17
        "\x07\x00Handed over \x07\x02Bear Claw\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #18
        "\x07\x00Handed over \x07\x02Savory Pinion\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #19
        0x8,
        "This is...?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #20
        0x102,
        (
            "#010FThe Bear Claw and Savory Pinion\x01",
            "you were looking for. Please use\x01",
            "them as medicinal ingredients.\x02\x03",

            "You requested these at the guild,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #21
        0x8,
        "That's right. I did put in a request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "I'm just surprised that you went to\x01",
            "all the trouble to do this for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "My thanks to the both of you,\x01",
            "Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "It appears that you both are\x01",
            "doing a wonderful job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "This is encouraging to know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#000FWe'll try to do our best.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #27
        0x8,
        (
            "With that attitude, I have nothing\x01",
            "to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "Make sure to act with caution\x01",
            "wherever your travels take you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "I pray that the Goddess will guide\x01",
            "you on your journey.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x00Quest \x07\x02[Medical Necessities] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x386, 1)
    OP_3F(0x39F, 1)
    OP_28(0x7, 0x4, 0x10)
    OP_28(0x7, 0x1, 0x1)
    OP_A2(0x1)
    OP_8C(0x8, 180, 0)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_1_335 end

    def Function_2_95A(): pass

    label("Function_2_95A")

    TalkBegin(0x8)

    ChrTalk(    #31
        0x8,
        (
            "Is there something else I can\x01",
            "help you with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "Or have you decided to deliver\x01",
            "a letter for me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E42")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A29"),
        (1, "loc_CC0"),
        (SWITCH_DEFAULT, "loc_E3F"),
    )


    label("loc_A29")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0xD, 0x4, 0x8)
    OP_28(0xD, 0x1, 0x1)
    OP_3E(0x329, 1)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #33
        0x101,
        "#000FSure, we'll do it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_ABE")

    ChrTalk(    #34
        0x103,
        (
            "#020FIt's just a letter, so sure.\x01",
            "Certainly doesn't take up much space!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABE")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #35
        0x8,
        "I really appreciate this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        "All right then, here you are.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x00Received \x07\x02Fr. Divine's Letter\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #38
        0x102,
        (
            "#010FSo all we need to do is give this\x01",
            "letter to Father Holstein in Bose,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #39
        0x8,
        (
            "Yes. The chapel is on the east\x01",
            "side of Bose City, so it should\x01",
            "be fairly easy to locate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "Traveling around other regions\x01",
            "and broadening your knowledge\x01",
            "is food for the mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "I pray that the Goddess will\x01",
            "guide you on your journey.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3F")

    label("loc_CC0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0xD, 0x1, 0x8000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #42
        0x101,
        (
            "#003FUm, I'm really sorry about this,\x01",
            "but I don't think we can do it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "Is that so? I suppose the Goddess\x01",
            "will forgive you...this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "However, there are many things\x01",
            "out there where haste can lead\x01",
            "to danger...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "Make sure to act with caution\x01",
            "wherever your travels take you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "I pray that the Goddess will\x01",
            "guide you on your journey.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3F")

    label("loc_E3F")

    Jump("loc_9C4")

    label("loc_E42")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_2_95A end

    def Function_3_E50(): pass

    label("Function_3_E50")

    OP_28(0xD, 0x4, 0x4)
    OP_28(0xD, 0x4, 0x2)

    label("loc_E5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12FF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EBF"),
        (1, "loc_1145"),
        (SWITCH_DEFAULT, "loc_12FC"),
    )


    label("loc_EBF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0xD, 0x4, 0x8)
    OP_28(0xD, 0x1, 0x1)
    OP_3E(0x329, 1)

    ChrTalk(    #47
        0x101,
        "#000FSure, we'll do it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_F51")

    ChrTalk(    #48
        0x103,
        (
            "#020FIt shouldn't be a problem since a\x01",
            "letter's not that big to begin with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F51")


    ChrTalk(    #49
        0x8,
        "I really appreciate this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        "All right then, here you are.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #51
        "\x07\x00Received \x07\x02Fr. Divine's Letter\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #52
        0x102,
        (
            "#010FSo all we need to do is give this\x01",
            "letter to Father Holstein in Bose,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(    #53
        0x8,
        (
            "Yes. The chapel is on the east\x01",
            "side of Bose City, so it should\x01",
            "be fairly easy to locate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "Traveling around other regions\x01",
            "and broadening your knowledge\x01",
            "is food for the mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "I pray that the Goddess will\x01",
            "guide you on your journey.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FC")

    label("loc_1145")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0xD, 0x1, 0x8000)

    ChrTalk(    #56
        0x101,
        (
            "#003FI'm really sorry about this Father,\x01",
            "but we've got some urgent business\x01",
            "that needs attending to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "Is that so? I suppose the Goddess\x01",
            "will forgive you...this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "However, there are many things\x01",
            "out there where haste can lead\x01",
            "to danger...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "Make sure to act with caution\x01",
            "wherever your travels take you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#000FSure, I'll do that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "I pray that the Goddess will\x01",
            "guide you on your journey.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FC")

    label("loc_12FC")

    Jump("loc_E5A")

    label("loc_12FF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_3_E50 end

    def Function_4_130D(): pass

    label("Function_4_130D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE678), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13C0")
    SetChrPos(0x101, 60600, 1000, 52500, 270)
    SetChrPos(0x102, 60600, 1000, 51300, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137C")
    SetChrPos(0x2, 61600, 1000, 51500, 270)
    SetChrPos(0x3, 61600, 1000, 50200, 315)
    Jump("loc_13BD")

    label("loc_137C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_139E")
    SetChrPos(0x2, 61600, 1000, 51500, 270)
    Jump("loc_13BD")

    label("loc_139E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BD")
    SetChrPos(0x103, 61600, 1000, 51500, 270)

    label("loc_13BD")

    Jump("loc_1456")

    label("loc_13C0")

    SetChrPos(0x101, 57400, 1000, 52500, 90)
    SetChrPos(0x102, 57400, 1000, 51300, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1415")
    SetChrPos(0x2, 56400, 1000, 51500, 90)
    SetChrPos(0x3, 56400, 1000, 50200, 45)
    Jump("loc_1456")

    label("loc_1415")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1437")
    SetChrPos(0x2, 56400, 1000, 51500, 90)
    Jump("loc_1456")

    label("loc_1437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1456")
    SetChrPos(0x103, 56400, 1000, 51500, 90)

    label("loc_1456")

    OP_69(0x101, 0x7D0)
    OP_0D()
    TurnDirection(0x8, 0x101, 400)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14F7")

    ChrTalk(    #62
        0x8,
        (
            "Well, if it isn't Estelle and Joshua!\x01",
            "Is there something I can help you\x01",
            "with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#000FThese are for you, Father Divine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15A8")

    label("loc_14F7")


    ChrTalk(    #64
        0x8,
        "Well, if it isn't Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "You seem to be in a cheerful\x01",
            "mood as usual.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #66
        0x101,
        (
            "#001FTee hee.\x02\x03",

            "Here you are. These are for you,\x01",
            "Father Divine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A8")

    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #67
        "\x07\x00Handed over \x07\x02Bear Claw\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #68
        "\x07\x00Handed over \x07\x02Savory Pinion\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #69
        0x8,
        "This is...?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #70
        0x102,
        (
            "#010FThe Bear Claw and Savory Pinion\x01",
            "you were looking for. Please use\x01",
            "them as medicinal ingredients.\x02\x03",

            "You requested these at the guild,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #71
        0x8,
        "That's right. I did put in a request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "I'm just surprised that you went to\x01",
            "all the trouble to do this for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "Weren't you hurt trying to\x01",
            "gather these?\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 5)
    Return()

    # Function_4_130D end

    def Function_5_17BD(): pass

    label("Function_5_17BD")


    ChrTalk(    #74
        0x101,
        (
            "#001FNope, we were totally fine. ♪\x02\x03",

            "#000F...I mean...we were fine...well, maybe\x01",
            "minus the 'totally' part...heh heh heh...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #75
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "I'm worried about your attitude,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#004FEh...?! Why? There's nothing to\x01",
            "be worried about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        "I know I've told you this before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "It's certainly a joyous occasion\x01",
            "when everything goes well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "However, it is at these times when\x01",
            "we should gird up our loins for the\x01",
            "trials that lie ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#007FO-kay. I'll be more careful from\x01",
            "now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "Hmm...since I seem to have\x01",
            "a bit of spare time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "How about I take this opportunity\x01",
            "to give you a special sermon...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #84
        0x101,
        (
            "#004F(NOOOOO, anything but that...)\x02\x03",

            "#506FI-I'm sorry, Father, but we've\x01",
            "really got to get going.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B27")

    ChrTalk(    #85
        0x102,
        (
            "#010FPlease excuse us, Father. We've\x01",
            "actually got an urgent mission\x01",
            "that needs our attention.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF5")

    label("loc_1B27")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #86
        0x101,
        (
            "#506FYou've still got work left to do,\x01",
            "right, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#017F(Why do you have to bring\x01",
            "me into this...?)\x02\x03",

            "#010FPlease excuse us, Father, but\x01",
            "we have to get back to the guild...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BED():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BED)

    label("loc_1BF5")

    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #88
        0x8,
        (
            "That's too bad. However, since it\x01",
            "has to do with your job I must\x01",
            "respect your position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "Thank you for all your hard work,\x01",
            "Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "I pray that the Goddess will always\x01",
            "be with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #91
        "\x07\x00Quest \x07\x02[Medical Necessities] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x386, 1)
    OP_3F(0x39F, 1)
    OP_28(0x7, 0x4, 0x10)
    OP_28(0x7, 0x1, 0x1)
    OP_A2(0x1)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_5_17BD end

    def Function_6_1D4E(): pass

    label("Function_6_1D4E")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0xE, 59100, 0, 45800, 0)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0x101, 59800, 0, 41000, 0)
    SetChrPos(0x102, 58700, 0, 40000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC5")
    SetChrPos(0x2, 59600, 0, 39000, 0)
    SetChrPos(0x3, 58600, 0, 38500, 0)
    Jump("loc_1DE4")

    label("loc_1DC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE4")
    SetChrPos(0x2, 59600, 0, 39000, 0)

    label("loc_1DE4")

    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    OP_6D(59100, 0, 45800, 3000)
    TurnDirection(0xE, 0x101, 0)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)

    ChrTalk(    #92
        0x101,
        (
            "#507FMwahaha... There's nowhere\x01",
            "left to run, little kitty.\x02\x03",

            "It's time to be caught!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0xE, 135, 400)
    Sleep(500)
    OP_8C(0xE, 225, 400)
    Sleep(500)
    SetChrPos(0xD, 59100, 0, 45800, 180)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xD, 0x40)
    OP_8F(0xD, 0xE6DC, 0x0, 0xB6D0, 0xBB8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F8A")

    def lambda_1F10():

        label("loc_1F10")

        TurnDirection(0x101, 0xD, 0)
        OP_48()
        Jump("loc_1F10")

    QueueWorkItem2(0x101, 1, lambda_1F10)

    def lambda_1F21():

        label("loc_1F21")

        TurnDirection(0x102, 0xD, 0)
        OP_48()
        Jump("loc_1F21")

    QueueWorkItem2(0x102, 1, lambda_1F21)

    def lambda_1F32():

        label("loc_1F32")

        TurnDirection(0x8, 0xD, 0)
        OP_48()
        Jump("loc_1F32")

    QueueWorkItem2(0x8, 1, lambda_1F32)

    def lambda_1F43():

        label("loc_1F43")

        TurnDirection(0x10F, 0xD, 0)
        OP_48()
        Jump("loc_1F43")

    QueueWorkItem2(0x10F, 1, lambda_1F43)

    def lambda_1F54():

        label("loc_1F54")

        TurnDirection(0x110, 0xD, 0)
        OP_48()
        Jump("loc_1F54")

    QueueWorkItem2(0x110, 1, lambda_1F54)
    OP_8E(0xD, 0xC224, 0x0, 0xC8C8, 0x1B58, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x10F, 0xFF)
    OP_44(0x110, 0xFF)
    Jump("loc_204F")

    label("loc_1F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_1FFC")

    def lambda_1F97():

        label("loc_1F97")

        TurnDirection(0x101, 0xD, 0)
        OP_48()
        Jump("loc_1F97")

    QueueWorkItem2(0x101, 1, lambda_1F97)

    def lambda_1FA8():

        label("loc_1FA8")

        TurnDirection(0x102, 0xD, 0)
        OP_48()
        Jump("loc_1FA8")

    QueueWorkItem2(0x102, 1, lambda_1FA8)

    def lambda_1FB9():

        label("loc_1FB9")

        TurnDirection(0x8, 0xD, 0)
        OP_48()
        Jump("loc_1FB9")

    QueueWorkItem2(0x8, 1, lambda_1FB9)

    def lambda_1FCA():

        label("loc_1FCA")

        TurnDirection(0x10F, 0xD, 0)
        OP_48()
        Jump("loc_1FCA")

    QueueWorkItem2(0x10F, 1, lambda_1FCA)
    OP_8E(0xD, 0xC224, 0x0, 0xC8C8, 0x1B58, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x10F, 0xFF)
    Jump("loc_204F")

    label("loc_1FFC")


    def lambda_2002():

        label("loc_2002")

        TurnDirection(0x101, 0xD, 0)
        OP_48()
        Jump("loc_2002")

    QueueWorkItem2(0x101, 1, lambda_2002)

    def lambda_2013():

        label("loc_2013")

        TurnDirection(0x102, 0xD, 0)
        OP_48()
        Jump("loc_2013")

    QueueWorkItem2(0x102, 1, lambda_2013)

    def lambda_2024():

        label("loc_2024")

        TurnDirection(0x8, 0xD, 0)
        OP_48()
        Jump("loc_2024")

    QueueWorkItem2(0x8, 1, lambda_2024)
    OP_8E(0xD, 0xC224, 0x0, 0xC8C8, 0x1B58, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)

    label("loc_204F")

    SetChrPos(0xD, 0, 0, 0, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A6")

    def lambda_2071():
        OP_92(0x10F, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2071)

    def lambda_2086():
        OP_92(0x110, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_2086)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    Jump("loc_20E1")

    label("loc_20A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_20D3")

    def lambda_20B3():
        OP_92(0x10F, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_20B3)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    Jump("loc_20E1")

    label("loc_20D3")

    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)

    label("loc_20E1")

    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    OP_85(0x8)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_6_1D4E end

    def Function_7_20F6(): pass

    label("Function_7_20F6")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    FadeToBright(1000, 0)
    OP_6D(46700, 5000, 49700, 0)
    SetChrPos(0xE, 52100, 5000, 48000, 90)
    SetChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x8)
    SetChrPos(0x101, 51700, 5000, 50300, 180)
    SetChrPos(0x102, 52100, 5000, 50800, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218C")
    SetChrPos(0x2, 51500, 5000, 51300, 180)
    SetChrPos(0x3, 52100, 5000, 51700, 180)
    Jump("loc_21AB")

    label("loc_218C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21AB")
    SetChrPos(0x2, 51500, 5000, 51300, 180)

    label("loc_21AB")

    OP_6D(51500, 5000, 49200, 3000)
    TurnDirection(0xE, 0x101, 0)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(    #93
        0x101,
        "#002FBe a good kitty and surrender.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8E(0x101, 0xC9F4, 0x1388, 0xC418, 0x7D0, 0x0)
    OP_8F(0xE, 0xCB84, 0x1388, 0xBA54, 0xBB8, 0x0)
    Sleep(1000)

    def lambda_2252():
        OP_8E(0x101, 0xC9F4, 0x1388, 0xC2EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2252)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)

    def lambda_2284():
        OP_8F(0xE, 0xCB84, 0x1388, 0xB928, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2284)
    Sleep(800)

    ChrTalk(    #94
        0x101,
        "#002FStay right there like that and...\x02",
    )

    CloseMessageWindow()

    def lambda_22D0():
        OP_8E(0x101, 0xC9F4, 0x1388, 0xC15C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22D0)
    OP_63(0xE)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)

    def lambda_2305():
        OP_8F(0xE, 0xCB84, 0x1388, 0xB5A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2305)
    OP_63(0xE)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xE, 45, 0)
    Sleep(50)
    OP_8C(0xE, 90, 0)
    Sleep(50)
    OP_8C(0xE, 135, 0)
    Sleep(50)
    OP_8C(0xE, 180, 0)
    Sleep(50)
    OP_8C(0xE, 225, 0)
    Sleep(50)
    OP_8C(0xE, 270, 0)
    Sleep(50)
    OP_8C(0xE, 315, 0)
    Sleep(50)
    OP_8C(0xE, 0, 0)
    OP_8C(0xE, 315, 0)
    Sleep(50)
    OP_8C(0xE, 270, 0)
    Sleep(50)
    OP_8C(0xE, 225, 0)
    Sleep(50)
    OP_8C(0xE, 180, 0)
    Sleep(50)
    OP_8C(0xE, 135, 0)
    Sleep(50)
    OP_8C(0xE, 90, 0)
    Sleep(50)
    OP_8C(0xE, 45, 0)
    Sleep(50)
    OP_8C(0xE, 0, 0)
    OP_8C(0xE, 45, 0)
    Sleep(50)
    OP_8C(0xE, 90, 0)
    Sleep(50)
    OP_8C(0xE, 135, 0)
    Sleep(50)
    OP_8C(0xE, 180, 0)
    Sleep(200)
    OP_43(0xE, 0x1, 0x1, 0x8)
    OP_A2(0x6)
    Sleep(1000)

    ChrTalk(    #95
        0x102,
        (
            "#014FEstelle, don't corner her like that.\x02\x03",

            "What do you intend to tell her\x01",
            "owner if she takes a dive off\x01",
            "the terrace?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #96
        0x101,
        (
            "#009FI-I know that, but it's not like there's\x01",
            "any other way to catch her.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24FA():

        label("loc_24FA")

        TurnDirection(0x101, 0x102, 0)
        OP_48()
        Jump("loc_24FA")

    QueueWorkItem2(0x101, 1, lambda_24FA)
    OP_8E(0x102, 0xCB84, 0x1388, 0xBD10, 0x3E8, 0x0)
    OP_44(0x101, 0xFF)
    Sleep(400)
    Fade(500)
    SetChrChipByIndex(0x102, 13)
    OP_0D()

    ChrTalk(    #97
        0x102,
        (
            "#011F#5PCome here, Aryll.\x01",
            "That's right, this way.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x6)
    Sleep(800)
    TurnDirection(0xE, 0x102, 600)
    Sleep(200)
    OP_62(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(600)

    ChrTalk(    #98
        0x102,
        (
            "#011F#5PI'm sorry the big bad Estelle\x01",
            "scared you like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #99
        0x101,
        "#009F(Jerk.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        (
            "#019F#5PCome on, let's go back and\x01",
            "see your owner.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0xE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)

    def lambda_265D():
        OP_8E(0xE, 0xCB20, 0x1388, 0xB98C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_265D)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #101
        0xE,
        "Nyayayaa～～.\x02",
    )

    CloseMessageWindow()
    Sleep(600)

    ChrTalk(    #102
        0x102,
        (
            "#019F#5PThat's a good girl, Aryll.\x02\x03",

            "All right, let's go.\x01",
            "Your owner's waiting for you.\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x400000)
    FadeToDark(500, 0, -1)
    NewScene("ED6_DT01/T0100   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_7_20F6 end

    def Function_8_2704(): pass

    label("Function_8_2704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2729")
    OP_63(0xE)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)
    OP_48()
    Jump("Function_8_2704")

    label("loc_2729")

    Return()

    # Function_8_2704 end

    def Function_9_272A(): pass

    label("Function_9_272A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A8")

    ChrTalk(    #103
        0x101,
        (
            "#006FLet's catch that kitty before we\x01",
            "do anything else.\x02\x03",

            "Especially since we've got her\x01",
            "trapped inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2826")

    label("loc_27A8")

    TurnDirection(0x102, 0x1, 400)

    ChrTalk(    #104
        0x102,
        (
            "#010FI think we'd better catch the\x01",
            "kitten since we're here.\x02\x03",

            "If we forget about her, something's\x01",
            "bound to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2826")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_272A end

    SaveToFile()

Try(main)
