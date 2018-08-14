from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '幽灵',                                 # 9
        '幽灵',                                 # 10
        '',                                     # 11
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
        "Function_3_1F1A",         # 03, 3
        "Function_4_2148",         # 04, 4
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D7")

    ChrTalk(    #0
        0x101,
        (
            "#1004F#5P啊……\x01",
            "这里就是终点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_3D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419")

    ChrTalk(    #1
        0x102,
        (
            "#1503F#5P看上去……\x01",
            "像是终点的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_419")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_456")

    ChrTalk(    #2
        0x10B,
        (
            "#212F#5P这里……\x01",
            "好像是终点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_456")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496")

    ChrTalk(    #3
        0x110,
        (
            "#1305F#5P哎呀……\x01",
            "这里就是终点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_496")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D5")

    ChrTalk(    #4
        0x107,
        (
            "#065F#5P这里……\x01",
            "应该就是终点吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_4D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50F")

    ChrTalk(    #5
        0x10A,
        "#814F#5P咦……这里就是终点？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_50F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54B")

    ChrTalk(    #6
        0x105,
        (
            "#1164F#5P这里……\x01",
            "就是终点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_54B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_586")

    ChrTalk(    #7
        0x103,
        "#1523F#5P这里……就是终点吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_586")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C0")

    ChrTalk(    #8
        0x106,
        "#555F#5P这里就是终点吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_5C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FF")

    ChrTalk(    #9
        0x108,
        (
            "#072F#5P看来……\x01",
            "这里就是终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_5FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_637")

    ChrTalk(    #10
        0x10E,
        "#178F#5P这里……是终点吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_637")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677")

    ChrTalk(    #11
        0x104,
        (
            "#1542F#5P唔……\x01",
            "好像这里就是终点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B1")

    ChrTalk(    #12
        0x10D,
        "#276F#5P……看来像到终点了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EB")

    label("loc_6B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EB")

    ChrTalk(    #13
        0x10C,
        (
            "#112F#5P嗯……\x01",
            "这里就是终点吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(    #14
        0x101,
        (
            "#1015F#5P唔……\x01",
            "可是，什么东西都没有……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_779")

    ChrTalk(    #15
        0x102,
        (
            "#1503F#5P奇怪……\x01",
            "怎么什么气息也感觉不到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_779")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B8")

    ChrTalk(    #16
        0x10B,
        (
            "#212F#5P好像……\x01",
            "没有一个人在呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_7B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FC")

    ChrTalk(    #17
        0x110,
        (
            "#1305F#5P嗯？\x01",
            "怎么感觉不到任何气息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_7FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_838")

    ChrTalk(    #18
        0x107,
        "#063F#5P好像……什么也没有啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_838")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_875")

    ChrTalk(    #19
        0x10A,
        (
            "#812F#5P怎么……\x01",
            "空空荡荡的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_875")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B0")

    ChrTalk(    #20
        0x105,
        "#1163F#5P……好像什么也没有。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_8B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F2")

    ChrTalk(    #21
        0x103,
        (
            "#1532F#5P嗯……\x01",
            "可是好像什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_8F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_931")

    ChrTalk(    #22
        0x106,
        (
            "#552F#5P哼……\x01",
            "可是却什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_978")

    ChrTalk(    #23
        0x108,
        (
            "#572F#5P怎么回事……\x01",
            "一点气息也感觉不到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_978")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BD")

    ChrTalk(    #24
        0x10E,
        (
            "#178F#5P奇怪……\x01",
            "怎么会没有任何气息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_9BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FF")

    ChrTalk(    #25
        0x104,
        (
            "#1540F#5P哦……\x01",
            "这还真是一干二净啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_9FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A40")

    ChrTalk(    #26
        0x10D,
        (
            "#276F#5P奇怪……\x01",
            "竟然没有任何气息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7A")

    ChrTalk(    #27
        0x10C,
        (
            "#112F#5P怎么……\x01",
            "这里没有人吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7A")

    Sleep(500)
    OP_20(0x5DC)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #28 op#A op#5
        "\x07\x02#15A待机模式解除……\x05\x02",
    )

    Jump("loc_AC9")

    label("loc_AC9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B02")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B69")

    label("loc_B02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2A")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B69")

    label("loc_B2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B52")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B69")

    label("loc_B52")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B69")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B96")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BFD")

    label("loc_B96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBE")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BFD")

    label("loc_BBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE6")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BFD")

    label("loc_BE6")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BFD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2A")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C91")

    label("loc_C2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C52")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C91")

    label("loc_C52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7A")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C91")

    label("loc_C7A")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C91")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBE")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D25")

    label("loc_CBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE6")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D25")

    label("loc_CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0E")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D25")

    label("loc_D0E")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D25")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D67")

    ChrTalk(    #29
        0x101,
        "#1020F#6P刚、刚才的声音是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_D67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA2")

    ChrTalk(    #30
        0x102,
        "#1502F#6P刚才的声音是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_DA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD4")

    ChrTalk(    #31
        0x110,
        "#264F#6P合成音……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_DD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0A")

    ChrTalk(    #32
        0x10B,
        "#216F#6P那、那是什么！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_E0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E46")

    ChrTalk(    #33
        0x107,
        "#065F#6P机、机械的声音……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_E46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8E")

    ChrTalk(    #34
        0x10A,
        (
            "#1317F#6P金属一般的声音……\x01",
            "到底是什么！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_E8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC7")

    ChrTalk(    #35
        0x105,
        "#1163F#6P刚才的声音是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_EC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F00")

    ChrTalk(    #36
        0x103,
        "#1523F#6P这个声音是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_F00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F36")

    ChrTalk(    #37
        0x106,
        "#052F#6P刚才的是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_F36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F70")

    ChrTalk(    #38
        0x108,
        "#072F#6P刚才的声音是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_F70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA6")

    ChrTalk(    #39
        0x10E,
        "#172F#6P怎么回事……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_FA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDF")

    ChrTalk(    #40
        0x104,
        "#1543F#6P这个声音是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_FDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1013")

    ChrTalk(    #41
        0x10D,
        "#273F#6P怎么了……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1046")

    label("loc_1013")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1046")

    ChrTalk(    #42
        0x10C,
        "#113F#6P这个声音是……！\x02",
    )

    CloseMessageWindow()

    label("loc_1046")


    def lambda_104C():
        OP_6B(4000, 16000)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_104C)
    OP_1D(0x2D)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #43 op#A op#5
        "\x07\x02#15A系统重新启动……\x05\x02",
    )

    Jump("loc_10A2")

    label("loc_10A2")

    CloseMessageWindow()
    SetChrName("合成音")

    AnonymousTalk(    #44 op#A op#5
        "\x07\x02#15A重新启动完毕……\x05\x02",
    )

    Jump("loc_10D5")

    label("loc_10D5")

    CloseMessageWindow()
    SetChrName("合成音")

    AnonymousTalk(    #45 op#A op#5
        "\x07\x02#15A确认坐标……\x05\x02",
    )

    Jump("loc_1104")

    label("loc_1104")

    CloseMessageWindow()
    SetChrName("合成音")

    AnonymousTalk(    #46 op#A op#5
        (
            "\x07\x02#35A『幻影城』……\x01",
            "左翼区域最深处……\x05\x02",
        )
    )

    Jump("loc_1148")

    label("loc_1148")

    CloseMessageWindow()
    SetChrName("合成音")

    AnonymousTalk(    #47 op#A op#5
        "\x07\x02#30A确认到区域内的入侵者……\x05\x02",
    )

    Jump("loc_1183")

    label("loc_1183")

    CloseMessageWindow()
    SetChrName("合成音")

    AnonymousTalk(    #48 op#A op#5
        "\x07\x02#30A即将进行实体化……\x05\x02",
    )

    Jump("loc_11B8")

    label("loc_11B8")

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

    def lambda_122A():
        OP_6D(3440, 1050, 27500, 5500)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_122A)

    def lambda_1242():
        OP_67(0, 5000, -10000, 5500)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_1242)

    def lambda_125A():
        OP_6B(3200, 5500)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_125A)

    def lambda_126A():
        OP_6C(45000, 5500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_126A)

    def lambda_127A():
        OP_6E(500, 5500)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_127A)
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

    def lambda_1368():
        OP_67(0, 4500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_1368)

    def lambda_1380():
        OP_6B(3200, 8000)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1380)

    def lambda_1390():
        OP_6E(360, 8000)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1390)
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

    def lambda_142B():
        OP_6D(0, 1000, 31750, 2000)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_142B)

    def lambda_1443():
        OP_67(0, 2000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_1443)

    def lambda_145B():
        OP_6B(2630, 2000)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_145B)

    def lambda_146B():
        OP_6E(480, 2000)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_146B)
    OP_B0(0x6, 0x23)
    OP_6F(0x6, 640)
    OP_70(0x6, 0x2A8)
    OP_73(0x6)
    Fade(200)

    def lambda_1495():
        OP_6E(395, 200)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1495)
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

    def lambda_1585():
        OP_6D(0, 300, 32049, 3000)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_1585)

    def lambda_159D():
        OP_67(0, 1460, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_159D)

    def lambda_15B5():
        OP_6B(5700, 3000)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_15B5)

    def lambda_15C5():
        OP_6E(310, 3000)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_15C5)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1635")

    ChrTalk(    #49
        0x101,
        "#1005F#5P唔……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_1635")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1664")

    ChrTalk(    #50
        0x102,
        "#1502F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_1664")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1694")

    ChrTalk(    #51
        0x110,
        "#265F#5P哇啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_1694")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C0")

    ChrTalk(    #52
        0x10B,
        "#216F#5P哇！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_16C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16EE")

    ChrTalk(    #53
        0x107,
        "#065F#5P哇哇！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_16EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171D")

    ChrTalk(    #54
        0x10A,
        "#1317F#5P哇哇！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_171D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174C")

    ChrTalk(    #55
        0x105,
        "#1162F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_174C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177B")

    ChrTalk(    #56
        0x103,
        "#1533F#5P嘁……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_177B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AB")

    ChrTalk(    #57
        0x106,
        "#057F#5P可恶……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_17AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D9")

    ChrTalk(    #58
        0x108,
        "#072F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_17D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1807")

    ChrTalk(    #59
        0x10E,
        "#178F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_1807")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183A")

    ChrTalk(    #60
        0x104,
        "#1546F#5P噢噢噢……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_183A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1868")

    ChrTalk(    #61
        0x10D,
        "#270F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_1868")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1893")

    ChrTalk(    #62
        0x10C,
        "#112F#5P唔……！\x02",
    )

    CloseMessageWindow()

    label("loc_1893")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B6")
    OP_62(0xF2, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_190E")

    label("loc_18B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D9")
    OP_62(0xF2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_190E")

    label("loc_18D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FC")
    OP_62(0xF2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_190E")

    label("loc_18FC")

    OP_62(0xF2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_190E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1931")
    OP_62(0xF3, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1989")

    label("loc_1931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1954")
    OP_62(0xF3, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1989")

    label("loc_1954")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1977")
    OP_62(0xF3, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1989")

    label("loc_1977")

    OP_62(0xF3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1989")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AC")
    OP_62(0xF4, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A04")

    label("loc_19AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CF")
    OP_62(0xF4, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A04")

    label("loc_19CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F2")
    OP_62(0xF4, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A04")

    label("loc_19F2")

    OP_62(0xF4, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1A04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A27")
    OP_62(0xF5, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A7F")

    label("loc_1A27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A4A")
    OP_62(0xF5, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A7F")

    label("loc_1A4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6D")
    OP_62(0xF5, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A7F")

    label("loc_1A6D")

    OP_62(0xF5, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1A7F")


    def lambda_1A85():
        OP_8F(0xFE, 0x4E2, 0x0, 0x2616, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1A85)
    Sleep(100)

    def lambda_1AA5():
        OP_8F(0xFE, 0xFFFFFBB4, 0x0, 0x254E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1AA5)
    Sleep(100)

    def lambda_1AC5():
        OP_8F(0xFE, 0x280, 0x0, 0x2DF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF3, 0, lambda_1AC5)
    Sleep(100)

    def lambda_1AE5():
        OP_8F(0xFE, 0xFFFFFDC6, 0x0, 0x2DDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF2, 0, lambda_1AE5)
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

    def lambda_1B6F():
        OP_6B(5200, 9000)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1B6F)
    SetMessageWindowPos(-1, 200, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #63 op#A op#5
        "\x07\x02#20A模式：完全歼灭……\x05\x02",
    )

    Jump("loc_1BB6")

    label("loc_1BB6")

    CloseMessageWindow()
    Sleep(500)

    AnonymousTalk(    #64 op#A op#5
        (
            "\x07\x02#25A幻想乐曲Ⅱ\x01",
            "『幽灵』……\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    AnonymousTalk(    #65 op#A op#5
        "\x07\x02#33A现在开始歼灭行动……\x05\x02",
    )

    OP_22(0x85, 0x1, 0x64)

    def lambda_1C1A():

        label("loc_1C1A")

        OP_7C(0x0, 0x96, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1C1A")

    QueueWorkItem2(0xF2, 3, lambda_1C1A)
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
        "\x07\x05请选择行进的线路。\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F19")
    OP_CC(0x0, 0x0, 0xFFFF, 0xAA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_END)), "loc_1D28")
    OP_CC(0x1, 0x0, "右门的道路")
    OP_CC(0x3, 0x0, 0x0)
    Jump("loc_1D36")

    label("loc_1D28")

    OP_CC(0x1, 0x0, "右门的道路")

    label("loc_1D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_END)), "loc_1D52")
    OP_CC(0x1, 0x0, "左门的道路")
    OP_CC(0x3, 0x0, 0x1)
    Jump("loc_1D60")

    label("loc_1D52")

    OP_CC(0x1, 0x0, "左门的道路")

    label("loc_1D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_END)), "loc_1D7C")
    OP_CC(0x1, 0x0, "正门的道路")
    OP_CC(0x3, 0x0, 0x2)
    Jump("loc_1D8A")

    label("loc_1D7C")

    OP_CC(0x1, 0x0, "正门的道路")

    label("loc_1D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DAA")
    OP_CC(0x1, 0x0, "大门的道路")
    Jump("loc_1DBC")

    label("loc_1DAA")

    OP_CC(0x1, 0x0, "大门的道路")
    OP_CC(0x3, 0x0, 0x3)

    label("loc_1DBC")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DE7"),
        (1, "loc_1E3D"),
        (2, "loc_1E93"),
        (3, "loc_1EE9"),
        (SWITCH_DEFAULT, "loc_1F16"),
    )


    label("loc_1DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3D")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E09")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E21")

    label("loc_1E09")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E21")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E21")

    label("loc_1E21")

    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7409   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F16")

    label("loc_1E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E93")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E5F")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E77")

    label("loc_1E5F")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E77")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E77")

    label("loc_1E77")

    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7413   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F16")

    label("loc_1E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE9")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB5")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1ECD")

    label("loc_1EB5")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ECD")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1ECD")

    label("loc_1ECD")

    OP_DC(0x0, 0x2)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7418   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F16")

    label("loc_1EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F16")
    OP_56(0x0)
    OP_DC(0x0, 0x3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7422   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F16")

    label("loc_1F16")

    Jump("loc_1CF7")

    label("loc_1F19")

    Return()

    # Function_2_14B end

    def Function_3_1F1A(): pass

    label("Function_3_1F1A")

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

    def lambda_2040():
        OP_6D(-1590, 1000, 20570, 3500)
        ExitThread()

    QueueWorkItem(0xF2, 0, lambda_2040)

    def lambda_2058():
        OP_67(0, 3990, -10000, 3500)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_2058)

    def lambda_2070():
        OP_6B(3300, 3500)
        ExitThread()

    QueueWorkItem(0xF2, 2, lambda_2070)

    def lambda_2080():
        OP_6C(315000, 3500)
        ExitThread()

    QueueWorkItem(0xF2, 3, lambda_2080)

    def lambda_2090():
        OP_6E(450, 3500)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_2090)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF2, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #67 op#A
        (
            "\x07\x02#60W#60A若不能将它们全部打倒，\x01",
            "你们就没有明天可言……\x02",
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

    # Function_3_1F1A end

    def Function_4_2148(): pass

    label("Function_4_2148")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_229A")
    OP_DC(0x0, 0x3)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2363")

    label("loc_229A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22FF")
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C3")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_22FC")

    label("loc_22C3")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E1")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_22FC")

    label("loc_22E1")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22FC")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22FC")

    Jump("loc_2363")

    label("loc_22FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2363")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_232A")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2363")

    label("loc_232A")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2348")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2363")

    label("loc_2348")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2363")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2363")

    Return()

    # Function_4_2148 end

    SaveToFile()

Try(main)
