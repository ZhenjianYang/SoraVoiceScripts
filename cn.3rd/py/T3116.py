from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3116   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3116.x',
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
        '加鲁诺',                               # 11
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
        'ED6_DT07/CH01190 ._CH',             # 00
        'ED6_DT07/CH02020 ._CH',             # 01
        'ED6_DT07/CH00060 ._CH',             # 02
        'ED6_DT27/CH03970 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01190P._CP',             # 00
        'ED6_DT07/CH02020P._CP',             # 01
        'ED6_DT07/CH00060P._CP',             # 02
        'ED6_DT27/CH03970P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = 3410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
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
        "Function_0_14A",          # 00, 0
        "Function_1_17B",          # 01, 1
        "Function_2_17C",          # 02, 2
        "Function_3_2A0",          # 03, 3
        "Function_4_136F",         # 04, 4
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B")
    ClearChrFlags(0x12, 0x80)

    label("loc_15B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_17A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_17A")

    Return()

    # Function_0_14A end

    def Function_1_17B(): pass

    label("Function_1_17B")

    Return()

    # Function_1_17B end

    def Function_2_17C(): pass

    label("Function_2_17C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_29C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_209")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #0
        0xFE,
        (
            "唔唔唔，\x01",
            "这里到底是削减还是不削减呢……\x02",
        )
    )

    Jump("loc_1CE")

    label("loc_1CE")

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "但是不再控制一点制造成本\x01",
            "会被帝国制造的领先……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C")

    label("loc_209")


    ChrTalk(    #2
        0xFE,
        "咦，你找艾莉卡博士？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "不，今天没看到呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "这里经常\x01",
            "会被器材堆满…………\x02",
        )
    )

    Jump("loc_26F")

    label("loc_26F")

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "难道又有新发明什么的\x01",
            "要完成了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_29C")

    TalkEnd(0xFE)
    Return()

    # Function_2_17C end

    def Function_3_2A0(): pass

    label("Function_3_2A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1280, 0, 12800, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -30, 0, 12840, 180)
    SetChrPos(0x11, -360, 0, 10320, 0)
    SetChrFlags(0x107, 0x4)
    SetChrPos(0x107, -2800, 0, 3260, 0)
    OP_22(0xE0, 0x1, 0x64)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_71(0x2002, 0x0)
    ExitThread()
    OP_70(0x1, 0x3)
    OP_70(0x2, 0x3)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x10,
        (
            "#101F#5P这个工作机是新型的，\x01",
            "可以以原来的十分之一精度\x01",
            "进行加工。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x11,
        (
            "#1457F#12P啧，\x01",
            "居然有这种东西……\x02\x03",

            "#1456F看来有必要\x01",
            "重新检讨基础设计啊！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #8
        0x107,
        (
            "#560F#1P啊，妈妈！\x02\x03",

            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x107, 0x4)
    SetChrPos(0x107, -360, 0, 3120, 0)

    def lambda_462():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x2256, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_462)
    Sleep(100)
    OP_22(0x6D, 0x0, 0x64)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    ChrTalk(    #9
        0x11,
        (
            "#1450F#5P哎呀，提妲。\x02\x03",

            "你那边顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x107,
        (
            "#061F#12P嗯。\x01",
            "回国文件那边没问题。\x02\x03",

            "工房长叔叔\x01",
            "说会马上准备好的。\x02\x03",

            "#560F对了，妈妈……\x02\x03",

            "我也想参加\x01",
            "导力装甲的开发。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 180, 500)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_23(0xE0)
    OP_22(0x9A, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #11
        0x11,
        "#1454F#5P提妲……？\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x4)

    ChrTalk(    #12
        0x107,
        (
            "#063F#12P嗯，那个……\x01",
            "虽然我没写在信里……\x02\x03",

            "其实我\x01",
            "曾经和玲在一起\x01",
            "待过一段时间……\x02\x03",

            "#062F玲虽然\x01",
            "加入了『结社』，\x01",
            "但她还是我的朋友。\x02",
        )
    )

    Jump("loc_662")

    label("loc_662")

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#1452F#5P玲………………\x02\x01",

            "#1457F我就觉得\x01",
            "好像在哪儿听过…………\x02\x03",

            "#1453F是帕蒂尔·玛蒂尔的操纵者吧。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x3)

    ChrTalk(    #14
        0x10,
        (
            "#100F#5P啊，艾莉卡。\x01",
            "让我来补充吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 500)
    Sleep(300)

    ChrTalk(    #15
        0x11,
        "#1830F#11P补充？\x02",
    )

    CloseMessageWindow()

    def lambda_746():
        OP_6D(-1660, -120, 12880, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_746)

    def lambda_75E():
        OP_67(0, 4320, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_75E)

    def lambda_776():
        OP_6C(36000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_776)

    def lambda_786():

        label("loc_786")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_786")

    QueueWorkItem2(0x107, 2, lambda_786)

    def lambda_797():
        OP_8E(0xFE, 0xFFFFF3BC, 0x0, 0x2878, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_797)
    WaitChrThread(0x11, 0x1)

    def lambda_7B7():
        OP_8E(0xFE, 0xFFFFF3BC, 0x0, 0x2DF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7B7)
    WaitChrThread(0x11, 0x1)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_22(0x8F, 0x0, 0x64)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x4)

    def lambda_809():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_809)

    def lambda_823():
        OP_95(0xFE, 0x0, 0x12C, 0x0, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_823)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    OP_44(0x107, 0x2)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_861():
        OP_8E(0xFE, 0xFFFFF358, 0x0, 0x2580, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_861)
    WaitChrThread(0x107, 0x1)

    def lambda_881():
        OP_8E(0xFE, 0xFFFFF358, 0x0, 0x26AC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_881)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    ChrTalk(    #16
        0x107,
        (
            "#065F妈、妈妈！？\x01",
            "那个…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#1457F#6P这到底是怎么回事呢。\x01",
            "阿尔巴特·拉赛尔……\x02\x03",

            "提妲居然和\x01",
            "『结社』的成员在一起……？\x02\x03",

            "#1459F这种事，\x01",
            "资料上没有写啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "#104F#5P啊～那是～……\x02\x03",

            "实在很难写出来嘛，\x01",
            "这种事……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x20)

    def lambda_9B6():
        OP_8E(0xFE, 0xFFFFF3BC, 0x0, 0x3110, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9B6)

    def lambda_9D1():
        OP_8F(0xFE, 0xFFFFF380, 0x12C, 0x3318, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9D1)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    ClearChrFlags(0x10, 0x20)

    ChrTalk(    #19
        0x11,
        (
            "#1459F#6P不是这个意思。\x02\x03",

            "你居然让提妲\x01",
            "置身于如此危险境地……\x02\x03",

            "#1830F#3S你这混帐，\x01",
            "到底是怎么对待你可爱的孙女的啊！！#2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x107,
        (
            "#062F妈、妈妈！\x01",
            "让我也参与开发吧！\x02\x03",

            "虽然我力量微薄，\x01",
            "但是还是想和\x01",
            "玲好好谈谈。\x02\x03",

            "用这个导力装甲\x01",
            "就可以对抗\x01",
            "帕蒂尔·玛蒂尔吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #21
        0x107,
        (
            "#068F我、我也\x01",
            "想要艾丝蒂尔姐姐\x01",
            "那样的力量……！\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_20(0xBB8)
    OP_44(0x10, 0x2)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #22
        0x11,
        "#1453F#5P…………提妲？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x4)

    def lambda_BCC():
        OP_96(0xFE, 0xFFFFF31C, 0x0, 0x337C, 0xA, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BCC)
    WaitChrThread(0x10, 0x1)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x8E, 0x0, 0x32)
    OP_22(0xD1, 0x0, 0x64)
    Sleep(300)
    TurnDirection(0x11, 0x107, 500)
    Sleep(300)

    def lambda_C1B():
        OP_8E(0xFE, 0xFFFFF3BC, 0x0, 0x2F1C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C1B)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #23
        0x11,
        (
            "#1452F#5P难不成你…………\x02\x03",

            "想用导力装甲，\x01",
            "和帕蒂尔·玛蒂尔作战？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x107,
        (
            "#564F#12P咦…………？\x02\x03",

            "不、不是那个意思，\x01",
            "我是…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#1457F#5P…………提妲。\x02\x03",

            "你明白制造导力装甲\x01",
            "是怎么一回事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x107,
        (
            "#064F#12P咦…………嗯、嗯。\x02\x03",

            "#560F虽然只是瞄了一眼，\x01",
            "不过应该是双足步行型……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        (
            "#1453F#5P不是说这个。\x02\x03",

            "导力装甲是兵器。\x01",
            "就算怎么美化也不会改变。\x02\x03",

            "#1452F说白了，\x01",
            "就是伤人的道具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x107,
        (
            "#063F#12P但、但是…………\x02\x03",

            "妈妈也不是为了这个\x01",
            "才制造的吧……？\x02\x03",

            "警备飞艇也是\x01",
            "为了保卫利贝尔而存在的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        (
            "#1457F#5P『为了什么』并不重要。\x02\x03",

            "实际使用兵器的\x01",
            "也不是我们。\x02\x03",

            "#1453F自己制造的机械，\x01",
            "会为许多人带来悲伤。\x02\x03",

            "#1452F提妲，\x01",
            "你想过这种事吗？\x02\x03",

            "即使如此也还是想要得到力量吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x107,
        "#065F#12P呜…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#1453F#5P我们所做的事情，\x01",
            "就包含了这种可能性。\x02\x03",

            "#1457F我也非常喜欢提妲。\x02\x03",

            "我明白你\x01",
            "对朋友的重视。\x02\x03",

            "但是，\x01",
            "并不能因此\x01",
            "就认同提妲的参与。\x02\x03",

            "#1452F你明白吧，提妲。\x02",
        )
    )

    Jump("loc_104F")

    label("loc_104F")

    CloseMessageWindow()

    ChrTalk(    #32
        0x107,
        (
            "#065F#12P#40W…………………………\x02\x03",

            "#562F但、但是…………\x01",
            "……我也…………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #33
        0x107,
        (
            "#069F#12P#3S……不是抱着\x01",
            "随随便便的心情，才说的……！\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x96)
    CloseMessageWindow()
    OP_8C(0x107, 90, 600)

    def lambda_1112():
        OP_8E(0xFE, 0xFFFFFAEC, 0x0, 0x2580, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1112)
    WaitChrThread(0x107, 0x1)

    def lambda_1132():
        OP_8E(0xFE, 0xFFFFFAEC, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1132)
    WaitChrThread(0x107, 0x1)
    OP_22(0x6D, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #34
        0x10,
        (
            "#104F#5P艾莉卡啊，\x01",
            "这次的事情\x01",
            "提妲应该也想了很多。\x02\x03",

            "#102F不能稍微\x01",
            "尊重一下她的想法吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        (
            "#1457F#6P但也不能因为这个\x01",
            "就让她参与兵器的开发啊。\x02\x03",

            "……研究成果离开自己的手之后\x01",
            "无论被如何使用，\x01",
            "研究者都是无法干涉的。\x02\x03",

            "#1453F我们对于这种事，\x01",
            "也只能事先有所觉悟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        "#104F#5P…………是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        (
            "#1452F#6P虽然也明白那孩子的心情，\x01",
            "但是绝不能让她\x01",
            "接触导力装甲计划。\x02\x03",

            "#1457F那个孩子，\x01",
            "不必为这种事而烦恼……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_134D():
        OP_6B(2960, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_134D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3112   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2A0 end

    def Function_4_136F(): pass

    label("Function_4_136F")


    def lambda_1375():
        OP_8E(0xFE, 0xFFFFFFE2, 0x0, 0x3700, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1375)
    WaitChrThread(0x10, 0x1)

    def lambda_1395():
        OP_8E(0xFE, 0xFFFFF768, 0x0, 0x3700, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1395)
    WaitChrThread(0x10, 0x1)

    def lambda_13B5():
        OP_8E(0xFE, 0xFFFFF380, 0x0, 0x3318, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13B5)
    WaitChrThread(0x10, 0x1)

    def lambda_13D5():
        OP_8E(0xFE, 0xFFFFF380, 0x0, 0x2FF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13D5)
    WaitChrThread(0x10, 0x1)

    def lambda_13F5():

        label("loc_13F5")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_13F5")

    QueueWorkItem2(0x10, 2, lambda_13F5)
    Return()

    # Function_4_136F end

    SaveToFile()

Try(main)
