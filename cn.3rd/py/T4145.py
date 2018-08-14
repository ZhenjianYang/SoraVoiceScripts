from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4145   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4145.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '艾莉卡博士',                           # 9
        '希德中校',                             # 10
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


    AddCharChip(
        'ED6_DT27/CH03970 ._CH',             # 00
        'ED6_DT27/CH03590 ._CH',             # 01
        'ED6_DT26/CH20373 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03970P._CP',             # 00
        'ED6_DT27/CH03590P._CP',             # 01
        'ED6_DT26/CH20373P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_134",          # 01, 1
        "Function_2_135",          # 02, 2
        "Function_3_A73",          # 03, 3
        "Function_4_BF0",          # 04, 4
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_120")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_133")

    label("loc_120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_133")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_133")

    Return()

    # Function_0_10A end

    def Function_1_134(): pass

    label("Function_1_134")

    Return()

    # Function_1_134 end

    def Function_2_135(): pass

    label("Function_2_135")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    AddParty(0x50, 0xFF, 0xFF)
    AddParty(0x4E, 0xFF, 0xFF)
    SetChrPos(0x109, -860, 0, -5920, 270)
    SetChrPos(0x151, 810, 250, -4590, 270)
    SetChrPos(0x14F, -770, 0, -4740, 270)
    SetChrChipByIndex(0x151, 1)
    SetChrChipByIndex(0x14F, 0)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x151, 0x0, 0x0, 0x3)
    OP_43(0x14F, 0x0, 0x0, 0x3)
    OP_6D(840, 350, -4190, 0)
    OP_67(0, 7940, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(45000, 0)
    OP_6E(448, 0)

    def lambda_1E3():
        OP_6B(1970, 8000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E3)

    def lambda_1F3():
        OP_67(0, 3180, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1F3)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x10, 0x2)
    Sleep(300)

    ChrTalk(    #0
        0x109,
        (
            "#1060F#6P#100P哎呀～……\x01",
            "没想到竟然会是\x01",
            "提妲的妈妈。\x02\x03",

            "听说你们夫妇两人\x01",
            "都在外国工作，\x01",
            "已经都回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x14F,
        "艾莉卡博士",
        (
            "#1452F#5P#100P发生了那样的事件\x01",
            "怎么能不立刻赶回来。\x02\x03",

            "#1457F当消息传到边境的时候\x01",
            "已经很晚了，\x01",
            "现在回来也只能收拾残局……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #2
        0x14F,
        "艾莉卡博士",
        (
            "#1832F#5P#100P真是的，\x01",
            "如果不回来的话，\x01",
            "那个死老头又会乱来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        (
            "#1066F#6P#100P您、您好像很生\x01",
            "拉赛尔博士的气啊？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #4
        0x14F,
        "艾莉卡博士",
        "#1455F#5P#100P#3S当然了！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #5
        0x14F,
        "艾莉卡博士",
        (
            "#1459F#5P#100P#2S竟然把提妲\x01",
            "带到那个崩坏坍塌的\x01",
            "浮游都市去！\x02\x03",

            "再怎么娇惯自己的孙女，\x01",
            "也得有个限度啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1064F#6P#100P哈、哈哈……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x14F,
        "艾莉卡博士",
        (
            "#1830F#5P#100P而且最可恨的是，\x01",
            "还让那种不良青年\x01",
            "接近我的女儿……\x02\x03",

            "该死的红毛男……\x01",
            "竟然把我的宝贝女儿给……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x109,
        (
            "#1066F#6P#100P红毛男……\x01",
            "是说阿加特吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x14F,
        "艾莉卡博士",
        (
            "#1830F#5P#100P不要在我面前\x01",
            "提到这个禁忌的名字！\x02\x03",

            "#1458F哼哼哼，给我等着，\x01",
            "阿加特·科洛斯纳……\x02\x03",

            "下次我还要\x01",
            "用更强力的机体\x01",
            "将你彻底击溃……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_66A():
        OP_6D(1600, 500, -4140, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_66A)
    OP_8F(0x109, 0x1AE, 0xFA, 0xFFFFE8A4, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #10
        0x109,
        (
            "#1066F#4P#100P（好、好像\x01",
            "  发生了不少事情……）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x151,
        "希德中校",
        (
            "#701F#5P#100P（唔……\x01",
            "  详细的情况我也不清楚。）\x02\x03",

            "（顺便一说，\x01",
            "  拉赛尔博士现在到国外旅行去了。）\x02\x03",

            "（所以这次有关的事宜\x01",
            "  都需要她的协助。）\x02",
        )
    )

    Jump("loc_78C")

    label("loc_78C")

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1060F#4P#100P（是这样吗……）\x02",
    )

    CloseMessageWindow()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_72(0x803, 0x0)
    ExitThread()
    OP_44(0x14F, 0x0)
    SetChrSubChip(0x14F, 0)
    OP_8C(0x14F, 90, 600)
    OP_44(0x109, 0x0)
    SetChrSubChip(0x109, 0)
    OP_44(0x151, 0x0)
    SetChrSubChip(0x151, 0)

    NpcTalk(    #13
        0x14F,
        "艾莉卡博士",
        "#1830F#3S#6P#100P──你们在听吗！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        "#1064F#4P#100P是！\x02",
    )


    NpcTalk(    #15
        0x151,
        "希德中校",
        "#702F#5P#100P是！\x02",
    )

    Jump("loc_895")

    label("loc_895")

    OP_56(0x1)
    OP_59()
    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #16
        0x14F,
        "艾莉卡博士",
        "#1832F#6P#100P哼，算了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14F, 270, 400)

    def lambda_8DB():
        OP_6D(840, 350, -4190, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8DB)

    def lambda_8F3():
        OP_8F(0xFE, 0xFFFFF8A8, 0xFFFFFF06, 0xFFFFEE08, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 0, lambda_8F3)
    Sleep(100)

    def lambda_913():
        OP_8F(0xFE, 0xFFFFFCA4, 0x0, 0xFFFFE8E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_913)
    Sleep(200)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x151, 0x0, 0x0, 0x3)
    OP_43(0x14F, 0x0, 0x0, 0x3)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_71(0x800, 0x0)
    ExitThread()
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_71(0x801, 0x0)
    ExitThread()
    OP_71(0x2003, 0x0)
    ExitThread()
    OP_71(0x803, 0x0)
    ExitThread()
    Sleep(3000)

    NpcTalk(    #17
        0x14F,
        "艾莉卡博士",
        (
            "#1452F#5P#100P──不过话说回来，\x01",
            "这楼梯还真是长啊。\x02\x03",

            "还要走多久才能到？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1060F#2P#100P啊，\x01",
            "应该很快就到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(    #19
        0x109,
        (
            "#1062F#2P#100P哦……\x01",
            "好像可以看到尽头了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x50, 0xFF)
    RemoveParty(0x4E, 0xFF)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4145   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_135 end

    def Function_3_A73(): pass

    label("Function_3_A73")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A98")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_BDA")

    label("loc_A98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_BDA")

    label("loc_AB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_BDA")

    label("loc_ACA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_BDA")

    label("loc_AE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_BDA")

    label("loc_AFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B15")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_BDA")

    label("loc_B15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_BDA")

    label("loc_B2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B47")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_BDA")

    label("loc_B47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B60")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_BDA")

    label("loc_B60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B79")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_BDA")

    label("loc_B79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B92")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_BDA")

    label("loc_B92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_BDA")

    label("loc_BAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_BDA")

    label("loc_BC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_BDA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BEF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_BDA")

    label("loc_BEF")

    Return()

    # Function_3_A73 end

    def Function_4_BF0(): pass

    label("Function_4_BF0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x109, -79990, 0, -3600, 0)
    SetChrPos(0x11, -79300, 0, -6300, 0)
    SetChrPos(0x10, -80660, 0, -5340, 0)
    OP_6D(-77590, 500, -15350, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(359, 0)
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
    LoadEffect(0x0, "map\\mp082_00.eff")
    LoadEffect(0x1, "scraft\\sc008_02.eff")
    LoadEffect(0x2, "map\\mp259_02.eff")
    LoadEffect(0x3, "map\\mpP90_00.eff")
    LoadEffect(0x4, "map\\mpP90_01.eff")
    LoadEffect(0x5, "map\\mpP90_04.eff")

    def lambda_D1B():
        OP_8E(0xFE, 0xFFFEC758, 0x0, 0x4C68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D1B)
    Sleep(50)

    def lambda_D3B():
        OP_8E(0xFE, 0xFFFECA00, 0x0, 0x4466, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D3B)
    Sleep(50)

    def lambda_D5B():
        OP_8E(0xFE, 0xFFFEC4EC, 0x0, 0x448E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_D5B)

    def lambda_D76():
        OP_6D(-77890, 500, 21500, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D76)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(-78410, 0, 20750, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(322, 0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)
    Sleep(300)

    ChrTalk(    #20
        0x11,
        "#702F没路了……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#1459F#6P喂……\x01",
            "这是怎么回事？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #22
        0x109,
        (
            "#1065F#5P艾莉卡博士、希德中校。\x02\x03",

            "#1063F如果要继续前进的话，\x01",
            "就必须对你们两人\x01",
            "采取某种措施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        "#700F唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1452F#6P听起来\x01",
            "很可疑呢。\x02\x03",

            "总之，\x01",
            "就是教会擅长的某种法术对吗？\x02",
        )
    )

    Jump("loc_F29")

    label("loc_F29")

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1075F#5P嗯，正是。\x02\x03",

            "#1060F具体而言，\x01",
            "就是请你们接受某种暗示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        "#702F暗示……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#1459F#6P是为了确保在这里所见的一切\x01",
            "不会被泄露给其他人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1060F#5P不，因为中校\x01",
            "还需要给上面进行汇报，\x01",
            "所以不能这样强人所难。\x02\x03",

            "#1075F仅仅是保证在这里所见之事\x01",
            "对可信任之人以外一律守口如瓶而已。\x02\x03",

            "#1066F……请你们在心中\x01",
            "铭记这一点就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#1457F#6P真是慎之又慎啊……\x02\x03",

            "#1456F只是这种程度的话，\x01",
            "就完全无所谓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#701F我明白了。\x02\x03",

            "只要在脑海中默念就行了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1060F#5P不用，\x01",
            "将身体自然放松就可以了。\x02\x03",

            "#1075F好，那就开始了──\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    Sleep(500)

    ChrTalk(    #32
        0x109,
        (
            "#1063F#5P──谨以空之女神之名，\x01",
            "将神圣之七耀召唤于此。\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x0, 0x109, -150, 800, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #33
        0x109,
        (
            "#1065F#5P空之金耀、识之银耀──\x02\x03",

            "请以相克之力\x01",
            "为他们呈现\x01",
            "通达圣域之道。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -80040, 1000, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC9)
    OP_82(0x0, 0x2)
    Sleep(2000)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0x10, 0, 800, 0, 0, 0, 0, 1400, 2400, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, 0, 800, 0, 0, 0, 0, 1400, 2400, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()

    ChrTalk(    #34
        0x10,
        "#1454F#6P！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        "#702F啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-78920, 500, 22990, 0)
    OP_67(0, 4260, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(33000, 0)
    OP_6E(330, 0)
    OP_22(0xD7, 0x0, 0x64)
    OP_22(0x146, 0x64, 0x1)
    PlayEffect(0x3, 0x7, 0xFF, -80000, 0, 21950, 0, 0, 0, 2300, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0xFF, -80000, 0, 21950, 0, 0, 0, 2300, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x5, 0xFF, -80000, 0, 21950, 0, 0, 0, 2300, 1600, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)

    def lambda_1487():
        OP_6B(2640, 800)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1487)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    OP_82(0x5, 0x0)
    OP_0D()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x10,
        "#1455F#6P什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        "#702F门……！？\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_0D()

    def lambda_1530():
        OP_6D(-78410, 0, 20750, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1530)

    def lambda_1548():
        OP_67(0, 4860, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1548)

    def lambda_1560():
        OP_6B(2550, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1560)

    def lambda_1570():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1570)

    def lambda_1580():
        OP_6E(322, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1580)
    WaitChrThread(0x109, 0x0)
    SetChrSubChip(0x109, 0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    Sleep(500)

    ChrTalk(    #38
        0x109,
        (
            "#1075F#5P感谢你们的合作。\x02\x03",

            "#1060F对可信任之人以外一律守口如瓶──\x01",
            "你们能发自内心这么想真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#1457F#6P……原来如此。\x02\x03",

            "#1459F如果只是口头敷衍，\x01",
            "就会『看不见』门吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#703F真是惊人……\x02\x03",

            "#700F看来我就是打听这种手法的原理，\x01",
            "也是自讨没趣吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x109,
        (
            "#1066F#5P嗯，如果可以的话，\x01",
            "还是请不要深究了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x10, 0x4)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    def lambda_173D():
        OP_6D(-78410, 0, 21400, 1200)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_173D)
    OP_8E(0x109, 0xFFFEC6FE, 0x0, 0x5398, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x70, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x10E)
    OP_73(0x3)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #42
        0x109,
        "#1060F#5P那么……我们进去吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    def lambda_17C1():
        OP_6D(-77850, 0, 23770, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_17C1)

    def lambda_17D9():
        OP_8E(0xFE, 0xFFFEC802, 0x0, 0x5FAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17D9)
    Sleep(150)

    def lambda_17F9():
        OP_8E(0xFE, 0xFFFEC4EC, 0x0, 0x5FAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_17F9)
    Sleep(300)

    def lambda_1819():
        OP_8E(0xFE, 0xFFFECA00, 0x0, 0x5FAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1819)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4144   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_4_BF0 end

    SaveToFile()

Try(main)
