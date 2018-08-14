from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4142   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4142.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '科蕾蒂',                               # 9
        '彭萨',                                 # 10
        '克鲁茨',                               # 11
        '古拉斯',                               # 12
        '古拉斯',                               # 13
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01023 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01143 ._CH',             # 05
        'ED6_DT07/CH01620 ._CH',             # 06
        'ED6_DT06/CH20020 ._CH',             # 07
        'ED6_DT06/CH20021 ._CH',             # 08
        'ED6_DT27/CH03233 ._CH',             # 09
        'ED6_DT26/CH20692 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01023P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01143P._CP',             # 05
        'ED6_DT07/CH01620P._CP',             # 06
        'ED6_DT06/CH20020P._CP',             # 07
        'ED6_DT06/CH20021P._CP',             # 08
        'ED6_DT27/CH03233P._CP',             # 09
        'ED6_DT26/CH20692P._CP',             # 0A
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 100,
        Y                   = -3850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x115,
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
        X                   = 5080,
        Z                   = 4700,
        Y                   = 1340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327688,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5000,
        Z                   = 4700,
        Y                   = 440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327688,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = 590,
        TriggerRange        = 400,
        ActorX              = 4560,
        ActorZ              = 1500,
        ActorY              = 2500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_229",          # 01, 1
        "Function_2_22A",          # 02, 2
        "Function_3_22F",          # 03, 3
        "Function_4_230",          # 04, 4
        "Function_5_235",          # 05, 5
        "Function_6_236",          # 06, 6
        "Function_7_1DDB",         # 07, 7
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_228")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)

    label("loc_228")

    Return()

    # Function_0_20A end

    def Function_1_229(): pass

    label("Function_1_229")

    Return()

    # Function_1_229 end

    def Function_2_22A(): pass

    label("Function_2_22A")

    Call(0, 3)
    Return()

    # Function_2_22A end

    def Function_3_22F(): pass

    label("Function_3_22F")

    Return()

    # Function_3_22F end

    def Function_4_230(): pass

    label("Function_4_230")

    Call(0, 5)
    Return()

    # Function_4_230 end

    def Function_5_235(): pass

    label("Function_5_235")

    Return()

    # Function_5_235 end

    def Function_6_236(): pass

    label("Function_6_236")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(1320, 0, -2340, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(25000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x151, 0x4)
    SetChrFlags(0x151, 0x40)
    SetChrPos(0x103, 5300, 4100, -400, 0)
    SetChrPos(0x151, 5200, 4100, 2320, 180)
    SetChrChipByIndex(0x103, 9)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x151, 10)
    SetChrSubChip(0x151, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    def lambda_2DE():
        OP_6D(6420, 4000, 1900, 5000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2DE)

    def lambda_2F6():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2F6)

    def lambda_306():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_306)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x15, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x103,
        "#1641F#3S……干杯！#2S\x02",
    )


    ChrTalk(    #1
        0x151,
        "#1651F#3S#1P……干杯！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()
    OP_22(0xB2, 0x0, 0x64)

    ChrTalk(    #2
        0x151,
        "#1654F#1P咕嘟咕嘟。\x02",
    )

    CloseMessageWindow()
    OP_22(0xB2, 0x0, 0x64)

    ChrTalk(    #3
        0x103,
        (
            "#1646F咕嘟咕嘟咕嘟……\x02\x03",

            "#1641F#3S呼啊～……！#2S\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x13, 1)
    SetChrSubChip(0x14, 1)
    OP_0D()

    ChrTalk(    #4
        0x103,
        (
            "#1640F可是，把所有的钱全捐出去了\x01",
            "是不是有些太夸张了？\x02\x03",

            "你难道没有考虑\x01",
            "自己的生活费吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x151,
        (
            "#1650F#1P是啊……一般情况下\x01",
            "是不会这么做的。\x02\x03",

            "#1654F不过，\x01",
            "这是我一开始就决定了的。\x02\x03",

            "我想要的\x01",
            "并不是那样的东西……\x02",
        )
    )

    Jump("loc_4FA")

    label("loc_4FA")

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x151,
        (
            "#1651F#1P呵呵，雪拉扎德也\x01",
            "晋升为正游击士了，恭喜你。\x02\x03",

            "虽然我还不太明白\x01",
            "那和准游击士有什么区别。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#1640F这个啊，权利和责任\x01",
            "都随之增加了嘛。\x02\x03",

            "我所想要的，\x01",
            "也并不只是正游击士的徽章而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x151,
        "#1653F#1P啊呀，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        "#1641F是啊～\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8)
    SetChrPos(0x12, 2820, 4000, 4780, 90)

    NpcTalk(    #10
        0x12,
        "青年的声音",
        "#2P……这样我就放心了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x151, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x12, 0x8)
    SetChrPos(0x12, -4220, 2000, 4780, 90)
    OP_43(0x12, 0x3, 0x0, 0x7)

    def lambda_6D4():
        OP_6D(3420, 4000, 4900, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_6D4)
    WaitChrThread(0x15, 0x0)
    Sleep(2000)

    def lambda_6F6():
        OP_6D(6420, 4000, 1900, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_6F6)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x12, 0x3)

    ChrTalk(    #11
        0x12,
        (
            "#840F看来你已经领会\x01",
            "游击士的心得了，\x01",
            "雪拉扎德。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #12
        0x103,
        (
            "#1643F哇，克鲁茨前辈。\x02\x03",

            "#1646F哎呀～那个，这酒是……\x01",
            "……那、那个叫什么来着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x12,
        (
            "#840F……因为是祝酒的缘故，\x01",
            "今晚我就睁一只眼闭一只眼了。\x02\x03",

            "不过，要控制在\x01",
            "不影响工作的程度才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        "#1645F好～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x12,
        "#843F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        "#1641F怎～么～了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x12,
        (
            "#843F雪拉扎德，\x01",
            "你既然已经是正游击士了……\x02\x03",

            "像往常那样\x01",
            "在白天工作时偷跑去喝酒，\x01",
            "或者夜里溜出去畅饮……\x02\x03",

            "还有趁我在忙的时候酒后闹事，\x01",
            "这些都收敛一下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_94E():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_94E)

    ChrTalk(    #18
        0x103,
        "#1645F呜呜……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x151, 0)
    Sleep(100)

    ChrTalk(    #19
        0x151,
        (
            "#1653F#1P雪拉扎德，\x01",
            "你竟然会做这样的事啊？\x02\x03",

            "简直是个坏孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x103,
        "#1645F不说了，不说了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        "#843F要慎重行事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x103,
        "#1643F#3S好、好的！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "#840F还有……\x01",
            "你不需要再用尊称和我谈话了。\x02\x03",

            "现在你已经和我一样是正游击士了。\x01",
            "我希望我们能以同事的身份相待。\x02\x03",

            "#841F我毕竟也还是个新人。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x151, 1)
    Sleep(1000)

    ChrTalk(    #24
        0x103,
        "#1648F……我可看不出来。\x02",
    )


    ChrTalk(    #25
        0x151,
        "#1653F#1P……是吗？\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_8C(0x12, 270, 400)
    Sleep(300)

    ChrTalk(    #26
        0x12,
        (
            "#843F…………进入正题。\x02\x03",

            "#842F爱娜小姐，\x01",
            "关于你伯父的事情……\x02\x03",

            "游击士协会方面\x01",
            "能够为你尽量申诉减刑。\x02\x03",

            "#844F不过雇佣猎兵团\x01",
            "本来是很严重的罪行……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x151, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x103,
        "#1643F#3S猎、猎兵团！？#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #28
        0x151,
        (
            "#1653F#1P这个……\x01",
            "莫非是那些黑衣人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        (
            "#842F嗯，是在利贝尔国内\x01",
            "已经确认了的猎兵团之一。\x02\x03",

            "最近在利贝尔也有\x01",
            "大大小小的许多猎兵团混入，\x01",
            "并且也都能找到主顾。\x02\x03",

            "当然这是违法的行为……\x01",
            "但军队似乎没有意愿采取行动。\x02\x03",

            "#843F……不过正好趁这个机会清扫了，\x01",
            "所以现在应该看不到那些家伙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        "#1643F清、清扫……\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #31
        0x103,
        (
            "#1642F（是这样啊，\x01",
            "  前辈那时恰好出现并非偶然……）\x02\x03",

            "（原来是对王国中的猎兵团\x01",
            "  进行的调查及剿灭作战。）\x02\x03",

            "（#1645F难怪最近一段时间\x01",
            "  他好像都很忙碌的样子……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103)

    ChrTalk(    #32
        0x12,
        (
            "#843F潜入国内的猎兵团瞄准了富裕阶层，\x01",
            "与他们结成了契约，\x01",
            "把老百姓卷入进来……\x02\x03",

            "#842F最近各地\x01",
            "都频繁爆发这类事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x151,
        "#1654F#1P这、这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x12,
        (
            "#843F这次的事情\x01",
            "始作俑者好像也是猎兵团的人。\x02\x03",

            "…………虽然发生了这样的事情，\x01",
            "但你的伯父或许也可以\x01",
            "称得上是被害人之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x151, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #35
        0x151,
        "#1653F#1P咦……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#1642F前、前辈……\x01",
            "这是什么意思！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #37
        0x103,
        (
            "#1644F克鲁茨前辈…………\x01",
            "如果那个大叔也是被害人之一的话，\x01",
            "也就意味着他无罪了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        (
            "#1644F#3S这种情况\x01",
            "爱娜能接受吗！？\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #39
        0x103,
        (
            "#1647F#3S那家伙可是\x01",
            "意图杀死爱娜的啊！！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #40
        0x12,
        (
            "#843F……雪拉，不用再叫我前辈了。\x02\x03",

            "#842F而且也不用这么大的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x103,
        "#1647F好、好的。可是……！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x12,
        (
            "#843F他不可能没有罪。\x02\x03",

            "#845F只是，\x01",
            "如果爱娜愿意的话，\x01",
            "就有希望争取减刑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        "#1643F这、这个…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x103)

    ChrTalk(    #44
        0x103,
        (
            "#1645F……这、这样啊。\x01",
            "吓我一跳……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x151,
        "#1654F#1P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "#843F……不必急于作出回答。\x02\x03",

            "因为调查取证\x01",
            "还要一周左右的时间。\x02\x03",

            "#840F你不需要\x01",
            "承担任何的责任，\x01",
            "也没有必要想得太多。\x02\x03",

            "只需要记住\x01",
            "你有宽恕他的选择\x01",
            "就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x151,
        "#1652F#1P……好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x12,
        (
            "#840F那么……\x01",
            "如果今后有什么困难的话，\x01",
            "不必犹豫，直接来找游击士协会就可以。\x02\x03",

            "我们绝非万能，\x01",
            "但一定可以助你一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x151,
        (
            "#1650F#1P我明白了。\x02\x03",

            "对不起，这次委托\x01",
            "是我没有把事情先说清楚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x12,
        (
            "#843F不，如果把我放到你的位置，\x01",
            "那就可以理解了。\x02\x03",

            "而且…………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x103, 500)
    Sleep(200)

    ChrTalk(    #51
        0x12,
        (
            "#842F独当一面的游击士\x01",
            "就算是对于语焉不详的委托，\x01",
            "也会对其实质内容一目了然。\x02\x03",

            "而绝不会不假思索地\x01",
            "随便将遇到困难的人赶回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        (
            "#1642F唔…………\x02\x03",

            "#1645F我的经验还是\x01",
            "远远不足啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x12,
        "#841F保持进取的精神就行了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 0, 500)
    Sleep(200)

    ChrTalk(    #54
        0x12,
        "#840F那么，我这就告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_1620():
        OP_8E(0xFE, 0x1AE0, 0xFA0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1620)
    Sleep(300)
    SetChrSubChip(0x103, 0)
    Sleep(300)

    ChrTalk(    #55
        0x103,
        (
            "#1643F啊，等一下……\x02\x03",

            "今天至少陪我\x01",
            "喝一杯吧！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #56
        0x12,
        (
            "#843F#3P不了，\x01",
            "我还要担任接待的职位。\x02\x03",

            "#845F……雪拉，\x01",
            "记得不要喝太多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x12, 315, 500)

    def lambda_16F5():
        OP_8E(0xFE, 0x16F8, 0xFA0, 0x1194, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_16F5)
    WaitChrThread(0x12, 0x1)

    def lambda_1715():
        OP_8E(0xFE, 0xFFFFFB3C, 0xFA0, 0x1194, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1715)
    Sleep(500)
    SetChrSubChip(0x151, 0)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #57
        0x103,
        (
            "#1645F哼……这个老顽固。\x02\x03",

            "#1640F啊，对～了。\x02\x03",

            "爱娜能喝酒吗？\x01",
            "陪我喝一点怎么样～⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x151,
        "#1650F#1P嗯、嗯……好吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x103,
        (
            "#1643F这、这个。\x01",
            "……你真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x151,
        (
            "#1650F#1P你已经关照我\x01",
            "那么多了……\x02\x03",

            "#1651F稍微来一点没问题㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x103,
        (
            "#1640F呵呵呵，\x01",
            "那今晚就一醉方休。\x02\x03",

            "#1641F（气质这么高雅的爱娜\x01",
            "  醉倒之后会是什么模样呢～……）\x02\x03",

            "#3S（啊，真·期·待！）#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x151, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x13, 5)
    SetChrSubChip(0x14, 5)
    OP_0D()
    Sleep(300)

    ChrTalk(    #62
        0x103,
        "#1641F#3S那，我们来干杯！#2S\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        "\x18\x07\x0C#40W温暖的金发、白皙的肌肤、湛蓝的眼眸――……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #64
        "\x18\x07\x0C#40W我曾经看到，对面那个世界的街区。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x18\x07\x0C#40W穿着美丽衣服的孩子们。受到祝福的孩子们。\x01",
            "幸福的孩子们绽放着天使般的笑容。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #66
        "\x18\x07\x0C#40W……为什么，我不属于那个世界？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #67
        "\x18\x07\x0C#40W我的心中一直抱有这个疑问。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #68
        (
            "\x18\x07\x0C#40W交织着嫉恨的羡慕。\x01",
            "掺杂着焦虑和拒绝的心情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #69
        "\x18\x07\x0C#40W可是我明明很清楚答案，那唯一的答案。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #70
        (
            "\x18\x07\x0C#40W为了生存而不断降低自己的底线，\x01",
            "明明自己已经陷入了那样的绝望之中。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #71
        (
            "\x18\x07\x0C#40W却一直在心中的某一处。\x01",
            "…………相信着。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #72
        "\x18\x07\x0C#40W终有一日，会迎来发自内心的微笑。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #73
        "\x18\x07\x0C#40W终有一日，会原谅曾经沦为那样的自己。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetChrName("")

    AnonymousTalk(    #74
        (
            "\x18\x07\x0C#40W――翌日，爱娜去了游击士协会\x01",
            "为伯父写了减刑请愿书。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #75
        (
            "\x18\x07\x0C#40W……而被她灌得烂醉的我\x01",
            "只能错过到场的机会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0xFA0)
    OP_21()
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #76
        "\x07\x00Episode『委托人』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_C2(0x1, 0x0)
    ClearParty()
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBB")
    Sleep(1000)
    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x4, 0x20)
    OP_3E(0x2D6, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x00得到了\x1F\xD6\x02\x07\x00。\x02",
    )

    Jump("loc_1D84")

    label("loc_1D84")

    CloseMessageWindow()
    AddMira(4000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #78
        "\x07\x00得到了\x07\x02４０００米拉\x07\x00。\x02",
    )

    Jump("loc_1DAF")

    label("loc_1DAF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1DBB")

    OP_A2(0x2504)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1DD1")
    NewScene("ED6_DT21/U4123   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1DDA")

    label("loc_1DD1")

    NewScene("ED6_DT21/U4121   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1DDA")

    Return()

    # Function_6_236 end

    def Function_7_1DDB(): pass

    label("Function_7_1DDB")


    def lambda_1DE1():
        OP_8E(0xFE, 0x16F8, 0xFA0, 0x12AC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1DE1)
    WaitChrThread(0x12, 0x1)

    def lambda_1E01():
        OP_8E(0xFE, 0x1AE0, 0xFA0, 0xEC4, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E01)
    WaitChrThread(0x12, 0x1)

    def lambda_1E21():
        OP_8E(0xFE, 0x1AE0, 0xFA0, 0x488, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E21)
    Sleep(800)
    SetChrSubChip(0x103, 2)
    Sleep(100)
    SetChrSubChip(0x151, 1)
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x12, 0x103, 400)
    Sleep(300)
    Return()

    # Function_7_1DDB end

    SaveToFile()

Try(main)
