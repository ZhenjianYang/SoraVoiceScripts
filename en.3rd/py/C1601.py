from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Blade Fang',                           # 9
        'Boiled Egger G',                       # 10
        'Target Camera',                        # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
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
        "Function_4_9C5",          # 04, 4
        "Function_5_A06",          # 05, 5
        "Function_6_A47",          # 06, 6
        "Function_7_D8E",          # 07, 7
        "Function_8_13CE",         # 08, 8
        "Function_9_1675",         # 09, 9
        "Function_10_1C35",        # 0A, 10
        "Function_11_1D7A",        # 0B, 11
        "Function_12_1EDE",        # 0C, 12
        "Function_13_2056",        # 0D, 13
        "Function_14_2180",        # 0E, 14
        "Function_15_231D",        # 0F, 15
        "Function_16_2450",        # 10, 16
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
    OP_C4(0x0, 0x20000000)
    OP_6D(55000, 0, -25480, 0)
    OP_67(0, 7860, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x113, 55000, 0, -31350, 0)
    SetChrPos(0x112, 55000, 0, -32650, 0)
    SetChrPos(0x111, 55000, 0, -33950, 0)

    def lambda_597():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF9FD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_597)
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
        "#1753F#5PThis place is pretty big inside, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x111,
        "#1740F#5PYeah. Tons of empty space to fight in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x113,
        (
            "#1763F#6PHmph. You know as well as I do making it\x01",
            "through this cave isn't gonna be the main\x01",
            "event.\x02\x03",

            "#1765FIt's him we're dealing with, here.\x02\x03",

            "He'll be waitin' for us at the end to challenge\x01",
            "us to a fight. I guarantee it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_729():
        TurnDirection(0xFE, 0x113, 500)
        ExitThread()

    QueueWorkItem(0x112, 2, lambda_729)
    Sleep(100)
    TurnDirection(0x111, 0x113, 500)
    Sleep(300)

    ChrTalk(    #3
        0x112,
        "#1756F#11PYou think so, too, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x111,
        (
            "#1749F#5P...Well, going by all our training so far, \x01",
            "it's a pretty safe guess.\x02\x03",

            "That's how every other exercise has ended.\x02\x03",

            "#1741FI wonder how well we're gonna be able to do\x01",
            "against him this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x112,
        (
            "#1751F#11PI feel like we've gotten pretty strong. We might\x01",
            "have a chance, but who knows?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x113,
        (
            "#1763F#6P...Either way, this is a good chance to get back\x01",
            "at him for having to put up with his crap all the\x01",
            "time.\x02\x03",

            "#1761FLet's get going and give him hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x111,
        "#1741F#5PYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x112,
        "#1756F#11PRight there with you!\x02",
    )

    CloseMessageWindow()

    def lambda_971():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF9FD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_971)

    def lambda_98C():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF9FD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_98C)
    WaitChrThread(0x111, 0x1)
    OP_8C(0x111, 0, 0)
    WaitChrThread(0x112, 0x1)
    OP_8C(0x112, 0, 0)
    OP_C4(0x1, 0x20000000)
    OP_A2(0x2F91)
    EventEnd(0x0)
    Return()

    # Function_3_50F end

    def Function_4_9C5(): pass

    label("Function_4_9C5")


    def lambda_9CB():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF96B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_9CB)
    WaitChrThread(0x112, 0x1)

    def lambda_9EB():
        OP_8E(0xFE, 0xD2B4, 0x0, 0xFFFF9D2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_9EB)
    WaitChrThread(0x112, 0x1)
    Return()

    # Function_4_9C5 end

    def Function_5_A06(): pass

    label("Function_5_A06")


    def lambda_A0C():
        OP_8E(0xFE, 0xD6D8, 0x0, 0xFFFF96B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_A0C)
    WaitChrThread(0x111, 0x1)

    def lambda_A2C():
        OP_8E(0xFE, 0xDAFC, 0x0, 0xFFFF9D2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_A2C)
    WaitChrThread(0x111, 0x1)
    Return()

    # Function_5_A06 end

    def Function_6_A47(): pass

    label("Function_6_A47")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1500)
    OP_6D(46040, 0, -760, 0)
    OP_67(0, 8140, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(170000, 0)
    OP_6E(262, 0)

    def lambda_A97():
        OP_6D(43040, 0, 2240, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_A97)

    def lambda_AAF():
        OP_6C(180000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_AAF)
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
        "#1753F#5PThat's one ugly monster.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x113,
        (
            "#1764F#5PIt might LOOK that way, but I bet it's small fry.\x02\x03",

            "#1761FProbably just to scare predators off. The weaker\x01",
            "somethin' is, the meaner it's gonna look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x111,
        (
            "#1740F#5PY-You think?\x02\x03",

            "#1749FThat description kinda sounds like it fits us,\x01",
            "too...\x02",
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
        "#1743F#5PI-I think it noticed us!\x02",
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
        "#1767F#5PTime to make it wish it hadn't!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)

    def lambda_D32():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_D32)

    def lambda_D42():
        OP_8E(0xFE, 0xAD34, 0x2BC, 0x7F8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D42)

    def lambda_D5D():
        OP_6D(48040, 0, -3240, 1000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_D5D)
    Sleep(600)
    OP_44(0x10, 0xFF)
    OP_44(0x12, 0xFF)
    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 7)
    Return()

    # Function_6_A47 end

    def Function_7_D8E(): pass

    label("Function_7_D8E")

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
        "#1767F#5PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x111,
        "#1748F*pant*...*pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x112,
        (
            "#1757F#5PWh-What the...?\x02\x03",

            "I thought we were stronger than this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x111,
        (
            "#1749FIt's not that we're weak... That monster was\x01",
            "just that strong.\x02\x03",

            "#1745FAgate sure didn't say anythin' about this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x112,
        (
            "#1755F#5P*sigh* Why'd he have to go and choose\x01",
            "here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x111,
        (
            "#1743F#6PSo much for your theory, Rocco.\x02\x03",

            "#1742FThat monster didn't just look strong.\x01",
            "It WAS strong!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FDC():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x113, 0, lambda_FDC)
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
            "#1764F#5P...\x02\x03",

            "#1763FHmph. You call that strong?\x02\x03",

            "#1761FYou've gotta be kiddin' me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x111,
        "#1743F#6PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x112,
        "#1753F#6PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    def lambda_10AA():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x112, 0, lambda_10AA)
    Sleep(200)
    Fade(500)
    OP_99(0x112, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    Sleep(100)

    def lambda_10EB():

        label("loc_10EB")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_10EB")

    QueueWorkItem2(0x112, 2, lambda_10EB)
    OP_0D()

    def lambda_10FD():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x111, 0, lambda_10FD)
    Sleep(200)
    Fade(500)
    OP_99(0x111, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    Sleep(100)

    def lambda_113E():

        label("loc_113E")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_113E")

    QueueWorkItem2(0x111, 2, lambda_113E)
    OP_0D()
    Sleep(300)

    ChrTalk(    #23
        0x111,
        (
            "#1747F#6PT-Tryin' to act like it's no big deal isn't\x01",
            "gonna impress us, y'know!\x02\x03",

            "We could see you strugglin' the whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x113,
        (
            "#1763F#5PMaybe you need your eyes checked, then.\x02\x03",

            "#1767FAnyway, who cares how tough it was?\x01",
            "Let's get moving.\x02\x03",

            "We've got work to do.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1260():
        OP_8E(0xFE, 0x89A8, 0x0, 0x251C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_1260)
    Sleep(1500)

    def lambda_1280():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x113, 0, lambda_1280)

    ChrTalk(    #25
        0x111,
        "#1743F#5PW-Wait a second!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x112,
        "#1753F#5PWhat's up with him?\x02",
    )

    CloseMessageWindow()

    def lambda_12D3():
        OP_8E(0xFE, 0x89A8, 0x0, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_12D3)
    Sleep(100)

    def lambda_12F3():
        OP_8E(0xFE, 0x89A8, 0x0, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_12F3)
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
    OP_9F(0x113, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x111, 34000, 0, 9600, 315)
    SetChrPos(0x112, 34000, 0, 9600, 315)
    SetChrPos(0x113, 34000, 0, 9600, 315)
    SetChrSubChip(0x111, 0)
    SetChrSubChip(0x112, 0)
    SetChrSubChip(0x113, 0)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_C4(0x1, 0x20000000)
    OP_A2(0x2F92)
    OP_B2(0x0, 0x0, 0x80)
    EventEnd(0x4)
    Return()

    # Function_7_D8E end

    def Function_8_13CE(): pass

    label("Function_8_13CE")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -17910, -500, 26070, 180)

    def lambda_13F2():
        OP_6D(-17860, -500, 26840, 4000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_13F2)

    def lambda_140A():
        OP_67(0, 7420, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_140A)

    def lambda_1422():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1422)

    def lambda_1432():
        OP_6B(2300, 4000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1432)
    WaitChrThread(0x12, 0x0)
    Sleep(1000)
    OP_9F(0x111, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x113, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x112, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x111, -12160, 0, 21500, 315)
    SetChrPos(0x113, -13340, 0, 20800, 315)
    SetChrPos(0x112, -12400, 0, 20280, 315)

    def lambda_14A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x111, 0, lambda_14A0)

    def lambda_14B2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x113, 0, lambda_14B2)

    def lambda_14C4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x112, 0, lambda_14C4)

    def lambda_14D6():
        OP_6D(-14880, 0, 23640, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_14D6)

    def lambda_14EE():
        OP_6B(2740, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_14EE)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #27
        0x111,
        "#1740F#12PWell, that one shouldn't be too tough...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x112,
        "#1756F#12PYeah. We've seen those things near Ruan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x113,
        "#1766F#12PLet's hop to it!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x113, 0x1000)
    SetChrFlags(0x111, 0x1000)
    SetChrFlags(0x112, 0x1000)

    def lambda_15A4():
        OP_6D(-17040, -500, 26800, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_15A4)

    def lambda_15BC():
        OP_6B(2300, 1000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_15BC)
    SetChrChipByIndex(0x113, 20)
    SetChrSubChip(0x113, 0)

    def lambda_15D6():
        OP_8E(0xFE, 0xFFFFBB7C, 0xFFFFFE0C, 0x648C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_15D6)
    Sleep(50)
    SetChrChipByIndex(0x111, 18)
    SetChrSubChip(0x111, 0)

    def lambda_1600():
        OP_8E(0xFE, 0xFFFFBD0C, 0xFFFFFE0C, 0x648C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_1600)
    Sleep(50)
    SetChrChipByIndex(0x112, 19)
    SetChrSubChip(0x112, 0)

    def lambda_162A():
        OP_8E(0xFE, 0xFFFFBC44, 0xFFFFFE0C, 0x648C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_162A)
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

    # Function_8_13CE end

    def Function_9_1675(): pass

    label("Function_9_1675")

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
            "#1749F#5PWell, it was easier to beat than the last \x01",
            "monster...\x02\x03",

            "#1742FHell of a lot stronger than the ones near\x01",
            "Ruan, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x112,
        (
            "#1752F#12PLooks like we're gonna have to accept that\x01",
            "all the monsters in here're tougher than the\x01",
            "ones we know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x113,
        (
            "#1764F#6PU-Ugh...\x02\x03",

            "#1767FWhy am I struggling against these guys?!\x01",
            "They should be nothing!\x02\x03",

            "Damn it, damn it, DAMN IT!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_189E():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x111, 2, lambda_189E)
    Sleep(100)

    def lambda_18B1():

        label("loc_18B1")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_18B1")

    QueueWorkItem2(0x112, 2, lambda_18B1)
    Sleep(300)

    ChrTalk(    #33
        0x111,
        (
            "#1743F#5PH-Hey... Calm down, Rocco.\x02\x03",

            "We might be struggling, but it's not like we\x01",
            "can't take 'em. As long as we take things\x01",
            "slow and rest after every fight, we got this.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0x113,
        (
            "#1767F#6PRest after every battle?!\x02\x03",

            "#1766FIf we need to take a break after every loser\x01",
            "of a monster like that, how're we ever gonna\x01",
            "catch up to that asshole?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x111,
        "#1742F#5PI-Is this really the time to think about that?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x113, 225, 500)
    Sleep(300)

    ChrTalk(    #36
        0x113,
        "#1767F#6PThe next one is gonna be a breeze. It is!\x02",
    )

    CloseMessageWindow()

    def lambda_1AB7():
        OP_8E(0xFE, 0xFFFF9A5C, 0x0, 0x4D76, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_1AB7)
    Sleep(1000)

    ChrTalk(    #37
        0x111,
        "#1743F#5PH-Hey! Rocco!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x112,
        (
            "#1753F#11PWhew... He's starting to let his temper get\x01",
            "the better of him.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x112, 0x2)

    def lambda_1B45():
        OP_8E(0xFE, 0xFFFF9A5C, 0x0, 0x4D76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_1B45)
    Sleep(100)

    def lambda_1B65():
        OP_8E(0xFE, 0xFFFF9A5C, 0x0, 0x479A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_1B65)
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
    OP_C4(0x1, 0x20000000)
    OP_A2(0x2F93)
    OP_B2(0x0, 0x1, 0x80)
    EventEnd(0x4)
    Return()

    # Function_9_1675 end

    def Function_10_1C35(): pass

    label("Function_10_1C35")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x160, 1)"), scpexpr(EXPR_END)), "loc_1CA3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05Found \x1F\x60\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE0)
    Jump("loc_1D0B")

    label("loc_1CA3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x07\x05Found \x1F\x60\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x60\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_1D0B")

    Jump("loc_1D6C")

    label("loc_1D0E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05All that's left at the bottom is the tiny glimmer of hope.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x1, 0x0)

    label("loc_1D6C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1C35 end

    def Function_11_1D7A(): pass

    label("Function_11_1D7A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E53")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1DE8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x05Found \x1F\xFC\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE1)
    Jump("loc_1E50")

    label("loc_1DE8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #43
        (
            "\x07\x05Found \x1F\xFC\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFC\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1E50")

    Jump("loc_1ED0")

    label("loc_1E53")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "\x07\x05Unfortunately, what you stole from me won't help relieve you of your\x01",
            "kleptomaniac issues.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x2, 0x0)

    label("loc_1ED0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1D7A end

    def Function_12_1EDE(): pass

    label("Function_12_1EDE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16E, 1)"), scpexpr(EXPR_END)), "loc_1F4C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05Found \x1F\x6E\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE2)
    Jump("loc_1FB4")

    label("loc_1F4C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "\x07\x05Found \x1F\x6E\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x6E\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1FB4")

    Jump("loc_2048")

    label("loc_1FB7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        (
            "\x07\x05Someone scrawled a limerick on the inside of the chest...oh. OH. Okay.\x01",
            "Wow. That's not gonna pass a T-rating.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x3, 0x0)

    label("loc_2048")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1EDE end

    def Function_13_2056(): pass

    label("Function_13_2056")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_20C4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x05Found \x1F\x07\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE3)
    Jump("loc_212C")

    label("loc_20C4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "\x07\x05Found \x1F\x07\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x07\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_212C")

    Jump("loc_2172")

    label("loc_212F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05The treasure was you all along!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x4, 0x0)

    label("loc_2172")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_2056 end

    def Function_14_2180(): pass

    label("Function_14_2180")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2259")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_21EE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        "\x07\x05Found \x1F\x07\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE4)
    Jump("loc_2256")

    label("loc_21EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        (
            "\x07\x05Found \x1F\x07\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x07\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_2256")

    Jump("loc_230F")

    label("loc_2259")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        (
            "\x07\x05Do you know the name of Estelle Bright? The thief without equal. In her\x01",
            "lifetime, she stole many treasures and left behind over a thousand chests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x5, 0x0)

    label("loc_230F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_2180 end

    def Function_15_231D(): pass

    label("Function_15_231D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_238B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x05Found \x1F\x05\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE5)
    Jump("loc_23F3")

    label("loc_238B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "\x07\x05Found \x1F\x05\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x05\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_23F3")

    Jump("loc_2442")

    label("loc_23F6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05Thanks for lifting that guilt off of me.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x6, 0x0)

    label("loc_2442")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_231D end

    def Function_16_2450(): pass

    label("Function_16_2450")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2529")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x207, 1)"), scpexpr(EXPR_END)), "loc_24BE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #57
        "\x07\x05Found \x1F\x07\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FE6)
    Jump("loc_2526")

    label("loc_24BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #58
        (
            "\x07\x05Found \x1F\x07\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x07\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_2526")

    Jump("loc_257F")

    label("loc_2529")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05Excuse me. I got lost... Can you take me with you?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x7, 0x0)

    label("loc_257F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_2450 end

    SaveToFile()

Try(main)
