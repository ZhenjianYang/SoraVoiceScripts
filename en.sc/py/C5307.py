from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5307   ._SN',
        MapName             = 'Other',
        Location            = 'C5307.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        'Elevator',                             # 9
        '',                                     # 10
        '',                                     # 11
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
        'ED6_DT29/CH12420 ._CH',             # 00
        'ED6_DT29/CH12421 ._CH',             # 01
        'ED6_DT29/CH12280 ._CH',             # 02
        'ED6_DT29/CH12281 ._CH',             # 03
        'ED6_DT29/CH12300 ._CH',             # 04
        'ED6_DT29/CH12301 ._CH',             # 05
        'ED6_DT29/CH12290 ._CH',             # 06
        'ED6_DT29/CH12291 ._CH',             # 07
        'ED6_DT29/CH12340 ._CH',             # 08
        'ED6_DT29/CH12341 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH12420P._CP',             # 00
        'ED6_DT29/CH12421P._CP',             # 01
        'ED6_DT29/CH12280P._CP',             # 02
        'ED6_DT29/CH12281P._CP',             # 03
        'ED6_DT29/CH12300P._CP',             # 04
        'ED6_DT29/CH12301P._CP',             # 05
        'ED6_DT29/CH12290P._CP',             # 06
        'ED6_DT29/CH12291P._CP',             # 07
        'ED6_DT29/CH12340P._CP',             # 08
        'ED6_DT29/CH12341P._CP',             # 09
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -107060,
        Z                   = 1500,
        Y                   = 9030,
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


    DeclMonster(
        X                   = -91860,
        Z                   = 2170,
        Y                   = 97190,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -99300,
        Z                   = 50,
        Y                   = 8630,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x530,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -78310,
        Z                   = 2690,
        Y                   = -74320,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 84130,
        Z                   = 2220,
        Y                   = -84980,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 5170,
        Y                   = -2000,
        Z                   = 110010,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 100000,
        Y                   = -2000,
        Z                   = 9010,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 10,
    )


    DeclActor(
        TriggerX            = -105100,
        TriggerZ            = 0,
        TriggerY            = 3560,
        TriggerRange        = 1000,
        ActorX              = -105130,
        ActorZ              = 0,
        ActorY              = 2950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -106430,
        TriggerZ            = 0,
        TriggerY            = 9060,
        TriggerRange        = 1000,
        ActorX              = -107060,
        ActorZ              = 0,
        ActorY              = 9030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -105100,
        TriggerZ            = 0,
        TriggerY            = 14350,
        TriggerRange        = 1000,
        ActorX              = -105070,
        ActorZ              = 0,
        ActorY              = 15000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92920,
        TriggerZ            = 0,
        TriggerY            = 14350,
        TriggerRange        = 1000,
        ActorX              = -92880,
        ActorZ              = 0,
        ActorY              = 15030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -91440,
        TriggerZ            = 0,
        TriggerY            = 8950,
        TriggerRange        = 1000,
        ActorX              = -90840,
        ActorZ              = 0,
        ActorY              = 8980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -93070,
        TriggerZ            = 0,
        TriggerY            = 3650,
        TriggerRange        = 1000,
        ActorX              = -92940,
        ActorZ              = 0,
        ActorY              = 2970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -710,
        TriggerZ            = 2000,
        TriggerY            = -93980,
        TriggerRange        = 1000,
        ActorX              = -80,
        ActorZ              = 2000,
        ActorY              = -93950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 92130,
        TriggerZ            = 8000,
        TriggerY            = -57040,
        TriggerRange        = 1200,
        ActorX              = 92130,
        ActorZ              = 9200,
        ActorY              = -57040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_30A",          # 00, 0
        "Function_1_31B",          # 01, 1
        "Function_2_479",          # 02, 2
        "Function_3_48F",          # 03, 3
        "Function_4_5F1",          # 04, 4
        "Function_5_7FD",          # 05, 5
        "Function_6_95B",          # 06, 6
        "Function_7_AE8",          # 07, 7
        "Function_8_C38",          # 08, 8
        "Function_9_D7A",          # 09, 9
        "Function_10_F09",         # 0A, 10
        "Function_11_10FE",        # 0B, 11
        "Function_12_122B",        # 0C, 12
        "Function_13_13C7",        # 0D, 13
    )


    def Function_0_30A(): pass

    label("Function_0_30A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A")
    Event(0, 12)

    label("loc_31A")

    Return()

    # Function_0_30A end

    def Function_1_31B(): pass

    label("Function_1_31B")

    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_359")
    OP_6F(0x2, 0)
    Jump("loc_360")

    label("loc_359")

    OP_6F(0x2, 60)

    label("loc_360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_372")
    OP_6F(0x3, 0)
    Jump("loc_379")

    label("loc_372")

    OP_6F(0x3, 60)

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B")
    OP_6F(0x4, 0)
    Jump("loc_392")

    label("loc_38B")

    OP_6F(0x4, 60)

    label("loc_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4")
    OP_6F(0x5, 0)
    Jump("loc_3AB")

    label("loc_3A4")

    OP_6F(0x5, 60)

    label("loc_3AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD")
    OP_6F(0x6, 0)
    Jump("loc_3C4")

    label("loc_3BD")

    OP_6F(0x6, 60)

    label("loc_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D6")
    OP_6F(0x7, 0)
    Jump("loc_3DD")

    label("loc_3D6")

    OP_6F(0x7, 60)

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x473, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF")
    OP_6F(0x8, 0)
    Jump("loc_3F6")

    label("loc_3EF")

    OP_6F(0x8, 60)

    label("loc_3F6")

    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_22(0x140, 0x0, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46C")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 92130, 9200, -57040, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_71(0x9, 0x20)
    OP_6F(0x9, 0)
    OP_70(0x9, 0xFA)
    Jump("loc_478")

    label("loc_46C")

    OP_72(0x9, 0x20)
    OP_6F(0x9, 250)

    label("loc_478")

    Return()

    # Function_1_31B end

    def Function_2_479(): pass

    label("Function_2_479")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_479")

    label("loc_48E")

    Return()

    # Function_2_479 end

    def Function_3_48F(): pass

    label("Function_3_48F")

    OP_EA(0x2, 0x4C, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_567")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_500")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2390)
    Jump("loc_564")

    label("loc_500")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_564")

    Jump("loc_5E3")

    label("loc_567")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05We're sorry; the item fairies haven't restocked\x01",
            "this chest yet. Please come visit again soon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_48F end

    def Function_4_5F1(): pass

    label("Function_4_5F1")

    OP_EA(0x2, 0x4D, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DB")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_91(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_648():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_648)

    def lambda_663():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_663)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(    #3
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x532, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6B6"),
        (2, "loc_6C8"),
        (1, "loc_6D8"),
        (SWITCH_DEFAULT, "loc_6DB"),
    )


    label("loc_6B6")

    OP_A2(0x2392)
    OP_6F(0x3, 60)
    Sleep(500)
    Jump("loc_6DB")

    label("loc_6C8")

    OP_6F(0x3, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_6D8")

    OP_B4(0x0)
    Return()

    label("loc_6DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2B, 1)"), scpexpr(EXPR_END)), "loc_727")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        "Found \x1F\x2B\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2391)
    Jump("loc_789")

    label("loc_727")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #5
        (
            "Found \x1F\x2B\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x2B\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_789")

    Jump("loc_7EF")

    label("loc_78C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        (
            "\x07\x05There's nothing in the chest, but the air\x01",
            "inside is strangely...humid.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7EF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5F1 end

    def Function_5_7FD(): pass

    label("Function_5_7FD")

    OP_EA(0x2, 0x4E, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_86E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\xFA\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2393)
    Jump("loc_8D2")

    label("loc_86E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "Found \x1F\xFA\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFA\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_8D2")

    Jump("loc_94D")

    label("loc_8D5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05An empty treasure chest. Full of promise\x01",
            "yet devoid of payoff. A perfect metaphor for me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_94D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7FD end

    def Function_6_95B(): pass

    label("Function_6_95B")

    OP_EA(0x2, 0x4F, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A33")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_9CC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\x01\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2394)
    Jump("loc_A30")

    label("loc_9CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\x01\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x01\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_A30")

    Jump("loc_ADA")

    label("loc_A33")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05Somewhere out there is a person who started\x01",
            "playing Trails in the Sky Second Chapter before\x01",
            "the first game. I bet they're very confused.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_ADA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_95B end

    def Function_7_AE8(): pass

    label("Function_7_AE8")

    OP_EA(0x2, 0x50, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x1E)
    OP_73(0x6)
    OP_6F(0x6, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #13
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2395)
    Jump("loc_C26")

    label("loc_BDF")


    AnonymousTalk(    #14
        (
            "\x07\x05Back again? You might be the most desperate\x01",
            "hero I've ever met.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_C26")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_AE8 end

    def Function_8_C38(): pass

    label("Function_8_C38")

    OP_EA(0x2, 0x51, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x472, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D10")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_CA9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2397)
    Jump("loc_D0D")

    label("loc_CA9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_D0D")

    Jump("loc_D6C")

    label("loc_D10")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05BREAKING NEWS! There's nothing in this chest.\x01",
            "More at eleven.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D6C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C38 end

    def Function_9_D7A(): pass

    label("Function_9_D7A")

    OP_EA(0x2, 0x52, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x473, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E52")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x171, 1)"), scpexpr(EXPR_END)), "loc_DEB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "Found \x1F\x71\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2398)
    Jump("loc_E4F")

    label("loc_DEB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "Found \x1F\x71\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x71\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_E4F")

    Jump("loc_EFB")

    label("loc_E52")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05Hey, I know you had high hopes for this chest,\x01",
            "but it's empty. Don't worry about it, though!\x01",
            "Maybe the next one will have something great.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EFB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_D7A end

    def Function_10_F09(): pass

    label("Function_10_F09")

    EventBegin(0x0)
    FadeToBright(0, 0)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 100000, -1750, 9010, 0)
    OP_48()
    Fade(1000)
    OP_6D(100000, 0, 9010, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 0, 10010, 0)
    OP_89(0x1, 101000, 0, 9010, 90)
    OP_89(0x2, 99000, 0, 9010, 270)
    OP_89(0x3, 100000, 0, 8010, 180)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_FC2():
        OP_8F(0xFE, 0x186A0, 0xFDE8, 0x2332, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FC2)
    Sleep(500)

    def lambda_FE2():
        OP_6D(100000, 35000, 9010, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE2)

    def lambda_FFA():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FFA)

    def lambda_1012():
        OP_6C(335000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1012)
    Sleep(500)

    def lambda_1027():
        OP_8F(0xFE, 0x186A0, 0xFDE8, 0x2332, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1027)
    Sleep(500)

    def lambda_1047():
        OP_8F(0xFE, 0x186A0, 0xFDE8, 0x2332, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1047)
    Sleep(400)

    def lambda_1067():
        OP_8F(0xFE, 0x186A0, 0xFDE8, 0x2332, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1067)
    Sleep(200)

    def lambda_1087():
        OP_8F(0xFE, 0x186A0, 0xFDE8, 0x2332, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1087)
    Sleep(100)

    def lambda_10A7():
        OP_8F(0xFE, 0x186A0, 0xFDE8, 0x2332, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10A7)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A2(0x2295)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_F09 end

    def Function_11_10FE(): pass

    label("Function_11_10FE")

    EventBegin(0x0)
    OP_A1(0x8, 0x1)
    SetChrPos(0x8, 5170, -1750, 110010, 90)
    OP_48()
    Fade(1000)
    OP_6D(5170, 0, 110010, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(298000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 5000, 0, 111000, 0)
    OP_89(0x1, 6000, 0, 110000, 90)
    OP_89(0x2, 4000, 0, 110000, 270)
    OP_89(0x3, 5000, 0, 109000, 180)
    OP_0D()
    Sleep(300)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_11B3():
        OP_67(0, 6500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11B3)

    def lambda_11CB():
        OP_6B(3700, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11CB)

    def lambda_11DB():
        OP_91(0xFE, 0x0, 0xFFFFD8F0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11DB)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A2(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_10FE end

    def Function_12_122B(): pass

    label("Function_12_122B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x1)
    SetChrPos(0x8, 5170, -11750, 110010, 90)
    OP_48()
    OP_6D(5170, 0, 110010, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 5000, 0, 111000, 0)
    OP_89(0x1, 6000, 0, 110000, 90)
    OP_89(0x2, 4000, 0, 110000, 270)
    OP_89(0x3, 5000, 0, 109000, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_12DA():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12DA)
    FadeToBright(1000, 0)
    SetPlaceName(0x121)

    def lambda_12F6():
        OP_91(0xFE, 0x0, 0x2710, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12F6)
    Sleep(2200)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 20, 0, 109960, 270)
    SetChrPos(0x1, 20, 0, 109960, 270)
    SetChrPos(0x2, 20, 0, 109960, 270)
    SetChrPos(0x3, 20, 0, 109960, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_12_122B end

    def Function_13_13C7(): pass

    label("Function_13_13C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_15CF")

    label("loc_142D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B4")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x9, 0x20)
    OP_6F(0x9, 300)
    OP_70(0x9, 0x1F4)
    OP_73(0x9)
    OP_6F(0x9, 500)
    OP_70(0x9, 0x2BC)
    OP_71(0x9, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 92130, 9200, -57040, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 92130, 9200, -57040, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x9, 0)
    OP_70(0x9, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_15B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15CE")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_15CE")

    Return()

    label("loc_15CF")

    Return()

    # Function_13_13C7 end

    SaveToFile()

Try(main)
