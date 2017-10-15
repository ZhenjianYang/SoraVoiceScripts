from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Function_2_6F2",          # 02, 2
        "Function_3_708",          # 03, 3
        "Function_4_84A",          # 04, 4
        "Function_5_99B",          # 05, 5
        "Function_6_AF7",          # 06, 6
        "Function_7_C75",          # 07, 7
        "Function_8_DD1",          # 08, 8
        "Function_9_FD6",          # 09, 9
        "Function_10_1145",        # 0A, 10
        "Function_11_126D",        # 0B, 11
        "Function_12_13C1",        # 0C, 12
        "Function_13_14DF",        # 0D, 13
        "Function_14_163B",        # 0E, 14
        "Function_15_177B",        # 0F, 15
        "Function_16_18DC",        # 10, 16
        "Function_17_1A3F",        # 11, 17
        "Function_18_1B88",        # 12, 18
        "Function_19_1C88",        # 13, 19
        "Function_20_1D00",        # 14, 20
        "Function_21_1E00",        # 15, 21
        "Function_22_1E78",        # 16, 22
        "Function_23_1F78",        # 17, 23
        "Function_24_1FF0",        # 18, 24
        "Function_25_20F0",        # 19, 25
        "Function_26_2168",        # 1A, 26
        "Function_27_2247",        # 1B, 27
        "Function_28_2326",        # 1C, 28
        "Function_29_2374",        # 1D, 29
        "Function_30_23C2",        # 1E, 30
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

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 6)), scpexpr(EXPR_END)), "loc_61E")
    SetChrFlags(0x9, 0x80)

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 7)), scpexpr(EXPR_END)), "loc_62A")
    SetChrFlags(0xA, 0x80)

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 0)), scpexpr(EXPR_END)), "loc_636")
    SetChrFlags(0xB, 0x80)

    label("loc_636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 1)), scpexpr(EXPR_END)), "loc_642")
    SetChrFlags(0xC, 0x80)

    label("loc_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 2)), scpexpr(EXPR_END)), "loc_64E")
    SetChrFlags(0xD, 0x80)

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 3)), scpexpr(EXPR_END)), "loc_65A")
    SetChrFlags(0xE, 0x80)

    label("loc_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D9, 4)), scpexpr(EXPR_END)), "loc_666")
    SetChrFlags(0xF, 0x80)

    label("loc_666")

    OP_1B(0x0, 0x0, 0x13)
    OP_1B(0x1, 0x0, 0x15)
    OP_1B(0x2, 0x0, 0x17)
    OP_1B(0x3, 0x0, 0x19)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E5")
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, 1100, -6000, -114690, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_71(0x11, 0x20)
    OP_6F(0x11, 0)
    OP_70(0x11, 0xFA)
    Jump("loc_6F1")

    label("loc_6E5")

    OP_72(0x11, 0x20)
    OP_6F(0x11, 250)

    label("loc_6F1")

    Return()

    # Function_1_473 end

    def Function_2_6F2(): pass

    label("Function_2_6F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_707")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6F2")

    label("loc_707")

    Return()

    # Function_2_6F2 end

    def Function_3_708(): pass

    label("Function_3_708")

    OP_EA(0x2, 0xE9, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x164, 1)"), scpexpr(EXPR_END)), "loc_779")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x64\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F50)
    Jump("loc_7DD")

    label("loc_779")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x64\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x64\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_7DD")

    Jump("loc_83C")

    label("loc_7E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05I wish you a wonderful day full of treasure chest\x01",
            "plundering.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_83C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_708 end

    def Function_4_84A(): pass

    label("Function_4_84A")

    OP_EA(0x2, 0xEA, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_922")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_8BB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F52)
    Jump("loc_91F")

    label("loc_8BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_91F")

    Jump("loc_98D")

    label("loc_922")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05You took a gamble on something being in this\x01",
            "chest, and I'm afraid you lost.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_98D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_84A end

    def Function_5_99B(): pass

    label("Function_5_99B")

    OP_EA(0x2, 0xEB, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A73")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17D, 1)"), scpexpr(EXPR_END)), "loc_A0C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\x7D\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F53)
    Jump("loc_A70")

    label("loc_A0C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\x7D\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x7D\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_A70")

    Jump("loc_AE9")

    label("loc_A73")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05If you want something else, you're going to have\x01",
            "to sign this legally-binding contract.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AE9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_99B end

    def Function_6_AF7(): pass

    label("Function_6_AF7")

    OP_EA(0x2, 0xEC, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_B68")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F55)
    Jump("loc_BCC")

    label("loc_B68")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_BCC")

    Jump("loc_C67")

    label("loc_BCF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05I don't think there's an “open every chest in\x01",
            "the game” trophy, but even if there were,\x01",
            "you've already opened this one.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C67")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_AF7 end

    def Function_7_C75(): pass

    label("Function_7_C75")

    OP_EA(0x2, 0xED, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_CE6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F56)
    Jump("loc_D4A")

    label("loc_CE6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_D4A")

    Jump("loc_DC3")

    label("loc_D4D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05You tell the chest to 'say aaah,' and it obliges.\x01",
            "Everything seems to be in order here!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DC3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_C75 end

    def Function_8_DD1(): pass

    label("Function_8_DD1")

    OP_EA(0x2, 0xEE, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBB")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_E28():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E28)

    def lambda_E43():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E43)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #15
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x418, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_E96"),
        (2, "loc_EA8"),
        (1, "loc_EB8"),
        (SWITCH_DEFAULT, "loc_EBB"),
    )


    label("loc_E96")

    OP_A2(0x1F58)
    OP_6F(0x6, 60)
    Sleep(500)
    Jump("loc_EBB")

    label("loc_EA8")

    OP_6F(0x6, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_EB8")

    OP_B4(0x0)
    Return()

    label("loc_EBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x154, 1)"), scpexpr(EXPR_END)), "loc_F07")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        "Found \x1F\x54\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F57)
    Jump("loc_F69")

    label("loc_F07")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #17
        (
            "Found \x1F\x54\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x54\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_F69")

    Jump("loc_FC8")

    label("loc_F6C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #18
        (
            "\x07\x05You've already looted this chest right down to\x01",
            "the bare bottom.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FC8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_DD1 end

    def Function_9_FD6(): pass

    label("Function_9_FD6")

    OP_EA(0x2, 0xEF, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_1047")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F59)
    Jump("loc_10AB")

    label("loc_1047")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_10AB")

    Jump("loc_1137")

    label("loc_10AE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05This chest's proud possessions have already\x01",
            "passed to some wandering adventurer's\x01",
            "satchel. Probably yours.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1137")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_FD6 end

    def Function_10_1145(): pass

    label("Function_10_1145")

    OP_EA(0x2, 0xF0, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_11B6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "Found \x1F\x05\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5A)
    Jump("loc_121A")

    label("loc_11B6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "Found \x1F\x05\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x05\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_121A")

    Jump("loc_125F")

    label("loc_121D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05 The empty chest's stomach gurgles.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_125F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1145 end

    def Function_11_126D(): pass

    label("Function_11_126D")

    OP_EA(0x2, 0xF1, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1345")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_12DE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5B)
    Jump("loc_1342")

    label("loc_12DE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_1342")

    Jump("loc_13B3")

    label("loc_1345")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "\x07\x05Watch out! This chest has nothing to lose!\x01",
            "There's no telling what it might do!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_13B3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_126D end

    def Function_12_13C1(): pass

    label("Function_12_13C1")

    OP_EA(0x2, 0xF2, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1499")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29D, 1)"), scpexpr(EXPR_END)), "loc_1432")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        "Found \x1F\x9D\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5C)
    Jump("loc_1496")

    label("loc_1432")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "Found \x1F\x9D\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x9D\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_1496")

    Jump("loc_14D1")

    label("loc_1499")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05Not exactly shy, are you?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_14D1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_13C1 end

    def Function_13_14DF(): pass

    label("Function_13_14DF")

    OP_EA(0x2, 0xF3, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_1550")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5E)
    Jump("loc_15B4")

    label("loc_1550")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_15B4")

    Jump("loc_162D")

    label("loc_15B7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x07\x05You briefly wonder how many jelly beans you\x01",
            "could fit in a treasure chest of this size.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_162D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_14DF end

    def Function_14_163B(): pass

    label("Function_14_163B")

    OP_EA(0x2, 0xF4, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1713")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_16AC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F5F)
    Jump("loc_1710")

    label("loc_16AC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_1710")

    Jump("loc_176D")

    label("loc_1713")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x07\x05I'm not so sure you understand the definition of\x01",
            "'empty'...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_176D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_163B end

    def Function_15_177B(): pass

    label("Function_15_177B")

    OP_EA(0x2, 0xF5, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1853")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D7, 1)"), scpexpr(EXPR_END)), "loc_17EC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "Found \x1F\xD7\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F60)
    Jump("loc_1850")

    label("loc_17EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "Found \x1F\xD7\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xD7\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_1850")

    Jump("loc_18CE")

    label("loc_1853")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x07\x05Look, I know I don't have anything, but we can\x01",
            "still hang out, right? Wait, come baaaaaaack!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_18CE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_177B end

    def Function_16_18DC(): pass

    label("Function_16_18DC")

    OP_EA(0x2, 0xF6, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_194D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F62)
    Jump("loc_19B1")

    label("loc_194D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #41
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_19B1")

    Jump("loc_1A31")

    label("loc_19B4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "\x07\x05Well, hello! Welcome to Treasure Chest Village.\x01",
            "You sure are a funny looking treasure chest...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1A31")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_18DC end

    def Function_17_1A3F(): pass

    label("Function_17_1A3F")

    OP_EA(0x2, 0xF7, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3EC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B17")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x145, 1)"), scpexpr(EXPR_END)), "loc_1AB0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #43
        "Found \x1F\x45\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F63)
    Jump("loc_1B14")

    label("loc_1AB0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "Found \x1F\x45\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x45\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_1B14")

    Jump("loc_1B7A")

    label("loc_1B17")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #45
        (
            "\x07\x05If this chest could talk, it would say, 'You took my\x01",
            "stuff already.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1B7A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_17_1A3F end

    def Function_18_1B88(): pass

    label("Function_18_1B88")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_18_1B88 end

    def Function_19_1C88(): pass

    label("Function_19_1C88")

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

    # Function_19_1C88 end

    def Function_20_1D00(): pass

    label("Function_20_1D00")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_20_1D00 end

    def Function_21_1E00(): pass

    label("Function_21_1E00")

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

    # Function_21_1E00 end

    def Function_22_1E78(): pass

    label("Function_22_1E78")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_22_1E78 end

    def Function_23_1F78(): pass

    label("Function_23_1F78")

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

    # Function_23_1F78 end

    def Function_24_1FF0(): pass

    label("Function_24_1FF0")

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
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_24_1FF0 end

    def Function_25_20F0(): pass

    label("Function_25_20F0")

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

    # Function_25_20F0 end

    def Function_26_2168(): pass

    label("Function_26_2168")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_26_2168 end

    def Function_27_2247(): pass

    label("Function_27_2247")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_27_2247 end

    def Function_28_2326(): pass

    label("Function_28_2326")


    def lambda_232C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_232C)

    def lambda_233E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_233E)

    def lambda_2350():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2350)

    def lambda_2362():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2362)
    Sleep(2500)
    Return()

    # Function_28_2326 end

    def Function_29_2374(): pass

    label("Function_29_2374")


    def lambda_237A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_237A)

    def lambda_238C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_238C)

    def lambda_239E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_239E)

    def lambda_23B0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_23B0)
    Sleep(2000)
    Return()

    # Function_29_2374 end

    def Function_30_23C2(): pass

    label("Function_30_23C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2428")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_25CA")

    label("loc_2428")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #47
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25AF")
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

    label("loc_25AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C9")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_25C9")

    Return()

    label("loc_25CA")

    Return()

    # Function_30_23C2 end

    SaveToFile()

Try(main)
