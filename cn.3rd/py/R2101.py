from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2101.x',
        MapIndex            = 100,
        MapDefaultBGM       = "ed60029",
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
        '玛诺利亚村方向',                       # 9
        '巴伦诺灯塔方向',                       # 10
        '古罗尼山道方向',                       # 11
        '波利',                                 # 12
        '目标用照相机',                         # 13
        '克拉姆',                               # 14
        '玛丽',                                 # 15
        '达尼艾尔',                             # 16
        '特蕾莎院长',                           # 17
        '库拉茨',                               # 18
        '',                                     # 19
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
        'ED6_DT07/CH02500 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02640 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH01260 ._CH',             # 05
        'ED6_DT26/CH20404 ._CH',             # 06
        'ED6_DT26/CH20707 ._CH',             # 07
        'ED6_DT26/CH20704 ._CH',             # 08
        'ED6_DT26/CH20703 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02500P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02640P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH01260P._CP',             # 05
        'ED6_DT26/CH20404P._CP',             # 06
        'ED6_DT26/CH20707P._CP',             # 07
        'ED6_DT26/CH20704P._CP',             # 08
        'ED6_DT26/CH20703P._CP',             # 09
    )

    DeclNpc(
        X                   = 13030,
        Z                   = -2070,
        Y                   = -137400,
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
        X                   = -72540,
        Z                   = -1880,
        Y                   = -134520,
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
        X                   = -18980,
        Z                   = -2000,
        Y                   = 6950,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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


    DeclEvent(
        X                   = -22120,
        Y                   = -3060,
        Z                   = -30980,
        Range               = -12380,
        Unknown_10          = 0xBF4,
        Unknown_14          = 0xFFFF9098,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -20260,
        Y                   = -2980,
        Z                   = -48950,
        Range               = -29910,
        Unknown_10          = 0xBA4,
        Unknown_14          = 0xFFFF48AE,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -16190,
        Y                   = -3020,
        Z                   = -46690,
        Range               = 2410,
        Unknown_10          = 0xB9A,
        Unknown_14          = 0xFFFF41F6,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -67840,
        Y                   = -3000,
        Z                   = -116100,
        Range               = -78240,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFE30B8,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = -16670,
        TriggerZ            = -1970,
        TriggerY            = -43720,
        TriggerRange        = 1500,
        ActorX              = -16670,
        ActorZ              = -300,
        ActorY              = -43720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20680,
        TriggerZ            = -2009,
        TriggerY            = -44860,
        TriggerRange        = 1500,
        ActorX              = -20680,
        ActorZ              = -350,
        ActorY              = -44860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_302",          # 00, 0
        "Function_1_329",          # 01, 1
        "Function_2_3A4",          # 02, 2
        "Function_3_898",          # 03, 3
        "Function_4_A76",          # 04, 4
        "Function_5_C59",          # 05, 5
        "Function_6_284A",         # 06, 6
        "Function_7_28B8",         # 07, 7
        "Function_8_2909",         # 08, 8
    )


    def Function_0_302(): pass

    label("Function_0_302")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_328")
    OP_A2(0x1)
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_328")

    Return()

    # Function_0_302 end

    def Function_1_329(): pass

    label("Function_1_329")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFD0648, 0x23002C)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351")
    OP_22(0x1C4, 0x1, 0x64)

    label("loc_351")

    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_B2(0x0, 0x3, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_380")
    OP_B2(0x1, 0x0, 0x80)
    Jump("loc_385")

    label("loc_380")

    OP_B2(0x1, 0x3, 0x80)

    label("loc_385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_3A3")
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A3")
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)

    label("loc_3A3")

    Return()

    # Function_1_329 end

    def Function_2_3A4(): pass

    label("Function_2_3A4")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-17140, -1600, -30940, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -17140, -2000, -35940, 0)
    SetChrPos(0x14F, -17140, -2000, -37940, 0)

    def lambda_421():
        OP_8E(0xFE, 0xFFFFBD0C, 0xFFFFF830, 0xFFFFBDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_421)

    def lambda_43C():
        OP_8E(0xFE, 0xFFFFBD0C, 0xFFFFF830, 0xFFFF96C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_43C)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x8, 0x9, 0xC8, 0x5)
    Sleep(2000)
    OP_63(0x14E)
    Sleep(1000)

    def lambda_489():
        OP_6D(-17140, -1600, -26940, 6000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_489)

    def lambda_4A1():
        OP_6B(2520, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4A1)

    ChrTalk(    #0 op#A op#5
        0x14E,
        (
            "#1718F#50A对了波利，\x01",
            "幸福之石是什么样子的呢？\x05\x02\x03",

            "#57A是不是和欧尼尔先生说的一样\x01",
            "是闪闪发光的金色呢……？\x05\x02\x03",

            "#1903F#45A啊，一定是很漂亮的石头吧……㈱\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    WaitChrThread(0x14F, 0x1)
    WaitChrThread(0x14, 0x0)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14F, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14F)
    OP_8C(0x14F, 90, 400)
    Sleep(1000)

    ChrTalk(    #1
        0x14F,
        "#1733F哦…………？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x1)
    FadeToDark(2000, 0, -1)

    def lambda_5C4():
        OP_6B(2420, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5C4)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x14E, -17380, -2000, -24340, 0)
    SetChrPos(0x14F, -14100, -2000, -23800, 0)
    OP_6D(-18980, -1600, -17900, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)

    def lambda_639():
        OP_8E(0xFE, 0xFFFFB5DC, 0xFFFFF830, 0xFFFFBA14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_639)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #2 op#A op#5
        0x14E,
        (
            "#1714F#45A我、我倒不是\x01",
            "真的相信欧尼尔先生的话哦？\x05\x02\x03",

            "#1719F#42A只是在想，说不定很适合\x01",
            "拿来当作送给老师的礼物呢～……！\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 180, 400)
    Sleep(500)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #3
        0x14E,
        "#1714F咦，波利！？\x02",
    )

    CloseMessageWindow()

    def lambda_743():
        OP_6D(-18020, -1700, -26860, 2500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_743)

    def lambda_75B():
        OP_8E(0xFE, 0xFFFFB99C, 0xFFFFF830, 0xFFFF9714, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_75B)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 140, 500)
    Sleep(800)
    OP_8C(0x14E, 260, 500)
    Sleep(1000)
    OP_8C(0x14E, 180, 500)
    Sleep(400)

    ChrTalk(    #4
        0x14E,
        (
            "#1712F难、难不成……\x01",
            "…………迷路了？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_8C(0x14E, 30, 500)
    Sleep(500)
    OP_8C(0x14E, 120, 500)
    Sleep(300)
    OP_8C(0x14E, 270, 500)
    Sleep(500)
    OP_8C(0x14E, 350, 500)
    Sleep(300)
    OP_63(0x14E)

    ChrTalk(    #5
        0x14E,
        "#1712F#3S波利！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 500)
    Sleep(300)

    ChrTalk(    #6
        0x14E,
        (
            "#1717F#3S波利！\x01",
            "跑到哪里去了！？#2S\x02",
        )
    )

    CloseMessageWindow()
    RemoveParty(0x4E, 0x0)
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2F22)
    EventEnd(0x0)
    Return()

    # Function_2_3A4 end

    def Function_3_898(): pass

    label("Function_3_898")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-23280, -1910, -46940, 0)
    OP_67(0, 3580, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(82000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -24460, -1910, -47120, 228)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_8C(0x14E, 304, 400)
    Sleep(800)
    OP_8C(0x14E, 135, 400)
    Sleep(800)

    ChrTalk(    #7
        0x14E,
        "#1717F#3S波利、波利！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x14E, 228, 400)
    Sleep(500)

    ChrTalk(    #8
        0x14E,
        (
            "#1715F真是的，\x01",
            "都说不要走散了啦！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -12140, -2000, -44260, 308)

    def lambda_9AD():
        OP_8E(0xFE, 0xFFFFBB54, 0xFFFFF830, 0xFFFF7338, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9AD)

    def lambda_9C8():
        OP_6D(-23570, -1960, -45850, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_9C8)

    def lambda_9E0():
        OP_67(0, 3580, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9E0)

    def lambda_9F8():
        OP_6C(70000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_9F8)
    Sleep(4500)

    ChrTalk(    #9
        0x14E,
        (
            "#1713F波利跑到哪里去了呢。\x02\x03",

            "#1716F……唉，真是没办法啊。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    SetChrFlags(0x13, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2F23)
    EventEnd(0x0)
    Return()

    # Function_3_898 end

    def Function_4_A76(): pass

    label("Function_4_A76")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-11330, -2000, -46400, 0)
    OP_67(0, 4620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(277000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -10050, -2000, -46560, 135)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_8C(0x14E, 50, 400)
    Sleep(800)
    OP_8C(0x14E, 230, 400)
    Sleep(800)

    ChrTalk(    #10
        0x14E,
        "#1717F#3S波利、波利！\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x14E, 135, 400)
    Sleep(500)

    ChrTalk(    #11
        0x14E,
        (
            "#1715F真是的，\x01",
            "都说不要走散了啦！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrPos(0x13, -19940, -2000, -43700, 0)

    def lambda_B90():
        OP_8E(0xFE, 0xFFFFC824, 0xFFFFF830, 0xFFFF7400, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B90)

    def lambda_BAB():
        OP_6D(-12720, -2000, -44240, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_BAB)

    def lambda_BC3():
        OP_67(0, 4620, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BC3)

    def lambda_BDB():
        OP_6C(280000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_BDB)
    Sleep(4500)

    ChrTalk(    #12
        0x14E,
        (
            "#1713F波利跑到哪里去了呢。\x02\x03",

            "#1716F……唉，真是没办法啊。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    SetChrFlags(0x13, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2F23)
    EventEnd(0x0)
    Return()

    # Function_4_A76 end

    def Function_5_C59(): pass

    label("Function_5_C59")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_23(0x1C4)
    OP_6D(-12640, -1900, -34160, 0)
    OP_67(0, 4360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(43000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -12640, -2300, -34160, 260)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x40)
    SetChrPos(0x19, -13040, -2000, -35500, 346)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrPos(0x13, -14100, -2000, -34800, 100)
    SetChrChipByIndex(0x14E, 9)
    SetChrSubChip(0x14E, 0)
    SetChrFlags(0x14E, 0x2)
    SetChrFlags(0x14E, 0x4)
    SetChrFlags(0x14E, 0x800)
    LoadEffect(0x0, "map\\mp074_00.eff")
    LoadEffect(0x1, "map\\mp075_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    Sleep(3000)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #13
        "\x07\x00……喂，没事吗？\x02",
    )

    Jump("loc_D7D")

    label("loc_D7D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #14
        "\x07\x00振作点啊！\x02",
    )

    Jump("loc_DAB")

    label("loc_DAB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_59()
    OP_22(0x1C4, 0x1, 0x64)
    OP_1D(0x76)
    FadeToBright(2000, 0)

    def lambda_DD3():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_DD3)
    Sleep(1000)

    def lambda_DE8():
        OP_9E(0xFE, 0x5, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_DE8)
    Sleep(1000)
    Fade(1000)
    SetChrChipByIndex(0x14E, 8)
    SetChrSubChip(0x14E, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_E48")

    ChrTalk(    #15
        0x19,
        (
            "#821F哦，太好了。\x01",
            "你醒过来了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E84")

    label("loc_E48")


    NpcTalk(    #16
        0x19,
        "男人",
        (
            "#821F#12P哦，太好了。\x01",
            "你醒过来了啊。\x02",
        )
    )

    Jump("loc_E83")

    label("loc_E83")

    CloseMessageWindow()

    label("loc_E84")


    ChrTalk(    #17
        0x13,
        "#1731F#6P玛丽～，你没事吧～？\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0xFFFFFF38, 1500, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)

    def lambda_ED3():
        OP_99(0xFE, 0x0, 0x4, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_ED3)
    WaitChrThread(0x14E, 0x2)

    def lambda_EE8():
        OP_99(0xFE, 0x4, 0x3, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_EE8)
    WaitChrThread(0x14E, 0x2)

    def lambda_EFD():
        OP_99(0xFE, 0x3, 0x4, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_EFD)
    WaitChrThread(0x14E, 0x2)

    def lambda_F12():
        OP_99(0xFE, 0x4, 0x2, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_F12)
    WaitChrThread(0x14E, 0x2)
    Fade(500)
    SetChrSubChip(0x14E, 5)
    Sleep(900)
    SetChrSubChip(0x14E, 7)
    Sleep(800)
    SetChrSubChip(0x14E, 5)
    Sleep(150)
    SetChrSubChip(0x14E, 6)
    Sleep(800)

    ChrTalk(    #18
        0x14E,
        (
            "#1714F#5P哎、哎……？\x02\x03",

            "………………？？\x02\x03",

            "那个奇怪的魔兽呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_FE9")

    ChrTalk(    #19
        0x19,
        (
            "#822F#12P……魔兽！？\x01",
            "你被魔兽袭击了吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102B")

    label("loc_FE9")


    NpcTalk(    #20
        0x19,
        "男人",
        (
            "#822F#12P……魔兽！？\x01",
            "你被魔兽袭击了吗！？\x02",
        )
    )

    Jump("loc_102A")

    label("loc_102A")

    CloseMessageWindow()

    label("loc_102B")

    SetChrSubChip(0x14E, 5)

    ChrTalk(    #21
        0x14E,
        "#1714F#5P啊，不是……\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x13, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(100)
    OP_62(0x19, 0x0, 2000, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x13)
    OP_63(0x19)

    ChrTalk(    #22
        0x13,
        "#1733F#6P这里没有什么魔兽哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14E,
        (
            "#1900F#5P好、好奇怪啊……\x02\x03",

            "#1713F刚才那是做梦吗……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, -12740, -2009, -44900, 350)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x40)
    SetChrPos(0x17, -11980, -2009, -45880, 350)
    Sleep(500)

    ChrTalk(    #24
        0x15,
        "#774F#3S#1P玛丽！#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x17,
        "#1722F#1P玛丽——！\x02",
    )

    CloseMessageWindow()

    def lambda_117E():
        OP_6D(-12020, -2000, -36520, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_117E)

    def lambda_1196():
        OP_6C(44000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1196)
    WaitChrThread(0x14, 0x0)

    def lambda_11AB():
        OP_8E(0xFE, 0xFFFFCD10, 0xFFFFF830, 0xFFFF7554, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_11AB)

    def lambda_11C6():
        OP_8E(0xFE, 0xFFFFD058, 0xFFFFF830, 0xFFFF72D4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_11C6)

    def lambda_11E1():

        label("loc_11E1")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_11E1")

    QueueWorkItem2(0x13, 3, lambda_11E1)

    def lambda_11F2():

        label("loc_11F2")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_11F2")

    QueueWorkItem2(0x19, 3, lambda_11F2)
    Sleep(500)
    SetChrSubChip(0x14E, 7)

    def lambda_120D():
        OP_8F(0xFE, 0xFFFFC568, 0xFFFFF830, 0xFFFF7298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_120D)

    def lambda_1228():
        OP_8F(0xFE, 0xFFFFC658, 0xFFFFF830, 0xFFFF7748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1228)
    Sleep(100)

    def lambda_1248():
        OP_6D(-12500, -2000, -34500, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1248)

    def lambda_1260():
        OP_6B(2860, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1260)

    def lambda_1270():
        OP_6E(254, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1270)
    WaitChrThread(0x19, 0x1)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x17, 0x1)
    OP_44(0x19, 0x3)
    OP_44(0x13, 0x3)
    TurnDirection(0x19, 0x15, 400)
    TurnDirection(0x13, 0x14E, 400)
    Sleep(300)

    ChrTalk(    #26
        0x15,
        (
            "#775F#12P……玛、玛丽！\x01",
            "你没事吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x14E, 65535)
    SetChrSubChip(0x14E, 0)
    ClearChrFlags(0x14E, 0x2)
    ClearChrFlags(0x14E, 0x4)
    ClearChrFlags(0x14E, 0x800)
    TurnDirection(0x14E, 0x15, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0x14E,
        "#1714F#5P嗯、嗯。一点事也没有……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0x15,
        "#778F#12P#3S什么叫一点事也没有啊！！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #29
        0x15,
        (
            "#775F#12P我已经和科洛丝姐姐、\x01",
            "约修亚哥哥他们约好\x01",
            "一定要保护大家的！\x02\x03",

            "#773F要是玛丽有个三长两短，\x01",
            "……那、那我…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x14E,
        "#1714F#5P克拉姆……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    OP_8C(0x15, 180, 500)
    Sleep(400)

    ChrTalk(    #31
        0x15,
        (
            "#773F#6P说、说到底你总是这样，\x01",
            "一个人勉强乱来！\x02\x03",

            "#773F老、老师的生日礼物，\x01",
            "我们大家会一起找的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 0, 500)
    Sleep(400)

    ChrTalk(    #32
        0x15,
        (
            "#778F#12P#3S你别擅自\x01",
            "做这么危险的事啊！#2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14E,
        "#1713F#5P……啊………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x17,
        (
            "#1722F#12P就是啊，玛丽！\x02\x03",

            "我们都担心死了，\x01",
            "你可不能再做这么危险的事了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x13,
        (
            "#1731F#6P大家到处找你呢～。\x02\x03",

            "都是因为玛丽\x01",
            "突然不见了嘛～。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x14E, 270, 400)
    Sleep(500)
    OP_8C(0x14E, 180, 400)
    Sleep(300)

    ChrTalk(    #36
        0x14E,
        (
            "#1713F#5P达尼艾尔…………\x01",
            "波利…………\x02\x03",

            "#1710F对不起，大家……\x02\x03",

            "#1719F…………谢谢你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #37
        0x15,
        (
            "#774F#12P哎……！？\x02\x03",

            "#773F不、不是这样的啦！\x02\x03",

            "#773F只不过，\x01",
            "找礼物时顺便，那个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x17,
        (
            "#1721F#12P那个，克拉姆他啊，\x01",
            "不是忘记在欧尼尔先生的店里\x01",
            "买饰品了吗？\x02\x03",

            "所以他刚才又去义卖会场买东西，\x01",
            "做好了生日宴会的准备～。\x02\x03",

            "#1720F还说『我要是不做，\x01",
            "玛丽会很困扰嘛』～……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    TurnDirection(0x15, 0x17, 500)
    Sleep(400)

    ChrTalk(    #39
        0x15,
        (
            "#776F#6P喂喂，达尼艾尔！\x01",
            "别给我揭穿嘛——！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x17,
        (
            "#1721F#12P然后，\x01",
            "接下来就去古罗尼山道……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1848():
        OP_8E(0xFE, 0xFFFFCF2C, 0xFFFFF830, 0xFFFF7428, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1848)
    WaitChrThread(0x15, 0x1)
    OP_22(0x7D, 0x0, 0x64)

    def lambda_186D():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_186D)

    def lambda_1887():
        OP_8F(0xFE, 0xFFFFCD10, 0xFFFFF830, 0xFFFF7554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1887)
    WaitChrThread(0x15, 0x1)

    def lambda_18A7():
        OP_8E(0xFE, 0xFFFFCF2C, 0xFFFFF830, 0xFFFF7428, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_18A7)
    WaitChrThread(0x15, 0x1)
    OP_22(0x7D, 0x0, 0x64)

    def lambda_18CC():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_18CC)

    def lambda_18E6():
        OP_8F(0xFE, 0xFFFFCD10, 0xFFFFF830, 0xFFFF7554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_18E6)
    WaitChrThread(0x15, 0x1)
    Sleep(300)
    TurnDirection(0x17, 0x15, 500)

    ChrTalk(    #41
        0x17,
        "#1723F#12P好、好痛啊克拉姆！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x14E,
        (
            "#1710F#5P…………………………\x02\x03",

            "（嘿嘿……怎么回事呢。\x01",
            "  我现在觉得好开心……）\x02\x03",

            "#1719F（……感觉好像做了个梦。）\x02\x03",

            "（非常温暖的梦……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1600)

    def lambda_19FA():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_19FA)
    Sleep(150)
    OP_8C(0x17, 0, 500)
    Sleep(250)

    ChrTalk(    #43
        0x15,
        (
            "#775F#12P玛、玛丽！？\x02\x03",

            "是不是\x01",
            "身体不舒服？？\x02",
        )
    )

    Jump("loc_1A5B")

    label("loc_1A5B")

    CloseMessageWindow()
    OP_44(0x19, 0x3)

    def lambda_1A66():

        label("loc_1A66")

        TurnDirection(0xFE, 0x14E, 400)
        OP_48()
        Jump("loc_1A66")

    QueueWorkItem2(0x19, 3, lambda_1A66)

    def lambda_1A77():
        OP_8F(0xFE, 0xFFFFCA68, 0xFFFFF830, 0xFFFF76E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1A77)
    WaitChrThread(0x19, 0x1)

    def lambda_1A97():
        OP_8F(0xFE, 0xFFFFCB6C, 0xFFFFF830, 0xFFFF7A40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1A97)
    WaitChrThread(0x19, 0x1)
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0x19, 6)
    SetChrSubChip(0x19, 1)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_1B05")

    ChrTalk(    #44
        0x19,
        (
            "#822F#1P没事吗？\x01",
            "会不会觉得头晕……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B40")

    label("loc_1B05")


    NpcTalk(    #45
        0x19,
        "男人",
        (
            "#822F#1P没事吗？\x01",
            "会不会觉得头晕……\x02",
        )
    )

    Jump("loc_1B3F")

    label("loc_1B3F")

    CloseMessageWindow()

    label("loc_1B40")

    OP_63(0x14E)
    OP_8C(0x14E, 260, 400)
    Sleep(500)

    ChrTalk(    #46
        0x14E,
        (
            "#1714F#2P啊，没关系。\x02\x03",

            "#1710F嘿嘿，\x01",
            "发生了不少事……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_1BC0")

    ChrTalk(    #47
        0x19,
        "#820F#1P……是吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C63")

    label("loc_1BC0")


    NpcTalk(    #48
        0x19,
        "男人",
        "#820F#1P……是吗。\x02",
    )

    Jump("loc_1BE9")

    label("loc_1BE9")

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #49
        0x14E,
        (
            "#1714F#2P（啊……我想起来了。）\x02\x03",

            "#1718F（这个游击士哥哥，\x01",
            "好像叫做库拉茨……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C63")

    Fade(500)
    SetChrChipByIndex(0x19, 5)
    SetChrSubChip(0x19, 0)
    Sleep(500)
    OP_44(0x19, 0x3)
    OP_8C(0x19, 180, 400)
    Sleep(500)

    ChrTalk(    #50
        0x19,
        "#821F#5P……好，回去吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x15,
        "#775F#12P嗯～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x17,
        (
            "#1723F#12P可、可是，\x01",
            "我们不是还没有\x01",
            "找到礼物吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x19,
        (
            "#820F#5P你说什么呢，\x01",
            "大家找来找去都精疲力尽了吧？\x02\x03",

            "#821F这里还有个\x01",
            "累坏了的大小姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #54
        0x14E,
        "#1714F#2P我、我其实……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x14E, 500)
    Sleep(400)

    ChrTalk(    #55
        0x19,
        (
            "#823F#1P好了。\x02\x03",

            "#820F我送你们，\x01",
            "今天就乖乖地\x01",
            "回去好好休息吧。\x02\x03",

            "要是随便行动弄出什么病来，\x01",
            "老师可是会伤心的哦？\x02\x03",

            "#821F要找礼物的话，\x01",
            "明天我帮你们找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x17,
        "#1721F#12P哇～，真的吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x13,
        (
            "#1733F#6P大哥哥～你看起来呆头呆脑，\x01",
            "其实还挺能干的嘛～。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x19, 0x13, 400)
    Sleep(300)

    ChrTalk(    #58
        0x19,
        (
            "#823F#5P呜……\x01",
            "呆头呆脑是多余的啦！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F32():
        OP_8E(0xFE, 0xFFFFC8EC, 0xFFFFF830, 0xFFFF7518, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1F32)
    WaitChrThread(0x19, 0x1)

    def lambda_1F52():
        OP_6D(-12500, -2000, -36500, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1F52)

    def lambda_1F6A():
        OP_8E(0xFE, 0xFFFFC8EC, 0xFFFFF830, 0xFFFF65DC, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1F6A)
    Sleep(200)

    def lambda_1F8A():
        OP_8E(0xFE, 0xFFFFC658, 0xFFFFF830, 0xFFFF6C6C, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1F8A)
    Sleep(50)

    def lambda_1FAA():
        OP_8E(0xFE, 0xFFFFCD10, 0xFFFFF830, 0xFFFF6C94, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1FAA)
    Sleep(50)

    def lambda_1FCA():
        OP_8E(0xFE, 0xFFFFCFF4, 0xFFFFF830, 0xFFFF69C4, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1FCA)
    Sleep(50)

    def lambda_1FEA():
        OP_8E(0xFE, 0xFFFFCE00, 0xFFFFF830, 0xFFFF7284, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1FEA)
    WaitChrThread(0x14E, 0x1)
    PlayEffect(0x0, 0x0, 0xFF, -12980, -1500, -36420, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    Fade(500)
    SetChrChipByIndex(0x14E, 7)
    SetChrSubChip(0x14E, 0)
    Sleep(500)

    ChrTalk(    #59
        0x14E,
        (
            "#1714F#5P咦……？\x01",
            "这是…………\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 0x1)

    def lambda_20A2():
        TurnDirection(0xFE, 0x14E, 400)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_20A2)
    Sleep(100)
    WaitChrThread(0x17, 0x1)

    def lambda_20BA():
        TurnDirection(0xFE, 0x14E, 400)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_20BA)
    Sleep(70)
    WaitChrThread(0x13, 0x1)

    def lambda_20D2():
        TurnDirection(0xFE, 0x14E, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_20D2)
    Sleep(120)
    WaitChrThread(0x19, 0x1)

    def lambda_20EA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_20EA)
    OP_82(0x0, 0x2)
    OP_22(0x80, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0xFF, -12980, -1400, -36420, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x96, 0x1)
    OP_62(0x17, 0x0, 1600, 0x2, 0x7, 0x96, 0x1)
    OP_62(0x15, 0x0, 1600, 0x2, 0x7, 0x96, 0x1)
    OP_62(0x13, 0x0, 1600, 0x2, 0x7, 0x96, 0x1)
    Sleep(1000)
    OP_63(0x19)
    OP_63(0x17)
    OP_63(0x15)
    OP_63(0x13)
    Sleep(300)

    ChrTalk(    #60
        0x19,
        "#825F#12P哦，这个是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #61
        0x17,
        (
            "#1723F#12P玛丽，\x01",
            "莫非那个就是……！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #62
        0x15,
        "#774F#3S#12P厉害～！！#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x13,
        "#1732F#6P是『幸福之石』呢～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(2000)
    OP_63(0x14E)
    Sleep(500)

    ChrTalk(    #64
        0x14E,
        (
            "#1710F#5P………………嗯。\x02\x03",

            "#1903F一定是这样没错吧……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22CA():
        OP_6B(2760, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_22CA)
    FadeToDark(2000, 0, -1)
    OP_24(0x1C4, 0x5A)
    Sleep(300)
    OP_24(0x1C4, 0x50)
    Sleep(300)
    OP_24(0x1C4, 0x46)
    Sleep(300)
    OP_24(0x1C4, 0x3C)
    Sleep(300)
    OP_24(0x1C4, 0x32)
    Sleep(300)
    OP_24(0x1C4, 0x28)
    Sleep(300)
    OP_24(0x1C4, 0x1E)
    Sleep(300)
    OP_23(0x1C4)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_C4(0x0, 0x800)
    Sleep(500)

    AnonymousTalk(    #65
        (
            "\x18\x07\x0C#40W克拉姆一边念叨着『有可能』，\x01",
            "一边把旧挂坠取了出来。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #66
        (
            "\x18\x07\x0C#40W那似乎是在玛诺利亚村的\x01",
            "义卖会上偶然找到的。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #67
        (
            "\x18\x07\x0C#40W在克拉姆和伙伴们的鼓励下，\x01",
            "我把幸福之石嵌进挂坠。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #68
        (
            "\x18\x07\x0C#40W……正好合适！\x01",
            "简直就像是量身定做的一样。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #69
        (
            "\x18\x07\x0C#40W穿过波利的金链子一试，\x01",
            "长度也刚刚好。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #70
        (
            "\x18\x07\x0C#40W最后用达尼艾尔小心拿来的\x01",
            "漂亮的小盒子和包装纸包装起来，\x01",
            "就成为了最棒的礼物。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS355._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS357._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS358._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(4000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(140, 320, -1, -1)
    SetChrName("玛丽")

    AnonymousTalk(    #71
        (
            "\x07\x0C#40W咦……？\x01",
            "有和那个魔兽一样的味道。\x02",
        )
    )

    Jump("loc_25D0")

    label("loc_25D0")

    CloseMessageWindow()
    SetChrName("玛丽")

    AnonymousTalk(    #72
        "\x07\x0C#40W是因为幸福之石是它送给我的吗？\x02",
    )

    Jump("loc_260B")

    label("loc_260B")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(280, 240, -1, -1)
    SetChrName("特蕾莎老师")

    AnonymousTalk(    #73
        "\x07\x0C#40W玛丽……？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(2000)
    SetMessageWindowPos(130, 320, -1, -1)
    SetChrName("玛丽")

    AnonymousTalk(    #74
        "\x07\x0C#40W……对了，我明白了。\x02",
    )

    Jump("loc_26A6")

    label("loc_26A6")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(130, 320, -1, -1)
    SetChrName("玛丽")

    AnonymousTalk(    #75
        "\x07\x0C#40W……那是温暖的、幸福的味道。\x02",
    )

    Jump("loc_270D")

    label("loc_270D")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #76
        "\x07\x00Episode『幸福之石』　～Fin～\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283D")
    Sleep(1000)
    OP_28(0x6, 0x4, 0x10)
    OP_28(0x6, 0x4, 0x20)
    OP_3E(0x12D, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x00得到了\x1F\x2D\x01\x07\x00。\x02",
    )

    Jump("loc_2804")

    label("loc_2804")

    CloseMessageWindow()
    AddMira(12000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #78
        "\x07\x00得到了\x07\x02１２０００米拉\x07\x00。\x02",
    )

    Jump("loc_2831")

    label("loc_2831")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_283D")

    OP_A2(0x2505)
    NewScene("ED6_DT21/U2600   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_5_C59 end

    def Function_6_284A(): pass

    label("Function_6_284A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #79
        (
            "\x07\x05东　卢安市　　　３７４塞尔矩\x01",
            "　　玛诺利亚村　　６３塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_284A end

    def Function_7_28B8(): pass

    label("Function_7_28B8")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #80
        "\x07\x05南　巴伦诺灯塔　　７０塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_28B8 end

    def Function_8_2909(): pass

    label("Function_8_2909")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2962")

    ChrTalk(    #81
        0x14E,
        (
            "#1714F这边是灯塔吧。\x02\x03",

            "#1900F好像不知不觉\x01",
            "就走出村子了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C0")

    label("loc_2962")


    ChrTalk(    #82
        0x14E,
        (
            "#1714F啊，这边是灯塔……\x02\x03",

            "义卖会是在玛诺利亚村里举行的，\x01",
            "得回去才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_29C0")

    OP_59()
    Fade(1000)
    SetChrPos(0x14E, -73000, -1950, -114600, 0)
    SetChrPos(0x14F, -73000, -1950, -114600, 0)
    OP_6D(-73000, -1950, -114000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_8_2909 end

    SaveToFile()

Try(main)
