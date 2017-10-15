from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0413   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0413.x',
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
        X                   = 17840,
        Z                   = 0,
        Y                   = 190,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 6515,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 170,
        Z                   = 0,
        Y                   = 7010,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x32,
        Unknown_18          = 6516,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19420,
        Z                   = 0,
        Y                   = 2050,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x33,
        Unknown_18          = 6517,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -16700,
        TriggerZ            = 0,
        TriggerY            = -13650,
        TriggerRange        = 1000,
        ActorX              = -16700,
        ActorZ              = 1500,
        ActorY              = -13650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_173",          # 01, 1
        "Function_2_1B1",          # 02, 2
    )


    def Function_0_172(): pass

    label("Function_0_172")

    Return()

    # Function_0_172 end

    def Function_1_173(): pass

    label("Function_1_173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185")
    OP_6F(0x0, 0)
    Jump("loc_18C")

    label("loc_185")

    OP_6F(0x0, 60)

    label("loc_18C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32E, 3)), scpexpr(EXPR_END)), "loc_198")
    SetChrFlags(0x8, 0x80)

    label("loc_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32E, 4)), scpexpr(EXPR_END)), "loc_1A4")
    SetChrFlags(0x9, 0x80)

    label("loc_1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32E, 5)), scpexpr(EXPR_END)), "loc_1B0")
    SetChrFlags(0xA, 0x80)

    label("loc_1B0")

    Return()

    # Function_1_173 end

    def Function_2_1B1(): pass

    label("Function_2_1B1")

    OP_EA(0x2, 0xF, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A2, 1)"), scpexpr(EXPR_END)), "loc_222")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xA2\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1955)
    Jump("loc_286")

    label("loc_222")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xA2\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xA2\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_286")

    Jump("loc_2B9")

    label("loc_289")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Sorry, I'm empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2B9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1B1 end

    SaveToFile()

Try(main)
