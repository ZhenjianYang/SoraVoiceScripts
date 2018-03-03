from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7402   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        'Gordias Type-0',                       # 9
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_11E",          # 01, 1
        "Function_2_125",          # 02, 2
        "Function_3_26BF",         # 03, 3
        "Function_4_28EE",         # 04, 4
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_E0")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_11D")

    label("loc_E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_FF")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_11D")

    label("loc_FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_11D")

    Return()

    # Function_0_CA end

    def Function_1_11E(): pass

    label("Function_1_11E")

    OP_71(0x406, 0x0)
    ExitThread()
    Return()

    # Function_1_11E end

    def Function_2_125(): pass

    label("Function_2_125")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x40, 0x2)
    OP_E0(238, 0x41, 0x3)
    OP_E0(239, 0x42, 0x2)
    OP_E0(239, 0x43, 0x3)
    OP_E0(240, 0x44, 0x2)
    OP_E0(240, 0x45, 0x3)
    OP_E0(241, 0x46, 0x2)
    OP_E0(241, 0x47, 0x3)
    SetChrPos(0xEE, -840, 0, -10480, 0)
    SetChrPos(0xEF, 550, 0, -10450, 0)
    SetChrPos(0xF0, -1260, 0, -12070, 0)
    SetChrPos(0xF1, 610, 0, -12180, 0)
    OP_6D(5130, -28700, 26260, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(7270, 0)
    OP_6C(45000, 0)
    OP_6E(672, 0)

    def lambda_1E0():
        OP_6D(5130, -100, 26260, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1E0)

    def lambda_1F8():
        OP_67(0, 6470, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1F8)

    def lambda_210():
        OP_8E(0xFE, 0xFFFFFB5A, 0x0, 0x2F9E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_210)
    Sleep(100)

    def lambda_230():
        OP_8E(0xFE, 0x212, 0x0, 0x2FBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_230)
    Sleep(100)

    def lambda_250():
        OP_8E(0xFE, 0xFFFFF948, 0x0, 0x27D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_250)
    Sleep(100)

    def lambda_270():
        OP_8E(0xFE, 0x1EA, 0x0, 0x2850, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_270)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEF, 0x1)

    def lambda_29F():
        OP_6B(7500, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_29F)

    def lambda_2AF():
        OP_6E(700, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2AF)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xF0, 0x1)
    WaitChrThread(0xF1, 0x1)
    Fade(1000)
    OP_6D(1100, 0, 12840, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(263, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")

    ChrTalk(    #0
        0x101,
        "#1002F#5PI'm guessing this is the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_369")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")

    ChrTalk(    #1
        0x102,
        "#1502F#5PI suppose this must be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_3B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE")

    ChrTalk(    #2
        0x10B,
        "#212F#5PI'm guessing this is the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_3FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_450")

    ChrTalk(    #3
        0x110,
        (
            "#1305F#5POh... I suppose this must be the end of this\x01",
            "wing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_450")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49B")

    ChrTalk(    #4
        0x107,
        "#065F#5PI-I guess this must be the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_49B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E4")

    ChrTalk(    #5
        0x10A,
        "#812F#5PI'm guessing this is the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_4E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_530")

    ChrTalk(    #6
        0x105,
        "#1162F#5PI suppose this must be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C")

    ChrTalk(    #7
        0x103,
        "#1522F#5PI suppose this must be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_57C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CA")

    ChrTalk(    #8
        0x106,
        "#057F#5PI guess this has gotta be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_5CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_615")

    ChrTalk(    #9
        0x108,
        "#072F#5PI suppose this must be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_660")

    ChrTalk(    #10
        0x10E,
        "#172F#5PI suppose this must be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_660")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B3")

    ChrTalk(    #11
        0x104,
        (
            "#1542F#5PHmm... I suppose this must be the end of\x01",
            "this wing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_6B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FE")

    ChrTalk(    #12
        0x10D,
        "#270F#5PI suppose this must be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_6FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_746")

    ChrTalk(    #13
        0x10C,
        "#112F#5PI suppose this must be the end of this wing.\x02",
    )

    CloseMessageWindow()

    label("loc_746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77F")

    ChrTalk(    #14
        0x101,
        "#1002F#5PIt sure looks that way...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_77F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BD")

    ChrTalk(    #15
        0x102,
        "#1502F#5PIt certainly seems that way...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_7BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F5")

    ChrTalk(    #16
        0x10B,
        "#210F#5PIt sure looks that way...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_7F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_839")

    ChrTalk(    #17
        0x110,
        "#1306F#5PWell, it certainly looks that way...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_839")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_876")

    ChrTalk(    #18
        0x107,
        "#065F#5PIt looks that way, at least...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_876")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B3")

    ChrTalk(    #19
        0x10A,
        "#812F#5PIt looks that way, at least...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_8B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F1")

    ChrTalk(    #20
        0x105,
        "#1162F#5PIt certainly seems that way...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_8F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F")

    ChrTalk(    #21
        0x103,
        "#1522F#5PIt certainly seems that way...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_92F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_967")

    ChrTalk(    #22
        0x106,
        "#552F#5PHeh. Sure looks that way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_967")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")

    ChrTalk(    #23
        0x108,
        "#072F#5PHmm... It looks that way, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_9A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EB")

    ChrTalk(    #24
        0x10E,
        "#178F#5PHmm... It looks that way, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_9EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E")

    ChrTalk(    #25
        0x104,
        "#1545F#5PHeh. It certainly appears that way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_A2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6C")

    ChrTalk(    #26
        0x10D,
        "#270F#5P...It looks that way, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA8")

    label("loc_A6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA8")

    ChrTalk(    #27
        0x10C,
        "#110F#5PThat does appear to be the case.\x02",
    )

    CloseMessageWindow()

    label("loc_AA8")

    Sleep(500)

    def lambda_AB3():

        label("loc_AB3")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_AB3")

    QueueWorkItem2(0x10, 3, lambda_AB3)
    OP_22(0x113, 0x1, 0x46)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFA")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B61")

    label("loc_AFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B22")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B61")

    label("loc_B22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4A")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B61")

    label("loc_B4A")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B61")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BF5")

    label("loc_B8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB6")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BF5")

    label("loc_BB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDE")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BF5")

    label("loc_BDE")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BF5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C22")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C89")

    label("loc_C22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4A")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C89")

    label("loc_C4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C72")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C89")

    label("loc_C72")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C89")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB6")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D1D")

    label("loc_CB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDE")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D1D")

    label("loc_CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D06")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D1D")

    label("loc_D06")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D1D")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D58")

    ChrTalk(    #28
        0x101,
        "#1020F#6PTh-That sounds like...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_D58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8C")

    ChrTalk(    #29
        0x102,
        "#1506F#6PThat sounds like...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_D8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC0")

    ChrTalk(    #30
        0x10B,
        "#216F#6PWh-What's that sound?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF6")

    ChrTalk(    #31
        0x107,
        "#065F#6PTh-That sounds like...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_DF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3A")

    ChrTalk(    #32
        0x10A,
        "#1317F#6PThis sound feels kind of familiar...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_E3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E70")

    ChrTalk(    #33
        0x105,
        "#1164F#6PTh-That sounds like...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_E70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB4")

    ChrTalk(    #34
        0x103,
        "#1523F#6PThis sound feels kind of familiar...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_EB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEA")

    ChrTalk(    #35
        0x106,
        "#052F#6PTh-That sounds like...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2D")

    ChrTalk(    #36
        0x108,
        "#073F#6PThis sound feels kind of familiar...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_F2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F60")

    ChrTalk(    #37
        0x10E,
        "#173F#6PI-It couldn't be...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_F60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA4")

    ChrTalk(    #38
        0x104,
        "#1542F#6PThis sound is...somewhat familiar...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_FA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD8")

    ChrTalk(    #39
        0x10D,
        "#273F#6PWhat's that sound...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1009")

    label("loc_FD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1009")

    ChrTalk(    #40
        0x10C,
        "#113F#6PWhat's that sound...?\x02",
    )

    CloseMessageWindow()

    label("loc_1009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1070")

    ChrTalk(    #41
        0x110,
        (
            "#1306FHeehee.\x02\x03",

            "#261FThat Lord of Phantasma really does know\x01",
            "how to shake things up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1070")

    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1084():

        label("loc_1084")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1084")

    QueueWorkItem2(0x10, 3, lambda_1084)
    OP_24(0x113, 0x50)
    Sleep(500)

    def lambda_10A8():

        label("loc_10A8")

        OP_7C(0x28, 0x28, 0xBB8, 0x64)
        OP_48()
        Jump("loc_10A8")

    QueueWorkItem2(0x10, 3, lambda_10A8)
    OP_24(0x113, 0x5A)
    Sleep(500)

    def lambda_10CC():

        label("loc_10CC")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_10CC")

    QueueWorkItem2(0x10, 3, lambda_10CC)
    OP_24(0x113, 0x64)
    SetChrPos(0x10, 0, 10000, 24000, 180)
    OP_A1(0x10, 0x6)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_B0(0x6, 0x1E)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x28)
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 260)
    OP_70(0x6, 0xF1)

    def lambda_112B():
        OP_8F(0xFE, 0x0, 0x0, 0x5DC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_112B)
    Fade(500)
    OP_6D(260, 3400, 23940, 0)
    OP_67(0, 14940, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(315000, 0)
    OP_6E(328, 0)

    def lambda_1188():
        OP_6B(1800, 1000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1188)
    SetChrPos(0xEE, -570, 0, 12740, 0)
    SetChrPos(0xEF, 640, 0, 12760, 0)
    SetChrPos(0xF0, -1100, 0, 10550, 0)
    SetChrPos(0xF1, 1250, 0, 10750, 0)
    Sleep(500)
    OP_44(0xF0, 0x1)
    OP_6D(60, 2750, 19490, 0)
    OP_67(0, -1270, -10000, 0)
    OP_6B(700, 0)
    OP_6C(0, 0)
    OP_6E(590, 0)

    def lambda_1222():
        OP_6B(1000, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1222)
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 221)
    OP_70(0x6, 0xF0)
    OP_44(0x10, 0x3)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0x1388, 0x5DC)
    WaitChrThread(0x10, 0x1)
    OP_73(0x6)
    OP_71(0x2006, 0x0)
    ExitThread()
    OP_D8(0x6, 0x3E8)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x28)
    Sleep(500)
    OP_44(0xF0, 0x1)
    OP_22(0xF0, 0x0, 0x64)
    OP_6D(-2990, 400, 20280, 0)
    OP_67(0, 5590, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(225000, 0)
    OP_6E(517, 0)

    def lambda_12D3():
        OP_6B(2000, 1000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_12D3)
    Sleep(500)
    Sleep(500)
    OP_44(0xF0, 0x1)
    OP_22(0xF0, 0x0, 0x64)
    OP_6D(3010, 3500, 26680, 0)
    OP_67(0, -1400, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(44000, 0)
    OP_6E(547, 0)

    def lambda_1333():
        OP_6B(2000, 1000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1333)
    Sleep(500)
    Sleep(500)
    OP_44(0xF0, 0x1)
    OP_22(0xF0, 0x0, 0x64)
    OP_6D(10, 3500, 23940, 0)
    OP_67(0, 1800, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(306, 0)

    def lambda_1393():
        OP_6B(2930, 1000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1393)
    Sleep(500)
    Sleep(1000)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)

    def lambda_13B7():
        OP_6D(0, 2500, 24310, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_13B7)

    def lambda_13CF():
        OP_67(0, 900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_13CF)

    def lambda_13E7():
        OP_6B(5710, 4000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_13E7)

    def lambda_13F7():
        OP_6E(234, 4000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_13F7)
    Sleep(3000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1588")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1437")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_148F")

    label("loc_1437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145A")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_148F")

    label("loc_145A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147D")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_148F")

    label("loc_147D")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_148F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B2")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_150A")

    label("loc_14B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D5")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_150A")

    label("loc_14D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F8")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_150A")

    label("loc_14F8")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_150A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152D")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1585")

    label("loc_152D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1550")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1585")

    label("loc_1550")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1573")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1585")

    label("loc_1573")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1585")

    Jump("loc_1BFA")

    label("loc_1588")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B9")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1611")

    label("loc_15B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DC")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1611")

    label("loc_15DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15FF")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1611")

    label("loc_15FF")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1611")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1634")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_168C")

    label("loc_1634")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1657")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_168C")

    label("loc_1657")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167A")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_168C")

    label("loc_167A")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_168C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16AF")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1707")

    label("loc_16AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D2")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1707")

    label("loc_16D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F5")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1707")

    label("loc_16F5")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1707")

    Jump("loc_1BFA")

    label("loc_170A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173B")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1793")

    label("loc_173B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175E")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1793")

    label("loc_175E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1781")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1793")

    label("loc_1781")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1793")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B6")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_180E")

    label("loc_17B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D9")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_180E")

    label("loc_17D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FC")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_180E")

    label("loc_17FC")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_180E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1831")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1889")

    label("loc_1831")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1854")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1889")

    label("loc_1854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1877")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1889")

    label("loc_1877")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1889")

    Jump("loc_1BFA")

    label("loc_188C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A0E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BD")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1915")

    label("loc_18BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E0")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1915")

    label("loc_18E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1903")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1915")

    label("loc_1903")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1915")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1938")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1990")

    label("loc_1938")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_195B")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1990")

    label("loc_195B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197E")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1990")

    label("loc_197E")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1990")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B3")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A0B")

    label("loc_19B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D6")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A0B")

    label("loc_19D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F9")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A0B")

    label("loc_19F9")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1A0B")

    Jump("loc_1BFA")

    label("loc_1A0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A31")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A89")

    label("loc_1A31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A54")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A89")

    label("loc_1A54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A77")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A89")

    label("loc_1A77")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1A89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AAC")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1B04")

    label("loc_1AAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACF")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1B04")

    label("loc_1ACF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF2")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1B04")

    label("loc_1AF2")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1B04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B27")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1B7F")

    label("loc_1B27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4A")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1B7F")

    label("loc_1B4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6D")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1B7F")

    label("loc_1B6D")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1B7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BA2")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1BFA")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC5")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1BFA")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE8")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1BFA")

    label("loc_1BE8")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1BFA")


    def lambda_1C00():
        OP_8F(0xFE, 0x4E2, 0x0, 0x2616, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1C00)
    Sleep(100)

    def lambda_1C20():
        OP_8F(0xFE, 0xFFFFFBB4, 0x0, 0x254E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1C20)
    Sleep(100)

    def lambda_1C40():
        OP_8F(0xFE, 0x280, 0x0, 0x2DF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1C40)
    Sleep(100)

    def lambda_1C60():
        OP_8F(0xFE, 0xFFFFFDC6, 0x0, 0x2DDC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1C60)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEF, 0x1)
    WaitChrThread(0xF0, 0x1)
    WaitChrThread(0xF1, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CCD")

    ChrTalk(    #42
        0x101,
        "#1005F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF4")

    ChrTalk(    #43
        0x102,
        "#1502F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1CF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D18")

    ChrTalk(    #44
        0x10B,
        "#216F#5PEeek!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1D18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3C")

    ChrTalk(    #45
        0x107,
        "#065F#5PEeek!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1D3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D65")

    ChrTalk(    #46
        0x10A,
        "#1317F#5POh, crap!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1D65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D8C")

    ChrTalk(    #47
        0x105,
        "#1162F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1D8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB3")

    ChrTalk(    #48
        0x103,
        "#1533F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD6")

    ChrTalk(    #49
        0x106,
        "#057F#5PGah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DFC")

    ChrTalk(    #50
        0x108,
        "#072F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1DFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E22")

    ChrTalk(    #51
        0x10E,
        "#178F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1E22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E49")

    ChrTalk(    #52
        0x104,
        "#1546F#5PNgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1E49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6F")

    ChrTalk(    #53
        0x10D,
        "#270F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E92")

    ChrTalk(    #54
        0x10C,
        "#112F#5PUgh...!\x02",
    )

    CloseMessageWindow()

    label("loc_1E92")

    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 0)
    SetChrSubChip(0xEE, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 2)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 4)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 6)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1F")

    ChrTalk(    #55
        0x107,
        "#065F#5PA-A golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_1F1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F55")

    ChrTalk(    #56
        0x101,
        "#1020F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_1F55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8A")

    ChrTalk(    #57
        0x106,
        "#057F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_1F8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC0")

    ChrTalk(    #58
        0x103,
        "#1533F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_1FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF6")

    ChrTalk(    #59
        0x105,
        "#1162F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_1FF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_202B")

    ChrTalk(    #60
        0x10A,
        "#812F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_202B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2062")

    ChrTalk(    #61
        0x10B,
        "#216F#5PA-A golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_2062")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2097")

    ChrTalk(    #62
        0x108,
        "#072F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_2097")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20CC")

    ChrTalk(    #63
        0x10E,
        "#172F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_20CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2102")

    ChrTalk(    #64
        0x104,
        "#1543F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_2102")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2137")

    ChrTalk(    #65
        0x10D,
        "#271F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2169")

    label("loc_2137")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2169")

    ChrTalk(    #66
        0x10C,
        "#117F#5PA golden Pater-Mater?!\x02",
    )

    CloseMessageWindow()

    label("loc_2169")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2422")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2248")

    ChrTalk(    #67
        0x110,
        (
            "#263F#5PIt's Gordias Type-0.\x02\x03",

            "#1306FIt's basically the prototype that went on to\x01",
            "become Pater-Mater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#1506F#5PIt might be even stronger than the real one,\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A5")

    label("loc_2248")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22F9")

    ChrTalk(    #69
        0x110,
        (
            "#1306F#5PIt's Gordias Type-0.\x02\x03",

            "It's basically the prototype that went on to\x01",
            "become Pater-Mater.\x02\x03",

            "#261FIt might be even stronger than the real one,\x01",
            "too! ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A5")

    label("loc_22F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A5")

    ChrTalk(    #70
        0x102,
        (
            "#1505F#5PIt's Gordias Type-0.\x02\x03",

            "It's basically the prototype that went on to\x01",
            "become Pater-Mater!\x02\x03",

            "#1506FIt might be even stronger than the real one,\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C8")

    ChrTalk(    #71
        0x101,
        "#1019F#5PFrick.\x02",
    )

    CloseMessageWindow()

    label("loc_23C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23EC")

    ChrTalk(    #72
        0x107,
        "#065F#5PEeeeeek!\x02",
    )

    CloseMessageWindow()

    label("loc_23EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2422")

    ChrTalk(    #73
        0x106,
        "#055F#5PYou've gotta be kidding...\x02",
    )

    CloseMessageWindow()

    label("loc_2422")

    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(500)
    OP_A2(0x2C23)
    OP_E6(0x0, 0x0)
    OP_1D(0xE1)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #74
        "\x07\x05Select a route.\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2478")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26BE")
    OP_CC(0x0, 0x0, 0xFFFF, 0xAA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_END)), "loc_24AE")
    OP_CC(0x1, 0x0, "Right Gate Path")
    OP_CC(0x3, 0x0, 0x0)
    Jump("loc_24C1")

    label("loc_24AE")

    OP_CC(0x1, 0x0, "Right Gate Path")

    label("loc_24C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_END)), "loc_24E1")
    OP_CC(0x1, 0x0, "Left Gate Path")
    OP_CC(0x3, 0x0, 0x1)
    Jump("loc_24F3")

    label("loc_24E1")

    OP_CC(0x1, 0x0, "Left Gate Path")

    label("loc_24F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_END)), "loc_2513")
    OP_CC(0x1, 0x0, "Main Gate Path")
    OP_CC(0x3, 0x0, 0x2)
    Jump("loc_2525")

    label("loc_2513")

    OP_CC(0x1, 0x0, "Main Gate Path")

    label("loc_2525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_254A")
    OP_CC(0x1, 0x0, "Giant Gate Path")
    Jump("loc_2561")

    label("loc_254A")

    OP_CC(0x1, 0x0, "Giant Gate Path")
    OP_CC(0x3, 0x0, 0x3)

    label("loc_2561")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_258C"),
        (1, "loc_25E2"),
        (2, "loc_2638"),
        (3, "loc_268E"),
        (SWITCH_DEFAULT, "loc_26BB"),
    )


    label("loc_258C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E2")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25AE")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25C6")

    label("loc_25AE")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C6")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25C6")

    label("loc_25C6")

    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7409   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26BB")

    label("loc_25E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2638")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2604")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_261C")

    label("loc_2604")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_261C")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_261C")

    label("loc_261C")

    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7413   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26BB")

    label("loc_2638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268E")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_265A")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2672")

    label("loc_265A")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2672")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2672")

    label("loc_2672")

    OP_DC(0x0, 0x2)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7418   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26BB")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26BB")
    OP_56(0x0)
    OP_DC(0x0, 0x3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7422   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26BB")

    label("loc_26BB")

    Jump("loc_2478")

    label("loc_26BE")

    Return()

    # Function_2_125 end

    def Function_3_26BF(): pass

    label("Function_3_26BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x40, 0x2)
    OP_E0(238, 0x41, 0x3)
    OP_E0(239, 0x42, 0x2)
    OP_E0(239, 0x43, 0x3)
    OP_E0(240, 0x44, 0x2)
    OP_E0(240, 0x45, 0x3)
    OP_E0(241, 0x46, 0x2)
    OP_E0(241, 0x47, 0x3)
    SetChrPos(0xEE, -1210, 0, 13920, 0)
    SetChrPos(0xEF, 650, 0, 14010, 0)
    SetChrPos(0xF0, -1410, 0, 12110, 0)
    SetChrPos(0xF1, 800, 0, 12420, 0)
    SetChrChipByIndex(0xEE, 0)
    SetChrSubChip(0xEE, 0)
    SetChrChipByIndex(0xEF, 2)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 4)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 6)
    SetChrSubChip(0xF1, 0)
    SetChrPos(0x10, 0, 0, 24000, 180)
    OP_A1(0x10, 0x6)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_B0(0x6, 0x1E)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x28)
    OP_82(0x85, 0x0)
    OP_6D(6080, 0, 30550, 0)
    OP_67(0, 3260, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(40000, 0)
    OP_6E(478, 0)

    def lambda_27D3():
        OP_6D(4880, 250, 23700, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_27D3)

    def lambda_27EB():
        OP_67(0, 3200, -10000, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_27EB)

    def lambda_2803():
        OP_6B(3620, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2803)

    def lambda_2813():
        OP_6C(45000, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2813)

    def lambda_2823():
        OP_6E(425, 3500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2823)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #75 op#A
        (
            "\x07\x02#60W#55AAs we speak, my minions are extending a warm\x01",
            "welcome to your friends...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC(0x0, 0x1)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_26BF end

    def Function_4_28EE(): pass

    label("Function_4_28EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x40, 0x2)
    OP_E0(238, 0x41, 0x3)
    OP_E0(239, 0x42, 0x2)
    OP_E0(239, 0x43, 0x3)
    OP_E0(240, 0x44, 0x2)
    OP_E0(240, 0x45, 0x3)
    OP_E0(241, 0x46, 0x2)
    OP_E0(241, 0x47, 0x3)
    SetChrPos(0xEE, -570, 0, 12740, 0)
    SetChrPos(0xEF, 640, 0, 12760, 0)
    SetChrPos(0xF0, -1100, 0, 10550, 0)
    SetChrPos(0xF1, 1250, 0, 10750, 0)
    SetChrChipByIndex(0xEE, 0)
    SetChrSubChip(0xEE, 0)
    SetChrChipByIndex(0xEF, 2)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 4)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 6)
    SetChrSubChip(0xF1, 0)
    SetChrPos(0x10, 0, 0, 24000, 180)
    OP_A1(0x10, 0x6)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_B0(0x6, 0x1E)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x28)
    OP_6D(0, 600, 25240, 0)
    OP_67(0, 2210, -10000, 0)
    OP_6B(4860, 0)
    OP_6C(0, 0)
    OP_6E(285, 0)
    FadeToBright(500, 0)
    OP_0D()
    Battle(0x334, 0x0, 0x0, 0x0, 0xFF)
    OP_A2(0x2C2A)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A40")
    OP_DC(0x0, 0x3)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B09")

    label("loc_2A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AA5")
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A69")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AA2")

    label("loc_2A69")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A87")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AA2")

    label("loc_2A87")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA2")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2AA2")

    Jump("loc_2B09")

    label("loc_2AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B09")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD0")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B09")

    label("loc_2AD0")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AEE")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B09")

    label("loc_2AEE")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B09")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2B09")

    Return()

    # Function_4_28EE end

    SaveToFile()

Try(main)
