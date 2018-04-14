from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4153   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4153.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '科洛丝',                               # 9
        '提妲',                                 # 10
        '玲',                                   # 11
        '王国军士兵',                           # 12
        '王国军士兵',                           # 13
        '王都格兰赛尔·西街区',                 # 14
        '格兰赛尔城方面',                       # 15
        '王都格兰赛尔·东街区',                 # 16
        '王都格兰赛尔·南街区',                 # 17
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
        'ED6_DT07/CH00040 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT27/CH03510 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00040P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT27/CH03510P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
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
        X                   = -6050,
        Z                   = 0,
        Y                   = 69190,
        Direction           = 190,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 6050,
        Z                   = 0,
        Y                   = 69190,
        Direction           = 190,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -40080,
        Z                   = 0,
        Y                   = 17660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 100,
        Z                   = 0,
        Y                   = 104130,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40430,
        Z                   = 0,
        Y                   = 64060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 0,
        Y                   = -3500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 18520,
        Y                   = 0,
        Z                   = 44050,
        Range               = 1500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_227",          # 01, 1
        "Function_2_24E",          # 02, 2
        "Function_3_29F",          # 03, 3
        "Function_4_2E8",          # 04, 4
        "Function_5_33A",          # 05, 5
        "Function_6_AF1",          # 06, 6
        "Function_7_B8A",          # 07, 7
        "Function_8_E01",          # 08, 8
        "Function_9_107D",         # 09, 9
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_226")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_226")

    Return()

    # Function_0_20A end

    def Function_1_227(): pass

    label("Function_1_227")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x23005E)
    OP_1B(0x6, 0x0, 0x7)
    OP_1B(0x7, 0x0, 0x8)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Return()

    # Function_1_227 end

    def Function_2_24E(): pass

    label("Function_2_24E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_273")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_289")

    label("loc_273")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289")
    OP_99(0xFE, 0x1, 0x7, 0x640)

    label("loc_289")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_289")

    label("loc_29E")

    Return()

    # Function_2_24E end

    def Function_3_29F(): pass

    label("Function_3_29F")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xB,
        (
            "由于警戒体制的强化\x01",
            "这里也被封锁了。\x02\x03",

            "任何人都\x01",
            "不准通过这里。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_29F end

    def Function_4_2E8(): pass

    label("Function_4_2E8")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xC,
        (
            "这里不允许任何人通过。\x02\x03",

            "上面下达了指示，\x01",
            "任何人都不准接近格兰赛尔城。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_2E8 end

    def Function_5_33A(): pass

    label("Function_5_33A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34D")
    Call(0, 6)

    label("loc_34D")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 5380, 0, 35040, 360)
    SetChrPos(0x101, 6180, 0, 34540, 360)
    SetChrPos(0xF7, 4690, 0, 34460, 360)
    SetChrPos(0x9, 6190, 0, 33520, 360)
    SetChrPos(0xA, 4770, 0, 33300, 360)
    OP_6D(6190, 250, 68540, 0)
    OP_67(0, 10150, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(56000, 0)
    OP_6E(403, 0)

    def lambda_3F4():
        OP_6D(9330, 250, 47830, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F4)
    FadeToBright(1000, 0)
    Sleep(2000)

    def lambda_41A():
        OP_8E(0xFE, 0x1504, 0x0, 0xB3D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_41A)
    Sleep(300)

    def lambda_43A():
        OP_8E(0xFE, 0x17E8, 0x0, 0xAE1A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43A)
    Sleep(50)

    def lambda_45A():
        OP_8E(0xFE, 0x134C, 0x0, 0xAE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_45A)
    Sleep(100)

    def lambda_47A():
        OP_8E(0xFE, 0x1824, 0x0, 0xAA00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47A)
    Sleep(50)

    def lambda_49A():
        OP_8E(0xFE, 0x136A, 0x0, 0xA924, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_49A)
    WaitChrThread(0xA, 0x1)
    OP_8C(0x8, 180, 400)
    Fade(1000)
    OP_6D(5550, 0, 44780, 0)
    OP_67(0, 8070, -10000, 0)
    OP_6B(4059, 0)
    OP_6C(45000, 0)
    OP_6E(180, 0)
    OP_0D()

    ChrTalk(    #2
        0x101,
        (
            "#1006F好了……\x01",
            "我们就到这里吧。\x02\x03",

            "科洛丝。\x01",
            "小心点回去哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#048F#5P呵呵，很近的\x01",
            "没关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "#264F咦，姐姐？\x01",
            "你住在这附近？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#045F#5P啊，嗯嗯。\x01",
            "住在亲属家里。\x02\x03",

            "#040F那么各位，我失陪了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5EB")

    ChrTalk(    #6
        0x106,
        "#051F#6P啊啊，明天见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_607")

    label("loc_5EB")


    ChrTalk(    #7
        0x103,
        "#021F#6P呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_607")


    ChrTalk(    #8
        0x9,
        "#061F#2P科洛丝姐姐，再见～～！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_638():
        OP_6D(5630, 0, 47820, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_638)
    OP_8E(0x8, 0x14FA, 0x0, 0xE59C, 0x9C4, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_6D(6030, 0, 44520, 1800)
    OP_8C(0x101, 225, 400)

    ChrTalk(    #9
        0x101,
        (
            "#1016F话说回来……\x01",
            "闹得还真夸张呢。\x02\x03",

            "奥利维尔把\x01",
            "穆拉先生都给找来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 90, 400)
    OP_8C(0xA, 45, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_70A")

    ChrTalk(    #10
        0x106,
        (
            "#051F#6P你不也是\x01",
            "把那个记者也叫来了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_737")

    label("loc_70A")


    ChrTalk(    #11
        0x103,
        (
            "#027F#6P你不也是\x01",
            "把记者先生都叫来了吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_737")


    ChrTalk(    #12
        0x101,
        (
            "#1008F啊哈哈……\x01",
            "想着无所谓的嘛。\x02\x03",

            "玲你们怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "#261F哈哈哈，很开心啊。\x02\x03",

            "饭菜也好吃\x01",
            "还听到很多有趣的事。\x02\x03",

            "钢琴也特别好听。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "#061F#4P嗯嗯，奥利维尔先生\x01",
            "的钢琴弹得很好啊。\x02\x03",

            "真有点吃惊呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8CC")

    ChrTalk(    #15
        0x101,
        (
            "#1016F嗯，好歹都是\x01",
            "自称演奏家来的嘛。\x02\x03",

            "#1006F阿加特\x01",
            "也还尽兴？\x02\x03",

            "和金先生他们\x01",
            "好像闹得挺开心的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #16
        0x106,
        (
            "#053F#6P和那家伙在一起\x01",
            "可真是聊个没完啊。\x02\x03",

            "#051F走了很多路也累了\x01",
            "赶快回去休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97B")

    label("loc_8CC")


    ChrTalk(    #17
        0x101,
        (
            "#1016F嗯，好歹都是\x01",
            "自称演奏家来的嘛。\x02\x03",

            "#1006F雪拉姐\x01",
            "也还尽兴？\x02\x03",

            "和金先生他们\x01",
            "好像闹得挺开心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x103,
        (
            "#027F#6P真的喝开了\x01",
            "可就停不下来了嘛。\x02\x03",

            "明天还有工作\x01",
            "今天早点休息吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97B")


    ChrTalk(    #19
        0x101,
        (
            "#1006F是吗……\x02\x03",

            "那么，我们也\x01",
            "回去酒店的房间吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    def lambda_9BD():
        OP_8E(0xFE, 0x4858, 0x2EE, 0xAC12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BD)
    Sleep(500)
    OP_8C(0x9, 90, 400)

    def lambda_9E4():
        OP_8E(0xFE, 0x4330, 0x190, 0xADAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9E4)
    Sleep(200)
    OP_8C(0xA, 90, 400)

    def lambda_A0B():
        OP_8E(0xFE, 0x4358, 0x19A, 0xAA1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A0B)
    Sleep(500)

    def lambda_A2B():
        OP_8E(0xFE, 0x3E1C, 0xFA, 0xABFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_A2B)
    OP_6D(18520, 750, 44050, 4000)
    WaitChrThread(0x101, 0x1)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    Sleep(1000)

    def lambda_A6F():
        OP_8E(0xFE, 0x4FF6, 0x2EE, 0xAC12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A6F)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_A99():
        OP_8E(0xFE, 0x4FF6, 0x2EE, 0xAC12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A99)
    Sleep(500)

    def lambda_AB9():
        OP_8E(0xFE, 0x4FF6, 0x2EE, 0xAC12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AB9)
    WaitChrThread(0x101, 0x1)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x101, 0x80)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_33A end

    def Function_6_AF1(): pass

    label("Function_6_AF1")

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
        (0, "loc_B6B"),
        (1, "loc_B71"),
        (SWITCH_DEFAULT, "loc_B77"),
    )


    label("loc_B6B")

    OP_A2(0x1200)
    Jump("loc_B77")

    label("loc_B71")

    OP_A2(0x1201)
    Jump("loc_B77")

    label("loc_B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B85")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_B89")

    label("loc_B85")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_B89")

    Return()

    # Function_6_AF1 end

    def Function_7_B8A(): pass

    label("Function_7_B8A")

    EventBegin(0x1)
    OP_4A(0xB, 255)
    OP_8C(0xB, 90, 400)

    ChrTalk(    #20
        0xB,
        (
            "哦，\x01",
            "请别再往前进了。\x02\x03",

            "由于警戒体制的强化\x01",
            "这里也被封锁了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D12")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFC")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_C03")

    label("loc_BFC")

    TurnDirection(0x103, 0x0, 400)

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C64")

    ChrTalk(    #21
        0x103,
        (
            "#022F（格兰赛尔城交给王国军\x01",
            "应该没问题吧。)\x02\x03",

            "（我们还是赶快\x01",
            "  去西街区那边吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAD")

    label("loc_C64")


    ChrTalk(    #22
        0x103,
        (
            "#022F（格兰赛尔城交给王国军\x01",
            "应该没问题吧。)\x02\x03",

            "(我们就赶紧去码头吧。)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDD")

    ChrTalk(    #23
        0x101,
        "#1002F（嗯，是啊。）\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()
    Jump("loc_D0C")

    label("loc_CDD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0C")

    ChrTalk(    #24
        0x109,
        "#1063F（啊啊，是啊。）\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()

    label("loc_D0C")

    OP_A2(0x0)
    Jump("loc_DDA")

    label("loc_D12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D28")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_D2F")

    label("loc_D28")

    TurnDirection(0x106, 0x0, 400)

    label("loc_D2F")


    ChrTalk(    #25
        0x106,
        (
            "#050F（格兰赛尔城交给王国军\x01",
            "应该没问题吧。)\x02\x03",

            "(我们就赶紧去码头吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA8")

    ChrTalk(    #26
        0x101,
        "#1002F（嗯，是啊。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x103, 400)
    Jump("loc_DD7")

    label("loc_DA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD7")

    ChrTalk(    #27
        0x109,
        "#1063F（啊啊，是啊。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x103, 400)

    label("loc_DD7")

    OP_A2(0x0)

    label("loc_DDA")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0xB, 180, 0)
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_B8A end

    def Function_8_E01(): pass

    label("Function_8_E01")

    EventBegin(0x1)
    OP_4A(0xC, 255)
    OP_8C(0xC, 270, 400)

    ChrTalk(    #28
        0xC,
        (
            "请不要再继续前进了。\x02\x03",

            "上面有指示说，任何人都\x01",
            "不得接近格兰赛尔城\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1056")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F8E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E78")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_E7F")

    label("loc_E78")

    TurnDirection(0x103, 0x0, 400)

    label("loc_E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE0")

    ChrTalk(    #29
        0x103,
        (
            "#022F（格兰赛尔城交给王国军\x01",
            "应该没问题吧。)\x02\x03",

            "（我们还是赶快\x01",
            "  去西街区那边吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F29")

    label("loc_EE0")


    ChrTalk(    #30
        0x103,
        (
            "#022F（格兰赛尔城交给王国军\x01",
            "应该没问题吧。)\x02\x03",

            "(我们就赶紧去码头吧。)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F29")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F59")

    ChrTalk(    #31
        0x101,
        "#1002F（嗯，是啊。）\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()
    Jump("loc_F88")

    label("loc_F59")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F88")

    ChrTalk(    #32
        0x109,
        "#1063F（啊啊，是啊。）\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()

    label("loc_F88")

    OP_A2(0x0)
    Jump("loc_1056")

    label("loc_F8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA4")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_FAB")

    label("loc_FA4")

    TurnDirection(0x106, 0x0, 400)

    label("loc_FAB")


    ChrTalk(    #33
        0x106,
        (
            "#050F（格兰赛尔城交给王国军\x01",
            "应该没问题吧。)\x02\x03",

            "(我们就赶紧去码头吧。)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1024")

    ChrTalk(    #34
        0x101,
        "#1002F（嗯，是啊。）\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()
    Jump("loc_1053")

    label("loc_1024")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1053")

    ChrTalk(    #35
        0x109,
        "#1063F（啊啊，是啊。）\x02",
    )

    TurnDirection(0x0, 0x103, 400)
    CloseMessageWindow()

    label("loc_1053")

    OP_A2(0x0)

    label("loc_1056")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0xC, 180, 0)
    OP_4B(0xC, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_8_E01 end

    def Function_9_107D(): pass

    label("Function_9_107D")

    SetPlaceName(0xB4)
    Return()

    # Function_9_107D end

    SaveToFile()

Try(main)
