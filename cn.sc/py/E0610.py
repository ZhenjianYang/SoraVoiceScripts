from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0610   ._SN',
        MapName             = 'Event',
        Location            = 'E0610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        '幻惑之铃露茜奥拉',                     # 9
        '瘦狼瓦鲁特',                           # 10
        '小丑肯帕雷拉',                         # 11
        '红莲士兵',                             # 12
        '红莲士兵',                             # 13
        '红莲士兵',                             # 14
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
        'ED6_DT27/CH03523 ._CH',             # 00
        'ED6_DT27/CH03503 ._CH',             # 01
        'ED6_DT27/CH03600 ._CH',             # 02
        'ED6_DT26/CH20396 ._CH',             # 03
        'ED6_DT26/CH20387 ._CH',             # 04
        'ED6_DT26/CH20392 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03523P._CP',             # 00
        'ED6_DT27/CH03503P._CP',             # 01
        'ED6_DT27/CH03600P._CP',             # 02
        'ED6_DT26/CH20396P._CP',             # 03
        'ED6_DT26/CH20387P._CP',             # 04
        'ED6_DT26/CH20392P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_27E",          # 01, 1
        "Function_2_284",          # 02, 2
        "Function_3_7B3",          # 03, 3
        "Function_4_C0B",          # 04, 4
        "Function_5_E4C",          # 05, 5
        "Function_6_122B",         # 06, 6
        "Function_7_127A",         # 07, 7
        "Function_8_12C2",         # 08, 8
        "Function_9_15A8",         # 09, 9
        "Function_10_1A21",        # 0A, 10
        "Function_11_1D3A",        # 0B, 11
        "Function_12_2325",        # 0C, 12
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1B9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_27D")

    label("loc_1B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1D3")
    OP_A3(0x10F1)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_27D")

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_1ED")
    OP_A3(0x10F2)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_27D")

    label("loc_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_207")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    Event(0, 5)
    Jump("loc_27D")

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_221")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    Event(0, 8)
    Jump("loc_27D")

    label("loc_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_23B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    Event(0, 9)
    Jump("loc_27D")

    label("loc_23B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_255")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F6)
    Event(0, 10)
    Jump("loc_27D")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_26F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F7)
    Event(0, 11)
    Jump("loc_27D")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_27D")
    OP_A3(0x10F8)
    Event(0, 12)

    label("loc_27D")

    Return()

    # Function_0_19A end

    def Function_1_27E(): pass

    label("Function_1_27E")

    OP_22(0x7A, 0x1, 0x46)
    Return()

    # Function_1_27E end

    def Function_2_284(): pass

    label("Function_2_284")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-2140, 0, 2420, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(315000, 0)
    OP_6E(522, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0x9, 2)
    SetChrPos(0x8, -630, 300, 2150, 180)
    SetChrPos(0x9, 1130, 300, 2150, 180)
    SetChrPos(0xA, -2470, 0, 1930, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#240F#5P──所谓的最后实验，\x01",
            "对手就是『那个东西』吗。\x02\x03",

            "就算是教授和莱维，\x01",
            "也没有办法轻松地解决呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#250F#2P呵呵，或许是吧。\x02\x03",

            "怎么说都是传说般的存在。\x01",
            "强度完全不在一个档次上啊。\x02\x03",

            "#252F……但是肯帕雷拉啊。\x01",
            "这可不像是你的作风啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_439():
        OP_8C(0xA, 90, 300)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_439)
    Sleep(200)
    SetChrSubChip(0x8, 0)
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(200)

    ChrTalk(    #2
        0xA,
        "#850F#5P哎呀呀，什么地方不像？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#252F#2P要是平常的你，\x01",
            "应该会很乐意和教授同行的。\x02\x03",

            "既然你这次没有这么做，\x01",
            "肯定是有其他更有趣的事吧？\x02\x03",

            "赶快从实招了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "#852F#5P讨厌啦，瓦鲁特。\x01",
            "就那么不信任我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#252F#2P呵呵，信任啊。\x01",
            "你的信用就像你的编号一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#241F#2PＮｏ．０──\x01",
            "呵呵，也就是信用为零啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "#855F#5P哎呀哎呀，你们两个好过分。\x02\x03",

            "#850F嗯，虽然我确实很想跟着去看看，\x01",
            "但真是不凑巧，现在有更紧急的工作呢。\x02\x03",

            "我打算向那位大人申请\x01",
            "方舟的使用许可。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x9,
        (
            "#253F#2P哈哈哈！真的假的！\x02\x03",

            "居然要\x01",
            "使用那种怪物啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#244F#2P『红色方舟』──古罗力亚斯。\x02\x03",

            "#242F你该不会……\x01",
            "打算把利贝尔化为焦土吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "#854F#5P呼呼，那就要看\x01",
            "教授和莱维怎么决定了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 300)
    Sleep(500)

    ChrTalk(    #11
        0xA,
        (
            "#853F#5P所以说，我待会儿\x01",
            "就必须马上出去一趟了。\x02\x03",

            "实验的经过，等回来之后\x01",
            "再慢慢讲给我听吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1600   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_284 end

    def Function_3_7B3(): pass

    label("Function_3_7B3")

    EventBegin(0x0)
    OP_24(0x7A, 0x46)
    SetChrFlags(0x102, 0x80)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, -70600, 1300, -160, 270)
    SetChrPos(0xC, -70600, 1200, 2150, 270)
    SetChrPos(0xD, -70600, 1200, -2500, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    OP_76(0x4, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x4, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_88F():

        label("loc_88F")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_88F")

    QueueWorkItem2(0x101, 3, lambda_88F)
    OP_71(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_71(0x5, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0xB,
        (
            "──高度１５５９亚矩。\x01",
            "由北东方向潜入利贝尔的领土内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        (
            "在抵达瓦雷利亚湖上空之前\x01",
            "就这样保持航向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        "明白。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 1)
    Sleep(300)

    ChrTalk(    #15
        0xC,
        (
            "利贝尔的警备艇\x01",
            "似乎没察觉到我们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xC,
        (
            "『隐形机能』吗……\x01",
            "实在是个很方便的装置。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xD, 2)
    Sleep(300)

    ChrTalk(    #17
        0xD,
        (
            "#6P不过，要不是有这隐形机能\x01",
            "那可就要引起大骚动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xD,
        (
            "#6P这艘飞船还不算什么，\x01",
            "等到那个怪物入侵的那天……。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xC,
        "哈哈，没错。\x02",
    )

    CloseMessageWindow()
    OP_20(0x0)
    OP_44(0x101, 0x3)
    OP_7C(0x0, 0x64, 0xBB8, 0x3E8)
    OP_22(0x1F7, 0x0, 0x55)
    Sleep(100)
    OP_22(0x1FA, 0x0, 0x55)
    Sleep(900)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0x1F7, 0x0, 0x55)
    Sleep(500)
    OP_7C(0x0, 0x64, 0xBB8, 0x3E8)
    OP_22(0x1FA, 0x0, 0x55)
    Sleep(1000)

    def lambda_ADA():

        label("loc_ADA")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_ADA")

    QueueWorkItem2(0x101, 3, lambda_ADA)
    SetChrSubChip(0xC, 0)
    Sleep(100)

    ChrTalk(    #20
        0xD,
        "#6P什…么…！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    Sleep(100)

    ChrTalk(    #21
        0xC,
        "是敌袭吗！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x59)
    Sleep(500)

    ChrTalk(    #22
        0xB,
        (
            "#5P别慌张！\x01",
            "雷达怎么了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        (
            "雷达有反应！\x01",
            "４点钟方向有小型艇接近！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xD,
        "#6P数据库比对──有了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xD,
        (
            "#6P是帝国莱恩福尔特社制造的飞船。\x01",
            "『卡普亚空贼团』所属的山猫号！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        "#5P空贼！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_7B3 end

    def Function_4_C0B(): pass

    label("Function_4_C0B")

    EventBegin(0x0)
    OP_24(0x7A, 0x64)
    SetChrFlags(0x102, 0x80)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, -70600, 1300, -160, 270)
    SetChrPos(0xC, -70600, 1200, 2150, 270)
    SetChrPos(0xD, -70600, 1200, -2500, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    OP_76(0x4, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x4, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_CE7():

        label("loc_CE7")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_CE7")

    QueueWorkItem2(0x101, 3, lambda_CE7)
    OP_71(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_71(0x5, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0xC,
        "空贼艇，脱离了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xD,
        "#6P怎么办，要追击吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        "#5P不……别去管它。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        (
            "#5P王国军的警备艇也就罢了，\x01",
            "现在不是和小角色纠缠的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xD,
        "#6P没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xC,
        (
            "现在以确保『古罗力亚斯』\x01",
            "的航线为最优先任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        "#5P……暂时先返航吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        (
            "#5P将空贼的情况\x01",
            "汇报给肯帕雷拉大人。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_C0B end

    def Function_5_E4C(): pass

    label("Function_5_E4C")

    EventBegin(0x0)
    OP_23(0x7A)
    OP_6D(2150, 0, 700, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_74(0xFF, 0x6, 0x8)
    OP_75(0xFF, 0x6, 0x0)
    FadeToBright(1000, 0)
    OP_43(0x102, 0x1, 0x0, 0x6)
    Sleep(1500)
    OP_43(0x101, 0x1, 0x0, 0x7)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #35
        0x102,
        (
            "#1032F#5P锁上门。\x02\x03",

            "我马上让飞船出发。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1005F明、明白了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 600)

    def lambda_F32():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F32)

    def lambda_F40():
        OP_8E(0xFE, 0xFFFFF39E, 0x0, 0xFFFFFFA6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F40)
    WaitChrThread(0x101, 0x1)

    def lambda_F60():
        OP_8E(0xFE, 0x1676, 0x0, 0xFFFFFFF6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F60)
    WaitChrThread(0x102, 0x1)
    OP_72(0x2, 0x10)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0xF)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x2)
    FadeToDark(1000, 0, -1)

    def lambda_FAA():
        OP_8E(0xFE, 0xFFFFE912, 0x0, 0x8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FAA)
    Sleep(100)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x102, 0x80)
    OP_0D()
    Sleep(1500)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x102, 0x1)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 4)
    SetChrSubChip(0x102, 0)
    SetChrPos(0x102, -70600, 1200, -220, 270)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x102,
        (
            "#1033F#5P（启动钥匙认证……）\x02\x03",

            "（输入认证编码……）\x02\x03",

            "#1035F（……好了！）\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x64)
    OP_75(0xFF, 0x6, 0x2)
    OP_74(0xFF, 0x6, 0x8)
    Sleep(100)
    OP_74(0xFF, 0x6, 0x9)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xA)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xB)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xC)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xD)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xE)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xF)
    Sleep(100)
    OP_75(0xFF, 0x6, 0x2)
    Sleep(1000)

    def lambda_113C():
        OP_6D(-69000, 1000, 300, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113C)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -63530, 0, -80, 270)

    def lambda_1170():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1170)
    OP_8E(0x101, 0xFFFEFD0E, 0x0, 0xFFFFFFCE, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #38
        0x101,
        "#1004F#4P哇哇……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 1)
    Sleep(300)

    ChrTalk(    #39
        0x102,
        (
            "#1031F#5P我用远程操控来打开舱口。\x02\x03",

            "马上就要出发了，快坐好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1006F#4P……嗯！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5406   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_E4C end

    def Function_6_122B(): pass

    label("Function_6_122B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 7480, 0, -60, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1252():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1252)
    OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFFFC4, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_122B end

    def Function_7_127A(): pass

    label("Function_7_127A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 7480, 0, -60, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_12A1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12A1)
    OP_8E(0xFE, 0x1388, 0x0, 0xFFFFFFC4, 0xFA0, 0x0)
    Return()

    # Function_7_127A end

    def Function_8_12C2(): pass

    label("Function_8_12C2")

    EventBegin(0x0)
    OP_24(0x7A, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x4, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0xC, 0x0, 0x0, 0x0)

    def lambda_137E():

        label("loc_137E")

        OP_7C(0x3C, 0x3C, 0xBB8, 0x64)
        OP_48()
        Jump("loc_137E")

    QueueWorkItem2(0x101, 2, lambda_137E)
    OP_D0(5000, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #41
        0x101,
        "#1020F掉、掉下去了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1031F#6P没关系……\x01",
            "马上就会调整过来。\x02",
        )
    )

    OP_D0(4000, 0)
    Sleep(500)
    OP_D0(3000, 0)
    Sleep(500)
    OP_D0(2000, 0)
    Sleep(500)
    OP_D0(1000, 0)
    Sleep(500)
    OP_D0(0, 0)
    Sleep(500)

    def lambda_143E():

        label("loc_143E")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_143E")

    QueueWorkItem2(0x101, 2, lambda_143E)

    ChrTalk(    #43 op#A op#5
        0x102,
        "#1035F#6P#5A……好。\x05\x02",
    )

    Sleep(1000)
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x3, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0x9, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0x3, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0x2, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_12C2 end

    def Function_9_15A8(): pass

    label("Function_9_15A8")

    EventBegin(0x0)
    OP_24(0x7A, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_1664():

        label("loc_1664")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1664")

    QueueWorkItem2(0x101, 3, lambda_1664)
    FadeToBright(1000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -71400, 2200, 2240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    Sleep(200)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #44
        0x101,
        (
            "#1020F#2P哇哇……\x01",
            "这个是雷达吧。\x02\x03",

            "有三个光点\x01",
            "朝我们接近了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#1030F#6P嗯，是追兵。\x02\x03",

            "看来要想办法\x01",
            "将他们甩掉才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1015F#2P约修亚……\x01",
            "原来你会操纵飞艇啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        (
            "#1031F#6P还好吧。\x02\x03",

            "#1035F只是，这艘飞船\x01",
            "并没有配备武器。\x02\x03",

            "所以情况不容乐观。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1007F#2P是吗……\x02\x03",

            "#1004F可是，为什么会特地\x01",
            "找了一艘没有武装的飞船呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1033F#6P……只有这艘正在维修的船，\x01",
            "安全防范措施比较薄弱。\x02\x03",

            "因为当时事态紧急，\x01",
            "也没有选择的余地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1015F#2P事态紧急……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        (
            "#1026F#2P那个……莫非是指……\x02\x03",

            "我被捉到\x01",
            "『古罗力亚斯』的事……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#1035F#6P……………………………\x02\x03",

            "#1031F没空说闲话了，\x01",
            "会有些摇晃，当心点！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x1FA, 0x1, 0x50)

    def lambda_199A():

        label("loc_199A")

        OP_7C(0x0, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_199A")

    QueueWorkItem2(0x101, 3, lambda_199A)
    Sleep(1000)
    OP_22(0x1FA, 0x1, 0x5A)

    def lambda_19BF():

        label("loc_19BF")

        OP_7C(0x0, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_19BF")

    QueueWorkItem2(0x101, 3, lambda_19BF)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #53
        0x101,
        "#1020F#2P哇哇哇……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F9)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_15A8 end

    def Function_10_1A21(): pass

    label("Function_10_1A21")

    EventBegin(0x0)
    OP_24(0x7A, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71670, 900, 1010, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_6D(-72410, 1200, 1310, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_1B1A():

        label("loc_1B1A")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1B1A")

    QueueWorkItem2(0x101, 3, lambda_1B1A)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -71400, 2200, 2240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #54
        0x102,
        "#1032F#6P可恶……真糟糕。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1002F#2P追击我们的这些家伙\x01",
            "相当有一手……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#1035F#6P应该是使用『结社』的\x01",
            "强化程序学会了操纵技术吧。\x02\x03",

            "虽然还无法灵活应用，\x01",
            "不过单方面追击还真不好对付。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1007F#2P是吗……\x02\x03",

            "#1015F但是，既然应用上还不行，\x01",
            "也就代表如果发生什么意外的话──\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x1FE, 0x0, 0x50)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0x101,
        "#1004F#2P中、中弹了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#1034F#6P不……\x01",
            "不是我们的船！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FA)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1A21 end

    def Function_11_1D3A(): pass

    label("Function_11_1D3A")

    EventBegin(0x0)
    OP_24(0x7A, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_1DF6():

        label("loc_1DF6")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1DF6")

    QueueWorkItem2(0x101, 3, lambda_1DF6)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -71400, 2200, 2240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #60
        0x101,
        "#1020F#2P那、那是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        "#1034F#6P『山猫号』……为什么？\x02",
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x46)
    Sleep(1000)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("扩音器的声音")

    AnonymousTalk(    #62
        "\x07\x05……约修亚！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("扩音器的声音")

    AnonymousTalk(    #63
        (
            "那艘船里的\x01",
            "是约修亚吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0x101,
        "#1019F#2P（这声音……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1031F#6P啊啊……我在这里！\x02\x03",

            "为什么你们会\x01",
            "在这里呢！？\x02\x03",

            "我还以为你们早就\x01",
            "离开利贝尔了……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #66
        (
            "嘿嘿，是哥哥他们担心\x01",
            "你会不会遇上什么困难。\x02\x03",

            "于是就一直在远处观察\x01",
            "那艘庞然大物的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("吉尔")

    AnonymousTalk(    #67
        (
            "哈哈，还真敢说呢。\x02\x03",

            "当初拼命在拜托我们的人\x01",
            "到底是谁啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #68
        "吉、吉尔哥！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("多伦")

    AnonymousTalk(    #69
        (
            "算啦，反正我们和『结社』\x01",
            "也有不少帐要算。\x02\x03",

            "等到全数奉还后\x01",
            "再离开利贝尔吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #70
        0x102,
        (
            "#1035F#6P……是吗……\x02\x03",

            "#1031F谢谢你们，真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #71
        (
            "嘿嘿……\x01",
            "你可要好好感谢我们哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("吉尔")

    AnonymousTalk(    #72
        (
            "不过，刚才一路看下来，\x01",
            "你好像没有进行反击呢。\x02\x03",

            "出了什么问题吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #73
        0x102,
        (
            "#1035F#6P因为我只弄到\x01",
            "一艘没有武装的飞船。\x02\x03",

            "所以稍微有点麻烦。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("吉尔")

    AnonymousTalk(    #74
        "是吗……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #75
        "怎、怎么办……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("多伦")

    AnonymousTalk(    #76
        (
            "…好～这样的话\x01",
            "那就兵分两路吧！\x02\x03",

            "只有一艘的话你应该甩得掉吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #77
        0x102,
        "#1031F#6P嗯……没问题。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("吉尔")

    AnonymousTalk(    #78
        "那好，愿女神保佑你！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #79
        (
            "约修亚……\x01",
            "一定要小心哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FB)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1D3A end

    def Function_12_2325(): pass

    label("Function_12_2325")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_23DD():

        label("loc_23DD")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_23DD")

    QueueWorkItem2(0x101, 3, lambda_23DD)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Sleep(100)
    SetChrSubChip(0x102, 2)
    Sleep(300)

    ChrTalk(    #80
        0x102,
        "#1031F#6P#6P艾丝蒂尔，雷达上怎样了？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #81
        0x101,
        (
            "#1006F#2P嗯……\x01",
            "光点已经消失了，\x02\x03",

            "看来是完全甩开了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        (
            "#1031F#6P是吗……\x02\x03",

            "#1033F…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1013F#2P……………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #84
        0x101,
        (
            "#1008F#2P嗯，那个……\x02\x03",

            "#1016F那些空贼，\x01",
            "是一群挺不错的人呢。\x02\x03",

            "真没想到他们竟会在这种时候\x01",
            "跑过来帮助我们……\x02\x03",

            "#1017F真是要另眼相看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#1033F#6P是啊……\x02\x03",

            "#1031F契约上的关系\x01",
            "虽然已经解除……\x02\x03",

            "但人与人的感情\x01",
            "似乎就没那么单纯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1016F#2P啊哈哈……\x01",
            "你到现在才明白这些吗。\x02\x03",

            "#1006F随着一次次的相遇，\x01",
            "时而欢喜，时而争吵，\x01",
            "而彼此之间的感情也会不断加深。\x02\x03",

            "这就是人与人之间的交往吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#1035F#6P啊啊……\x02\x03",

            "#1030F但是在我生存过的世界里，\x01",
            "这些东西并非是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1020F#2P啊……\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Sleep(500)
    SetChrSubChip(0x102, 0)
    OP_21()
    OP_1D(0x5B)
    Sleep(500)

    def lambda_2726():
        OP_6B(2730, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2726)
    Sleep(1500)

    ChrTalk(    #89
        0x102,
        (
            "#1035F#6P杀人，或是被杀。\x02\x03",

            "抢夺，或是被抢。\x02\x03",

            "我在遇到你之前，\x01",
            "只是一直重复着这种事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1026F#2P但、但是……\x02\x03",

            "#1003F你也有过和姐姐、莱维\x01",
            "生活在一起的幸福时光吧……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        (
            "#1033F#6P……莱维和你说的吗。\x02\x03",

            "#1035F……………………………………\x02\x03",

            "#1045F那段记忆虽然还在，\x01",
            "但对我来说，就像是别人的经历一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1026F#2P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#1031F#6P我的心灵崩溃的时候……\x01",
            "在哈梅尔的那些回忆，\x01",
            "就已经不属于我自己了。\x02\x03",

            "自那之后，我就已经不再是人，\x01",
            "只是一个会呼吸的木偶而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1026F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#1031F#6P姐姐死去时的状况，\x01",
            "至今仍然记忆犹新。\x02\x03",

            "#1035F那个时候，我和姐姐\x01",
            "遭到了伏击男子的偷袭。\x02\x03",

            "那男人把我打飞……\x01",
            "整个人压在姐姐上面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1020F#2P…………！………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#1033F#6P年幼的我，虽然不明白\x01",
            "那意味着什么……\x02\x03",

            "但心中还是感到厌恶，\x01",
            "上前揪住那人的后背。\x02\x03",

            "#1035F我们两人打成一团，\x01",
            "结果我马上就被弹开……\x02\x03",

            "但不知何时，我的手中\x01",
            "已经握着那男子的枪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1026F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        (
            "#1045F#6P现在回想起来，那时的我\x01",
            "大概就已经具备杀人的才能了吧。\x02\x03",

            "虽然从来都没学过，\x01",
            "但我却迅速地拉开了保险栓，\x01",
            "并毫不犹豫地扣动了扳机。\x02\x03",

            "喉咙被打穿的男子\x01",
            "满脸诧异地望着我，\x01",
            "口中吐出了鲜血。\x02\x03",

            "直到这时，我才终于意识到\x01",
            "自己开枪杀了人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1003F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#1032F#6P但是，那男子还没断气。\x02\x03",

            "他眼中充满血丝，\x01",
            "不停地喘着粗气，\x01",
            "接着抽出军刀就向我扑来。\x02\x03",

            "#1033F就像面对野兽袭击一样，\x01",
            "我不禁蜷起身体闭上了双眼……\x02\x03",

            "#1035F但我却没有感受到任何冲击，\x01",
            "而是有什么柔软的东西紧紧抱住了我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1026F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        (
            "#1033F#6P当我睁开双眼时，\x01",
            "首先映入眼帘的是姐姐微笑的面容。\x02\x03",

            "那男子不知在何时已经倒下了……\x01",
            "而莱维就在一旁呆呆地站着。\x02\x03",

            "姐姐在被莱维扶起之后，\x01",
            "便将自己的口琴交给了我……\x02\x03",

            "#1035F然后缓缓闭上了双眼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1027F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#1035F#6P……记得很清楚对吧？\x02\x03",

            "#1045F但是，就算这样说出来，\x01",
            "我也感觉不到哀伤和痛苦，\x02\x03",

            "就像在读别人的日记一样。\x01",
            "实在是不可思议呢。\x02\x03",

            "#1033F而和你在一起的时候……\x01",
            "也是一样的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1026F#2P………啊啊……………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        (
            "#1045F#6P在接触到你的温暖之后，\x01",
            "我的确感觉到自己变了。\x02\x03",

            "和你在一起会感到喜悦，\x01",
            "也会开始觉得你很可爱。\x02\x03",

            "但在我的内心深处，\x01",
            "总觉得这一切像是别人的事情一样。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #108
        (
            "\x07\x00#20W或许……\x01",
            "那才是我真正的感觉吧。\x02\x03",

            "虚无空洞……\x01",
            "我就像是有缺陷的人偶一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_24(0x7A, 0x32)
    Sleep(100)
    OP_24(0x7A, 0x28)
    Sleep(100)
    OP_24(0x7A, 0x1E)
    Sleep(100)
    OP_24(0x7A, 0x14)
    Sleep(100)
    OP_24(0x7A, 0xA)
    Sleep(100)
    OP_24(0x7A, 0x0)
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2325 end

    SaveToFile()

Try(main)
