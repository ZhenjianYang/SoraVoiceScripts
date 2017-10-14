from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Carna',                                # 9
        'Vogel 570',                            # 10
        'Vogel 570',                            # 11
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
        "Function_4_71D",          # 04, 4
        "Function_5_8AC",          # 05, 5
        "Function_6_983",          # 06, 6
        "Function_7_ABE",          # 07, 7
        "Function_8_C3C",          # 08, 8
        "Function_9_DAF",          # 09, 9
        "Function_10_ED8",         # 0A, 10
        "Function_11_F7B",         # 0B, 11
        "Function_12_101E",        # 0C, 12
        "Function_13_10C1",        # 0D, 13
        "Function_14_1164",        # 0E, 14
        "Function_15_1207",        # 0F, 15
        "Function_16_140B",        # 10, 16
        "Function_17_1850",        # 11, 17
        "Function_18_198C",        # 12, 18
        "Function_19_19F7",        # 13, 19
        "Function_20_1A55",        # 14, 20
        "Function_21_1AB3",        # 15, 21
        "Function_22_249C",        # 16, 22
        "Function_23_269A",        # 17, 23
        "Function_24_2723",        # 18, 24
        "Function_25_2780",        # 19, 25
        "Function_26_2793",        # 1A, 26
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

    OP_EA(0x2, 0xA4, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x3, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "Found #2C#59IWind Sepith x200#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D10)
    Jump("loc_70B")

    label("loc_6A2")


    AnonymousTalk(    #1
        (
            "\x07\x05Watch out! There's been somebody going around\x01",
            "looting all my friends, and I think he just got me!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_70B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_628 end

    def Function_4_71D(): pass

    label("Function_4_71D")

    OP_EA(0x2, 0xA5, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x185, 1)"), scpexpr(EXPR_END)), "loc_78E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\x85\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D12)
    Jump("loc_7F2")

    label("loc_78E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\x85\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x85\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_7F2")

    Jump("loc_89E")

    label("loc_7F5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05You sneakily crack the lid of the chest and take\x01",
            "a peek inside. Sadly, no treasure chest fairies\x01",
            "flying around in there. No items, either.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_89E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_71D end

    def Function_5_8AC(): pass

    label("Function_5_8AC")

    OP_EA(0x2, 0xA6, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_926")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x2, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        "Found #2C#58IFire Sepith x200#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D14)
    Jump("loc_971")

    label("loc_926")


    AnonymousTalk(    #6
        (
            "\x07\x05I've been looted two games now!\x01",
            "I won't stand for this much longer!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_971")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_8AC end

    def Function_6_983(): pass

    label("Function_6_983")

    OP_EA(0x2, 0xA7, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_9F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D16)
    Jump("loc_A58")

    label("loc_9F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_A58")

    Jump("loc_AB0")

    label("loc_A5B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05The chest is empty. And if it could eat you, it\x01",
            "would.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AB0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_983 end

    def Function_7_ABE(): pass

    label("Function_7_ABE")

    OP_EA(0x2, 0xA8, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B96")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x150, 1)"), scpexpr(EXPR_END)), "loc_B2F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\x50\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D17)
    Jump("loc_B93")

    label("loc_B2F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\x50\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x50\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_B93")

    Jump("loc_C2E")

    label("loc_B96")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05All of this chest's worldly possessions now\x01",
            "reside within your pack. Unless you sold\x01",
            "them. You didn't SELL them, did you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C2E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_ABE end

    def Function_8_C3C(): pass

    label("Function_8_C3C")

    OP_EA(0x2, 0xA9, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D14")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_CAD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D18)
    Jump("loc_D11")

    label("loc_CAD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_D11")

    Jump("loc_DA1")

    label("loc_D14")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05As you search the empty chest's insides,\x01",
            "just in case you missed something last time,\x01",
            "it gives you a splinter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DA1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C3C end

    def Function_9_DAF(): pass

    label("Function_9_DAF")

    OP_EA(0x2, 0xAA, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E87")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17B, 1)"), scpexpr(EXPR_END)), "loc_E20")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "Found \x1F\x7B\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D19)
    Jump("loc_E84")

    label("loc_E20")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "Found \x1F\x7B\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x7B\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_E84")

    Jump("loc_ECA")

    label("loc_E87")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05This chest is as empty as your soul.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_ECA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_DAF end

    def Function_10_ED8(): pass

    label("Function_10_ED8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F53")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x1E)
    OP_73(0x11)
    OP_64(0x8, 0x1)
    OP_10(0xE, 0x1)
    OP_A2(0x1C13)
    Jump("loc_F77")

    label("loc_F53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F77")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_F77")

    label("loc_F77")

    TalkEnd(0xFF)
    Return()

    # Function_10_ED8 end

    def Function_11_F7B(): pass

    label("Function_11_F7B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF6")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x1E)
    OP_73(0x13)
    OP_64(0x9, 0x1)
    OP_10(0x18, 0x1)
    OP_A2(0x1C14)
    Jump("loc_101A")

    label("loc_FF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_101A")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_101A")

    label("loc_101A")

    TalkEnd(0xFF)
    Return()

    # Function_11_F7B end

    def Function_12_101E(): pass

    label("Function_12_101E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1099")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x1A, 0)
    OP_70(0x1A, 0x1E)
    OP_73(0x1A)
    OP_64(0xA, 0x1)
    OP_10(0x1, 0x1)
    OP_A2(0x1C15)
    Jump("loc_10BD")

    label("loc_1099")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10BD")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_10BD")

    label("loc_10BD")

    TalkEnd(0xFF)
    Return()

    # Function_12_101E end

    def Function_13_10C1(): pass

    label("Function_13_10C1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113C")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x10, 0)
    OP_70(0x10, 0x1E)
    OP_73(0x10)
    OP_64(0xB, 0x1)
    OP_10(0x2, 0x1)
    OP_A2(0x1C16)
    Jump("loc_1160")

    label("loc_113C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1160")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_1160")

    label("loc_1160")

    TalkEnd(0xFF)
    Return()

    # Function_13_10C1 end

    def Function_14_1164(): pass

    label("Function_14_1164")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 15)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DF")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x16, 0)
    OP_70(0x16, 0x1E)
    OP_73(0x16)
    OP_64(0xC, 0x1)
    OP_10(0x1E, 0x1)
    OP_A2(0x1C17)
    Jump("loc_1203")

    label("loc_11DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1203")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_1203")

    label("loc_1203")

    TalkEnd(0xFF)
    Return()

    # Function_14_1164 end

    def Function_15_1207(): pass

    label("Function_15_1207")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 1)), scpexpr(EXPR_END)), "loc_1222")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 4)), scpexpr(EXPR_END)), "loc_1233")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 6)), scpexpr(EXPR_END)), "loc_1244")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1244")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1270"),
        (1, "loc_127D"),
        (3, "loc_12D5"),
        (7, "loc_1352"),
        (SWITCH_DEFAULT, "loc_13F3"),
    )


    label("loc_1270")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13F3")

    label("loc_127D")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Red Cardkey]\x01",      # 0
            "[Don't Use]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12B8"),
        (1, "loc_12C5"),
        (SWITCH_DEFAULT, "loc_12D2"),
    )


    label("loc_12B8")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12D2")

    label("loc_12C5")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12D2")

    label("loc_12D2")

    Jump("loc_13F3")

    label("loc_12D5")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Red Cardkey]\x01",        # 0
            "[Use Green Cardkey]\x01",      # 1
            "[Don't Use]\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1328"),
        (1, "loc_1335"),
        (2, "loc_1342"),
        (SWITCH_DEFAULT, "loc_134F"),
    )


    label("loc_1328")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_134F")

    label("loc_1335")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_134F")

    label("loc_1342")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_134F")

    label("loc_134F")

    Jump("loc_13F3")

    label("loc_1352")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Red Cardkey]\x01",        # 0
            "[Use Green Cardkey]\x01",      # 1
            "[Use Blue Cardkey]\x01",       # 2
            "[Don't Use]\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13BC"),
        (1, "loc_13C9"),
        (2, "loc_13D6"),
        (3, "loc_13E3"),
        (SWITCH_DEFAULT, "loc_13F0"),
    )


    label("loc_13BC")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13F0")

    label("loc_13C9")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13F0")

    label("loc_13D6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13F0")

    label("loc_13E3")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13F0")

    label("loc_13F0")

    Jump("loc_13F3")

    label("loc_13F3")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_15_1207 end

    def Function_16_140B(): pass

    label("Function_16_140B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1422")
    Call(0, 23)
    Call(0, 24)

    label("loc_1422")

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
        "#1005F#6POh, no...!\x02",
    )

    CloseMessageWindow()

    def lambda_14FD():
        OP_6D(-93030, 20, 123000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14FD)

    def lambda_1515():
        OP_67(0, 5090, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1515)

    def lambda_152D():
        OP_6B(2610, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_152D)

    def lambda_153D():
        OP_6E(340, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_153D)
    Sleep(2000)

    def lambda_1552():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1552)
    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 29)
    SetChrSubChip(0x8, 0)
    Sleep(1000)

    ChrTalk(    #25
        0x8,
        "#837F#4P...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 11)
    SetChrChipByIndex(0x109, 25)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_15AF"),
        (5, "loc_15B7"),
        (3, "loc_15BF"),
        (4, "loc_15C7"),
        (6, "loc_15CF"),
        (7, "loc_15D7"),
        (SWITCH_DEFAULT, "loc_15DF"),
    )


    label("loc_15AF")

    SetChrChipByIndex(0xF8, 13)
    Jump("loc_15DF")

    label("loc_15B7")

    SetChrChipByIndex(0xF8, 15)
    Jump("loc_15DF")

    label("loc_15BF")

    SetChrChipByIndex(0xF8, 17)
    Jump("loc_15DF")

    label("loc_15C7")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_15DF")

    label("loc_15CF")

    SetChrChipByIndex(0xF8, 21)
    Jump("loc_15DF")

    label("loc_15D7")

    SetChrChipByIndex(0xF8, 23)
    Jump("loc_15DF")

    label("loc_15DF")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1600"),
        (5, "loc_1608"),
        (3, "loc_1610"),
        (4, "loc_1618"),
        (6, "loc_1620"),
        (7, "loc_1628"),
        (SWITCH_DEFAULT, "loc_1630"),
    )


    label("loc_1600")

    SetChrChipByIndex(0xF9, 13)
    Jump("loc_1630")

    label("loc_1608")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_1630")

    label("loc_1610")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_1630")

    label("loc_1618")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_1630")

    label("loc_1620")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_1630")

    label("loc_1628")

    SetChrChipByIndex(0xF9, 23)
    Jump("loc_1630")

    label("loc_1630")


    def lambda_1636():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1636)
    Sleep(60)

    def lambda_1656():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1656)
    Sleep(100)

    def lambda_1676():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1676)
    Sleep(70)

    def lambda_1696():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1696)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #26
        0x101,
        "#1002F#5PThey got Carna too...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1717")

    ChrTalk(    #27
        0x106,
        "#057F#5PTch. No choice but to fight, then...\x02",
    )

    CloseMessageWindow()
    Jump("loc_17B5")

    label("loc_1717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1750")

    ChrTalk(    #28
        0x103,
        "#022F#5PWe have no choice, then...\x02",
    )

    CloseMessageWindow()
    Jump("loc_17B5")

    label("loc_1750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1783")

    ChrTalk(    #29
        0x108,
        "#072F#5PWe must fight, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17B5")

    label("loc_1783")


    ChrTalk(    #30
        0x109,
        "#1063F#5PNo choice but to get rough, then...\x02",
    )

    CloseMessageWindow()

    label("loc_17B5")

    Sleep(200)
    OP_43(0x9, 0x0, 0x0, 0x13)
    Sleep(200)
    OP_43(0xA, 0x0, 0x0, 0x14)
    Sleep(1000)

    def lambda_17D8():
        OP_6D(-93220, 20, 124000, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17D8)

    def lambda_17F0():
        OP_6B(2130, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17F0)
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
        (1, "loc_1846"),
        (SWITCH_DEFAULT, "loc_184B"),
    )


    label("loc_1846")

    OP_B4(0x0)
    Jump("loc_184B")

    label("loc_184B")

    Call(0, 21)
    Return()

    # Function_16_140B end

    def Function_17_1850(): pass

    label("Function_17_1850")

    SetChrChipByIndex(0x101, 12)
    SetChrChipByIndex(0x109, 26)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_187B"),
        (5, "loc_1883"),
        (3, "loc_188B"),
        (4, "loc_1893"),
        (6, "loc_189B"),
        (7, "loc_18A3"),
        (SWITCH_DEFAULT, "loc_18AB"),
    )


    label("loc_187B")

    SetChrChipByIndex(0xF8, 14)
    Jump("loc_18AB")

    label("loc_1883")

    SetChrChipByIndex(0xF8, 16)
    Jump("loc_18AB")

    label("loc_188B")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_18AB")

    label("loc_1893")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_18AB")

    label("loc_189B")

    SetChrChipByIndex(0xF8, 22)
    Jump("loc_18AB")

    label("loc_18A3")

    SetChrChipByIndex(0xF8, 24)
    Jump("loc_18AB")

    label("loc_18AB")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_18CC"),
        (5, "loc_18D4"),
        (3, "loc_18DC"),
        (4, "loc_18E4"),
        (6, "loc_18EC"),
        (7, "loc_18F4"),
        (SWITCH_DEFAULT, "loc_18FC"),
    )


    label("loc_18CC")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_18FC")

    label("loc_18D4")

    SetChrChipByIndex(0xF9, 16)
    Jump("loc_18FC")

    label("loc_18DC")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_18FC")

    label("loc_18E4")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_18FC")

    label("loc_18EC")

    SetChrChipByIndex(0xF9, 22)
    Jump("loc_18FC")

    label("loc_18F4")

    SetChrChipByIndex(0xF9, 24)
    Jump("loc_18FC")

    label("loc_18FC")

    SetChrFlags(0x101, 0x1000)

    def lambda_1907():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1907)
    Sleep(50)
    SetChrFlags(0x109, 0x1000)

    def lambda_192C():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_192C)
    Sleep(50)
    SetChrFlags(0xF8, 0x1000)

    def lambda_1951():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1951)
    Sleep(50)
    SetChrFlags(0xF9, 0x1000)

    def lambda_1976():
        OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1976)
    Return()

    # Function_17_1850 end

    def Function_18_198C(): pass

    label("Function_18_198C")

    SetChrChipByIndex(0x8, 31)

    def lambda_1997():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1997)
    Sleep(50)
    SetChrChipByIndex(0x9, 1)

    def lambda_19BC():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_19BC)
    Sleep(50)
    SetChrChipByIndex(0xA, 1)

    def lambda_19E1():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_19E1)
    Return()

    # Function_18_198C end

    def Function_19_19F7(): pass

    label("Function_19_19F7")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -91180, 1200, 128710, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_1A34():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A34)
    OP_8F(0xFE, 0xFFFE9BD4, 0x0, 0x1F6C6, 0x7D0, 0x0)
    Return()

    # Function_19_19F7 end

    def Function_20_1A55(): pass

    label("Function_20_1A55")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -94460, 1200, 128720, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_1A92():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A92)
    OP_8F(0xFE, 0xFFFE8F04, 0x0, 0x1F6D0, 0x7D0, 0x0)
    Return()

    # Function_20_1A55 end

    def Function_21_1AB3(): pass

    label("Function_21_1AB3")

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
            "#1007F#5PEvery time I fight her, she seems to\x01",
            "kick my butt harder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        "#1060F#6PAll right, my turn.\x02",
    )

    CloseMessageWindow()

    def lambda_1C47():
        OP_6D(-93520, 20, 125240, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1C47)
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
        "#836F#4PErgh...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x8, 1)
    Sleep(1000)

    ChrTalk(    #34
        0x8,
        (
            "#835F#4PYou guys...\x02\x03",

            "You managed to get here, huh...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    OP_0D()

    def lambda_1DC4():
        OP_8F(0x109, 0xFFFE9396, 0x14, 0x1DFEC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DC4)

    ChrTalk(    #35
        0x101,
        "#1020F#5PCarna, are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#833F#4PAside from feeling like I was run over\x01",
            "by an airship...yeah, I'm okay.\x02\x03",

            "#832FMore importantly, did you find the others?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EF9")

    ChrTalk(    #37
        0x103,
        (
            "#020F#5PDon't worry, we freed Grant a moment ago.\x02\x03",

            "#025FWe still haven't found Anelace, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2014")

    label("loc_1EF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F93")

    ChrTalk(    #38
        0x106,
        (
            "#051F#5PDon't worry. We met Grant and had to give\x01",
            "him a once over, too, but he's fine.\x02\x03",

            "#053FFraid we haven't seen Anelace, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2014")

    label("loc_1F93")


    ChrTalk(    #39
        0x101,
        (
            "#1006F#5PWe beat the mind control out of\x01",
            "Grant just a bit ago.\x02\x03",

            "#1007FWe haven't seen Anelace, though.\x01",
            "I'm kinda worried...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2014")


    ChrTalk(    #40
        0x8,
        (
            "#833F#4PI see...\x02\x03",

            "#832FI'm guessing you also had a run in with\x01",
            "an Enforcer or three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1002F#5PNo, we've been hip deep in machines,\x01",
            "but no Enforcers.\x02\x03",

            "Aside from you guys, there doesn't seem\x01",
            "to be anyone here at all, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#834F#4PReally? That's strange...\x02\x03",

            "There were a few dozen research\x01",
            "staff and jaegers on guard here when\x01",
            "we infiltrated.\x02\x03",

            "#833FI guess it's possible they've abandoned\x01",
            "the base...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_221E")

    ChrTalk(    #43
        0x108,
        (
            "#074F#5PHmmmm.\x02\x03",

            "#070FWe shouldn't let our guard down,\x01",
            "but it does look that way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2287")

    label("loc_221E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2253")

    ChrTalk(    #44
        0x105,
        "#043F#5PIt is very possible...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2287")

    label("loc_2253")


    ChrTalk(    #45
        0x101,
        "#1015F#5PMaybe... That would be weird, though.\x02",
    )

    CloseMessageWindow()

    label("loc_2287")


    ChrTalk(    #46
        0x8,
        (
            "#835F#4PI should be able to make it out on my own.\x02\x03",

            "Please, find Anelace as soon as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1006F#5PLeave it to us!\x02",
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

    def lambda_233E():

        label("loc_233E")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_233E")

    QueueWorkItem2(0x101, 1, lambda_233E)

    def lambda_234F():

        label("loc_234F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_234F")

    QueueWorkItem2(0x109, 1, lambda_234F)

    def lambda_2360():

        label("loc_2360")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2360")

    QueueWorkItem2(0xF8, 1, lambda_2360)

    def lambda_2371():

        label("loc_2371")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2371")

    QueueWorkItem2(0xF9, 1, lambda_2371)

    def lambda_2382():
        OP_6D(-93050, 20, 118350, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2382)
    OP_8E(0x8, 0xFFFE9DF0, 0x14, 0x1E1D6, 0x7D0, 0x0)

    def lambda_23AE():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23AE)
    OP_8E(0x8, 0xFFFE9F58, 0x0, 0x1D48E, 0x9C4, 0x0)

    def lambda_23DC():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23DC)
    OP_8E(0x8, 0xFFFE9698, 0x0, 0x1C368, 0x7D0, 0x0)

    def lambda_240A():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_240A)
    OP_8E(0x8, 0xFFFE94C2, 0x0, 0x1BA6C, 0x9C4, 0x0)

    def lambda_2438():
        OP_8E(0xFE, 0xFFFE95B2, 0x0, 0x1B7D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2438)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)

    def lambda_2482():
        OP_6D(-93110, 20, 122720, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2482)
    WaitChrThread(0x101, 0x0)
    EventEnd(0x0)
    Return()

    # Function_21_1AB3 end

    def Function_22_249C(): pass

    label("Function_22_249C")

    EventBegin(0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x21, 0x0, 0x3)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #48
        (
            "\x07\x02#1S[Treatment of Combatants] Temporary combatants acquired\x01",
            "from jaeger corps and other sources\x01",
            "receive the following treatments:\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_74(0x21, 0x0, 0x4)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #49
        (
            "\x07\x02#1S1: Physical Enhancement Program 2: Combat Technique\x01",
            "Enhancement Program 3: Chain of Command Obedience Program\x01",
            "4: Protection of Secrecy Hypnosis Program (※FOLLOWING TEXT\x01",
            "REDACTED)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267B")
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #50
        "\x07\x00Received #1019i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FB, 1)
    Sleep(500)

    label("loc_267B")

    OP_A2(0x1C0C)
    OP_28(0x98, 0x1, 0x80)
    OP_74(0x21, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x1)
    Return()

    # Function_22_249C end

    def Function_23_269A(): pass

    label("Function_23_269A")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2716"),
        (1, "loc_271C"),
        (SWITCH_DEFAULT, "loc_2722"),
    )


    label("loc_2716")

    OP_A2(0x1200)
    Jump("loc_2722")

    label("loc_271C")

    OP_A2(0x1201)
    Jump("loc_2722")

    label("loc_2722")

    Return()

    # Function_23_269A end

    def Function_24_2723(): pass

    label("Function_24_2723")

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

    # Function_24_2723 end

    def Function_25_2780(): pass

    label("Function_25_2780")

    OP_A3(0x1C9A)
    OP_A2(0x1C9B)
    OP_A3(0x1C9C)
    OP_A3(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_25_2780 end

    def Function_26_2793(): pass

    label("Function_26_2793")

    OP_A3(0x1C9A)
    OP_A3(0x1C9B)
    OP_A2(0x1C9C)
    OP_A3(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_26_2793 end

    SaveToFile()

Try(main)
