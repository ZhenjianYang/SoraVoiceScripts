from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2114   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2114.x',
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
        X                   = -6850,
        Z                   = 0,
        Y                   = -1810,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BB,
        Unknown_18          = 4951,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40,
        Z                   = 0,
        Y                   = 4290,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1B9,
        Unknown_18          = 4952,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -7770,
        TriggerZ            = 0,
        TriggerY            = 1550,
        TriggerRange        = 1000,
        ActorX              = -7770,
        ActorZ              = 0,
        ActorY              = 890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7970,
        TriggerZ            = 0,
        TriggerY            = 1500,
        TriggerRange        = 1000,
        ActorX              = 7970,
        ActorZ              = 0,
        ActorY              = 800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_16B",          # 01, 1
        "Function_2_1B6",          # 02, 2
        "Function_3_30B",          # 03, 3
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Return()

    # Function_0_16A end

    def Function_1_16B(): pass

    label("Function_1_16B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D")
    OP_6F(0x0, 0)
    Jump("loc_184")

    label("loc_17D")

    OP_6F(0x0, 60)

    label("loc_184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196")
    OP_6F(0x1, 0)
    Jump("loc_19D")

    label("loc_196")

    OP_6F(0x1, 60)

    label("loc_19D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26A, 7)), scpexpr(EXPR_END)), "loc_1A9")
    SetChrFlags(0x8, 0x80)

    label("loc_1A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26B, 0)), scpexpr(EXPR_END)), "loc_1B5")
    SetChrFlags(0x9, 0x80)

    label("loc_1B5")

    Return()

    # Function_1_16B end

    def Function_2_1B6(): pass

    label("Function_2_1B6")

    OP_EA(0x2, 0x87, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_227")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xF8\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1314)
    Jump("loc_28B")

    label("loc_227")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xF8\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF8\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_28B")

    Jump("loc_2FD")

    label("loc_28E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You begin to suspect that this treasure chest is\x01",
            "a portal to the Meat Dimension.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2FD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1B6 end

    def Function_3_30B(): pass

    label("Function_3_30B")

    OP_EA(0x2, 0x88, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_37C")
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
    OP_A2(0x1315)
    Jump("loc_3E0")

    label("loc_37C")

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

    label("loc_3E0")

    Jump("loc_47B")

    label("loc_3E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05You imagine this chest as it once was,\x01",
            "brimming with treasure and full of delight.\x01",
            "You can hardly bear to look at it now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_47B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_30B end

    SaveToFile()

Try(main)
