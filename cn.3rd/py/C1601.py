from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1601   ._SN',
        MapName             = 'Bose',
        Location            = 'C1601.x',
        MapIndex            = 250,
        MapDefaultBGM       = "ed60125",
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
        '刀刃毒牙',                             # 9
        '暴躁气泡Ｇ',                           # 10
        '目标用照相机',                         # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT29/CH12450 ._CH',             # 00
        'ED6_DT29/CH12451 ._CH',             # 01
        'ED6_DT09/CH10840 ._CH',             # 02
        'ED6_DT09/CH10841 ._CH',             # 03
        'ED6_DT29/CH12460 ._CH',             # 04
        'ED6_DT29/CH12461 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10551 ._CH',             # 07
        'ED6_DT29/CH12500 ._CH',             # 08
        'ED6_DT29/CH12501 ._CH',             # 09
        'ED6_DT29/CH12560 ._CH',             # 0A
        'ED6_DT29/CH12561 ._CH',             # 0B
        'ED6_DT07/CH00450 ._CH',             # 0C
        'ED6_DT07/CH00460 ._CH',             # 0D
        'ED6_DT07/CH00470 ._CH',             # 0E
        'ED6_DT07/CH00454 ._CH',             # 0F
        'ED6_DT07/CH00464 ._CH',             # 10
        'ED6_DT07/CH00474 ._CH',             # 11
        'ED6_DT07/CH00451 ._CH',             # 12
        'ED6_DT07/CH00461 ._CH',             # 13
        'ED6_DT07/CH00471 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT29/CH12450P._CP',             # 00
        'ED6_DT29/CH12451P._CP',             # 01
        'ED6_DT09/CH10840P._CP',             # 02
        'ED6_DT09/CH10841P._CP',             # 03
        'ED6_DT29/CH12460P._CP',             # 04
        'ED6_DT29/CH12461P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10551P._CP',             # 07
        'ED6_DT29/CH12500P._CP',             # 08
        'ED6_DT29/CH12501P._CP',             # 09
        'ED6_DT29/CH12560P._CP',             # 0A
        'ED6_DT29/CH12561P._CP',             # 0B
        'ED6_DT07/CH00450P._CP',             # 0C
        'ED6_DT07/CH00460P._CP',             # 0D
        'ED6_DT07/CH00470P._CP',             # 0E
        'ED6_DT07/CH00454P._CP',             # 0F
        'ED6_DT07/CH00464P._CP',             # 10
        'ED6_DT07/CH00474P._CP',             # 11
        'ED6_DT07/CH00451P._CP',             # 12
        'ED6_DT07/CH00461P._CP',             # 13
        'ED6_DT07/CH00471P._CP',             # 14
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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


    DeclMonster(
        X                   = 53510,
        Z                   = 0,
        Y                   = 950,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24860,
        Z                   = 0,
        Y                   = 24240,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17380,
        Z                   = -500,
        Y                   = 25790,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32729,
        Z                   = 0,
        Y                   = 59600,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -48130,
        Z                   = 0,
        Y                   = 4050,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -11760,
        Z                   = 0,
        Y                   = -136770,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -250,
        Z                   = 0,
        Y                   = -132820,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 48670,
        Y                   = 0,
        Z                   = -2650,
        Range               = 47390,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x13E2,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -5670,
        Y                   = 0,
        Z                   = 23320,
        Range               = -4090,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x34C6,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = -7780,
        TriggerZ            = 0,
        TriggerY            = -128550,
        TriggerRange        = 1000,
        ActorX              = -7780,
        ActorZ              = 0,
        ActorY              = -127890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 227170,
        TriggerZ            = 0,
        TriggerY            = 11830,
        TriggerRange        = 1000,
        ActorX              = 227870,
        ActorZ              = 0,
        ActorY              = 11830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -29260,
        TriggerZ            = 0,
        TriggerY            = 54810,
        TriggerRange        = 1000,
        ActorX              = -29260,
        ActorZ              = 0,
        ActorY              = 54110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -34020,
        TriggerZ            = 0,
        TriggerY            = 67570,
        TriggerRange        = 1000,
        ActorX              = -34020,
        ActorZ              = 0,
        ActorY              = 68190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -240,
        TriggerZ            = 0,
        TriggerY            = -136030,
        TriggerRange        = 1000,
        ActorX              = 380,
        ActorZ              = 0,
        ActorY              = -136030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 215690,
        TriggerZ            = 0,
        TriggerY            = 23150,
        TriggerRange        = 1000,
        ActorX              = 215690,
        ActorZ              = 0,
        ActorY              = 23810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 206060,
        TriggerZ            = 0,
        TriggerY            = 12220,
        TriggerRange        = 1000,
        ActorX              = 205400,
        ActorZ              = 0,
        ActorY              = 12180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3B2",          # 00, 0
        "Function_1_3FB",          # 01, 1
        "Function_2_4F9",          # 02, 2
        "Function_3_50F",          # 03, 3
        "Function_4_90B",          # 04, 4
        "Function_5_94C",          # 05, 5
        "Function_6_98D",          # 06, 6
        "Function_7_C93",          # 07, 7
        "Function_8_1252",         # 08, 8
        "Function_9_1494",         # 09, 9
        "Function_10_192A",        # 0A, 10
        "Function_11_1A4A",        # 0B, 11
        "Function_12_1B6A",        # 0C, 12
        "Function_13_1C8A",        # 0D, 13
        "Function_14_1DAA",        # 0E, 14
        "Function_15_1ECA",        # 0F, 15
        "Function_16_1FEA",        # 10, 16
    )


    def Function_0_3B2(): pass

    label("Function_0_3B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_3D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD")
    SetChrFlags(0x14, 0x80)

    label("loc_3DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_3FA")

    Return()

    # Function_0_3B2 end

    def Function_1_3FB(): pass

    label("Function_1_3FB")

    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449")
    OP_B2(0x1, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 2)), scpexpr(EXPR_END)), "loc_43D")
    OP_B2(0x0, 0x0, 0x80)

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 3)), scpexpr(EXPR_END)), "loc_449")
    OP_B2(0x0, 0x1, 0x80)

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B")
    OP_6F(0x0, 0)
    Jump("loc_462")

    label("loc_45B")

    OP_6F(0x0, 60)

    label("loc_462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_474")
    OP_6F(0x1, 0)
    Jump("loc_47B")

    label("loc_474")

    OP_6F(0x1, 60)

    label("loc_47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48D")
    OP_6F(0x2, 0)
    Jump("loc_494")

    label("loc_48D")

    OP_6F(0x2, 60)

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A6")
    OP_6F(0x3, 0)
    Jump("loc_4AD")

    label("loc_4A6")

    OP_6F(0x3, 60)

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF")
    OP_6F(0x4, 0)
    Jump("loc_4C6")

    label("loc_4BF")

    OP_6F(0x4, 60)

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D8")
    OP_6F(0x5, 0)
    Jump("loc_4DF")

    label("loc_4D8")

    OP_6F(0x5, 60)

    label("loc_4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F1")
    OP_6F(0x6, 0)
    Jump("loc_4F8")

    label("loc_4F1")

    OP_6F(0x6, 60)

    label("loc_4F8")

    Return()

    # Function_1_3FB end

    def Function_2_4F9(): pass

    label("Function_2_4F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4F9")

    label("loc_50E")

    Return()

    # Function_2_4F9 end

    def Function_3_50F(): pass

    label("Function_3_50F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(55000, 0, -25480, 0)
    OP_67(0, 7860, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x113, 55000, 0, -31350, 0)
    SetChrPos(0x112, 55000, 0, -32650, 0)
    SetChrPos(0x111, 55000, 0, -33950, 0)

    def lambda_591():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF9FD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_591)
    Sleep(100)
    OP_43(0x112, 0x3, 0x0, 0x4)
    Sleep(100)
    OP_43(0x111, 0x3, 0x0, 0x5)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    WaitChrThread(0x111, 0x3)

    ChrTalk(    #0
        0x112,
        "#1753F#5P咦，这里比想象中的要大。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x111,
        (
            "#1740F#5P的确如此，这样的话，\x01",
            "就用不着担心没有地方落脚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x113,
        (
            "#1763F#6P哼，通过洞窟什么的\x01",
            "不过是游戏罢了。\x02\x03",

            "#1765F说到底都是那家伙想出来的。\x02\x03",

            "等到了最深处，\x01",
            "一定会不由分说就打过来的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E1():
        TurnDirection(0xFE, 0x113, 500)
        ExitThread()

    QueueWorkItem(0x112, 2, lambda_6E1)
    Sleep(100)
    TurnDirection(0x111, 0x113, 500)
    Sleep(300)

    ChrTalk(    #3
        0x112,
        "#1756F#11P啊，果然洛克也这么想？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x111,
        (
            "#1749F#5P……嗯，\x01",
            "考虑到之前的训练，\x01",
            "有这种想法也是理所当然的。\x02\x03",

            "训练的时候也是，\x01",
            "到最后总是变成打架。\x02\x03",

            "#1741F好了，就看我们现在\x01",
            "能怎样对付大哥了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x112,
        (
            "#1751F#11P我们也变强了很多，\x01",
            "应该有胜算才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x113,
        (
            "#1763F#6P……总而言之，\x01",
            "这是一解平日之恨的好机会。\x02\x03",

            "#1761F赶快找到他，\x01",
            "然后把他海扁一顿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x111,
        "#1741F#5P噢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x112,
        "#1756F#11PＯＫ～！\x02",
    )

    CloseMessageWindow()

    def lambda_8BD():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF9FD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_8BD)

    def lambda_8D8():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF9FD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_8D8)
    WaitChrThread(0x111, 0x1)
    OP_8C(0x111, 0, 0)
    WaitChrThread(0x112, 0x1)
    OP_8C(0x112, 0, 0)
    OP_A2(0x2F91)
    EventEnd(0x0)
    Return()

    # Function_3_50F end

    def Function_4_90B(): pass

    label("Function_4_90B")


    def lambda_911():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF96B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_911)
    WaitChrThread(0x112, 0x1)

    def lambda_931():
        OP_8E(0xFE, 0xD2B4, 0x0, 0xFFFF9D2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_931)
    WaitChrThread(0x112, 0x1)
    Return()

    # Function_4_90B end

    def Function_5_94C(): pass

    label("Function_5_94C")


    def lambda_952():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF96B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_952)
    WaitChrThread(0x111, 0x1)

    def lambda_972():
        OP_8E(0xFE, 0xDAFC, 0x0, 0xFFFF9D2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_972)
    WaitChrThread(0x111, 0x1)
    Return()

    # Function_5_94C end

    def Function_6_98D(): pass

    label("Function_6_98D")

    EventBegin(0x0)
    Fade(1500)
    OP_6D(46040, 0, -760, 0)
    OP_67(0, 8140, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(170000, 0)
    OP_6E(262, 0)

    def lambda_9D7():
        OP_6D(43040, 0, 2240, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_9D7)

    def lambda_9EF():
        OP_6C(180000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9EF)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 40400, 700, 6100, 336)
    SetChrPos(0x111, 45520, 0, 1380, 320)
    SetChrPos(0x112, 46320, 0, 1340, 320)
    SetChrPos(0x113, 44940, 0, 800, 320)
    WaitChrThread(0x12, 0x0)
    Sleep(500)

    ChrTalk(    #9
        0x112,
        (
            "#1753F#5P……那、那家伙，\x01",
            "好像非常的强啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x113,
        (
            "#1764F#5P哼、哼，只是虚张声势吧。\x02\x03",

            "#1761F越是弱的家伙，\x01",
            "就越会靠外表伪装自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x111,
        (
            "#1740F#5P是、是这样吗？\x02\x03",

            "#1749F我说，\x01",
            "这不正是在说我们吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x10, 130, 500)
    OP_22(0x122, 0x0, 0x64)
    Sleep(500)
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x111,
        "#1743F#5P被、被发现了！？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x113, 14)
    SetChrSubChip(0x113, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x113,
        "#1767F#5P很好，一鼓作气收拾掉它！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)

    def lambda_C37():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_C37)

    def lambda_C47():
        OP_8E(0xFE, 0xAD34, 0x2BC, 0x7F8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C47)

    def lambda_C62():
        OP_6D(48040, 0, -3240, 1000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C62)
    Sleep(600)
    OP_44(0x10, 0xFF)
    OP_44(0x12, 0xFF)
    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 7)
    Return()

    # Function_6_98D end

    def Function_7_C93(): pass

    label("Function_7_C93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x10, 0x80)
    OP_6D(42220, 0, 2700, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x111, 42360, 0, 4300, 315)
    SetChrPos(0x112, 43800, 0, 3980, 315)
    SetChrPos(0x113, 41540, 0, 2600, 315)
    SetChrChipByIndex(0x111, 15)
    SetChrSubChip(0x111, 3)
    SetChrChipByIndex(0x112, 16)
    SetChrSubChip(0x112, 3)
    SetChrChipByIndex(0x113, 17)
    SetChrSubChip(0x113, 3)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #14
        0x113,
        "#1767F#5P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x111,
        "#1748F呼、呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x112,
        (
            "#1757F#5P好、好像有点奇怪……？\x02\x03",

            "我们有这么弱吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x111,
        (
            "#1749F不、不对……\x01",
            "是魔兽太强了。\x02\x03",

            "#1745F这、这跟听说的\x01",
            "相差太远了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x112,
        (
            "#1755F#5P唉唉，大哥啊……\x01",
            "为什么选了这种地方啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x111,
        (
            "#1743F#6P对了，我说洛克。\x02\x03",

            "#1742F刚才的魔兽，\x01",
            "不是的确强得一塌糊涂吗！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EB1():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x113, 0, lambda_EB1)
    Sleep(200)
    Fade(500)
    OP_99(0x113, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x113, 65535)
    SetChrSubChip(0x113, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #20
        0x113,
        (
            "#1764F#5P……………\x02\x03",

            "#1763F……哼，刚才的很强？\x02\x03",

            "#1761F别开玩笑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x111,
        "#1743F#6P……什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x112,
        "#1753F#6P……哎？\x02",
    )

    CloseMessageWindow()

    def lambda_F8F():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x112, 0, lambda_F8F)
    Sleep(200)
    Fade(500)
    OP_99(0x112, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    Sleep(100)

    def lambda_FD0():

        label("loc_FD0")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_FD0")

    QueueWorkItem2(0x112, 2, lambda_FD0)
    OP_0D()

    def lambda_FE2():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x111, 0, lambda_FE2)
    Sleep(200)
    Fade(500)
    OP_99(0x111, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    Sleep(100)

    def lambda_1023():

        label("loc_1023")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_1023")

    QueueWorkItem2(0x111, 2, lambda_1023)
    OP_0D()
    Sleep(300)

    ChrTalk(    #23
        0x111,
        (
            "#1747F#6P别、别逞强了。\x02\x03",

            "你不是也陷入苦战了吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x113,
        (
            "#1763F#5P……你们啊，\x01",
            "唧唧喳喳吵死人了。\x02\x03",

            "#1767F总之，\x01",
            "我们现在只有前进了。\x02\x03",

            "来，赶快走了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10F3():
        OP_8E(0xFE, 0x89A8, 0x0, 0x251C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_10F3)
    Sleep(1500)

    ChrTalk(    #25
        0x111,
        "#1743F#5P啊，等一下嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x112,
        (
            "#1753F#5P洛克这家伙，\x01",
            "在生什么气呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1168():
        OP_8E(0xFE, 0x89A8, 0x0, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_1168)
    Sleep(100)

    def lambda_1188():
        OP_8E(0xFE, 0x89A8, 0x0, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_1188)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x113, 0xFF)
    OP_6D(34000, 0, 9600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x111, 34000, 0, 9600, 315)
    SetChrPos(0x112, 34000, 0, 9600, 315)
    SetChrPos(0x113, 34000, 0, 9600, 315)
    SetChrSubChip(0x111, 0)
    SetChrSubChip(0x112, 0)
    SetChrSubChip(0x113, 0)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F92)
    OP_B2(0x0, 0x0, 0x80)
    EventEnd(0x4)
    Return()

    # Function_7_C93 end

    def Function_8_1252(): pass

    label("Function_8_1252")

    EventBegin(0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -17910, -500, 26070, 180)

    def lambda_1270():
        OP_6D(-17860, -500, 26840, 4000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1270)

    def lambda_1288():
        OP_67(0, 7420, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1288)

    def lambda_12A0():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_12A0)

    def lambda_12B0():
        OP_6B(2300, 4000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_12B0)
    WaitChrThread(0x12, 0x0)
    Sleep(1000)
    SetChrPos(0x111, -12160, 0, 21500, 315)
    SetChrPos(0x113, -13340, 0, 20800, 315)
    SetChrPos(0x112, -12400, 0, 20280, 315)

    def lambda_12FD():
        OP_6D(-14880, 0, 23640, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_12FD)

    def lambda_1315():
        OP_6B(2740, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1315)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #27
        0x111,
        "#1740F#12P这次的应该没问题吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x112,
        (
            "#1756F#12P这家伙\x01",
            "在卢安的时候也见到过呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x113,
        "#1766F#12P哼，快攻解决掉！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x113, 0x1000)
    SetChrFlags(0x111, 0x1000)
    SetChrFlags(0x112, 0x1000)

    def lambda_13C3():
        OP_6D(-17040, -500, 26800, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_13C3)

    def lambda_13DB():
        OP_6B(2300, 1000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_13DB)
    SetChrChipByIndex(0x113, 20)
    SetChrSubChip(0x113, 0)

    def lambda_13F5():
        OP_8E(0xFE, 0xFFFFBB7C, 0xFFFFFE0C, 0x648C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_13F5)
    Sleep(50)
    SetChrChipByIndex(0x111, 18)
    SetChrSubChip(0x111, 0)

    def lambda_141F():
        OP_8E(0xFE, 0xFFFFBD0C, 0xFFFFFE0C, 0x648C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_141F)
    Sleep(50)
    SetChrChipByIndex(0x112, 19)
    SetChrSubChip(0x112, 0)

    def lambda_1449():
        OP_8E(0xFE, 0xFFFFBC44, 0xFFFFFE0C, 0x648C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_1449)
    Sleep(500)
    OP_44(0x113, 0xFF)
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x12, 0xFF)
    ClearChrFlags(0x113, 0x1000)
    ClearChrFlags(0x111, 0x1000)
    ClearChrFlags(0x112, 0x1000)
    Battle(0x39F, 0x0, 0x2, 0x0, 0xFF)
    Call(0, 9)
    Return()

    # Function_8_1252 end

    def Function_9_1494(): pass

    label("Function_9_1494")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x11, 0x80)
    OP_6D(-18390, -500, 27500, 0)
    OP_67(0, 8460, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x111, -18390, -500, 27430, 180)
    SetChrPos(0x113, -19190, -500, 25900, 45)
    SetChrPos(0x112, -17590, -500, 25900, 315)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x113, 65535)
    SetChrSubChip(0x113, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x111,
        (
            "#1749F#5P比一开始的还强……\x02\x03",

            "#1742F比我们知道的家伙\x01",
            "真是强太多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x112,
        (
            "#1752F#12P看来，这里的魔兽\x01",
            "都是相当强悍啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x113,
        (
            "#1764F#6P可、可恶……\x02\x03",

            "#1767F为什么面对这种杂鱼\x01",
            "还得陷入苦战啊。\x02\x03",

            "可恶、可恶可恶可恶……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_164B():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x111, 2, lambda_164B)
    Sleep(100)

    def lambda_165E():

        label("loc_165E")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_165E")

    QueueWorkItem2(0x112, 2, lambda_165E)
    Sleep(300)

    ChrTalk(    #33
        0x111,
        (
            "#1743F#5P洛、洛克……冷静点。\x02\x03",

            "虽然是这个样子，\x01",
            "不过边休息边前进总能到的嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0x113,
        (
            "#1767F#6P边休息边前进！？\x02\x03",

            "#1766F对付杂鱼都得这样，\x01",
            "究竟什么时候\x01",
            "才能赶上那家伙啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x111,
        "#1742F#5P你、你问我我问谁啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x113, 225, 500)
    Sleep(300)

    ChrTalk(    #36
        0x113,
        (
            "#1767F#6P下次……\x01",
            "下次一定要轻松解决。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17C0():
        OP_8E(0xFE, 0xFFFF9A5C, 0x0, 0x4D76, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_17C0)
    Sleep(1000)

    ChrTalk(    #37
        0x111,
        "#1743F#5P喂、喂，洛克！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x112,
        (
            "#1753F#11P唉～\x01",
            "那家伙完全被热血冲昏了头了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x112, 0x2)

    def lambda_1840():
        OP_8E(0xFE, 0xFFFF9A5C, 0x0, 0x4D76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_1840)
    Sleep(100)

    def lambda_1860():
        OP_8E(0xFE, 0xFFFF9A5C, 0x0, 0x479A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_1860)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x113, 0xFF)
    OP_6D(-25580, 0, 20100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x111, -25580, 0, 20100, 225)
    SetChrPos(0x112, -25580, 0, 20100, 225)
    SetChrPos(0x113, -25580, 0, 20100, 225)
    SetChrSubChip(0x111, 0)
    SetChrSubChip(0x112, 0)
    SetChrSubChip(0x113, 0)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F93)
    OP_B2(0x0, 0x1, 0x80)
    EventEnd(0x4)
    Return()

    # Function_9_1494 end

    def Function_10_192A(): pass

    label("Function_10_192A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x160, 1)"), scpexpr(EXPR_END)), "loc_199C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x00得到了\x1F\x60\x01\x07\x00。\x02",
    )

    Jump("loc_1981")

    label("loc_1981")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE0)
    Jump("loc_1A08")

    label("loc_199C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "宝箱里装有\x1F\x60\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x60\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_19E9")

    label("loc_19E9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_1A08")

    Jump("loc_1A3C")

    label("loc_1A0B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1A3C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_192A end

    def Function_11_1A4A(): pass

    label("Function_11_1A4A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1ABC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    Jump("loc_1AA1")

    label("loc_1AA1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE1)
    Jump("loc_1B28")

    label("loc_1ABC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #43
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1B09")

    label("loc_1B09")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1B28")

    Jump("loc_1B5C")

    label("loc_1B2B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1B5C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1A4A end

    def Function_12_1B6A(): pass

    label("Function_12_1B6A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16E, 1)"), scpexpr(EXPR_END)), "loc_1BDC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x00得到了\x1F\x6E\x01\x07\x00。\x02",
    )

    Jump("loc_1BC1")

    label("loc_1BC1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE2)
    Jump("loc_1C48")

    label("loc_1BDC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "宝箱里装有\x1F\x6E\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x6E\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1C29")

    label("loc_1C29")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1C48")

    Jump("loc_1C7C")

    label("loc_1C4B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1C7C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1B6A end

    def Function_13_1C8A(): pass

    label("Function_13_1C8A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_1CFC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x00得到了\x1F\x07\x02\x07\x00。\x02",
    )

    Jump("loc_1CE1")

    label("loc_1CE1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE3)
    Jump("loc_1D68")

    label("loc_1CFC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "宝箱里装有\x1F\x07\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x07\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1D49")

    label("loc_1D49")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1D68")

    Jump("loc_1D9C")

    label("loc_1D6B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1D9C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_1C8A end

    def Function_14_1DAA(): pass

    label("Function_14_1DAA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_1E1C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        "\x07\x00得到了\x1F\x07\x02\x07\x00。\x02",
    )

    Jump("loc_1E01")

    label("loc_1E01")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE4)
    Jump("loc_1E88")

    label("loc_1E1C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        (
            "宝箱里装有\x1F\x07\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x07\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1E69")

    label("loc_1E69")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_1E88")

    Jump("loc_1EBC")

    label("loc_1E8B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1EBC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1DAA end

    def Function_15_1ECA(): pass

    label("Function_15_1ECA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_1F3C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    Jump("loc_1F21")

    label("loc_1F21")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE5)
    Jump("loc_1FA8")

    label("loc_1F3C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x05\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1F89")

    label("loc_1F89")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_1FA8")

    Jump("loc_1FDC")

    label("loc_1FAB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1FDC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_1ECA end

    def Function_16_1FEA(): pass

    label("Function_16_1FEA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_205C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #57
        "\x07\x00得到了\x1F\x07\x02\x07\x00。\x02",
    )

    Jump("loc_2041")

    label("loc_2041")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE6)
    Jump("loc_20C8")

    label("loc_205C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #58
        (
            "宝箱里装有\x1F\x07\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x07\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_20A9")

    label("loc_20A9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_20C8")

    Jump("loc_20FC")

    label("loc_20CB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_20FC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_1FEA end

    SaveToFile()

Try(main)
