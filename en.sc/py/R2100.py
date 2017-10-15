from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2100   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2100.x',
        MapIndex            = 100,
        MapDefaultBGM       = "ed60029",
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
        'Manoria Village',                      # 9
        'Krone Trail',                          # 10
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
        'ED6_DT09/CH10160 ._CH',             # 00
        'ED6_DT09/CH10161 ._CH',             # 01
        'ED6_DT09/CH10450 ._CH',             # 02
        'ED6_DT09/CH10451 ._CH',             # 03
        'ED6_DT09/CH10220 ._CH',             # 04
        'ED6_DT09/CH10221 ._CH',             # 05
        'ED6_DT09/CH10470 ._CH',             # 06
        'ED6_DT09/CH10471 ._CH',             # 07
        'ED6_DT09/CH10480 ._CH',             # 08
        'ED6_DT09/CH10481 ._CH',             # 09
        'ED6_DT09/CH11060 ._CH',             # 0A
        'ED6_DT09/CH11061 ._CH',             # 0B
        'ED6_DT09/CH10460 ._CH',             # 0C
        'ED6_DT09/CH10461 ._CH',             # 0D
        'ED6_DT29/CH12100 ._CH',             # 0E
        'ED6_DT29/CH12101 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10160P._CP',             # 00
        'ED6_DT09/CH10161P._CP',             # 01
        'ED6_DT09/CH10450P._CP',             # 02
        'ED6_DT09/CH10451P._CP',             # 03
        'ED6_DT09/CH10220P._CP',             # 04
        'ED6_DT09/CH10221P._CP',             # 05
        'ED6_DT09/CH10470P._CP',             # 06
        'ED6_DT09/CH10471P._CP',             # 07
        'ED6_DT09/CH10480P._CP',             # 08
        'ED6_DT09/CH10481P._CP',             # 09
        'ED6_DT09/CH11060P._CP',             # 0A
        'ED6_DT09/CH11061P._CP',             # 0B
        'ED6_DT09/CH10460P._CP',             # 0C
        'ED6_DT09/CH10461P._CP',             # 0D
        'ED6_DT29/CH12100P._CP',             # 0E
        'ED6_DT29/CH12101P._CP',             # 0F
    )

    DeclNpc(
        X                   = -18570,
        Z                   = -2000,
        Y                   = -37710,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 100500,
        Z                   = -2070,
        Y                   = 132300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 26400,
        Z                   = -2050,
        Y                   = 109110,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22850,
        Z                   = -2020,
        Y                   = 80880,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x170,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24710,
        Z                   = -2070,
        Y                   = 44250,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16680,
        Z                   = -2060,
        Y                   = 9800,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x170,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10660,
        Z                   = -1950,
        Y                   = 86530,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 53700,
        Z                   = -2000,
        Y                   = 127140,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x170,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 35120,
        TriggerZ            = -1980,
        TriggerY            = 46370,
        TriggerRange        = 1000,
        ActorX              = 35820,
        ActorZ              = -1950,
        ActorY              = 46370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_236",          # 00, 0
        "Function_1_237",          # 01, 1
        "Function_2_271",          # 02, 2
    )


    def Function_0_236(): pass

    label("Function_0_236")

    Return()

    # Function_0_236 end

    def Function_1_237(): pass

    label("Function_1_237")

    OP_16(0x2, 0xFA0, 0xFFFE7578, 0xFFFEE6C0, 0x23002B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B")
    OP_6F(0x0, 0)
    Jump("loc_262")

    label("loc_25B")

    OP_6F(0x0, 60)

    label("loc_262")

    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C4, 0x1, 0x64)
    Return()

    # Function_1_237 end

    def Function_2_271(): pass

    label("Function_2_271")

    OP_EA(0x2, 0xDF, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15E, 1)"), scpexpr(EXPR_END)), "loc_2E2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x5E\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1300)
    Jump("loc_346")

    label("loc_2E2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x5E\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x5E\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_346")

    Jump("loc_3EF")

    label("loc_349")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You open the chest to see a man's face,\x01",
            "just smiling at you. Unsettled, you back away\x01",
            "and close the lid. Let's not open that one again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3EF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_271 end

    SaveToFile()

Try(main)
