from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3117_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3117.x',
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_1167",         # 03, 3
        "Function_4_12FC",         # 04, 4
        "Function_5_2409",         # 05, 5
        "Function_6_2D21",         # 06, 6
        "Function_7_3BE8",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-2740, 0, 8680, 0)
    SetChrPos(0x101, -2790, 0, 7830, 0)
    SetChrPos(0x102, -1340, 0, 8370, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105")
    SetChrPos(0x107, -2190, 0, 6710, 315)

    label("loc_105")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0x106, -1500, 0, 6000, 315)

    label("loc_124")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_143")
    SetChrPos(0x110, -2210, 0, 4820, 315)

    label("loc_143")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_162")
    SetChrPos(0x13C, -1500, 0, 6000, 315)

    label("loc_162")

    SetChrFlags(0x9, 0x10)
    TalkBegin(0x9)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2CC")
    ClearChrFlags(0x9, 0x10)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x9, 0x101, 400)
    OP_4A(0x9, 255)

    ChrTalk(    #0
        0x9,
        "Hmm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "If you're looking for Ray,\x01",
            "he's out to lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#000FNo, no...\x02\x03",

            "We checked out the bulletin\x01",
            "board, and...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #3
        0x9,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "Well, thank you.\x01",
            "I'm glad you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "My name's Terry. I'm a\x01",
            "researcher here at the\x01",
            "central factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_473")

    label("loc_2CC")

    ClearChrFlags(0x9, 0x10)

    ChrTalk(    #6
        0x9,
        (
            "I finally managed to make a\x01",
            "prototype. I've just been\x01",
            "waiting for testers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "All I can do in the meantime\x01",
            "is some fine tuning of the\x01",
            "insole...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#000FUm, excuse me...\x02\x03",

            "We came because we saw your\x01",
            "posting on the bulletin board...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x9, 255)
    Sleep(800)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #9
        0x9,
        (
            "Ah, you're finally here.\x01",
            "I was getting a little\x01",
            "tired of waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "My name's Terry. I'm a\x01",
            "researcher here at the\x01",
            "Central Factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_473")


    ChrTalk(    #11
        0x101,
        "#006FI'm Estelle, bracer-in-training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#010FI'm Joshua.\x01",
            "It's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        "Likewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "Getting straight to business...\x01",
            "I have a task for you. Do your\x01",
            "schedules allow for it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0")

    label("loc_539")

    ClearChrFlags(0x9, 0x10)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x9, 0x101, 400)
    OP_4A(0x9, 255)

    ChrTalk(    #15
        0x9,
        "Ah, hello again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "Well? Have your schedules\x01",
            "opened up?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A0")

    FadeToDark(300, 0, 100)
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

    MenuEnd(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D7")

    ChrTalk(    #17
        0x101,
        (
            "#007FMmmm, sorry.\x02\x03",

            "Now's just not a good time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "*sigh* All of the bracers\x01",
            "are busy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "Well, please let me know\x01",
            "when you have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#000FWill do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#010FI'm sure we'll talk again.\x02",
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x1, 0x400)

    def lambda_6C3():
        OP_8C(0x9, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6C3)
    OP_4B(0x9, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_6D7")


    ChrTalk(    #22
        0x101,
        (
            "#000FSure. I don't see a problem\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#010FThe request said you needed \x01",
            "help with testing a new style\x01",
            "of sneaker?\x02\x03",

            "Could you give us a\x01",
            "little more detail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        "Oh, certainly.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #25
        0x9,
        "But first, here.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)
    Sleep(300)
    SetChrFlags(0xB, 0x80)
    TurnDirection(0x9, 0x101, 400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #26
        "\x07\x00Received \x07\x02(Alpha) Strega\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #27
        0x101,
        "#000FIs this your new kind of sneaker?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "Yes. The Strega Corporation is\x01",
            "conducting research on new\x01",
            "projects to bring to market.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Terry")

    ChrTalk(    #29
        0x9,
        (
            "This particular test requires\x01",
            "you to wear these prototypes\x01",
            "around to various places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "Upon the successful completion of\x01",
            "this test, all that will remain\x01",
            "is to put them into production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#501FHmmm... I see...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x101,
        (
            "#004F...HEEEEEYY.\x01",
            "Just a second there, buddy!\x02\x03",

            "Did you just say...the\x01",
            "Strega Corporation?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #33
        0x9,
        "Uh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        "Y-Yes...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#004FSo then, this new line of sneakers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "Yes, it's the Strega Corporation's\x01",
            "newest product...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "Didn't I just say all this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#004F...!!!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_62(0x101, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #39
        0x101,
        (
            "#001FOh, great Aidios...\x02\x03",

            "Thank you for bestowing upon\x01",
            "me...er, US, this magnificent\x01",
            "job...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_8C(0x102, 225, 400)
    Sleep(800)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #40
        0x9,
        (
            "Uhh...\x01",
            "Are you all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        "Why the sudden prayer...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #42
        0x102,
        (
            "#018F...Don't mind her.\x02\x03",

            "#017FEstelle's something of a\x01",
            "sneaker collector.\x02\x03",

            "More to the point, she pretty\x01",
            "much adores the Strega-brand\x01",
            "ones.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9A")

    ChrTalk(    #43
        0x107,
        "#064FOhhh, I get it now.\x02",
    )

    CloseMessageWindow()

    label("loc_C9A")

    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #44
        0x9,
        (
            "Oh...so you might say she\x01",
            "has sneaker-mania, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "I was just a little taken\x01",
            "aback by her reaction...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)

    ChrTalk(    #46
        0x102,
        (
            "#018F...Estelle, would you snap\x01",
            "out of it?\x02\x03",

            "I get that you're excited,\x01",
            "but we do have work to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #47
        0x101,
        (
            "#008FUh... Ahem!\x01",
            "Yes, you are correct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "Hmm... Well, you certainly have\x01",
            "spirit. A scary amount, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "So will you do the test?\x01",
            "Please don't pray at me\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#005FYES! ABSOLUTELY!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #51
        0x102,
        "#018F...See what I mean?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #52
        0x9,
        (
            "I-It's all right.\x01",
            "Please, proceed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#010FSo we'll take on the job...\x02\x03",

            "#010F...but you want us to wear these\x01",
            "shoes everywhere we go?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #54
        0x9,
        "Yes, that's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "From the Elmo spa to the Wolf Fort,\x01",
            "all the way to the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "And when you feel you've\x01",
            "tested them out properly,\x01",
            "bring them back to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "The layer between the sole and\x01",
            "insole is my responsibility, so\x01",
            "I have to see how it holds up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#006FSo you need us to report back\x01",
            "when we have the chance.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #59
        0x9,
        "That, at least.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "Now, see if you can wear\x01",
            "them out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#006FHeh heh...\x01",
            "Just leave it to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        "#010FIf you'll excuse us...\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11C, 1)
    OP_28(0x2A, 0x4, 0x8)
    OP_28(0x2A, 0x4, 0x4)
    OP_28(0x2A, 0x1, 0x1)
    OP_28(0x2A, 0x1, 0x2)
    OP_28(0x2A, 0x1, 0x4)
    OP_A2(0x2)

    def lambda_1153():
        OP_8C(0x9, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1153)
    OP_4B(0x9, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_2_AC end

    def Function_3_1167(): pass

    label("Function_3_1167")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-2740, 0, 8680, 0)
    SetChrPos(0x101, -2790, 0, 7830, 0)
    SetChrPos(0x102, -1340, 0, 8370, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C0")
    SetChrPos(0x107, -2190, 0, 6710, 315)

    label("loc_11C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DF")
    SetChrPos(0x106, -1500, 0, 6000, 315)

    label("loc_11DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11FE")
    SetChrPos(0x110, -2210, 0, 4820, 315)

    label("loc_11FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121D")
    SetChrPos(0x13C, -1500, 0, 6000, 315)

    label("loc_121D")

    SetChrFlags(0x9, 0x10)
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x101, 0)
    OP_4A(0x9, 255)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_1259")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1259")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_1272")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1272")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_128B")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_128B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_12A4")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_12BD")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_12CB")
    Call(1, 4)
    Jump("loc_12E2")

    label("loc_12CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12DE")
    Call(1, 5)
    Jump("loc_12E2")

    label("loc_12DE")

    Call(1, 6)

    label("loc_12E2")


    def lambda_12E8():
        OP_8C(0x9, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12E8)
    OP_4B(0x9, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_3_1167 end

    def Function_4_12FC(): pass

    label("Function_4_12FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x11C)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C0")
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #63
        0x9,
        "Eh? Don't you have the shoes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "Oh, no...\x01",
            "Now the test is no good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "I'm afraid I have to list\x01",
            "your work as a failure.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #66
        0x101,
        (
            "#007F*gulp*\x01",
            "I-I'm sorry.\x02\x03",

            "It was our job, and I didn't\x01",
            "put everything into it like\x01",
            "I should have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "Well, I should be able to do\x01",
            "something with the minimal\x01",
            "data I have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "I hope you'll enjoy the finished\x01",
            "product once it's released.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x4, 0x40)
    OP_A2(0x4)
    Return()

    label("loc_14C0")


    ChrTalk(    #69
        0x101,
        (
            "#000FHi there, Terry.\x02\x03",

            "We've done plenty of walking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        "Ah, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "If you'll just let me examine\x01",
            "the shoes for a moment...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(    #72
        0x9,
        "...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D2F")
    OP_2B(0x2A, 0x2)
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #73
        0x9,
        (
            "...Impressive. The soles are\x01",
            "extremely worn down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "It looks like I selected poor\x01",
            "materials in its making.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #75
        0x9,
        (
            "Yes, I'd call the test a\x01",
            "huge success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#501FWhew...\x01",
            "That's a relief.\x02\x03",

            "I was afraid you were going\x01",
            "to say that you needed us to\x01",
            "do more walking.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_16EF")

    ChrTalk(    #77
        0x107,
        (
            "#061FHee hee...\x01",
            "Thank goodness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1714")

    label("loc_16EF")


    ChrTalk(    #78
        0x107,
        (
            "#061FHee hee...\x01",
            "Thank goodness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1714")


    ChrTalk(    #79
        0x9,
        "So there were no problems?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "No sudden slips or the\x01",
            "material going rigid...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#006FNope. It all went fine.\x02\x03",

            "They fit great and were as\x01",
            "comfortable as a worn-out,\x01",
            "old pair of shoes.\x02\x03",

            "True Stregas, through and through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "Ah, yes. You're a big fan\x01",
            "of the Strega brand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "Perhaps I should give you\x01",
            "a gift, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        (
            "Since you exceeded my expectations\x01",
            "in the test, I'll give you an \x01",
            "equivalent bonus.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #85
        "\x07\x00Received \x07\x02(Beta) Strega\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #86
        0x101,
        (
            "#004FA-Are these what I think\x01",
            "they are...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        (
            "They're a reference copy of\x01",
            "a new product line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "It hasn't been announced yet,\x01",
            "but they should be available\x01",
            "in stores soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#014FAre you sure it's okay\x01",
            "for us to have these?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #90
        0x9,
        (
            "Yes, we've already passed this\x01",
            "phase of development, so I\x01",
            "don't need them anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "I'd rather they be on the feet\x01",
            "of someone who can appreciate\x01",
            "their true value.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #92
        0x101,
        (
            "#001FWow! Thank you!!\x02\x03",

            "We got to help with development AND\x01",
            "got a brand new pair of pre-production\x01",
            "sneakers in the process.\x02\x03",

            "Best. Job. Ever.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #93
        0x9,
        (
            "Ha ha...\x01",
            "My sentiments exactly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "Thanks to your efforts in\x01",
            "testing, my research results\x01",
            "are sure to be certified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#006FGood luck with your work.\x01",
            "I can't wait to see the\x01",
            "next new product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        (
            "Yes, I'll be reporting these\x01",
            "results to my boss, right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#010FThanks for everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#001FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11D, 1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #99
        "\x07\x00Quest \x07\x02[Product Testing] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_1D2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2173")
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #100
        0x9,
        (
            "...Yes, it looks like the sole\x01",
            "has been worn down enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "It looks like I selected poor\x01",
            "materials in its making.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #102
        0x9,
        "Okay, the test was a success.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#501FWhew...\x01",
            "That's a relief.\x02\x03",

            "I was afraid you were going\x01",
            "to say that you needed us to\x01",
            "do more walking.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1EAB")

    ChrTalk(    #104
        0x107,
        (
            "#061FHee hee...\x01",
            "Thank goodness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED0")

    label("loc_1EAB")


    ChrTalk(    #105
        0x107,
        (
            "#061FHee hee...\x01",
            "Thank goodness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED0")


    ChrTalk(    #106
        0x9,
        "So there were no problems?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "No sudden slips or the\x01",
            "material going rigid...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#006FNope. It all went fine.\x02\x03",

            "They fit great and were as\x01",
            "comfortable as a worn-out,\x01",
            "old pair of shoes.\x02\x03",

            "True Stregas, through and through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "Well, these are just the\x01",
            "prototypes. The final product\x01",
            "will be a great improvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x9,
        (
            "Thank you for your help. You've\x01",
            "done me a great favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#006FGood luck with your work.\x01",
            "I can't wait to see the\x01",
            "next new product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "Ha ha... I'll be sure to let\x01",
            "my employers know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        "#010FThanks for everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#001FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #115
        "\x07\x00Quest \x07\x02[Product Testing] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_2173")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_2408")
    OP_63(0x9)
    Sleep(400)

    ChrTalk(    #116
        0x9,
        "...Hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "I'm sorry to say, but you\x01",
            "haven't walked around enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "The sole isn't worn down\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#003FHuh...so it isn't.\x02\x03",

            "I thought for sure we'd\x01",
            "walked around enough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "*sigh* And I don't have enough\x01",
            "time to conduct further tests.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #121
        0x9,
        (
            "I'm sorry, but I'll have to list\x01",
            "this as a 'failure to complete.'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #122
        0x101,
        (
            "#007F*gulp*\x01",
            "I-I'm sorry.\x02\x03",

            "It was our job, and I didn't\x01",
            "put everything into it like\x01",
            "I should have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        (
            "I should be able to do something\x01",
            "with the minimal data I have.\x01",
            "It'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "Well, I hope you'll enjoy\x01",
            "the final product when\x01",
            "it's released.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x4, 0x40)
    OP_28(0x2A, 0x1, 0x20)
    OP_A2(0x4)
    Return()

    label("loc_2408")

    Return()

    # Function_4_12FC end

    def Function_5_2409(): pass

    label("Function_5_2409")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x11C)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2491")
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #125
        0x9,
        (
            "Eh?\x01",
            "Don't you have the shoes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x9,
        (
            "The test is no good without\x01",
            "those alpha-model Stregas.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    label("loc_2491")


    ChrTalk(    #127
        0x101,
        (
            "#000FWe're here to report in, Terry.\x02\x03",

            "We're kinda in a hurry, so we'll\x01",
            "have to make this fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        "Ah, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        (
            "Let me take a look at\x01",
            "the shoes, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(    #130
        0x9,
        "...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_29AA")
    OP_2B(0x2A, 0x2)
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #131
        0x9,
        (
            "...Impressive. The soles are\x01",
            "extremely worn down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x9,
        (
            "It looks like I selected poor\x01",
            "materials in its making.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #133
        0x9,
        (
            "Yes, I'd call the test a\x01",
            "huge success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#501FWhew...\x01",
            "Thank goodness.\x02\x03",

            "So does that mean the\x01",
            "job's done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x9,
        (
            "Yes, and I appreciate it. You've\x01",
            "done me a great favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x9,
        (
            "Oh, hold on a moment.\x01",
            "Weren't you a big fan\x01",
            "of the Strega brand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x9,
        (
            "I'd like for you to have\x01",
            "these, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #138
        "\x07\x00Received \x07\x02(Beta) Strega\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #139
        0x101,
        (
            "#000FA-Are these what I think\x01",
            "they are...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x9,
        (
            "They're a reference copy\x01",
            "of a new product line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x9,
        (
            "We've already passed this\x01",
            "phase of development, so I\x01",
            "don't need them anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #142
        0x101,
        (
            "#001FWow! Thank you!!\x02\x03",

            "I'll be looking forward to\x01",
            "the next line of products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x9,
        (
            "I'll be sure to pass that\x01",
            "on to my employers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x9,
        "Take care in your journeys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        "#010FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#001FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11D, 1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #147
        "\x07\x00Quest \x07\x02[Product Testing] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_29AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2B")
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #148
        0x9,
        (
            "...Yes, it looks like the sole\x01",
            "has been worn down enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x9,
        (
            "It looks like I selected poor\x01",
            "materials in its making.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #150
        0x9,
        "Okay, the test was a success.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        (
            "#501FWhew...\x01",
            "Thank goodness.\x02\x03",

            "So does that mean the\x01",
            "job's done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x9,
        (
            "Yes, and I appreciate it. You've\x01",
            "done me a great favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#006FI'll be looking forward to\x01",
            "the next line of products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "I'll be sure to pass that\x01",
            "on to my employers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x9,
        "Take care in your journeys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        "#010FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#001FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #158
        "\x07\x00Quest \x07\x02[Product Testing] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_2C2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_2D20")
    OP_63(0x9)
    Sleep(400)

    ChrTalk(    #159
        0x9,
        (
            "I'm sorry to say, but you haven't\x01",
            "walked around enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        "The sole isn't worn down at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#505FHmmm...\x01",
            "Yeah, you're right.\x02\x03",

            "#000FWell, we'll take them back out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #162
        0x9,
        (
            "Yes...\x01",
            "Sorry for the trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x1, 0x8)
    Return()

    label("loc_2D20")

    Return()

    # Function_5_2409 end

    def Function_6_2D21(): pass

    label("Function_6_2D21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x11C)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA9")
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #163
        0x9,
        (
            "Eh?\x01",
            "Don't you have the shoes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x9,
        (
            "The test is no good without\x01",
            "those alpha-model Stregas.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    label("loc_2DA9")


    ChrTalk(    #165
        0x101,
        (
            "#000FHi there, Terry.\x02\x03",

            "We've done plenty of walking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x9,
        "Ah, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        (
            "If you'll just let me examine\x01",
            "the shoes for a moment...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(    #168
        0x9,
        "...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3619")
    OP_2B(0x2A, 0x2)
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #169
        0x9,
        (
            "...Impressive. The soles are\x01",
            "extremely worn down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        (
            "It looks like I selected poor\x01",
            "materials in its making.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #171
        0x9,
        (
            "Yes, I'd call the test a\x01",
            "huge success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#501FWhew...\x01",
            "That's a relief.\x02\x03",

            "I was afraid you were going\x01",
            "to say that you needed us to\x01",
            "do more walking.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2FD8")

    ChrTalk(    #173
        0x107,
        (
            "#061FHee hee...\x01",
            "Thank goodness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FFD")

    label("loc_2FD8")


    ChrTalk(    #174
        0x107,
        (
            "#061FHee hee...\x01",
            "Thank goodness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FFD")


    ChrTalk(    #175
        0x9,
        "So there were no problems?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "No sudden slips or the\x01",
            "material going rigid...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#006FNope. It all went fine.\x02\x03",

            "They fit great, and were as\x01",
            "comfortable as a worn-out,\x01",
            "old pair of shoes.\x02\x03",

            "True Stregas, through and through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        (
            "Ah, yes. You're a big fan\x01",
            "of the Strega brand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        (
            "Perhaps I should give you\x01",
            "a gift, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        (
            "Since you exceeded my expectations\x01",
            "in the test, I'll give you an \x01",
            "equivalent bonus.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #181
        "\x07\x00Received \x07\x02(Beta) Strega\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #182
        0x101,
        (
            "#004FA-Are these what I think\x01",
            "they are...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x9,
        (
            "They're a reference copy of\x01",
            "a new product line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x9,
        (
            "It hasn't been announced yet,\x01",
            "but they should be available\x01",
            "in stores soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        (
            "#014FAre you sure it's okay\x01",
            "for us to have these?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #186
        0x9,
        (
            "Yes, we've already passed this\x01",
            "phase of development, so I\x01",
            "don't need them anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x9,
        (
            "I'd rather they be on the feet\x01",
            "of someone who can appreciate\x01",
            "their true value.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #188
        0x101,
        (
            "#001FWow! Thank you!!\x02\x03",

            "We got to help with development AND\x01",
            "got a brand new pair of pre-production\x01",
            "sneakers in the process.\x02\x03",

            "Best. Job. Ever.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #189
        0x9,
        (
            "Ha ha...\x01",
            "My sentiments exactly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        (
            "Thanks to your efforts in\x01",
            "testing, my research results\x01",
            "are sure to be certified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#006FGood luck with your work.\x01",
            "I can't wait to see the\x01",
            "next new product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x9,
        (
            "Yes, I'll be reporting these\x01",
            "results to my boss, right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x102,
        "#010FThanks for everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        "#001FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11D, 1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #195
        "\x07\x00Quest \x07\x02[Product Testing] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_3619")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5E")
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #196
        0x9,
        (
            "...Yes, it looks like the sole\x01",
            "has been worn down enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x9,
        (
            "It looks like I selected poor\x01",
            "materials in its making.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #198
        0x9,
        "Okay, the test was a success.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        (
            "#501FWhew...\x01",
            "That's a relief.\x02\x03",

            "I was afraid you were going\x01",
            "to say that you needed us to\x01",
            "do more walking.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3795")

    ChrTalk(    #200
        0x107,
        (
            "#061FHee hee...\x01",
            "Thank goodness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BA")

    label("loc_3795")


    ChrTalk(    #201
        0x107,
        (
            "#061FHee hee...\x01",
            "Thank goodness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37BA")


    ChrTalk(    #202
        0x9,
        "So there were no problems?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x9,
        (
            "No sudden slips or the\x01",
            "material going rigid...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#006FNope. It all went fine.\x02\x03",

            "They fit great, and were as\x01",
            "comfortable as a worn-out,\x01",
            "old pair of shoes.\x02\x03",

            "True Stregas, through and through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x9,
        (
            "Well, these are just the\x01",
            "prototypes. The final product\x01",
            "will be a great improvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x9,
        (
            "Thank you for your help. You've\x01",
            "done me a great favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#006FGood luck with your work.\x01",
            "I can't wait to see the\x01",
            "next new product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x9,
        (
            "Ha ha... I'll be sure to let\x01",
            "my employers know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        "#010FThanks for everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#001FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #211
        "\x07\x00Quest \x07\x02[Product Testing] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_3A5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3BE7")
    OP_63(0x9)
    Sleep(400)

    ChrTalk(    #212
        0x9,
        "...Hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x9,
        (
            "I'm sorry to say, but you\x01",
            "haven't walked around enough.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #214
        0x9,
        (
            "The sole isn't worn down\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        (
            "#505FHmmm...\x01",
            "Yeah, you're right.\x02\x03",

            "I thought for sure we'd\x01",
            "walked around enough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x102,
        (
            "#010FOh, well. We'll just have\x01",
            "to take them back out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x9,
        (
            "Yes, please.\x01",
            "I'm sorry to trouble you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        (
            "#006FSure thing.\x02\x03",

            "We'll be back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x9,
        "Thank you...\x02",
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x1, 0x8)
    Return()

    label("loc_3BE7")

    Return()

    # Function_6_2D21 end

    def Function_7_3BE8(): pass

    label("Function_7_3BE8")

    SetChrFlags(0xC, 0x80)
    OP_64(0x2, 0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #220
        "\x07\x00Found \x07\x02Tomorrow's Cooking\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x341, 1)
    OP_28(0x2D, 0x1, 0x8)
    TalkEnd(0xFF)
    Return()

    # Function_7_3BE8 end

    SaveToFile()

Try(main)
