from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0301   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0301.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 19,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH12430 ._CH',             # 00
        'ED6_DT29/CH12431 ._CH',             # 01
        'ED6_DT09/CH10010 ._CH',             # 02
        'ED6_DT09/CH10011 ._CH',             # 03
        'ED6_DT09/CH10280 ._CH',             # 04
        'ED6_DT09/CH10281 ._CH',             # 05
        'ED6_DT29/CH12400 ._CH',             # 06
        'ED6_DT29/CH12401 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12430P._CP',             # 00
        'ED6_DT29/CH12431P._CP',             # 01
        'ED6_DT09/CH10010P._CP',             # 02
        'ED6_DT09/CH10011P._CP',             # 03
        'ED6_DT09/CH10280P._CP',             # 04
        'ED6_DT09/CH10281P._CP',             # 05
        'ED6_DT29/CH12400P._CP',             # 06
        'ED6_DT29/CH12401P._CP',             # 07
    )

    DeclMonster(
        X                   = 6930,
        Z                   = 40,
        Y                   = -26770,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5350,
        Z                   = -180,
        Y                   = -27890,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15690,
        Z                   = -310,
        Y                   = 1410,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3030,
        Z                   = 410,
        Y                   = 24850,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6930,
        Z                   = 40,
        Y                   = -26770,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x40,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5350,
        Z                   = -180,
        Y                   = -27890,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15690,
        Z                   = -310,
        Y                   = 1410,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3030,
        Z                   = 410,
        Y                   = 24850,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -14410,
        TriggerZ            = -120,
        TriggerY            = 8350,
        TriggerRange        = 1000,
        ActorX              = -14410,
        ActorZ              = -120,
        ActorY              = 9060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22500,
        TriggerZ            = -150,
        TriggerY            = 35130,
        TriggerRange        = 1000,
        ActorX              = -22500,
        ActorZ              = -150,
        ActorY              = 35720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18070,
        TriggerZ            = -120,
        TriggerY            = 17440,
        TriggerRange        = 1000,
        ActorX              = 18470,
        ActorZ              = -120,
        ActorY              = 17840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_236",          # 00, 0
        "Function_1_237",          # 01, 1
        "Function_2_351",          # 02, 2
        "Function_3_4C8",          # 03, 3
        "Function_4_5F2",          # 04, 4
    )


    def Function_0_236(): pass

    label("Function_0_236")

    Return()

    # Function_0_236 end

    def Function_1_237(): pass

    label("Function_1_237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x316, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_246")
    OP_64(0x3, 0x1)

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_258")
    OP_6F(0x4, 0)
    Jump("loc_25F")

    label("loc_258")

    OP_6F(0x4, 60)

    label("loc_25F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271")
    OP_6F(0x5, 0)
    Jump("loc_278")

    label("loc_271")

    OP_6F(0x5, 60)

    label("loc_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A")
    OP_6F(0x6, 0)
    Jump("loc_291")

    label("loc_28A")

    OP_6F(0x6, 60)

    label("loc_291")

    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2EF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_303")

    label("loc_2EF")

    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_303")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331")
    OP_C4(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_331")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)

    label("loc_331")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34A")
    OP_10(0x2, 0x0)
    OP_10(0x4, 0x1)
    Jump("loc_350")

    label("loc_34A")

    OP_10(0x2, 0x1)
    OP_10(0x4, 0x0)

    label("loc_350")

    Return()

    # Function_1_237 end

    def Function_2_351(): pass

    label("Function_2_351")

    OP_EA(0x2, 0x2, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_429")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4D, 1)"), scpexpr(EXPR_END)), "loc_3C2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x4D\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1961)
    Jump("loc_426")

    label("loc_3C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x4D\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x4D\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_426")

    Jump("loc_4BA")

    label("loc_429")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Nothing in here but dust. Lots of dust, actually.\x01",
            "And a nasty smell. Wait, this chest isn't a tiny\x01",
            "coffin, is it?!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_351 end

    def Function_3_4C8(): pass

    label("Function_3_4C8")

    OP_EA(0x2, 0x3, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17A, 1)"), scpexpr(EXPR_END)), "loc_539")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x7A\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1962)
    Jump("loc_59D")

    label("loc_539")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x7A\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x7A\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_59D")

    Jump("loc_5E4")

    label("loc_5A0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05This is what your curiosity gets you.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5E4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4C8 end

    def Function_4_5F2(): pass

    label("Function_4_5F2")

    OP_EA(0x2, 0x4, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_663")
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
    OP_A2(0x1964)
    Jump("loc_6C7")

    label("loc_663")

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
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_6C7")

    Jump("loc_72F")

    label("loc_6CA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05The chest yawns open as if to swallow you into\x01",
            "its infinite emptiness.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_72F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5F2 end

    SaveToFile()

Try(main)
