from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1102   ._SN',
        MapName             = 'Bose',
        Location            = 'C1102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C1102_1 ._SN',
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
        'Enhanced Jaeger',                      # 9
        'Enhanced Jaeger',                      # 10
        'Vogel',                                # 11
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
        'ED6_DT07/CH00162 ._CH',             # 00
        'ED6_DT06/CH20020 ._CH',             # 01
        'ED6_DT09/CH10300 ._CH',             # 02
        'ED6_DT09/CH10301 ._CH',             # 03
        'ED6_DT27/CH03610 ._CH',             # 04
        'ED6_DT27/CH03750 ._CH',             # 05
        'ED6_DT29/CH12350 ._CH',             # 06
        'ED6_DT29/CH12351 ._CH',             # 07
        'ED6_DT29/CH12570 ._CH',             # 08
        'ED6_DT29/CH12571 ._CH',             # 09
        'ED6_DT29/CH12574 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH00162P._CP',             # 00
        'ED6_DT06/CH20020P._CP',             # 01
        'ED6_DT09/CH10300P._CP',             # 02
        'ED6_DT09/CH10301P._CP',             # 03
        'ED6_DT27/CH03610P._CP',             # 04
        'ED6_DT27/CH03750P._CP',             # 05
        'ED6_DT29/CH12350P._CP',             # 06
        'ED6_DT29/CH12351P._CP',             # 07
        'ED6_DT29/CH12570P._CP',             # 08
        'ED6_DT29/CH12571P._CP',             # 09
        'ED6_DT29/CH12574P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -29330,
        Z                   = -500,
        Y                   = 36850,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAC,
        Unknown_18          = 6698,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -84750,
        Z                   = -410,
        Y                   = 68560,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAC,
        Unknown_18          = 6699,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 50700,
        Z                   = 0,
        Y                   = 57550,
        Unknown_0C          = 225,
        Unknown_0E          = 6,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAC,
        Unknown_18          = 6700,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 49810,
        Z                   = 0,
        Y                   = 10380,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAC,
        Unknown_18          = 6701,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 75930,
        Z                   = -500,
        Y                   = 185910,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 193,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDAD,
        Unknown_18          = 6702,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -46900,
        Y                   = -2000,
        Z                   = 26000,
        Range               = -46100,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x7530,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = 7410,
        TriggerZ            = 0,
        TriggerY            = 43900,
        TriggerRange        = 1000,
        ActorX              = 6750,
        ActorZ              = 0,
        ActorY              = 43900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -75700,
        TriggerZ            = 0,
        TriggerY            = 30920,
        TriggerRange        = 1000,
        ActorX              = -75080,
        ActorZ              = 0,
        ActorY              = 30400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -89670,
        TriggerZ            = -250,
        TriggerY            = 78010,
        TriggerRange        = 1000,
        ActorX              = -90330,
        ActorZ              = -250,
        ActorY              = 78140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -80220,
        TriggerZ            = -250,
        TriggerY            = 76890,
        TriggerRange        = 1000,
        ActorX              = -79560,
        ActorZ              = -250,
        ActorY              = 76890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41820,
        TriggerZ            = -250,
        TriggerY            = 99770,
        TriggerRange        = 1000,
        ActorX              = -41820,
        ActorZ              = -250,
        ActorY              = 99110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28930,
        TriggerZ            = -130,
        TriggerY            = 47490,
        TriggerRange        = 1000,
        ActorX              = -28930,
        ActorZ              = 1500,
        ActorY              = 47490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -69290,
        TriggerZ            = 0,
        TriggerY            = 170530,
        TriggerRange        = 1000,
        ActorX              = -69860,
        ActorZ              = 0,
        ActorY              = 170530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_30A",          # 00, 0
        "Function_1_3C7",          # 01, 1
        "Function_2_504",          # 02, 2
        "Function_3_662",          # 03, 3
        "Function_4_7BB",          # 04, 4
        "Function_5_8E5",          # 05, 5
        "Function_6_A51",          # 06, 6
        "Function_7_BDA",          # 07, 7
        "Function_8_CFE",          # 08, 8
        "Function_9_D0A",          # 09, 9
        "Function_10_E4B",         # 0A, 10
        "Function_11_13BD",        # 0B, 11
        "Function_12_1654",        # 0C, 12
        "Function_13_1750",        # 0D, 13
    )


    def Function_0_30A(): pass

    label("Function_0_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_362")

    label("loc_327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_346")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_362")

    label("loc_346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_362")
    OP_A3(0x10F1)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(1, 1)

    label("loc_362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392")
    ClearChrFlags(0xB, 0x80)

    label("loc_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F")
    ClearChrFlags(0xC, 0x80)

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC")
    ClearChrFlags(0xD, 0x80)

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9")
    ClearChrFlags(0xE, 0x80)

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6")
    ClearChrFlags(0xF, 0x80)

    label("loc_3C6")

    Return()

    # Function_0_30A end

    def Function_1_3C7(): pass

    label("Function_1_3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9")
    OP_6F(0x0, 0)
    Jump("loc_3E0")

    label("loc_3D9")

    OP_6F(0x0, 60)

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2")
    OP_6F(0x1, 0)
    Jump("loc_3F9")

    label("loc_3F2")

    OP_6F(0x1, 60)

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B")
    OP_6F(0x2, 0)
    Jump("loc_412")

    label("loc_40B")

    OP_6F(0x2, 60)

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_424")
    OP_6F(0x3, 0)
    Jump("loc_42B")

    label("loc_424")

    OP_6F(0x3, 60)

    label("loc_42B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D")
    OP_6F(0x4, 0)
    Jump("loc_444")

    label("loc_43D")

    OP_6F(0x4, 60)

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x367, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_456")
    OP_6F(0x6, 0)
    Jump("loc_45D")

    label("loc_456")

    OP_6F(0x6, 60)

    label("loc_45D")

    OP_E0(0x3, 0x10, 0xC9, 0xFE, 0xFF, 0x38, 0xFF, 0xFF, 0xFF, 0x5A, 0x2C, 0x1, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_476")
    OP_64(0x5, 0x1)

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C2")

    label("loc_48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_1B(0x4, 0x0, 0xD)
    Jump("loc_4C2")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_4C2")

    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_503")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_503")
    Event(1, 0)

    label("loc_503")

    Return()

    # Function_1_3C7 end

    def Function_2_504(): pass

    label("Function_2_504")

    OP_EA(0x2, 0x2B, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_575")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B33)
    Jump("loc_5D9")

    label("loc_575")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_5D9")

    Jump("loc_654")

    label("loc_5DC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05An empty treasure chest. Full of promise\x01",
            "yet devoid of payoff. A perfect metaphor for me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_654")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_504 end

    def Function_3_662(): pass

    label("Function_3_662")

    OP_EA(0x2, 0x2C, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_6D3")
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
    OP_A2(0x1B34)
    Jump("loc_737")

    label("loc_6D3")

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

    label("loc_737")

    Jump("loc_7AD")

    label("loc_73A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Nothing in here. Good. We don't want people\x01",
            "refilling these while we're not looking.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7AD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_662 end

    def Function_4_7BB(): pass

    label("Function_4_7BB")

    OP_EA(0x2, 0x2D, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_893")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3D7, 1)"), scpexpr(EXPR_END)), "loc_82C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xD7\x03\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B35)
    Jump("loc_890")

    label("loc_82C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xD7\x03\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xD7\x03\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_890")

    Jump("loc_8D7")

    label("loc_893")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Ugh... Must we go through this AGAIN?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8D7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_7BB end

    def Function_5_8E5(): pass

    label("Function_5_8E5")

    OP_EA(0x2, 0x2E, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_956")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B36)
    Jump("loc_9BA")

    label("loc_956")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_9BA")

    Jump("loc_A43")

    label("loc_9BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05You rest your head atop the empty chest.\x01",
            "You rapidly withdraw as you hear what sounds\x01",
            "like a heartbeat.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A43")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_8E5 end

    def Function_6_A51(): pass

    label("Function_6_A51")

    OP_EA(0x2, 0x2F, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x366, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B29")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1AA, 1)"), scpexpr(EXPR_END)), "loc_AC2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xAA\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B37)
    Jump("loc_B26")

    label("loc_AC2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xAA\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xAA\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_B26")

    Jump("loc_BCC")

    label("loc_B29")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05They all look the same to you now. Every one\x01",
            "of them, so helpless, so vulnerable--a mere\x01",
            "target for you and your insatiable hunger. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BCC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A51 end

    def Function_7_BDA(): pass

    label("Function_7_BDA")

    OP_EA(0x2, 0x30, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x367, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15C, 1)"), scpexpr(EXPR_END)), "loc_C4B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\x5C\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B38)
    Jump("loc_CAF")

    label("loc_C4B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\x5C\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x5C\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_CAF")

    Jump("loc_CF0")

    label("loc_CB2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05I've been waiting for this day!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CF0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_BDA end

    def Function_8_CFE(): pass

    label("Function_8_CFE")

    EventBegin(0x0)
    NewScene("ED6_DT21/C1103   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_8_CFE end

    def Function_9_D0A(): pass

    label("Function_9_D0A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1D")
    Call(0, 12)

    label("loc_D1D")

    OP_6D(1020, 0, 6630, 0)
    OP_67(0, 8740, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 430, 0, 6420, 0)
    SetChrPos(0x107, 1480, 0, 6290, 0)
    SetChrPos(0xF8, -160, 0, 5280, 0)
    SetChrPos(0xF9, 1570, 0, 5060, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x107,
        "#065F#6PW-Was that Agate's voice?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1002FThe way it's echoing...I think he must be\x01",
            "in the big open mining pit!\x02\x03",

            "#1005FCome on! Let's hurry!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_9_D0A end

    def Function_10_E4B(): pass

    label("Function_10_E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136E")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E79")
    Call(0, 12)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_E79")

    Fade(1000)
    OP_6D(-29880, -430, 46640, 0)
    OP_67(0, 10510, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -29170, -500, 45850, 0)
    SetChrPos(0x107, -30200, -500, 45730, 0)
    SetChrPos(0xF8, -30290, -500, 44420, 0)
    SetChrPos(0xF9, -29090, -500, 44350, 0)
    OP_0D()

    ChrTalk(    #20
        0x101,
        "#1020F#5PWhat the...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x107,
        "#065F#6PUm, Estelle, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1020F#5PThis way should lead right into the\x01",
            "mining pit...\x02\x03",

            "Why is it blocked off by rocks?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1008")

    ChrTalk(    #23
        0x105,
        (
            "#043F#5PPerhaps the dragon did something that\x01",
            "caused the passage to cave in?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CE")

    label("loc_1008")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1065")

    ChrTalk(    #24
        0x103,
        (
            "#022F#5PThe dragon must've done something that\x01",
            "caused a small cave-in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CE")

    label("loc_1065")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CE")

    ChrTalk(    #25
        0x104,
        (
            "#035F#5PHm. Perhaps our draconic quarry caused\x01",
            "the passage to collapse in his raging.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CE")


    ChrTalk(    #26
        0x107,
        (
            "#062F#6PUm, okay, then! I'll use my cannon!\x01",
            "Stand b--\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 0)
    OP_0D()
    Sleep(500)

    def lambda_1129():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1129)
    Sleep(100)

    def lambda_113C():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_113C)
    Sleep(10)
    TurnDirection(0xF8, 0x107, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B2")

    ChrTalk(    #27
        0x108,
        (
            "#072F#5PNo, don't, Tita.\x02\x03",

            "An explosion could just make\x01",
            "it collapse further.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1287")

    label("loc_11B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1236")

    ChrTalk(    #28
        0x104,
        (
            "#032F#5PNo. Hold your blasting for now.\x02\x03",

            "A large explosion could simply\x01",
            "cause the tunnel to further collapse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1287")

    label("loc_1236")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1287")

    ChrTalk(    #29
        0x103,
        (
            "#022F#5PTita, no.\x02\x03",

            "An explosion will just cave it in further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1287")

    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #30
        0x107,
        "#561F#6PBut, but...!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    Sleep(300)

    ChrTalk(    #31
        0x101,
        (
            "#1002F#2PTita...I know how you feel,\x01",
            "but stay calm, okay?\x02\x03",

            "Let's see if we can find\x01",
            "another way around.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #32
        0x107,
        "#062F#6PO-Okay!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A18)
    OP_28(0x94, 0x1, 0x20)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_13BC")

    label("loc_136E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05The way is blocked by rocks.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_13BC")

    Return()

    # Function_10_E4B end

    def Function_11_13BD(): pass

    label("Function_11_13BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 1)), scpexpr(EXPR_END)), "loc_13C5")
    Return()

    label("loc_13C5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E6")
    Call(0, 12)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_13E6")

    Fade(1000)
    OP_6D(-48350, 50, 28560, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -47490, 50, 28410, 270)
    SetChrPos(0x107, -47470, 50, 27380, 270)
    SetChrPos(0xF8, -46180, 50, 28740, 270)
    SetChrPos(0xF9, -45960, 0, 27320, 270)
    OP_0D()

    ChrTalk(    #34
        0x101,
        (
            "#1004F#6PHuh?\x02\x03",

            "This bridge was broken the\x01",
            "last time we came here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153C")

    ChrTalk(    #35
        0x103,
        (
            "#022F#2PI believe I remember hearing that the army\x01",
            "repaired it after the bandit incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1015F#6POh, okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_153C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C8")

    ChrTalk(    #37
        0x105,
        (
            "#042F#2PIt must have been repaired in the interim.\x01",
            "Perhaps by the Royal Army, or local miners?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1015F#6PMaybe...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_15C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1643")

    ChrTalk(    #39
        0x104,
        (
            "#035F#2PHmm. Perhaps someone, such as the Royal\x01",
            "Army or the residents, repaired it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1015FMaybe...\x02",
    )

    CloseMessageWindow()

    label("loc_1643")

    OP_A2(0x1A19)
    OP_28(0x94, 0x1, 0x40)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_11_13BD end

    def Function_12_1654(): pass

    label("Function_12_1654")

    FadeToDark(0, 0, -1)
    OP_6D(-41010, -360, 62470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_170A"),
        (1, "loc_1710"),
        (SWITCH_DEFAULT, "loc_1716"),
    )


    label("loc_170A")

    OP_A2(0x1200)
    Jump("loc_1716")

    label("loc_1710")

    OP_A2(0x1201)
    Jump("loc_1716")

    label("loc_1716")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_12_1654 end

    def Function_13_1750(): pass

    label("Function_13_1750")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1794")

    ChrTalk(    #41
        0x101,
        "#1002FAgate's further in... We need to hurry!\x02",
    )

    CloseMessageWindow()
    Jump("loc_18FC")

    label("loc_1794")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D3")

    ChrTalk(    #42
        0x103,
        "#022FAgate is ahead. We must hurry to him!\x02",
    )

    CloseMessageWindow()
    Jump("loc_18FC")

    label("loc_17D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1823")

    ChrTalk(    #43
        0x105,
        (
            "#042FAgate should be ahead of us.\x01",
            "We must hurry to his aid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18FC")

    label("loc_1823")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1879")

    ChrTalk(    #44
        0x104,
        (
            "#032FOur Heavy Blade requires aid further in.\x01",
            "Come! Let us hurry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18FC")

    label("loc_1879")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BF")

    ChrTalk(    #45
        0x107,
        "#065FAgate's further in... We've GOT to help him!\x02",
    )

    CloseMessageWindow()
    Jump("loc_18FC")

    label("loc_18BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FC")

    ChrTalk(    #46
        0x108,
        "#072FAgate is further in. We must help him!\x02",
    )

    CloseMessageWindow()

    label("loc_18FC")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_13_1750 end

    SaveToFile()

Try(main)
