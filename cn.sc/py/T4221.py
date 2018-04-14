from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4221   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4221.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '雷沃尔',                               # 9
        '雪拉扎德',                             # 10
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


    AddCharChip(
        'ED6_DT26/CH20260 ._CH',             # 00
        'ED6_DT26/CH20234 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT26/CH20261 ._CH',             # 03
        'ED6_DT07/CH01270 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT26/CH20260P._CP',             # 00
        'ED6_DT26/CH20234P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT26/CH20261P._CP',             # 03
        'ED6_DT07/CH01270P._CP',             # 04
    )

    DeclNpc(
        X                   = 143260,
        Z                   = 0,
        Y                   = 3310,
        Direction           = 356,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_112",          # 00, 0
        "Function_1_11F",          # 01, 1
        "Function_2_19D",          # 02, 2
        "Function_3_358",          # 03, 3
        "Function_4_E2F",          # 04, 4
        "Function_5_F96",          # 05, 5
    )


    def Function_0_112(): pass

    label("Function_0_112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E")
    Event(0, 3)

    label("loc_11E")

    Return()

    # Function_0_112 end

    def Function_1_11F(): pass

    label("Function_1_11F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B")
    OP_B1("t4221_y")
    Jump("loc_144")

    label("loc_13B")

    OP_B1("t4221_n")

    label("loc_144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_181")
    OP_22(0x87, 0x1, 0x1E)
    OP_22(0xAE, 0x1, 0x1E)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_77(0xFF, 0xBF, 0xB7, 0x0, 0x0)

    label("loc_181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_END)), "loc_19C")
    OP_1B(0x1, 0x0, 0x4)
    OP_1B(0x2, 0x0, 0x4)
    OP_1B(0x3, 0x0, 0x5)
    OP_1B(0x4, 0x0, 0x5)

    label("loc_19C")

    Return()

    # Function_1_11F end

    def Function_2_19D(): pass

    label("Function_2_19D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1F3")

    ChrTalk(    #0
        0xFE,
        (
            "好、好像从门外传来了\x01",
            "悲鸣和愤怒的声音……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "到、到底发生了什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_354")

    label("loc_1F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_260")

    ChrTalk(    #2
        0xFE,
        (
            "科洛蒂娅殿下看来\x01",
            "要在城堡里逗留一阵子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "有她在的话\x01",
            "城堡里的气氛就会很活跃，\x01",
            "真令人高兴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354")

    label("loc_260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_301")

    ChrTalk(    #4
        0xFE,
        "凯诺娜小姐被捕了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "这样一来情报部的余党\x01",
            "就被一网打尽了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "也能稍稍减轻尤莉亚\x01",
            "小姐肩上的负担吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "最后果然还是\x01",
            "正义取得了胜利。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354")

    label("loc_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_354")

    ChrTalk(    #8
        0xFE,
        (
            "啊，科洛蒂娅殿下，\x01",
            "您回来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "有何吩咐？\x01",
            "要不要我来准备一些饮品？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_354")

    TalkEnd(0xFE)
    Return()

    # Function_2_19D end

    def Function_3_358(): pass

    label("Function_3_358")

    OP_35(0x0, 0x0)
    OP_BB(0x0, 0x6, 0xE7)
    OP_31(0x0, 0xFE, 0x0)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    OP_6D(79650, 350, 55020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 85060, 500, 60710, 180)
    OP_72(0x5, 0x4)
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x8)
    OP_6F(0x5, 5)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    FadeToBright(2000, 0)

    def lambda_40F():
        OP_6D(85310, 350, 60680, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40F)

    def lambda_427():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_427)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #10
        0x101,
        "#007F……唔～……好刺眼…………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 16)
    Sleep(200)
    SetChrSubChip(0x101, 0)
    Sleep(200)
    SetChrSubChip(0x101, 16)
    Sleep(200)
    SetChrSubChip(0x101, 0)
    Sleep(1000)

    def lambda_49C():
        OP_99(0x101, 0x0, 0x8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_49C)
    Sleep(300)
    OP_71(0x5, 0x8)
    OP_6F(0x5, 5)
    OP_B0(0x5, 0x28)
    OP_70(0x5, 0x3B)
    Sleep(1500)

    def lambda_4CD():
        OP_99(0xFE, 0x8, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4CD)

    ChrTalk(    #11 op#A op#5
        0x101,
        "#504F#25A嘿～～～～～……\x05\x02",
    )

    OP_9E(0x101, 0xF, 0x0, 0x7D0, 0xFA0)

    def lambda_50B():
        OP_99(0xFE, 0xC, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50B)
    Sleep(1000)
    SetChrSubChip(0x101, 14)
    Sleep(200)
    SetChrSubChip(0x101, 17)
    Sleep(200)
    SetChrSubChip(0x101, 18)
    Sleep(500)

    ChrTalk(    #12
        0x101,
        "#501F嗯～～睡得真香呢～～！\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x12, 0x15, 0x3E8)
    Sleep(500)
    OP_99(0x101, 0x15, 0x12, 0x3E8)
    SetChrSubChip(0x101, 23)
    Sleep(1000)
    SetChrSubChip(0x101, 18)
    Sleep(500)

    ChrTalk(    #13
        0x101,
        (
            "#004F咦……\x02\x03",

            "……………………………………\x02\x03",

            "#505F对了，我们\x01",
            "昨天留宿在王都里面了。\x02\x03",

            "和约修亚一起逛了庆典……\x01",
            "回来途中吃了冰淇淋……\x02\x03",

            "晚上和老爸一起参加晚餐会……\x02\x03",

            "……然后………\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_AD(0x2400B7, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x101,
        (
            "#580F………………………………\x02\x03",

            "……不………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    Sleep(100)
    OP_22(0x23B, 0x0, 0x3C)
    SetChrChipByIndex(0x101, 65535)
    OP_8C(0x101, 270, 0)

    def lambda_6D3():
        OP_96(0xFE, 0x1462C, 0x0, 0xECF4, 0x258, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D3)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x1)

    def lambda_700():
        OP_6D(83470, 0, 60260, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_700)

    def lambda_718():
        OP_67(0, 8000, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_718)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_8C(0x101, 180, 1000)
    Sleep(1000)
    OP_8C(0x101, 90, 1000)
    Sleep(1000)
    OP_8C(0x101, 270, 1000)
    Sleep(1000)
    OP_8C(0x101, 180, 1000)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        (
            "#587F这是……\x01",
            "约修亚和老爸的房间……\x02\x03",

            "我应该……\x01",
            "是和雪拉姐睡一个房间的……\x02\x03",

            "那个……\x01",
            "……我是什么时候开始睡着的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(100)
    Fade(500)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x101,
        (
            "#580F啊……\x02\x03",

            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #17
        0x101,
        "#005F#4S约修亚！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()

    def lambda_8A8():
        OP_8E(0x101, 0x137AE, 0x0, 0xBDA6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8A8)
    Sleep(100)

    def lambda_8C8():
        OP_6D(80350, 0, 51510, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C8)

    def lambda_8E0():
        OP_67(0, 8000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8E0)
    Sleep(1500)

    def lambda_8FD():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8FD)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(79000, 0, 7200, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, 79210, 0, 9810, 180)
    SetChrPos(0x9, 67190, 0, 9780, 180)
    ClearChrFlags(0x9, 0x80)

    def lambda_99C():
        OP_8E(0x101, 0x13452, 0x0, 0x820, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_99C)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 90, 1000)
    Sleep(1000)
    OP_8C(0x101, 270, 1000)
    Sleep(1000)
    OP_8C(0x101, 90, 1000)
    OP_69(0x9, 0x7D0)

    def lambda_9F6():

        label("loc_9F6")

        OP_69(0x9, 0x0)
        OP_48()
        Jump("loc_9F6")

    QueueWorkItem2(0x9, 3, lambda_9F6)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    OP_8E(0x9, 0x103BA, 0x0, 0x6F4, 0x7D0, 0x0)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x9, 0x101, 500)
    Sleep(500)
    OP_44(0x9, 0x3)

    def lambda_A58():
        OP_6D(76750, 0, 2160, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A58)

    def lambda_A70():
        OP_67(0, 8000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A70)

    def lambda_A88():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A88)

    def lambda_A98():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A98)
    OP_8E(0x9, 0x12426, 0x0, 0x834, 0x7D0, 0x0)

    ChrTalk(    #18
        0x9,
        (
            "#6P#020F哎呀，艾丝蒂尔。\x01",
            "这么晚才睡醒呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(    #19
        0x101,
        "#587F#2P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "#6P#021F真是的，昨天那么晚还不回来，\x01",
            "叫人担心死了。\x02\x03",

            "不过看起来，你应该是\x01",
            "和约修亚聊了很多──\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x9, 0x7D0, 0x1388, 0x0)

    ChrTalk(    #21
        0x101,
        "#005F#2P雪拉姐，约修亚在哪儿！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        "#6P#023F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#005F#2P我在找约修亚！\x02\x03",

            "雪拉姐，你见过他吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "#6P#023F今天早上没见到过……\x02\x03",

            "话说回来，你不是昨天太累了\x01",
            "就睡在那边的房间了吗？\x02\x03",

            "醒来的时候他不在？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#580F#2P咦……！？\x02\x03",

            "我太累，就睡了……\x01",
            "你是听谁说的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        "#6P#023F老师说的啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#580F#2P老、老爸！？\x02\x03",

            "#005F那么！\x01",
            "你有没有看见老爸！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#6P#022F老师他刚才走上楼梯\x01",
            "去了空中庭园……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#002F#2P！！！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 800)

    def lambda_D32():
        OP_6D(78660, 0, 2110, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_D32)

    def lambda_D4A():
        OP_8E(0xFE, 0x16512, 0x0, 0x938, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D4A)
    Sleep(500)

    ChrTalk(    #30
        0x9,
        "#023F啊，等等，艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    OP_69(0x9, 0x5DC)

    ChrTalk(    #31
        0x9,
        "#022F……怎么回事……？\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_DBE():
        OP_6E(240, 1000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_DBE)
    Fade(1000)
    SetChrChipByIndex(0x9, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x9,
        (
            "#022F………………………………\x02\x03",

            "#522F逆位的『恋人』……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1002)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_358 end

    def Function_4_E2F(): pass

    label("Function_4_E2F")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_E51"),
        (1, "loc_E85"),
        (2, "loc_EB7"),
        (5, "loc_EE4"),
        (7, "loc_F11"),
        (6, "loc_F42"),
        (SWITCH_DEFAULT, "loc_F75"),
    )


    label("loc_E51")


    ChrTalk(    #33
        0x101,
        (
            "#1002F不，不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F75")

    label("loc_E85")


    ChrTalk(    #34
        0x102,
        (
            "#1042F不对，不是这边。\x01",
            "……赶紧去女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F75")

    label("loc_EB7")


    ChrTalk(    #35
        0x103,
        (
            "#022F这边不对。\x01",
            "……赶紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F75")

    label("loc_EE4")


    ChrTalk(    #36
        0x106,
        (
            "#057F没时间磨蹭了，\x01",
            "赶快去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F75")

    label("loc_F11")


    ChrTalk(    #37
        0x108,
        (
            "#072F没空去别处了。\x01",
            "……抓紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F75")

    label("loc_F42")


    ChrTalk(    #38
        0x107,
        (
            "#062F不、不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F75")

    label("loc_F75")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_4_E2F end

    def Function_5_F96(): pass

    label("Function_5_F96")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_FB8"),
        (1, "loc_FEC"),
        (2, "loc_101E"),
        (5, "loc_104B"),
        (7, "loc_1078"),
        (6, "loc_10A9"),
        (SWITCH_DEFAULT, "loc_10DC"),
    )


    label("loc_FB8")


    ChrTalk(    #39
        0x101,
        (
            "#1002F不，不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC")

    label("loc_FEC")


    ChrTalk(    #40
        0x102,
        (
            "#1042F不对，不是这边。\x01",
            "……赶紧去女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC")

    label("loc_101E")


    ChrTalk(    #41
        0x103,
        (
            "#022F这边不对。\x01",
            "……赶紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC")

    label("loc_104B")


    ChrTalk(    #42
        0x106,
        (
            "#057F没时间磨蹭了，\x01",
            "赶快去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC")

    label("loc_1078")


    ChrTalk(    #43
        0x108,
        (
            "#072F没空去别处了。\x01",
            "……抓紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC")

    label("loc_10A9")


    ChrTalk(    #44
        0x107,
        (
            "#062F不、不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC")

    label("loc_10DC")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_5_F96 end

    SaveToFile()

Try(main)
