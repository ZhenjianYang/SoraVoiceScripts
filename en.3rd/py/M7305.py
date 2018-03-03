from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7305   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7305.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60175",
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
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH14720 ._CH',             # 00
        'ED6_DT29/CH14721 ._CH',             # 01
        'ED6_DT29/CH14440 ._CH',             # 02
        'ED6_DT29/CH14440 ._CH',             # 03
        'ED6_DT29/CH14760 ._CH',             # 04
        'ED6_DT29/CH14761 ._CH',             # 05
        'ED6_DT29/CH14770 ._CH',             # 06
        'ED6_DT29/CH14771 ._CH',             # 07
        'ED6_DT29/CH14340 ._CH',             # 08
        'ED6_DT29/CH14340 ._CH',             # 09
        'ED6_DT29/CH14140 ._CH',             # 0A
        'ED6_DT29/CH14140 ._CH',             # 0B
        'ED6_DT29/CH14150 ._CH',             # 0C
        'ED6_DT29/CH14150 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH14720P._CP',             # 00
        'ED6_DT29/CH14721P._CP',             # 01
        'ED6_DT29/CH14440P._CP',             # 02
        'ED6_DT29/CH14440P._CP',             # 03
        'ED6_DT29/CH14760P._CP',             # 04
        'ED6_DT29/CH14761P._CP',             # 05
        'ED6_DT29/CH14770P._CP',             # 06
        'ED6_DT29/CH14771P._CP',             # 07
        'ED6_DT29/CH14340P._CP',             # 08
        'ED6_DT29/CH14340P._CP',             # 09
        'ED6_DT29/CH14140P._CP',             # 0A
        'ED6_DT29/CH14140P._CP',             # 0B
        'ED6_DT29/CH14150P._CP',             # 0C
        'ED6_DT29/CH14150P._CP',             # 0D
    )

    DeclMonster(
        X                   = -320,
        Z                   = 8730,
        Y                   = 23090,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17410,
        Z                   = 14500,
        Y                   = 39590,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16710,
        Z                   = 17630,
        Y                   = 60390,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -100,
        Z                   = 21600,
        Y                   = 75480,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17290,
        Z                   = 17630,
        Y                   = 59940,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17580,
        Z                   = 14500,
        Y                   = 39730,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -33250,
        TriggerZ            = 21000,
        TriggerY            = 77780,
        TriggerRange        = 1000,
        ActorX              = -33250,
        ActorZ              = 22000,
        ActorY              = 77780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 32650,
        TriggerZ            = 21000,
        TriggerY            = 76670,
        TriggerRange        = 1000,
        ActorX              = 32650,
        ActorZ              = 22000,
        ActorY              = 76670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_20B",          # 01, 1
        "Function_2_291",          # 02, 2
        "Function_3_3AF",          # 03, 3
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Return()

    # Function_0_20A end

    def Function_1_20B(): pass

    label("Function_1_20B")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFEA840, 0x230098)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270")
    OP_6F(0x0, 0)
    Jump("loc_277")

    label("loc_270")

    OP_6F(0x0, 60)

    label("loc_277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289")
    OP_6F(0x1, 0)
    Jump("loc_290")

    label("loc_289")

    OP_6F(0x1, 60)

    label("loc_290")

    Return()

    # Function_1_20B end

    def Function_2_291(): pass

    label("Function_2_291")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x182, 1)"), scpexpr(EXPR_END)), "loc_2FF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x82\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C6C)
    Jump("loc_367")

    label("loc_2FF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x82\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x82\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_367")

    Jump("loc_3A1")

    label("loc_36A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_3A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_291 end

    def Function_3_3AF(): pass

    label("Function_3_3AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_41D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C6D)
    Jump("loc_485")

    label("loc_41D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_485")

    Jump("loc_4BF")

    label("loc_488")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_4BF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3AF end

    SaveToFile()

Try(main)
