from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1121_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1121_1 ._SN',
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
        "Function_1_165",          # 01, 1
        "Function_2_10E7",         # 02, 2
        "Function_3_121F",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BB")
    OP_2A(0xB5, 0xB6, 0xFFFF)
    Jump("loc_161")

    label("loc_BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_DA")
    OP_2A(0xB1, 0xB2, 0xB3, 0x78, 0x7A, 0x7B, 0xB4, 0x79, 0x7C, 0xFFFF)
    Jump("loc_161")

    label("loc_DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_F5")
    OP_2A(0xB1, 0xB2, 0xB3, 0x78, 0x7A, 0x7B, 0xB4, 0xFFFF)
    Jump("loc_161")

    label("loc_F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_10E")
    OP_2A(0xB1, 0xB2, 0xB3, 0x78, 0x7A, 0x7B, 0xFFFF)
    Jump("loc_161")

    label("loc_10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_127")
    OP_2A(0xB1, 0xB2, 0xB3, 0x78, 0x7A, 0x7B, 0xFFFF)
    Jump("loc_161")

    label("loc_127")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        "\x07\x05No jobs are available.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_161")

    TalkEnd(0xFF)
    Return()

    # Function_0_AA end

    def Function_1_165(): pass

    label("Function_1_165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FC")

    ChrTalk(    #1
        0x101,
        (
            "#1002FWait a minute!\x01",
            "Do you think this might be it?\x02\x03",

            "The place mentioned on the card.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_259")

    ChrTalk(    #2
        0x103,
        (
            "#022FIt is possible, but...\x02\x03",

            "We can continue that case later.\x01",
            "We need to get to Ravennue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #3
        0x101,
        "#1002FAh, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8")

    label("loc_259")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DB")

    ChrTalk(    #4
        0x108,
        (
            "#072FIt is possible, but now's not the time.\x02\x03",

            "We must get to Ravennue immediately.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #5
        0x101,
        "#1002FRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8")

    label("loc_2DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E")

    ChrTalk(    #6
        0x104,
        (
            "#030FIt's quite possible.\x02\x03",

            "Now, however, is not the time to ponder.\x01",
            "We must go to Ravennue at once.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #7
        0x101,
        "#1002FRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8")

    label("loc_36E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F8")

    ChrTalk(    #8
        0x105,
        (
            "#042FYes, it might be.\x02\x03",

            "But that case can wait, can't it?\x01",
            "We must get to Ravennue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #9
        0x101,
        "#1002FRight, of course.\x02",
    )

    CloseMessageWindow()

    label("loc_3F8")

    TalkEnd(0xFF)
    Return()

    label("loc_3FC")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 27040, 0, 22430, 270)
    SetChrPos(0xF7, 28320, 0, 22190, 270)
    SetChrPos(0xF8, 29010, 0, 21500, 270)
    SetChrPos(0xF9, 27620, 0, 24010, 220)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_464")
    SetChrPos(0x4, 29870, 0, 22190, 270)

    label("loc_464")

    OP_6D(28000, 0, 23000, 0)
    OP_67(0, 4340, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05When Estelle investigated the book, she found a\x01",
            "card stuck to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #11
        0x101,
        (
            "#1002FOkay, found it.\x02\x03",

            "#1015FLet's see...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 17)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05'Should you seek the third key,\x01",
            "seek ye the reverently-held casket.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #13
        0x101,
        "#1007FYup. We got it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_682")

    ChrTalk(    #14
        0x105,
        (
            "#047F'FTHKC2E'--advance each letter by one,\x01",
            "and it becomes 'GUILD3F.'\x02\x03",

            "#040FThe third floor of the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_875")

    label("loc_682")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_732")

    ChrTalk(    #15
        0x107,
        (
            "#060FIf you take each letter in 'FTHKC2E'\x01",
            "and make it the next letter in the\x01",
            "alphabet, it's 'GUILD3F'!\x02\x03",

            "It has to mean the third floor of the\x01",
            "guildhouse!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_875")

    label("loc_732")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CF")

    ChrTalk(    #16
        0x104,
        (
            "#035FOf course. Advance each letter and\x01",
            "number in 'FTHKC2E' by one, and it\x01",
            "becomes 'GUILD3F.'\x02\x03",

            "#030FThe third floor of the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_875")

    label("loc_7CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_875")

    ChrTalk(    #17
        0x103,
        (
            "#020FTake 'FTHKC2E' and advance each letter\x01",
            "or number by one, and you get 'GUILD3F.'\x02\x03",

            "Pretty obvious that means the third floor\x01",
            "of the guildhouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_875")


    ChrTalk(    #18
        0x101,
        (
            "#1015FThat's the riddle solved, I guess.\x02\x03",

            "#1007FBut what the hell?! Seriously!\x01",
            "Right in the middle of the guildhouse?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97A")

    ChrTalk(    #19
        0x106,
        (
            "#057FThat clown's tryin' to mock us.\x02\x03",

            "We'll have to show him what mockery\x01",
            "gets you the next time we see him.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_B6A")

    label("loc_97A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A32")

    ChrTalk(    #20
        0x108,
        (
            "#075FIt does seem like he's mocking us\x01",
            "openly at this point.\x02\x03",

            "#072FWhen we meet him next, we'll have\x01",
            "to show him exaaactly how we feel\x01",
            "about being mocked.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_B6A")

    label("loc_A32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AE2")

    ChrTalk(    #21
        0x103,
        (
            "#025F*sigh* He rather is having his way with\x01",
            "us at this point, isn't he?\x02\x03",

            "I'm all for showing him what we think of\x01",
            "that the next time we meet him.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_B6A")

    label("loc_AE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6A")

    ChrTalk(    #22
        0x104,
        (
            "#031FMy rival is certainly having his fun with\x01",
            "us now.\x02\x03",

            "We should 'thank' him profusely when\x01",
            "we see him next.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_B6A")


    ChrTalk(    #23
        0x101,
        "#1002FYeah, no kidding.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE9")

    ChrTalk(    #24
        0x104,
        (
            "#030FThe next hint is a 'reverently-held casket.'\x02\x03",

            "Another metaphor.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    Jump("loc_D5F")

    label("loc_BE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5B")

    ChrTalk(    #25
        0x103,
        (
            "#022FSo the next hint is a 'reverently-held casket.'\x02\x03",

            "That must be another metaphor.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_D5F")

    label("loc_C5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD8")

    ChrTalk(    #26
        0x107,
        (
            "#062FThe next thing is a 'reverently-held casket,'\x01",
            "right?\x02\x03",

            "I don't think he means it literally.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Jump("loc_D5F")

    label("loc_CD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5F")

    ChrTalk(    #27
        0x105,
        (
            "#042FRegardless, our next objective seems\x01",
            "to be this 'reverently-held casket.'\x02\x03",

            "Presumably another metaphor.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_D5F")


    ChrTalk(    #28
        0x101,
        (
            "#1002FPretty safe to assume so, yeah.\x02\x03",

            "There aren't exactly a ton of caskets\x01",
            "just lying around Bose. \x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E42")

    ChrTalk(    #29
        0x108,
        (
            "#073FI was thinking the same thing.\x02\x03",

            "#070FWe should consider what the 'casket'\x01",
            "could actually be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1005")

    label("loc_E42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EFB")

    ChrTalk(    #30
        0x106,
        (
            "#051FMy thoughts exactly. Startin' to get\x01",
            "into the clown's head, eh?\x02\x03",

            "Speakin' of heads, let's put ours\x01",
            "together and figure out what this\x01",
            "casket's supposed to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1005")

    label("loc_EFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F82")

    ChrTalk(    #31
        0x103,
        (
            "#020FMy thoughts exactly, Estelle.\x02\x03",

            "Let's brainstorm and figure out what\x01",
            "he could be referring to as a 'casket.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1005")

    label("loc_F82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1005")

    ChrTalk(    #32
        0x104,
        (
            "#030FHeh, sharp as always, Estelle.\x02\x03",

            "Let's ponder on caskets for a while\x01",
            "and attempt to see through the riddle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1005")

    OP_A2(0x1)
    OP_A3(0x0)
    OP_28(0x78, 0x1, 0x10)
    OP_28(0x78, 0x1, 0x20)
    OP_64(0x3, 0x1)

    def lambda_1021():
        OP_8E(0x0, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1021)

    def lambda_103C():
        OP_8E(0x1, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_103C)

    def lambda_1057():
        OP_8E(0x2, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_1057)

    def lambda_1072():
        OP_8E(0x3, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_1072)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AE")

    def lambda_1099():
        OP_8E(0x4, 0x6C34, 0x0, 0x56B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x4, 0, lambda_1099)

    label("loc_10AE")

    OP_6D(27700, 0, 22200, 1000)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E4")
    WaitChrThread(0x4, 0x0)

    label("loc_10E4")

    EventEnd(0x0)
    Return()

    # Function_1_165 end

    def Function_2_10E7(): pass

    label("Function_2_10E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F4")
    Return()

    label("loc_10F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1106")
    Return()

    label("loc_1106")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_1141")
    Call(1, 3)
    Jump("loc_1218")

    label("loc_1141")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_1150")
    Call(1, 3)
    Jump("loc_1218")

    label("loc_1150")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_11C2")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1218")

    label("loc_11C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1218")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_2_10E7 end

    def Function_3_121F(): pass

    label("Function_3_121F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130D")

    ChrTalk(    #35
        0x8,
        (
            "#632FI see, you've decided to take up that\x01",
            "missing persons case.\x02\x03",

            "That one's going to be a challenge,\x01",
            "I suspect, but do your best to solve it.\x02\x03",

            "That poor woman who submitted the\x01",
            "request seems at the end of her rope.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_13B2")

    label("loc_130D")


    ChrTalk(    #36
        0x8,
        (
            "#632FThat poor woman who submitted the\x01",
            "request has no one left to turn to but us.\x02\x03",

            "That one's going to be a challenge,\x01",
            "I suspect, but do your best to solve it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B2")

    TalkEnd(0x8)
    Return()

    # Function_3_121F end

    SaveToFile()

Try(main)
