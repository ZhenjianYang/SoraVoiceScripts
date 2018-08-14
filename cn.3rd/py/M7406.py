from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7406   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7406.x',
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
        'Ｒ-巨兽',                              # 9
        '',                                     # 10
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
        "Function_3_2191",         # 03, 3
        "Function_4_21AD",         # 04, 4
        "Function_5_2222",         # 05, 5
        "Function_6_2444",         # 06, 6
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_E0")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_11D")

    label("loc_E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_FF")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_11D")

    label("loc_FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_11D")

    Return()

    # Function_0_CA end

    def Function_1_11E(): pass

    label("Function_1_11E")

    OP_71(0x408, 0x0)
    ExitThread()
    Return()

    # Function_1_11E end

    def Function_2_125(): pass

    label("Function_2_125")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(246, 0x40, 0x2)
    OP_E0(246, 0x41, 0x3)
    OP_E0(247, 0x42, 0x2)
    OP_E0(247, 0x43, 0x3)
    OP_E0(248, 0x44, 0x2)
    OP_E0(248, 0x45, 0x3)
    OP_E0(249, 0x46, 0x2)
    OP_E0(249, 0x47, 0x3)
    SetChrPos(0xF6, -840, 0, -10480, 0)
    SetChrPos(0xF7, 550, 0, -10450, 0)
    SetChrPos(0xF8, -1260, 0, -12070, 0)
    SetChrPos(0xF9, 610, 0, -12180, 0)
    OP_6D(5130, -28700, 26260, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(7270, 0)
    OP_6C(45000, 0)
    OP_6E(672, 0)

    def lambda_1E0():
        OP_6D(5130, -100, 26260, 8000)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_1E0)

    def lambda_1F8():
        OP_67(0, 6470, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1F8)

    def lambda_210():
        OP_8E(0xFE, 0xFFFFFB5A, 0x0, 0x2F9E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF6, 0, lambda_210)
    Sleep(100)

    def lambda_230():
        OP_8E(0xFE, 0x212, 0x0, 0x2FBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_230)
    Sleep(100)

    def lambda_250():
        OP_8E(0xFE, 0xFFFFF948, 0x0, 0x2882, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_250)
    Sleep(100)

    def lambda_270():
        OP_8E(0xFE, 0x1EA, 0x0, 0x2850, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_270)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xF6, 0x1)
    WaitChrThread(0xF7, 0x1)

    def lambda_29F():
        OP_6B(7500, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_29F)

    def lambda_2AF():
        OP_6E(700, 3000)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2AF)
    WaitChrThread(0xF6, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Fade(1000)
    OP_6D(1100, 0, 12850, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")

    ChrTalk(    #0
        0x101,
        (
            "#1015F#5P好像来到了一个\x01",
            "相当宽敞的地方……\x02\x03",

            "这里就是终点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4")

    ChrTalk(    #1
        0x102,
        (
            "#1505F#5P看来这里就是终点了呢。\x02\x03",

            "#1503F可是，这里还真宽敞啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_3E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E")

    ChrTalk(    #2
        0x10B,
        (
            "#210F#5P嘿……\x01",
            "真是个宽敞的地方呢。\x02\x03",

            "这里就是终点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_43E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F")

    ChrTalk(    #3
        0x110,
        (
            "#261F#5P嘻嘻，看来这里是终点呢。\x02\x03",

            "#265F不过好像\x01",
            "空空荡荡的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_49F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_500")

    ChrTalk(    #4
        0x107,
        (
            "#560F#5P好、好像是终点呢。\x02\x03",

            "不过，\x01",
            "怎么这么宽敞……\x02",
        )
    )

    Jump("loc_4FC")

    label("loc_4FC")

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_500")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55C")

    ChrTalk(    #5
        0x10A,
        (
            "#818F#5P来到了一个\x01",
            "相当宽敞的地方……\x02\x03",

            "这里会是终点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_55C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB")

    ChrTalk(    #6
        0x105,
        (
            "#1163F#5P来到了一个\x01",
            "相当宽敞的地方呢……\x02\x03",

            "这里就是终点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_5BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_624")

    ChrTalk(    #7
        0x103,
        (
            "#1523F#5P唔……\x01",
            "来到了一个相当宽敞的地方呢。\x02\x03",

            "#1522F这里就是终点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_624")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686")

    ChrTalk(    #8
        0x106,
        (
            "#555F#5P好像突然就来到了\x01",
            "一个宽敞的地方啊。\x02\x03",

            "这里就是终点吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E7")

    ChrTalk(    #9
        0x108,
        (
            "#074F#5P这就是终点吗。\x02\x03",

            "#070F话说回来……\x01",
            "这儿还真是宽敞啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_6E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_748")

    ChrTalk(    #10
        0x10E,
        (
            "#176F#5P来到了一个\x01",
            "相当宽敞的地方……\x02\x03",

            "#178F这里就是终点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_748")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B5")

    ChrTalk(    #11
        0x104,
        (
            "#1545F#5P看来这里就是终点了。\x02\x03",

            "#1540F不过……\x01",
            "这么宽敞还真是出乎意料啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_7B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824")

    ChrTalk(    #12
        0x10D,
        (
            "#272F#5P好像来到了一个\x01",
            "相当宽敞的地方……\x02\x03",

            "#277F不过，看来这里就是终点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_888")

    label("loc_824")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_888")

    ChrTalk(    #13
        0x10C,
        (
            "#119F#5P看来这里就是终点了吧。\x02\x03",

            "#110F不过……\x01",
            "真是个宽敞的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_888")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D6")

    ChrTalk(    #14
        0x101,
        (
            "#1016F#5P呵呵，\x01",
            "在这么宽敞的地方真想大喊一声啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_8D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91E")

    ChrTalk(    #15
        0x102,
        (
            "#1503F#5P（这么宽敞……\x01",
            "  到底是为什么？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_91E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96F")

    ChrTalk(    #16
        0x10B,
        (
            "#210F#5P嘿，在这么宽敞的地方\x01",
            "想干什么就能干什么啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_96F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B8")

    ChrTalk(    #17
        0x110,
        (
            "#267F#5P（这么宽敞……\x01",
            "  到底是为什么呢？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_9B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0B")

    ChrTalk(    #18
        0x107,
        (
            "#062F#5P（为、为什么会\x01",
            "  弄出这么宽敞的地方呢……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_A0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A56")

    ChrTalk(    #19
        0x10A,
        (
            "#819F#5P唔，\x01",
            "在这么宽敞的地方真想飞奔起来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_A56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA2")

    ChrTalk(    #20
        0x105,
        (
            "#1162F#5P（这么宽敞……\x01",
            "  到底是为什么……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_AA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF2")

    ChrTalk(    #21
        0x103,
        (
            "#1522F#5P（唔……\x01",
            "  这么宽敞的地方，让人在意啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_AF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3F")

    ChrTalk(    #22
        0x106,
        (
            "#552F#5P（真奇怪……\x01",
            "  这么宽敞到底是为什么？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B86")

    ChrTalk(    #23
        0x108,
        (
            "#072F#5P（唔……\x01",
            "  为什么会这么宽敞呢？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_B86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCD")

    ChrTalk(    #24
        0x10E,
        (
            "#178F#5P（这么宽敞……\x01",
            "  到底是为什么？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_BCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C19")

    ChrTalk(    #25
        0x104,
        (
            "#1542F#5P（唔……\x01",
            "  这么宽敞到底是为什么呢？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_C19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C60")

    ChrTalk(    #26
        0x10D,
        (
            "#276F#5P（这么宽敞……\x01",
            "  到底是为什么？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_C60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA")

    ChrTalk(    #27
        0x10C,
        (
            "#112F#5P（这么宽敞……\x01",
            "  应该有什么原因才对。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAA")

    Sleep(300)
    OP_20(0x7D0)
    OP_22(0x11F, 0x0, 0x50)

    def lambda_CBF():
        OP_7C(0x5, 0x5, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF6, 3, lambda_CBF)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFE")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D65")

    label("loc_CFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D26")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D65")

    label("loc_D26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4E")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D65")

    label("loc_D4E")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D65")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D92")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DF9")

    label("loc_D92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBA")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DF9")

    label("loc_DBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE2")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DF9")

    label("loc_DE2")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_DF9")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E26")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E8D")

    label("loc_E26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4E")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E8D")

    label("loc_E4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E76")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E8D")

    label("loc_E76")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E8D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBA")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F21")

    label("loc_EBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE2")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F21")

    label("loc_EE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0A")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F21")

    label("loc_F0A")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F21")

    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0x3)
    Sleep(650)
    OP_B0(0x8, 0xF)
    OP_6F(0x8, 500)
    OP_70(0x8, 0x208)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F81")

    ChrTalk(    #28
        0x101,
        "#1020F#6P刚、刚才的叫声是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_F81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBC")

    ChrTalk(    #29
        0x102,
        "#1506F#6P刚才的咆哮是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_FBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1002")

    ChrTalk(    #30
        0x110,
        (
            "#1306F#6P哎呀……\x01",
            "似乎不是普通的魔兽呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_1002")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1038")

    ChrTalk(    #31
        0x10B,
        "#216F#6P刚、刚才的是！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_1038")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1070")

    ChrTalk(    #32
        0x107,
        "#065F#6P难、难不成……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_1070")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AF")

    ChrTalk(    #33
        0x10A,
        "#1317F#6P是、是魔兽的叫声……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_10AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E8")

    ChrTalk(    #34
        0x105,
        "#1162F#6P刚才的咆哮是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_10E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1121")

    ChrTalk(    #35
        0x103,
        "#1523F#6P刚才的叫声是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_1121")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1164")

    ChrTalk(    #36
        0x106,
        (
            "#055F#6P喂！？\x01",
            "刚才那个难不成是……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_1164")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119E")

    ChrTalk(    #37
        0x108,
        "#072F#6P刚才的……难道是！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_119E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DA")

    ChrTalk(    #38
        0x10E,
        "#173F#6P难不成刚才那是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_11DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1220")

    ChrTalk(    #39
        0x104,
        (
            "#1544F#6P这是……\x01",
            "我有种很糟糕的预感呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_1220")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125C")

    ChrTalk(    #40
        0x10D,
        "#273F#6P怎么了……刚才那是！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_129A")

    label("loc_125C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129A")

    ChrTalk(    #41
        0x10C,
        (
            "#112F#6P这个……\x01",
            "不是普通的魔兽啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_129A")

    Sleep(300)
    OP_1D(0x9A)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_82(0x83, 0x0)
    OP_82(0x85, 0x0)
    OP_6D(-4019, 20000, 30250, 0)
    OP_67(0, 10600, -10000, 0)
    OP_6B(9630, 0)
    OP_6C(134000, 0)
    OP_6E(200, 0)

    def lambda_1310():
        OP_6D(1680, 1600, 24890, 10000)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_1310)

    def lambda_1328():
        OP_67(0, 4030, -10000, 10000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1328)

    def lambda_1340():
        OP_6B(9180, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1340)

    def lambda_1350():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_1350)

    def lambda_1360():
        OP_6E(186, 10000)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1360)
    SetChrPos(0x10, 0, 30000, 30000, 180)
    OP_A1(0x10, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()

    def lambda_138C():
        OP_8F(0xFE, 0xFFFFF448, 0x1B58, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_138C)
    Sleep(2000)

    def lambda_13AC():
        OP_8F(0xFE, 0x7D0, 0x1B58, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13AC)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_72(0x2008, 0x0)
    ExitThread()
    OP_D8(0x8, 0x3E8)
    OP_6F(0x8, 520)
    OP_70(0x8, 0x212)

    def lambda_13E8():
        OP_8C(0xFE, 200, 100)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_13E8)

    def lambda_13F6():
        OP_8F(0xFE, 0x1388, 0x0, 0x7530, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13F6)
    WaitChrThread(0x10, 0x1)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0x1388, 0x5DC)
    OP_73(0x8)
    OP_6F(0x8, 530)
    OP_70(0x8, 0x230)
    OP_73(0x8)
    OP_71(0x2008, 0x0)
    ExitThread()
    OP_6F(0x8, 5)
    OP_70(0x8, 0x37)
    WaitChrThread(0xF6, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Fade(500)
    OP_6D(0, 1600, 27240, 0)
    OP_67(0, 1830, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(357000, 0)
    OP_6E(260, 0)

    def lambda_14AD():
        OP_6B(6350, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_14AD)
    OP_72(0x414, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x10, 7000, 0, 30000, 205)
    SetChrPos(0xF6, -570, 0, 12740, 0)
    SetChrPos(0xF7, 640, 0, 12760, 0)
    SetChrPos(0xF8, -900, 0, 10550, 0)
    SetChrPos(0xF9, 1450, 0, 10750, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B9")

    ChrTalk(    #42
        0x101,
        "#1005F#5P唔……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_15B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E8")

    ChrTalk(    #43
        0x102,
        "#1502F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_15E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1618")

    ChrTalk(    #44
        0x110,
        "#264F#5P哇啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_1618")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1644")

    ChrTalk(    #45
        0x10B,
        "#216F#5P哇！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_1644")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1672")

    ChrTalk(    #46
        0x107,
        "#065F#5P哇哇！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_1672")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A1")

    ChrTalk(    #47
        0x10A,
        "#1317F#5P哇哇！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_16A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D0")

    ChrTalk(    #48
        0x105,
        "#1162F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_16D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16FF")

    ChrTalk(    #49
        0x103,
        "#1533F#5P嘁……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_16FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172F")

    ChrTalk(    #50
        0x106,
        "#057F#5P可恶……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_172F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175D")

    ChrTalk(    #51
        0x108,
        "#072F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_175D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178B")

    ChrTalk(    #52
        0x10E,
        "#178F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_178B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17BE")

    ChrTalk(    #53
        0x104,
        "#1546F#5P噢噢噢……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_17BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17EC")

    ChrTalk(    #54
        0x10D,
        "#270F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_17EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1817")

    ChrTalk(    #55
        0x10C,
        "#112F#5P唔……！\x02",
    )

    CloseMessageWindow()

    label("loc_1817")

    WaitChrThread(0xF8, 0x1)
    OP_43(0x10, 0x0, 0x0, 0x4)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184B")
    OP_62(0xF6, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_18A3")

    label("loc_184B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186E")
    OP_62(0xF6, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_18A3")

    label("loc_186E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF6)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1891")
    OP_62(0xF6, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_18A3")

    label("loc_1891")

    OP_62(0xF6, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_18A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C6")
    OP_62(0xF7, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_191E")

    label("loc_18C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E9")
    OP_62(0xF7, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_191E")

    label("loc_18E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF7)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190C")
    OP_62(0xF7, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_191E")

    label("loc_190C")

    OP_62(0xF7, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_191E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1941")
    OP_62(0xF8, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1999")

    label("loc_1941")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1964")
    OP_62(0xF8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1999")

    label("loc_1964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1987")
    OP_62(0xF8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1999")

    label("loc_1987")

    OP_62(0xF8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1999")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BC")
    OP_62(0xF9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A14")

    label("loc_19BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DF")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A14")

    label("loc_19DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A02")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_1A14")

    label("loc_1A02")

    OP_62(0xF9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_1A14")


    def lambda_1A1A():
        OP_8F(0xFE, 0x5AA, 0x0, 0x2616, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1A1A)
    Sleep(100)

    def lambda_1A3A():
        OP_8F(0xFE, 0xFFFFFC7C, 0x0, 0x254E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_1A3A)
    Sleep(100)

    def lambda_1A5A():
        OP_8F(0xFE, 0x280, 0x0, 0x2DF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1A5A)
    Sleep(100)

    def lambda_1A7A():
        OP_8F(0xFE, 0xFFFFFDC6, 0x0, 0x2DDC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF6, 0, lambda_1A7A)
    WaitChrThread(0xF6, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF6, 0)
    SetChrSubChip(0xF6, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF7, 2)
    SetChrSubChip(0xF7, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF8, 4)
    SetChrSubChip(0xF8, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF9, 6)
    SetChrSubChip(0xF9, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x10, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3F")

    ChrTalk(    #56
        0x106,
        "#057F#5P红色的……雷格纳特！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7C")

    ChrTalk(    #57
        0x101,
        "#1020F#5P红、红色的雷格纳特！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1B7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB6")

    ChrTalk(    #58
        0x107,
        "#065F#5P雷、雷格纳特先生！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1BB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BF3")

    ChrTalk(    #59
        0x103,
        "#1533F#5P红色的……雷格纳特！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1BF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C2E")

    ChrTalk(    #60
        0x105,
        "#1163F#5P雷格纳特先生……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C68")

    ChrTalk(    #61
        0x10B,
        "#216F#5P那、那个时候的龙！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1C68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA4")

    ChrTalk(    #62
        0x108,
        "#072F#5P红色的……雷格纳特！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1CA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CDE")

    ChrTalk(    #63
        0x10E,
        "#172F#5P雷、雷格纳特大人！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D1B")

    ChrTalk(    #64
        0x104,
        "#1549F#5P红色的……雷格纳特！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1D1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D59")

    ChrTalk(    #65
        0x10D,
        "#271F#5P那个时候的古代龙……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1D59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D9A")

    ChrTalk(    #66
        0x10A,
        "#1317F#5P难、难不成是……古代龙！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1D9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD1")

    ChrTalk(    #67
        0x10C,
        "#114F#5P那是……古代龙吗！？\x02",
    )

    CloseMessageWindow()

    label("loc_1DD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E55")

    ChrTalk(    #68
        0x110,
        (
            "#265F#5P哇，这是古代龙……！\x02\x03",

            "#261F而且似乎还是像『黑色方舟』一样\x01",
            "经过变化的形态呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC6")

    label("loc_1E55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EC6")

    ChrTalk(    #69
        0x110,
        (
            "#265F#5P哇，这是古代龙……！\x02\x03",

            "#261F我还是第一次看到，\x01",
            "实在是厉害呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F13")

    ChrTalk(    #70
        0x102,
        (
            "#1506F#5P和『黑色方舟』一样\x01",
            "经过变化的形态吗……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F13")

    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2C25)
    OP_E6(0x0, 0x2)
    OP_1D(0xE1)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #71
        "\x07\x05请选择行进的线路。\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2190")
    OP_CC(0x0, 0x0, 0xFFFF, 0xAA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_END)), "loc_1F9F")
    OP_CC(0x1, 0x0, "右门的道路")
    OP_CC(0x3, 0x0, 0x0)
    Jump("loc_1FAD")

    label("loc_1F9F")

    OP_CC(0x1, 0x0, "右门的道路")

    label("loc_1FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_END)), "loc_1FC9")
    OP_CC(0x1, 0x0, "左门的道路")
    OP_CC(0x3, 0x0, 0x1)
    Jump("loc_1FD7")

    label("loc_1FC9")

    OP_CC(0x1, 0x0, "左门的道路")

    label("loc_1FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_END)), "loc_1FF3")
    OP_CC(0x1, 0x0, "正门的道路")
    OP_CC(0x3, 0x0, 0x2)
    Jump("loc_2001")

    label("loc_1FF3")

    OP_CC(0x1, 0x0, "正门的道路")

    label("loc_2001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2021")
    OP_CC(0x1, 0x0, "大门的道路")
    Jump("loc_2033")

    label("loc_2021")

    OP_CC(0x1, 0x0, "大门的道路")
    OP_CC(0x3, 0x0, 0x3)

    label("loc_2033")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_205E"),
        (1, "loc_20B4"),
        (2, "loc_210A"),
        (3, "loc_2160"),
        (SWITCH_DEFAULT, "loc_218D"),
    )


    label("loc_205E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B4")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2080")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2098")

    label("loc_2080")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2098")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2098")

    label("loc_2098")

    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7409   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_218D")

    label("loc_20B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210A")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D6")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20EE")

    label("loc_20D6")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20EE")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20EE")

    label("loc_20EE")

    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7413   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_218D")

    label("loc_210A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2160")
    OP_56(0x0)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_212C")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2144")

    label("loc_212C")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2144")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2144")

    label("loc_2144")

    OP_DC(0x0, 0x2)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7418   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_218D")

    label("loc_2160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_218D")
    OP_56(0x0)
    OP_DC(0x0, 0x3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7422   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_218D")

    label("loc_218D")

    Jump("loc_1F6E")

    label("loc_2190")

    Return()

    # Function_2_125 end

    def Function_3_2191(): pass

    label("Function_3_2191")

    Sleep(400)

    label("loc_2196")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21AC")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("loc_2196")

    label("loc_21AC")

    Return()

    # Function_3_2191 end

    def Function_4_21AD(): pass

    label("Function_4_21AD")

    Fade(500)
    OP_72(0x2008, 0x0)
    ExitThread()
    OP_D8(0x8, 0x3E8)
    OP_6F(0x8, 80)
    OP_70(0x8, 0x78)
    Sleep(1300)

    def lambda_21D5():
        OP_6B(6900, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_21D5)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x258)
    OP_7C(0x12C, 0x12C, 0x1388, 0x258)
    OP_73(0x8)
    OP_D8(0x8, 0x3E8)
    OP_71(0x2008, 0x0)
    ExitThread()
    OP_6F(0x8, 5)
    OP_70(0x8, 0x37)
    Return()

    # Function_4_21AD end

    def Function_5_2222(): pass

    label("Function_5_2222")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(246, 0x40, 0x2)
    OP_E0(246, 0x41, 0x3)
    OP_E0(247, 0x42, 0x2)
    OP_E0(247, 0x43, 0x3)
    OP_E0(248, 0x44, 0x2)
    OP_E0(248, 0x45, 0x3)
    OP_E0(249, 0x46, 0x2)
    OP_E0(249, 0x47, 0x3)
    SetChrPos(0xF6, -570, 0, 12740, 0)
    SetChrPos(0xF7, 640, 0, 12760, 0)
    SetChrPos(0xF8, -1100, 0, 10550, 0)
    SetChrPos(0xF9, 1250, 0, 10750, 0)
    SetChrChipByIndex(0xF6, 0)
    SetChrSubChip(0xF6, 0)
    SetChrChipByIndex(0xF7, 2)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 4)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 6)
    SetChrSubChip(0xF9, 0)
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    SetChrPos(0x10, 7000, 0, 30000, 205)
    OP_A1(0x10, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()
    OP_B0(0x8, 0xF)
    OP_6F(0x8, 5)
    OP_70(0x8, 0x37)
    OP_6D(0, 1600, 30240, 0)
    OP_67(0, 2600, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(20000, 0)
    OP_6E(256, 0)

    def lambda_233F():
        OP_6D(0, 1600, 27240, 3500)
        ExitThread()

    QueueWorkItem(0xF6, 0, lambda_233F)

    def lambda_2357():
        OP_67(0, 1830, -10000, 3500)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_2357)

    def lambda_236F():
        OP_6B(5800, 3500)
        ExitThread()

    QueueWorkItem(0xF6, 2, lambda_236F)

    def lambda_237F():
        OP_6C(357000, 3500)
        ExitThread()

    QueueWorkItem(0xF6, 3, lambda_237F)

    def lambda_238F():
        OP_6E(260, 3500)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_238F)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF6, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #72 op#A
        (
            "\x07\x02#60W#60A只能迎来被吞没的命运，\x01",
            "化为『影之国』的食粮……\x02",
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
    OP_DC(0x0, 0x3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2222 end

    def Function_6_2444(): pass

    label("Function_6_2444")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(246, 0x40, 0x2)
    OP_E0(246, 0x41, 0x3)
    OP_E0(247, 0x42, 0x2)
    OP_E0(247, 0x43, 0x3)
    OP_E0(248, 0x44, 0x2)
    OP_E0(248, 0x45, 0x3)
    OP_E0(249, 0x46, 0x2)
    OP_E0(249, 0x47, 0x3)
    SetChrPos(0xF6, -570, 0, 12740, 0)
    SetChrPos(0xF7, 640, 0, 12760, 0)
    SetChrPos(0xF8, -1100, 0, 10550, 0)
    SetChrPos(0xF9, 1250, 0, 10750, 0)
    SetChrChipByIndex(0xF6, 0)
    SetChrSubChip(0xF6, 0)
    SetChrChipByIndex(0xF7, 2)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 4)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 6)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x10, 0, 0, 30000, 180)
    OP_A1(0x10, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()
    OP_B0(0x8, 0xF)
    OP_6F(0x8, 5)
    OP_70(0x8, 0x37)
    OP_6D(0, 1600, 27240, 0)
    OP_67(0, 2410, -10000, 0)
    OP_6B(7000, 0)
    OP_6C(0, 0)
    OP_6E(260, 0)
    FadeToBright(500, 0)
    OP_0D()
    Battle(0x336, 0x0, 0x0, 0x0, 0xFF)
    OP_A2(0x2C2C)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2596")
    OP_DC(0x0, 0x3)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_265F")

    label("loc_2596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25FB")
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25BF")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_25F8")

    label("loc_25BF")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25DD")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_25F8")

    label("loc_25DD")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F8")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_25F8")

    Jump("loc_265F")

    label("loc_25FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_265F")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2626")
    OP_DC(0x0, 0x0)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_265F")

    label("loc_2626")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2644")
    OP_DC(0x0, 0x1)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_265F")

    label("loc_2644")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_265F")
    OP_DC(0x0, 0x2)
    OP_A2(0x2507)
    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_265F")

    Return()

    # Function_6_2444 end

    SaveToFile()

Try(main)
