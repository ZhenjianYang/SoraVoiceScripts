from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3130   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3130.x',
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
        '皮克塞恩教区长',                       # 9
        '修女琪爱拉',                           # 10
        '莱恩',                                 # 11
        '艾妲',                                 # 12
        '玛多克工房长',                         # 13
        '目标用照相机',                         # 14
        '',                                     # 15
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT07/CH01450 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH02620 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01450P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH02620P._CP',             # 04
    )

    DeclNpc(
        X                   = 59010,
        Z                   = 1000,
        Y                   = 52150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 56310,
        Z                   = 1000,
        Y                   = 50360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 63750,
        Z                   = 0,
        Y                   = 45060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 59010,
        Z                   = 1000,
        Y                   = 50160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 59000,
        Z                   = 0,
        Y                   = 47000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_1F1",          # 01, 1
        "Function_2_1F2",          # 02, 2
        "Function_3_1F7",          # 03, 3
        "Function_4_38D",          # 04, 4
        "Function_5_4A9",          # 05, 5
        "Function_6_67E",          # 06, 6
        "Function_7_765",          # 07, 7
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D1")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)

    label("loc_1D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1F0")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_1F0")

    Return()

    # Function_0_1B6 end

    def Function_1_1F1(): pass

    label("Function_1_1F1")

    Return()

    # Function_1_1F1 end

    def Function_2_1F2(): pass

    label("Function_2_1F2")

    Call(0, 3)
    Return()

    # Function_2_1F2 end

    def Function_3_1F7(): pass

    label("Function_3_1F7")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 7)), scpexpr(EXPR_END)), "loc_25F")

    ChrTalk(    #0
        0x10,
        (
            "雾香好像还没有\x01",
            "和大家说过这事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "嗯，\x01",
            "是打算瞒着大家出发吗……\x02",
        )
    )

    Jump("loc_25B")

    label("loc_25B")

    CloseMessageWindow()
    Jump("loc_389")

    label("loc_25F")


    ChrTalk(    #2
        0x10,
        "哎呀，是阿加特啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "……雾香要回国的事\x01",
            "你听说了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 0)), scpexpr(EXPR_END)), "loc_2C9")

    ChrTalk(    #4
        0x106,
        "#050F啊啊，刚才听说了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FF")

    label("loc_2C9")


    ChrTalk(    #5
        0x106,
        (
            "#050F啊啊…………\x02\x03",

            "嘉恩那家伙\x01",
            "告诉过我了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF")


    ChrTalk(    #6
        0x10,
        "是吗…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "这座城市的居民，\x01",
            "多多少少\x01",
            "都有受过她照顾呢。\x02",
        )
    )

    Jump("loc_352")

    label("loc_352")

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "在她出发之前，\x01",
            "大家能为她做点什么就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F87)

    label("loc_389")

    TalkEnd(0x10)
    Return()

    # Function_3_1F7 end

    def Function_4_38D(): pass

    label("Function_4_38D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_4A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_412")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(500)

    ChrTalk(    #9
        0xFE,
        (
            "……这件事还是\x01",
            "暂时瞒着工房长吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "现在告诉他，\x01",
            "感觉好像有点残酷……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5")

    label("loc_412")


    ChrTalk(    #11
        0xFE,
        (
            "其实我昨天听到了\x01",
            "教区长和雾香小姐的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "雾香小姐好像要辞去游击士协会\x01",
            "接待的工作回共和国去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "……感觉会变得寂寞起来呢……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4A5")

    TalkEnd(0xFE)
    Return()

    # Function_4_38D end

    def Function_5_4A9(): pass

    label("Function_5_4A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_67A")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4C8"),
        (1, "loc_545"),
        (2, "loc_607"),
        (SWITCH_DEFAULT, "loc_67A"),
    )


    label("loc_4C8")


    ChrTalk(    #14
        0x14,
        (
            "#803F终于要进行\x01",
            "导力装甲的实验了……\x02\x03",

            "啊啊，空之女神啊……\x02\x03",

            "请保佑实验\x01",
            "平安结束……！\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67A")

    label("loc_545")


    ChrTalk(    #15
        0x14,
        (
            "#803F还、还有一件事\x01",
            "我有点在意。\x02\x03",

            "拉赛尔博士\x01",
            "似乎在和列曼自治州的\x01",
            "熟人取得联系。\x02\x03",

            "而且据说还约好\x01",
            "下次去见面……\x02\x03",

            "#805F啊啊，\x01",
            "拜托别再惹什么事了……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67A")

    label("loc_607")


    def lambda_60D():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_60D)
    Sleep(1000)

    ChrTalk(    #16
        0x14,
        (
            "#803F啊啊，空之女神，还有雾香小姐。\x01",
            "请你们守护蔡斯吧……！\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67A")

    label("loc_67A")

    TalkEnd(0xFE)
    Return()

    # Function_5_4A9 end

    def Function_6_67E(): pass

    label("Function_6_67E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_761")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6E1")

    ChrTalk(    #17
        0xFE,
        (
            "工房长最近\x01",
            "也经常来祈祷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "呵呵，\x01",
            "他的信念也觉醒了吗？\x02",
        )
    )

    Jump("loc_6DD")

    label("loc_6DD")

    CloseMessageWindow()
    Jump("loc_761")

    label("loc_6E1")


    ChrTalk(    #19
        0xFE,
        (
            "呼，\x01",
            "中午的祷告就到这里吧。\x02",
        )
    )

    Jump("loc_709")

    label("loc_709")

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "虽然这次又是\x01",
            "逃掉工作而来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "不过工房长也来了，\x01",
            "应该没关系吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_761")

    TalkEnd(0xFE)
    Return()

    # Function_6_67E end

    def Function_7_765(): pass

    label("Function_7_765")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(59900, 0, 49800, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 59000, 0, 47000, 0)
    OP_4A(0x14, 0)
    SetChrPos(0x107, 59000, 0, 37520, 0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7EA():
        OP_6D(59900, 0, 44300, 6000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_7EA)

    def lambda_802():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_802)
    FadeToBright(2000, 0)
    Sleep(4500)
    OP_22(0x6, 0x0, 0x64)

    def lambda_825():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_825)

    def lambda_837():
        OP_8E(0xFE, 0xE678, 0x0, 0xA988, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_837)
    Sleep(800)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x107, 0x1)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #22
        0x107,
        "#061F#12P啊，工房长叔叔！\x02",
    )

    CloseMessageWindow()

    def lambda_89E():
        OP_6D(60340, 0, 47520, 1300)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_89E)

    def lambda_8B6():
        OP_67(0, 5040, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8B6)

    def lambda_8CE():
        OP_8E(0xFE, 0xE678, 0x0, 0xB1BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_8CE)
    WaitChrThread(0x107, 0x1)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x107,
        "#064F#12P……工房长叔叔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x14,
        (
            "#803F#5P啊啊，空之女神啊。\x01",
            "请守护弱小的我们吧……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x14, 180, 500)
    Sleep(300)

    ChrTalk(    #25
        0x14,
        (
            "#802F#5P呀，你好，提妲。\x01",
            "怎么了……？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x14,
        (
            "#805F#5P难、难不成实验失败了，\x01",
            "释放出了有毒气体吗！？\x02\x03",

            "还、还是说这次是大爆炸，\x01",
            "把工房半边都炸飞了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x107,
        (
            "#561F#12P那、那个…………\x01",
            "对不起，工房长叔叔。\x02\x03",

            "爷爷和妈妈\x01",
            "总是给您添麻烦……\x02\x03",

            "#560F不过没关系。\x01",
            "今天还没发生任何事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x14,
        (
            "#802F#5P是、是吗……\x01",
            "#803F…………太好了……\x02\x03",

            "看来我对女神的祈祷\x01",
            "还是奏效了。\x02\x03",

            "#806F啊，\x01",
            "那就连明天的那份也一起祈祷吧……\x02",
        )
    )

    Jump("loc_B8F")

    label("loc_B8F")

    CloseMessageWindow()
    OP_8C(0x14, 0, 500)
    Sleep(500)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x107,
        (
            "#560F#12P那、那个，工房长叔叔。\x02\x03",

            "……其实我有点事\x01",
            "想拜托您……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14)
    Sleep(300)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x14, 180, 500)
    Sleep(300)

    ChrTalk(    #30
        0x14,
        "#802F#5P拜托，是吗……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x07\x05提妲说明了情况，\x01",
            "拜托工房长准备双亲的回国文件。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #32
        0x14,
        (
            "#801F#5P原来如此，\x01",
            "这次是从天而降的吗。\x02\x03",

            "难怪连提妲你\x01",
            "也会吃惊了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x14)
    Sleep(500)

    ChrTalk(    #33
        0x14,
        "#802F#3S#5P偷……偷渡…………！？\x02",
    )

    Sleep(50)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #34
        0x107,
        "#064F#12P啊，可能是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x14,
        (
            "#806F#5P啊哈哈，真伤脑筋啊。\x01",
            "要赶快申请许可证了……\x02\x03",

            "#800F提妲，\x01",
            "你能代替我祈祷吗。\x02\x03",

            "保佑这次发明\x01",
            "不要再出什么事……就这样！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x107,
        (
            "#065F#12P啊，好的。\x01",
            "我知道了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x14,
        "#800F#5P拜、拜托你了！\x02",
    )

    CloseMessageWindow()

    def lambda_E9F():

        label("loc_E9F")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_E9F")

    QueueWorkItem2(0x107, 2, lambda_E9F)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x14, 135, 500)

    def lambda_EC9():
        OP_8E(0xFE, 0xEA60, 0x0, 0xB3B0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_EC9)
    WaitChrThread(0x14, 0x1)

    def lambda_EE9():
        OP_8E(0xFE, 0xEA60, 0x0, 0x927C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_EE9)
    WaitChrThread(0x14, 0x1)
    Sleep(1000)

    ChrTalk(    #38
        0x107,
        "#062F#5P嗯……\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0x2)
    OP_8C(0x107, 0, 500)
    Sleep(300)
    OP_8E(0x107, 0xE678, 0x0, 0xB6D0, 0x4B0, 0x0)
    Sleep(1000)

    ChrTalk(    #39
        0x107,
        (
            "#563F#12P（保佑妈妈和爷爷\x01",
            "  不要乱来……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #40
        0x107,
        (
            "#063F#12P（……但是，\x01",
            "  我能做什么呢……）\x02\x03",

            "（我又不像\x01",
            "  艾丝蒂尔姐姐那样强……）\x02\x03",

            "（那个时候也是，\x01",
            "  什么话也没办法向玲传达……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #41
        0x107,
        (
            "#064F#12P（……对、对了！）\x02\x03",

            "#062F（我也去参加\x01",
            "  导力装甲的开发吧。）\x02\x03",

            "（要是有\x01",
            "  和帕蒂尔·玛蒂尔一样强的\x01",
            "  导力装甲……）\x02\x03",

            "（那么我说不定\x01",
            "  也能和玲\x01",
            "  好好对话了。）\x02\x03",

            "（好、好的……！\x01",
            "  去拜托妈妈试试吧！）\x02",
        )
    )

    Jump("loc_115F")

    label("loc_115F")

    CloseMessageWindow()
    OP_8C(0x107, 180, 600)

    def lambda_116D():
        OP_8E(0xFE, 0xE678, 0x0, 0x93F8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_116D)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3116   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_765 end

    SaveToFile()

Try(main)
