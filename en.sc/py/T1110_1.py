from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1110_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1110_1 ._SN',
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
        "Function_1_99D",          # 01, 1
        "Function_2_C28",          # 02, 2
        "Function_3_10CC",         # 03, 3
        "Function_4_1222",         # 04, 4
        "Function_5_12FA",         # 05, 5
        "Function_6_13A3",         # 06, 6
        "Function_7_1498",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x11, 17570, 0, 30850, 90)
    SetChrPos(0x101, 19190, 0, 30760, 270)
    SetChrPos(0xF7, 20060, 0, 30110, 270)
    SetChrPos(0xF8, 20850, 0, 31090, 270)
    SetChrPos(0xF9, 19940, 0, 31760, 270)
    OP_6D(19700, 0, 31270, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1000F#4PUm, excuse me!\x02\x03",

            "You're Ms. Mirano, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x11,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        "You all must be bracers?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_226")

    ChrTalk(    #3
        0x104,
        (
            "#030FI am but an assistant, but you are correct.\x02\x03",

            "You desire escort to Ravennue Village,\x01",
            "yes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_375")

    label("loc_226")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_292")

    ChrTalk(    #4
        0x108,
        (
            "#070FThat's right, ma'am.\x02\x03",

            "We understand you want to be escorted\x01",
            "to Ravennue Village?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_375")

    label("loc_292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_301")

    ChrTalk(    #5
        0x103,
        (
            "#020FYes, ma'am, that's correct.\x02\x03",

            "You're looking for an escort to\x01",
            "Ravennue Village, yes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_375")

    label("loc_301")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_375")

    ChrTalk(    #6
        0x106,
        (
            "#050FThat's right, ma'am.\x02\x03",

            "Your posting said you were looking\x01",
            "for an escort to Ravennue Village?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_375")


    ChrTalk(    #7
        0x11,
        "That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "I'd like to head to that lovely little town\x01",
            "and have a look at their orchards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "Though, if I may, you look a little young\x01",
            "for a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "Are you quite sure you can do this?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x101,
        (
            "#1009F#4PExcuse me, ma'am.\x02\x03",

            "I AM a certified senior bracer.\x01",
            "I'm totally capable of doing this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_548")

    ChrTalk(    #12
        0x106,
        (
            "#057FI'll vouch for her abilities.\x02\x03",

            "If that's not good enough, then\x01",
            "you're welcome to find someone\x01",
            "else. Ma'am.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74D")

    label("loc_548")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_609")

    ChrTalk(    #13
        0x103,
        (
            "#026FI can fully vouch for Estelle's abilities\x01",
            "as a bracer, ma'am.\x02\x03",

            "If that's unsatisfactory, I'm afraid\x01",
            "you'll have to wait for another local\x01",
            "bracer to become available.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74D")

    label("loc_609")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A3")

    ChrTalk(    #14
        0x108,
        (
            "#072FI assure you that Estelle is qualified.\x02\x03",

            "If that does not satisfy, you'll have\x01",
            "to wait for another bracer to become\x01",
            "available.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74D")

    label("loc_6A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74D")

    ChrTalk(    #15
        0x104,
        (
            "#032FI can assure you, madam, that Estelle\x01",
            "is extremely capable.\x02\x03",

            "You are, of course, welcome to wait for\x01",
            "another bracer if you are still unsatisfied.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74D")


    ChrTalk(    #16
        0x11,
        (
            "Oh, my! I suppose you really can't\x01",
            "judge by a cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "I always liked putting my own covers\x01",
            "on my books, anyway. I'll trust you,\x01",
            "young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        "How about it? Shall we be off?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_28(0x7C, 0x1, 0x1)
    OP_28(0x7C, 0x4, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_891")

    ChrTalk(    #19
        0x101,
        "#1006F#4PSure. We're ready when you are.\x02",
    )

    CloseMessageWindow()
    Call(1, 2)
    Return()

    label("loc_891")


    ChrTalk(    #20
        0x101,
        (
            "#1008F#4PEr, um. Aaactually, we have other\x01",
            "things we need to do right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        "Other things? Ahead of escorting me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "Hmph! Fine. Finish it quickly so we can\x01",
            "leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1007F#4PS-Sorry, ma'am. We'll be right back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        "Please do.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_28(0x7C, 0x1, 0x8000)
    EventEnd(0x0)
    OP_4B(0x11, 255)
    OP_44(0x11, 0x0)
    OP_43(0x11, 0x0, 0x0, 0x2)
    Return()

    # Function_0_AA end

    def Function_1_99D(): pass

    label("Function_1_99D")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x11, 255)
    SetChrPos(0x11, 17570, 0, 30850, 90)
    SetChrPos(0x101, 19190, 0, 30760, 270)
    SetChrPos(0xF7, 20060, 0, 30110, 270)
    SetChrPos(0xF8, 20850, 0, 31090, 270)
    SetChrPos(0xF9, 19940, 0, 31760, 270)
    OP_6D(19700, 0, 31270, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_A82")

    ChrTalk(    #25
        0x11,
        "My, that was quick!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        "How about it? Shall we be off?\x02",
    )

    CloseMessageWindow()
    Jump("loc_ACB")

    label("loc_A82")


    ChrTalk(    #27
        0x11,
        "There you are. I've been waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        "So, are you ready to go now?\x02",
    )

    CloseMessageWindow()

    label("loc_ACB")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4B")

    ChrTalk(    #29
        0x101,
        "#1006F#4PSure. We're ready when you are.\x02",
    )

    CloseMessageWindow()
    Call(1, 2)
    Return()

    label("loc_B4B")


    ChrTalk(    #30
        0x101,
        "#1015F#4PWe're, uh, still not quite ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        "Ahem! Still?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        (
            "Come to me when you're done\x01",
            "with EVERYTHING.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1007F#4PI'm so sorry! We'll be back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        "I'll be waiting right here. Still.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_4B(0x11, 255)
    OP_44(0x11, 0x0)
    OP_43(0x11, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_1_99D end

    def Function_2_C28(): pass

    label("Function_2_C28")


    ChrTalk(    #35
        0x11,
        "Very good! Let's be off, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1000F#4PSo we're going to Ravennue, right?\x02\x03",

            "In that case, we'll want to head out\x01",
            "the west gate of the city.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0B")

    ChrTalk(    #37
        0x105,
        (
            "#040FYes, that's right, and then up the\x01",
            "mountain road.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC9")

    label("loc_D0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D4C")

    ChrTalk(    #38
        0x108,
        "#070FRight, and then up the mountain road.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DC9")

    label("loc_D4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8D")

    ChrTalk(    #39
        0x103,
        "#020FRight, and then up the mountain road.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DC9")

    label("loc_D8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC9")

    ChrTalk(    #40
        0x106,
        "#051FYeah, and then west 'n north a bit.\x02",
    )

    CloseMessageWindow()

    label("loc_DC9")


    ChrTalk(    #41
        0x11,
        "I'll meet you by the west gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "I imagine you have a few things to\x01",
            "prepare before we go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1018F#4PYeah, a little prep time would be\x01",
            "great. Thanks!\x02\x03",

            "We'll be right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "Very good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        "Don't keep me waiting long, now.\x02",
    )

    CloseMessageWindow()

    def lambda_EBE():

        label("loc_EBE")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_EBE")

    QueueWorkItem2(0x0, 1, lambda_EBE)

    def lambda_ECF():

        label("loc_ECF")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_ECF")

    QueueWorkItem2(0x1, 1, lambda_ECF)

    def lambda_EE0():

        label("loc_EE0")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_EE0")

    QueueWorkItem2(0x2, 1, lambda_EE0)

    def lambda_EF1():

        label("loc_EF1")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_EF1")

    QueueWorkItem2(0x3, 1, lambda_EF1)
    Sleep(400)

    def lambda_F07():
        OP_6D(19700, 0, 39150, 4000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_F07)
    OP_8E(0x11, 0x4BB4, 0x0, 0x7F4E, 0x7D0, 0x0)
    OP_8E(0x11, 0x4BB4, 0x0, 0x942A, 0x7D0, 0x0)
    OP_8E(0x11, 0x4664, 0x0, 0x942A, 0x7D0, 0x0)

    def lambda_F5B():
        OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F5B)
    OP_8E(0x11, 0x40EC, 0x0, 0x942A, 0x7D0, 0x0)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x2)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    SetChrFlags(0x11, 0x80)
    Fade(1000)
    OP_6D(20620, 0, 31160, 0)
    OP_0D()

    def lambda_FB7():
        OP_8C(0x101, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FB7)
    Sleep(100)

    def lambda_FCA():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_FCA)

    def lambda_FD8():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_FD8)
    Sleep(100)
    OP_8C(0xF8, 270, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #46
        0x101,
        "#1006F#6PLet's get going.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1033")

    ChrTalk(    #47
        0x109,
        "#1060FRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_1033")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1059")

    ChrTalk(    #48
        0x105,
        "#040FAll right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_1059")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_107A")

    ChrTalk(    #49
        0x107,
        "#060FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_107A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A0")

    ChrTalk(    #50
        0x104,
        "#030FOf course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_10A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C3")

    ChrTalk(    #51
        0x108,
        "#070FAll right!\x02",
    )

    CloseMessageWindow()

    label("loc_10C3")

    OP_28(0x7C, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_2_C28 end

    def Function_3_10CC(): pass

    label("Function_3_10CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D9")
    Return()

    label("loc_10D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10EB")
    Return()

    label("loc_10EB")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xA)"), scpexpr(EXPR_END)), "loc_1126")
    Call(1, 4)
    Jump("loc_121B")

    label("loc_1126")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x12)"), scpexpr(EXPR_END)), "loc_1135")
    Call(1, 5)
    Jump("loc_121B")

    label("loc_1135")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xE)"), scpexpr(EXPR_END)), "loc_1144")
    Call(1, 6)
    Jump("loc_121B")

    label("loc_1144")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xB)"), scpexpr(EXPR_END)), "loc_1153")
    Call(1, 7)
    Jump("loc_121B")

    label("loc_1153")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_11C5")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_121B")

    label("loc_11C5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_121B")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_3_10CC end

    def Function_4_1222(): pass

    label("Function_4_1222")

    TalkBegin(0xA)

    ChrTalk(    #54
        0xA,
        (
            "You're looking for a girl who was\x01",
            "lost during the war?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "That's tragic. I wish I could help,\x01",
            "but I'm afraid I don't know anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        (
            "Keep asking around, though. I bet\x01",
            "you'll find someone who knows.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_4_1222 end

    def Function_5_12FA(): pass

    label("Function_5_12FA")

    TalkBegin(0x12)

    ChrTalk(    #57
        0x12,
        (
            "You're looking for a girl who was\x01",
            "orphaned during the war?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        "*sigh* That's so sad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x12,
        (
            "STILL makes my chest hurt thinking\x01",
            "about those times, even now.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_5_12FA end

    def Function_6_13A3(): pass

    label("Function_6_13A3")

    TalkBegin(0xE)

    ChrTalk(    #60
        0xE,
        (
            "During the Hundred Days War, so\x01",
            "many little ones like that girl became\x01",
            "orphans...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xE,
        (
            "No matter who says what, that will\x01",
            "always be a tragedy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xE,
        (
            "Anyone should be able to realize that,\x01",
            "looking at that photograph. And yet...\x01",
            "*sigh*\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_6_13A3 end

    def Function_7_1498(): pass

    label("Function_7_1498")

    TalkBegin(0xB)

    ChrTalk(    #63
        0xB,
        "So that child was lost during the war?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "I don't know what to say. How horrifying...\x01",
            "I mean, I have a daughter of my own.\x01",
            "I can't even imagine how painful it would be.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_7_1498 end

    SaveToFile()

Try(main)
