from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1214   ._SN',
        MapName             = 'Bose',
        Location            = 'C1214.x',
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
        'ED6_DT09/CH10410 ._CH',             # 00
        'ED6_DT09/CH10411 ._CH',             # 01
        'ED6_DT09/CH10420 ._CH',             # 02
        'ED6_DT09/CH10421 ._CH',             # 03
        'ED6_DT09/CH10430 ._CH',             # 04
        'ED6_DT09/CH10431 ._CH',             # 05
        'ED6_DT09/CH10440 ._CH',             # 06
        'ED6_DT09/CH10441 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10410P._CP',             # 00
        'ED6_DT09/CH10411P._CP',             # 01
        'ED6_DT09/CH10420P._CP',             # 02
        'ED6_DT09/CH10421P._CP',             # 03
        'ED6_DT09/CH10430P._CP',             # 04
        'ED6_DT09/CH10431P._CP',             # 05
        'ED6_DT09/CH10440P._CP',             # 06
        'ED6_DT09/CH10441P._CP',             # 07
    )

    DeclNpc(
        X                   = 10,
        Z                   = 1000,
        Y                   = -18040,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -20,
        Z                   = 0,
        Y                   = 3950,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x8F,
        Unknown_18          = 7081,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20,
        Z                   = 0,
        Y                   = -4200,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x8F,
        Unknown_18          = 7082,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = -17250,
        TriggerRange        = 1000,
        ActorX              = 10,
        ActorZ              = 0,
        ActorY              = -18040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9320,
        TriggerZ            = 0,
        TriggerY            = 9340,
        TriggerRange        = 1000,
        ActorX              = 8670,
        ActorZ              = 0,
        ActorY              = 8680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9260,
        TriggerZ            = 0,
        TriggerY            = -9330,
        TriggerRange        = 1000,
        ActorX              = -8820,
        ActorZ              = 0,
        ActorY              = -8890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9370,
        TriggerZ            = 0,
        TriggerY            = -9350,
        TriggerRange        = 1000,
        ActorX              = 8910,
        ActorZ              = 0,
        ActorY              = -8880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9360,
        TriggerZ            = 0,
        TriggerY            = 9260,
        TriggerRange        = 1000,
        ActorX              = -8830,
        ActorZ              = 0,
        ActorY              = 8860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = -22520,
        TriggerRange        = 1000,
        ActorX              = 4610,
        ActorZ              = 0,
        ActorY              = -23140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4490,
        TriggerZ            = 0,
        TriggerY            = -22490,
        TriggerRange        = 1000,
        ActorX              = -4490,
        ActorZ              = 0,
        ActorY              = -23150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_23E",          # 00, 0
        "Function_1_23F",          # 01, 1
        "Function_2_307",          # 02, 2
        "Function_3_31D",          # 03, 3
        "Function_4_52A",          # 04, 4
        "Function_5_675",          # 05, 5
        "Function_6_7C0",          # 06, 6
        "Function_7_94D",          # 07, 7
        "Function_8_AD2",          # 08, 8
        "Function_9_C2E",          # 09, 9
    )


    def Function_0_23E(): pass

    label("Function_0_23E")

    Return()

    # Function_0_23E end

    def Function_1_23F(): pass

    label("Function_1_23F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251")
    OP_6F(0x0, 0)
    Jump("loc_258")

    label("loc_251")

    OP_6F(0x0, 60)

    label("loc_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A")
    OP_6F(0x1, 0)
    Jump("loc_271")

    label("loc_26A")

    OP_6F(0x1, 60)

    label("loc_271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283")
    OP_6F(0x2, 0)
    Jump("loc_28A")

    label("loc_283")

    OP_6F(0x2, 60)

    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C")
    OP_6F(0x3, 0)
    Jump("loc_2A3")

    label("loc_29C")

    OP_6F(0x3, 60)

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5")
    OP_6F(0x4, 0)
    Jump("loc_2BC")

    label("loc_2B5")

    OP_6F(0x4, 60)

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE")
    OP_6F(0x5, 0)
    Jump("loc_2D5")

    label("loc_2CE")

    OP_6F(0x5, 60)

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E7")
    OP_6F(0x6, 0)
    Jump("loc_2EE")

    label("loc_2E7")

    OP_6F(0x6, 60)

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x375, 1)), scpexpr(EXPR_END)), "loc_2FA")
    SetChrFlags(0x9, 0x80)

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x375, 2)), scpexpr(EXPR_END)), "loc_306")
    SetChrFlags(0xA, 0x80)

    label("loc_306")

    Return()

    # Function_1_23F end

    def Function_2_307(): pass

    label("Function_2_307")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_307")

    label("loc_31C")

    Return()

    # Function_2_307 end

    def Function_3_31D(): pass

    label("Function_3_31D")

    OP_EA(0x2, 0xA, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_374():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_374)

    def lambda_38F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_38F)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x92, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3E2"),
        (2, "loc_3F4"),
        (1, "loc_404"),
        (SWITCH_DEFAULT, "loc_407"),
    )


    label("loc_3E2")

    OP_A2(0x1B60)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_407")

    label("loc_3F4")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_404")

    OP_B4(0x0)
    Return()

    label("loc_407")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x6E, 1)"), scpexpr(EXPR_END)), "loc_453")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found \x1F\x6E\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B5F)
    Jump("loc_4B5")

    label("loc_453")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "Found \x1F\x6E\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6E\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4B5")

    Jump("loc_51C")

    label("loc_4B8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "\x07\x05It's empty, obviously. Probably should have\x01",
            "thought this one through...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_51C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_31D end

    def Function_4_52A(): pass

    label("Function_4_52A")

    OP_EA(0x2, 0x3D, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_602")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_59B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B61)
    Jump("loc_5FF")

    label("loc_59B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_5FF")

    Jump("loc_667")

    label("loc_602")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05Inside the chest is a tear in the fabric of reality.\x01",
            "DON'T poke at it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_667")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_52A end

    def Function_5_675(): pass

    label("Function_5_675")

    OP_EA(0x2, 0x3E, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_6E6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B62)
    Jump("loc_74A")

    label("loc_6E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
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

    label("loc_74A")

    Jump("loc_7B2")

    label("loc_74D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05As you open this already-empty chest,\x01",
            "its hinges pinch you in revenge.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7B2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_675 end

    def Function_6_7C0(): pass

    label("Function_6_7C0")

    OP_EA(0x2, 0x3F, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_898")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x146, 1)"), scpexpr(EXPR_END)), "loc_831")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\x46\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B63)
    Jump("loc_895")

    label("loc_831")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\x46\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x46\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_895")

    Jump("loc_93F")

    label("loc_898")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05Remember the stuff you took from here last time?\x01",
            "Yeah, the chest was TRYING to afford chest college.\x01",
            "Guess it has to start over again...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_93F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7C0 end

    def Function_7_94D(): pass

    label("Function_7_94D")

    OP_EA(0x2, 0x40, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A25")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_9BE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B64)
    Jump("loc_A22")

    label("loc_9BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_A22")

    Jump("loc_AC4")

    label("loc_A25")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05You open the empty chest open again and again,\x01",
            "cackling manically to yourself. You KNOW it\x01",
            "contains some secret. It just has to!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AC4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_94D end

    def Function_8_AD2(): pass

    label("Function_8_AD2")

    OP_EA(0x2, 0x41, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_B43")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B65)
    Jump("loc_BA7")

    label("loc_B43")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
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

    label("loc_BA7")

    Jump("loc_C20")

    label("loc_BAA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05How many years does it take for a story of heroes\x01",
            "to become a legend of heroes, anyway?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C20")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_AD2 end

    def Function_9_C2E(): pass

    label("Function_9_C2E")

    OP_EA(0x2, 0x42, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D06")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1AE, 1)"), scpexpr(EXPR_END)), "loc_C9F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "Found \x1F\xAE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B66)
    Jump("loc_D03")

    label("loc_C9F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "Found \x1F\xAE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xAE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_D03")

    Jump("loc_D9D")

    label("loc_D06")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05Sure, the chest LOOKS nice enough, but you\x01",
            "wouldn't want to get on its bad side. Especially\x01",
            "with your hand inside of it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D9D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_C2E end

    SaveToFile()

Try(main)
