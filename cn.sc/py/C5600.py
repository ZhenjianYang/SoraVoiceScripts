from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5600   ._SN',
        MapName             = 'Other',
        Location            = 'C5600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        '小丑肯帕雷拉',                         # 9
        '银发的青年',                           # 10
        '怀斯曼教授',                           # 11
        '歼灭天使玲',                           # 12
        '高速飞艇',                             # 13
        '帕蒂尔·玛蒂尔',                       # 14
        '目标用照相机',                         # 15
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12000 ._CH',             # 02
        'ED6_DT29/CH12001 ._CH',             # 03
        'ED6_DT29/CH12000 ._CH',             # 04
        'ED6_DT29/CH12001 ._CH',             # 05
        'ED6_DT29/CH12000 ._CH',             # 06
        'ED6_DT29/CH12001 ._CH',             # 07
        'ED6_DT29/CH12000 ._CH',             # 08
        'ED6_DT29/CH12001 ._CH',             # 09
        'ED6_DT27/CH03600 ._CH',             # 0A
        'ED6_DT07/CH02040 ._CH',             # 0B
        'ED6_DT27/CH03550 ._CH',             # 0C
        'ED6_DT27/CH03510 ._CH',             # 0D
        'ED6_DT26/CH20295 ._CH',             # 0E
        'ED6_DT26/CH20305 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12000P._CP',             # 02
        'ED6_DT29/CH12001P._CP',             # 03
        'ED6_DT29/CH12000P._CP',             # 04
        'ED6_DT29/CH12001P._CP',             # 05
        'ED6_DT29/CH12000P._CP',             # 06
        'ED6_DT29/CH12001P._CP',             # 07
        'ED6_DT29/CH12000P._CP',             # 08
        'ED6_DT29/CH12001P._CP',             # 09
        'ED6_DT27/CH03600P._CP',             # 0A
        'ED6_DT07/CH02040P._CP',             # 0B
        'ED6_DT27/CH03550P._CP',             # 0C
        'ED6_DT27/CH03510P._CP',             # 0D
        'ED6_DT26/CH20295P._CP',             # 0E
        'ED6_DT26/CH20305P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 9520,
        TriggerZ            = 9000,
        TriggerY            = 6150,
        TriggerRange        = 1000,
        ActorX              = 9960,
        ActorZ              = 9000,
        ActorY              = 6600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_252",          # 01, 1
        "Function_2_283",          # 02, 2
        "Function_3_299",          # 03, 3
        "Function_4_403",          # 04, 4
        "Function_5_1450",         # 05, 5
        "Function_6_26C2",         # 06, 6
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_244")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 5)
    Jump("loc_251")

    label("loc_244")

    Event(0, 4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_251")

    Return()

    # Function_0_22E end

    def Function_1_252(): pass

    label("Function_1_252")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFE3AE0, 0x230073)
    OP_22(0x1C5, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B")
    OP_6F(0x1, 0)
    Jump("loc_282")

    label("loc_27B")

    OP_6F(0x1, 60)

    label("loc_282")

    Return()

    # Function_1_252 end

    def Function_2_283(): pass

    label("Function_2_283")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_298")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_283")

    label("loc_298")

    Return()

    # Function_2_283 end

    def Function_3_299(): pass

    label("Function_3_299")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E9, 1)"), scpexpr(EXPR_END)), "loc_308")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xE9\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D28)
    Jump("loc_36E")

    label("loc_308")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xE9\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xE9\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_36E")

    Jump("loc_3A2")

    label("loc_371")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3A2")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x43)"), scpexpr(EXPR_END)), "loc_3C1")
    Jump("loc_3FA")

    label("loc_3C1")


    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xE9\x01\x07\x00的食谱。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #4
        "\x1F\xE9\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_3FA")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_299 end

    def Function_4_403(): pass

    label("Function_4_403")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    OP_6D(2380, 30000, -14320, 0)
    OP_67(0, 10010, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(340000, 0)
    OP_6E(730, 0)
    OP_11(0xA0, 0xB4, 0xFF, 0x3A98, 0x30D40, 0x0)
    SetChrPos(0x101, -26000, 18450, 11200, 180)
    SetChrPos(0x8, -26000, 18450, 11200, 180)
    OP_A1(0xC, 0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 700)
    OP_70(0x0, 0x30C)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, 21380, 20000, -38500, 0)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x3E8, 0x2710, 0x1)

    def lambda_4D7():
        OP_6C(330000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4D7)

    def lambda_4E7():
        OP_67(0, 12010, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4E7)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5 op#A
        (
            "\x07\x05#50A同一时刻。\x01",
            "利贝尔王国，某处──\x02",
        )
    )

    Sleep(100)
    FadeToBright(1000, 0)
    Sleep(3000)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    OP_22(0x79, 0x0, 0x64)
    Fade(1000)
    OP_44(0x8, 0xFF)
    OP_6D(-31780, 30000, -16820, 0)
    OP_67(0, 8060, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(59000, 0)
    OP_6E(697, 0)
    OP_0D()

    def lambda_5AE():
        OP_6D(-31780, 25000, 5000, 5000)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_5AE)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x57E4, 0x3E80, 0x1)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x57E4, 0x3A98, 0x1)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x57E4, 0x36B0, 0x1)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x4E20, 0x32C8, 0x1)
    OP_8C(0xC, 0, 400)
    SetChrFlags(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x1ADB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x0, 0x20)
    OP_6F(0x0, 780)
    OP_70(0x0, 0x320)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)

    def lambda_681():
        OP_8F(0xFE, 0xFFFF9B38, 0x3B2E, 0x2E90, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_681)
    Sleep(1500)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xC, 0x1)
    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_82(0x1, 0x2)
    OP_6F(0x0, 1000)
    OP_70(0x0, 0x41A)
    OP_73(0x0)
    Sleep(200)
    OP_6F(0x0, 1050)
    OP_70(0x0, 0x456)
    OP_73(0x0)
    OP_23(0x79)
    OP_23(0xCC)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Fade(1000)
    OP_6D(-13700, 30000, 8590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(296000, 0)
    OP_6E(409, 0)
    OP_0D()
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 1110)
    OP_70(0x0, 0x474)
    OP_73(0x0)
    OP_B0(0x0, 0x3C)
    OP_6F(0x0, 1140)
    OP_70(0x0, 0x4B0)
    Sleep(200)
    OP_22(0xFD, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    SetChrBattleFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x80)
    StopSound(0xEA60, 0x30D40, 0x1770)

    def lambda_7C7():
        OP_6D(-25090, 15200, -1540, 6000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7C7)

    def lambda_7DF():
        OP_67(0, 11430, -18000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7DF)

    def lambda_7F7():
        OP_6B(2090, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7F7)

    def lambda_807():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_807)

    def lambda_817():
        OP_6E(230, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_817)
    OP_8E(0x8, 0xFFFF9CE6, 0x3A98, 0xFFFFFA38, 0x7D0, 0x0)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    Sleep(500)

    NpcTalk(    #6
        0x8,
        "奇怪的少年",
        (
            "#5P#850F哟。\x01",
            "很棒的地方嘛。\x02\x03",

            "#5P教授的品味还真不错啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -16600, 15000, 4170, 237)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #7
        0x9,
        "青年的声音",
        "#3P你真慢啊，肯帕雷拉。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_8F5():
        OP_6D(-21040, 15200, 1680, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8F5)

    def lambda_90D():
        OP_6B(2300, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_90D)
    TurnDirection(0x8, 0x9, 500)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)

    def lambda_92E():
        OP_92(0x9, 0x8, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_92E)
    Sleep(500)

    def lambda_948():
        OP_69(0x8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_948)

    def lambda_956():
        OP_6C(270000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_956)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x0)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(    #8
        0x8,
        (
            "#851F呀，『剑帝』。\x01",
            "好久不见啦。\x02\x03",

            "你不在的这半年间，\x01",
            "我真是寂寞难耐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "#124F哼，口是心非。\x02\x03",

            "#123F对帝国游击士协会的袭击，\x01",
            "听说是由你负责的。\x02\x03",

            "作为卡西乌斯·布莱特的对手，\x01",
            "想必你相当地开心吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#850F什么啊，原来你知道啦。\x02\x03",

            "#851F呀～那位大叔\x01",
            "真是个不得了的人物啊。\x02\x03",

            "明明应该不知道我的存在，\x01",
            "却能采取一连串正确的对策。\x02\x03",

            "托他的福，我手中的猎兵团\x01",
            "被消灭了一支。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "#124F『杰斯塔猎兵团』吗。\x02\x03",

            "#120F虽然也训练了一下，\x01",
            "但毕竟还是些平庸之辈。\x02\x03",

            "要作为『剑圣』的对手，\x01",
            "担子稍微重了点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#853F不过，能拖住他的行动\x01",
            "直到你的工作完成，算是很不错了。\x02\x03",

            "#850F哎呀，难道你\x01",
            "很期待和他的对决吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "#123F呵呵……一点点。\x02\x03",

            "#124F不过，山中的猛虎\x01",
            "也被名为军务的锁链束缚住了。\x02\x03",

            "从正面进攻的话，\x01",
            "已经不可能阻止我们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#850F呵呵，教授的计划\x01",
            "看来进行得很顺利呢。\x02\x03",

            "那么，其它的成员\x01",
            "都来到利贝尔了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#120F啊啊，昨天才刚刚集合。\x02\x03",

            "#124F布卢布兰那家伙，\x01",
            "好像老早就过来准备了。\x02\x03",

            "『怪盗绅士』、『瘦狼』、\x01",
            "『幻惑之铃』、『歼灭天使』……\x02\x03",

            "#123F跑来的偏偏\x01",
            "都是些古怪的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#851F嘻嘻，你不也是\x01",
            "相当古怪嘛。\x02\x03",

            "#854F话说回来，『他』……\x01",
            "听说现在行踪不明了，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        "#120F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#854F嘻嘻，真是期待啊。\x02\x03",

            "在我们『执行者』当中，\x01",
            "他的隐秘行动也算首屈一指的呢。\x02\x03",

            "面对『剑帝』和『白面』，\x01",
            "他能努力到什么程度呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#121F……………………………\x02\x03",

            "#124F毕竟是好几年前\x01",
            "就从结社洗手不干的人。\x02\x03",

            "应该不会成为多大的威胁。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, -17000, 15200, 8000, 226)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #20
        0xA,
        "男性的声音",
        (
            "#1P不不。\x01",
            "我认为没有这回事哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x9, 0xA, 500)
    Sleep(500)
    Fade(1000)
    OP_6D(-20220, 15200, 2810, 0)
    OP_67(0, 11430, -18000, 0)
    OP_6B(2390, 0)
    OP_6C(0, 0)
    OP_6E(230, 0)
    SetChrPos(0xA, -18440, 15000, 4740, 229)
    SetChrPos(0x9, -24430, 15000, 240, 41)
    SetChrPos(0x8, -24930, 15000, -1890, 24)

    def lambda_FAD():

        label("loc_FAD")

        TurnDirection(0x9, 0xA, 500)
        OP_48()
        Jump("loc_FAD")

    QueueWorkItem2(0x9, 1, lambda_FAD)
    TurnDirection(0x8, 0xA, 500)

    def lambda_FC5():
        OP_6D(-23900, 15000, -700, 3000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FC5)
    OP_8E(0xA, 0xFFFFA4FC, 0x3A98, 0xFFFFFE48, 0x7D0, 0x0)
    OP_0D()
    WaitChrThread(0xA, 0x1)
    Sleep(500)

    ChrTalk(    #21
        0xA,
        (
            "#2P#1150F呀，肯帕雷拉。\x01",
            "还劳烦你特地过来一趟。\x02\x03",

            "你成功地拖延了卡西乌斯·布莱特\x01",
            "的行动，真是帮了我一个大忙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#851F#6P嘻嘻，这是份很愉快的工作。\x02\x03",

            "#850F不过教授的计划书\x01",
            "我拜读过了……\x02\x03",

            "这实在是相当\x01",
            "令人愉快的想法嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "#2P#1151F哈哈哈，能让你这个小丑\x01",
            "这么说，真是我的荣幸。\x02\x03",

            "不过，实际的计划\x01",
            "将会更加令人期待哦。\x02\x03",

            "毕竟前来参与这次行动的诸位，\x01",
            "每个人都拥有各自的目的。\x02\x03",

            "我……还有这位也是一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "#124F#5P……我不否定。\x02\x03",

            "#121F我可没有受你\x01",
            "暗示影响的道理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        "#2P#1154F哎呀哎呀，真冷淡啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#851F#6P呵呵，原来如此。\x01",
            "看来似乎有不少的隐情。\x02\x03",

            "#854F算了，教授的恶趣味\x01",
            "已经可以称得上是艺术了。\x02\x03",

            "就让我尽情地享受吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "#2P#1151F呵呵……\x01",
            "说什么恶趣味，多难听啊。\x02\x03",

            "算了，你就尽情地\x01",
            "欣赏本次的计划吧。\x02\x03",

            "以我们『盟主』的代理人身份。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "#851F#6P嘻嘻，交给我吧。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_44(0x9, 0xFF)
    OP_8C(0x9, 187, 0)
    OP_8C(0xA, 235, 0)
    OP_6D(-25190, 15200, -2240, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(215000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #29
        0x8,
        (
            "#853F#5P执行者Ｎｏ.０──\x01",
            "『小丑』肯帕雷拉。\x02\x03",

            "#854F现在开始观察使徒\x01",
            "怀斯曼的『福音计划』。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    Sleep(300)
    OP_24(0x1C5, 0x5A)
    Sleep(300)
    OP_24(0x1C5, 0x50)
    Sleep(300)
    OP_24(0x1C5, 0x46)
    Sleep(300)
    OP_24(0x1C5, 0x3C)
    Sleep(300)
    OP_24(0x1C5, 0x32)
    Sleep(300)
    OP_24(0x1C5, 0x28)
    Sleep(300)
    OP_24(0x1C5, 0x1E)
    Sleep(300)
    OP_24(0x1C5, 0x14)
    Sleep(300)
    OP_24(0x1C5, 0xA)
    Sleep(300)
    OP_24(0x1C5, 0x0)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/T5200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_403 end

    def Function_5_1450(): pass

    label("Function_5_1450")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1463")
    Call(0, 6)

    label("loc_1463")

    OP_71(0x0, 0x4)
    OP_6D(-13460, 15200, -850, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(6010, 0)
    OP_6C(0, 0)
    OP_6E(598, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, -26000, 18450, 11200, 180)
    OP_A1(0xD, 0x2)
    OP_71(0x2, 0x20)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0xF)
    OP_6F(0x2, 501)
    OP_70(0x2, 0x208)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x2)
    OP_CF(0xB, 0x2, "Frame85__ren")
    OP_8C(0xB, 180, 0)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, 21380, 20000, -38500, 0)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x3E8, 0x2710, 0x1)

    def lambda_1543():
        OP_6D(-23730, 15200, 7580, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1543)

    def lambda_155B():
        OP_67(0, 7830, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_155B)

    def lambda_1573():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1573)

    def lambda_1583():
        OP_6B(4200, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1583)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0x79, 0x0, 0x64)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x57E4, 0x3E80, 0x1)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x57E4, 0x3A98, 0x1)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x57E4, 0x36B0, 0x1)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x4E20, 0x32C8, 0x1)
    OP_8C(0xD, 0, 400)
    OP_72(0x2, 0x20)
    OP_B0(0x2, 0xA)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x1E1)

    def lambda_1619():
        OP_8F(0xFE, 0xFFFF9B38, 0x4E20, 0x2E90, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1619)
    Sleep(1500)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xD, 90, 50)
    Fade(1000)
    OP_6D(-27510, 15200, 10990, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xD, -24960, 18450, 7270, 90)

    def lambda_16A2():
        OP_8F(0xFE, 0xFFFF9F20, 0x3BC4, 0x1C34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_16A2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 421)
    OP_70(0x2, 0x1CC)
    OP_0D()
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xD, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xFA0, 0x1F4)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 421)
    OP_23(0x79)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xB, 0x1)
    Sleep(500)

    ChrTalk(    #30
        0xB,
        (
            "#260F哈哈哈，把那些野猪一样的\x01",
            "飞艇全部甩开了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        "#260F谢谢你，『帕蒂尔·玛蒂尔』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xD,
        "#4P…………………………\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, -12840, 14800, 9830, 270)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #33
        0x9,
        "青年的声音",
        "#1P终于回来了，玲。\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_17DA():
        OP_6D(-20330, 15200, 9930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17DA)
    Sleep(500)

    def lambda_17F7():
        OP_8E(0xFE, 0xFFFFC252, 0x3B60, 0x23D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_17F7)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x2)
    OP_8C(0xB, 180, 400)
    WaitChrThread(0x9, 0x0)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #34
        0xB,
        "#260F莱维！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x2)
    OP_CF(0xB, 0x2, "Frame86__ren")
    OP_8C(0xB, 90, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xB, 0xFFFFAFC4, 0x3B60, 0x240E, 0x258, 0x5DC)
    SetChrFlags(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_188D():
        OP_8E(0xFE, 0xFFFFBCB2, 0x3B60, 0x2350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_188D)

    def lambda_18A8():
        OP_6D(-16620, 15200, 9110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18A8)

    def lambda_18C0():
        OP_67(0, 5290, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18C0)

    def lambda_18D8():
        OP_6B(3420, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18D8)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #35
        0xB,
        (
            "#260F嘿嘿，我回来了。\x02\x03",

            "玲可是按照你的吩咐，\x01",
            "成功做完了实验哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#120F呵呵，辛苦了。\x02\x03",

            "不过你把事情搞得\x01",
            "还真是大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        (
            "#260F因为这次说是\x01",
            "不能杀人嘛。\x02\x03",

            "这么无聊，\x01",
            "至少要热闹热闹嘛。\x02\x03",

            "托你的福，\x01",
            "开了个很开心的茶会哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#120F呵呵……是吗。\x02\x03",

            "实验的结果怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "#260F这个嘛。\x01",
            "还算不错吧。\x02\x03",

            "虽然被教会的哥哥\x01",
            "给搅了一下局……\x02\x03",

            "但运作很稳定，\x01",
            "我想足够用于实战了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        "#120F嗯，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xB,
        (
            "#260F不过『福音』\x01",
            "现在还不能量产吧？\x02\x03",

            "能否作为兵器使用，\x01",
            "现在还无法确定呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "#120F没有量产的必要啊。\x02\x03",

            "此次的实验也是\x01",
            "单纯以测试新型\x01",
            "福音的潜在能力为目的。\x02\x03",

            "并不是以制作兵器\x01",
            "为目的的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "#260F咦，是吗？\x02\x03",

            "算了。\x01",
            "我也没什么兴趣。\x02\x03",

            "对了，话说回来……\x01",
            "约修亚还没找到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#120F啊啊……\x02\x03",

            "我们为了扰乱军队而放出的\x01",
            "人形兵器被破坏了好几架。\x02\x03",

            "恐怕就是他干的好事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        (
            "#260F嗯～真有一手。\x02\x03",

            "虽然玲也很擅长捉迷藏，\x01",
            "但还是敌不过约修亚……\x02\x03",

            "啊～啊，不好玩。\x02\x03",

            "为什么不干脆\x01",
            "返回结社呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        "#120F谁知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "#260F这么说来教授倒是\x01",
            "说过由于艾丝蒂尔的原因\x01",
            "约修亚才不会回来。\x02\x03",

            "艾丝蒂尔好像也在\x01",
            "寻找约修亚呢～\x02\x03",

            "到底怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#120F玲……\x02\x03",

            "教授说的话\x01",
            "还是不要盲目相信的好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        "#260F为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "#120F所谓真相，\x01",
            "每个人的看法都不同。\x02\x03",

            "譬如月亮的脸\x01",
            "被大家比喻成各种各样的形态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xB,
        "#260F比如小兔子啦，或者螃蟹之类的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "#120F是啊。\x02\x03",

            "教授所讲出来的“真实”\x01",
            "和玲自己感悟到的“真实”是不同的。\x02\x03",

            "你一定要自己去看，自己去感受，\x01",
            "只有这样才能体会到属于玲自己的“真实”。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        (
            "#260F嗯～听起来好深奥哦，\x01",
            "玲不是很明白……\x02\x03",

            "不过玲好像确实\x01",
            "挺喜欢艾丝蒂尔她们…\x02\x03",

            "就算下次再见面，\x01",
            "大概也不会马上就杀死她们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#120F那就好。\x02\x03",

            "你很了不起哦，玲。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFFBF28, 0x3B60, 0x2364, 0x7D0, 0x0)
    Fade(250)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    OP_0D()
    OP_99(0x9, 0x0, 0x2, 0x3E8)
    OP_99(0x9, 0x3, 0x6, 0x3E8)
    OP_99(0x9, 0x3, 0x6, 0x3E8)
    Fade(250)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 0)
    OP_0D()
    OP_8F(0x9, 0xFFFFC252, 0x3B60, 0x23D2, 0x7D0, 0x0)

    ChrTalk(    #55
        0xB,
        "#260F嘿嘿……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, -7420, 15000, 13980, 270)
    SetChrPos(0x8, -7990, 15000, 14810, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #56
        0xA,
        "男性的声音",
        "#1P呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2006():
        OP_8E(0xFE, 0xFFFFBC9E, 0x3B60, 0x1EDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2006)

    def lambda_2021():
        OP_8E(0xFE, 0xFFFFC3C4, 0x3B60, 0x215C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2021)
    Sleep(500)

    def lambda_2041():
        OP_8E(0xFE, 0xFFFFC43C, 0x3B60, 0x2684, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2041)

    def lambda_205C():
        OP_6D(-16030, 15200, 9710, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_205C)

    def lambda_2074():
        OP_6C(32000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2074)

    def lambda_2084():
        OP_6B(3290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2084)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 90, 400)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #57
        0xB,
        (
            "#260F教授……\x01",
            "还有肯帕雷拉！\x02\x03",

            "你也来了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#850F呼呼，前几天刚到。\x02\x03",

            "你在王都似乎\x01",
            "过得相当愉快啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        (
            "#260F嘿嘿嘿，还好啦。\x02\x03",

            "要是事先知道你要来的话，\x01",
            "绝对会招待你一起参加的。\x02\x03",

            "当时的场面可是非常热闹的哦！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_21F7")

    ChrTalk(    #60
        0x8,
        (
            "#850F呵呵，那可真是遗憾啊。\x02\x03",

            "我也请游击士大姐姐她们\x01",
            "看了场人偶剧……\x02\x03",

            "但比起你的茶会来，\x01",
            "实在是不值一提啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2268")

    label("loc_21F7")


    ChrTalk(    #61
        0x8,
        (
            "#850F呵呵，那可真是遗憾啊。\x02\x03",

            "我也请游击士大哥哥他们\x01",
            "看了场人偶剧……\x02\x03",

            "但比起你的茶会来，\x01",
            "实在是不值一提啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2268")


    ChrTalk(    #62
        0xA,
        (
            "#1150F哈哈，下次有机会\x01",
            "再请我吧。\x02\x03",

            "不过玲……\x02\x03",

            "你好像和艾丝蒂尔\x01",
            "相当投缘吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "#260F嘿嘿，还好啦。\x02\x03",

            "并不像教授说的那么讨厌，\x01",
            "是个还挺不错的大姐姐呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "#1150F哈哈，我也没\x01",
            "说过她是个讨厌的人啊。\x02\x03",

            "实话说，倒真是一个性格善良，\x01",
            "魅力十足的小姑娘呢。\x02\x03",

            "只是，约修亚之所以不愿意回来，\x01",
            "原因确实是因为她。\x02\x03",

            "对吧，莱维？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "#120F我不否认这是原因之一。\x02\x03",

            "但是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#1150F如何，玲。\x02\x03",

            "如果艾丝蒂尔成为我们的同伴，\x01",
            "你会不会很高兴？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        "#120F同……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "#260F让艾丝蒂尔成为同伴？\x02\x03",

            "……嘻嘻。\x01",
            "那当然好啊！很好玩的样子！\x02\x03",

            "虽然实力还差得很远，\x01",
            "但只要经过锻炼，应该也会很快变强吧……\x02\x03",

            "而且，如果艾丝蒂尔加入的话，\x01",
            "约修亚也会回来对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        "#1150F呵呵，这是当然的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#850F啊哈哈，不愧是教授。\x01",
            "你还真是有兴致呀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#120F教授，玩笑开过头了吧……\x02\x03",

            "即使是你，\x01",
            "也不能无视本人的意志，\x01",
            "强行将她拉入结社。\x02\x03",

            "这可是『盟主』制定的`\x01",
            "『噬身之蛇』规约。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xA,
        (
            "#1150F哼哼，这自然不用你说。\x02\x03",

            "你以为身为『蛇之使徒』的我\x01",
            "会做出那种事吗？\x02\x03",

            "包括你和约修亚在内，\x01",
            "我也没有强迫过任何人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        "#120F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "#1150F要是那么做的话，\x01",
            "难得的乐趣就都被破坏了。\x02\x03",

            "必须让她完全自愿地\x01",
            "加入我们才行。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1450 end

    def Function_6_26C2(): pass

    label("Function_6_26C2")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_273C"),
        (1, "loc_2742"),
        (SWITCH_DEFAULT, "loc_2748"),
    )


    label("loc_273C")

    OP_A2(0x1200)
    Jump("loc_2748")

    label("loc_2742")

    OP_A2(0x1201)
    Jump("loc_2748")

    label("loc_2748")

    Return()

    # Function_6_26C2 end

    SaveToFile()

Try(main)
