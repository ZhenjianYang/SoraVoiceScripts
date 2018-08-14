from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1111   ._SN',
        MapName             = 'Bose',
        Location            = 'T1111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '梅贝尔市长',                           # 9
        '莉拉',                                 # 10
        '萨拉',                                 # 11
        '管家门特斯',                           # 12
        '亚妮拉丝',                             # 13
        '目标用照相机',                         # 14
        '',                                     # 15
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
        'ED6_DT07/CH02360 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH02363 ._CH',             # 03
        'ED6_DT07/CH01560 ._CH',             # 04
        'ED6_DT27/CH03090 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02360P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH02363P._CP',             # 03
        'ED6_DT07/CH01560P._CP',             # 04
        'ED6_DT27/CH03090P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1BA",          # 01, 1
        "Function_2_1BB",          # 02, 2
        "Function_3_646",          # 03, 3
        "Function_4_6A1",          # 04, 4
        "Function_5_714",          # 05, 5
        "Function_6_782",          # 06, 6
        "Function_7_7F8",          # 07, 7
        "Function_8_87D",          # 08, 8
        "Function_9_29DD",         # 09, 9
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_1B9")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_1B9")

    Return()

    # Function_0_19A end

    def Function_1_1BA(): pass

    label("Function_1_1BA")

    Return()

    # Function_1_1BA end

    def Function_2_1BB(): pass

    label("Function_2_1BB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, -120710, 200, 68600, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -120260, 0, 65470, 0)
    OP_6D(-121830, 0, 68600, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(315000, 0)
    OP_6E(322, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x13,
        (
            "#6P那么……\x02\x03",

            "……你想问莉拉的情况？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#610F#2P有没有什么值得注意的地方？\x02\x03",

            "比如……\x01",
            "和没见过的人在一起之类的。\x02",
        )
    )

    Jump("loc_2FA")

    label("loc_2FA")

    CloseMessageWindow()

    ChrTalk(    #2
        0x13,
        (
            "#6P唔，\x01",
            "这个的话我有印象。\x02\x03",

            "那是前几天，\x01",
            "我拜访特里诺先生家的时候……\x02\x03",

            "我亲眼看见\x01",
            "莉拉和一个陌生的男人\x01",
            "并肩走在一起。\x02",
        )
    )

    Jump("loc_381")

    label("loc_381")

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "#610F#2P那，他是怎样的人呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x13,
        (
            "#6P好像是某家店的侍应生……\x01",
            "大概就是这种感觉吧。\x02\x03",

            "感觉是一位\x01",
            "正直的好青年。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, -62700, -3000, 65960, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -64050, -3000, 65990, 90)
    SetChrFlags(0x13, 0x80)
    OP_6D(-64500, -3000, 66970, 0)
    OP_67(0, 5580, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(275, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #5
        0x12,
        (
            "#5P啊，这么说来……\x02\x03",

            "以前那个人\x01",
            "送莉拉回过家哦。\x02\x03",

            "还有，\x01",
            "两个人还一起买过东西……\x02",
        )
    )

    Jump("loc_501")

    label("loc_501")

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#610F是吗……\x02\x03",

            "看来不会有错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "#5P啊……\x01",
            "难、难不成？\x02\x03",

            "那、那个人\x01",
            "莫非就是莉拉的？\x02",
        )
    )

    Jump("loc_575")

    label("loc_575")

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#610F萨拉……\x01",
            "现在只要默默支持她就好了。\x02\x03",

            "我也打算这样做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        (
            "#5P好、好的……我明白了。\x02\x03",

            "哎～\x01",
            "不过那个莉拉竟然……\x02\x03",

            "呼，\x01",
            "真是世事难料啊～。\x02",
        )
    )

    Jump("loc_628")

    label("loc_628")

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1BB end

    def Function_3_646(): pass

    label("Function_3_646")

    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_656():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_656)

    def lambda_668():
        OP_8E(0xFE, 0xFFFE32E8, 0x0, 0xFB0D, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_668)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFE2BEA, 0x0, 0x1007C, 0x5DC, 0x0)
    Return()

    # Function_3_646 end

    def Function_4_6A1(): pass

    label("Function_4_6A1")


    def lambda_6A7():
        OP_8E(0xFE, 0xFFFE32E8, 0x0, 0xFB0D, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A7)
    WaitChrThread(0xFE, 0x2)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)

    def lambda_6D8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D8)

    def lambda_6EA():
        OP_8E(0xFE, 0xFFFE33EC, 0x0, 0xF424, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6EA)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_6A1 end

    def Function_5_714(): pass

    label("Function_5_714")

    OP_8C(0xFE, 90, 400)
    OP_8F(0xFE, 0xFFFE33B0, 0x0, 0xFBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)

    def lambda_746():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_746)

    def lambda_758():
        OP_8E(0xFE, 0xFFFE336A, 0x0, 0xF42E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_758)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_5_714 end

    def Function_6_782(): pass

    label("Function_6_782")

    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_792():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_792)

    def lambda_7A4():
        OP_8E(0xFE, 0xFFFE33EC, 0x0, 0xFC07, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7A4)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFE2E24, 0x0, 0xFC07, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE2A3C, 0x0, 0xFFEF, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_782 end

    def Function_7_7F8(): pass

    label("Function_7_7F8")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_810():
        OP_8E(0xFE, 0xFFFE32E8, 0x0, 0xFB0D, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_810)
    WaitChrThread(0xFE, 0x2)
    OP_8C(0xFE, 180, 500)
    Sleep(200)
    OP_22(0x6, 0x0, 0x64)

    def lambda_841():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_841)

    def lambda_853():
        OP_8E(0xFE, 0xFFFE33EC, 0x0, 0xF424, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_853)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_7F8 end

    def Function_8_87D(): pass

    label("Function_8_87D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -120000, 0, 65800, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, -120710, 200, 68600, 180)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrPos(0x13, -115800, 0, 60820, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -120510, 0, 66280, 0)
    OP_6D(-122340, 0, 69030, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(322, 0)
    FadeToBright(2000, 0)
    OP_6B(2550, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #10
        0x10,
        (
            "#615F#11P原来如此……\x01",
            "是『川蝉亭』的雷纳德先生啊。\x02\x03",

            "#610F莉拉真是的，\x01",
            "什么时候认识他的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x14,
        (
            "#814F#6P咦，\x01",
            "市长也知道\x01",
            "雷纳德先生的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#610F#11P虽然没有直接见过面，\x01",
            "但名字还是知道的。\x02\x03",

            "说到湖畔的『川蝉亭』，\x01",
            "那可是最近突然热门起来的知名旅馆嘛。\x02\x03",

            "#615F这几年似乎收益颇丰，\x01",
            "作为投资对象可是\x01",
            "无可挑剔的优秀呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x14,
        (
            "#816F#6P嗯、嗯嗯……\x01",
            "特里诺先生也这么说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#615F#11P看了相关的报告书，\x01",
            "他交涉的手段也十分\x01",
            "正规和适当呢……\x02\x03",

            "#611F对他本人的评价\x01",
            "应该是相当优秀吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        (
            "#819F#6P嗯嗯，那是当然。\x02\x03",

            "#1310F他妹妹索菲娜小姐\x01",
            "也是非常大方开朗的人。\x02\x03",

            "#811F就算莉拉小姐嫁过去\x01",
            "也不必担心吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#611F#11P这、这实在是\x01",
            "有点言之过早……\x02\x03",

            "#618F不过，是啊……\x01",
            "说不定什么时候\x01",
            "就会发展成这样呢。\x02\x03",

            "#617F呵呵……虽然开心，\x01",
            "但另一方面还是有点寂寞呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        "#1314F#6P市长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "#615F#11P……总而言之，\x01",
            "调查辛苦你了。\x02\x03",

            "#611F我已经知道了\x01",
            "莉拉的确有\x01",
            "看男人的眼光……\x02\x03",

            "之后就耐心等待\x01",
            "本人的报告了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        (
            "#819F#6P呵呵，是啊。\x01",
            "我也觉得这样不错。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x71, 0x0, 0x64)
    Sleep(800)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_DE1():
        OP_6D(-121020, 0, 68070, 1200)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_DE1)

    def lambda_DF9():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_DF9)
    Sleep(200)
    SetChrSubChip(0x10, 1)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -115800, 0, 60820, 0)

    NpcTalk(    #20
        0x11,
        "莉拉的声音",
        (
            "#2P……小姐，\x01",
            "我是莉拉。\x02\x03",

            "能不能\x01",
            "占用您一点时间？\x02",
        )
    )

    Jump("loc_E8E")

    label("loc_E8E")

    CloseMessageWindow()

    ChrTalk(    #21
        0x14,
        "#814F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#617F#5P呵呵……\x01",
            "真是说到就到呢。\x02\x03",

            "#611F难不成……\x01",
            "她终于打算\x01",
            "跟我说明情况了吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x10, 500)
    Sleep(300)

    ChrTalk(    #23
        0x14,
        (
            "#819F#6P呵呵……\x01",
            "很有可能呢。\x02\x03",

            "#1310F嗯，\x01",
            "那我就不打扰你们，\x01",
            "先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10, 0)
    Sleep(200)

    ChrTalk(    #24
        0x10,
        (
            "#615F#11P不……\x01",
            "如果愿意的话，\x01",
            "希望你也留下来。\x02\x03",

            "#610F如果她要说这件事的话，\x01",
            "我也不打算隐瞒\x01",
            "调查她的事情的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x14,
        (
            "#814F#6P啊……\x02\x03",

            "#816F我明白了。\x01",
            "既然这样的话……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #26
        0x11,
        "莉拉的声音",
        "#2P……小姐？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10, 1)
    Sleep(200)

    ChrTalk(    #27
        0x10,
        (
            "#610F#5P啊，对不起。\x02\x03",

            "……可以了，莉拉。\x01",
            "你进来吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x11,
        "莉拉的声音",
        "#2P打扰了……\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_10EF():
        OP_6D(-121830, 0, 68600, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_10EF)
    SetChrPos(0x11, -117780, 0, 62500, 0)
    OP_43(0x11, 0x0, 0x0, 0x3)
    Sleep(200)

    def lambda_1124():

        label("loc_1124")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_1124")

    QueueWorkItem2(0x14, 2, lambda_1124)
    Sleep(300)

    def lambda_113A():
        OP_8F(0xFE, 0xFFFE2370, 0x0, 0x101E4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_113A)
    Sleep(1500)
    SetChrSubChip(0x10, 0)
    WaitChrThread(0x11, 0x0)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x14, 400)
    Sleep(300)

    ChrTalk(    #29
        0x11,
        (
            "#622F#12P啊……亚妮拉丝小姐？\x02\x03",

            "#623F非常抱歉。\x01",
            "没想到你们正在谈话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x14,
        (
            "#819F#5P啊，\x01",
            "请别介意我的事。\x02\x03",

            "#816F我只是来\x01",
            "向市长汇报委托的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        "#622F#12P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "#615F#11P别管这个了……\x01",
            "什么事，莉拉？\x02\x03",

            "#610F难不成……\x01",
            "是有什么事要和我商量吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #33
        0x11,
        (
            "#620F#6P商量……\x01",
            "倒是不太一样。\x02\x03",

            "我是有件事\x01",
            "想和小姐谈一谈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "#617F#11P哎、哎呀……\x01",
            "是什么事呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        (
            "#621F#6P嗯，\x01",
            "其实是关于湖畔的『川蝉亭』的事……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x10,
        "#610F#11P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x14,
        "#816F#5P果然是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x11,
        "#622F#6P……小姐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#617F#11P哼哼……\x02\x03",

            "#611F莉拉，\x01",
            "你以为我什么也没发觉吗？\x02\x03",

            "我已经全都知道了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0x11,
        "#625F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#615F#11P虽然对你有点抱歉，\x01",
            "其实我拜托亚妮拉丝小姐\x01",
            "已经帮我调查过了。\x02\x03",

            "因为最近你的样子\x01",
            "有点奇怪……\x02\x03",

            "#618F……对不起，莉拉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "#621F#6P是这样吗……\x02\x03",

            "#620F哪里，\x01",
            "是我做出让您误解的事，\x01",
            "该我道歉才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#613F#11P对、对了，那个……\x02\x03",

            "#617F雷纳德先生\x01",
            "对你还好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x14,
        (
            "#1317F#5P（市、市长……）\x02\x03",

            "#819F（再怎么说\x01",
            "  这也太直接了吧……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        (
            "#622F#6P嗯，是个很亲切的人……\x01",
            "他怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "#618F#11P不、不是这个意思……\x01",
            "真是让人心急啊。\x02\x03",

            "#612F你应该还有……\x01",
            "还有别的什么话要说吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#623F#6P是……\x02\x03",

            "#621F那就商量一下\x01",
            "关于具体日程的事……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(300)

    ChrTalk(    #48
        0x14,
        "#1317F#5P#4S咦咦！？\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "#613F#11P日、日程是指……\x02\x03",

            "#614F#3S难道已经进展到这一步了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x11,
        (
            "#620F#6P是的，本来打算一直保密到最后\x01",
            "给小姐一个惊喜的。\x02\x03",

            "在研究了日程表之后，\x01",
            "已经设定好了大致的日期……\x02\x03",

            "#621F……我就这样\x01",
            "接着说可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "#618F#11P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_44(0x14, 0xFF)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x14, 0x10, 500)
    Sleep(400)
    TurnDirection(0x14, 0x11, 500)
    Sleep(200)

    ChrTalk(    #52
        0x14,
        "#819F#5P哎，这个，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x11,
        "#622F#6P……小姐？\x02",
    )

    CloseMessageWindow()
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #54
        0x10,
        "#618F#11P#60W#1S……莉拉………笨…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        "#625F#6P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #56
        0x10,
        "#616F#11P#5S莉拉大笨蛋！\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        "#628F#6P#3S！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#618F#11P虽、虽然\x01",
            "不是不能理解\x01",
            "想让我大吃一惊的心情……！\x02\x03",

            "#619F就算如此……\x01",
            "没想到都进展到\x01",
            "这种地步了……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        "#625F#6P那个，小姐……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#616F#11P莉拉的确\x01",
            "可以有自己的隐私，\x01",
            "这是理所应当的！\x02\x03",

            "但是，这么重要的事\x01",
            "至今为止一点商量都没有\x01",
            "就决定了，实在是……！\x02\x03",

            "#619F我、我和你的关系\x01",
            "就只是这种程度而已吗……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        "#622F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "#618F#11P而、而且……\x01",
            "你们两个，\x01",
            "开始交往才一个月而已吧！？\x02\x03",

            "这实在是……\x01",
            "再怎么说也太快了吧！\x02\x03",

            "#619F莉拉，你明白吗！？\x02\x03",

            "对女孩子来说……\x01",
            "这可是一生中最重要的事啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x14,
        (
            "#1317F#5P市、市长……\x01",
            "您冷静点……！\x02\x03",

            "莉、莉拉小姐\x01",
            "说不定也是经过很多烦恼\x01",
            "才决定的……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x11,
        (
            "#627F#6P那个……\x02\x03",

            "#625F难不成，\x01",
            "这里面有什么重大的误会？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x14,
        "#814F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        "#618F#11P#40W……莉……拉…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "#621F#6P……我说的日程\x01",
            "是关于小姐的休假。\x02\x03",

            "最近，您一直忙于工作，\x01",
            "也该好好休息一下了，\x01",
            "所以我就擅自进行了安排。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x14)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #68
        0x14,
        "#1317F#1P#3S哎！？\x02",
    )


    ChrTalk(    #69
        0x10,
        "#613F#2P#3S呃！？\x02",
    )

    OP_56(0x1)
    OP_59()
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #70
        0x11,
        (
            "#627F#6P最近很热门的『川蝉亭』，\x01",
            "以前小姐曾经说过\x01",
            "想要去一次的……\x02\x03",

            "于是就趁着雷纳德先生\x01",
            "来柏斯超市购物的时候\x01",
            "和他商量这件事……\x02\x03",

            "#623F……看来造成了\x01",
            "重大的误解呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        "#613F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x14,
        "#819F#5P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#625F#6P呼……\x01",
            "真拿小姐没办法呢。\x02\x03",

            "#624F首先，\x01",
            "如果是这种事情的话，\x01",
            "比起我来小姐应该更优先考虑吧。\x02\x03",

            "来说媒的人\x01",
            "已经多如繁星了，\x01",
            "却总是因为工作无法顾及……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "#618F#11P呜，那个是……\x01",
            "因为太忙所以就……\x02\x03",

            "#617F话、话说回来……\x01",
            "你和雷纳德先生真的什么也没有？\x02\x03",

            "谈了这么多次，\x01",
            "没有产生好感之类的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "#623F#6P他确实是个\x01",
            "亲切又令人\x01",
            "产生好感的人……\x02\x03",

            "但是我从来没有\x01",
            "把他作为那种对象来考虑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#612F#11P为、为什么？\x02\x03",

            "那个，你也是年轻女孩，\x01",
            "如果没有这种经验……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        (
            "#621F#6P……趁此机会\x01",
            "我就说清楚好了。\x02\x03",

            "对我莉拉来说，\x01",
            "小姐的幸福是比任何事都优先的。\x02\x03",

            "这才是我无可替代的\x01",
            "喜悦和生存意义。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x10,
        "#613F#11P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x11,
        (
            "#621F#6P至少在小姐的亲事\x01",
            "定下来之前，我丝毫没有\x01",
            "考虑自己对象的念头。\x02\x03",

            "#623F……所以小姐。\x02\x03",

            "如果要担心莉拉的话，\x01",
            "请先考虑一下\x01",
            "自己的幸福吧。\x02\x03",

            "#627F就算不提这件事，\x01",
            "最近小姐也实在太过操劳，\x01",
            "太不爱惜自己了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        (
            "#616F#11P啊啊真是的，我知道啦！\x02\x03",

            "相、相亲就不提了，\x01",
            "我会多少照顾一下自己的！\x02\x03",

            "日程什么的都交给你，\x01",
            "休假的事你就继续安排好了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        (
            "#621F#6P呵呵，我明白了。\x02\x03",

            "#620F那么我就先退下了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x14, 400)
    Sleep(300)

    ChrTalk(    #82
        0x11,
        "#621F#12P亚妮拉丝小姐，失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x14,
        "#814F#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 135, 400)

    def lambda_24BD():

        label("loc_24BD")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_24BD")

    QueueWorkItem2(0x14, 2, lambda_24BD)

    def lambda_24CE():
        OP_6D(-121430, 0, 68300, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_24CE)
    OP_43(0x11, 0x0, 0x0, 0x4)
    Sleep(1500)
    SetChrSubChip(0x10, 1)
    WaitChrThread(0x11, 0x0)
    OP_44(0x14, 0x2)
    Sleep(1000)

    def lambda_2505():
        OP_6D(-122340, 0, 69030, 1200)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2505)
    OP_44(0x14, 0xFF)
    TurnDirection(0x14, 0x10, 400)
    WaitChrThread(0x10, 0x1)
    Sleep(300)

    ChrTalk(    #84
        0x14,
        (
            "#1317F#5P呃，嗯……\x02\x03",

            "#1316F对不起……\x01",
            "看来是我调查不足呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10, 0)
    Sleep(300)

    ChrTalk(    #85
        0x10,
        (
            "#617F#11P哪、哪里……\x01",
            "亚妮拉丝小姐的报告书\x01",
            "完全没有任何问题。\x02\x03",

            "#618F要说有问题，\x01",
            "都怪我胡思乱想……\x02\x03",

            "唉……\x01",
            "又被莉拉说教了。\x02",
        )
    )

    Jump("loc_2628")

    label("loc_2628")

    CloseMessageWindow()

    ChrTalk(    #86
        0x14,
        (
            "#819F#5P啊哈哈……别难过了。\x02\x03",

            "#1314F……不过……\x01",
            "我好羡慕你们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10,
        "#613F#11P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x14,
        (
            "#1310F#5P嗯，\x01",
            "那么我也先告辞了。\x02\x03",

            "#819F承蒙款待了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 135, 500)

    def lambda_26EE():
        OP_6D(-121430, 0, 68300, 1200)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_26EE)
    OP_43(0x14, 0x0, 0x0, 0x7)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x9)

    ChrTalk(    #89 op#A
        0x10,
        "#613F#5P#25A啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x0)
    Sleep(300)

    def lambda_2742():
        OP_6D(-122700, 0, 70040, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2742)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #90
        0x10,
        (
            "#618F#5P哎、哎呀……\x01",
            "亚妮拉丝小姐真是的……\x02\x03",

            "#615F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(300)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #91
        0x10,
        (
            "#617F#11P呵呵……话说回来。\x02\x03",

            "知道真相之后\x01",
            "竟然感到如此安心，\x01",
            "我也真是不成熟啊……\x02\x03",

            "#618F唉……\x01",
            "我到什么时候\x01",
            "才能不再依靠莉拉呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2886():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2886)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #92
        "\x07\x00Episode『操之过急的父母心』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D0")
    Sleep(1000)
    OP_28(0xB, 0x4, 0x10)
    OP_28(0xB, 0x4, 0x20)
    OP_3E(0x1EF, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #93
        "\x07\x00得到了\x1F\xEF\x01\x07\x00。\x02",
    )

    Jump("loc_2947")

    label("loc_2947")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2988")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x44)"), scpexpr(EXPR_END)), "loc_2962")
    Jump("loc_2988")

    label("loc_2962")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #94
        "\x1F\xEF\x01\x07\x00的制作方法已经记下了。\x02",
    )

    CloseMessageWindow()

    label("loc_2988")

    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(50000)
    AddMira(50000)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #95
        "\x07\x00得到了\x07\x02１０００００米拉\x07\x00。\x02",
    )

    Jump("loc_29C4")

    label("loc_29C4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_29D0")

    OP_A2(0x2506)
    NewScene("ED6_DT21/U2512   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_8_87D end

    def Function_9_29DD(): pass

    label("Function_9_29DD")

    SetChrSubChip(0x10, 0)
    Sleep(1000)
    SetChrSubChip(0x10, 1)
    Return()

    # Function_9_29DD end

    SaveToFile()

Try(main)
