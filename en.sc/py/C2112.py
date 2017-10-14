from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2112   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2112.x',
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
        'ED6_DT09/CH10560 ._CH',             # 00
        'ED6_DT09/CH10561 ._CH',             # 01
        'ED6_DT09/CH10570 ._CH',             # 02
        'ED6_DT09/CH10571 ._CH',             # 03
        'ED6_DT09/CH10580 ._CH',             # 04
        'ED6_DT09/CH10581 ._CH',             # 05
        'ED6_DT09/CH10590 ._CH',             # 06
        'ED6_DT09/CH10591 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10560P._CP',             # 00
        'ED6_DT09/CH10561P._CP',             # 01
        'ED6_DT09/CH10570P._CP',             # 02
        'ED6_DT09/CH10571P._CP',             # 03
        'ED6_DT09/CH10580P._CP',             # 04
        'ED6_DT09/CH10581P._CP',             # 05
        'ED6_DT09/CH10590P._CP',             # 06
        'ED6_DT09/CH10591P._CP',             # 07
    )

    DeclMonster(
        X                   = -150,
        Z                   = 0,
        Y                   = -10,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B9,
        Unknown_18          = 4945,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21120,
        Z                   = 0,
        Y                   = 3940,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BB,
        Unknown_18          = 4946,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21420,
        Z                   = 0,
        Y                   = 3700,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BA,
        Unknown_18          = 4947,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -21770,
        TriggerZ            = 0,
        TriggerY            = -2940,
        TriggerRange        = 1000,
        ActorX              = -21820,
        ActorZ              = 0,
        ActorY              = -3560,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22320,
        TriggerZ            = 0,
        TriggerY            = -80,
        TriggerRange        = 1000,
        ActorX              = 22880,
        ActorZ              = 0,
        ActorY              = -170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_186",          # 00, 0
        "Function_1_187",          # 01, 1
        "Function_2_1DE",          # 02, 2
        "Function_3_319",          # 03, 3
    )


    def Function_0_186(): pass

    label("Function_0_186")

    Return()

    # Function_0_186 end

    def Function_1_187(): pass

    label("Function_1_187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199")
    OP_6F(0x0, 0)
    Jump("loc_1A0")

    label("loc_199")

    OP_6F(0x0, 60)

    label("loc_1A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2")
    OP_6F(0x1, 0)
    Jump("loc_1B9")

    label("loc_1B2")

    OP_6F(0x1, 60)

    label("loc_1B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26A, 1)), scpexpr(EXPR_END)), "loc_1C5")
    SetChrFlags(0x8, 0x80)

    label("loc_1C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26A, 2)), scpexpr(EXPR_END)), "loc_1D1")
    SetChrFlags(0x9, 0x80)

    label("loc_1D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26A, 3)), scpexpr(EXPR_END)), "loc_1DD")
    SetChrFlags(0xA, 0x80)

    label("loc_1DD")

    Return()

    # Function_1_187 end

    def Function_2_1DE(): pass

    label("Function_2_1DE")

    OP_EA(0x2, 0x85, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_24F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xF5\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1310)
    Jump("loc_2B3")

    label("loc_24F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xF5\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF5\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2B3")

    Jump("loc_30B")

    label("loc_2B6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05This treasure chest is on strike until further\x01",
            "notice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_30B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1DE end

    def Function_3_319(): pass

    label("Function_3_319")

    OP_EA(0x2, 0x86, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3DC, 1)"), scpexpr(EXPR_END)), "loc_38A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xDC\x03\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1311)
    Jump("loc_3EE")

    label("loc_38A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xDC\x03\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xDC\x03\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_3EE")

    Jump("loc_479")

    label("loc_3F1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Inside the empty chest is carved:\x01",
            "'Olivier is handsome.'\x01",
            "You briefly wonder if he put that there himself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_479")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_319 end

    SaveToFile()

Try(main)
