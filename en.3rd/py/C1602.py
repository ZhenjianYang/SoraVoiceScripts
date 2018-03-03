from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Ghost Epitaph',                        # 9
        'Octobone',                             # 10
        'Target Camera',                        # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
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
        "Function_4_99A",          # 04, 4
        "Function_5_1110",         # 05, 5
        "Function_6_1221",         # 06, 6
        "Function_7_15A4",         # 07, 7
        "Function_8_15CC",         # 08, 8
        "Function_9_1B5B",         # 09, 9
        "Function_10_1C9C",        # 0A, 10
        "Function_11_1DD0",        # 0B, 11
        "Function_12_1F10",        # 0C, 12
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
    OP_C4(0x0, 0x20000000)
    TurnDirection(0x0, 0x10, 0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_593():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x111, 0, lambda_593)

    def lambda_5A5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x113, 0, lambda_5A5)

    def lambda_5B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x112, 0, lambda_5B7)

    def lambda_5C9():
        OP_6D(-16640, -500, -18500, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_5C9)

    def lambda_5E1():
        OP_67(0, 7820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5E1)

    def lambda_5F9():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5F9)

    def lambda_609():
        OP_6B(2450, 3000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_609)
    WaitChrThread(0x12, 0x0)
    Sleep(1500)
    SetChrPos(0x111, -16680, -500, -10260, 180)
    SetChrPos(0x113, -14390, -500, -10530, 180)
    SetChrPos(0x112, -15780, -500, -10890, 180)

    def lambda_656():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x111, 0, lambda_656)

    def lambda_668():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x113, 0, lambda_668)

    def lambda_67A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x112, 0, lambda_67A)

    def lambda_68C():
        OP_6D(-16500, -500, -14420, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_68C)

    def lambda_6A4():
        OP_67(0, 7100, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6A4)

    def lambda_6BC():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_6BC)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #0
        0x112,
        (
            "#1753F#12PHuh? Why's there a frozen rock in the middle\x01",
            "of the path?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x111,
        (
            "#1742F#12PI dunno... It doesn't look like anything special,\x01",
            "but that's a weird place for one to be.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_783():
        OP_8E(0xFE, 0xFFFFC25C, 0xFFFFFE0C, 0xFFFFC644, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_783)
    Sleep(500)
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x113,
        (
            "#1766F#12PWhat's your damage?! Don't wander over to\x01",
            "random crap when you don't know what it is!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x112, 0x1)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_62(0x112, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_86E():
        OP_8F(0xFE, 0xFFFFC25C, 0xFFFFFE0C, 0xFFFFC7D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_86E)
    Sleep(500)

    ChrTalk(    #3
        0x112,
        "#1757F#12PWhoa! It's moving!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x111,
        "#1749F#12P...Maybe that warning was a liiittle too late.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x113, 0x1000)
    SetChrFlags(0x111, 0x1000)

    def lambda_8F8():
        OP_6D(-16500, -500, -18420, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_8F8)

    def lambda_910():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_910)
    SetChrChipByIndex(0x113, 20)
    SetChrSubChip(0x113, 0)

    def lambda_92A():
        OP_8E(0xFE, 0xFFFFC554, 0xFFFFFE0C, 0xFFFFBF3C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_92A)
    SetChrChipByIndex(0x111, 18)
    SetChrSubChip(0x111, 0)

    def lambda_94F():
        OP_8E(0xFE, 0xFFFFC16C, 0xFFFFFE0C, 0xFFFFBF3C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_94F)
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

    def Function_4_99A(): pass

    label("Function_4_99A")

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
        "#1753F#6PWhew... That scared the heck outta me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x111,
        (
            "#1749F#11PNo doubt. Who'd have thought a rock would\x01",
            "turn into a monster?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x113, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x113,
        (
            "#1767F#5PWell, maybe you wouldn't have been scared\x01",
            "if you hadn't been such a dumbass!\x02\x03",

            "What was I just saying about draggin' me\x01",
            "down?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B79():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x112, 2, lambda_B79)
    Sleep(100)
    OP_8C(0x111, 180, 400)
    Sleep(300)

    ChrTalk(    #8
        0x112,
        "#1755F#12PS-Sorry, man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x113,
        (
            "#1763F#5PFor the love of Aidios...\x02\x03",

            "#1765FThat goes for you, too, Deen.\x02\x03",

            "You ever gonna grow out of being such\x01",
            "a damn coward?\x02\x03",

            "#1764FUgh... At this rate, we're not even gonna\x01",
            "be able to get through here by sundown.\x02\x03",

            "Maybe it's time I cut the dead weight and\x01",
            "went on by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x111,
        (
            "#1742F#12P...\x02\x03",

            "#1749F...Then go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x113,
        "#1762F#5PWhat was that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x111,
        (
            "#1744F#12PYou heard me.\x02\x03",

            "#1747FIf you're that determined to go by yourself,\x01",
            "be my guest!\x02\x03",

            "You're the tough one here, right? You can\x01",
            "handle everything in here by yourself, right?!\x02\x03",

            "Why would you want a bunch'a weaklings like\x01",
            "us around? Get movin', tough guy! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x113,
        "#1767F#5PTry sayin' that again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x111,
        (
            "#1747F#12PBesides, the only reason we're even here in\x01",
            "this cave right now is because YOU thought\x01",
            "this was a good idea!\x02\x03",

            "I'm sick of it! And I sure as hell don't wanna\x01",
            "be told I'm getting in the way by the guy who\x01",
            "forced me into this crap!\x02\x03",

            "#1744FCome on, Rais. We're outta here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x111, 0, 400)
    Sleep(500)

    ChrTalk(    #15
        0x112,
        (
            "#1754F#12PYeah. I'm good with that.\x02\x03",

            "#1752FI know when I'm not needed. No point in hanging\x01",
            "around after being told I'm dead weight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x113,
        (
            "#1763F#5P...Heh. That's how it's gonna be, huh?\x02\x03",

            "#1761FSee ya never.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x113, 180, 500)
    Sleep(100)

    def lambda_1048():
        OP_8E(0xFE, 0xFFFFC3EC, 0x1F4, 0xFFFF86E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_1048)
    WaitChrThread(0x113, 0x1)

    ChrTalk(    #17
        0x112,
        (
            "#1755F#6PDoesn't he ever get tired keepin' up that\x01",
            "act 24/7?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x111,
        "#1745F#5PWho cares? He's on his own now.\x02",
    )

    CloseMessageWindow()

    def lambda_10D8():
        OP_8E(0xFE, 0xFFFFC0E0, 0xFFFFFE0C, 0xFFFFBCE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_10D8)
    WaitChrThread(0x112, 0x1)
    OP_C4(0x1, 0x20000000)
    OP_A2(0x2F95)
    RemoveParty(0x12, 0x0)
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    EventEnd(0x0)
    Return()

    # Function_4_99A end

    def Function_5_1110(): pass

    label("Function_5_1110")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 5)), scpexpr(EXPR_END)), "loc_1205")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1179")

    ChrTalk(    #19
        0x111,
        (
            "#1742FHe can go get himself killed for all\x01",
            "I care.\x02\x03",

            "#1744FWe're goin' home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1205")

    label("loc_1179")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1205")

    ChrTalk(    #20
        0x112,
        "#1755FThis way leads farther in, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x111,
        (
            "#1742FHe can go get himself killed for all\x01",
            "I care.\x02\x03",

            "#1744FWe're goin' home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1205")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_5_1110 end

    def Function_6_1221(): pass

    label("Function_6_1221")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1000)
    OP_6D(21720, -500, -14620, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x112, 16400, -1000, -7960, 135)
    SetChrPos(0x111, 14200, -1000, -7760, 135)

    def lambda_1298():
        OP_8E(0xFE, 0x54B0, 0xFFFFFE0C, 0xFFFFCB58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_1298)
    Sleep(50)

    def lambda_12B8():
        OP_8E(0xFE, 0x5488, 0xFFFFFE0C, 0xFFFFC4A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_12B8)
    OP_0D()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 31440, 500, -17500, 270)
    WaitChrThread(0x112, 0x1)
    Sleep(300)

    ChrTalk(    #22
        0x112,
        (
            "#1754F#6PYou think Rocco's still all right?\x02\x03",

            "#1755FHe might be pretty strong, but the monsters in\x01",
            "here are, like, way stronger than any one of us.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x111, 0x1)

    ChrTalk(    #23
        0x111,
        (
            "#1744F#12PHmph. Who cares?\x02\x03",

            "#1745FHe was the one who said he wanted to go ahead\x01",
            "on his own. He made his bed--let him lie in it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1416():
        OP_8E(0xFE, 0x666C, 0xFFFFFE0C, 0xFFFFB9EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_1416)
    Sleep(200)
    OP_43(0x112, 0x3, 0x0, 0x7)
    Sleep(300)

    def lambda_1442():
        OP_6D(29660, 0, -18460, 2500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1442)

    def lambda_145A():
        OP_67(0, 4940, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_145A)

    def lambda_1472():
        OP_6C(122000, 2500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1472)

    def lambda_1482():
        OP_6B(3200, 2500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1482)
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
        "#1747F#12PHaven't seen one like this before!\x02",
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
        "#1757F#6PWhat IS this creepy thing?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)

    def lambda_1560():
        OP_6B(2700, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1560)

    def lambda_1570():
        OP_8E(0xFE, 0x6950, 0x0, 0xFFFFBA64, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1570)
    Sleep(600)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    Battle(0x3A2, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 8)
    Return()

    # Function_6_1221 end

    def Function_7_15A4(): pass

    label("Function_7_15A4")


    def lambda_15AA():
        OP_8E(0xFE, 0x6658, 0xFFFFFE0C, 0xFFFFBEB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_15AA)
    WaitChrThread(0x112, 0x1)
    TurnDirection(0x112, 0x11, 500)
    Return()

    # Function_7_15A4 end

    def Function_8_15CC(): pass

    label("Function_8_15CC")

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
        "#1757F#6PMan... That was nasty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x111,
        (
            "#1745F#12PAnd Rocco's walking ahead alone in a place \x01",
            "crawlin' with monsters just like that...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16EE():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x111, 0, lambda_16EE)
    Sleep(200)
    Fade(500)
    OP_99(0x111, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    OP_0D()

    def lambda_172B():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x112, 0, lambda_172B)
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
            "#1754F#6P...Hey, Deen?\x02\x03",

            "#1752FI feel like this really ain't the time for us to\x01",
            "be fighting each other and tryin' to act big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x111,
        "#1745F#11P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x111, 0x112, 400)
    Sleep(300)

    ChrTalk(    #30
        0x111,
        "#1749F#11PHey, Rais?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x112,
        "#1753F#6PYeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x111,
        (
            "#1742F#11PHave you ever seen Rocco show any sign\x01",
            "of weakness before? Ever?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x112,
        (
            "#1753F#6PWell...\x02\x03",

            "#1755FNow that you mention it, no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x111,
        (
            "#1749F#11PSame here...\x02\x03",

            "He might be pretendin' he's strong all the time,\x01",
            "but he never lets any sign of weakness slip or\x01",
            "whines like we do.\x02\x03",

            "#1745FHe's always the one who's pushing us and tryin'\x01",
            "to make us better ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x112,
        (
            "#1754F#6PYeah... I guess you're right.\x02\x03",

            "#1750FI mean, if it wasn't for him, we really wouldn't\x01",
            "be here. We'd still be loiterin' around back in\x01",
            "Ruan forever, probably.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x111, 270, 400)
    Sleep(300)

    ChrTalk(    #36
        0x111,
        (
            "#1744F#5P...\x02\x03",

            "We can let all the dead weight stuff slide this\x01",
            "once.\x02\x03",

            "#1741FMaybe he pisses me off sometimes, but I ain't\x01",
            "about to turn my back on him when he's always \x01",
            "had ours.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x112, 270, 500)
    Sleep(300)

    ChrTalk(    #37
        0x112,
        "#1756F#5PHahaha. Damn straight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F96)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    EventEnd(0x0)
    Return()

    # Function_8_15CC end

    def Function_9_1B5B(): pass

    label("Function_9_1B5B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C34")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_1BC9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x05Found \x1F\x07\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE8)
    Jump("loc_1C31")

    label("loc_1BC9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x07\x05Found \x1F\x07\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x07\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_1C31")

    Jump("loc_1C8E")

    label("loc_1C34")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x05The lock on the front of the chest is just painted on.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x8, 0x0)

    label("loc_1C8E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1B5B end

    def Function_10_1C9C(): pass

    label("Function_10_1C9C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D75")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_1D0A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05Found \x1F\x07\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE9)
    Jump("loc_1D72")

    label("loc_1D0A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "\x07\x05Found \x1F\x07\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x07\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1D72")

    Jump("loc_1DC2")

    label("loc_1D75")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #43
        "\x07\x05You've stolen my treasure...and my heart.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x9, 0x0)

    label("loc_1DC2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1C9C end

    def Function_11_1DD0(): pass

    label("Function_11_1DD0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_1E3E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05Found \x1F\x07\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FEA)
    Jump("loc_1EA6")

    label("loc_1E3E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #45
        (
            "\x07\x05Found \x1F\x07\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x07\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1EA6")

    Jump("loc_1F02")

    label("loc_1EA9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05I have a somewhat unfavorable premonition about this.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xA, 0x0)

    label("loc_1F02")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1DD0 end

    def Function_12_1F10(): pass

    label("Function_12_1F10")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1F7E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05Found \x1F\xFC\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FEB)
    Jump("loc_1FE6")

    label("loc_1F7E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #48
        (
            "\x07\x05Found \x1F\xFC\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFC\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1FE6")

    Jump("loc_2075")

    label("loc_1FE9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "\x07\x05What makes the chests of Liberl so talkative, anyway? Most other\x01",
            "countries prefer strong, silent chests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xB, 0x0)

    label("loc_2075")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1F10 end

    SaveToFile()

Try(main)
