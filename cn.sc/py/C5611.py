from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5611   ._SN',
        MapName             = 'Other',
        Location            = 'C5611.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60061",
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
        '卡露娜',                               # 9
        '哨兵570',                              # 10
        '哨兵570',                              # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12320 ._CH',             # 02
        'ED6_DT29/CH12321 ._CH',             # 03
        'ED6_DT29/CH12330 ._CH',             # 04
        'ED6_DT29/CH12331 ._CH',             # 05
        'ED6_DT29/CH12350 ._CH',             # 06
        'ED6_DT29/CH12351 ._CH',             # 07
        'ED6_DT29/CH12000 ._CH',             # 08
        'ED6_DT29/CH12201 ._CH',             # 09
        'ED6_DT07/CH01240 ._CH',             # 0A
        'ED6_DT27/CH04000 ._CH',             # 0B
        'ED6_DT27/CH04001 ._CH',             # 0C
        'ED6_DT07/CH00120 ._CH',             # 0D
        'ED6_DT07/CH00121 ._CH',             # 0E
        'ED6_DT07/CH00150 ._CH',             # 0F
        'ED6_DT07/CH00151 ._CH',             # 10
        'ED6_DT07/CH00130 ._CH',             # 11
        'ED6_DT07/CH00131 ._CH',             # 12
        'ED6_DT07/CH00140 ._CH',             # 13
        'ED6_DT07/CH00141 ._CH',             # 14
        'ED6_DT07/CH00160 ._CH',             # 15
        'ED6_DT07/CH00161 ._CH',             # 16
        'ED6_DT07/CH00170 ._CH',             # 17
        'ED6_DT07/CH00171 ._CH',             # 18
        'ED6_DT27/CH04080 ._CH',             # 19
        'ED6_DT27/CH04081 ._CH',             # 1A
        'ED6_DT26/CH20405 ._CH',             # 1B
        'ED6_DT27/CH03084 ._CH',             # 1C
        'ED6_DT07/CH00400 ._CH',             # 1D
        'ED6_DT26/CH20373 ._CH',             # 1E
        'ED6_DT07/CH00401 ._CH',             # 1F
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12320P._CP',             # 02
        'ED6_DT29/CH12321P._CP',             # 03
        'ED6_DT29/CH12330P._CP',             # 04
        'ED6_DT29/CH12331P._CP',             # 05
        'ED6_DT29/CH12350P._CP',             # 06
        'ED6_DT29/CH12351P._CP',             # 07
        'ED6_DT29/CH12000P._CP',             # 08
        'ED6_DT29/CH12201P._CP',             # 09
        'ED6_DT07/CH01240P._CP',             # 0A
        'ED6_DT27/CH04000P._CP',             # 0B
        'ED6_DT27/CH04001P._CP',             # 0C
        'ED6_DT07/CH00120P._CP',             # 0D
        'ED6_DT07/CH00121P._CP',             # 0E
        'ED6_DT07/CH00150P._CP',             # 0F
        'ED6_DT07/CH00151P._CP',             # 10
        'ED6_DT07/CH00130P._CP',             # 11
        'ED6_DT07/CH00131P._CP',             # 12
        'ED6_DT07/CH00140P._CP',             # 13
        'ED6_DT07/CH00141P._CP',             # 14
        'ED6_DT07/CH00160P._CP',             # 15
        'ED6_DT07/CH00161P._CP',             # 16
        'ED6_DT07/CH00170P._CP',             # 17
        'ED6_DT07/CH00171P._CP',             # 18
        'ED6_DT27/CH04080P._CP',             # 19
        'ED6_DT27/CH04081P._CP',             # 1A
        'ED6_DT26/CH20405P._CP',             # 1B
        'ED6_DT27/CH03084P._CP',             # 1C
        'ED6_DT07/CH00400P._CP',             # 1D
        'ED6_DT26/CH20373P._CP',             # 1E
        'ED6_DT07/CH00401P._CP',             # 1F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 2,
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
        Unknown3            = 2,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 75020,
        Z                   = 0,
        Y                   = 90910,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 86930,
        Z                   = 0,
        Y                   = -61050,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -145090,
        Z                   = 0,
        Y                   = -59140,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 18990,
        Y                   = -1000,
        Z                   = 151320,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 30960,
        Y                   = -1000,
        Z                   = 151350,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 26,
    )


    DeclActor(
        TriggerX            = -19300,
        TriggerZ            = 0,
        TriggerY            = 145970,
        TriggerRange        = 1000,
        ActorX              = -20000,
        ActorZ              = 0,
        ActorY              = 145970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -140290,
        TriggerZ            = 0,
        TriggerY            = -59010,
        TriggerRange        = 1000,
        ActorX              = -141000,
        ActorZ              = 0,
        ActorY              = -59010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -135290,
        TriggerZ            = 0,
        TriggerY            = 18060,
        TriggerRange        = 1000,
        ActorX              = -136000,
        ActorZ              = 0,
        ActorY              = 17970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 70300,
        TriggerZ            = 0,
        TriggerY            = 95020,
        TriggerRange        = 1000,
        ActorX              = 70960,
        ActorZ              = 0,
        ActorY              = 95020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 74300,
        TriggerZ            = 0,
        TriggerY            = 4460,
        TriggerRange        = 1000,
        ActorX              = 75000,
        ActorZ              = 0,
        ActorY              = 4550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 82300,
        TriggerZ            = 0,
        TriggerY            = -57020,
        TriggerRange        = 1000,
        ActorX              = 83010,
        ActorZ              = 0,
        ActorY              = -57020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49710,
        TriggerZ            = 0,
        TriggerY            = 32470,
        TriggerRange        = 1000,
        ActorX              = -49050,
        ActorZ              = 0,
        ActorY              = 32509,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -93050,
        TriggerZ            = 0,
        TriggerY            = 131020,
        TriggerRange        = 800,
        ActorX              = -93050,
        ActorZ              = 1000,
        ActorY              = 131020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23370,
        TriggerZ            = 0,
        TriggerY            = -6800,
        TriggerRange        = 800,
        ActorX              = 23370,
        ActorZ              = 1100,
        ActorY              = -6800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92840,
        TriggerZ            = 0,
        TriggerY            = -56890,
        TriggerRange        = 800,
        ActorX              = -92840,
        ActorZ              = 1100,
        ActorY              = -56890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 32759,
        TriggerZ            = 0,
        TriggerY            = 151710,
        TriggerRange        = 800,
        ActorX              = 32759,
        ActorZ              = 1100,
        ActorY              = 151710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14340,
        TriggerZ            = 0,
        TriggerY            = 146480,
        TriggerRange        = 800,
        ActorX              = 14340,
        ActorZ              = 1100,
        ActorY              = 146480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -103760,
        TriggerZ            = 0,
        TriggerY            = 20520,
        TriggerRange        = 800,
        ActorX              = -103760,
        ActorZ              = 1100,
        ActorY              = 20520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_48B",          # 01, 1
        "Function_2_612",          # 02, 2
        "Function_3_628",          # 03, 3
        "Function_4_6CD",          # 04, 4
        "Function_5_7E4",          # 05, 5
        "Function_6_889",          # 06, 6
        "Function_7_9A0",          # 07, 7
        "Function_8_AB7",          # 08, 8
        "Function_9_BCE",          # 09, 9
        "Function_10_CE5",         # 0A, 10
        "Function_11_D81",         # 0B, 11
        "Function_12_E1D",         # 0C, 12
        "Function_13_EB9",         # 0D, 13
        "Function_14_F55",         # 0E, 14
        "Function_15_FF1",         # 0F, 15
        "Function_16_11FF",        # 10, 16
        "Function_17_1627",        # 11, 17
        "Function_18_1763",        # 12, 18
        "Function_19_17CE",        # 13, 19
        "Function_20_182C",        # 14, 20
        "Function_21_188A",        # 15, 21
        "Function_22_2077",        # 16, 22
        "Function_23_21EE",        # 17, 23
        "Function_24_2278",        # 18, 24
        "Function_25_22D5",        # 19, 25
        "Function_26_22E8",        # 1A, 26
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A")
    Event(0, 16)

    label("loc_48A")

    Return()

    # Function_0_472 end

    def Function_1_48B(): pass

    label("Function_1_48B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7F), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x84), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BF")
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    Jump("loc_4C3")

    label("loc_4BF")

    OP_78(0x74, 0x6A, 0x7C)

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D5")
    OP_6F(0x0, 0)
    Jump("loc_4DC")

    label("loc_4D5")

    OP_6F(0x0, 60)

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE")
    OP_6F(0x1, 0)
    Jump("loc_4F5")

    label("loc_4EE")

    OP_6F(0x1, 60)

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507")
    OP_6F(0x2, 0)
    Jump("loc_50E")

    label("loc_507")

    OP_6F(0x2, 60)

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_520")
    OP_6F(0x3, 0)
    Jump("loc_527")

    label("loc_520")

    OP_6F(0x3, 60)

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539")
    OP_6F(0x4, 0)
    Jump("loc_540")

    label("loc_539")

    OP_6F(0x4, 60)

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552")
    OP_6F(0x5, 0)
    Jump("loc_559")

    label("loc_552")

    OP_6F(0x5, 60)

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56B")
    OP_6F(0x6, 0)
    Jump("loc_572")

    label("loc_56B")

    OP_6F(0x6, 60)

    label("loc_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x382, 3)), scpexpr(EXPR_END)), "loc_588")
    OP_64(0x8, 0x1)
    OP_10(0xE, 0x1)
    OP_71(0x11, 0x10)
    Jump("loc_590")

    label("loc_588")

    OP_10(0xE, 0x0)
    OP_72(0x11, 0x10)

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x382, 4)), scpexpr(EXPR_END)), "loc_5A6")
    OP_64(0x9, 0x1)
    OP_10(0x18, 0x1)
    OP_71(0x13, 0x10)
    Jump("loc_5AE")

    label("loc_5A6")

    OP_10(0x18, 0x0)
    OP_72(0x13, 0x10)

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x382, 5)), scpexpr(EXPR_END)), "loc_5C4")
    OP_64(0xA, 0x1)
    OP_10(0x1, 0x1)
    OP_71(0x1A, 0x10)
    Jump("loc_5CC")

    label("loc_5C4")

    OP_10(0x1, 0x0)
    OP_72(0x1A, 0x10)

    label("loc_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x382, 6)), scpexpr(EXPR_END)), "loc_5E2")
    OP_64(0xB, 0x1)
    OP_10(0x2, 0x1)
    OP_71(0x10, 0x10)
    Jump("loc_5EA")

    label("loc_5E2")

    OP_10(0x2, 0x0)
    OP_72(0x10, 0x10)

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x382, 7)), scpexpr(EXPR_END)), "loc_600")
    OP_64(0xC, 0x1)
    OP_10(0x1E, 0x1)
    OP_71(0x16, 0x10)
    Jump("loc_608")

    label("loc_600")

    OP_10(0x1E, 0x0)
    OP_72(0x16, 0x10)

    label("loc_608")

    OP_74(0x21, 0x0, 0x0)
    Return()

    # Function_1_48B end

    def Function_2_612(): pass

    label("Function_2_612")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_627")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_612")

    label("loc_627")

    Return()

    # Function_2_612 end

    def Function_3_628(): pass

    label("Function_3_628")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x3, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了\x07\x02#59I风之耀晶片×２００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D10)
    Jump("loc_6BB")

    label("loc_6A1")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_6BB")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_628 end

    def Function_4_6CD(): pass

    label("Function_4_6CD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x185, 1)"), scpexpr(EXPR_END)), "loc_73C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\x85\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D12)
    Jump("loc_7A2")

    label("loc_73C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\x85\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x85\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_7A2")

    Jump("loc_7D6")

    label("loc_7A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7D6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6CD end

    def Function_5_7E4(): pass

    label("Function_5_7E4")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x2, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        (
            "\x07\x00得到了\x07\x02#58I火之耀晶片×２００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D14)
    Jump("loc_877")

    label("loc_85D")


    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_877")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7E4 end

    def Function_6_889(): pass

    label("Function_6_889")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_961")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_8F8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D16)
    Jump("loc_95E")

    label("loc_8F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_95E")

    Jump("loc_992")

    label("loc_961")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_992")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_889 end

    def Function_7_9A0(): pass

    label("Function_7_9A0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A78")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x150, 1)"), scpexpr(EXPR_END)), "loc_A0F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\x50\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D17)
    Jump("loc_A75")

    label("loc_A0F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "宝箱里装有\x1F\x50\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x50\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_A75")

    Jump("loc_AA9")

    label("loc_A78")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AA9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_9A0 end

    def Function_8_AB7(): pass

    label("Function_8_AB7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_B26")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D18)
    Jump("loc_B8C")

    label("loc_B26")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_B8C")

    Jump("loc_BC0")

    label("loc_B8F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BC0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_AB7 end

    def Function_9_BCE(): pass

    label("Function_9_BCE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17B, 1)"), scpexpr(EXPR_END)), "loc_C3D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\x7B\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D19)
    Jump("loc_CA3")

    label("loc_C3D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\x7B\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x7B\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_CA3")

    Jump("loc_CD7")

    label("loc_CA6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CD7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_BCE end

    def Function_10_CE5(): pass

    label("Function_10_CE5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D59")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x1E)
    OP_73(0x11)
    OP_64(0x8, 0x1)
    OP_10(0xE, 0x1)
    OP_A2(0x1C13)
    Jump("loc_D7D")

    label("loc_D59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7D")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_D7D")

    label("loc_D7D")

    TalkEnd(0xFF)
    Return()

    # Function_10_CE5 end

    def Function_11_D81(): pass

    label("Function_11_D81")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF5")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x1E)
    OP_73(0x13)
    OP_64(0x9, 0x1)
    OP_10(0x18, 0x1)
    OP_A2(0x1C14)
    Jump("loc_E19")

    label("loc_DF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E19")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_E19")

    label("loc_E19")

    TalkEnd(0xFF)
    Return()

    # Function_11_D81 end

    def Function_12_E1D(): pass

    label("Function_12_E1D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E91")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x1A, 0)
    OP_70(0x1A, 0x1E)
    OP_73(0x1A)
    OP_64(0xA, 0x1)
    OP_10(0x1, 0x1)
    OP_A2(0x1C15)
    Jump("loc_EB5")

    label("loc_E91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EB5")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_EB5")

    label("loc_EB5")

    TalkEnd(0xFF)
    Return()

    # Function_12_E1D end

    def Function_13_EB9(): pass

    label("Function_13_EB9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2D")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x10, 0)
    OP_70(0x10, 0x1E)
    OP_73(0x10)
    OP_64(0xB, 0x1)
    OP_10(0x2, 0x1)
    OP_A2(0x1C16)
    Jump("loc_F51")

    label("loc_F2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F51")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_F51")

    label("loc_F51")

    TalkEnd(0xFF)
    Return()

    # Function_13_EB9 end

    def Function_14_F55(): pass

    label("Function_14_F55")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC9")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x16, 0)
    OP_70(0x16, 0x1E)
    OP_73(0x16)
    OP_64(0xC, 0x1)
    OP_10(0x1E, 0x1)
    OP_A2(0x1C17)
    Jump("loc_FED")

    label("loc_FC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FED")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_FED")

    label("loc_FED")

    TalkEnd(0xFF)
    Return()

    # Function_14_F55 end

    def Function_15_FF1(): pass

    label("Function_15_FF1")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 1)), scpexpr(EXPR_END)), "loc_100C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 4)), scpexpr(EXPR_END)), "loc_101D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_101D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 6)), scpexpr(EXPR_END)), "loc_102E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_102E")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_105A"),
        (1, "loc_1067"),
        (3, "loc_10C3"),
        (7, "loc_1143"),
        (SWITCH_DEFAULT, "loc_11E7"),
    )


    label("loc_105A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E7")

    label("loc_1067")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色密码卡】\x01",      # 0
            "【什么也不做】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10A6"),
        (1, "loc_10B3"),
        (SWITCH_DEFAULT, "loc_10C0"),
    )


    label("loc_10A6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10C0")

    label("loc_10B3")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10C0")

    label("loc_10C0")

    Jump("loc_11E7")

    label("loc_10C3")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色密码卡】\x01",      # 0
            "【使用绿色密码卡】\x01",      # 1
            "【什么也不做】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1119"),
        (1, "loc_1126"),
        (2, "loc_1133"),
        (SWITCH_DEFAULT, "loc_1140"),
    )


    label("loc_1119")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1140")

    label("loc_1126")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1140")

    label("loc_1133")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1140")

    label("loc_1140")

    Jump("loc_11E7")

    label("loc_1143")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色密码卡】\x01",      # 0
            "【使用绿色密码卡】\x01",      # 1
            "【使用蓝色密码卡】\x01",      # 2
            "【什么也不做】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11B0"),
        (1, "loc_11BD"),
        (2, "loc_11CA"),
        (3, "loc_11D7"),
        (SWITCH_DEFAULT, "loc_11E4"),
    )


    label("loc_11B0")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E4")

    label("loc_11BD")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E4")

    label("loc_11CA")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E4")

    label("loc_11D7")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E4")

    label("loc_11E4")

    Jump("loc_11E7")

    label("loc_11E7")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_15_FF1 end

    def Function_16_11FF(): pass

    label("Function_16_11FF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1216")
    Call(0, 23)
    Call(0, 24)

    label("loc_1216")

    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, -92720, 0, 128000, 0)
    SetChrPos(0x8, -92720, 0, 127000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -92180, 20, 116110, 0)
    SetChrPos(0x109, -93490, 20, 116110, 0)
    SetChrPos(0xF8, -92180, 0, 114880, 0)
    SetChrPos(0xF9, -93490, 0, 114830, 0)
    OP_6D(-93240, 20, 116200, 0)
    OP_67(0, 7620, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(271, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #24
        0x101,
        "#1005F#6P啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_12EF():
        OP_6D(-93030, 20, 123000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12EF)

    def lambda_1307():
        OP_67(0, 5090, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1307)

    def lambda_131F():
        OP_6B(2610, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_131F)

    def lambda_132F():
        OP_6E(340, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_132F)
    Sleep(2000)

    def lambda_1344():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1344)
    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 29)
    SetChrSubChip(0x8, 0)
    Sleep(1000)

    ChrTalk(    #25
        0x8,
        "#837F#2P………………………………\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 11)
    SetChrChipByIndex(0x109, 25)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_13B6"),
        (5, "loc_13BE"),
        (3, "loc_13C6"),
        (4, "loc_13CE"),
        (6, "loc_13D6"),
        (7, "loc_13DE"),
        (SWITCH_DEFAULT, "loc_13E6"),
    )


    label("loc_13B6")

    SetChrChipByIndex(0xF8, 13)
    Jump("loc_13E6")

    label("loc_13BE")

    SetChrChipByIndex(0xF8, 15)
    Jump("loc_13E6")

    label("loc_13C6")

    SetChrChipByIndex(0xF8, 17)
    Jump("loc_13E6")

    label("loc_13CE")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_13E6")

    label("loc_13D6")

    SetChrChipByIndex(0xF8, 21)
    Jump("loc_13E6")

    label("loc_13DE")

    SetChrChipByIndex(0xF8, 23)
    Jump("loc_13E6")

    label("loc_13E6")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1407"),
        (5, "loc_140F"),
        (3, "loc_1417"),
        (4, "loc_141F"),
        (6, "loc_1427"),
        (7, "loc_142F"),
        (SWITCH_DEFAULT, "loc_1437"),
    )


    label("loc_1407")

    SetChrChipByIndex(0xF9, 13)
    Jump("loc_1437")

    label("loc_140F")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_1437")

    label("loc_1417")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_1437")

    label("loc_141F")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_1437")

    label("loc_1427")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_1437")

    label("loc_142F")

    SetChrChipByIndex(0xF9, 23)
    Jump("loc_1437")

    label("loc_1437")


    def lambda_143D():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_143D)
    Sleep(60)

    def lambda_145D():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_145D)
    Sleep(100)

    def lambda_147D():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_147D)
    Sleep(70)

    def lambda_149D():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_149D)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #26
        0x101,
        "#1002F#6P果然卡露娜前辈也……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_150D")

    ChrTalk(    #27
        0x106,
        "#057F#6P可恶，只能拚了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_158C")

    label("loc_150D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153A")

    ChrTalk(    #28
        0x103,
        "#022F#6P只能拚了呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_158C")

    label("loc_153A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156B")

    ChrTalk(    #29
        0x108,
        "#072F#6P看来只能拚了啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_158C")

    label("loc_156B")


    ChrTalk(    #30
        0x109,
        "#1063F#6P看来只能拚了呢……\x02",
    )

    CloseMessageWindow()

    label("loc_158C")

    Sleep(200)
    OP_43(0x9, 0x0, 0x0, 0x13)
    Sleep(200)
    OP_43(0xA, 0x0, 0x0, 0x14)
    Sleep(1000)

    def lambda_15AF():
        OP_6D(-93220, 20, 124000, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_15AF)

    def lambda_15C7():
        OP_6B(2130, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_15C7)
    OP_43(0x101, 0x0, 0x0, 0x11)
    OP_43(0x8, 0x0, 0x0, 0x12)
    Sleep(300)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x41F, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_161D"),
        (SWITCH_DEFAULT, "loc_1622"),
    )


    label("loc_161D")

    OP_B4(0x0)
    Jump("loc_1622")

    label("loc_1622")

    Call(0, 21)
    Return()

    # Function_16_11FF end

    def Function_17_1627(): pass

    label("Function_17_1627")

    SetChrChipByIndex(0x101, 12)
    SetChrChipByIndex(0x109, 26)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_1652"),
        (5, "loc_165A"),
        (3, "loc_1662"),
        (4, "loc_166A"),
        (6, "loc_1672"),
        (7, "loc_167A"),
        (SWITCH_DEFAULT, "loc_1682"),
    )


    label("loc_1652")

    SetChrChipByIndex(0xF8, 14)
    Jump("loc_1682")

    label("loc_165A")

    SetChrChipByIndex(0xF8, 16)
    Jump("loc_1682")

    label("loc_1662")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_1682")

    label("loc_166A")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_1682")

    label("loc_1672")

    SetChrChipByIndex(0xF8, 22)
    Jump("loc_1682")

    label("loc_167A")

    SetChrChipByIndex(0xF8, 24)
    Jump("loc_1682")

    label("loc_1682")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_16A3"),
        (5, "loc_16AB"),
        (3, "loc_16B3"),
        (4, "loc_16BB"),
        (6, "loc_16C3"),
        (7, "loc_16CB"),
        (SWITCH_DEFAULT, "loc_16D3"),
    )


    label("loc_16A3")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_16D3")

    label("loc_16AB")

    SetChrChipByIndex(0xF9, 16)
    Jump("loc_16D3")

    label("loc_16B3")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_16D3")

    label("loc_16BB")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_16D3")

    label("loc_16C3")

    SetChrChipByIndex(0xF9, 22)
    Jump("loc_16D3")

    label("loc_16CB")

    SetChrChipByIndex(0xF9, 24)
    Jump("loc_16D3")

    label("loc_16D3")

    SetChrFlags(0x101, 0x1000)

    def lambda_16DE():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16DE)
    Sleep(50)
    SetChrFlags(0x109, 0x1000)

    def lambda_1703():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1703)
    Sleep(50)
    SetChrFlags(0xF8, 0x1000)

    def lambda_1728():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1728)
    Sleep(50)
    SetChrFlags(0xF9, 0x1000)

    def lambda_174D():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_174D)
    Return()

    # Function_17_1627 end

    def Function_18_1763(): pass

    label("Function_18_1763")

    SetChrChipByIndex(0x8, 31)

    def lambda_176E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_176E)
    Sleep(50)
    SetChrChipByIndex(0x9, 1)

    def lambda_1793():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1793)
    Sleep(50)
    SetChrChipByIndex(0xA, 1)

    def lambda_17B8():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_17B8)
    Return()

    # Function_18_1763 end

    def Function_19_17CE(): pass

    label("Function_19_17CE")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -91180, 1200, 128710, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_180B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_180B)
    OP_8F(0xFE, 0xFFFE9BD4, 0x0, 0x1F6C6, 0x7D0, 0x0)
    Return()

    # Function_19_17CE end

    def Function_20_182C(): pass

    label("Function_20_182C")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -94460, 1200, 128720, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_1869():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1869)
    OP_8F(0xFE, 0xFFFE8F04, 0x0, 0x1F6D0, 0x7D0, 0x0)
    Return()

    # Function_20_182C end

    def Function_21_188A(): pass

    label("Function_21_188A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_44(0x8, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_44(0x8, 0x3)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x8, -92930, 20, 125700, 180)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x101, -92200, 20, 122860, 0)
    SetChrPos(0x109, -93290, 20, 122860, 0)
    SetChrPos(0xF8, -92200, 20, 121500, 0)
    SetChrPos(0xF9, -93290, 20, 121500, 0)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x109, 0x1000)
    ClearChrFlags(0xF8, 0x1000)
    ClearChrFlags(0xF9, 0x1000)
    OP_6D(-93520, 20, 124240, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(315000, 0)
    OP_6E(273, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #31
        0x101,
        (
            "#1007F#6P果、果然是\x01",
            "一场苦战……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        "#1060F#6P好，该我出场了。\x02",
    )

    CloseMessageWindow()

    def lambda_19F7():
        OP_6D(-93520, 20, 125240, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19F7)
    OP_8E(0x109, 0xFFFE951C, 0x14, 0x1E3FC, 0x5DC, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    SetChrChipByIndex(0x109, 30)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    Sleep(1000)
    LoadEffect(0x0, "scraft\\\\sc008_02.eff")
    PlayEffect(0x0, 0xFF, 0x109, 300, 1100, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    LoadEffect(0x0, "scraft\\\\sc001_05.eff")
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_9E(0x8, 0x14, 0x0, 0x1F4, 0xBB8)
    Sleep(1000)

    ChrTalk(    #33
        0x8,
        "#836F#2P唔……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x8, 1)
    Sleep(1000)

    ChrTalk(    #34
        0x8,
        (
            "#835F#2P你、你们……\x02\x03",

            "竟然能跑到\x01",
            "这种地方来……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    OP_0D()

    def lambda_1B6D():
        OP_8F(0x109, 0xFFFE9396, 0x14, 0x1DFEC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B6D)

    ChrTalk(    #35
        0x101,
        "#1020F#6P卡露娜前辈，你没事吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#833F#2P啊啊……不要紧……\x02\x03",

            "#832F话说回来……\x01",
            "找到其它人了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3A")

    ChrTalk(    #37
        0x103,
        (
            "#020F#6P刚才把库拉茨\x01",
            "救出来了。\x02\x03",

            "#025F亚妮拉丝还没……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1C3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C89")

    ChrTalk(    #38
        0x106,
        (
            "#051F#6P刚才把库拉茨\x01",
            "救出来了。\x02\x03",

            "#053F还没找到亚妮拉丝。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1C89")


    ChrTalk(    #39
        0x101,
        (
            "#1006F#6P刚刚才把库拉茨\x01",
            "前辈救出来了。\x02\x03",

            "#1007F亚妮拉丝还没有……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCF")


    ChrTalk(    #40
        0x8,
        (
            "#833F#2P是吗……\x02\x03",

            "#832F没有碰上那些\x01",
            "『执行者』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1002F#6P没有，倒是跟那些\x01",
            "人形兵器战斗了好几次……\x02\x03",

            "这里好像完全\x01",
            "没有人的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#834F#2P好奇怪……\x02\x03",

            "其它士兵和研究员\x01",
            "应该还有几十人才对……\x02\x03",

            "#833F或许已经……\x01",
            "撤退了也说不定。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0C")

    ChrTalk(    #43
        0x108,
        (
            "#074F#6P嗯……\x02\x03",

            "#070F虽然不可大意，\x01",
            "但也有这个可能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E71")

    label("loc_1E0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E41")

    ChrTalk(    #44
        0x105,
        "#043F#6P这个可能性似乎很高……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E71")

    label("loc_1E41")


    ChrTalk(    #45
        0x101,
        (
            "#1015F#6P原来如此……\x01",
            "这个可能性应该不低。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E71")


    ChrTalk(    #46
        0x8,
        (
            "#835F#2P我可以想办法\x01",
            "一个人逃出去……\x02\x03",

            "至于亚妮拉丝……\x01",
            "请你们尽快找到她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1006F#6P嗯……交给我们吧！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C0B)
    OP_28(0x98, 0x1, 0x40)
    OP_9E(0x8, 0x14, 0x0, 0x12C, 0xBB8)
    Fade(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 10)
    OP_0D()
    Sleep(1000)

    def lambda_1F19():

        label("loc_1F19")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1F19")

    QueueWorkItem2(0x101, 1, lambda_1F19)

    def lambda_1F2A():

        label("loc_1F2A")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1F2A")

    QueueWorkItem2(0x109, 1, lambda_1F2A)

    def lambda_1F3B():

        label("loc_1F3B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1F3B")

    QueueWorkItem2(0xF8, 1, lambda_1F3B)

    def lambda_1F4C():

        label("loc_1F4C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1F4C")

    QueueWorkItem2(0xF9, 1, lambda_1F4C)

    def lambda_1F5D():
        OP_6D(-93050, 20, 118350, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F5D)
    OP_8E(0x8, 0xFFFE9DF0, 0x14, 0x1E1D6, 0x7D0, 0x0)

    def lambda_1F89():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F89)
    OP_8E(0x8, 0xFFFE9F58, 0x0, 0x1D48E, 0x9C4, 0x0)

    def lambda_1FB7():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FB7)
    OP_8E(0x8, 0xFFFE9698, 0x0, 0x1C368, 0x7D0, 0x0)

    def lambda_1FE5():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FE5)
    OP_8E(0x8, 0xFFFE94C2, 0x0, 0x1BA6C, 0x9C4, 0x0)

    def lambda_2013():
        OP_8E(0xFE, 0xFFFE95B2, 0x0, 0x1B7D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2013)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)

    def lambda_205D():
        OP_6D(-93110, 20, 122720, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_205D)
    WaitChrThread(0x101, 0x0)
    EventEnd(0x0)
    Return()

    # Function_21_188A end

    def Function_22_2077(): pass

    label("Function_22_2077")

    EventBegin(0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x21, 0x0, 0x3)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #48
        (
            "\x07\x02#1S『对战斗员的处置』\x01",
            " \x01",
            "对于从各地的猎兵团等处\x01",
            "临时确保的战斗员，\x01",
            "应该施予以下的处置。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_74(0x21, 0x0, 0x4)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #49
        (
            "\x07\x02#1S①身体能力强化程序\x01",
            "②战斗技术学习程序\x01",
            "③命令系统植入程序\x01",
            "④机密保持暗示程序（※以下删除）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21CF")
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #50
        "\x07\x00得到了\x1F\xFB\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FB, 1)
    Sleep(500)

    label("loc_21CF")

    OP_A2(0x1C0C)
    OP_28(0x98, 0x1, 0x80)
    OP_74(0x21, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x1)
    Return()

    # Function_22_2077 end

    def Function_23_21EE(): pass

    label("Function_23_21EE")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_226B"),
        (1, "loc_2271"),
        (SWITCH_DEFAULT, "loc_2277"),
    )


    label("loc_226B")

    OP_A2(0x1200)
    Jump("loc_2277")

    label("loc_2271")

    OP_A2(0x1201)
    Jump("loc_2277")

    label("loc_2277")

    Return()

    # Function_23_21EE end

    def Function_24_2278(): pass

    label("Function_24_2278")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_24_2278 end

    def Function_25_22D5(): pass

    label("Function_25_22D5")

    OP_A3(0x1C9A)
    OP_A2(0x1C9B)
    OP_A3(0x1C9C)
    OP_A3(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_25_22D5 end

    def Function_26_22E8(): pass

    label("Function_26_22E8")

    OP_A3(0x1C9A)
    OP_A3(0x1C9B)
    OP_A2(0x1C9C)
    OP_A3(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_26_22E8 end

    SaveToFile()

Try(main)
