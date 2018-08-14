from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1602   ._SN',
        MapName             = 'Bose',
        Location            = 'C1602.x',
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
        '幽灵碑文',                             # 9
        '邪骨章鱼',                             # 10
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        X                   = 33560,
        Z                   = 0,
        Y                   = -17800,
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
        X                   = 9220,
        Z                   = -1000,
        Y                   = -5220,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10130,
        Z                   = 0,
        Y                   = 41950,
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
        X                   = -31690,
        Z                   = 0,
        Y                   = 17530,
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
        X                   = -22920,
        Z                   = -1000,
        Y                   = 3720,
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
        X                   = -17070,
        Z                   = -500,
        Y                   = -6360,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 159370,
        Z                   = 0,
        Y                   = -1020,
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
        X                   = 184150,
        Z                   = -500,
        Y                   = -2380,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3AA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 186100,
        Z                   = 0,
        Y                   = 12660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3AA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 209310,
        Z                   = 0,
        Y                   = -1090,
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
        X                   = 230690,
        Z                   = -500,
        Y                   = -3880,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3AA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -23870,
        Y                   = -500,
        Z                   = -10300,
        Range               = -4090,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xFFFFCB3A,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = 24660,
        Y                   = -500,
        Z                   = -12280,
        Range               = 26470,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xFFFFABFA,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -18940,
        Y                   = -500,
        Z                   = -21160,
        Range               = -11720,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xFFFFB334,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 16510,
        TriggerZ            = 0,
        TriggerY            = 40840,
        TriggerRange        = 1000,
        ActorX              = 17170,
        ActorZ              = 0,
        ActorY              = 40840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 245230,
        TriggerZ            = 0,
        TriggerY            = 25460,
        TriggerRange        = 1000,
        ActorX              = 245680,
        ActorZ              = 0,
        ActorY              = 25970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9970,
        TriggerZ            = 0,
        TriggerY            = 48740,
        TriggerRange        = 1000,
        ActorX              = 10010,
        ActorZ              = 0,
        ActorY              = 49440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -16170,
        TriggerZ            = 0,
        TriggerY            = 17900,
        TriggerRange        = 1000,
        ActorX              = -15800,
        ActorZ              = 0,
        ActorY              = 18460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3D6",          # 00, 0
        "Function_1_417",          # 01, 1
        "Function_2_54C",          # 02, 2
        "Function_3_562",          # 03, 3
        "Function_4_8B1",          # 04, 4
        "Function_5_EC3",          # 05, 5
        "Function_6_FD4",          # 06, 6
        "Function_7_12DE",         # 07, 7
        "Function_8_1306",         # 08, 8
        "Function_9_1788",         # 09, 9
        "Function_10_18A8",        # 0A, 10
        "Function_11_19C8",        # 0B, 11
        "Function_12_1AE8",        # 0C, 12
    )


    def Function_0_3D6(): pass

    label("Function_0_3D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A")
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -15520, 200, -17210, 0)

    label("loc_40A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_416")

    label("loc_416")

    Return()

    # Function_0_3D6 end

    def Function_1_417(): pass

    label("Function_1_417")

    OP_22(0x1C7, 0x0, 0x64)
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_496")
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A0")

    label("loc_496")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A0")

    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E7")
    OP_B2(0x1, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 5)), scpexpr(EXPR_END)), "loc_4D6")
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 6)), scpexpr(EXPR_END)), "loc_4E7")
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F9")
    OP_6F(0x0, 0)
    Jump("loc_500")

    label("loc_4F9")

    OP_6F(0x0, 60)

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_512")
    OP_6F(0x1, 0)
    Jump("loc_519")

    label("loc_512")

    OP_6F(0x1, 60)

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B")
    OP_6F(0x2, 0)
    Jump("loc_532")

    label("loc_52B")

    OP_6F(0x2, 60)

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_544")
    OP_6F(0x3, 0)
    Jump("loc_54B")

    label("loc_544")

    OP_6F(0x3, 60)

    label("loc_54B")

    Return()

    # Function_1_417 end

    def Function_2_54C(): pass

    label("Function_2_54C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_561")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_54C")

    label("loc_561")

    Return()

    # Function_2_54C end

    def Function_3_562(): pass

    label("Function_3_562")

    EventBegin(0x0)
    TurnDirection(0x0, 0x10, 0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_58D():
        OP_6D(-16640, -500, -18500, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_58D)

    def lambda_5A5():
        OP_67(0, 7820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5A5)

    def lambda_5BD():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5BD)

    def lambda_5CD():
        OP_6B(2450, 3000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_5CD)
    WaitChrThread(0x12, 0x0)
    Sleep(1500)
    SetChrPos(0x111, -16680, -500, -10260, 180)
    SetChrPos(0x113, -14390, -500, -10530, 180)
    SetChrPos(0x112, -15780, -500, -10890, 180)

    def lambda_61A():
        OP_6D(-16500, -500, -14420, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_61A)

    def lambda_632():
        OP_67(0, 7100, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_632)

    def lambda_64A():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_64A)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #0
        0x112,
        (
            "#1753F#12P那是什么？\x01",
            "那种地方竟然有冻起来的石头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x111,
        (
            "#1742F#12P看起来不过是石头……\x01",
            "到底是什么啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D7():
        OP_8E(0xFE, 0xFFFFC25C, 0xFFFFFE0C, 0xFFFFC644, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_6D7)
    Sleep(500)
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x113,
        (
            "#1766F#12P笨蛋，\x01",
            "不要靠近那种莫名其妙的东西！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x112, 0x1)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_62(0x112, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_797():
        OP_8F(0xFE, 0xFFFFC25C, 0xFFFFFE0C, 0xFFFFC7D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_797)
    Sleep(500)

    ChrTalk(    #3
        0x112,
        "#1757F#12P哇，这家伙在动！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x111,
        "#1749F#12P……看来太迟了。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x113, 0x1000)
    SetChrFlags(0x111, 0x1000)

    def lambda_80F():
        OP_6D(-16500, -500, -18420, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_80F)

    def lambda_827():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_827)
    SetChrChipByIndex(0x113, 20)
    SetChrSubChip(0x113, 0)

    def lambda_841():
        OP_8E(0xFE, 0xFFFFC554, 0xFFFFFE0C, 0xFFFFBF3C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_841)
    SetChrChipByIndex(0x111, 18)
    SetChrSubChip(0x111, 0)

    def lambda_866():
        OP_8E(0xFE, 0xFFFFC16C, 0xFFFFFE0C, 0xFFFFBF3C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_866)
    Sleep(500)
    OP_44(0x113, 0xFF)
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x12, 0xFF)
    ClearChrFlags(0x113, 0x1000)
    ClearChrFlags(0x111, 0x1000)
    ClearChrFlags(0x112, 0x1000)
    Battle(0x3A1, 0x0, 0x1, 0x0, 0xFF)
    Call(0, 4)
    Return()

    # Function_3_562 end

    def Function_4_8B1(): pass

    label("Function_4_8B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-16400, -500, -18800, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x111, -16160, -500, -17180, 90)
    SetChrPos(0x113, -15380, -500, -18780, 0)
    SetChrPos(0x112, -14840, -500, -17100, 270)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x113, 65535)
    SetChrSubChip(0x113, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #5
        0x112,
        "#1753F#6P呼～真是吓一大跳。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x111,
        (
            "#1749F#11P啊啊，没想到\x01",
            "那种岩石居然是魔兽。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x113, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x113,
        (
            "#1767F#5P喂，雷斯……\x01",
            "你在犯什么傻！？\x02\x03",

            "我刚才不是说过\x01",
            "要你别拖后腿吗！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A3C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x112, 2, lambda_A3C)
    Sleep(100)
    OP_8C(0x111, 180, 400)
    Sleep(300)

    ChrTalk(    #8
        0x112,
        "#1755F#12P啊、啊啊……抱歉啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x113,
        (
            "#1763F#5P真是的，就会碍事。\x02\x03",

            "#1765F……还有迪恩。\x02\x03",

            "你就知道害怕，\x01",
            "也太胆小了。\x02\x03",

            "#1764F真是的，和你们一起走\x01",
            "太阳都要下山了……\x02\x03",

            "哼，我一个人去\x01",
            "搞不好还快点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x111,
        (
            "#1742F#12P………………………………\x02\x03",

            "#1749F……既然都这么说了，那你就自己走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x113,
        "#1762F#5P啊，你说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x111,
        (
            "#1744F#12P……没听见吗？\x02\x03",

            "#1747F既然都这么说了，\x01",
            "你就自己一个人走吧！\x02\x03",

            "你一个人\x01",
            "不是能打得更好吗！？\x02\x03",

            "我们不过是\x01",
            "碍手碍脚的累赘对吧！？\x02",
        )
    )

    Jump("loc_C7F")

    label("loc_C7F")

    CloseMessageWindow()

    ChrTalk(    #13
        0x113,
        "#1767F#5P什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x111,
        (
            "#1747F#12P说到底，\x01",
            "说要接受这个考试的也是你！\x02\x03",

            "我们不过是被迫来陪你的，\x01",
            "真是麻烦死了！\x02\x03",

            "#1744F……雷斯，走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x111, 0, 400)
    Sleep(500)

    ChrTalk(    #15
        0x112,
        (
            "#1754F#12P嗯，确实……\x02\x03",

            "#1752F都说我们是累赘了，\x01",
            "没道理继续跟你走了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x113,
        (
            "#1763F#5P……哼，\x01",
            "这就是你们的回答吗。\x02\x03",

            "#1761F正好，你们爱怎样怎样好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x113, 180, 500)
    Sleep(100)

    def lambda_DFC():
        OP_8E(0xFE, 0xFFFFC3EC, 0x1F4, 0xFFFF86E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_DFC)
    WaitChrThread(0x113, 0x1)

    ChrTalk(    #17
        0x112,
        (
            "#1755F#6P那家伙……\x01",
            "他那么冲动，\x01",
            "你不觉得会有麻烦吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x111,
        (
            "#1745F#5P管他的，\x01",
            "我和他已经没关系了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E91():
        OP_8E(0xFE, 0xFFFFC0E0, 0xFFFFFE0C, 0xFFFFBCE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_E91)
    WaitChrThread(0x112, 0x1)
    OP_A2(0x2F95)
    RemoveParty(0x12, 0x0)
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    EventEnd(0x0)
    Return()

    # Function_4_8B1 end

    def Function_5_EC3(): pass

    label("Function_5_EC3")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 5)), scpexpr(EXPR_END)), "loc_FB8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F30")

    ChrTalk(    #19
        0x111,
        (
            "#1742F嘁，那种家伙\x01",
            "就让他自己撞个头破血流吧。\x02\x03",

            "#1744F我们回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB8")

    label("loc_F30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB8")

    ChrTalk(    #20
        0x112,
        "#1755F这边是前进的路吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x111,
        (
            "#1742F嘁，那种家伙\x01",
            "就让他自己撞个头破血流吧。\x02\x03",

            "#1744F我们回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB8")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_5_EC3 end

    def Function_6_FD4(): pass

    label("Function_6_FD4")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(21720, -500, -14620, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x112, 16400, -1000, -7960, 135)
    SetChrPos(0x111, 14200, -1000, -7760, 135)

    def lambda_1045():
        OP_8E(0xFE, 0x54B0, 0xFFFFFE0C, 0xFFFFCB58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_1045)
    Sleep(50)

    def lambda_1065():
        OP_8E(0xFE, 0x5488, 0xFFFFFE0C, 0xFFFFC4A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_1065)
    OP_0D()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 31440, 500, -17500, 270)
    WaitChrThread(0x112, 0x1)
    Sleep(300)

    ChrTalk(    #22
        0x112,
        (
            "#1754F#6P洛克那家伙，没问题吧？\x02\x03",

            "#1755F再怎么说，\x01",
            "一个人突破这里也太困难了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x111, 0x1)

    ChrTalk(    #23
        0x111,
        (
            "#1744F#12P哼，别理他。\x02\x03",

            "#1745F说一个人比较好的\x01",
            "不是他自己吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1157():
        OP_8E(0xFE, 0x666C, 0xFFFFFE0C, 0xFFFFB9EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_1157)
    Sleep(200)
    OP_43(0x112, 0x3, 0x0, 0x7)
    Sleep(300)

    def lambda_1183():
        OP_6D(29660, 0, -18460, 2500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1183)

    def lambda_119B():
        OP_67(0, 4940, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_119B)

    def lambda_11B3():
        OP_6C(122000, 2500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_11B3)

    def lambda_11C3():
        OP_6B(3200, 2500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_11C3)
    Sleep(2000)
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x111, 0x1)
    TurnDirection(0x111, 0x11, 500)
    Sleep(300)

    ChrTalk(    #24
        0x111,
        "#1747F#12P是新出现的魔兽吗！？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x111, 12)
    SetChrSubChip(0x111, 0)
    OP_0D()
    Sleep(500)
    WaitChrThread(0x112, 0x3)

    ChrTalk(    #25
        0x112,
        "#1757F#6P好恶心，这是什么啊！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)

    def lambda_129A():
        OP_6B(2700, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_129A)

    def lambda_12AA():
        OP_8E(0xFE, 0x6950, 0x0, 0xFFFFBA64, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12AA)
    Sleep(600)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    Battle(0x3A2, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 8)
    Return()

    # Function_6_FD4 end

    def Function_7_12DE(): pass

    label("Function_7_12DE")


    def lambda_12E4():
        OP_8E(0xFE, 0x6658, 0xFFFFFE0C, 0xFFFFBEB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_12E4)
    WaitChrThread(0x112, 0x1)
    TurnDirection(0x112, 0x11, 500)
    Return()

    # Function_7_12DE end

    def Function_8_1306(): pass

    label("Function_8_1306")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(30040, 0, -19340, 0)
    OP_67(0, 6980, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x111, 15)
    SetChrSubChip(0x111, 3)
    SetChrChipByIndex(0x112, 16)
    SetChrSubChip(0x112, 3)
    SetChrPos(0x111, 28920, 0, -18960, 90)
    SetChrPos(0x112, 29020, 0, -17680, 90)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #26
        0x112,
        "#1757F#6P果、果然好可怕……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x111,
        (
            "#1745F#12P那家伙……\x01",
            "这里满是这样的魔兽，\x01",
            "就他一个人……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_140C():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x111, 0, lambda_140C)
    Sleep(200)
    Fade(500)
    OP_99(0x111, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    OP_0D()

    def lambda_1449():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x112, 0, lambda_1449)
    Sleep(200)
    Fade(500)
    OP_99(0x112, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    OP_0D()
    TurnDirection(0x112, 0x111, 400)
    Sleep(500)

    ChrTalk(    #28
        0x112,
        (
            "#1754F#6P我说，迪恩。\x02\x03",

            "#1752F……现在可不是\x01",
            "耍性子的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x111,
        "#1745F#11P……………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x111, 0x112, 400)
    Sleep(300)

    ChrTalk(    #30
        0x111,
        "#1749F#11P我说……雷斯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x112,
        "#1753F#6P……嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x111,
        (
            "#1742F#11P洛克他，\x01",
            "好像从没示过弱吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x112,
        (
            "#1753F#6P啊啊……\x02\x03",

            "#1755F这么说来，还从来没听到过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x111,
        (
            "#1749F#11P就是啊……\x02\x03",

            "他总是逞强，\x01",
            "却从没像我们一样示过弱。\x02\x03",

            "#1745F无论什么时候，\x01",
            "他总是在身后\x01",
            "推着我们前进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x112,
        (
            "#1754F#6P确实……\x01",
            "你这么一说，倒是没错。\x02\x03",

            "#1750F要是没有他，\x01",
            "我们怎么会\x01",
            "想当游击士呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x111, 270, 400)
    Sleep(300)

    ChrTalk(    #36
        0x111,
        (
            "#1744F#5P…………………………\x02\x03",

            "……嘿，真没办法。\x02\x03",

            "#1741F虽然他实在让人火大……\x01",
            "不过还是赶快追上去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x112, 270, 500)
    Sleep(300)

    ChrTalk(    #37
        0x112,
        "#1756F#5P啊哈哈，好！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F96)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    EventEnd(0x0)
    Return()

    # Function_8_1306 end

    def Function_9_1788(): pass

    label("Function_9_1788")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1869")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_17FA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x00得到了\x1F\x07\x02\x07\x00。\x02",
    )

    Jump("loc_17DF")

    label("loc_17DF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE8)
    Jump("loc_1866")

    label("loc_17FA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "宝箱里装有\x1F\x07\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x07\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1847")

    label("loc_1847")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_1866")

    Jump("loc_189A")

    label("loc_1869")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_189A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1788 end

    def Function_10_18A8(): pass

    label("Function_10_18A8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1989")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_191A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x00得到了\x1F\x07\x02\x07\x00。\x02",
    )

    Jump("loc_18FF")

    label("loc_18FF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE9)
    Jump("loc_1986")

    label("loc_191A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "宝箱里装有\x1F\x07\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x07\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1967")

    label("loc_1967")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1986")

    Jump("loc_19BA")

    label("loc_1989")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #43
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_19BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_18A8 end

    def Function_11_19C8(): pass

    label("Function_11_19C8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_1A3A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x00得到了\x1F\x07\x02\x07\x00。\x02",
    )

    Jump("loc_1A1F")

    label("loc_1A1F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FEA)
    Jump("loc_1AA6")

    label("loc_1A3A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #45
        (
            "宝箱里装有\x1F\x07\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x07\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1A87")

    label("loc_1A87")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1AA6")

    Jump("loc_1ADA")

    label("loc_1AA9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1ADA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_19C8 end

    def Function_12_1AE8(): pass

    label("Function_12_1AE8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1B5A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    Jump("loc_1B3F")

    label("loc_1B3F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FEB)
    Jump("loc_1BC6")

    label("loc_1B5A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #48
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1BA7")

    label("loc_1BA7")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1BC6")

    Jump("loc_1BFA")

    label("loc_1BC9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1BFA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1AE8 end

    SaveToFile()

Try(main)
