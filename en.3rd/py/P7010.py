from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P7010   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7010.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60211",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_C7",           # 01, 1
        "Function_2_CE",           # 02, 2
        "Function_3_125A",         # 03, 3
        "Function_4_12BD",         # 04, 4
        "Function_5_131D",         # 05, 5
        "Function_6_137D",         # 06, 6
        "Function_7_13DD",         # 07, 7
        "Function_8_13FC",         # 08, 8
        "Function_9_1447",         # 09, 9
        "Function_10_1492",        # 0A, 10
        "Function_11_14D6",        # 0B, 11
        "Function_12_151A",        # 0C, 12
        "Function_13_1541",        # 0D, 13
        "Function_14_1568",        # 0E, 14
        "Function_15_158F",        # 0F, 15
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_C6")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_C6")

    Return()

    # Function_0_AA end

    def Function_1_C7(): pass

    label("Function_1_C7")

    OP_72(0x1001, 0x0)
    ExitThread()
    Return()

    # Function_1_C7 end

    def Function_2_CE(): pass

    label("Function_2_CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 1010, -300, -2200, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F")
    SetChrPos(0xEF, -240, -300, -2200, 0)
    SetChrPos(0xF0, 1010, -300, -2200, 0)
    SetChrPos(0xF1, -240, -300, -2200, 0)
    Jump("loc_1B4")

    label("loc_12F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173")
    SetChrPos(0xF0, -240, -300, -2200, 0)
    SetChrPos(0xEF, 1010, -300, -2200, 0)
    SetChrPos(0xF1, -240, -300, -2200, 0)
    Jump("loc_1B4")

    label("loc_173")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4")
    SetChrPos(0xF1, -240, -300, -2200, 0)
    SetChrPos(0xEF, 1010, -300, -2200, 0)
    SetChrPos(0xF0, -240, -300, -2200, 0)

    label("loc_1B4")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-790, 4300, 20090, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(338000, 0)
    OP_6E(346, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_22D():
        OP_6D(1360, 4300, 1740, 7500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_22D)

    def lambda_245():
        OP_67(0, 5800, -10000, 7500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_245)

    def lambda_25D():
        OP_6B(2520, 7500)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_25D)

    def lambda_26D():
        OP_6C(326000, 7500)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_26D)

    def lambda_27D():
        OP_6E(346, 7500)
        ExitThread()

    QueueWorkItem(0xF1, 2, lambda_27D)
    Sleep(4500)
    OP_22(0x177, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2")
    OP_43(0xEF, 0x0, 0x0, 0xD)
    Sleep(600)
    OP_43(0x109, 0x0, 0x0, 0xC)
    Sleep(700)
    OP_43(0xF0, 0x0, 0x0, 0xE)
    Sleep(200)
    OP_43(0xF1, 0x0, 0x0, 0xF)
    Jump("loc_347")

    label("loc_2D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E")
    OP_43(0xF0, 0x0, 0x0, 0xD)
    Sleep(600)
    OP_43(0x109, 0x0, 0x0, 0xC)
    Sleep(700)
    OP_43(0xEF, 0x0, 0x0, 0xE)
    Sleep(200)
    OP_43(0xF1, 0x0, 0x0, 0xF)
    Jump("loc_347")

    label("loc_30E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347")
    OP_43(0xF1, 0x0, 0x0, 0xD)
    Sleep(600)
    OP_43(0x109, 0x0, 0x0, 0xC)
    Sleep(700)
    OP_43(0xEF, 0x0, 0x0, 0xE)
    Sleep(200)
    OP_43(0xF0, 0x0, 0x0, 0xF)

    label("loc_347")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x2)
    Fade(500)
    OP_6D(-800, 0, 4500, 0)
    OP_67(0, 6040, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(315000, 0)
    OP_6E(303, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1802F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1065F#6PIt all started five years ago. A jaeger corps\x01",
            "someone had hired took this place over out\x01",
            "of nowhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #2
        0x109,
        (
            "#1840F#12PBy the way, how much do you remember of\x01",
            "that day, Ries?\x02\x03",

            "Just so I know.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #3
        0x10F,
        (
            "#1802F#5PI...\x02\x03",

            "#1445FI just remember a group of men in black forcing\x01",
            "their way through the gate and charging in here.\x02\x03",

            "They tied everyone up, took the matron up to the\x01",
            "second floor...\x02\x03",

            "...and then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1065F#12PNext thing you knew, you were in a bed\x01",
            "in the hospital in town, right?\x02\x03",

            "#1067FAfter which you found out that Rufina and\x01",
            "I had come to rescue everyone...\x02\x03",

            "...and that she had died in the process.\x02\x03",

            "#1840FThat about right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        (
            "#1446F#5P...Mm-hmm.\x02\x03",

            "#1802FJust what happened, Kevin?\x02\x03",

            "All I've heard is that it was the work of\x01",
            "someone who opposed the church...\x02\x03",

            "#1445F...but I haven't had a chance to meet you\x01",
            "since then, much less to ask you about it.\x02\x03",

            "I tried asking Instructor Selnate, but she\x01",
            "wouldn't say a word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1075F#12PThat doesn't surprise me.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #7
        0x109,
        (
            "#1067F#6PThe Gralsritter's commander can't admit this\x01",
            "orphanage was being used as a smokescreen \x01",
            "for an artifact that needed sealing away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        "#1802F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #9
        0x10F,
        "#1444F#5P#4SIt what...?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_88A():
        OP_6D(-700, 0, 11410, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_88A)
    OP_43(0x109, 0x0, 0x0, 0x8)

    def lambda_8A9():

        label("loc_8A9")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_8A9")

    QueueWorkItem2(0xEF, 0, lambda_8A9)

    def lambda_8BA():

        label("loc_8BA")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_8BA")

    QueueWorkItem2(0xF0, 0, lambda_8BA)

    def lambda_8CB():

        label("loc_8CB")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_8CB")

    QueueWorkItem2(0xF1, 0, lambda_8CB)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90B")
    OP_43(0xEF, 0x0, 0x0, 0x9)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x0, 0xA)
    Sleep(700)
    OP_43(0xF1, 0x0, 0x0, 0xB)
    Jump("loc_968")

    label("loc_90B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93B")
    OP_43(0xF0, 0x0, 0x0, 0x9)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(700)
    OP_43(0xF1, 0x0, 0x0, 0xB)
    Jump("loc_968")

    label("loc_93B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_968")
    OP_43(0xF1, 0x0, 0x0, 0x9)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x0, 0xA)
    Sleep(700)
    OP_43(0xF0, 0x0, 0x0, 0xB)

    label("loc_968")

    WaitChrThread(0xEE, 0x1)

    def lambda_973():
        OP_6D(-5400, 0, 14960, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_973)

    def lambda_98B():
        OP_67(0, 5610, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_98B)

    def lambda_9A3():
        OP_6B(2450, 4000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_9A3)

    def lambda_9B3():
        OP_6E(322, 4000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_9B3)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)

    ChrTalk(    #10
        0x109,
        "#1063F#5PHere we go.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x109, 0x0, 0x0, 0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A38")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A9F")

    label("loc_A38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A60")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A9F")

    label("loc_A60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A88")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A9F")

    label("loc_A88")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A9F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACC")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B33")

    label("loc_ACC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF4")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B33")

    label("loc_AF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B33")

    label("loc_B1C")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B33")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B60")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BC7")

    label("loc_B60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B88")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BC7")

    label("loc_B88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB0")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BC7")

    label("loc_BB0")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BC7")

    Sleep(1500)

    ChrTalk(    #11
        0x10F,
        "#1802F#6P...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C11")

    ChrTalk(    #12
        0x10D,
        "#270F#6PA secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_C11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")

    ChrTalk(    #13
        0x10C,
        "#112F#6PA secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C74")

    ChrTalk(    #14
        0x104,
        "#1542F#6PA secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_C74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA5")

    ChrTalk(    #15
        0x10E,
        "#172F#6PA secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD6")

    ChrTalk(    #16
        0x108,
        "#072F#6PA secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D07")

    ChrTalk(    #17
        0x106,
        "#057F#6PA secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_D07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D39")

    ChrTalk(    #18
        0x103,
        "#1522F#6PA secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_D39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6D")

    ChrTalk(    #19
        0x105,
        "#1163F#6PA-A secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_D6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA0")

    ChrTalk(    #20
        0x10A,
        "#812F#6PA-A secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_DA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD3")

    ChrTalk(    #21
        0x107,
        "#065F#6PA-A secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E09")

    ChrTalk(    #22
        0x110,
        "#1305F#6PA secret passage, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_E09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E3C")

    ChrTalk(    #23
        0x10B,
        "#216F#6PA-A secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_E3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6E")

    ChrTalk(    #24
        0x102,
        "#1502F#6PA secret passage?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9F")

    label("loc_E6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9F")

    ChrTalk(    #25
        0x101,
        "#1020F#6PA-A secret passage?!\x02",
    )

    CloseMessageWindow()

    label("loc_E9F")

    WaitChrThread(0x109, 0x0)
    Sleep(300)

    def lambda_EAF():
        OP_6D(-6400, 0, 14960, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_EAF)

    def lambda_EC7():
        OP_8E(0xFE, 0xFFFFE2B4, 0x0, 0x3732, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EC7)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0xEE, 0x1)
    OP_E0(239, 0x40, 0x1)
    OP_E0(240, 0x41, 0x1)
    OP_E0(241, 0x42, 0x1)
    SetChrPos(0x109, -35730, 0, 8770, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F58")
    SetChrPos(0xEF, -35730, 0, 8770, 270)
    SetChrPos(0xF0, -35730, 0, 8770, 270)
    SetChrPos(0xF1, -35730, 0, 8770, 270)
    Jump("loc_FDD")

    label("loc_F58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9C")
    SetChrPos(0xF0, -35730, 0, 8770, 270)
    SetChrPos(0xEF, -35730, 0, 8770, 270)
    SetChrPos(0xF1, -35730, 0, 8770, 270)
    Jump("loc_FDD")

    label("loc_F9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDD")
    SetChrPos(0xF1, -35730, 0, 8770, 270)
    SetChrPos(0xEF, -35730, 0, 8770, 270)
    SetChrPos(0xF0, -35730, 0, 8770, 270)

    label("loc_FDD")

    SetChrChipByIndex(0xEF, 0)
    SetChrChipByIndex(0xF0, 1)
    SetChrChipByIndex(0xF1, 2)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-42080, 1500, 11170, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(315000, 0)
    OP_6E(295, 0)

    def lambda_105B():
        OP_6D(-42080, -1500, 11170, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_105B)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(3000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B3")
    OP_43(0xEF, 0x0, 0x0, 0x4)
    Sleep(700)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Jump("loc_1110")

    label("loc_10B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E3")
    OP_43(0xF0, 0x0, 0x0, 0x4)
    Sleep(700)
    OP_43(0xEF, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Jump("loc_1110")

    label("loc_10E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1110")
    OP_43(0xF1, 0x0, 0x0, 0x4)
    Sleep(700)
    OP_43(0xEF, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF0, 0x0, 0x0, 0x6)

    label("loc_1110")

    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #26
        0x10F,
        (
            "#1449F#11PW-Wait!\x02\x03",

            "If there was an artifact here...you don't \x01",
            "mean...?!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xEE, 0x3)
    Sleep(300)

    ChrTalk(    #27
        0x109,
        "#1840F#5PYup.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #28
        0x109,
        (
            "#1065F#6PBelow here is a primal ground used to seal\x01",
            "artifacts away.\x02\x03",

            "#1063FJust like the one under Grancel Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #29
        0x10F,
        "#1802F#11P#3S...!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/P7012   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_CE end

    def Function_3_125A(): pass

    label("Function_3_125A")


    def lambda_1260():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1260)
    OP_8E(0xFE, 0xFFFF6C26, 0x0, 0x229C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6C08, 0x0, 0x2A80, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5E20, 0xFFFFFC18, 0x2A58, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5CAE, 0xFFFFF830, 0x1B80, 0x7D0, 0x0)
    Return()

    # Function_3_125A end

    def Function_4_12BD(): pass

    label("Function_4_12BD")


    def lambda_12C3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12C3)
    OP_8E(0xFE, 0xFFFF6C26, 0x0, 0x229C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF6C08, 0x0, 0x2A80, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF5E20, 0xFFFFFC18, 0x2A58, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 600)
    Return()

    # Function_4_12BD end

    def Function_5_131D(): pass

    label("Function_5_131D")


    def lambda_1323():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1323)
    OP_8E(0xFE, 0xFFFF6C26, 0x0, 0x229C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF6C08, 0x0, 0x2A80, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF6334, 0xFFFFFDC6, 0x2A6C, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 600)
    Return()

    # Function_5_131D end

    def Function_6_137D(): pass

    label("Function_6_137D")


    def lambda_1383():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1383)
    OP_8E(0xFE, 0xFFFF6C26, 0x0, 0x229C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF6C08, 0x0, 0x2A80, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF69CE, 0x0, 0x29FE, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 600)
    Return()

    # Function_6_137D end

    def Function_7_13DD(): pass

    label("Function_7_13DD")

    OP_22(0x6C, 0x0, 0x64)
    Sleep(200)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x168)
    OP_73(0x1)
    OP_23(0x70)
    Return()

    # Function_7_13DD end

    def Function_8_13FC(): pass

    label("Function_8_13FC")

    OP_8E(0xFE, 0x50, 0x0, 0x1B12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x2AE4, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 0)
    OP_8F(0xFE, 0xFFFFEDA4, 0x0, 0x3674, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_13FC end

    def Function_9_1447(): pass

    label("Function_9_1447")

    OP_8C(0xFE, 0, 0)
    OP_8E(0xFE, 0x50, 0x0, 0x1B12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x2AE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF33A, 0x0, 0x33EA, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_1447 end

    def Function_10_1492(): pass

    label("Function_10_1492")

    OP_8E(0xFE, 0x50, 0x0, 0x1B12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x2AE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF538, 0x0, 0x2E7C, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_10_1492 end

    def Function_11_14D6(): pass

    label("Function_11_14D6")

    OP_8E(0xFE, 0x50, 0x0, 0x1B12, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x2AE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF998, 0x0, 0x3142, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_11_14D6 end

    def Function_12_151A(): pass

    label("Function_12_151A")


    def lambda_1520():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1520)
    OP_8F(0xFE, 0x35C, 0x0, 0xCBC, 0x7D0, 0x0)
    Return()

    # Function_12_151A end

    def Function_13_1541(): pass

    label("Function_13_1541")


    def lambda_1547():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1547)
    OP_8F(0xFE, 0xFFFFFD80, 0x0, 0xC76, 0x7D0, 0x0)
    Return()

    # Function_13_1541 end

    def Function_14_1568(): pass

    label("Function_14_1568")


    def lambda_156E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_156E)
    OP_8F(0xFE, 0x50A, 0x0, 0x564, 0x7D0, 0x0)
    Return()

    # Function_14_1568 end

    def Function_15_158F(): pass

    label("Function_15_158F")


    def lambda_1595():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1595)
    OP_8F(0xFE, 0xFFFFFE20, 0x0, 0x53C, 0x7D0, 0x0)
    Return()

    # Function_15_158F end

    SaveToFile()

Try(main)
