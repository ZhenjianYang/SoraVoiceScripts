from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3119   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3119.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3119   ._SN',
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
        '拉赛尔博士',                           # 9
        '艾莉卡',                               # 10
        '丹',                                   # 11
        '特莱斯主任',                           # 12
        '威尔姆',                               # 13
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH02620 ._CH',             # 01
        'ED6_DT07/CH01190 ._CH',             # 02
        'ED6_DT07/CH01540 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
        'ED6_DT27/CH03970 ._CH',             # 05
        'ED6_DT27/CH03980 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH02620P._CP',             # 01
        'ED6_DT07/CH01190P._CP',             # 02
        'ED6_DT07/CH01540P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
        'ED6_DT27/CH03970P._CP',             # 05
        'ED6_DT27/CH03980P._CP',             # 06
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
        Direction           = 180,
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
        Direction           = 180,
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
        X                   = -440,
        Z                   = 0,
        Y                   = 10490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4650,
        Z                   = 1000,
        Y                   = 6180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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


    DeclEvent(
        X                   = -106990,
        Y                   = 0,
        Z                   = -550,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -540,
        TriggerZ            = 0,
        TriggerY            = 6300,
        TriggerRange        = 800,
        ActorX              = -540,
        ActorZ              = 900,
        ActorY              = 6300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_21C",          # 01, 1
        "Function_2_235",          # 02, 2
        "Function_3_2DC",          # 03, 3
        "Function_4_42E",          # 04, 4
        "Function_5_5B6",          # 05, 5
        "Function_6_10C7",         # 06, 6
        "Function_7_1141",         # 07, 7
        "Function_8_1169",         # 08, 8
        "Function_9_1201",         # 09, 9
        "Function_10_122C",        # 0A, 10
        "Function_11_2A95",        # 0B, 11
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FC")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    label("loc_1FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_21B")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_21B")

    Return()

    # Function_0_1E6 end

    def Function_1_21C(): pass

    label("Function_1_21C")

    OP_71(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x415, 0x0)
    ExitThread()
    Return()

    # Function_1_21C end

    def Function_2_235(): pass

    label("Function_2_235")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_266"),
        (1, "loc_272"),
        (2, "loc_27E"),
        (3, "loc_28A"),
        (4, "loc_296"),
        (5, "loc_2A2"),
        (6, "loc_2AE"),
        (SWITCH_DEFAULT, "loc_2BA"),
    )


    label("loc_266")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_2C6")

    label("loc_272")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_2C6")

    label("loc_27E")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_2C6")

    label("loc_28A")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_2C6")

    label("loc_296")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2C6")

    label("loc_2A2")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_2C6")

    label("loc_2AE")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2C6")

    label("loc_2BA")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2C6")

    label("loc_2C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2C6")

    label("loc_2DB")

    Return()

    # Function_2_235 end

    def Function_3_2DC(): pass

    label("Function_3_2DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_42A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_397")

    ChrTalk(    #0
        0xFE,
        (
            "其实艾莉卡博士也提出了\x01",
            "卡佩尔计划的概要书呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "但是因为和拉赛尔博士打赌输了，\x01",
            "所以不得不撤下自己的计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "反正无论谁掌主导权，\x01",
            "我们都会一样辛苦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42A")

    label("loc_397")


    ChrTalk(    #3
        0xFE,
        (
            "哎呀哎呀，\x01",
            "正想着卡佩尔系统修复工作终于结束了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "又有别的新发明了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "真是的，\x01",
            "拉赛尔家人的精力就是不一样啊。\x02",
        )
    )

    Jump("loc_426")

    label("loc_426")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_42A")

    TalkEnd(0xFE)
    Return()

    # Function_3_2DC end

    def Function_4_42E(): pass

    label("Function_4_42E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_5B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4F1")

    ChrTalk(    #6
        0xFE,
        (
            "这个系统\x01",
            "是由许多单元\x01",
            "组合起来的。\x02",
        )
    )

    Jump("loc_474")

    label("loc_474")

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "虽然卡佩尔本体没问题，\x01",
            "但系统数据的恢复和调整\x01",
            "还是要花两个月以上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "那种奇怪的现象\x01",
            "最好别再出现了…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B2")

    label("loc_4F1")


    ChrTalk(    #9
        0xFE,
        (
            "………………喏，\x01",
            "就是那个导力停止现象啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "在那之后启动卡佩尔系统时，\x01",
            "好像就发生误操作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "…………所有数据\x01",
            "都被删除了！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "修复就花了两个月以上时间，\x01",
            "真是可恶啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_5B2")

    TalkEnd(0xFE)
    Return()

    # Function_4_42E end

    def Function_5_5B6(): pass

    label("Function_5_5B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(820, 0, 12190, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_72(0x415, 0x0)
    ExitThread()
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x11, -430, 0, 10460, 0)
    SetChrPos(0x107, -1670, 0, 2060, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x11,
        (
            "#1452F…………这就是\x01",
            "『帕蒂尔·玛蒂尔』……\x02\x03",

            "看起来，\x01",
            "发挥出来的实力还不到１０％……\x02\x03",

            "#1457F原来如此，\x01",
            "的确是强悍的规格啊……\x02",
        )
    )

    Jump("loc_6FD")

    label("loc_6FD")

    CloseMessageWindow()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #14
        0x107,
        "#061F#1P妈妈！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(500)
    SetChrPos(0x107, 950, 0, 2620, 0)

    def lambda_740():
        OP_8E(0xFE, 0x3B6, 0x0, 0x1F18, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_740)
    WaitChrThread(0x107, 0x1)

    def lambda_760():
        OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x22F6, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_760)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 0, 500)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x107,
        (
            "#064F#12P咦，这是……\x02\x03",

            "帕蒂尔·玛蒂尔的数据？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x107, 500)
    Sleep(300)

    ChrTalk(    #16
        0x11,
        "#1450F#5P哎呀提妲，来得正好。\x02",
    )

    CloseMessageWindow()

    def lambda_836():
        OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x274C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_836)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #17
        0x11,
        (
            "#1456F#5P那个，提妲。\x01",
            "你看过这东西的实体吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        (
            "#560F#12P咦…………？\x01",
            "嗯、嗯……\x02\x03",

            "看倒是看过……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x11,
        (
            "#1451F#5P实物是怎样的感觉呢！？\x02\x03",

            "喂，告诉我告诉我～！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_920():
        OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x25E4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_920)
    WaitChrThread(0x11, 0x1)

    def lambda_940():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_940)
    Sleep(1000)

    ChrTalk(    #20
        0x107,
        (
            "#067F#12P嗯………………\x01",
            "嗯，那个……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #21
        0x107,
        (
            "#561F#12P我、我不太清楚……\x01",
            "就是很大很大……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E8():
        OP_8F(0xFE, 0xFFFFFE52, 0x0, 0x274C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9E8)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #22
        0x11,
        (
            "#1833F#5P啊……确实是啊。\x02\x03",

            "#1833F你这身高抬头看\x01",
            "也看不清楚呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        (
            "#0564F#12P那个，妈妈……\x02\x03",

            "你为什么在看\x01",
            "帕蒂尔·玛蒂尔的数据呢？\x02\x03",

            "那个，新发明是……？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 500)
    Sleep(600)
    OP_8C(0x107, 80, 500)
    Sleep(600)
    OP_8C(0x107, 0, 500)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x107,
        "#064F#12P难、难不成……！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, -1670, 0, 2060, 0)

    NpcTalk(    #25
        0x10,
        "声音",
        "#1P一点不错。\x02",
    )

    Jump("loc_B82")

    label("loc_B82")

    CloseMessageWindow()
    OP_59()
    OP_20(0xBB8)
    SetChrPos(0x10, -170, 0, 500, 0)
    SetChrPos(0x12, -910, 0, -210, 0)

    def lambda_BB1():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_BB1)

    def lambda_BBF():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_BBF)

    def lambda_BCD():
        OP_6D(-430, 0, 8650, 2500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_BCD)

    def lambda_BE5():
        OP_6C(0, 2500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BE5)

    def lambda_BF5():
        OP_67(0, 5540, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_BF5)

    def lambda_C0D():
        OP_8E(0xFE, 0xFFFFFF56, 0x0, 0x111C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C0D)
    Sleep(500)

    def lambda_C2D():
        OP_8E(0xFE, 0xFFFFFC72, 0x0, 0xE10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C2D)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #26
        0x12,
        (
            "#1460F#6P这边已经准备完毕。\x01",
            "随时可以开始作业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        (
            "#1456F#5P好，看来人已经齐了呢。\x02\x03",

            "#1457F……现在我们\x01",
            "开始着手开发\x01",
            "能够对抗帕蒂尔·玛蒂尔的人形兵器。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0x11,
        "#1455F#3S『导力装甲』计划，启动！！#2S\x02",
    )

    OP_7C(0x0, 0x190, 0xFA0, 0x12C)
    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0x107, 0x11, 600)
    Sleep(500)
    OP_63(0x107)

    ChrTalk(    #29
        0x107,
        "#065F#6P#3S咦咦～～～！！？\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x12C)
    CloseMessageWindow()
    FadeToDark(2000, 0, -1)

    def lambda_DBB():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_DBB)
    OP_0D()
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Sleep(3000)
    OP_6D(820, 0, 12190, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    SetChrPos(0x107, -430, 0, 10460, 0)
    OP_1D(0x53)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #30
        0x107,
        (
            "#062F#40W『帕蒂尔·玛蒂尔』……\x02\x03",

            "为什么，为什么……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)
    OP_8C(0x107, 180, 400)
    Sleep(300)

    def lambda_EBD():
        OP_6D(630, 0, 11140, 2000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_EBD)

    def lambda_ED5():
        OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x2210, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_ED5)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x107, 0x2)
    Sleep(300)

    ChrTalk(    #31
        0x107,
        (
            "#063F#5P（每次听到有新发明，\x01",
            "  我总是感到非常高兴。）\x02\x03",

            "（然后忘记一切，\x01",
            "  和爷爷一起\x01",
            "  投入其中……）\x02\x03",

            "（但是今天，\x01",
            "  却感到有一点点悲伤…………）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS583._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)

    ChrTalk(    #32
        0x107,
        "#562F#5P……这样，真的好吗……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1035():
        OP_6D(630, 0, 12500, 1500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1035)

    def lambda_104D():
        OP_67(0, 4500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_104D)
    OP_8C(0x107, 0, 300)
    WaitChrThread(0x107, 0x2)
    Sleep(500)

    ChrTalk(    #33
        0x107,
        "#063F#12P#40W玲…………\x02",
    )

    CloseMessageWindow()

    def lambda_109A():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_109A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3115   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_5_5B6 end

    def Function_6_10C7(): pass

    label("Function_6_10C7")

    OP_8C(0x10, 180, 500)
    OP_62(0x10, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    def lambda_10EB():
        OP_8E(0xFE, 0xFFFFFEF2, 0x0, 0x46A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_10EB)
    WaitChrThread(0x10, 0x1)

    def lambda_110B():
        OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0x1AE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_110B)
    WaitChrThread(0x10, 0x1)

    def lambda_112B():
        OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0xFFFFFA6A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_112B)
    Return()

    # Function_6_10C7 end

    def Function_7_1141(): pass

    label("Function_7_1141")

    OP_8C(0x12, 180, 500)
    Sleep(300)

    def lambda_1153():
        OP_8E(0xFE, 0xFFFFFC72, 0x0, 0xFFFFFA2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1153)
    Return()

    # Function_7_1141 end

    def Function_8_1169(): pass

    label("Function_8_1169")

    OP_62(0x11, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    def lambda_1186():
        OP_8E(0xFE, 0xFFFFF8E4, 0x0, 0x2274, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1186)
    WaitChrThread(0x11, 0x1)

    def lambda_11A6():
        OP_8E(0xFE, 0xFFFFF8E4, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_11A6)
    WaitChrThread(0x11, 0x1)

    def lambda_11C6():
        OP_8E(0xFE, 0xFFFFFC04, 0x0, 0x2BC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_11C6)
    WaitChrThread(0x11, 0x1)

    def lambda_11E6():
        OP_8E(0xFE, 0xFFFFFC04, 0x0, 0xFFFFFA2E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_11E6)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_8_1169 end

    def Function_9_1201(): pass

    label("Function_9_1201")

    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)
    OP_8C(0x107, 0, 600)
    Sleep(1000)
    OP_8C(0x107, 180, 600)
    Return()

    # Function_9_1201 end

    def Function_10_122C(): pass

    label("Function_10_122C")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-200, 0, 7100, 1000)
    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("CAPEL")
    SetMessageWindowPos(250, 78, 36, 12)

    AnonymousTalk(    #34
        (
            "\x07\x02#1SThe Orbal Calculator\x01",
            "CAPEL SYSTEM Ver.7.0\x01",
            "Copyright(C)Z.C.F. 1197-1202\x01",
            "MODE:Information Retrieval\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W..........#20WOK!\x01",
            "#200W　#20W\x01",
            "#1S已连接到数据库。\x01",
            "请选择要搜索的内容。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_133D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A72")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        55,
        80,
        1,
        "【中央工房相关】　　\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_138B"),
        (SWITCH_DEFAULT, "loc_2A62"),
    )


    label("loc_138B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A52")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        55,
        153,
        1,
        (
            "【设立·沿革】\x01",            # 0
            "【技术一览】\x01",              # 1
            "【相关信息搜索】　　\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13F4"),
        (1, "loc_1A57"),
        (2, "loc_2743"),
        (SWITCH_DEFAULT, "loc_2A42"),
    )


    label("loc_13F4")


    AnonymousTalk(    #35
        (
            "\x07\x02#1S【Ｓ１１５４】（Ｓ…七耀历）\x01",
            "Ｃ·爱普斯泰恩博士于列曼自治州去世。\x01",
            "【Ｓ１１５５】\x01",
            "Ａ·拉赛尔博士回到利贝尔王国。\x01",
            "回国后提倡普及导力器技术，\x01",
            "但是没得到世人的认可和支持。\x01",
            "【Ｓ１１５７】\x01",
            "拉赛尔博士带领蔡斯的钟表工匠普及导力器。\x01",
            "同年，『蔡斯技术工房』（即之后的中央工房）设立。\x01",
            "【Ｓ１１６０】\x01",
            "埃德佳Ⅲ世在视察蔡斯技术工房后提供巨额资金建设工\x01",
            "房。拉赛尔博士出任首任工房长。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #36
        (
            "\x07\x02#1S【Ｓ１１６２】\x01",
            "埃德佳Ⅲ世去世。艾莉茜雅Ⅱ世即位。\x01",
            "【Ｓ１１６４】\x01",
            "『伦格兰德大桥』落成。\x01",
            "【Ｓ１１６８】\x01",
            "首部导力飞艇『加拉托拉巴号』诞生。\x01",
            "（经过３９次飞行实验失败后的产物）\x01",
            "【Ｓ１１７３】\x01",
            "蔡斯技术工房开始对共和国乌尔努社和帝国莱恩福尔特\x01",
            "社输出导力器技术。工房改名为『中央工房』。\x01",
            "【Ｓ１１７５】\x01",
            "飞艇公社设立。定期船『林德号』开始服役。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #37
        (
            "\x07\x02#1S【Ｓ１１７７】\x01",
            "定期船『赛希莉亚号』开始服役。\x01",
            "【Ｓ１１７８】\x01",
            "移动工房船『莱普尼兹号』开始服役。\x01",
            "【Ｓ１１８０】\x01",
            "中央工房搬迁（即现在的建筑物）。\x01",
            "开掘卡鲁迪亚平原丘陵的一角，地下工房建成。\x01",
            "【Ｓ１１８２】\x01",
            "拉赛尔工房长退休。\x01",
            "玛多克技术主任出任第二任工房长。\x01",
            "【Ｓ１１８５】\x01",
            "自然科学和医学研究部门设立。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #38
        (
            "\x07\x02#1S【Ｓ１１８７】\x01",
            "客船『埃迪鲁那号』在卡尔瓦德领海沉没。\x01",
            "尤迪斯王太子夫妇去世。\x01",
            "【Ｓ１１９０】\x01",
            "与爱普斯泰恩财团合作，\x01",
            "发表了『导力网络』的构想。\x01",
            "【Ｓ１１９２】\x01",
            "『百日战役』爆发。\x01",
            "中央工房被埃雷波尼亚帝国接管。\x01",
            "拉赛尔博士在雷斯顿要塞开发出警备飞艇，\x01",
            "并将其用于反攻作战中，取得了显赫的战功，\x01",
            "从此警备飞艇作为王国军的主力兵器而被使用。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #39
        (
            "\x07\x02#1S【Ｓ１１９３】\x01",
            "利贝尔王国和埃雷波尼亚帝国缔结和平条约。\x01",
            "战后，王国再次向帝国输出导力器。\x01",
            "【Ｓ１１９７】\x01",
            "导力演算器『卡佩尔』Ver.1完成。\x01",
            "【Ｓ１１９９】\x01",
            "高速巡洋舰『埃尔赛尤号』开发工程开始。\x01",
            "【Ｓ１２０２】\x01",
            "高速巡洋舰『埃尔赛尤号』竣工，进入试飞阶段。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4F")

    label("loc_1A57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2733")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AF5")

    Menu(
        2,
        55,
        259,
        1,
        (
            "【导力器】\x01",              # 0
            "【结晶回路】\x01",            # 1
            "【七耀石】\x01",              # 2
            "【导力飞艇】\x01",            # 3
            "【导力兵器】\x01",            # 4
            "【战术导力器】\x01",          # 5
            "【游击士协会招牌】\x01",      # 6
        )
    )

    Jump("loc_1B4A")

    label("loc_1AF5")


    Menu(
        2,
        55,
        259,
        1,
        (
            "【导力器】\x01",          # 0
            "【结晶回路】\x01",        # 1
            "【七耀石】\x01",          # 2
            "【导力飞艇】\x01",        # 3
            "【导力兵器】\x01",        # 4
            "【战术导力器】\x01",      # 5
        )
    )


    label("loc_1B4A")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B72"),
        (1, "loc_1CFD"),
        (2, "loc_1DC9"),
        (3, "loc_1EDF"),
        (4, "loc_201F"),
        (5, "loc_2199"),
        (6, "loc_24CD"),
        (SWITCH_DEFAULT, "loc_2723"),
    )


    label("loc_1B72")


    AnonymousTalk(    #40
        (
            "\x07\x02#1S项目：导力器（Orbment）\x01",
            "在半世纪前由Ｃ·爱普斯泰恩博士所发明，是能从七耀\x01",
            "石中提取导力，从而引发各种各样现象的机械装置的总\x01",
            "称。导力器内部的构造和齿轮的运动，使加工七耀石而\x01",
            "成的结晶回路相互干涉，可以引发丰富多彩的现象。导\x01",
            "力器的实用性，除了能产生丰富现象以外，还在于拥有\x01",
            "『经过一段时间内部的导力可以自然恢复』这种特异的\x01",
            "便利性。另外，经济效率也要远远地领先于各种外燃、\x01",
            "内燃引擎设备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2730")

    label("loc_1CFD")


    AnonymousTalk(    #41
        (
            "\x07\x02#1S项目：结晶回路（Quartz）\x01",
            "将七耀石的碎片（耀晶片，Sepith）精制、加工而成的\x01",
            "具有结晶构造的回路。作为能量源的同时，本身还是引\x01",
            "起各种各样现象的装置。但结晶回路必须安装在导力器\x01",
            "内才可以发挥作用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2730")

    label("loc_1DC9")


    AnonymousTalk(    #42
        (
            "\x07\x02#1S项目：七耀石（Septium）\x01",
            "是在大陆全土分布的７种贵重矿石的总称。因被人们称\x01",
            "为『古代的宝石』、『神秘的象征』而变得珍重。近代\x01",
            "一种将体积过小不能成为宝石的碎片（耀晶片）精制加\x01",
            "工制作出结晶回路的技术被发明出来，因此导致七耀石\x01",
            "资源的重要性在大陆诸国一夜之间变得十分重要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2730")

    label("loc_1EDF")


    AnonymousTalk(    #43
        (
            "\x07\x02#1S项目：导力飞艇\x01",
            "导力飞艇可以称得上是导力技术精华凝聚而成的结晶。\x01",
            "集合了用于重力制御的大型飞翔装置和供给大量能量的\x01",
            "导力引擎两大技术，使得如此大的飞艇在空中飞行成为\x01",
            "可能。\x01",
            "为了实现高效率的导力传送和十分复杂的船体控制，最\x01",
            "新的飞艇大多搭载了高性能的导力演算器。２０亚矩以\x01",
            "上的大型飞艇又被称为『飞船』。\x02",
        )
    )

    Jump("loc_201B")

    label("loc_201B")

    CloseMessageWindow()
    Jump("loc_2730")

    label("loc_201F")


    AnonymousTalk(    #44
        (
            "\x07\x02#1S项目：导力兵器\x01",
            "即以导力枪、导力炮作为代表，使用导力技术的兵器体\x01",
            "系。现在已成为大多数国家军队的主力装备。\x01",
            "导力枪枪管内具有能将能量按照螺旋线聚集并高速射出\x01",
            "豆粒大小的金属子弹的构造，与发射火药的枪相比，填\x01",
            "弹量大幅增加，而且还能够调节枪的威力。\x01",
            "导力炮则可以发射封装了能量的炮弹（导力弹）并产生\x01",
            "爆炸，与发射火药的炮相比，其后坐力小，而且也可以\x01",
            "自由调节威力大小。\x01",
            "　\x02",
        )
    )

    Jump("loc_2195")

    label("loc_2195")

    CloseMessageWindow()
    Jump("loc_2730")

    label("loc_2199")


    AnonymousTalk(    #45
        (
            "\x07\x02#1S项目：战术导力器\x01",
            "可以发动导力魔法的导力器。大小和怀表差不多，内部\x01",
            "构造则相当精致优雅。\x01",
            "战术导力器具有安装结晶回路后能够提高持有者能力的\x01",
            "设计，使内部结晶回路与持有者达到同步，引发出『共\x01",
            "鸣现象』，以代替传统释放魔法所需的复杂的齿轮和驱\x01",
            "动装置，使持有者能够发动各种导力魔法。\x01",
            "而且，根据复数结晶回路属性和性能的组合不同，持有\x01",
            "者能够使用的导力魔法也会发生变化，具有相当的灵活\x01",
            "性。\x01",
            "　\x02",
        )
    )

    Jump("loc_2326")

    label("loc_2326")

    CloseMessageWindow()

    AnonymousTalk(    #46
        (
            "\x07\x02#1S追加：新型战术导力器\x01",
            "作为战术导力器的开发者，爱普斯泰恩财团对过去的型号进\x01",
            "行大幅改良，并且成功投入实用的新规格战术导力器。和过\x01",
            "去只有六个结晶回路插槽的旧型号相比，这种新型号则具备\x01",
            "了七个结晶回路插槽，可以实现更为灵活的结晶回路组合。\x01",
            "新型号不仅使可以使用的魔法变得多元化，而且使其威力也\x01",
            "得到了飞跃性的提升。但是，由于新型号和过去型号的基本\x01",
            "构造有很大的不同，新型战术导力器也有着无法互换结晶回\x01",
            "路的缺陷。\x01",
            "　\x02",
        )
    )

    Jump("loc_24C9")

    label("loc_24C9")

    CloseMessageWindow()
    Jump("loc_2730")

    label("loc_24CD")

    OP_28(0x6C, 0x1, 0x8)

    AnonymousTalk(    #47
        (
            "\x07\x02#1S内容：游击士协会招牌\x01",
            "这就是英俊潇洒的怪盗绅士布卢布兰凭借其天才般的超级无\x01",
            "敌手腕从傻瓜般的超级无能游击士协会之一的蔡斯支部的檐\x01",
            "头偷走的金属招牌。虽然没什么经济价值，不过给予协会相\x01",
            "关人员的打击是无穷的，正在读此文的诸位想必也强烈地感\x01",
            "受到了屈辱感吧。好了，闲话到此为止。该是时候给出下一\x01",
            "个提示了。\x01",
            "　\x01",
            "　　┌──────────────────┐　　\x01",
            "　　│　　　　第３把钥匙再次位于市内。　　│　\x01",
            "　　│      抬头看那『尖帽子三兄弟』吧。  │　　\x01",
            "　　└──────────────────┘\x01",
            "　※另外，这个记录会自动删除。　　　　\x01",
            "　　所以再次极力推荐诸位赶快做好应做的笔记！　\x02",
        )
    )

    Jump("loc_271F")

    label("loc_271F")

    CloseMessageWindow()
    Jump("loc_2730")

    label("loc_2723")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2730")

    label("loc_2730")

    Jump("loc_1A57")

    label("loc_2733")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_2A4F")

    label("loc_2743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A32")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        55,
        255,
        1,
        (
            "【内燃引擎设备】\x01",      # 0
            "【汽油】\x01",              # 1
            "【运输车】\x01",            # 2
        )
    )

    Jump("loc_2794")

    label("loc_2794")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27AC"),
        (1, "loc_2887"),
        (2, "loc_2943"),
        (SWITCH_DEFAULT, "loc_2A22"),
    )


    label("loc_27AC")


    AnonymousTalk(    #48
        (
            "\x07\x02#1S项目：内燃引擎设备\x01",
            "在机关装置内燃烧燃料以获得能量的动力源。与导力机\x01",
            "关相比经济效率低下，而且还会产生噪音、废气等各种\x01",
            "问题，因此已经停止开发和生产。\x01\x01",
            "『内燃引擎设备』\x01",
            "库存量：１台\x01",
            "管理责任人：格斯塔夫维修长\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2F")

    label("loc_2887")


    AnonymousTalk(    #49
        (
            "\x07\x02#1S项目：汽油\x01",
            "将天然产生的液态碳氢化合物（石油）分馏、精制而成\x01",
            "的液体。常作为内燃引擎设备的燃料以及工业生产的溶\x01",
            "剂使用。\x01\x01",
            "库存：中型桶×４０\x01",
            "保管地点：导力器生产工场\x02",
        )
    )

    Jump("loc_293F")

    label("loc_293F")

    CloseMessageWindow()
    Jump("loc_2A2F")

    label("loc_2943")

    OP_28(0x29, 0x1, 0x8000)

    AnonymousTalk(    #50
        (
            "\x07\x02#1S项目：运输车\x01",
            "使用导力引擎驱动的各种车辆的总称。因为乘坐的舒适\x01",
            "度较差，速度也很慢，所以基本不用于客运方面，而主\x01",
            "要用来进行中短距离的货物运输。\x01\x01",
            "『运输车用驱动导力器』\x01",
            "库存量：不明\x01",
            "保管地点：地下工场搬入口\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2F")

    label("loc_2A22")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A2F")

    label("loc_2A2F")

    Jump("loc_2743")

    label("loc_2A32")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_2A4F")

    label("loc_2A42")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A4F")

    label("loc_2A4F")

    Jump("loc_138B")

    label("loc_2A52")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Jump("loc_2A6F")

    label("loc_2A62")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A6F")

    label("loc_2A6F")

    Jump("loc_133D")

    label("loc_2A72")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x1)
    Return()

    # Function_10_122C end

    def Function_11_2A95(): pass

    label("Function_11_2A95")

    SetPlaceName(0x9A)
    Return()

    # Function_11_2A95 end

    SaveToFile()

Try(main)
