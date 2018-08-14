from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '极限级零式',                           # 9
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
        "Function_3_267F",         # 03, 3
        "Function_4_2897",         # 04, 4
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350")

    ChrTalk(    #0
        0x101,
        "#1002F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_350")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_381")

    ChrTalk(    #1
        0x102,
        "#1502F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_381")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1")

    ChrTalk(    #2
        0x10B,
        "#212F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_3B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E8")

    ChrTalk(    #3
        0x110,
        "#1305F#5P哎呀，这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_3E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C")

    ChrTalk(    #4
        0x107,
        "#065F#5P这、这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_41C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C")

    ChrTalk(    #5
        0x10A,
        "#812F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_44C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47D")

    ChrTalk(    #6
        0x105,
        "#1162F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_47D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE")

    ChrTalk(    #7
        0x103,
        "#1522F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_4AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE")

    ChrTalk(    #8
        0x106,
        "#057F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_4DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50E")

    ChrTalk(    #9
        0x108,
        "#072F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_50E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53E")

    ChrTalk(    #10
        0x10E,
        "#172F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_53E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_573")

    ChrTalk(    #11
        0x104,
        "#1542F#5P唔，这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_573")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A3")

    ChrTalk(    #12
        0x10D,
        "#270F#5P这里是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D0")

    label("loc_5A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")

    ChrTalk(    #13
        0x10C,
        "#112F#5P这里是……\x02",
    )

    CloseMessageWindow()

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_612")

    ChrTalk(    #14
        0x101,
        (
            "#1002F#5P看上去……\x01",
            "像是到了终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_612")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_654")

    ChrTalk(    #15
        0x102,
        (
            "#1502F#5P看上去……\x01",
            "像是到了终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_654")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_691")

    ChrTalk(    #16
        0x10B,
        (
            "#210F#5P唔……\x01",
            "像是到了终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_691")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D5")

    ChrTalk(    #17
        0x110,
        (
            "#1306F#5P嘻嘻……\x01",
            "看来这里就是终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_6D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716")

    ChrTalk(    #18
        0x107,
        (
            "#065F#5P是、是不是\x01",
            "已经到终点了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_716")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_755")

    ChrTalk(    #19
        0x10A,
        (
            "#812F#5P看来……\x01",
            "像是到了终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_755")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_795")

    ChrTalk(    #20
        0x105,
        (
            "#1162F#5P看来……\x01",
            "应该到终点了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_795")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D9")

    ChrTalk(    #21
        0x103,
        (
            "#1522F#5P原来如此……\x01",
            "这里就是终点吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_7D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_816")

    ChrTalk(    #22
        0x106,
        (
            "#552F#5P哼……\x01",
            "这里就是终点吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_816")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_855")

    ChrTalk(    #23
        0x108,
        (
            "#072F#5P唔……\x01",
            "看来已经到终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_855")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_892")

    ChrTalk(    #24
        0x10E,
        (
            "#178F#5P看来……\x01",
            "这里就是终点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_892")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D2")

    ChrTalk(    #25
        0x104,
        (
            "#1545F#5P呵……\x01",
            "看来已经到终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_8D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_910")

    ChrTalk(    #26
        0x10D,
        "#270F#5P……看来这里就是终点吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_910")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94C")

    ChrTalk(    #27
        0x10C,
        (
            "#110F#5P唔……\x01",
            "看来已经到终点了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94C")

    Sleep(500)

    def lambda_957():

        label("loc_957")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_957")

    QueueWorkItem2(0x10, 3, lambda_957)
    OP_22(0x113, 0x1, 0x46)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99E")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A05")

    label("loc_99E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C6")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A05")

    label("loc_9C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EE")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A05")

    label("loc_9EE")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A05")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A32")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A99")

    label("loc_A32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A99")

    label("loc_A5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A82")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A99")

    label("loc_A82")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A99")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC6")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B2D")

    label("loc_AC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B2D")

    label("loc_AEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B16")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B2D")

    label("loc_B16")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B2D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BC1")

    label("loc_B5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B82")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BC1")

    label("loc_B82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BC1")

    label("loc_BAA")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BC1")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFD")

    ChrTalk(    #28
        0x101,
        "#1020F#6P这、这声音……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_BFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C36")

    ChrTalk(    #29
        0x102,
        "#1506F#6P这声音……不会吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_C36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C70")

    ChrTalk(    #30
        0x10B,
        "#216F#6P什、什么，这声音……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_C70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAD")

    ChrTalk(    #31
        0x107,
        (
            "#065F#6P这声音……\x01",
            "难、难道是！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_CAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF1")

    ChrTalk(    #32
        0x10A,
        (
            "#1317F#6P这声音……\x01",
            "好像在哪里听到过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D28")

    ChrTalk(    #33
        0x105,
        "#1164F#6P这、这声音是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_D28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6C")

    ChrTalk(    #34
        0x103,
        (
            "#1523F#6P这声音……\x01",
            "好像在哪里听到过！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_D6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA2")

    ChrTalk(    #35
        0x106,
        "#052F#6P这声音是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_DA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE5")

    ChrTalk(    #36
        0x108,
        (
            "#073F#6P这声音……\x01",
            "好像在哪里听到过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_DE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1D")

    ChrTalk(    #37
        0x10E,
        "#173F#6P这声音……不会吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E63")

    ChrTalk(    #38
        0x104,
        (
            "#1542F#6P这声音是……\x01",
            "好像在哪里听到过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_E63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9B")

    ChrTalk(    #39
        0x10D,
        "#273F#6P什么呀……这声音？\x02",
    )

    CloseMessageWindow()
    Jump("loc_ECC")

    label("loc_E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECC")

    ChrTalk(    #40
        0x10C,
        "#113F#6P这声音是……？\x02",
    )

    CloseMessageWindow()

    label("loc_ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F35")

    ChrTalk(    #41
        0x110,
        (
            "#1306F嘻嘻，是这样啊。\x02\x03",

            "#261F嘻嘻……\x01",
            "『影之王』小姐\x01",
            "还真是会讨好人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F35")

    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_F49():

        label("loc_F49")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_F49")

    QueueWorkItem2(0x10, 3, lambda_F49)
    OP_24(0x113, 0x50)
    Sleep(500)

    def lambda_F6D():

        label("loc_F6D")

        OP_7C(0x28, 0x28, 0xBB8, 0x64)
        OP_48()
        Jump("loc_F6D")

    QueueWorkItem2(0x10, 3, lambda_F6D)
    OP_24(0x113, 0x5A)
    Sleep(500)

    def lambda_F91():

        label("loc_F91")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_F91")

    QueueWorkItem2(0x10, 3, lambda_F91)
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

    def lambda_FF0():
        OP_8F(0xFE, 0x0, 0x0, 0x5DC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_FF0)
    Fade(500)
    OP_6D(260, 3400, 23940, 0)
    OP_67(0, 14940, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(315000, 0)
    OP_6E(328, 0)

    def lambda_104D():
        OP_6B(1800, 1000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_104D)
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

    def lambda_10E7():
        OP_6B(1000, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_10E7)
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

    def lambda_1198():
        OP_6B(2000, 1000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1198)
    Sleep(500)
    Sleep(500)
    OP_44(0xF0, 0x1)
    OP_22(0xF0, 0x0, 0x64)
    OP_6D(3010, 3500, 26680, 0)
    OP_67(0, -1400, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(44000, 0)
    OP_6E(547, 0)

    def lambda_11F8():
        OP_6B(2000, 1000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_11F8)
    Sleep(500)
    Sleep(500)
    OP_44(0xF0, 0x1)
    OP_22(0xF0, 0x0, 0x64)
    OP_6D(10, 3500, 23940, 0)
    OP_67(0, 1800, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(306, 0)

    def lambda_1258():
        OP_6B(2930, 1000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1258)
    Sleep(500)
    Sleep(1000)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)

    def lambda_127C():
        OP_6D(0, 2500, 24310, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_127C)

    def lambda_1294():
        OP_67(0, 900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1294)

    def lambda_12AC():
        OP_6B(5710, 4000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_12AC)

    def lambda_12BC():
        OP_6E(234, 4000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_12BC)
    Sleep(3000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FC")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1354")

    label("loc_12FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131F")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1354")

    label("loc_131F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1342")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1354")

    label("loc_1342")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1354")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1377")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_13CF")

    label("loc_1377")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139A")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_13CF")

    label("loc_139A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BD")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_13CF")

    label("loc_13BD")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_13CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F2")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_144A")

    label("loc_13F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1415")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_144A")

    label("loc_1415")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1438")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_144A")

    label("loc_1438")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_144A")

    Jump("loc_1ABF")

    label("loc_144D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147E")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_14D6")

    label("loc_147E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A1")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_14D6")

    label("loc_14A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C4")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_14D6")

    label("loc_14C4")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_14D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F9")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1551")

    label("loc_14F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151C")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1551")

    label("loc_151C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153F")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1551")

    label("loc_153F")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1551")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1574")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_15CC")

    label("loc_1574")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1597")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_15CC")

    label("loc_1597")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15BA")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_15CC")

    label("loc_15BA")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_15CC")

    Jump("loc_1ABF")

    label("loc_15CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1751")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1600")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1658")

    label("loc_1600")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1623")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1658")

    label("loc_1623")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1646")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1658")

    label("loc_1646")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167B")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_16D3")

    label("loc_167B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169E")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_16D3")

    label("loc_169E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C1")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_16D3")

    label("loc_16C1")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_16D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F6")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_174E")

    label("loc_16F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1719")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_174E")

    label("loc_1719")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173C")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_174E")

    label("loc_173C")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_174E")

    Jump("loc_1ABF")

    label("loc_1751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1782")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_17DA")

    label("loc_1782")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A5")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_17DA")

    label("loc_17A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C8")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_17DA")

    label("loc_17C8")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_17DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FD")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1855")

    label("loc_17FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1820")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1855")

    label("loc_1820")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1843")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1855")

    label("loc_1843")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1855")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1878")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_18D0")

    label("loc_1878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189B")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_18D0")

    label("loc_189B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BE")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_18D0")

    label("loc_18BE")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_18D0")

    Jump("loc_1ABF")

    label("loc_18D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F6")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_194E")

    label("loc_18F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1919")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_194E")

    label("loc_1919")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_193C")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_194E")

    label("loc_193C")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_194E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1971")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_19C9")

    label("loc_1971")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1994")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_19C9")

    label("loc_1994")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B7")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_19C9")

    label("loc_19B7")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_19C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19EC")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A44")

    label("loc_19EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A0F")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A44")

    label("loc_1A0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A32")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A44")

    label("loc_1A32")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1A44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A67")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1ABF")

    label("loc_1A67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8A")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1ABF")

    label("loc_1A8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AAD")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1ABF")

    label("loc_1AAD")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1ABF")


    def lambda_1AC5():
        OP_8F(0xFE, 0x4E2, 0x0, 0x2616, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1AC5)
    Sleep(100)

    def lambda_1AE5():
        OP_8F(0xFE, 0xFFFFFBB4, 0x0, 0x254E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1AE5)
    Sleep(100)

    def lambda_1B05():
        OP_8F(0xFE, 0x280, 0x0, 0x2DF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1B05)
    Sleep(100)

    def lambda_1B25():
        OP_8F(0xFE, 0xFFFFFDC6, 0x0, 0x2DDC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1B25)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEF, 0x1)
    WaitChrThread(0xF0, 0x1)
    WaitChrThread(0xF1, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9C")

    ChrTalk(    #42
        0x101,
        "#1005F#5P唔……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCB")

    ChrTalk(    #43
        0x102,
        "#1502F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1BCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BF7")

    ChrTalk(    #44
        0x10B,
        "#216F#5P哇！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1BF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C25")

    ChrTalk(    #45
        0x107,
        "#065F#5P哇哇！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C54")

    ChrTalk(    #46
        0x10A,
        "#1317F#5P哇哇！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1C54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C83")

    ChrTalk(    #47
        0x105,
        "#1162F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1C83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB2")

    ChrTalk(    #48
        0x103,
        "#1533F#5P嘁……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1CB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE2")

    ChrTalk(    #49
        0x106,
        "#057F#5P可恶……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1CE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D10")

    ChrTalk(    #50
        0x108,
        "#072F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1D10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3E")

    ChrTalk(    #51
        0x10E,
        "#178F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1D3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D71")

    ChrTalk(    #52
        0x104,
        "#1546F#5P噢噢噢……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1D71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D9F")

    ChrTalk(    #53
        0x10D,
        "#270F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DCA")

    label("loc_1D9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DCA")

    ChrTalk(    #54
        0x10C,
        "#112F#5P唔……！\x02",
    )

    CloseMessageWindow()

    label("loc_1DCA")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E66")

    ChrTalk(    #55
        0x107,
        "#065F#5P金、金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_1E66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA9")

    ChrTalk(    #56
        0x101,
        "#1020F#5P金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_1EA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EED")

    ChrTalk(    #57
        0x106,
        "#057F#5P是金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_1EED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F30")

    ChrTalk(    #58
        0x103,
        "#1533F#5P金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_1F30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F73")

    ChrTalk(    #59
        0x105,
        "#1162F#5P金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_1F73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB5")

    ChrTalk(    #60
        0x10A,
        "#812F#5P金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_1FB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFB")

    ChrTalk(    #61
        0x10B,
        "#216F#5P金、金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_1FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_203F")

    ChrTalk(    #62
        0x108,
        "#072F#5P是金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_203F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2083")

    ChrTalk(    #63
        0x10E,
        "#172F#5P是金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_2083")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C6")

    ChrTalk(    #64
        0x104,
        "#1543F#5P金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_20C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210A")

    ChrTalk(    #65
        0x10D,
        "#271F#5P金色的『帕蒂尔·玛蒂尔』么！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_210A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_214B")

    ChrTalk(    #66
        0x10C,
        "#117F#5P是金色的『帕蒂尔·玛蒂尔』！？\x02",
    )

    CloseMessageWindow()

    label("loc_214B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2401")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_221F")

    ChrTalk(    #67
        0x110,
        (
            "#263F#5P『极限级零式』……\x02\x03",

            "#1306F十三工房开发的\x01",
            "可称得上是『帕蒂尔·玛蒂尔』\x01",
            "原型的机体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#1506F#5P说不定……\x01",
            "威力还更胜一筹！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2369")

    label("loc_221F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C4")

    ChrTalk(    #69
        0x110,
        (
            "#1306F#5P『极限级零式』……\x02\x03",

            "十三工房开发的\x01",
            "可称得上是『帕蒂尔·玛蒂尔』\x01",
            "原型的机体。\x02\x03",

            "#261F说不定……\x01",
            "力量还更胜一筹吧⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2369")

    label("loc_22C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2369")

    ChrTalk(    #70
        0x102,
        (
            "#1505F#5P『极限级零式』……\x02\x03",

            "十三工房开发的\x01",
            "可称得上是『帕蒂尔·玛蒂尔』\x01",
            "原型的机体……！\x02\x03",

            "#1506F说不定……\x01",
            "力量还更胜一筹！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2369")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_239F")

    ChrTalk(    #71
        0x101,
        "#1019F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    label("loc_239F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23CA")

    ChrTalk(    #72
        0x107,
        "#065F#5P哎——！\x02",
    )

    CloseMessageWindow()

    label("loc_23CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2401")

    ChrTalk(    #73
        0x106,
        "#055F#5P喂喂……开玩笑吧！？\x02",
    )

    CloseMessageWindow()

    label("loc_2401")

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
        "\x07\x05请选择行进的线路。\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_245C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_267E")
    OP_CC(0x0, 0x0, 0xFFFF, 0xAA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_END)), "loc_248D")
    OP_CC(0x1, 0x0, "右门的道路")
    OP_CC(0x3, 0x0, 0x0)
    Jump("loc_249B")

    label("loc_248D")

    OP_CC(0x1, 0x0, "右门的道路")

    label("loc_249B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_END)), "loc_24B7")
    OP_CC(0x1, 0x0, "左门的道路")
    OP_CC(0x3, 0x0, 0x1)
    Jump("loc_24C5")

    label("loc_24B7")

    OP_CC(0x1, 0x0, "左门的道路")

    label("loc_24C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_END)), "loc_24E1")
    OP_CC(0x1, 0x0, "正门的道路")
    OP_CC(0x3, 0x0, 0x2)
    Jump("loc_24EF")

    label("loc_24E1")

    OP_CC(0x1, 0x0, "正门的道路")

    label("loc_24EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_250F")
    OP_CC(0x1, 0x0, "大门的道路")
    Jump("loc_2521")

    label("loc_250F")

    OP_CC(0x1, 0x0, "大门的道路")
    OP_CC(0x3, 0x0, 0x3)

    label("loc_2521")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_254C"),
        (1, "loc_25A2"),
        (2, "loc_25F8"),
        (3, "loc_264E"),
        (SWITCH_DEFAULT, "loc_267B"),
    )


    label("loc_254C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A2")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_256E")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2586")

    label("loc_256E")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2586")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2586")

    label("loc_2586")

    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7409   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_267B")

    label("loc_25A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F8")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C4")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25DC")

    label("loc_25C4")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25DC")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25DC")

    label("loc_25DC")

    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7413   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_267B")

    label("loc_25F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264E")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_261A")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2632")

    label("loc_261A")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2632")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2632")

    label("loc_2632")

    OP_DC(0x0, 0x2)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7418   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_267B")

    label("loc_264E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_267B")
    OP_56(0x0)
    OP_DC(0x0, 0x3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7422   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_267B")

    label("loc_267B")

    Jump("loc_245C")

    label("loc_267E")

    Return()

    # Function_2_125 end

    def Function_3_267F(): pass

    label("Function_3_267F")

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

    def lambda_2793():
        OP_6D(4880, 250, 23700, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2793)

    def lambda_27AB():
        OP_67(0, 3200, -10000, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_27AB)

    def lambda_27C3():
        OP_6B(3620, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_27C3)

    def lambda_27D3():
        OP_6C(45000, 3500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_27D3)

    def lambda_27E3():
        OP_6E(425, 3500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_27E3)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #75 op#A
        (
            "\x07\x02#60W#55A碰巧，我的仆人们\x01",
            "也去迎接你们的同伴了……\x02",
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

    # Function_3_267F end

    def Function_4_2897(): pass

    label("Function_4_2897")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29E9")
    OP_DC(0x0, 0x3)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AB2")

    label("loc_29E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A4E")
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A12")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A4B")

    label("loc_2A12")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A30")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A4B")

    label("loc_2A30")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4B")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2A4B")

    Jump("loc_2AB2")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AB2")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A79")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AB2")

    label("loc_2A79")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A97")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AB2")

    label("loc_2A97")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB2")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2AB2")

    Return()

    # Function_4_2897 end

    SaveToFile()

Try(main)
