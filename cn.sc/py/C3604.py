from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3604   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3604.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12660 ._CH',             # 00
        'ED6_DT29/CH12661 ._CH',             # 01
        'ED6_DT29/CH12670 ._CH',             # 02
        'ED6_DT29/CH12671 ._CH',             # 03
        'ED6_DT29/CH12680 ._CH',             # 04
        'ED6_DT29/CH12681 ._CH',             # 05
        'ED6_DT29/CH12690 ._CH',             # 06
        'ED6_DT29/CH12691 ._CH',             # 07
        'ED6_DT29/CH12700 ._CH',             # 08
        'ED6_DT29/CH12701 ._CH',             # 09
        'ED6_DT29/CH12710 ._CH',             # 0A
        'ED6_DT29/CH12711 ._CH',             # 0B
        'ED6_DT29/CH12720 ._CH',             # 0C
        'ED6_DT29/CH12721 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12660P._CP',             # 00
        'ED6_DT29/CH12661P._CP',             # 01
        'ED6_DT29/CH12670P._CP',             # 02
        'ED6_DT29/CH12671P._CP',             # 03
        'ED6_DT29/CH12680P._CP',             # 04
        'ED6_DT29/CH12681P._CP',             # 05
        'ED6_DT29/CH12690P._CP',             # 06
        'ED6_DT29/CH12691P._CP',             # 07
        'ED6_DT29/CH12700P._CP',             # 08
        'ED6_DT29/CH12701P._CP',             # 09
        'ED6_DT29/CH12710P._CP',             # 0A
        'ED6_DT29/CH12711P._CP',             # 0B
        'ED6_DT29/CH12720P._CP',             # 0C
        'ED6_DT29/CH12721P._CP',             # 0D
    )

    DeclNpc(
        X                   = 10040,
        Z                   = -2600,
        Y                   = 11460,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -30540,
        Z                   = -50,
        Y                   = 17720,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7878,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34650,
        Z                   = 200,
        Y                   = -14550,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7879,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28640,
        Z                   = -50,
        Y                   = -21610,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7880,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 30780,
        Z                   = -7650,
        Y                   = -48870,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7881,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32320,
        Z                   = -7450,
        Y                   = -57600,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x411,
        Unknown_18          = 7882,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10,
        Z                   = -4050,
        Y                   = -70900,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7883,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30670,
        Z                   = -4050,
        Y                   = -53210,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7884,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 30780,
        TriggerZ            = 400,
        TriggerY            = 4440,
        TriggerRange        = 1000,
        ActorX              = 30780,
        ActorZ              = 400,
        ActorY              = 3740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18710,
        TriggerZ            = 400,
        TriggerY            = 11470,
        TriggerRange        = 1000,
        ActorX              = 18050,
        ActorZ              = 400,
        ActorY              = 11470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10,
        TriggerZ            = -7200,
        TriggerY            = -53840,
        TriggerRange        = 1000,
        ActorX              = 10,
        ActorZ              = -7200,
        ActorY              = -54500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11340,
        TriggerZ            = -7200,
        TriggerY            = -42070,
        TriggerRange        = 1000,
        ActorX              = 11870,
        ActorZ              = -7200,
        ActorY              = -42410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18680,
        TriggerZ            = -7200,
        TriggerY            = -11480,
        TriggerRange        = 1000,
        ActorX              = -18020,
        ActorZ              = -7200,
        ActorY              = -11480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9290,
        TriggerZ            = -3600,
        TriggerY            = 11460,
        TriggerRange        = 1000,
        ActorX              = 10040,
        ActorZ              = -3600,
        ActorY              = 11460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30750,
        TriggerZ            = 400,
        TriggerY            = -7010,
        TriggerRange        = 1000,
        ActorX              = -30750,
        ActorZ              = 400,
        ActorY              = -7710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17870,
        TriggerZ            = 4400,
        TriggerY            = 25200,
        TriggerRange        = 1000,
        ActorX              = 18400,
        ActorZ              = 4400,
        ActorY              = 24860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30790,
        TriggerZ            = 400,
        TriggerY            = -4460,
        TriggerRange        = 1000,
        ActorX              = 30790,
        ActorZ              = 400,
        ActorY              = -3800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13590,
        TriggerZ            = -3600,
        TriggerY            = -27580,
        TriggerRange        = 1000,
        ActorX              = 13030,
        ActorZ              = -3600,
        ActorY              = -27960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30,
        TriggerZ            = -3600,
        TriggerY            = -94270,
        TriggerRange        = 1000,
        ActorX              = 30,
        ActorZ              = -3600,
        ActorY              = -94970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17700,
        TriggerZ            = -7200,
        TriggerY            = -45730,
        TriggerRange        = 1000,
        ActorX              = 17120,
        ActorZ              = -7200,
        ActorY              = -45370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13700,
        TriggerZ            = -10800,
        TriggerY            = -95360,
        TriggerRange        = 1000,
        ActorX              = 13320,
        ActorZ              = -10800,
        ActorY              = -95950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14260,
        TriggerZ            = -3600,
        TriggerY            = -43720,
        TriggerRange        = 1000,
        ActorX              = -13650,
        ActorZ              = -3600,
        ActorY              = -43350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30720,
        TriggerZ            = -3600,
        TriggerY            = -33900,
        TriggerRange        = 1000,
        ActorX              = -30720,
        ActorZ              = -3600,
        ActorY              = -33240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1100,
        TriggerZ            = -7200,
        TriggerY            = -114690,
        TriggerRange        = 1200,
        ActorX              = 1100,
        ActorZ              = -6000,
        ActorY              = -114690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_43E",          # 00, 0
        "Function_1_473",          # 01, 1
        "Function_2_6CA",          # 02, 2
        "Function_3_6E0",          # 03, 3
        "Function_4_7F7",          # 04, 4
        "Function_5_90E",          # 05, 5
        "Function_6_A25",          # 06, 6
        "Function_7_B3C",          # 07, 7
        "Function_8_C53",          # 08, 8
        "Function_9_E23",          # 09, 9
        "Function_10_F3A",         # 0A, 10
        "Function_11_1051",        # 0B, 11
        "Function_12_1168",        # 0C, 12
        "Function_13_127F",        # 0D, 13
        "Function_14_1396",        # 0E, 14
        "Function_15_14AD",        # 0F, 15
        "Function_16_15C4",        # 10, 16
        "Function_17_16DB",        # 11, 17
        "Function_18_17F2",        # 12, 18
        "Function_19_18ED",        # 13, 19
        "Function_20_1965",        # 14, 20
        "Function_21_1A60",        # 15, 21
        "Function_22_1AD8",        # 16, 22
        "Function_23_1BD3",        # 17, 23
        "Function_24_1C4B",        # 18, 24
        "Function_25_1D46",        # 19, 25
        "Function_26_1DBE",        # 1A, 26
        "Function_27_1EB1",        # 1B, 27
        "Function_28_1FA4",        # 1C, 28
        "Function_29_1FF2",        # 1D, 29
        "Function_30_2040",        # 1E, 30
    )


    def Function_0_43E(): pass

    label("Function_0_43E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_456"),
        (101, "loc_45D"),
        (102, "loc_464"),
        (103, "loc_46B"),
        (SWITCH_DEFAULT, "loc_472"),
    )


    label("loc_456")

    Event(0, 18)
    Jump("loc_472")

    label("loc_45D")

    Event(0, 20)
    Jump("loc_472")

    label("loc_464")

    Event(0, 22)
    Jump("loc_472")

    label("loc_46B")

    Event(0, 24)
    Jump("loc_472")

    label("loc_472")

    Return()

    # Function_0_43E end

    def Function_1_473(): pass

    label("Function_1_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_485")
    OP_6F(0x1, 0)
    Jump("loc_48C")

    label("loc_485")

    OP_6F(0x1, 60)

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E")
    OP_6F(0x2, 0)
    Jump("loc_4A5")

    label("loc_49E")

    OP_6F(0x2, 60)

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7")
    OP_6F(0x3, 0)
    Jump("loc_4BE")

    label("loc_4B7")

    OP_6F(0x3, 60)

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D0")
    OP_6F(0x4, 0)
    Jump("loc_4D7")

    label("loc_4D0")

    OP_6F(0x4, 60)

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E9")
    OP_6F(0x5, 0)
    Jump("loc_4F0")

    label("loc_4E9")

    OP_6F(0x5, 60)

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_502")
    OP_6F(0x6, 0)
    Jump("loc_509")

    label("loc_502")

    OP_6F(0x6, 60)

    label("loc_509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51B")
    OP_6F(0x7, 0)
    Jump("loc_522")

    label("loc_51B")

    OP_6F(0x7, 60)

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_534")
    OP_6F(0x8, 0)
    Jump("loc_53B")

    label("loc_534")

    OP_6F(0x8, 60)

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54D")
    OP_6F(0x9, 0)
    Jump("loc_554")

    label("loc_54D")

    OP_6F(0x9, 60)

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_566")
    OP_6F(0xA, 0)
    Jump("loc_56D")

    label("loc_566")

    OP_6F(0xA, 60)

    label("loc_56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F")
    OP_6F(0xB, 0)
    Jump("loc_586")

    label("loc_57F")

    OP_6F(0xB, 60)

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_598")
    OP_6F(0xC, 0)
    Jump("loc_59F")

    label("loc_598")

    OP_6F(0xC, 60)

    label("loc_59F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1")
    OP_6F(0xD, 0)
    Jump("loc_5B8")

    label("loc_5B1")

    OP_6F(0xD, 60)

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CA")
    OP_6F(0xE, 0)
    Jump("loc_5D1")

    label("loc_5CA")

    OP_6F(0xE, 60)

    label("loc_5D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E3")
    OP_6F(0xF, 0)
    Jump("loc_5EA")

    label("loc_5E3")

    OP_6F(0xF, 60)

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 6)), scpexpr(EXPR_END)), "loc_5F6")
    SetChrFlags(0x9, 0x80)

    label("loc_5F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 7)), scpexpr(EXPR_END)), "loc_602")
    SetChrFlags(0xA, 0x80)

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 0)), scpexpr(EXPR_END)), "loc_60E")
    SetChrFlags(0xB, 0x80)

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 1)), scpexpr(EXPR_END)), "loc_61A")
    SetChrFlags(0xC, 0x80)

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 2)), scpexpr(EXPR_END)), "loc_626")
    SetChrFlags(0xD, 0x80)

    label("loc_626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 3)), scpexpr(EXPR_END)), "loc_632")
    SetChrFlags(0xE, 0x80)

    label("loc_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 4)), scpexpr(EXPR_END)), "loc_63E")
    SetChrFlags(0xF, 0x80)

    label("loc_63E")

    OP_1B(0x0, 0x0, 0x13)
    OP_1B(0x1, 0x0, 0x15)
    OP_1B(0x2, 0x0, 0x17)
    OP_1B(0x3, 0x0, 0x19)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BD")
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, 1100, -6000, -114690, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_71(0x11, 0x20)
    OP_6F(0x11, 0)
    OP_70(0x11, 0xFA)
    Jump("loc_6C9")

    label("loc_6BD")

    OP_72(0x11, 0x20)
    OP_6F(0x11, 250)

    label("loc_6C9")

    Return()

    # Function_1_473 end

    def Function_2_6CA(): pass

    label("Function_2_6CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6CA")

    label("loc_6DF")

    Return()

    # Function_2_6CA end

    def Function_3_6E0(): pass

    label("Function_3_6E0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x164, 1)"), scpexpr(EXPR_END)), "loc_74F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x64\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F50)
    Jump("loc_7B5")

    label("loc_74F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x64\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x64\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_7B5")

    Jump("loc_7E9")

    label("loc_7B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7E9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_6E0 end

    def Function_4_7F7(): pass

    label("Function_4_7F7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_866")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F52)
    Jump("loc_8CC")

    label("loc_866")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_8CC")

    Jump("loc_900")

    label("loc_8CF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_900")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_7F7 end

    def Function_5_90E(): pass

    label("Function_5_90E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17D, 1)"), scpexpr(EXPR_END)), "loc_97D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x7D\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F53)
    Jump("loc_9E3")

    label("loc_97D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x7D\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x7D\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_9E3")

    Jump("loc_A17")

    label("loc_9E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A17")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_90E end

    def Function_6_A25(): pass

    label("Function_6_A25")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_A94")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F55)
    Jump("loc_AFA")

    label("loc_A94")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_AFA")

    Jump("loc_B2E")

    label("loc_AFD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B2E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A25 end

    def Function_7_B3C(): pass

    label("Function_7_B3C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C14")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_BAB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F56)
    Jump("loc_C11")

    label("loc_BAB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_C11")

    Jump("loc_C45")

    label("loc_C14")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C45")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B3C end

    def Function_8_C53(): pass

    label("Function_8_C53")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D32")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_CA5():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CA5)

    def lambda_CC0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CC0)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #15
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x418, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D0D"),
        (2, "loc_D1F"),
        (1, "loc_D2F"),
        (SWITCH_DEFAULT, "loc_D32"),
    )


    label("loc_D0D")

    OP_A2(0x1F58)
    OP_6F(0x6, 60)
    Sleep(500)
    Jump("loc_D32")

    label("loc_D1F")

    OP_6F(0x6, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_D2F")

    OP_B4(0x0)
    Return()

    label("loc_D32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x154, 1)"), scpexpr(EXPR_END)), "loc_D81")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\x54\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F57)
    Jump("loc_DE3")

    label("loc_D81")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\x54\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x54\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_DE3")

    Jump("loc_E15")

    label("loc_DE6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E15")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C53 end

    def Function_9_E23(): pass

    label("Function_9_E23")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_E92")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F59)
    Jump("loc_EF8")

    label("loc_E92")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_EF8")

    Jump("loc_F2C")

    label("loc_EFB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F2C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_E23 end

    def Function_10_F3A(): pass

    label("Function_10_F3A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1012")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_FA9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5A)
    Jump("loc_100F")

    label("loc_FA9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x05\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_100F")

    Jump("loc_1043")

    label("loc_1012")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1043")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_F3A end

    def Function_11_1051(): pass

    label("Function_11_1051")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1129")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_10C0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5B)
    Jump("loc_1126")

    label("loc_10C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_1126")

    Jump("loc_115A")

    label("loc_1129")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_115A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1051 end

    def Function_12_1168(): pass

    label("Function_12_1168")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1240")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29D, 1)"), scpexpr(EXPR_END)), "loc_11D7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x00得到了\x1F\x9D\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5C)
    Jump("loc_123D")

    label("loc_11D7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "宝箱里装有\x1F\x9D\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x9D\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_123D")

    Jump("loc_1271")

    label("loc_1240")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1271")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1168 end

    def Function_13_127F(): pass

    label("Function_13_127F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1357")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_12EE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5E)
    Jump("loc_1354")

    label("loc_12EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_1354")

    Jump("loc_1388")

    label("loc_1357")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1388")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_127F end

    def Function_14_1396(): pass

    label("Function_14_1396")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_1405")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5F)
    Jump("loc_146B")

    label("loc_1405")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_146B")

    Jump("loc_149F")

    label("loc_146E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_149F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1396 end

    def Function_15_14AD(): pass

    label("Function_15_14AD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1585")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D7, 1)"), scpexpr(EXPR_END)), "loc_151C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x00得到了\x1F\xD7\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F60)
    Jump("loc_1582")

    label("loc_151C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "宝箱里装有\x1F\xD7\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xD7\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_1582")

    Jump("loc_15B6")

    label("loc_1585")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_15B6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_14AD end

    def Function_16_15C4(): pass

    label("Function_16_15C4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_1633")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F62)
    Jump("loc_1699")

    label("loc_1633")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #41
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_1699")

    Jump("loc_16CD")

    label("loc_169C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_16CD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_15C4 end

    def Function_17_16DB(): pass

    label("Function_17_16DB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x145, 1)"), scpexpr(EXPR_END)), "loc_174A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #43
        "\x07\x00得到了\x1F\x45\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F63)
    Jump("loc_17B0")

    label("loc_174A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "宝箱里装有\x1F\x45\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x45\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_17B0")

    Jump("loc_17E4")

    label("loc_17B3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_17E4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_17_16DB end

    def Function_18_17F2(): pass

    label("Function_18_17F2")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 4190, 36000, 0)
    SetChrPos(0x101, 500, 4190, 35500, 180)
    SetChrPos(0x102, -500, 4190, 35500, 180)
    SetChrPos(0xF8, 500, 4190, 36500, 180)
    SetChrPos(0xF9, -500, 4190, 36500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 26)
    Call(0, 28)
    Fade(500)
    OP_6D(90, 4190, 34080, 0)
    SetChrPos(0x0, 90, 4190, 34080, 180)
    SetChrPos(0x1, 90, 4190, 34080, 180)
    SetChrPos(0x2, 90, 4190, 34080, 180)
    SetChrPos(0x3, 90, 4190, 34080, 180)
    EventEnd(0x0)
    Return()

    # Function_18_17F2 end

    def Function_19_18ED(): pass

    label("Function_19_18ED")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 4190, 36000, 0)
    SetChrPos(0x101, -500, 4190, 36500, 0)
    SetChrPos(0x102, 500, 4190, 36500, 0)
    SetChrPos(0xF8, -500, 4190, 35500, 0)
    SetChrPos(0xF9, 500, 4190, 35500, 0)
    OP_0D()
    Call(0, 26)
    Call(0, 29)
    NewScene("ED6_DT21/C3603   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_19_18ED end

    def Function_20_1965(): pass

    label("Function_20_1965")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(30800, 190, 18500, 0)
    SetChrPos(0x101, 31300, 190, 18000, 180)
    SetChrPos(0x102, 30300, 190, 18000, 180)
    SetChrPos(0xF8, 31300, 190, 19000, 180)
    SetChrPos(0xF9, 30300, 190, 19000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 26)
    Call(0, 28)
    Fade(500)
    OP_6D(30800, 190, 16219, 0)
    SetChrPos(0x0, 30800, 190, 16219, 180)
    SetChrPos(0x1, 30800, 190, 16219, 180)
    SetChrPos(0x2, 30800, 190, 16219, 180)
    SetChrPos(0x3, 30800, 190, 16219, 180)
    EventEnd(0x0)
    Return()

    # Function_20_1965 end

    def Function_21_1A60(): pass

    label("Function_21_1A60")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(30800, 190, 18500, 0)
    SetChrPos(0x101, 30300, 190, 19000, 0)
    SetChrPos(0x102, 31300, 190, 19000, 0)
    SetChrPos(0xF8, 30300, 190, 18000, 0)
    SetChrPos(0xF9, 31300, 190, 18000, 0)
    OP_0D()
    Call(0, 26)
    Call(0, 29)
    NewScene("ED6_DT21/C3603   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_21_1A60 end

    def Function_22_1AD8(): pass

    label("Function_22_1AD8")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-30800, -7410, -17000, 0)
    SetChrPos(0x101, -30300, -7410, -17500, 180)
    SetChrPos(0x102, -31300, -7410, -17500, 180)
    SetChrPos(0xF8, -30300, -7410, -16500, 180)
    SetChrPos(0xF9, -31300, -7410, -16500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 26)
    Call(0, 28)
    Fade(500)
    OP_6D(-30660, -7410, -19230, 0)
    SetChrPos(0x0, -30660, -7410, -19230, 180)
    SetChrPos(0x1, -30660, -7410, -19230, 180)
    SetChrPos(0x2, -30660, -7410, -19230, 180)
    SetChrPos(0x3, -30660, -7410, -19230, 180)
    EventEnd(0x0)
    Return()

    # Function_22_1AD8 end

    def Function_23_1BD3(): pass

    label("Function_23_1BD3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-30800, -7410, -17000, 0)
    SetChrPos(0x101, -31300, -7410, -16500, 0)
    SetChrPos(0x102, -30300, -7410, -16500, 0)
    SetChrPos(0xF8, -31300, -7410, -17500, 0)
    SetChrPos(0xF9, -30300, -7410, -17500, 0)
    OP_0D()
    Call(0, 26)
    Call(0, 29)
    NewScene("ED6_DT21/C3603   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_23_1BD3 end

    def Function_24_1C4B(): pass

    label("Function_24_1C4B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, -6530, -106500, 0)
    SetChrPos(0x101, 500, -6530, -107000, 180)
    SetChrPos(0x102, -500, -6530, -107000, 180)
    SetChrPos(0xF8, 500, -6530, -106000, 180)
    SetChrPos(0xF9, -500, -6530, -106000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 27)
    Call(0, 28)
    Fade(500)
    OP_6D(-20, -6880, -108860, 0)
    SetChrPos(0x0, -20, -6880, -108860, 180)
    SetChrPos(0x1, -20, -6880, -108860, 180)
    SetChrPos(0x2, -20, -6880, -108860, 180)
    SetChrPos(0x3, -20, -6880, -108860, 180)
    EventEnd(0x0)
    Return()

    # Function_24_1C4B end

    def Function_25_1D46(): pass

    label("Function_25_1D46")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, -6530, -106500, 0)
    SetChrPos(0x101, -500, -6530, -106000, 0)
    SetChrPos(0x102, 500, -6530, -106000, 0)
    SetChrPos(0xF8, -500, -6530, -107000, 0)
    SetChrPos(0xF9, 500, -6530, -107000, 0)
    OP_0D()
    Call(0, 27)
    Call(0, 29)
    NewScene("ED6_DT21/C3605   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_1D46 end

    def Function_26_1DBE(): pass

    label("Function_26_1DBE")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_26_1DBE end

    def Function_27_1EB1(): pass

    label("Function_27_1EB1")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_27_1EB1 end

    def Function_28_1FA4(): pass

    label("Function_28_1FA4")


    def lambda_1FAA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1FAA)

    def lambda_1FBC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1FBC)

    def lambda_1FCE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1FCE)

    def lambda_1FE0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1FE0)
    Sleep(2500)
    Return()

    # Function_28_1FA4 end

    def Function_29_1FF2(): pass

    label("Function_29_1FF2")


    def lambda_1FF8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1FF8)

    def lambda_200A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_200A)

    def lambda_201C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_201C)

    def lambda_202E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_202E)
    Sleep(2000)
    Return()

    # Function_29_1FF2 end

    def Function_30_2040(): pass

    label("Function_30_2040")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2093")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05好像是导力停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_2238")

    label("loc_2093")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #47
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221D")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x11, 0x20)
    OP_6F(0x11, 300)
    OP_70(0x11, 0x1F4)
    OP_73(0x11)
    OP_6F(0x11, 500)
    OP_70(0x11, 0x2BC)
    OP_71(0x11, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x3, "map\\\\mp027_01.eff")
    PlayEffect(0x3, 0x3, 0xFF, 1100, -6000, -114690, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x3, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, 1100, -6000, -114690, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_70(0x11, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_221D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2237")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2237")

    Return()

    label("loc_2238")

    Return()

    # Function_30_2040 end

    SaveToFile()

Try(main)
