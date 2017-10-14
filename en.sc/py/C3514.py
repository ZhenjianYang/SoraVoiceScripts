from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3514   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3514.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10710 ._CH',             # 00
        'ED6_DT09/CH10711 ._CH',             # 01
        'ED6_DT09/CH10720 ._CH',             # 02
        'ED6_DT09/CH10721 ._CH',             # 03
        'ED6_DT09/CH10730 ._CH',             # 04
        'ED6_DT09/CH10731 ._CH',             # 05
        'ED6_DT09/CH10740 ._CH',             # 06
        'ED6_DT09/CH10741 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10710P._CP',             # 00
        'ED6_DT09/CH10711P._CP',             # 01
        'ED6_DT09/CH10720P._CP',             # 02
        'ED6_DT09/CH10721P._CP',             # 03
        'ED6_DT09/CH10730P._CP',             # 04
        'ED6_DT09/CH10731P._CP',             # 05
        'ED6_DT09/CH10740P._CP',             # 06
        'ED6_DT09/CH10741P._CP',             # 07
    )

    DeclMonster(
        X                   = 2040,
        Z                   = 0,
        Y                   = 3920,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 5517,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 3970,
        Z                   = 0,
        Y                   = -1960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 5518,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1920,
        Z                   = 0,
        Y                   = -4010,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 5519,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4080,
        Z                   = 0,
        Y                   = 1890,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 5520,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -120,
        Z                   = 0,
        Y                   = -17970,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F8,
        Unknown_18          = 5521,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -4690,
        TriggerZ            = 0,
        TriggerY            = -22750,
        TriggerRange        = 1000,
        ActorX              = -4690,
        ActorZ              = 0,
        ActorY              = -23410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4740,
        TriggerZ            = 0,
        TriggerY            = -22710,
        TriggerRange        = 1000,
        ActorX              = 4800,
        ActorZ              = 0,
        ActorY              = -23330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_1BF",          # 01, 1
        "Function_2_22E",          # 02, 2
        "Function_3_3BD",          # 03, 3
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Return()

    # Function_0_1BE end

    def Function_1_1BF(): pass

    label("Function_1_1BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1")
    OP_6F(0x0, 0)
    Jump("loc_1D8")

    label("loc_1D1")

    OP_6F(0x0, 60)

    label("loc_1D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA")
    OP_6F(0x1, 0)
    Jump("loc_1F1")

    label("loc_1EA")

    OP_6F(0x1, 60)

    label("loc_1F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B1, 5)), scpexpr(EXPR_END)), "loc_1FD")
    SetChrFlags(0x8, 0x80)

    label("loc_1FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B1, 6)), scpexpr(EXPR_END)), "loc_209")
    SetChrFlags(0x9, 0x80)

    label("loc_209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B1, 7)), scpexpr(EXPR_END)), "loc_215")
    SetChrFlags(0xA, 0x80)

    label("loc_215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B2, 0)), scpexpr(EXPR_END)), "loc_221")
    SetChrFlags(0xB, 0x80)

    label("loc_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B2, 1)), scpexpr(EXPR_END)), "loc_22D")
    SetChrFlags(0xC, 0x80)

    label("loc_22D")

    Return()

    # Function_1_1BF end

    def Function_2_22E(): pass

    label("Function_2_22E")

    OP_EA(0x2, 0xCD, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x274, 1)"), scpexpr(EXPR_END)), "loc_29F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x74\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1549)
    Jump("loc_303")

    label("loc_29F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x74\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x74\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_303")

    Jump("loc_3AF")

    label("loc_306")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05What if our universe is a chest in someone ELSE's\x01",
            "universe, and someone's going to open us up,\x01",
            "take everything, and just keep coming back?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3AF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_22E end

    def Function_3_3BD(): pass

    label("Function_3_3BD")

    OP_EA(0x2, 0xCE, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_42E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x154A)
    Jump("loc_492")

    label("loc_42E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_492")

    Jump("loc_50C")

    label("loc_495")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05You know this chest is empty, so why do you do\x01",
            "this to yourself? Why do you keep hoping?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_50C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3BD end

    SaveToFile()

Try(main)
