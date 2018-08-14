from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3115   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3115.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '拉赛尔博士',                           # 9
        '艾莉卡',                               # 10
        '普罗梅笛',                             # 11
        '康丝坦茨',                             # 12
        '雨果',                                 # 13
        '伊格尔',                               # 14
        '目标用照相机',                         # 15
        '',                                     # 16
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
        'ED6_DT07/CH02620 ._CH',             # 00
        'ED6_DT07/CH02623 ._CH',             # 01
        'ED6_DT07/CH01230 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH02440 ._CH',             # 04
        'ED6_DT07/CH01680 ._CH',             # 05
        'ED6_DT07/CH01100 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH01430 ._CH',             # 08
        'ED6_DT27/CH03970 ._CH',             # 09
        'ED6_DT07/CH01250 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02620P._CP',             # 00
        'ED6_DT07/CH02623P._CP',             # 01
        'ED6_DT07/CH01230P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH02440P._CP',             # 04
        'ED6_DT07/CH01680P._CP',             # 05
        'ED6_DT07/CH01100P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH01430P._CP',             # 08
        'ED6_DT27/CH03970P._CP',             # 09
        'ED6_DT07/CH01250P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2350,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -107400,
        Z                   = 0,
        Y                   = -90,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -103500,
        Z                   = 0,
        Y                   = 108340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -102790,
        Z                   = 0,
        Y                   = 98030,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_222",          # 01, 1
        "Function_2_226",          # 02, 2
        "Function_3_2EA",          # 03, 3
        "Function_4_3FA",          # 04, 4
        "Function_5_50E",          # 05, 5
        "Function_6_63B",          # 06, 6
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_202")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_221")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_221")

    Return()

    # Function_0_1E2 end

    def Function_1_222(): pass

    label("Function_1_222")

    OP_82(0x80, 0x0)
    Return()

    # Function_1_222 end

    def Function_2_226(): pass

    label("Function_2_226")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_2E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_290")

    ChrTalk(    #0
        0xFE,
        (
            "唔，\x01",
            "好像错过时机了啊。\x02",
        )
    )

    Jump("loc_25B")

    label("loc_25B")

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "本来还希望在工房船\x01",
            "出航之前让他签字的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6")

    label("loc_290")


    ChrTalk(    #2
        0xFE,
        (
            "不过，\x01",
            "工房长好像出去了呢。\x02",
        )
    )

    Jump("loc_2BB")

    label("loc_2BB")

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "我还想让他给\x01",
            "这些文件签字呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2E6")

    TalkEnd(0xFE)
    Return()

    # Function_2_226 end

    def Function_3_2EA(): pass

    label("Function_3_2EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_3F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_393")

    ChrTalk(    #4
        0xFE,
        (
            "那孩子，\x01",
            "最近好像经常偷懒的样子……\x02",
        )
    )

    Jump("loc_331")

    label("loc_331")

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "让年轻人去做体力劳动\x01",
            "是这里的规矩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "就算房间再脏乱，\x01",
            "我也不打算去动一根指头。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F6")

    label("loc_393")


    ChrTalk(    #7
        0xFE,
        "我的工作就是教育新人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "我要指示新人\x01",
            "去处理资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "所以我一根指头\x01",
            "也不用动。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3F6")

    TalkEnd(0xFE)
    Return()

    # Function_3_2EA end

    def Function_4_3FA(): pass

    label("Function_4_3FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_50A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_46B")

    ChrTalk(    #10
        0xFE,
        "这么说来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "怎么感觉\x01",
            "中央工房好安静啊。\x02",
        )
    )

    Jump("loc_44D")

    label("loc_44D")

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "……唔，是错觉吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_50A")

    label("loc_46B")


    ChrTalk(    #13
        0xFE,
        (
            "呼，\x01",
            "埃尔赛尤的修补作业终于结束了。\x02",
        )
    )

    Jump("loc_49B")

    label("loc_49B")

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "感觉也好久没有\x01",
            "回到中央工房了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "不过还有\x01",
            "引擎周边需要调整，\x01",
            "还不能松劲就是了。\x02",
        )
    )

    Jump("loc_506")

    label("loc_506")

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_50A")

    TalkEnd(0xFE)
    Return()

    # Function_4_3FA end

    def Function_5_50E(): pass

    label("Function_5_50E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_637")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5AA")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #16
        0xFE,
        "唔唔，这个设计图是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "唔，\x01",
            "画这个图的不是拉赛尔呢。\x02",
        )
    )

    Jump("loc_572")

    label("loc_572")

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "要是那家伙，\x01",
            "一定会到处都有\x01",
            "随便书写的笔记。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_637")

    label("loc_5AA")


    ChrTalk(    #19
        0xFE,
        (
            "佛莱迪那家伙，\x01",
            "回洛连特之后\x01",
            "不知道过得还好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "他虽然年轻，\x01",
            "却是相当有骨气的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "将来一定会\x01",
            "成为优秀的专业人士的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_637")

    TalkEnd(0xFE)
    Return()

    # Function_5_50E end

    def Function_6_63B(): pass

    label("Function_6_63B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-101240, 0, 100160, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, -102660, 0, 97700, 270)
    SetChrPos(0x11, -103650, 0, 99100, 180)
    SetChrPos(0x107, -98510, 0, 101000, 270)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x10,
        (
            "#100F艾莉卡，这配线是怎么回事。\x02\x03",

            "怎么看都是没用的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        (
            "#1456F这是应对噪音用的。\x02\x03",

            "这次非常精密，\x01",
            "需要下相当的工夫。\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_70(0x2, 0x1E)
    OP_73(0x2)

    def lambda_788():
        OP_8E(0xFE, 0xFFFE76D6, 0x0, 0x18A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_788)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 225, 400)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    Sleep(300)

    ChrTalk(    #24
        0x107,
        "#060F#5P哎，妈妈？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#1456F也就是说，\x01",
            "这里的导力压变动在这里被吸收……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "#100F唔唔，原来如此啊……\x02",
    )

    CloseMessageWindow()

    def lambda_841():
        OP_8E(0xFE, 0xFFFE6B50, 0x0, 0x18A88, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_841)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 180, 500)
    Sleep(300)

    ChrTalk(    #27
        0x107,
        "#0560F#3S#1P妈妈！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(900)

    def lambda_8D8():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_8D8)
    Sleep(100)

    def lambda_8EB():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_8EB)
    Sleep(300)

    ChrTalk(    #28
        0x11,
        (
            "#1454F#6P哎呀提妲。\x01",
            "你在这种地方干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        (
            "#560F#5P那、那个…………\x02\x03",

            "我是不是，\x01",
            "也能做些什么呢。\x02\x03",

            "我想为玲\x01",
            "做一些事情……\x02\x03",

            "#561F但是，\x01",
            "又不知道做什么才好……\x02",
        )
    )

    Jump("loc_9CE")

    label("loc_9CE")

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#1454F#6P？？？\x01",
            "虽然不太明白……\x02\x03",

            "#1450F不过你要是想帮忙，\x01",
            "就拜托你做一件事吧。\x02\x03",

            "其实还有一些\x01",
            "麻烦的工作没办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x107,
        (
            "#064F#5P咦…………？\x02\x03",

            "#061F嗯、嗯，好啊。\x01",
            "只要我能做到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        (
            "#1451F#6P其实呢，\x01",
            "虽然不是什么大不了的事……\x02\x03",

            "想麻烦你去\x01",
            "跟玛多克先生说一声，\x01",
            "准备一下我们的回国文件。\x02\x03",

            "#1450F你看，\x01",
            "我们的回国方式不是那么合法吧？\x01",
            "所以好像需要正式的文件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x107,
        "#064F#5P嗯、嗯…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        (
            "#1458F#6P丹对这个好像\x01",
            "特别担心的样子呢。\x02\x03",

            "#1456F……那么，之后就拜托你啦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BF6():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_BF6)
    Sleep(300)

    def lambda_C09():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_C09)
    Sleep(300)

    ChrTalk(    #35
        0x107,
        (
            "#560F#1P嗯、嗯…………\x02\x03",

            "………………………………\x02\x03",

            "#561F（我本来不是\x01",
            "  这个意思啦……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x107)

    ChrTalk(    #36
        0x107,
        (
            "#060F#1P（唉，算了。\x01",
            "  妈妈好像也很为难。）\x02\x03",

            "（赶快去办完吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 500)

    def lambda_D01():
        OP_8E(0xFE, 0xFFFE76D6, 0x0, 0x18A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_D01)
    WaitChrThread(0x107, 0x1)
    OP_70(0x2, 0x1E)
    OP_73(0x2)

    def lambda_D2B():
        OP_8E(0xFE, 0xFFFE7F32, 0x0, 0x18A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_D2B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_63B end

    SaveToFile()

Try(main)
