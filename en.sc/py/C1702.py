from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1702   ._SN',
        MapName             = 'Bose',
        Location            = 'C1702.x',
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
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
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
        'ED6_DT29/CH12800 ._CH',             # 00
        'ED6_DT29/CH12801 ._CH',             # 01
        'ED6_DT29/CH12810 ._CH',             # 02
        'ED6_DT29/CH12811 ._CH',             # 03
        'ED6_DT29/CH12820 ._CH',             # 04
        'ED6_DT29/CH12821 ._CH',             # 05
        'ED6_DT29/CH12830 ._CH',             # 06
        'ED6_DT29/CH12831 ._CH',             # 07
        'ED6_DT29/CH12840 ._CH',             # 08
        'ED6_DT29/CH12841 ._CH',             # 09
        'ED6_DT29/CH12850 ._CH',             # 0A
        'ED6_DT29/CH12851 ._CH',             # 0B
        'ED6_DT29/CH12860 ._CH',             # 0C
        'ED6_DT29/CH12861 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12800P._CP',             # 00
        'ED6_DT29/CH12801P._CP',             # 01
        'ED6_DT29/CH12810P._CP',             # 02
        'ED6_DT29/CH12811P._CP',             # 03
        'ED6_DT29/CH12820P._CP',             # 04
        'ED6_DT29/CH12821P._CP',             # 05
        'ED6_DT29/CH12830P._CP',             # 06
        'ED6_DT29/CH12831P._CP',             # 07
        'ED6_DT29/CH12840P._CP',             # 08
        'ED6_DT29/CH12841P._CP',             # 09
        'ED6_DT29/CH12850P._CP',             # 0A
        'ED6_DT29/CH12851P._CP',             # 0B
        'ED6_DT29/CH12860P._CP',             # 0C
        'ED6_DT29/CH12861P._CP',             # 0D
    )

    DeclMonster(
        X                   = -6530,
        Z                   = 400,
        Y                   = -39740,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 8187,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5460,
        Z                   = 400,
        Y                   = -40310,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 8188,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -60,
        Z                   = 400,
        Y                   = -1320,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F7,
        Unknown_18          = 8189,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6310,
        Z                   = 400,
        Y                   = 40240,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 8190,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5540,
        Z                   = 400,
        Y                   = 39770,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 8191,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -66580,
        Z                   = 400,
        Y                   = 75070,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 7808,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -74870,
        Z                   = 400,
        Y                   = 66550,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7809,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -76050,
        Z                   = 400,
        Y                   = -67860,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7810,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -67900,
        Z                   = 400,
        Y                   = -75980,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F6,
        Unknown_18          = 7811,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 67970,
        Z                   = 400,
        Y                   = -75600,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F4,
        Unknown_18          = 7812,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 75900,
        Z                   = 400,
        Y                   = -67970,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F7,
        Unknown_18          = 7813,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 66360,
        Z                   = 400,
        Y                   = 74560,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F5,
        Unknown_18          = 7814,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 74650,
        Z                   = 400,
        Y                   = 66690,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F8,
        Unknown_18          = 7815,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 30,
        TriggerZ            = -50,
        TriggerY            = 39240,
        TriggerRange        = 1000,
        ActorX              = 30,
        ActorZ              = -50,
        ActorY              = 39940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 80,
        TriggerZ            = -50,
        TriggerY            = -40760,
        TriggerRange        = 1000,
        ActorX              = 80,
        ActorZ              = -50,
        ActorY              = -40050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -71270,
        TriggerZ            = 0,
        TriggerY            = 71150,
        TriggerRange        = 1000,
        ActorX              = -70740,
        ActorZ              = 0,
        ActorY              = 70800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -71480,
        TriggerZ            = 0,
        TriggerY            = -71470,
        TriggerRange        = 1000,
        ActorX              = -71860,
        ActorZ              = 0,
        ActorY              = -72030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71530,
        TriggerZ            = 0,
        TriggerY            = -71540,
        TriggerRange        = 1000,
        ActorX              = 71990,
        ActorZ              = 0,
        ActorY              = -72000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71140,
        TriggerZ            = 0,
        TriggerY            = 71150,
        TriggerRange        = 1000,
        ActorX              = 70730,
        ActorZ              = 0,
        ActorY              = 70630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_35E",          # 00, 0
        "Function_1_3D5",          # 01, 1
        "Function_2_562",          # 02, 2
        "Function_3_699",          # 03, 3
        "Function_4_7DA",          # 04, 4
        "Function_5_938",          # 05, 5
        "Function_6_ACE",          # 06, 6
        "Function_7_C00",          # 07, 7
        "Function_8_D8D",          # 08, 8
        "Function_9_E9F",          # 09, 9
        "Function_10_F20",         # 0A, 10
        "Function_11_1032",        # 0B, 11
        "Function_12_10B3",        # 0C, 12
        "Function_13_11C5",        # 0D, 13
        "Function_14_1246",        # 0E, 14
        "Function_15_1346",        # 0F, 15
        "Function_16_13BE",        # 10, 16
        "Function_17_14BE",        # 11, 17
        "Function_18_1536",        # 12, 18
        "Function_19_1636",        # 13, 19
        "Function_20_16AE",        # 14, 20
        "Function_21_17AE",        # 15, 21
        "Function_22_1826",        # 16, 22
        "Function_23_1926",        # 17, 23
        "Function_24_199E",        # 18, 24
        "Function_25_1AB0",        # 19, 25
        "Function_26_1B31",        # 1A, 26
        "Function_27_1C43",        # 1B, 27
        "Function_28_1CC4",        # 1C, 28
        "Function_29_1DA3",        # 1D, 29
        "Function_30_1E82",        # 1E, 30
        "Function_31_1ED0",        # 1F, 31
    )


    def Function_0_35E(): pass

    label("Function_0_35E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_38E"),
        (101, "loc_395"),
        (102, "loc_39C"),
        (103, "loc_3A3"),
        (104, "loc_3AA"),
        (105, "loc_3B1"),
        (106, "loc_3B8"),
        (107, "loc_3BF"),
        (108, "loc_3C6"),
        (109, "loc_3CD"),
        (SWITCH_DEFAULT, "loc_3D4"),
    )


    label("loc_38E")

    Event(0, 8)
    Jump("loc_3D4")

    label("loc_395")

    Event(0, 10)
    Jump("loc_3D4")

    label("loc_39C")

    Event(0, 12)
    Jump("loc_3D4")

    label("loc_3A3")

    Event(0, 14)
    Jump("loc_3D4")

    label("loc_3AA")

    Event(0, 16)
    Jump("loc_3D4")

    label("loc_3B1")

    Event(0, 18)
    Jump("loc_3D4")

    label("loc_3B8")

    Event(0, 20)
    Jump("loc_3D4")

    label("loc_3BF")

    Event(0, 22)
    Jump("loc_3D4")

    label("loc_3C6")

    Event(0, 24)
    Jump("loc_3D4")

    label("loc_3CD")

    Event(0, 26)
    Jump("loc_3D4")

    label("loc_3D4")

    Return()

    # Function_0_35E end

    def Function_1_3D5(): pass

    label("Function_1_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7")
    OP_6F(0x0, 0)
    Jump("loc_3EE")

    label("loc_3E7")

    OP_6F(0x0, 60)

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_400")
    OP_6F(0x1, 0)
    Jump("loc_407")

    label("loc_400")

    OP_6F(0x1, 60)

    label("loc_407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419")
    OP_6F(0x2, 0)
    Jump("loc_420")

    label("loc_419")

    OP_6F(0x2, 60)

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_432")
    OP_6F(0x3, 0)
    Jump("loc_439")

    label("loc_432")

    OP_6F(0x3, 60)

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B")
    OP_6F(0x4, 0)
    Jump("loc_452")

    label("loc_44B")

    OP_6F(0x4, 60)

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464")
    OP_6F(0x5, 0)
    Jump("loc_46B")

    label("loc_464")

    OP_6F(0x5, 60)

    label("loc_46B")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 3)), scpexpr(EXPR_END)), "loc_49F")
    SetChrFlags(0x8, 0x80)

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 4)), scpexpr(EXPR_END)), "loc_4AB")
    SetChrFlags(0x9, 0x80)

    label("loc_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 5)), scpexpr(EXPR_END)), "loc_4B7")
    SetChrFlags(0xA, 0x80)

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 6)), scpexpr(EXPR_END)), "loc_4C3")
    SetChrFlags(0xB, 0x80)

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FF, 7)), scpexpr(EXPR_END)), "loc_4CF")
    SetChrFlags(0xC, 0x80)

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 0)), scpexpr(EXPR_END)), "loc_4DB")
    SetChrFlags(0xD, 0x80)

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 1)), scpexpr(EXPR_END)), "loc_4E7")
    SetChrFlags(0xE, 0x80)

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 2)), scpexpr(EXPR_END)), "loc_4F3")
    SetChrFlags(0xF, 0x80)

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 3)), scpexpr(EXPR_END)), "loc_4FF")
    SetChrFlags(0x10, 0x80)

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 4)), scpexpr(EXPR_END)), "loc_50B")
    SetChrFlags(0x11, 0x80)

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 5)), scpexpr(EXPR_END)), "loc_517")
    SetChrFlags(0x12, 0x80)

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 6)), scpexpr(EXPR_END)), "loc_523")
    SetChrFlags(0x13, 0x80)

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D0, 7)), scpexpr(EXPR_END)), "loc_52F")
    SetChrFlags(0x14, 0x80)

    label("loc_52F")

    OP_1B(0x0, 0x0, 0x9)
    OP_1B(0x1, 0x0, 0xB)
    OP_1B(0x2, 0x0, 0xD)
    OP_1B(0x3, 0x0, 0xF)
    OP_1B(0x4, 0x0, 0x11)
    OP_1B(0x5, 0x0, 0x13)
    OP_1B(0x6, 0x0, 0x15)
    OP_1B(0x7, 0x0, 0x17)
    OP_1B(0x8, 0x0, 0x19)
    OP_1B(0x9, 0x0, 0x1B)
    Return()

    # Function_1_3D5 end

    def Function_2_562(): pass

    label("Function_2_562")

    OP_EA(0x2, 0x73, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_5D3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA4)
    Jump("loc_637")

    label("loc_5D3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_637")

    Jump("loc_68B")

    label("loc_63A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Mind doing me a favor and not opening me up\x01",
            "again?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_68B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_562 end

    def Function_3_699(): pass

    label("Function_3_699")

    OP_EA(0x2, 0x74, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_771")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x136, 1)"), scpexpr(EXPR_END)), "loc_70A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x36\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA5)
    Jump("loc_76E")

    label("loc_70A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x36\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x36\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_76E")

    Jump("loc_7CC")

    label("loc_771")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Any chance you could put that thing back where\x01",
            "you found it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7CC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_699 end

    def Function_4_7DA(): pass

    label("Function_4_7DA")

    OP_EA(0x2, 0x75, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_84B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA6)
    Jump("loc_8AF")

    label("loc_84B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_8AF")

    Jump("loc_92A")

    label("loc_8B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05Even though there wasn't anything in the chest,\x01",
            "opening it showered you in confetti! Yay!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_92A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_7DA end

    def Function_5_938(): pass

    label("Function_5_938")

    OP_EA(0x2, 0x76, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A10")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D3, 1)"), scpexpr(EXPR_END)), "loc_9A9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\xD3\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA7)
    Jump("loc_A0D")

    label("loc_9A9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\xD3\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xD3\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_A0D")

    Jump("loc_AC0")

    label("loc_A10")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05No matter where you go in this life, there's\x01",
            "always someone looking to take you for all you've\x01",
            "got. It happened to me, and it WILL happen to you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AC0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_938 end

    def Function_6_ACE(): pass

    label("Function_6_ACE")

    OP_EA(0x2, 0x77, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B97")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    AddSepith(0x0, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "Found\x01",
            "#2C#56IEarth Sepith x300\x01",
            "#62ITime Sepith x100\x01",
            "#60ISpace Sepith x100\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1FA8)
    Jump("loc_BEE")

    label("loc_B97")


    AnonymousTalk(    #13
        (
            "\x07\x05Think you can just take my stuff and run off?\x01",
            "You'll be hearing from my lawyer.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_BEE")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_ACE end

    def Function_7_C00(): pass

    label("Function_7_C00")

    OP_EA(0x2, 0x78, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_C71")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1FA9)
    Jump("loc_CD5")

    label("loc_C71")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_CD5")

    Jump("loc_D7F")

    label("loc_CD8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05You open the chest so quickly that it catches\x01",
            "fire, scorching its contents to ashes. Maybe\x01",
            "this'll teach you to contain your excitement!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D7F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_C00 end

    def Function_8_D8D(): pass

    label("Function_8_D8D")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 200, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -500, 200, -66000, 0)
    SetChrPos(0x102, 500, 200, -66000, 0)
    SetChrPos(0xF8, -500, 200, -67000, 0)
    SetChrPos(0xF9, 500, 200, -67000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(-60, 200, -64400, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -60, 200, -64400, 0)
    SetChrPos(0x1, -60, 200, -64400, 0)
    SetChrPos(0x2, -60, 200, -64400, 0)
    SetChrPos(0x3, -60, 200, -64400, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_8_D8D end

    def Function_9_E9F(): pass

    label("Function_9_E9F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 500, 200, -67000, 180)
    SetChrPos(0x102, -500, 200, -67000, 180)
    SetChrPos(0xF8, 500, 200, -66000, 180)
    SetChrPos(0xF9, -500, 200, -66000, 180)
    OP_0D()
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_9_E9F end

    def Function_10_F20(): pass

    label("Function_10_F20")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-46700, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -47200, 200, 46700, 0)
    SetChrPos(0x102, -46200, 200, 46700, 0)
    SetChrPos(0xF8, -47200, 200, 45700, 0)
    SetChrPos(0xF9, -46200, 200, 45700, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(-46770, 200, 48120, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -46770, 200, 48120, 0)
    SetChrPos(0x1, -46770, 200, 48120, 0)
    SetChrPos(0x2, -46770, 200, 48120, 0)
    SetChrPos(0x3, -46770, 200, 48120, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_10_F20 end

    def Function_11_1032(): pass

    label("Function_11_1032")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-46700, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -46200, 200, 45700, 180)
    SetChrPos(0x102, -47200, 200, 45700, 180)
    SetChrPos(0xF8, -46200, 200, 46700, 180)
    SetChrPos(0xF9, -47200, 200, 46700, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1032 end

    def Function_12_10B3(): pass

    label("Function_12_10B3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(46600, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 46100, 200, 46700, 0)
    SetChrPos(0x102, 47100, 200, 46700, 0)
    SetChrPos(0xF8, 46100, 200, 45700, 0)
    SetChrPos(0xF9, 47100, 200, 45700, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(46620, 200, 48180, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 46620, 200, 48180, 0)
    SetChrPos(0x1, 46620, 200, 48180, 0)
    SetChrPos(0x2, 46620, 200, 48180, 0)
    SetChrPos(0x3, 46620, 200, 48180, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_12_10B3 end

    def Function_13_11C5(): pass

    label("Function_13_11C5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(46600, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 47100, 200, 45700, 180)
    SetChrPos(0x102, 46100, 200, 45700, 180)
    SetChrPos(0xF8, 47100, 200, 46700, 180)
    SetChrPos(0xF9, 46100, 200, 46700, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_13_11C5 end

    def Function_14_1246(): pass

    label("Function_14_1246")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(46500, 200, -46100, 0)
    SetChrPos(0x101, 47000, 200, -46600, 180)
    SetChrPos(0x102, 46000, 200, -46600, 180)
    SetChrPos(0xF8, 47000, 200, -45600, 180)
    SetChrPos(0xF9, 46000, 200, -45600, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(46630, 200, -48040, 0)
    SetChrPos(0x0, 46630, 200, -48040, 180)
    SetChrPos(0x1, 46630, 200, -48040, 180)
    SetChrPos(0x2, 46630, 200, -48040, 180)
    SetChrPos(0x3, 46630, 200, -48040, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_14_1246 end

    def Function_15_1346(): pass

    label("Function_15_1346")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(46500, 200, -46100, 0)
    SetChrPos(0x101, 46000, 200, -45600, 0)
    SetChrPos(0x102, 47000, 200, -45600, 0)
    SetChrPos(0xF8, 46000, 200, -46600, 0)
    SetChrPos(0xF9, 47000, 200, -46600, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1346 end

    def Function_16_13BE(): pass

    label("Function_16_13BE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-46500, 200, -46000, 0)
    SetChrPos(0x101, -46000, 200, -46500, 180)
    SetChrPos(0x102, -47000, 200, -46500, 180)
    SetChrPos(0xF8, -46000, 200, -45500, 180)
    SetChrPos(0xF9, -47000, 200, -45500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(-46470, 200, -47980, 0)
    SetChrPos(0x0, -46470, 200, -47980, 180)
    SetChrPos(0x1, -46470, 200, -47980, 180)
    SetChrPos(0x2, -46470, 200, -47980, 180)
    SetChrPos(0x3, -46470, 200, -47980, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_16_13BE end

    def Function_17_14BE(): pass

    label("Function_17_14BE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-46500, 200, -46000, 0)
    SetChrPos(0x101, -47000, 200, -45500, 0)
    SetChrPos(0x102, -46000, 200, -45500, 0)
    SetChrPos(0xF8, -47000, 200, -46500, 0)
    SetChrPos(0xF9, -46000, 200, -46500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1701   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_17_14BE end

    def Function_18_1536(): pass

    label("Function_18_1536")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x101, 500, 200, 66000, 180)
    SetChrPos(0x102, -500, 200, 66000, 180)
    SetChrPos(0xF8, 500, 200, 67000, 180)
    SetChrPos(0xF9, -500, 200, 67000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(130, 200, 64560, 0)
    SetChrPos(0x0, 130, 200, 64560, 180)
    SetChrPos(0x1, 130, 200, 64560, 180)
    SetChrPos(0x2, 130, 200, 64560, 180)
    SetChrPos(0x3, 130, 200, 64560, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_18_1536 end

    def Function_19_1636(): pass

    label("Function_19_1636")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x101, -500, 200, 67000, 0)
    SetChrPos(0x102, 500, 200, 67000, 0)
    SetChrPos(0xF8, -500, 200, 66000, 0)
    SetChrPos(0xF9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1636 end

    def Function_20_16AE(): pass

    label("Function_20_16AE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-96100, 200, 96700, 0)
    SetChrPos(0x101, -95600, 200, 96200, 180)
    SetChrPos(0x102, -96600, 200, 96200, 180)
    SetChrPos(0xF8, -95600, 200, 97200, 180)
    SetChrPos(0xF9, -96600, 200, 97200, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(-96090, 200, 94660, 0)
    SetChrPos(0x0, -96090, 200, 94660, 180)
    SetChrPos(0x1, -96090, 200, 94660, 180)
    SetChrPos(0x2, -96090, 200, 94660, 180)
    SetChrPos(0x3, -96090, 200, 94660, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_20_16AE end

    def Function_21_17AE(): pass

    label("Function_21_17AE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-96100, 200, 96700, 0)
    SetChrPos(0x101, -96600, 200, 97200, 0)
    SetChrPos(0x102, -95600, 200, 97200, 0)
    SetChrPos(0xF8, -96600, 200, 96200, 0)
    SetChrPos(0xF9, -95600, 200, 96200, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_21_17AE end

    def Function_22_1826(): pass

    label("Function_22_1826")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(96200, 200, 96700, 0)
    SetChrPos(0x101, 96700, 200, 96200, 180)
    SetChrPos(0x102, 95700, 200, 96200, 180)
    SetChrPos(0xF8, 96700, 200, 97200, 180)
    SetChrPos(0xF9, 95700, 200, 97200, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 30)
    Fade(500)
    OP_6D(96270, 200, 94740, 0)
    SetChrPos(0x0, 96270, 200, 94740, 180)
    SetChrPos(0x1, 96270, 200, 94740, 180)
    SetChrPos(0x2, 96270, 200, 94740, 180)
    SetChrPos(0x3, 96270, 200, 94740, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_22_1826 end

    def Function_23_1926(): pass

    label("Function_23_1926")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(96200, 200, 96700, 0)
    SetChrPos(0x101, 95700, 200, 97200, 0)
    SetChrPos(0x102, 96700, 200, 97200, 0)
    SetChrPos(0xF8, 95700, 200, 96200, 0)
    SetChrPos(0xF9, 96700, 200, 96200, 0)
    OP_0D()
    Call(0, 28)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_23_1926 end

    def Function_24_199E(): pass

    label("Function_24_199E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 95500, 200, -96000, 0)
    SetChrPos(0x102, 96500, 200, -96000, 0)
    SetChrPos(0xF8, 95500, 200, -97000, 0)
    SetChrPos(0xF9, 96500, 200, -97000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(95950, 200, -94510, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 95950, 200, -94510, 0)
    SetChrPos(0x1, 95950, 200, -94510, 0)
    SetChrPos(0x2, 95950, 200, -94510, 0)
    SetChrPos(0x3, 95950, 200, -94510, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_24_199E end

    def Function_25_1AB0(): pass

    label("Function_25_1AB0")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 96500, 200, -97000, 180)
    SetChrPos(0x102, 95500, 200, -97000, 180)
    SetChrPos(0xF8, 96500, 200, -96000, 180)
    SetChrPos(0xF9, 95500, 200, -96000, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_25_1AB0 end

    def Function_26_1B31(): pass

    label("Function_26_1B31")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -96500, 200, -96000, 0)
    SetChrPos(0x102, -95500, 200, -96000, 0)
    SetChrPos(0xF8, -96500, 200, -97000, 0)
    SetChrPos(0xF9, -95500, 200, -97000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 29)
    Call(0, 30)
    Fade(500)
    OP_6D(-96080, 200, -94480, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -96080, 200, -94480, 0)
    SetChrPos(0x1, -96080, 200, -94480, 0)
    SetChrPos(0x2, -96080, 200, -94480, 0)
    SetChrPos(0x3, -96080, 200, -94480, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_26_1B31 end

    def Function_27_1C43(): pass

    label("Function_27_1C43")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -95500, 200, -97000, 180)
    SetChrPos(0x102, -96500, 200, -97000, 180)
    SetChrPos(0xF8, -95500, 200, -96000, 180)
    SetChrPos(0xF9, -96500, 200, -96000, 180)
    OP_0D()
    Call(0, 29)
    Call(0, 31)
    NewScene("ED6_DT21/C1703   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_27_1C43 end

    def Function_28_1CC4(): pass

    label("Function_28_1CC4")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_28_1CC4 end

    def Function_29_1DA3(): pass

    label("Function_29_1DA3")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_29_1DA3 end

    def Function_30_1E82(): pass

    label("Function_30_1E82")


    def lambda_1E88():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E88)

    def lambda_1E9A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1E9A)

    def lambda_1EAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1EAC)

    def lambda_1EBE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1EBE)
    Sleep(2500)
    Return()

    # Function_30_1E82 end

    def Function_31_1ED0(): pass

    label("Function_31_1ED0")


    def lambda_1ED6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1ED6)

    def lambda_1EE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1EE8)

    def lambda_1EFA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1EFA)

    def lambda_1F0C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1F0C)
    Sleep(2000)
    Return()

    # Function_31_1ED0 end

    SaveToFile()

Try(main)
