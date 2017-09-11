from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1132_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1132.x',
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
        "Function_1_136",          # 01, 1
        "Function_2_489",          # 02, 2
        "Function_3_6AB",          # 03, 3
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_78")
    Call(1, 2)
    Jump("loc_135")

    label("loc_78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_89")
    Call(1, 1)
    Jump("loc_135")

    label("loc_89")

    SetChrFlags(0xA, 0x10)
    TalkBegin(0xA)

    ChrTalk(    #0
        0xFE,
        (
            "Man, this is not a good time to be\x01",
            "canceling airliner flights...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Why does it seem like this kind of\x01",
            "stuff always happens whenever I'm\x01",
            "in a hurry?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    ClearChrFlags(0xA, 0x10)

    label("loc_135")

    Return()

    # Function_0_66 end

    def Function_1_136(): pass

    label("Function_1_136")

    EventBegin(0x0)
    Fade(1000)

    def lambda_143():
        OP_6D(-86090, 0, 119620, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_143)
    SetChrPos(0x101, -85900, 0, 119750, 270)
    SetChrPos(0x102, -84500, 0, 119350, 270)
    SetChrPos(0x103, -84900, 0, 120550, 270)
    SetChrFlags(0xA, 0x10)
    OP_4A(0xA, 255)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    Sleep(400)
    OP_28(0x10, 0x4, 0x4)
    OP_28(0x10, 0x1, 0x1)

    ChrTalk(    #2
        0x101,
        (
            "#000F#4PPardon us.\x02\x03",

            "But are you Mr. Hardt?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #3
        0xA,
        "Huh...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)

    ChrTalk(    #4
        0xA,
        (
            "Did you by chance see my request\x01",
            "on the bulletin board?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#000F#4PYep, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        (
            "Oh, you finally came, huh? I've been\x01",
            "waiting around here forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "I need to get to Ruan ASAP, so I'm\x01",
            "looking for an escort to take me to\x01",
            "the Krone Pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "What do you say? Do you think\x01",
            "you can handle that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_478")
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

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_39F"),
        (1, "loc_3B3"),
        (SWITCH_DEFAULT, "loc_475"),
    )


    label("loc_39F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Call(1, 3)
    Jump("loc_475")

    label("loc_3B3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0x10, 0x1, 0x8000)

    ChrTalk(    #9
        0x101,
        (
            "#000F#4PI'm sorry, but we're a little busy\x01",
            "at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "Seriously? You've got to be kidding\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "Man, it looks like my next business\x01",
            "deal is sunk.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_475")

    label("loc_475")

    Jump("loc_33A")

    label("loc_478")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0xA, 255)
    EventEnd(0x0)
    Return()

    # Function_1_136 end

    def Function_2_489(): pass

    label("Function_2_489")

    EventBegin(0x0)
    Fade(1000)

    def lambda_496():
        OP_6D(-86090, 0, 119620, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_496)
    SetChrPos(0x101, -85900, 0, 119750, 270)
    SetChrPos(0x102, -84500, 0, 119350, 270)
    SetChrPos(0x103, -84900, 0, 120550, 270)
    SetChrFlags(0xA, 0x10)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    OP_4A(0xA, 255)
    OP_8C(0xA, 90, 400)
    Sleep(400)

    ChrTalk(    #12
        0xA,
        "Hi there, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "So what do you say? Can I get you to\x01",
            "escort me to the Krone Checkpoint?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_695")
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

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_5C0"),
        (1, "loc_5D4"),
        (SWITCH_DEFAULT, "loc_692"),
    )


    label("loc_5C0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Call(1, 3)
    Jump("loc_692")

    label("loc_5D4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0x10, 0x1, 0x8000)

    ChrTalk(    #14
        0x101,
        (
            "#505F#4PUm, I'm sorry, but we're still a\x01",
            "little busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        (
            "Seriously? You've got to be kidding\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "Man, it looks like my next business\x01",
            "deal is sunk.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_692")

    label("loc_692")

    Jump("loc_55B")

    label("loc_695")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0xA, 255)
    ClearChrFlags(0xA, 0x10)
    EventEnd(0x0)
    Return()

    # Function_2_489 end

    def Function_3_6AB(): pass

    label("Function_3_6AB")

    OP_28(0x10, 0x1, 0x2)

    ChrTalk(    #17
        0x101,
        "#006F#4PYeah, sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "Boy am I glad to hear that!\x01",
            "You guys are like saviors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "I hear the mountain trail has a lot\x01",
            "of monsters, so I'm too scared to\x01",
            "walk it alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#000F#4PBut what are you going to do after\x01",
            "you reach the checkpoint?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "I've got the guild taking care of\x01",
            "that, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "I've got a bracer from the Ruan\x01",
            "branch coming to meet me there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#000F#4PAh, I see.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 400)

    ChrTalk(    #24
        0x102,
        (
            "#010F#4PSo what should we do now?\x02\x03",

            "Is everyone ready to go?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #25
        0x103,
        (
            "#020F#4PNo, I think we should meet up\x01",
            "somewhere else later.\x02\x03",

            "We need to prepare for the trip.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 45, 400)

    ChrTalk(    #26
        0xA,
        "That's fine by me.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)

    ChrTalk(    #27
        0xA,
        (
            "I'll be waiting at the west gate so\x01",
            "once you're ready to go, please\x01",
            "come find me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    def lambda_973():

        label("loc_973")

        TurnDirection(0x101, 0xA, 0)
        OP_48()
        Jump("loc_973")

    QueueWorkItem2(0x101, 1, lambda_973)

    def lambda_984():

        label("loc_984")

        TurnDirection(0x102, 0xA, 0)
        OP_48()
        Jump("loc_984")

    QueueWorkItem2(0x102, 1, lambda_984)

    def lambda_995():

        label("loc_995")

        TurnDirection(0x103, 0xA, 0)
        OP_48()
        Jump("loc_995")

    QueueWorkItem2(0x103, 1, lambda_995)

    def lambda_9A6():
        OP_90(0x101, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A6)

    def lambda_9C1():
        OP_90(0x102, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9C1)
    SetChrFlags(0xA, 0x40)
    OP_8E(0xA, 0xFFFEBBC8, 0x0, 0x1D0D8, 0x7D0, 0x0)
    OP_8E(0xA, 0xFFFEC26C, 0x0, 0x1D2CC, 0x7D0, 0x0)

    def lambda_A09():
        OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A09)
    OP_8E(0xA, 0xFFFECA3C, 0x0, 0x1D2CC, 0x7D0, 0x0)
    SetChrFlags(0xA, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x103, 0x1)
    Sleep(800)

    def lambda_A45():
        OP_90(0x101, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A45)

    def lambda_A60():
        OP_90(0x102, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A60)
    WaitChrThread(0x102, 0x2)

    def lambda_A80():
        OP_8C(0x101, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A80)
    TurnDirection(0x102, 0x101, 400)
    Sleep(800)

    ChrTalk(    #28
        0x102,
        (
            "#010F#4PLet's see...the west gate, huh?\x01",
            "So you mean by the mayor's\x01",
            "residence.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #29
        0x103,
        (
            "#020FOkay, then. Let's get to work,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#000FRoger that!\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_3_6AB end

    SaveToFile()

Try(main)
