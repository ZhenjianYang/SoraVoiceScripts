from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1110   ._SN',
        MapName             = 'Bose',
        Location            = 'T1110.x',
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
        '莫德娜',                               # 9
        '特里诺',                               # 10
        '亚妮拉丝',                             # 11
        '目标用照相机',                         # 12
        '',                                     # 13
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01480 ._CH',             # 04
        'ED6_DT07/CH01220 ._CH',             # 05
        'ED6_DT07/CH01010 ._CH',             # 06
        'ED6_DT07/CH01000 ._CH',             # 07
        'ED6_DT07/CH01183 ._CH',             # 08
        'ED6_DT07/CH01230 ._CH',             # 09
        'ED6_DT07/CH01200 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01143 ._CH',             # 0C
        'ED6_DT27/CH03090 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01480P._CP',             # 04
        'ED6_DT07/CH01220P._CP',             # 05
        'ED6_DT07/CH01010P._CP',             # 06
        'ED6_DT07/CH01000P._CP',             # 07
        'ED6_DT07/CH01183P._CP',             # 08
        'ED6_DT07/CH01230P._CP',             # 09
        'ED6_DT07/CH01200P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01143P._CP',             # 0C
        'ED6_DT27/CH03090P._CP',             # 0D
    )

    DeclNpc(
        X                   = -18730,
        Z                   = 70,
        Y                   = 33060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -21100,
        Z                   = 0,
        Y                   = 33600,
        Direction           = 180,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        "Function_1_1C3",          # 01, 1
        "Function_2_1C4",          # 02, 2
        "Function_3_1C9",          # 03, 3
        "Function_4_1ED",          # 04, 4
        "Function_5_211",          # 05, 5
        "Function_6_2AE",          # 06, 6
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1C2")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_1C2")

    Return()

    # Function_0_19A end

    def Function_1_1C3(): pass

    label("Function_1_1C3")

    Return()

    # Function_1_1C3 end

    def Function_2_1C4(): pass

    label("Function_2_1C4")

    Call(6, 2)
    Return()

    # Function_2_1C4 end

    def Function_3_1C9(): pass

    label("Function_3_1C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EC")
    OP_8D(0xFE, 26200, 71400, 28400, 72600, 2000)
    Jump("Function_3_1C9")

    label("loc_1EC")

    Return()

    # Function_3_1C9 end

    def Function_4_1ED(): pass

    label("Function_4_1ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_210")
    OP_8D(0xFE, 17430, 68790, 23880, 64870, 1500)
    Jump("Function_4_1ED")

    label("loc_210")

    Return()

    # Function_4_1ED end

    def Function_5_211(): pass

    label("Function_5_211")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2AD")
    OP_8E(0xFE, 0xFFFFA6F0, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFAB8C, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFADE4, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAEC0, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFADE4, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAB8C, 0x0, 0x11B34, 0x7D0, 0x0)
    Jump("Function_5_211")

    label("loc_2AD")

    Return()

    # Function_5_211 end

    def Function_6_2AE(): pass

    label("Function_6_2AE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-19160, 0, 34000, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -20640, 0, 31700, 0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#A
        "\x07\x00#4S#15A证言③\x18\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x10,
        (
            "#11P最近，\x01",
            "和市长家的莉拉小姐在一起的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#11P啊啊，\x01",
            "这么说来我和老公一起\x01",
            "去超市的时候看到过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "#11P两个人好像\x01",
            "在一起挑选特产之类的商品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        "#5P呵呵，我也记得呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x11,
        (
            "#5P那可真是\x01",
            "亲密无间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "#5P让人觉得\x01",
            "简直像新婚夫妇一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        "#814F#12P已、已经这么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "#11P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#11P这人说话\x01",
            "总是很夸张，\x01",
            "不用太在意啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#5P呵呵，\x01",
            "这种事说夸张一点比较有趣嘛。\x02",
        )
    )

    Jump("loc_54D")

    label("loc_54D")

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        "#819F#12P啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#11P不过，\x01",
            "我的确记得见过那个男人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#11P唔，叫什么来着……\x01",
            "你记得吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#5P说什么傻话，当然记得了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#5P我啊，\x01",
            "只要打过交道的人都不会忘记的哦。\x02",
        )
    )

    Jump("loc_635")

    label("loc_635")

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#5P那个人……\x01",
            "应该是叫做雷纳德吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #17
        0x12,
        (
            "#814F#12P说到雷纳德先生……\x02\x03",

            "#1310F难不成，是那个『川蝉亭』的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#5P……怎么，原来你知道啊。\x01",
            "真没意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12,
        (
            "#819F#12P啊哈哈，\x01",
            "我经常因为工作去那个旅馆，\x01",
            "所以至少知道长相和名字……\x02\x03",

            "#816F不过特里诺先生，\x01",
            "你是不是和雷纳德先生有私交啊。\x02\x03",

            "……他是怎样的人\x01",
            "能不能告诉我呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#5P这倒没问题……\x01",
            "不过接下来要收情报费哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        "#1317F#12P#3S呃。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#11P哎～，老公啊！\x01",
            "别开玩笑啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#11P这可是一直\x01",
            "关照我们的游击士哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#5P哇哈哈，抱歉抱歉。\x01",
            "一不小心老毛病又犯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x12,
        "#819F#12P啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "#5P说起来啊，\x01",
            "雷纳德可是非常正直的人……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)

    def lambda_911():
        OP_6B(3120, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_911)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    SetMapFlags(0x2000000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_2AE end

    SaveToFile()

Try(main)
