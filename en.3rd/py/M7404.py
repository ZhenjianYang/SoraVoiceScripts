from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7404   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7404.x',
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
        'Gespenst',                             # 9
        'Gespenst',                             # 10
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
        "Function_0_EA",           # 00, 0
        "Function_1_13E",          # 01, 1
        "Function_2_14B",          # 02, 2
        "Function_3_1FB8",         # 03, 3
        "Function_4_21FA",         # 04, 4
    )


    def Function_0_EA(): pass

    label("Function_0_EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_100")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_13D")

    label("loc_100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_11F")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_13D")

    label("loc_11F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_13D")

    Return()

    # Function_0_EA end

    def Function_1_13E(): pass

    label("Function_1_13E")

    OP_71(0x406, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    Return()

    # Function_1_13E end

    def Function_2_14B(): pass

    label("Function_2_14B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp271_00.eff")
    LoadEffect(0x1, "monster\\ms30105a.eff")
    LoadEffect(0x2, "monster\\ms30803a.eff")
    LoadEffect(0x3, "map\\mp277_00.eff")
    OP_E0(242, 0x40, 0x2)
    OP_E0(242, 0x41, 0x3)
    OP_E0(243, 0x42, 0x2)
    OP_E0(243, 0x43, 0x3)
    OP_E0(244, 0x44, 0x2)
    OP_E0(244, 0x45, 0x3)
    OP_E0(245, 0x46, 0x2)
    OP_E0(245, 0x47, 0x3)
    SetChrPos(0xF2, -840, 0, -10480, 0)
    SetChrPos(0xF3, 550, 0, -10450, 0)
    SetChrPos(0xF4, -1260, 0, -12070, 0)
    SetChrPos(0xF5, 610, 0, -12180, 0)
    OP_6D(5130, -28700, 26260, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(7270, 0)
    OP_6C(45000, 0)
    OP_6E(672, 0)

    def lambda_25A():
        OP_6D(5130, -100, 26260, 8000)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_25A)

    def lambda_272():
        OP_67(0, 6470, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_272)

    def lambda_28A():
        OP_8E(0xFE, 0xFFFFFB5A, 0x0, 0x2F9E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF2, 0, lambda_28A)
    Sleep(100)

    def lambda_2AA():
        OP_8E(0xFE, 0x212, 0x0, 0x2FBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF3, 0, lambda_2AA)
    Sleep(100)

    def lambda_2CA():
        OP_8E(0xFE, 0xFFFFF948, 0x0, 0x283C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2CA)
    Sleep(100)

    def lambda_2EA():
        OP_8E(0xFE, 0x1EA, 0x0, 0x2850, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2EA)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xF2, 0x1)
    WaitChrThread(0xF3, 0x1)

    def lambda_319():
        OP_6B(7500, 3000)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_319)

    def lambda_329():
        OP_6E(700, 3000)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_329)
    WaitChrThread(0xF2, 0x0)
    WaitChrThread(0xF3, 0x0)
    WaitChrThread(0xF4, 0x0)
    WaitChrThread(0xF5, 0x0)
    WaitChrThread(0xF4, 0x1)
    WaitChrThread(0xF5, 0x1)
    Fade(1000)
    OP_6D(1300, 0, 13000, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E0")

    ChrTalk(    #0
        0x101,
        "#1004F#5PI...guess this is the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_3E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A")

    ChrTalk(    #1
        0x102,
        "#1503F#5PI guess this must be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_42A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_470")

    ChrTalk(    #2
        0x10B,
        "#212F#5PI...guess this is the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_470")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB")

    ChrTalk(    #3
        0x110,
        "#1305F#5POh... This looks like the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_4BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_501")

    ChrTalk(    #4
        0x107,
        "#065F#5PI...guess this is the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_501")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_547")

    ChrTalk(    #5
        0x10A,
        "#814F#5PI...guess this is the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_547")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589")

    ChrTalk(    #6
        0x105,
        "#1164F#5PThis must be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_589")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")

    ChrTalk(    #7
        0x103,
        "#1523F#5PI...guess this is the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_619")

    ChrTalk(    #8
        0x106,
        "#555F#5PI guess this must be the end of this wing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_619")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_663")

    ChrTalk(    #9
        0x108,
        "#072F#5POh... This looks like the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_663")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B0")

    ChrTalk(    #10
        0x10E,
        "#178F#5POh... This appears to be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_6B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FF")

    ChrTalk(    #11
        0x104,
        "#1542F#5PHmm... This appears to be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_6FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_749")

    ChrTalk(    #12
        0x10D,
        "#276F#5P...This appears to be the end of this wing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_794")

    ChrTalk(    #13
        0x10C,
        "#112F#5PHmm... This appears to be the end of this wing.\x02",
    )

    CloseMessageWindow()

    label("loc_794")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D1")

    ChrTalk(    #14
        0x101,
        "#1015F#5PThere's nothing here, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_7D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83F")

    ChrTalk(    #15
        0x102,
        (
            "#1503F#5PThat's strange. I would've expected there\x01",
            "to be something here waiting for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_83F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87B")

    ChrTalk(    #16
        0x10B,
        "#212F#5PThere's nothing here, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_87B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C9")

    ChrTalk(    #17
        0x110,
        "#1305F#5PStrange... I can't sense anything here at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_8C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_903")

    ChrTalk(    #18
        0x107,
        "#063F#5PBut there's nothing here...\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_903")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_935")

    ChrTalk(    #19
        0x10A,
        "#812F#5PIt's empty, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_935")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_972")

    ChrTalk(    #20
        0x105,
        "#1163F#5PThere's nothing here, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_972")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E0")

    ChrTalk(    #21
        0x103,
        (
            "#1532F#5PThat's strange. I would've expected there\x01",
            "to be something here waiting for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_9E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A24")

    ChrTalk(    #22
        0x106,
        "#552F#5PBah. Wonder why there's nothing here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_A24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A71")

    ChrTalk(    #23
        0x108,
        "#572F#5PStrange... I can't sense anything here at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_A71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABE")

    ChrTalk(    #24
        0x10E,
        "#178F#5PStrange... I can't sense anything here at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_ABE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2E")

    ChrTalk(    #25
        0x104,
        (
            "#1540F#5PHow peculiar... I would have expected there\x01",
            "to be something waiting here for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_B2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B")

    ChrTalk(    #26
        0x10D,
        "#276F#5PStrange... I can't sense anything here at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBB")

    ChrTalk(    #27
        0x10C,
        "#112F#5PHmm... And yet there's nothing here.\x02",
    )

    CloseMessageWindow()

    label("loc_BBB")

    Sleep(500)
    OP_20(0x5DC)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #28 op#A op#5
        "\x07\x02#15ADisengaging standby mode...\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C49")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CB0")

    label("loc_C49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C71")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CB0")

    label("loc_C71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C99")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CB0")

    label("loc_C99")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CB0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDD")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D44")

    label("loc_CDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D05")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D44")

    label("loc_D05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2D")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D44")

    label("loc_D2D")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D44")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D71")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DD8")

    label("loc_D71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D99")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DD8")

    label("loc_D99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC1")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DD8")

    label("loc_DC1")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_DD8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E05")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E6C")

    label("loc_E05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2D")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E6C")

    label("loc_E2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E55")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E6C")

    label("loc_E55")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E6C")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA3")

    ChrTalk(    #29
        0x101,
        "#1020F#6PWh-What was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_EA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED2")

    ChrTalk(    #30
        0x102,
        "#1502F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_ED2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F11")

    ChrTalk(    #31
        0x110,
        "#264F#6PWas that a synthesized voice...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_F11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F42")

    ChrTalk(    #32
        0x10B,
        "#216F#6PWh-What was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_F42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F73")

    ChrTalk(    #33
        0x107,
        "#065F#6PWh-What was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_F73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA5")

    ChrTalk(    #34
        0x10A,
        "#1317F#6PWh-What was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_FA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD4")

    ChrTalk(    #35
        0x105,
        "#1163F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_FD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1003")

    ChrTalk(    #36
        0x103,
        "#1523F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_1003")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1031")

    ChrTalk(    #37
        0x106,
        "#052F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_1031")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105F")

    ChrTalk(    #38
        0x108,
        "#072F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_105F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108D")

    ChrTalk(    #39
        0x10E,
        "#172F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_108D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BC")

    ChrTalk(    #40
        0x104,
        "#1543F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_10BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EA")

    ChrTalk(    #41
        0x10D,
        "#273F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_10EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1115")

    ChrTalk(    #42
        0x10C,
        "#113F#6PWhat was that?!\x02",
    )

    CloseMessageWindow()

    label("loc_1115")


    def lambda_111B():
        OP_6B(4000, 16000)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_111B)
    OP_1D(0x2D)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #43 op#A op#5
        "\x07\x02#15ARebooting systems...\x05\x02",
    )

    CloseMessageWindow()
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #44 op#A op#5
        "\x07\x02#15AReboot process complete.\x05\x02",
    )

    CloseMessageWindow()
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #45 op#A op#5
        "\x07\x02#15ALocation confirmed.\x05\x02",
    )

    CloseMessageWindow()
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #46 op#A op#5
        (
            "\x07\x02#35ACurrently situated in the left wing\x01",
            "of Phantasmagoria.\x05\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #47 op#A op#5
        "\x07\x02#30AConfirming the presence of intruders.\x05\x02",
    )

    CloseMessageWindow()
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #48 op#A op#5
        "\x07\x02#30ACommencing materialization process.\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(500)
    OP_44(0xF4, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x415, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_6D(220, 0, 19000, 0)
    OP_67(0, 3000, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(55000, 0)
    OP_6E(450, 0)

    def lambda_1321():
        OP_6D(3440, 1050, 27500, 5500)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_1321)

    def lambda_1339():
        OP_67(0, 5000, -10000, 5500)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_1339)

    def lambda_1351():
        OP_6B(3200, 5500)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1351)

    def lambda_1361():
        OP_6C(45000, 5500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1361)

    def lambda_1371():
        OP_6E(500, 5500)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1371)
    OP_0D()
    OP_22(0x1BB, 0x0, 0x64)
    OP_22(0x1BC, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0xFF, 0, 2800, 24000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 0, 2800, 24000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x10, 0, 0, 24000, 0)
    OP_A1(0x10, 0x6)
    OP_B0(0x6, 0x1E)
    OP_6F(0x6, 50)
    OP_70(0x6, 0x32)
    SetChrPos(0x11, 0, 0, 24000, 0)
    OP_A1(0x11, 0x17)
    OP_B0(0x17, 0x1E)
    OP_6F(0x17, 50)
    OP_70(0x17, 0x32)
    WaitChrThread(0xF2, 0x1)
    WaitChrThread(0xF3, 0x1)
    WaitChrThread(0xF4, 0x1)
    WaitChrThread(0xF5, 0x1)
    Sleep(500)

    def lambda_145F():
        OP_67(0, 4500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_145F)

    def lambda_1477():
        OP_6B(3200, 8000)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1477)

    def lambda_1487():
        OP_6E(360, 8000)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1487)
    OP_82(0x1, 0x2)
    Fade(2000)
    OP_22(0x3BE, 0x0, 0x64)
    OP_72(0x417, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    OP_82(0x0, 0x2)
    Fade(2000)
    OP_82(0x0, 0x0)
    OP_22(0x28F, 0x0, 0x64)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_0D()
    OP_23(0x149)
    Fade(1000)
    OP_44(0xF2, 0x1)
    OP_44(0xF3, 0x1)
    OP_44(0xF4, 0x1)
    OP_44(0xF5, 0x1)
    OP_6D(0, 0, 31750, 0)
    OP_67(0, 5250, -10000, 0)
    OP_6B(3530, 0)
    OP_6C(0, 0)
    OP_6E(483, 0)

    def lambda_1522():
        OP_6D(0, 1000, 31750, 2000)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_1522)

    def lambda_153A():
        OP_67(0, 2000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_153A)

    def lambda_1552():
        OP_6B(2630, 2000)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1552)

    def lambda_1562():
        OP_6E(480, 2000)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1562)
    OP_B0(0x6, 0x23)
    OP_6F(0x6, 640)
    OP_70(0x6, 0x2A8)
    OP_73(0x6)
    Fade(200)

    def lambda_158C():
        OP_6E(395, 200)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_158C)
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_B0(0x6, 0x23)
    OP_6F(0x6, 680)
    OP_70(0x6, 0x2C1)
    Sleep(100)
    OP_22(0xF2, 0x0, 0x64)
    OP_7C(0xFA, 0xFA, 0xBB8, 0x64)
    OP_73(0x6)
    WaitChrThread(0xF2, 0x1)
    WaitChrThread(0xF3, 0x1)
    WaitChrThread(0xF4, 0x1)
    WaitChrThread(0xF5, 0x1)
    Fade(500)
    PlayEffect(0x1, 0x7, 0x10, -10, 3230, 800, 180, -32, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xF3, 0x0, 0x64)
    Sleep(2000)
    OP_6F(0x6, 706)
    OP_70(0x6, 0x2DA)
    SetChrPos(0xF2, -570, 0, 12740, 0)
    SetChrPos(0xF3, 640, 0, 12760, 0)
    SetChrPos(0xF4, -1100, 0, 10550, 0)
    SetChrPos(0xF5, 1250, 0, 10750, 0)

    def lambda_167C():
        OP_6D(0, 300, 32049, 3000)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_167C)

    def lambda_1694():
        OP_67(0, 1460, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_1694)

    def lambda_16AC():
        OP_6B(5700, 3000)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_16AC)

    def lambda_16BC():
        OP_6E(310, 3000)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_16BC)
    OP_73(0x6)
    OP_71(0x2006, 0x0)
    ExitThread()
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 50)
    OP_70(0x6, 0x59)
    OP_0D()
    WaitChrThread(0xF2, 0x1)
    WaitChrThread(0xF3, 0x1)
    WaitChrThread(0xF4, 0x1)
    WaitChrThread(0xF5, 0x1)
    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1722")

    ChrTalk(    #49
        0x101,
        "#1005F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_1722")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1749")

    ChrTalk(    #50
        0x102,
        "#1502F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_1749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1770")

    ChrTalk(    #51
        0x110,
        "#265F#5POh my...\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_1770")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1794")

    ChrTalk(    #52
        0x10B,
        "#216F#5PEeek!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_1794")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B8")

    ChrTalk(    #53
        0x107,
        "#065F#5PEeek!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_17B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DD")

    ChrTalk(    #54
        0x10A,
        "#1317F#5PWhoa!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_17DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1804")

    ChrTalk(    #55
        0x105,
        "#1162F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_1804")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182B")

    ChrTalk(    #56
        0x103,
        "#1533F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_182B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184E")

    ChrTalk(    #57
        0x106,
        "#057F#5PGah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_184E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1874")

    ChrTalk(    #58
        0x108,
        "#072F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_1874")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189A")

    ChrTalk(    #59
        0x10E,
        "#178F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_189A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C1")

    ChrTalk(    #60
        0x104,
        "#1546F#5PNgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_18C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E7")

    ChrTalk(    #61
        0x10D,
        "#270F#5PUgh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_18E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190A")

    ChrTalk(    #62
        0x10C,
        "#112F#5PUgh...!\x02",
    )

    CloseMessageWindow()

    label("loc_190A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192D")
    OP_62(0xF2, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1985")

    label("loc_192D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1950")
    OP_62(0xF2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1985")

    label("loc_1950")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1973")
    OP_62(0xF2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1985")

    label("loc_1973")

    OP_62(0xF2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1985")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A8")
    OP_62(0xF3, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A00")

    label("loc_19A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CB")
    OP_62(0xF3, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A00")

    label("loc_19CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19EE")
    OP_62(0xF3, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A00")

    label("loc_19EE")

    OP_62(0xF3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1A00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A23")
    OP_62(0xF4, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A7B")

    label("loc_1A23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A46")
    OP_62(0xF4, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A7B")

    label("loc_1A46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A69")
    OP_62(0xF4, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A7B")

    label("loc_1A69")

    OP_62(0xF4, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1A7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A9E")
    OP_62(0xF5, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1AF6")

    label("loc_1A9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC1")
    OP_62(0xF5, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1AF6")

    label("loc_1AC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE4")
    OP_62(0xF5, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1AF6")

    label("loc_1AE4")

    OP_62(0xF5, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1AF6")


    def lambda_1AFC():
        OP_8F(0xFE, 0x4E2, 0x0, 0x2616, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1AFC)
    Sleep(100)

    def lambda_1B1C():
        OP_8F(0xFE, 0xFFFFFBB4, 0x0, 0x254E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1B1C)
    Sleep(100)

    def lambda_1B3C():
        OP_8F(0xFE, 0x280, 0x0, 0x2DF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF3, 0, lambda_1B3C)
    Sleep(100)

    def lambda_1B5C():
        OP_8F(0xFE, 0xFFFFFDC6, 0x0, 0x2DDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF2, 0, lambda_1B5C)
    WaitChrThread(0xF2, 0x0)
    WaitChrThread(0xF3, 0x0)
    WaitChrThread(0xF4, 0x0)
    WaitChrThread(0xF5, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF2, 0)
    SetChrSubChip(0xF2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF3, 2)
    SetChrSubChip(0xF3, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF4, 4)
    SetChrSubChip(0xF4, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF5, 6)
    SetChrSubChip(0xF5, 0)
    OP_0D()
    Sleep(300)
    Sleep(500)

    def lambda_1BE6():
        OP_6B(5200, 9000)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1BE6)
    SetMessageWindowPos(-1, 200, -1, -1)
    SetChrName("Synthesized Voice")

    AnonymousTalk(    #63 op#A op#5
        "\x07\x02#20ASwitching to Genocide mode.\x05\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    AnonymousTalk(    #64 op#A op#5
        "\x07\x02#25AReverie Mk.2, Gespenst...\x05\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    AnonymousTalk(    #65 op#A op#5
        "\x07\x02#33ACommencing elimination of intruders.\x05\x02",
    )

    OP_22(0x85, 0x1, 0x64)

    def lambda_1C99():

        label("loc_1C99")

        OP_7C(0x0, 0x96, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1C99")

    QueueWorkItem2(0xF2, 3, lambda_1C99)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_44(0xF2, 0x3)
    OP_24(0x85, 0x5A)
    Sleep(150)
    OP_24(0x85, 0x50)
    Sleep(150)
    OP_24(0x85, 0x46)
    Sleep(150)
    OP_24(0x85, 0x3C)
    Sleep(150)
    OP_24(0x85, 0x32)
    Sleep(150)
    OP_24(0x85, 0x28)
    Sleep(150)
    OP_24(0x85, 0x1E)
    Sleep(150)
    OP_24(0x85, 0x14)
    Sleep(150)
    OP_24(0x85, 0xA)
    Sleep(150)
    OP_24(0x85, 0x0)
    Sleep(150)
    OP_23(0x85)
    OP_21()
    Sleep(1000)
    OP_A2(0x2C24)
    OP_E6(0x0, 0x1)
    OP_1D(0xE1)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05Select a route.\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB7")
    OP_CC(0x0, 0x0, 0xFFFF, 0xAA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_END)), "loc_1DA7")
    OP_CC(0x1, 0x0, "Right Gate Path")
    OP_CC(0x3, 0x0, 0x0)
    Jump("loc_1DBA")

    label("loc_1DA7")

    OP_CC(0x1, 0x0, "Right Gate Path")

    label("loc_1DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_END)), "loc_1DDA")
    OP_CC(0x1, 0x0, "Left Gate Path")
    OP_CC(0x3, 0x0, 0x1)
    Jump("loc_1DEC")

    label("loc_1DDA")

    OP_CC(0x1, 0x0, "Left Gate Path")

    label("loc_1DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_END)), "loc_1E0C")
    OP_CC(0x1, 0x0, "Main Gate Path")
    OP_CC(0x3, 0x0, 0x2)
    Jump("loc_1E1E")

    label("loc_1E0C")

    OP_CC(0x1, 0x0, "Main Gate Path")

    label("loc_1E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E43")
    OP_CC(0x1, 0x0, "Giant Gate Path")
    Jump("loc_1E5A")

    label("loc_1E43")

    OP_CC(0x1, 0x0, "Giant Gate Path")
    OP_CC(0x3, 0x0, 0x3)

    label("loc_1E5A")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E85"),
        (1, "loc_1EDB"),
        (2, "loc_1F31"),
        (3, "loc_1F87"),
        (SWITCH_DEFAULT, "loc_1FB4"),
    )


    label("loc_1E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDB")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA7")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EBF")

    label("loc_1EA7")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EBF")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EBF")

    label("loc_1EBF")

    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7409   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FB4")

    label("loc_1EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F31")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EFD")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F15")

    label("loc_1EFD")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F15")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F15")

    label("loc_1F15")

    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7413   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FB4")

    label("loc_1F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F87")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F53")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F6B")

    label("loc_1F53")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6B")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F6B")

    label("loc_1F6B")

    OP_DC(0x0, 0x2)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7418   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FB4")

    label("loc_1F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FB4")
    OP_56(0x0)
    OP_DC(0x0, 0x3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7422   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FB4")

    label("loc_1FB4")

    Jump("loc_1D71")

    label("loc_1FB7")

    Return()

    # Function_2_14B end

    def Function_3_1FB8(): pass

    label("Function_3_1FB8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(242, 0x40, 0x2)
    OP_E0(242, 0x41, 0x3)
    OP_E0(243, 0x42, 0x2)
    OP_E0(243, 0x43, 0x3)
    OP_E0(244, 0x44, 0x2)
    OP_E0(244, 0x45, 0x3)
    OP_E0(245, 0x46, 0x2)
    OP_E0(245, 0x47, 0x3)
    SetChrPos(0xF2, -530, 0, 13480, 0)
    SetChrPos(0xF3, 1320, 0, 13560, 0)
    SetChrPos(0xF4, -370, 0, 11580, 0)
    SetChrPos(0xF5, 1940, 0, 11420, 0)
    SetChrChipByIndex(0xF2, 0)
    SetChrSubChip(0xF2, 0)
    SetChrChipByIndex(0xF3, 2)
    SetChrSubChip(0xF3, 0)
    SetChrChipByIndex(0xF4, 4)
    SetChrSubChip(0xF4, 0)
    SetChrChipByIndex(0xF5, 6)
    SetChrSubChip(0xF5, 0)
    OP_71(0x415, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    SetChrPos(0x10, 0, 0, 24000, 0)
    OP_A1(0x10, 0x6)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_71(0x2006, 0x0)
    ExitThread()
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 50)
    OP_70(0x6, 0x59)
    OP_82(0x84, 0x0)
    OP_6D(-4640, 10, 31070, 0)
    OP_67(0, 3570, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(325000, 0)
    OP_6E(472, 0)

    def lambda_20DE():
        OP_6D(-1590, 1000, 20570, 3500)
        ExitThread()

    QueueWorkItem(0xF2, 0, lambda_20DE)

    def lambda_20F6():
        OP_67(0, 3990, -10000, 3500)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_20F6)

    def lambda_210E():
        OP_6B(3300, 3500)
        ExitThread()

    QueueWorkItem(0xF2, 2, lambda_210E)

    def lambda_211E():
        OP_6C(315000, 3500)
        ExitThread()

    QueueWorkItem(0xF2, 3, lambda_211E)

    def lambda_212E():
        OP_6E(450, 3500)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_212E)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF2, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #67 op#A
        (
            "\x07\x02#60W#60AShould a single group of them fail, the future\x01",
            "will be closed forever...\x02",
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
    OP_DC(0x0, 0x2)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1FB8 end

    def Function_4_21FA(): pass

    label("Function_4_21FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(242, 0x40, 0x2)
    OP_E0(242, 0x41, 0x3)
    OP_E0(243, 0x42, 0x2)
    OP_E0(243, 0x43, 0x3)
    OP_E0(244, 0x44, 0x2)
    OP_E0(244, 0x45, 0x3)
    OP_E0(245, 0x46, 0x2)
    OP_E0(245, 0x47, 0x3)
    SetChrPos(0xF2, -570, 0, 12740, 0)
    SetChrPos(0xF3, 640, 0, 12760, 0)
    SetChrPos(0xF4, -1100, 0, 10550, 0)
    SetChrPos(0xF5, 1250, 0, 10750, 0)
    SetChrChipByIndex(0xF2, 0)
    SetChrSubChip(0xF2, 0)
    SetChrChipByIndex(0xF3, 2)
    SetChrSubChip(0xF3, 0)
    SetChrChipByIndex(0xF4, 4)
    SetChrSubChip(0xF4, 0)
    SetChrChipByIndex(0xF5, 6)
    SetChrSubChip(0xF5, 0)
    SetChrPos(0x10, 0, 0, 24000, 0)
    OP_A1(0x10, 0x6)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 50)
    OP_70(0x6, 0x59)
    OP_6D(0, 600, 25240, 0)
    OP_67(0, 2210, -10000, 0)
    OP_6B(4860, 0)
    OP_6C(0, 0)
    OP_6E(285, 0)
    FadeToBright(500, 0)
    OP_0D()
    Battle(0x335, 0x0, 0x0, 0x0, 0xFF)
    OP_A2(0x2C2B)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_234C")
    OP_DC(0x0, 0x3)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2415")

    label("loc_234C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23B1")
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2375")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_23AE")

    label("loc_2375")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2393")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_23AE")

    label("loc_2393")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23AE")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_23AE")

    Jump("loc_2415")

    label("loc_23B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2415")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23DC")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2415")

    label("loc_23DC")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23FA")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2415")

    label("loc_23FA")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2415")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2415")

    Return()

    # Function_4_21FA end

    SaveToFile()

Try(main)
