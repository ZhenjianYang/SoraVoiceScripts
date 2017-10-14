from ED6SCScenarioHelper import *

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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
    )

    DeclMonster(
        X                   = 53080,
        Z                   = 0,
        Y                   = 1650,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24670,
        Z                   = 0,
        Y                   = 22960,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -8910,
        Z                   = 0,
        Y                   = 21050,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20410,
        Z                   = -500,
        Y                   = 27460,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41620,
        Z                   = 1000,
        Y                   = 45310,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32180,
        Z                   = 0,
        Y                   = 61060,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -48200,
        Z                   = 0,
        Y                   = 5330,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9720,
        Z                   = 0,
        Y                   = -137210,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 217380,
        Z                   = 0,
        Y                   = 12010,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
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
        TalkFunctionIndex   = 2,
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
        TalkFunctionIndex   = 3,
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
        TalkFunctionIndex   = 4,
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
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -940,
        TriggerZ            = 0,
        TriggerY            = -135030,
        TriggerRange        = 1000,
        ActorX              = -180,
        ActorZ              = 0,
        ActorY              = -135030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
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
        TalkFunctionIndex   = 7,
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
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_302",          # 00, 0
        "Function_1_333",          # 01, 1
        "Function_2_43E",          # 02, 2
        "Function_3_546",          # 03, 3
        "Function_4_6A6",          # 04, 4
        "Function_5_800",          # 05, 5
        "Function_6_96A",          # 06, 6
        "Function_7_AC1",          # 07, 7
        "Function_8_BE2",          # 08, 8
        "Function_9_D38",          # 09, 9
    )


    def Function_0_302(): pass

    label("Function_0_302")

    OP_11(0xFF, 0xFF, 0xFF, 0x9C40, 0x12110, 0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_31E"),
        (SWITCH_DEFAULT, "loc_332"),
    )


    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F")
    SetMapFlags(0x10000000)
    Event(0, 9)

    label("loc_32F")

    Jump("loc_332")

    label("loc_332")

    Return()

    # Function_0_302 end

    def Function_1_333(): pass

    label("Function_1_333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345")
    OP_6F(0x0, 0)
    Jump("loc_34C")

    label("loc_345")

    OP_6F(0x0, 60)

    label("loc_34C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E")
    OP_6F(0x1, 0)
    Jump("loc_365")

    label("loc_35E")

    OP_6F(0x1, 60)

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377")
    OP_6F(0x2, 0)
    Jump("loc_37E")

    label("loc_377")

    OP_6F(0x2, 60)

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390")
    OP_6F(0x3, 0)
    Jump("loc_397")

    label("loc_390")

    OP_6F(0x3, 60)

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9")
    OP_6F(0x4, 0)
    Jump("loc_3B0")

    label("loc_3A9")

    OP_6F(0x4, 60)

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x371, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C2")
    OP_6F(0x5, 0)
    Jump("loc_3C9")

    label("loc_3C2")

    OP_6F(0x5, 60)

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x371, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB")
    OP_6F(0x6, 0)
    Jump("loc_3E2")

    label("loc_3DB")

    OP_6F(0x6, 60)

    label("loc_3E2")

    OP_E0(0x4, 0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0, 0x0, 0x0, 0x8A, 0xF0, 0xFD, 0xFF)
    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_333 end

    def Function_2_43E(): pass

    label("Function_2_43E")

    OP_EA(0x2, 0x5C, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_516")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17B, 1)"), scpexpr(EXPR_END)), "loc_4AF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x7B\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B80)
    Jump("loc_513")

    label("loc_4AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x7B\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x7B\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_513")

    Jump("loc_538")

    label("loc_516")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05No.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_538")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_43E end

    def Function_3_546(): pass

    label("Function_3_546")

    OP_EA(0x2, 0x5D, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16C, 1)"), scpexpr(EXPR_END)), "loc_5B7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x6C\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B82)
    Jump("loc_61B")

    label("loc_5B7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x6C\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6C\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_61B")

    Jump("loc_698")

    label("loc_61E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05There's nothing in the chest. You briefly\x01",
            "wonder if you could use it as a makeshift\x01",
            "boat...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_698")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_546 end

    def Function_4_6A6(): pass

    label("Function_4_6A6")

    OP_EA(0x2, 0x5E, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xC5, 1)"), scpexpr(EXPR_END)), "loc_717")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xC5\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B84)
    Jump("loc_77B")

    label("loc_717")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xC5\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xC5\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_77B")

    Jump("loc_7F2")

    label("loc_77E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05There is nothing in the chest but spiders now.\x01",
            "They all stare at you and clap. Bravo.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7F2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6A6 end

    def Function_5_800(): pass

    label("Function_5_800")

    OP_EA(0x2, 0x5F, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_871")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B86)
    Jump("loc_8D5")

    label("loc_871")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
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

    label("loc_8D5")

    Jump("loc_95C")

    label("loc_8D8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05You look under the chest, hoping to find the\x01",
            "keys to a BRAND NEW AIRSHIP! ...You don't find\x01",
            "anything.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_95C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_800 end

    def Function_6_96A(): pass

    label("Function_6_96A")

    OP_EA(0x2, 0x60, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x370, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A42")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_9DB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B87)
    Jump("loc_A3F")

    label("loc_9DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_A3F")

    Jump("loc_AB3")

    label("loc_A42")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05This treasure chest graduated at the top of its\x01",
            "class at the Riches Royal Academy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AB3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_96A end

    def Function_7_AC1(): pass

    label("Function_7_AC1")

    OP_EA(0x2, 0x61, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x371, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B99")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_B32")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B88)
    Jump("loc_B96")

    label("loc_B32")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_B96")

    Jump("loc_BD4")

    label("loc_B99")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05I dunno what you expected...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BD4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_AC1 end

    def Function_8_BE2(): pass

    label("Function_8_BE2")

    OP_EA(0x2, 0x62, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x371, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_C53")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B89)
    Jump("loc_CB7")

    label("loc_C53")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_CB7")

    Jump("loc_D2A")

    label("loc_CBA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05This chest remembers your previous visit and is\x01",
            "none too happy to see you return.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D2A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_BE2 end

    def Function_9_D38(): pass

    label("Function_9_D38")

    OP_C8(0x200, 0x32, "C_PLAC17._CH", 0x0, 0x3E8)
    OP_DE("Ancient Dragon Nest")
    OP_A2(0x1A84)
    Return()

    # Function_9_D38 end

    SaveToFile()

Try(main)
