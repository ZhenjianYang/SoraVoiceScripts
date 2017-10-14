from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1212   ._SN',
        MapName             = 'Bose',
        Location            = 'C1212.x',
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

    DeclMonster(
        X                   = -13760,
        Z                   = 0,
        Y                   = 16490,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x91,
        Unknown_18          = 7072,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14080,
        Z                   = 0,
        Y                   = -14300,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x91,
        Unknown_18          = 7073,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -60,
        Z                   = 0,
        Y                   = 40,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x91,
        Unknown_18          = 7074,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14040,
        Z                   = 0,
        Y                   = -14060,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x91,
        Unknown_18          = 7075,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -17190,
        TriggerZ            = 0,
        TriggerY            = 12850,
        TriggerRange        = 1000,
        ActorX              = -16720,
        ActorZ              = 1500,
        ActorY              = 13450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_17E",          # 00, 0
        "Function_1_17F",          # 01, 1
        "Function_2_1C9",          # 02, 2
    )


    def Function_0_17E(): pass

    label("Function_0_17E")

    Return()

    # Function_0_17E end

    def Function_1_17F(): pass

    label("Function_1_17F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191")
    OP_6F(0x0, 0)
    Jump("loc_198")

    label("loc_191")

    OP_6F(0x0, 60)

    label("loc_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x374, 0)), scpexpr(EXPR_END)), "loc_1A4")
    SetChrFlags(0x8, 0x80)

    label("loc_1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x374, 1)), scpexpr(EXPR_END)), "loc_1B0")
    SetChrFlags(0x9, 0x80)

    label("loc_1B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x374, 2)), scpexpr(EXPR_END)), "loc_1BC")
    SetChrFlags(0xA, 0x80)

    label("loc_1BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x374, 3)), scpexpr(EXPR_END)), "loc_1C8")
    SetChrFlags(0xB, 0x80)

    label("loc_1C8")

    Return()

    # Function_1_17F end

    def Function_2_1C9(): pass

    label("Function_2_1C9")

    OP_EA(0x2, 0x33, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x0, 0x32)
    AddSepith(0x1, 0x32)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x32)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "Found\x01",
            "#2C#56IEarth Sepith x50\x01",
            "#57IWater Sepith x50\x01",
            "#58IFire Sepith x50\x01",
            "#59IWind Sepith x50#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B53)
    Jump("loc_2CC")

    label("loc_28C")


    AnonymousTalk(    #1
        (
            "\x07\x05The chest is empty.\x01",
            "...No, seriously. It's really empty.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2CC")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1C9 end

    SaveToFile()

Try(main)
