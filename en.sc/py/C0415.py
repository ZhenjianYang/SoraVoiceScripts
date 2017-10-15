from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0415   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0415.x',
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
        'ED6_DT09/CH10040 ._CH',             # 00
        'ED6_DT09/CH10041 ._CH',             # 01
        'ED6_DT09/CH10070 ._CH',             # 02
        'ED6_DT09/CH10071 ._CH',             # 03
        'ED6_DT09/CH10150 ._CH',             # 04
        'ED6_DT09/CH10151 ._CH',             # 05
        'ED6_DT09/CH10190 ._CH',             # 06
        'ED6_DT09/CH10191 ._CH',             # 07
        'ED6_DT29/CH12140 ._CH',             # 08
        'ED6_DT29/CH12141 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10040P._CP',             # 00
        'ED6_DT09/CH10041P._CP',             # 01
        'ED6_DT09/CH10070P._CP',             # 02
        'ED6_DT09/CH10071P._CP',             # 03
        'ED6_DT09/CH10150P._CP',             # 04
        'ED6_DT09/CH10151P._CP',             # 05
        'ED6_DT09/CH10190P._CP',             # 06
        'ED6_DT09/CH10191P._CP',             # 07
        'ED6_DT29/CH12140P._CP',             # 08
        'ED6_DT29/CH12141P._CP',             # 09
    )

    DeclMonster(
        X                   = 12510,
        Z                   = 0,
        Y                   = -10,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 6523,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12570,
        Z                   = 0,
        Y                   = -30,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 6524,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -8590,
        TriggerZ            = 0,
        TriggerY            = -9040,
        TriggerRange        = 1000,
        ActorX              = -8150,
        ActorZ              = 0,
        ActorY              = -9480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4360,
        TriggerZ            = 0,
        TriggerY            = 22580,
        TriggerRange        = 1000,
        ActorX              = -4450,
        ActorZ              = 0,
        ActorY              = 23190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4390,
        TriggerZ            = 0,
        TriggerY            = 22620,
        TriggerRange        = 1000,
        ActorX              = 4430,
        ActorZ              = 0,
        ActorY              = 23230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19E",          # 00, 0
        "Function_1_19F",          # 01, 1
        "Function_2_203",          # 02, 2
        "Function_3_391",          # 03, 3
        "Function_4_525",          # 04, 4
    )


    def Function_0_19E(): pass

    label("Function_0_19E")

    Return()

    # Function_0_19E end

    def Function_1_19F(): pass

    label("Function_1_19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1")
    OP_6F(0x0, 0)
    Jump("loc_1B8")

    label("loc_1B1")

    OP_6F(0x0, 60)

    label("loc_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA")
    OP_6F(0x1, 0)
    Jump("loc_1D1")

    label("loc_1CA")

    OP_6F(0x1, 60)

    label("loc_1D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3")
    OP_6F(0x2, 0)
    Jump("loc_1EA")

    label("loc_1E3")

    OP_6F(0x2, 60)

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32F, 3)), scpexpr(EXPR_END)), "loc_1F6")
    SetChrFlags(0x8, 0x80)

    label("loc_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32F, 4)), scpexpr(EXPR_END)), "loc_202")
    SetChrFlags(0x9, 0x80)

    label("loc_202")

    Return()

    # Function_1_19F end

    def Function_2_203(): pass

    label("Function_2_203")

    OP_EA(0x2, 0x10, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18, 1)"), scpexpr(EXPR_END)), "loc_274")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x18\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1958)
    Jump("loc_2D8")

    label("loc_274")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x18\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x18\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2D8")

    Jump("loc_383")

    label("loc_2DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05As you open the box again, you think about what\x01",
            "it would be like if you lived inside it like a little\x01",
            "house. It'd be cramped, but quaint.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_383")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_203 end

    def Function_3_391(): pass

    label("Function_3_391")

    OP_EA(0x2, 0x11, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x184, 1)"), scpexpr(EXPR_END)), "loc_402")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x84\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x195A)
    Jump("loc_466")

    label("loc_402")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x84\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x84\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_466")

    Jump("loc_517")

    label("loc_469")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05YOU might look at this chest and think its empty,\x01",
            "but that's just negative thinking. Others see this\x01",
            "baby and marvel at the amazing air inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_517")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_391 end

    def Function_4_525(): pass

    label("Function_4_525")

    OP_EA(0x2, 0x12, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29E, 1)"), scpexpr(EXPR_END)), "loc_596")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\x9E\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x195C)
    Jump("loc_5FA")

    label("loc_596")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\x9E\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x9E\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_5FA")

    Jump("loc_64E")

    label("loc_5FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05You find the greatest treasure of all: friendship.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_64E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_525 end

    SaveToFile()

Try(main)
