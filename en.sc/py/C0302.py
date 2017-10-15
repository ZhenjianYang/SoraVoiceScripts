from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0302   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0302.x',
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
        X                   = 55300,
        Z                   = 160,
        Y                   = -13730,
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
        X                   = 49420,
        Z                   = 40,
        Y                   = 7980,
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
        X                   = 58410,
        Z                   = -10,
        Y                   = -820,
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
        X                   = 69340,
        Z                   = -90,
        Y                   = 4080,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 48430,
        TriggerZ            = -90,
        TriggerY            = 16780,
        TriggerRange        = 1000,
        ActorX              = 48560,
        ActorZ              = -90,
        ActorY              = 17480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 77150,
        TriggerZ            = -50,
        TriggerY            = 8730,
        TriggerRange        = 1000,
        ActorX              = 77860,
        ActorZ              = -50,
        ActorY              = 8730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 65900,
        TriggerZ            = 90,
        TriggerY            = -5510,
        TriggerRange        = 1000,
        ActorX              = 65239,
        ActorZ              = 90,
        ActorY              = -5800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1C6",          # 00, 0
        "Function_1_1C7",          # 01, 1
        "Function_2_290",          # 02, 2
        "Function_3_403",          # 03, 3
        "Function_4_573",          # 04, 4
    )


    def Function_0_1C6(): pass

    label("Function_0_1C6")

    Return()

    # Function_0_1C6 end

    def Function_1_1C7(): pass

    label("Function_1_1C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9")
    OP_6F(0x4, 0)
    Jump("loc_1E0")

    label("loc_1D9")

    OP_6F(0x4, 60)

    label("loc_1E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2")
    OP_6F(0x5, 0)
    Jump("loc_1F9")

    label("loc_1F2")

    OP_6F(0x5, 60)

    label("loc_1F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B")
    OP_6F(0x6, 0)
    Jump("loc_212")

    label("loc_20B")

    OP_6F(0x6, 60)

    label("loc_212")

    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_260")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)

    label("loc_260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_272")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_282")
    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)
    Jump("loc_28F")

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_END)), "loc_28F")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)

    label("loc_28F")

    Return()

    # Function_1_1C7 end

    def Function_2_290(): pass

    label("Function_2_290")

    OP_EA(0x2, 0x5, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x161, 1)"), scpexpr(EXPR_END)), "loc_301")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x61\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1965)
    Jump("loc_365")

    label("loc_301")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x61\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x61\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_365")

    Jump("loc_3F5")

    label("loc_368")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05After minutes of frantic searching, you close\x01",
            "the lid, panting heavily. It's time to admit you\x01",
            "have a problem.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3F5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_290 end

    def Function_3_403(): pass

    label("Function_3_403")

    OP_EA(0x2, 0x6, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x134, 1)"), scpexpr(EXPR_END)), "loc_474")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x34\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1967)
    Jump("loc_4D8")

    label("loc_474")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x34\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x34\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_4D8")

    Jump("loc_565")

    label("loc_4DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05It's empty, but you notice a little hole in the\x01",
            "back of the box. The view from there isn't too\x01",
            "bad, either!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_565")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_403 end

    def Function_4_573(): pass

    label("Function_4_573")

    OP_EA(0x2, 0x7, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x130, 1)"), scpexpr(EXPR_END)), "loc_5E4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\x30\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1969)
    Jump("loc_648")

    label("loc_5E4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\x30\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x30\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_648")

    Jump("loc_69D")

    label("loc_64B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Oh, hey, is there still something in here? ...Nope.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_69D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_573 end

    SaveToFile()

Try(main)
