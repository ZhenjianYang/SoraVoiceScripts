from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P7012   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7012.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60174",
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
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT26/CH20373 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT26/CH20373P._CP',             # 00
    )

    ScpFunction(
        "Function_0_B2",           # 00, 0
        "Function_1_DC",           # 01, 1
        "Function_2_DD",           # 02, 2
        "Function_3_8AB",          # 03, 3
        "Function_4_2265",         # 04, 4
    )


    def Function_0_B2(): pass

    label("Function_0_B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_C8")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 3)
    Jump("loc_DB")

    label("loc_C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_DB")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_DB")

    Return()

    # Function_0_B2 end

    def Function_1_DC(): pass

    label("Function_1_DC")

    Return()

    # Function_1_DC end

    def Function_2_DD(): pass

    label("Function_2_DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 480, -140, -4930, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E")
    SetChrPos(0xEF, -470, 280, -5370, 90)
    SetChrPos(0xF0, -1820, 900, -5500, 90)
    SetChrPos(0xF1, -1960, 840, -4500, 90)
    Jump("loc_1C3")

    label("loc_13E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182")
    SetChrPos(0xF0, -470, 280, -5370, 90)
    SetChrPos(0xEF, -1820, 900, -5500, 90)
    SetChrPos(0xF1, -1960, 840, -4500, 90)
    Jump("loc_1C3")

    label("loc_182")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C3")
    SetChrPos(0xF1, -470, 280, -5370, 90)
    SetChrPos(0xEF, -1820, 900, -5500, 90)
    SetChrPos(0xF0, -1960, 840, -4500, 90)

    label("loc_1C3")

    OP_43(0xEE, 0x0, 0x0, 0x4)
    OP_43(0xEF, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x4)
    OP_43(0xF1, 0x0, 0x0, 0x4)
    OP_6D(-300, 830, -4800, 0)
    OP_67(0, 7940, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(327000, 0)
    OP_6E(448, 0)
    StopSound(0x2710, 0xF618, 0x1F40)

    def lambda_22F():
        OP_6B(1970, 8000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_22F)

    def lambda_23F():
        OP_67(0, 3180, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_23F)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x3)
    WaitChrThread(0x10F, 0x3)

    ChrTalk(    #0
        0x109,
        (
            "#1067F#100P#6PI'm sure you remember...\x02\x03",

            "The day it all happened, Rufina and I were due to\x01",
            "come back here for the first time in a while.\x02\x03",

            "We were both coming from different places we'd\x01",
            "been sent, so we wanted to meet up in town and\x01",
            "come the rest of the way here together.\x02\x03",

            "#1065FBut then her train was delayed, leaving me in town\x01",
            "to wait for her alone.\x02\x03",

            "That was when I got word of what happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x24016B, 0x0, 0x0, 0x12C)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Kevin")

    AnonymousTalk(    #1
        (
            "\x07\x0C#40WAll I could think was that you and the other kids were in danger...and so I\x01",
            "decided to try and take out the jaegers here alone.\x02\x03",

            "They weren't all that experienced, so fighting them wasn't even hard for a\x01",
            "squire like me.\x02\x03",

            "Before long, I was able to disable them all and free the matron and the\x01",
            "other kids.\x02\x03",

            "Or so I thought. You were nowhere to be seen.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x12C)
    Sleep(2000)

    ChrTalk(    #2
        0x109,
        (
            "#1065F#100P#6PI asked the other kids where you were. They told\x01",
            "me one of the jaegers had taken you somewhere\x01",
            "else and that you were unconscious.\x02\x03",

            "I looked frantically all over trying to find you before\x01",
            "eventually stumbling across this place.\x02\x03",

            "#1840FAs for how...\x02\x03",

            "You remember how you didn't have your ribbon\x01",
            "in your hair when you woke up, Ries? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        (
            "#1802F#100P#5PI-I do...\x02\x03",

            "What does that have to do with anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1075F#100P#6PI found that ribbon in front of the secret passage\x01",
            "we've just gone through.\x02\x03",

            "And there were new footprints near it, too. Made it\x01",
            "easy to find the entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1444F#100P#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1067F#100P#6PAnyway...\x02\x03",

            "...after getting in here, I made my way down this\x01",
            "staircase in pursuit of the jaeger that had taken\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1500)
    OP_A2(0x2505)
    NewScene("ED6_DT21/P7012   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_DD end

    def Function_3_8AB(): pass

    label("Function_3_8AB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    StopSound(0x80E8, 0xF618, 0x0)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_72(0x803, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_71(0x404, 0x0)
    ExitThread()
    SetChrPos(0x109, 79760, 0, -8450, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93E")
    SetChrPos(0xEF, 79840, 0, -10580, 0)
    SetChrPos(0xF0, 80570, 0, -12380, 0)
    SetChrPos(0xF1, 79500, 0, -12590, 0)
    Jump("loc_9C3")

    label("loc_93E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982")
    SetChrPos(0xF0, 79840, 0, -10580, 0)
    SetChrPos(0xEF, 80570, 0, -12380, 0)
    SetChrPos(0xF1, 79500, 0, -12590, 0)
    Jump("loc_9C3")

    label("loc_982")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C3")
    SetChrPos(0xF1, 79840, 0, -10580, 0)
    SetChrPos(0xEF, 80570, 0, -12380, 0)
    SetChrPos(0xF0, 79500, 0, -12590, 0)

    label("loc_9C3")

    OP_6D(78260, 1050, -16040, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(325, 0)

    def lambda_A06():
        OP_8F(0xFE, 0x13920, 0x0, 0x4B1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A06)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8C")

    def lambda_A34():
        OP_8F(0xFE, 0x1397A, 0x0, 0x43A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_A34)
    Sleep(50)

    def lambda_A54():
        OP_8F(0xFE, 0x13CFE, 0x0, 0x3C82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_A54)
    Sleep(50)

    def lambda_A74():
        OP_8F(0xFE, 0x13740, 0x0, 0x3CB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_A74)
    Jump("loc_B61")

    label("loc_A8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF8")

    def lambda_AA0():
        OP_8F(0xFE, 0x1397A, 0x0, 0x43A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_AA0)
    Sleep(50)

    def lambda_AC0():
        OP_8F(0xFE, 0x13CFE, 0x0, 0x3D4A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_AC0)
    Sleep(50)

    def lambda_AE0():
        OP_8F(0xFE, 0x13740, 0x0, 0x3D7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_AE0)
    Jump("loc_B61")

    label("loc_AF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B61")

    def lambda_B0C():
        OP_8F(0xFE, 0x1397A, 0x0, 0x43A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_B0C)
    Sleep(50)

    def lambda_B2C():
        OP_8F(0xFE, 0x13CFE, 0x0, 0x3D4A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_B2C)
    Sleep(50)

    def lambda_B4C():
        OP_8F(0xFE, 0x13740, 0x0, 0x3D7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_B4C)

    label("loc_B61")

    Sleep(1500)

    def lambda_B6C():
        OP_6D(78260, 1050, 20160, 11000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_B6C)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Fade(500)
    OP_6D(78430, 0, 19800, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(297, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #7
        0x109,
        (
            "#1065F#11PHey, Ries?\x02\x03",

            "#1063FDo you remember what I was like back\x01",
            "when you first met me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        (
            "#1445F#6P...Yeah.\x02\x03",

            "#1446FI was still young at the time, but it's as\x01",
            "fresh as if it were only yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_AD(0x24016A, 0x0, 0x0, 0x12C)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Ries")

    AnonymousTalk(    #9
        (
            "\x07\x0C#40WYou looked like you'd been swallowed by blackness. Like there wasn't a single\x01",
            "thread of hope bound to you.\x02\x03",

            "It was...scary.\x02\x03",

            "I kept wondering what must have happened to you--what you must have seen\x01",
            "to make you end up that way.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x12C)
    Sleep(1500)

    ChrTalk(    #10
        0x109,
        "#1840F#11PHaha... What must have happened to me, huh?\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    Sleep(500)

    ChrTalk(    #11
        0x109,
        (
            "#1067F#11PRufina seemed like she knew...\x02\x03",

            "#1840FBefore I met you, I killed my mom.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC0")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F27")

    label("loc_EC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE8")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F27")

    label("loc_EE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F10")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F27")

    label("loc_F10")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F27")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F54")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FBB")

    label("loc_F54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FBB")

    label("loc_F7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA4")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FBB")

    label("loc_FA4")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_FBB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_104F")

    label("loc_FE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1010")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_104F")

    label("loc_1010")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1038")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_104F")

    label("loc_1038")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_104F")

    Sleep(1000)

    ChrTalk(    #12
        0x10F,
        "#1444F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108B")

    ChrTalk(    #13
        0x104,
        "#1543F#6P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_108B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AE")

    ChrTalk(    #14
        0x102,
        "#1504F#6P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_10AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D0")

    ChrTalk(    #15
        0x10B,
        "#216F#6P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_10D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F7")

    ChrTalk(    #16
        0x106,
        "#055F#6PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_10F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_111E")

    ChrTalk(    #17
        0x10E,
        "#178F#6PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_111E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1146")

    ChrTalk(    #18
        0x103,
        "#1523F#6PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_1146")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116E")

    ChrTalk(    #19
        0x101,
        "#1004F#6PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_116E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1196")

    ChrTalk(    #20
        0x105,
        "#1163F#6PWha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_1196")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B8")

    ChrTalk(    #21
        0x110,
        "#264F#6P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_11B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DB")

    ChrTalk(    #22
        0x10A,
        "#1317F#6P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_11DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11FF")

    ChrTalk(    #23
        0x10D,
        "#270F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_11FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1223")

    ChrTalk(    #24
        0x108,
        "#072F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_1223")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1249")

    ChrTalk(    #25
        0x107,
        "#065F#6P...Wha...?\x02",
    )

    CloseMessageWindow()

    label("loc_1249")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_126D")

    ChrTalk(    #26
        0x10C,
        "#113F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_126D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1291")

    ChrTalk(    #27
        0x107,
        "#065F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_1291")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B5")

    ChrTalk(    #28
        0x108,
        "#072F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_12B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D9")

    ChrTalk(    #29
        0x10D,
        "#270F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_12D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12FE")

    ChrTalk(    #30
        0x10A,
        "#1317F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_12FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1322")

    ChrTalk(    #31
        0x110,
        "#264F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_1322")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1347")

    ChrTalk(    #32
        0x105,
        "#1163F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_1347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136C")

    ChrTalk(    #33
        0x101,
        "#1004F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_136C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1391")

    ChrTalk(    #34
        0x103,
        "#1523F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_1391")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B5")

    ChrTalk(    #35
        0x10E,
        "#178F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_13B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D9")

    ChrTalk(    #36
        0x106,
        "#055F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_13D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13FD")

    ChrTalk(    #37
        0x10B,
        "#216F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_13FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_141F")

    ChrTalk(    #38
        0x102,
        "#1504F#6P...?!\x02",
    )

    CloseMessageWindow()

    label("loc_141F")


    ChrTalk(    #39
        0x109,
        (
            "#1840F#11PMaybe 'killed' isn't the right expression.\x01",
            "It's not like I directly did it.\x02\x03",

            "#1075FI still let her die, though. I've still got a \x01",
            "responsibility for what happened.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_AD(0x24015D, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Kevin")

    AnonymousTalk(    #40
        (
            "\x07\x0C#40WGrowing up, it was basically me and my mom for the most part.\x02\x03",

            "My father showed his face from time to time, but not that much. From what\x01",
            "I understand, he had another family elsewhere.\x02\x03",

            "But even without him, she did her best to look after me on her own. I loved\x01",
            "her dearly.\x02\x03",

            "Kids in the neighborhood used to make fun of me for how I talked,\x01",
            "which I got from her...but I just beat them up most of the time.\x02\x03",

            "She was always kind, she loved cooking, and...yeah. I thought the world of\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_6D(123020, 0, 12050, 0)
    OP_67(0, 4960, -10000, 0)
    OP_6B(2510, 0)
    OP_6C(315000, 0)
    OP_6E(325, 0)
    OP_AE(0xC8)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Kevin")

    AnonymousTalk(    #41
        (
            "\x07\x0C#40WWhen I was seven, my father, who had all the money in the world, chose to\x01",
            "abandon her.\x02\x03",

            "At the best of times, she was always a frail person...and after that, she grew\x01",
            "more and more despondent. Her health suffered...\x02\x03",

            "I tried everything a kid could do to cheer her up, but nothing I did worked.\x02\x03",

            "And during one winter's day when she must have finally had enough.\x02\x03",

            "She came over while I was sleeping and tried to strangle me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Ries")

    AnonymousTalk(    #42
        "\x07\x0C#3S...!!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS461._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(2500)
    OP_C6(0x0, 0x3, -5592406, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 200, -1, -1)
    SetChrName("")

    AnonymousTalk(    #43 op#A
        "\x07\x00#50W#20AI'm so sorry, Kevin...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #44 op#A
        "\x07\x00#50W#25AI failed as your mother...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #45 op#A
        (
            "\x07\x00#50W#50A...but I'm so tired...\x01",
            "I'm so, so tired...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #46 op#A
        "\x07\x00#50W#55A...At least this way...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #47 op#A
        (
            "\x07\x00#50W#60A...At least this way,\x01",
            "the two of us can...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(150)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    Sleep(2000)
    OP_C7(0x1, 0xFF, 0x0)
    FadeToBright(0, 0)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Kevin")

    AnonymousTalk(    #48
        (
            "\x07\x0C#40WI guess she figured that if we were both going to suffer, we might as well\x01",
            "take the easy way out as a family.\x02\x03",

            "But I wouldn't let her take me with her.\x02\x03",

            "Before I knew what I was doing, I'd pushed her aside and ran barefoot out\x01",
            "into the snow.\x02\x03",

            "I wandered around for a while after that. I couldn't understand what had\x01",
            "happened or what she'd been trying to do...\x02\x03",

            "Eventually, I could feel myself getting hungry. I thought that maybe she'd\x01",
            "been able to clear her head.\x02\x03",

            "I made my way back home, nervous as could be, and...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AD(0x24015F, 0x0, 0x0, 0x64)
    Sleep(3000)
    Sleep(500)
    FadeToDark(0, 16777215, -1)
    OP_0D()
    OP_AE(0x64)
    Sleep(3000)
    OP_6D(78090, -200, 19770, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(315000, 0)
    OP_6E(297, 0)
    Sleep(1000)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #49
        0x10F,
        "#1960F#6P#60W...I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x109,
        (
            "#1844F#11P#40WHaha. Sorry for making you listen to all this.\x02\x03",

            "#1843FStill, I think that's probably when it happened.\x02\x03",

            "#1845FWhen my Stigma was carved inside me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x10F,
        "#1809F#6P...What?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1E49():
        OP_6D(78520, 0, 21620, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1E49)

    def lambda_1E61():
        OP_67(0, 4840, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1E61)

    def lambda_1E79():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1E79)

    def lambda_1E89():
        OP_6E(330, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1E89)
    OP_8C(0x109, 0, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    Sleep(600)
    LoadEffect(0x0, "map\\mp058_00.eff")
    LoadEffect(0x1, "scraft\\sc008_02.eff")
    LoadEffect(0x2, "map\\mpP90_00.eff")
    LoadEffect(0x3, "map\\mpP90_01.eff")
    LoadEffect(0x4, "map\\mpP90_04.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 80170, 1000, 19900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC9)
    OP_82(0x0, 0x2)
    Sleep(2000)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_22(0x146, 0x64, 0x1)
    PlayEffect(0x2, 0x0, 0xFF, 80130, 0, 21750, 0, 0, 0, 1800, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0xFF, 80130, 0, 21750, 0, 0, 0, 1800, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, 80130, 0, 21750, 0, 0, 0, 1800, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_23(0x146)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_0D()
    SetChrSubChip(0x109, 0)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_2065():
        OP_6D(77520, 0, 23520, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2065)

    def lambda_207D():
        OP_8F(0xFE, 0x138BC, 0x0, 0x535C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_207D)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_22(0x70, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x10E)
    OP_73(0x3)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    SetChrFlags(0x3, 0x4)

    def lambda_20CC():
        OP_8F(0xFE, 0x13902, 0x0, 0x6770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_20CC)
    Sleep(500)

    def lambda_20EC():
        OP_6D(77520, 0, 25000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_20EC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216A")

    def lambda_2112():
        OP_8F(0xFE, 0x13902, 0x0, 0x6770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2112)
    Sleep(300)

    def lambda_2132():
        OP_8F(0xFE, 0x13B00, 0x0, 0x6766, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2132)
    Sleep(600)

    def lambda_2152():
        OP_8F(0xFE, 0x13740, 0x0, 0x6748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2152)
    Jump("loc_223F")

    label("loc_216A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D6")

    def lambda_217E():
        OP_8F(0xFE, 0x13902, 0x0, 0x6770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_217E)
    Sleep(300)

    def lambda_219E():
        OP_8F(0xFE, 0x13B00, 0x0, 0x6766, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_219E)
    Sleep(600)

    def lambda_21BE():
        OP_8F(0xFE, 0x13740, 0x0, 0x6748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_21BE)
    Jump("loc_223F")

    label("loc_21D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223F")

    def lambda_21EA():
        OP_8F(0xFE, 0x13902, 0x0, 0x6770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_21EA)
    Sleep(300)

    def lambda_220A():
        OP_8F(0xFE, 0x13B00, 0x0, 0x6766, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_220A)
    Sleep(600)

    def lambda_222A():
        OP_8F(0xFE, 0x13740, 0x0, 0x6748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_222A)

    label("loc_223F")

    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x1)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/P7013   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_8AB end

    def Function_4_2265(): pass

    label("Function_4_2265")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_228A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_23CC")

    label("loc_228A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A3")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_23CC")

    label("loc_22A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22BC")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_23CC")

    label("loc_22BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D5")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_23CC")

    label("loc_22D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22EE")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_23CC")

    label("loc_22EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2307")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_23CC")

    label("loc_2307")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2320")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_23CC")

    label("loc_2320")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2339")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_23CC")

    label("loc_2339")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2352")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_23CC")

    label("loc_2352")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_23CC")

    label("loc_236B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2384")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_23CC")

    label("loc_2384")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_239D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_23CC")

    label("loc_239D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B6")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_23CC")

    label("loc_23B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23CC")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_23CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23E1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_23CC")

    label("loc_23E1")

    Return()

    # Function_4_2265 end

    SaveToFile()

Try(main)
