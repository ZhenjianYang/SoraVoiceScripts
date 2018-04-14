from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5401   ._SN',
        MapName             = 'Other',
        Location            = 'C5401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '怀斯曼教授',                           # 9
        '剑帝莱维',                             # 10
        '怪盗布卢布兰',                         # 11
        '瘦狼瓦鲁特',                           # 12
        '幻惑之铃露茜奥拉',                     # 13
        '小丑肯帕雷拉',                         # 14
        '歼灭天使玲',                           # 15
        '强化猎兵',                             # 16
        '强化猎兵',                             # 17
        '残像',                                 # 18
        '残像',                                 # 19
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
        'ED6_DT26/CH20383 ._CH',             # 00
        'ED6_DT27/CH03550 ._CH',             # 01
        'ED6_DT27/CH04547 ._CH',             # 02
        'ED6_DT27/CH04548 ._CH',             # 03
        'ED6_DT27/CH03530 ._CH',             # 04
        'ED6_DT27/CH03500 ._CH',             # 05
        'ED6_DT27/CH03520 ._CH',             # 06
        'ED6_DT27/CH03600 ._CH',             # 07
        'ED6_DT27/CH03510 ._CH',             # 08
        'ED6_DT27/CH04000 ._CH',             # 09
        'ED6_DT27/CH04001 ._CH',             # 0A
        'ED6_DT27/CH04003 ._CH',             # 0B
        'ED6_DT27/CH04004 ._CH',             # 0C
        'ED6_DT26/CH20208 ._CH',             # 0D
        'ED6_DT27/CH03540 ._CH',             # 0E
        'ED6_DT27/CH04620 ._CH',             # 0F
        'ED6_DT26/CH20237 ._CH',             # 10
        'ED6_DT26/CH20280 ._CH',             # 11
        'ED6_DT26/CH20305 ._CH',             # 12
        'ED6_DT26/CH20439 ._CH',             # 13
        'ED6_DT27/CH04002 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT26/CH20383P._CP',             # 00
        'ED6_DT27/CH03550P._CP',             # 01
        'ED6_DT27/CH04547P._CP',             # 02
        'ED6_DT27/CH04548P._CP',             # 03
        'ED6_DT27/CH03530P._CP',             # 04
        'ED6_DT27/CH03500P._CP',             # 05
        'ED6_DT27/CH03520P._CP',             # 06
        'ED6_DT27/CH03600P._CP',             # 07
        'ED6_DT27/CH03510P._CP',             # 08
        'ED6_DT27/CH04000P._CP',             # 09
        'ED6_DT27/CH04001P._CP',             # 0A
        'ED6_DT27/CH04003P._CP',             # 0B
        'ED6_DT27/CH04004P._CP',             # 0C
        'ED6_DT26/CH20208P._CP',             # 0D
        'ED6_DT27/CH03540P._CP',             # 0E
        'ED6_DT27/CH04620P._CP',             # 0F
        'ED6_DT26/CH20237P._CP',             # 10
        'ED6_DT26/CH20280P._CP',             # 11
        'ED6_DT26/CH20305P._CP',             # 12
        'ED6_DT26/CH20439P._CP',             # 13
        'ED6_DT27/CH04002P._CP',             # 14
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_2DD",          # 01, 1
        "Function_2_2FC",          # 02, 2
        "Function_3_27D9",         # 03, 3
        "Function_4_27F6",         # 04, 4
        "Function_5_286D",         # 05, 5
        "Function_6_294B",         # 06, 6
        "Function_7_2996",         # 07, 7
        "Function_8_29F2",         # 08, 8
        "Function_9_2AB3",         # 09, 9
        "Function_10_2B74",        # 0A, 10
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2C3")
    OP_A3(0x10F0)
    Event(0, 10)
    Jump("loc_2DC")

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_2DC")

    Return()

    # Function_0_2B2 end

    def Function_1_2DD(): pass

    label("Function_1_2DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FB")

    Return()

    # Function_1_2DD end

    def Function_2_2FC(): pass

    label("Function_2_2FC")

    EventBegin(0x0)
    SetChrPos(0x101, -960, 0, 45690, 0)
    SetChrPos(0x8, -1000, 1600, 89800, 0)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)

    def lambda_330():

        label("loc_330")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_330")

    QueueWorkItem2(0x8, 0, lambda_330)
    OP_6D(-740, 0, 50090, 0)
    OP_67(0, 13680, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(410, 0)
    OP_1F(0x64, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_38F():
        OP_6D(1180, 1500, 94610, 9000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_38F)

    def lambda_3A7():
        OP_67(0, 16910, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A7)

    def lambda_3BF():
        OP_6B(2900, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3BF)

    def lambda_3CF():
        OP_6C(45000, 9000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3CF)

    def lambda_3DF():
        OP_6E(550, 9000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3DF)

    def lambda_3EF():
        OP_8E(0xFE, 0xFFFFFC40, 0x0, 0xF848, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EF)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    Sleep(1000)

    def lambda_418():
        OP_6D(-350, 1500, 90480, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_418)

    def lambda_430():
        OP_67(0, 5350, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_430)

    def lambda_448():
        OP_6B(2020, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_448)

    def lambda_458():
        OP_6C(57000, 8000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_458)

    def lambda_468():
        OP_6E(512, 8000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_468)
    WaitChrThread(0x101, 0x0)
    OP_71(0x4, 0x4)
    OP_79(0x9, 0x2)
    OP_7B()
    SetChrPos(0x101, -900, 0, 78060, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(1000)
    OP_6B(1600, 6000)
    Sleep(1000)
    OP_20(0x7D0)
    OP_21()
    OP_44(0x8, 0x0)
    Sleep(1000)

    ChrTalk(    #0
        0x8,
        (
            "#1154F#5P欢迎……\x01",
            "欢迎来到『红色方舟』古罗力亚斯。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    ClearChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 1)
    SetChrPos(0x8, -2000, 1500, 89380, 0)
    OP_0D()
    OP_1D(0x70)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #1
        0x8,
        "#1151F#5P好久不见了，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-1380, 1600, 84070, 0)
    OP_67(0, 4660, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(33000, 0)
    OP_6E(545, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #2
        0x101,
        (
            "#1002F亚鲁瓦教授……\x01",
            "果然是你。\x02\x03",

            "刚才听到你的声音\x01",
            "总算想起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#1154F#5P呵呵，\x01",
            "不愧是『剑圣』的女儿。\x02\x03",

            "#1150F虽然我并没有施加重咒，但想不到你\x01",
            "竟然能靠自己的力量将封锁的记忆找回。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1002F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_68A():
        OP_8F(0x8, 0xFFFFFC7C, 0x5DC, 0x14FBE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_68A)
    Sleep(1000)
    Fade(500)
    OP_72(0x4, 0x4)
    OP_79(0x9, 0x1)
    OP_7B()
    OP_6D(-900, 0, 88050, 0)
    OP_67(0, 3050, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(0, 0)
    OP_6E(362, 0)
    OP_6D(-960, 0, 88610, 0)
    OP_67(0, 2550, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(0, 0)
    OP_6E(362, 0)
    WaitChrThread(0x8, 0x3)
    OP_0D()
    Sleep(500)

    ChrTalk(    #5
        0x8,
        (
            "#1150F#5P顺带一提，\x01",
            "我真正的名字叫盖鲁格·怀斯曼。\x02\x03",

            "负责掌管『噬身之蛇』，\x01",
            "是『蛇之使徒』的一柱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1002F#6P『蛇之使徒』……\x01",
            "就是『结社』的最高干部？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#1154F#5P嗯，算是吧。\x02\x03",

            "#1150F好了，正如之前所说，\x01",
            "我准备要回答你的疑问。\x02\x03",

            "有什么想问的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1003F#6P…………………………………\x02\x03",

            "#1007F……想问的事情太多，\x01",
            "都不知道该从哪里问起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#1151F#5P不用着急。\x01",
            "慢慢想一下吧。\x02\x03",

            "不介意的话，\x01",
            "听我弹奏一曲如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1007F#6P不用了。\x02\x03",

            "#1019F不过话说回来，\x01",
            "没想到你还有这种兴趣……\x02\x03",

            "看来以前自称贫穷考古学者\x01",
            "的那些话全部都是谎言吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#1154F呵呵，贫穷不贫穷暂且不去计较，\x01",
            "研究考古学倒是真的。\x02\x03",

            "#1150F顺带一提，在我还身处教会的时候\x01",
            "就开始喜欢风琴了。\x02\x03",

            "虽然没那个帝国人那么厉害，\x01",
            "不过水平也还拿得出手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1004F#6P身、身处教会……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#1151F只是所谓的学僧啦。\x02\x03",

            "#1154F虽然遇到『盟主』之后\x01",
            "我就舍弃了信仰之道……\x02\x03",

            "不过那时学到的古代遗物知识\x01",
            "直到现在也相当有用。\x02\x03",

            "#1150F没错，在这次的计划中也是如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1002F#6P………………………………\x02\x03",

            "挑唆上校\x01",
            "发动政变……\x02\x03",

            "在各地进行『福音』实验，\x01",
            "引发各种混乱……\x02\x03",

            "也全部……都是你干的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#1154F说得没错──\x02\x03",

            "#1151F一切都是为了『福音计划』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1002F#6P『福音计划』……\x02\x03",

            "那个研究所的数据库里\x01",
            "也有这个项目……\x02\x03",

            "总之就是要拿到\x01",
            "『辉之环』的计划对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#1154F说拿到\x01",
            "有点不恰当……\x02\x03",

            "#1150F不过，这么想\x01",
            "也可以吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1005F#6P『辉之环』是什么？\x02\x03",

            "据说是女神的至宝，\x01",
            "不过具体是怎样的东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#1151F关于『辉之环』的真面目，\x01",
            "目前请让我暂时保密。\x02\x03",

            "难得的巨大惊喜，\x01",
            "我可不想提前透露出来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1019F#6P惊喜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#1150F计划已经进行到第３阶段。\x02\x03",

            "再过不久，它的真正面目\x01",
            "就会呈现在所有人的面前。\x02\x03",

            "#1154F呵呵……请期待那一刻的到来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1002F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#1154F而当『环』现身之时……\x02\x03",

            "#1151F我们将能够确认\x01",
            "人类的可能性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F#6P人类的可能性……\x02\x03",

            "『雷格纳特』似乎也说过\x01",
            "这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#1153F哦，那只圣兽\x01",
            "连这些话也告诉你们了吗。\x02\x03",

            "#1150F唔，看来你不光是\x01",
            "顶着父亲的光环而已呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1022F#6P恭维话就到此为止吧！\x02\x03",

            "#1019F什么嘛……说是回答我的问题，\x01",
            "结果还不是自己一个人喋喋不休。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#1154F这真是失礼了……\x01",
            "我并不是有意的。\x02\x03",

            "#1150F不过，你最想问的事情\x01",
            "我应该能很清楚地回答哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x101,
        "#1026F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#1151F哎呀，为何\x01",
            "如此地犹豫呢？\x02\x03",

            "不必害怕，\x01",
            "鼓起勇气问吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1003F#6P………………………………\x02\x03",

            "约修亚……他在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#1154F呵呵……\x01",
            "这我也不知道。\x02\x03",

            "好像是与空贼们在一起\x01",
            "谋划着什么的样子……\x02\x03",

            "目前的动向还不清楚。\x02\x03",

            "#1150F不过现在应该还平安无事，这一点\x01",
            "应该是没有错才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1025F#6P是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#1154F将约修亚的能力调整为\x01",
            "隐密活动和对集团作战这项工作，\x02\x03",

            "是我亲手进行的。\x01",
            "不过，完成度似乎远远超出我的预料。\x02\x03",

            "#1151F呵呵呵……他究竟能奋战到\x01",
            "什么程度呢？真是令人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1002F#6P你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#1153F啊啊，别露出\x01",
            "那么可怕的表情嘛。\x02\x03",

            "#1150F当初托付给我的时候，\x01",
            "约修亚的心已经崩溃了。\x02\x03",

            "要重新构筑这样的心，\x01",
            "对我来说也是第一次尝试。\x02\x03",

            "#1154F作为一个研究者，\x01",
            "在意自己的成果不是理所当然的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1003F#6P…………………………………\x02\x03",

            "……那场诞辰庆典的时候，\x01",
            "你对约修亚说了什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#1150F我只是解除了封锁的记忆，\x01",
            "将真相告诉给他而已。\x02\x03",

            "#1154F被你家收养的他，\x01",
            "在无意识下作为间谍\x01",
            "向『结社』传送情报的事……\x02\x03",

            "还有，多亏有他的情报，\x01",
            "理查德上校的政变才能成功，\x01",
            "而我们的计划也准备就绪的事。\x02\x03",

            "#1151F作为奖励，\x01",
            "我就把他从『结社』中解放了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1027F#6P……………………………\x02\x03",

            "……我终于明白了……\x02\x03",

            "约修亚为什么……\x01",
            "会在那个夜晚……消失不见……\x02\x03",

            "为什么会露出那样的表情……\x01",
            "对我说再见……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#1150F呀，有关这一点，\x01",
            "我也觉得很遗憾啊。\x02\x03",

            "恢复自我的约修亚\x01",
            "竟然会从你们面前消失。\x02\x03",

            "#1154F我曾经还特意劝说过他，\x01",
            "让他装作一无所知的样子，\x01",
            "继续和你们一起生活就好了……\x02\x03",

            "#1151F呵呵，好心没好报吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_71(0x4, 0x4)
    OP_79(0x9, 0x2)
    OP_7B()
    OP_6D(270, 420, 83800, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(386, 0)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(500)

    ChrTalk(    #40
        0x101,
        (
            "#1025F#2P你竟然……\x01",
            "说得出这种话……\x02\x03",

            "明明就是你逼得约修亚\x01",
            "只能选择这条路……\x02\x03",

            "#1027F逼得他…现出那副表情……\x01",
            "把口琴交给我……\x02\x03",

            "对我说再见了……艾丝蒂尔……\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1023F#3S#2P这全部的全部！#2S！\x02\x03",

            "#1023F#3S#2P不都是你造成的吗！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_16B8():
        OP_6D(-660, 1500, 85500, 600)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_16B8)

    def lambda_16D0():
        OP_6B(2200, 600)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_16D0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x101, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrSubChip(0x9, 9)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, -990, 2500, 84790, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x1000)

    def lambda_1725():
        OP_8F(0xFE, 0xFFFFFC22, 0x5DC, 0x14B36, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1725)

    def lambda_1740():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1740)
    OP_22(0x99, 0x0, 0x64)
    Sleep(300)
    OP_43(0x9, 0x0, 0x0, 0x3)
    Sleep(500)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x101, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_17B3():
        OP_6D(-980, 1500, 81840, 300)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17B3)

    def lambda_17CB():
        OP_67(0, 3600, -10000, 300)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17CB)

    def lambda_17E3():
        OP_6B(2800, 300)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_17E3)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x2)
    OP_43(0x101, 0x0, 0x0, 0x5)

    ChrTalk(    #42 op#5
        0x101,
        "#2P啊……\x05\x02",
    )

    Sleep(500)
    WaitChrThread(0x101, 0x0)
    OP_99(0x101, 0x1, 0x3, 0x5DC)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0x9, 0x1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_99(0x9, 0x6, 0x7, 0x5DC)
    Sleep(500)

    ChrTalk(    #43
        0x9,
        "#121F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1021F#2P『剑帝』莱维……\x02\x03",

            "你、你到底是从哪里出现的……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 14)
    OP_0D()
    Sleep(500)

    ChrTalk(    #45
        0x9,
        (
            "#124F#5P……我从一开始就在这里。\x02\x03",

            "#120F只是你没注意到而已。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 100, -1, -1)
    SetChrName("男人的声音")

    AnonymousTalk(    #46
        (
            "\x07\x05真是的……\x01",
            "实在是没有风度的举止啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_1950():
        OP_6D(-450, 1500, 84100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1950)

    def lambda_1968():
        OP_67(0, 3600, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1968)

    def lambda_1980():
        OP_6B(2420, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1980)

    def lambda_1990():
        OP_6C(35000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1990)
    SetChrPos(0xA, -5300, 1500, 85140, 135)
    SetChrPos(0xB, 5040, 1500, 85050, 225)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x4)
    OP_43(0xA, 0x0, 0x0, 0x6)
    Sleep(500)
    OP_43(0xB, 0x0, 0x0, 0x7)
    Sleep(2000)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, 570, 1500, 84590, 180)

    def lambda_1A0A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1A0A)
    OP_22(0x99, 0x0, 0x64)
    OP_43(0x11, 0x1, 0x0, 0x8)
    OP_43(0x12, 0x1, 0x0, 0x9)
    Sleep(800)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0xC, 0x1)

    def lambda_1A50():

        label("loc_1A50")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_1A50")

    QueueWorkItem2(0x101, 3, lambda_1A50)
    OP_99(0x101, 0x3, 0x0, 0x3E8)
    OP_44(0x101, 0x3)
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◆布卢布兰的挑战全部完成】\x01",          # 0
            "【◆布卢布兰的挑战完成１个以上】\x01",      # 1
            "【◆无视了布卢布兰的挑战】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B2C"),
        (1, "loc_1B43"),
        (2, "loc_1B5A"),
        (SWITCH_DEFAULT, "loc_1B71"),
    )


    label("loc_1B2C")

    OP_28(0x6C, 0x4, 0x10)
    OP_28(0x77, 0x4, 0x10)
    OP_28(0x78, 0x4, 0x10)
    OP_28(0xC4, 0x4, 0x10)
    Jump("loc_1B71")

    label("loc_1B43")

    OP_28(0x6C, 0x4, 0x10)
    OP_28(0x77, 0x3, 0x10)
    OP_28(0x78, 0x3, 0x10)
    OP_28(0xC4, 0x3, 0x10)
    Jump("loc_1B71")

    label("loc_1B5A")

    OP_28(0x6C, 0x3, 0x10)
    OP_28(0x77, 0x3, 0x10)
    OP_28(0x78, 0x3, 0x10)
    OP_28(0xC4, 0x3, 0x10)
    Jump("loc_1B71")

    label("loc_1B71")

    FadeToBright(300, 0)

    label("loc_1B7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B8E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BA2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1BA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BB6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1BB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BCA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1BCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C2F")

    ChrTalk(    #47
        0xA,
        (
            "#231F#5P毕竟你也曾出色地\x01",
            "完成过我的挑战。\x02\x03",

            "在做出行动之前还是先稍微动动脑子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D13")

    label("loc_1C2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CAA")

    ChrTalk(    #48
        0xA,
        (
            "#232F#5P虽然有些勉强，\x01",
            "但至少你也曾经接受过我的挑战。\x02\x03",

            "在做出行动之前还是先稍微动动脑子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D13")

    label("loc_1CAA")


    ChrTalk(    #49
        0xA,
        (
            "#233F#5P都是因为你一直无视我的挑战，\x01",
            "所以才会表现得这么差劲。\x02\x03",

            "在做出行动之前还是先稍微动动脑子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D13")


    ChrTalk(    #50
        0xB,
        (
            "#252F#5P哇哈哈，别这么说啊。\x02\x03",

            "毫不犹豫地打向『白面』，\x01",
            "没有一定的胆量也是办不到的呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xC,
        (
            "#244F#5P呵呵～暂且不说本领如何，\x01",
            "单单就这勇气而言，确实可嘉。\x02\x03",

            "#240F还是说，只是因为天生反应迟钝呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DDE():
        OP_6D(-450, 960, 82000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DDE)
    Sleep(500)
    OP_8F(0x101, 0xFFFFFBE6, 0x0, 0x12750, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #52
        0x101,
        "#1026F#2P啊……呜………\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, 2800, 0, 79120, 225)
    SetMessageWindowPos(400, 150, -1, -1)
    SetChrName("少年的声音")

    AnonymousTalk(    #53
        (
            "\x07\x05哈哈哈……\x01",
            "你就是『剑圣』的千金吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1EA7():
        OP_6D(340, 480, 81240, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EA7)

    def lambda_1EBF():
        OP_67(0, 4260, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EBF)

    def lambda_1ED7():
        OP_6B(2460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1ED7)
    Sleep(500)
    TurnDirection(0x101, 0xD, 400)
    Sleep(1000)
    LoadEffect(0x1, "map\\\\mp055_00.eff")
    SetChrFlags(0xD, 0x8000)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xD, 0x80)
    PlayEffect(0x1, 0x1, 0xD, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1F56():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1F56)
    OP_22(0x99, 0x0, 0x64)
    Sleep(1800)
    OP_82(0x1, 0x2)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #54
        0xD,
        "#853F#5P呵呵，初次见面吧。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xD, 0)
    OP_99(0xD, 0x0, 0x3, 0x5DC)

    ChrTalk(    #55
        0xD,
        (
            "#854F#5P我是执行者Ｎｏ．０──\x01",
            "『小丑』肯帕雷拉。\x02\x03",

            "#851F今后多多关照哦㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xD, 0x3, 0x0, 0x5DC)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 7)
    SetChrSubChip(0xD, 0)
    Sleep(500)

    ChrTalk(    #56
        0x101,
        "#1020F#5P呜……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -1010, 0, 67570, 0)

    NpcTalk(    #57
        0xE,
        "少女的声音",
        (
            "#1P真是的，大家不要一起\x01",
            "吓唬艾丝蒂尔啦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2086():
        OP_6D(-1070, 0, 74320, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2086)

    def lambda_209E():
        OP_6B(2600, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_209E)
    TurnDirection(0x101, 0xE, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_20BF():
        OP_6D(-890, 0, 78320, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20BF)

    def lambda_20D7():
        OP_6B(2430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20D7)
    OP_8E(0xE, 0xFFFFFBC8, 0x0, 0x1200C, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #58
        0x101,
        "#1026F#5P玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xE,
        (
            "#263F#4P嘻嘻……\x01",
            "不必担心。\x02\x03",

            "#260F他们并不是为了杀艾丝蒂尔\x01",
            "才聚集在这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#1004F#5P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_217B():

        label("loc_217B")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_217B")

    QueueWorkItem2(0x101, 1, lambda_217B)

    def lambda_218C():
        OP_6D(-380, 950, 82220, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_218C)

    def lambda_21A4():
        OP_67(0, 4710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_21A4)

    def lambda_21BC():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_21BC)

    def lambda_21CC():
        OP_6E(360, 3000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_21CC)
    OP_8E(0xE, 0x172, 0x0, 0x126D8, 0x7D0, 0x0)
    OP_8E(0xE, 0x172, 0x0, 0x12FE8, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x1)

    ChrTalk(    #61
        0xE,
        (
            "#261F#2P对了，教授。\x02\x03",

            "早点把那件事\x01",
            "告诉艾丝蒂尔吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#1154F#6P呵呵……\x01",
            "就这么办吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_226A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_226A)

    def lambda_2278():
        OP_6D(-940, 940, 81750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2278)

    def lambda_2290():
        OP_67(0, 4230, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2290)

    def lambda_22A8():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22A8)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 14)

    def lambda_22C2():
        OP_8E(0xFE, 0xFFFFF5EC, 0x5DC, 0x14B4A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_22C2)
    Sleep(200)

    def lambda_22E2():
        OP_8E(0xFE, 0xFFFFFB14, 0x5DC, 0x14438, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22E2)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #63
        0x8,
        (
            "#1150F#5P如何，艾丝蒂尔。\x02\x03",

            "你是否愿意加入\x01",
            "我们『噬身之蛇』呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1004F#2P咦……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #65
        0x101,
        (
            "#1016F#2P……抱歉。\x01",
            "我好像听错了。\x02\x03",

            "#1008F能不能再说一次？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#1154F#5P我在问你，要不要\x01",
            "加入『噬身之蛇』。\x02\x03",

            "#1151F一开始先作为『执行者』候补。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1020F#2P什、什、什……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #68
        0x101,
        "#1005F#2P#4S你说什么～！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#1151F#5P呵呵，不必\x01",
            "那么吃惊吧？\x02\x03",

            "考虑一下吧！\x02\x03",

            "如果你加入『结社』的话，\x01",
            "约修亚也就不用那么为难了，\x01",
            "他一定会乖乖回到你身边来，你难道不这么想吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1026F#2P啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #71
        0xE,
        (
            "#265F#5P艾丝蒂尔的愿望\x01",
            "不就是想和约修亚重逢么？\x02\x03",

            "只要加入『结社』，\x01",
            "这个愿望马上就能实现了哦。\x02\x03",

            "#261F呵呵呵……\x01",
            "这还有什么要考虑的？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    Sleep(500)

    ChrTalk(    #72
        0x101,
        (
            "#1003F#6P……但、但是……\x02\x03",

            "………我…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#1150F#5P呵呵，慢慢考虑吧。\x02\x03",

            "#1154F等一下我们必须\x01",
            "暂时离开舰艇。\x02\x03",

            "当我回来的时候\x01",
            "再给我答案吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x8, 19)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x8, 1)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0xF, -1830, 0, 69620, 0)
    SetChrPos(0x10, -220, 0, 69620, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)

    def lambda_26D2():
        OP_6D(360, 680, 80540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26D2)

    def lambda_26EA():
        OP_67(0, 3470, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26EA)

    def lambda_2702():
        OP_6B(3220, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2702)

    def lambda_2712():
        OP_8E(0xFE, 0xFFFFF8DA, 0x0, 0x12110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2712)
    Sleep(100)

    def lambda_2732():
        OP_8E(0xFE, 0xFFFFFF24, 0x0, 0x12110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2732)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #74
        0x8,
        (
            "#1151F#5P不好意思，在那之前\x01",
            "我必须要限制你的自由。\x02\x03",

            "需要什么东西\x01",
            "尽管跟他们说就行了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x1C93)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C5400   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2FC end

    def Function_3_27D9(): pass

    label("Function_3_27D9")

    OP_99(0x9, 0x9, 0xF, 0xDAC)
    SetChrChipByIndex(0x9, 3)
    OP_99(0x9, 0x0, 0x5, 0xDAC)
    OP_22(0x1F5, 0x0, 0x64)
    Return()

    # Function_3_27D9 end

    def Function_4_27F6(): pass

    label("Function_4_27F6")

    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)

    def lambda_2806():
        OP_8E(0xFE, 0xFFFFFC22, 0x5DC, 0x1465E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2806)
    Sleep(200)
    SetChrChipByIndex(0x101, 20)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)

    def lambda_2835():
        OP_96(0xFE, 0xFFFFFC22, 0x708, 0x14690, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2835)
    Sleep(100)

    def lambda_2858():
        OP_99(0xFE, 0x0, 0x7, 0x8FC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2858)
    Sleep(100)
    OP_22(0x1F4, 0x0, 0x64)
    Return()

    # Function_4_27F6 end

    def Function_5_286D(): pass

    label("Function_5_286D")

    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 1)
    SetChrChipByIndex(0x101, 11)

    def lambda_288C():
        OP_96(0xFE, 0xFFFFFC90, 0x0, 0x1374A, 0x5DC, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_288C)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x4)

    def lambda_28B4():
        OP_96(0xFE, 0xFFFFFC68, 0x0, 0x12E3A, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28B4)
    WaitChrThread(0x101, 0x1)

    def lambda_28D7():
        OP_8F(0xFE, 0xFFFFFCB8, 0x0, 0x12926, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28D7)
    Sleep(100)

    def lambda_28F7():
        OP_8F(0xFE, 0xFFFFFCB8, 0x0, 0x12926, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28F7)
    Sleep(100)

    def lambda_2917():
        OP_8F(0xFE, 0xFFFFFCB8, 0x0, 0x12926, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2917)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    Return()

    # Function_5_286D end

    def Function_6_294B(): pass

    label("Function_6_294B")

    SetChrFlags(0xFE, 0x4)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2961():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2961)
    OP_8E(0xFE, 0xFFFFEEBC, 0x5DC, 0x14A78, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFFF01A, 0x5DC, 0x14780, 0x5DC, 0x0)
    Return()

    # Function_6_294B end

    def Function_7_2996(): pass

    label("Function_7_2996")

    SetChrFlags(0xFE, 0x4)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_29AC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29AC)
    OP_8E(0xFE, 0xAAA, 0x5DC, 0x14B72, 0x5DC, 0x0)
    OP_8E(0xFE, 0x596, 0x5DC, 0x14438, 0x5DC, 0x0)
    OP_8C(0xFE, 205, 400)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_2996 end

    def Function_8_29F2(): pass

    label("Function_8_29F2")

    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 570, 1500, 84590, 180)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2A19():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2A19)
    ClearChrFlags(0x11, 0x80)
    OP_91(0x11, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x11, 0x80)
    Return()

    # Function_8_29F2 end

    def Function_9_2AB3(): pass

    label("Function_9_2AB3")

    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 570, 1500, 84590, 180)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2ADA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2ADA)
    ClearChrFlags(0x12, 0x80)
    OP_91(0x12, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x12, 0x80)
    Return()

    # Function_9_2AB3 end

    def Function_10_2B74(): pass

    label("Function_10_2B74")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(210, 0, 53260, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(551, 0)
    SetChrPos(0xD, -1190, 1500, 85710, 0)
    ClearChrFlags(0xD, 0x80)

    def lambda_2BE3():
        OP_6D(-970, 5670, 90410, 8000)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2BE3)

    def lambda_2BFB():
        OP_67(0, 4170, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2BFB)

    def lambda_2C13():
        OP_6B(3050, 8000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2C13)

    def lambda_2C23():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2C23)

    def lambda_2C33():
        OP_6E(449, 8000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C33)
    OP_71(0x6, 0x4)
    OP_72(0x7, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xD, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-450, 1500, 86520, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    OP_71(0x4, 0x4)
    OP_79(0x9, 0x2)
    OP_7B()
    OP_0D()
    Sleep(500)

    ChrTalk(    #75
        0xD,
        (
            "#850F#2P呵呵，相当\x01",
            "令人期待不是吗。\x02\x03",

            "看这个样子，\x01",
            "今天就能到达中枢塔了呢。\x02\x03",

            "#855F不过，如果就这么照计划进行，\x01",
            "『观察者』的意义就不存在了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)
    Sleep(500)

    ChrTalk(    #76
        0xD,
        (
            "#853F#5P在真正的最终幕上演之前，\x01",
            "似乎还有点时间……\x02\x03",

            "#854F在此之前去捉弄一下\x01",
            "基尔巴特来取乐好了？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #77
        (
            "\x07\x05就这样，艾丝蒂尔等人\x01",
            "和空贼们一起从『古罗力亚斯』逃了出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #78
        (
            "\x07\x05途中与追赶上来的强化猎兵\x01",
            "数次展开交战之后……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #79
        (
            "\x07\x05艾丝蒂尔等人甩开追击，\x01",
            "设法回到了居住区域。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C5801   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2B74 end

    SaveToFile()

Try(main)
