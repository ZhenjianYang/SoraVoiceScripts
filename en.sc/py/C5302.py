from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5302   ._SN',
        MapName             = 'Other',
        Location            = 'C5302.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        'Elevator',                             # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT29/CH12010 ._CH',             # 00
        'ED6_DT29/CH12010 ._CH',             # 01
        'ED6_DT29/CH12080 ._CH',             # 02
        'ED6_DT29/CH12081 ._CH',             # 03
        'ED6_DT29/CH12050 ._CH',             # 04
        'ED6_DT29/CH12051 ._CH',             # 05
        'ED6_DT29/CH12140 ._CH',             # 06
        'ED6_DT29/CH12141 ._CH',             # 07
        'ED6_DT29/CH12420 ._CH',             # 08
        'ED6_DT29/CH12421 ._CH',             # 09
        'ED6_DT29/CH12340 ._CH',             # 0A
        'ED6_DT29/CH12341 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH12010P._CP',             # 00
        'ED6_DT29/CH12010P._CP',             # 01
        'ED6_DT29/CH12080P._CP',             # 02
        'ED6_DT29/CH12081P._CP',             # 03
        'ED6_DT29/CH12050P._CP',             # 04
        'ED6_DT29/CH12051P._CP',             # 05
        'ED6_DT29/CH12140P._CP',             # 06
        'ED6_DT29/CH12141P._CP',             # 07
        'ED6_DT29/CH12420P._CP',             # 08
        'ED6_DT29/CH12421P._CP',             # 09
        'ED6_DT29/CH12340P._CP',             # 0A
        'ED6_DT29/CH12341P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -91600,
        Z                   = 2160,
        Y                   = 96970,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x530,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -98800,
        Z                   = 140,
        Y                   = 15500,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x529,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -99020,
        Z                   = 90,
        Y                   = 2280,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x528,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -71000,
        Z                   = 4240,
        Y                   = -78680,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 120,
        Z                   = 2000,
        Y                   = -94140,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x530,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 84070,
        Z                   = 2170,
        Y                   = -85430,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 100070,
        Y                   = -2000,
        Z                   = 9050,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 10,
    )


    DeclActor(
        TriggerX            = -107040,
        TriggerZ            = 0,
        TriggerY            = 5010,
        TriggerRange        = 1000,
        ActorX              = -107640,
        ActorZ              = 0,
        ActorY              = 4980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107050,
        TriggerZ            = 0,
        TriggerY            = 7600,
        TriggerRange        = 1000,
        ActorX              = -107650,
        ActorZ              = 0,
        ActorY              = 7570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107050,
        TriggerZ            = 0,
        TriggerY            = 10290,
        TriggerRange        = 1000,
        ActorX              = -107690,
        ActorZ              = 0,
        ActorY              = 10200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107050,
        TriggerZ            = 0,
        TriggerY            = 12900,
        TriggerRange        = 1000,
        ActorX              = -107650,
        ActorZ              = 0,
        ActorY              = 12870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 13070,
        TriggerRange        = 1000,
        ActorX              = -90030,
        ActorZ              = 0,
        ActorY              = 13100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 10470,
        TriggerRange        = 1000,
        ActorX              = -90090,
        ActorZ              = 0,
        ActorY              = 10500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 7650,
        TriggerRange        = 1000,
        ActorX              = -90010,
        ActorZ              = 0,
        ActorY              = 7690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 5050,
        TriggerRange        = 1000,
        ActorX              = -90020,
        ActorZ              = 0,
        ActorY              = 4960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_312",          # 00, 0
        "Function_1_323",          # 01, 1
        "Function_2_420",          # 02, 2
        "Function_3_581",          # 03, 3
        "Function_4_6F1",          # 04, 4
        "Function_5_83A",          # 05, 5
        "Function_6_994",          # 06, 6
        "Function_7_B02",          # 07, 7
        "Function_8_C5A",          # 08, 8
        "Function_9_D85",          # 09, 9
        "Function_10_EA7",         # 0A, 10
        "Function_11_1096",        # 0B, 11
    )


    def Function_0_312(): pass

    label("Function_0_312")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_322")
    Event(0, 11)

    label("loc_322")

    Return()

    # Function_0_312 end

    def Function_1_323(): pass

    label("Function_1_323")

    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361")
    OP_6F(0x1, 0)
    Jump("loc_368")

    label("loc_361")

    OP_6F(0x1, 60)

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A")
    OP_6F(0x2, 0)
    Jump("loc_381")

    label("loc_37A")

    OP_6F(0x2, 60)

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393")
    OP_6F(0x3, 0)
    Jump("loc_39A")

    label("loc_393")

    OP_6F(0x3, 60)

    label("loc_39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC")
    OP_6F(0x4, 0)
    Jump("loc_3B3")

    label("loc_3AC")

    OP_6F(0x4, 60)

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5")
    OP_6F(0x5, 0)
    Jump("loc_3CC")

    label("loc_3C5")

    OP_6F(0x5, 60)

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE")
    OP_6F(0x6, 0)
    Jump("loc_3E5")

    label("loc_3DE")

    OP_6F(0x6, 60)

    label("loc_3E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7")
    OP_6F(0x7, 0)
    Jump("loc_3FE")

    label("loc_3F7")

    OP_6F(0x7, 60)

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410")
    OP_6F(0x8, 0)
    Jump("loc_417")

    label("loc_410")

    OP_6F(0x8, 60)

    label("loc_417")

    OP_10(0x0, 0x0)
    OP_22(0x140, 0x0, 0x64)
    Return()

    # Function_1_323 end

    def Function_2_420(): pass

    label("Function_2_420")

    OP_EA(0x2, 0x30, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_491")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x06\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x236C)
    Jump("loc_4F5")

    label("loc_491")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x06\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x06\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4F5")

    Jump("loc_573")

    label("loc_4F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You gaze into the empty black void of the chest\x01",
            "and, for a fleeting moment, feel very small.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_573")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_420 end

    def Function_3_581(): pass

    label("Function_3_581")

    OP_EA(0x2, 0x31, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_678")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x236D)
    Jump("loc_6DF")

    label("loc_678")


    AnonymousTalk(    #4
        (
            "\x07\x05The chest is pleased that you have returned.\x01",
            "You can be its friend. Its special 'awake' friend.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_6DF")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_581 end

    def Function_4_6F1(): pass

    label("Function_4_6F1")

    OP_EA(0x2, 0x32, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x172, 1)"), scpexpr(EXPR_END)), "loc_762")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\x72\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x236F)
    Jump("loc_7C6")

    label("loc_762")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\x72\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x72\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_7C6")

    Jump("loc_82C")

    label("loc_7C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05I had saved some coffee for you, but then it was\x01",
            "taken in a mugging.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_82C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6F1 end

    def Function_5_83A(): pass

    label("Function_5_83A")

    OP_EA(0x2, 0x33, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_912")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_8AB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2370)
    Jump("loc_90F")

    label("loc_8AB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_90F")

    Jump("loc_986")

    label("loc_912")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05There is nothing in the chest but spiders now.\x01",
            "They all stare at you and clap. Bravo.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_986")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_83A end

    def Function_6_994(): pass

    label("Function_6_994")

    OP_EA(0x2, 0x34, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_A05")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "Found \x1F\x01\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2371)
    Jump("loc_A69")

    label("loc_A05")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "Found \x1F\x01\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x01\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_A69")

    Jump("loc_AF4")

    label("loc_A6C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05As you open the chest, a number of trapped,\x01",
            "screaming souls come swirling out.\x01",
            "...That's probably normal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AF4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_994 end

    def Function_7_B02(): pass

    label("Function_7_B02")

    OP_EA(0x2, 0x35, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15B, 1)"), scpexpr(EXPR_END)), "loc_B73")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "Found \x1F\x5B\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2372)
    Jump("loc_BD7")

    label("loc_B73")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "Found \x1F\x5B\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x5B\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_BD7")

    Jump("loc_C4C")

    label("loc_BDA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05The chest is empty. Your screams of\x01",
            "disappointment resound off of its wooden walls.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C4C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B02 end

    def Function_8_C5A(): pass

    label("Function_8_C5A")

    OP_EA(0x2, 0x36, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D32")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_CCB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2374)
    Jump("loc_D2F")

    label("loc_CCB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_D2F")

    Jump("loc_D77")

    label("loc_D32")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05Looks like another open-and-shut case!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D77")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C5A end

    def Function_9_D85(): pass

    label("Function_9_D85")

    OP_EA(0x2, 0x37, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_DF6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2375)
    Jump("loc_E5A")

    label("loc_DF6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_E5A")

    Jump("loc_E99")

    label("loc_E5D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05Sorry, better luck next time.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E99")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_D85 end

    def Function_10_EA7(): pass

    label("Function_10_EA7")

    EventBegin(0x0)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 100070, -1750, 9050, 0)
    OP_48()
    Fade(1000)
    OP_6D(100070, 0, 9050, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 14000, 10000, 0)
    OP_89(0x1, 101000, 14000, 9000, 90)
    OP_89(0x2, 99000, 14000, 9000, 270)
    OP_89(0x3, 100000, 14000, 8000, 180)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_F57():
        OP_8F(0xFE, 0x18E5C, 0xEA60, 0x352, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F57)
    Sleep(500)

    def lambda_F77():
        OP_6D(100070, 35000, 9050, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F77)

    def lambda_F8F():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F8F)

    def lambda_FA7():
        OP_6C(335000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FA7)
    Sleep(500)

    def lambda_FBC():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FBC)
    Sleep(500)

    def lambda_FDC():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FDC)
    Sleep(400)

    def lambda_FFC():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FFC)
    Sleep(200)

    def lambda_101C():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_101C)
    Sleep(100)

    def lambda_103C():
        OP_8F(0xFE, 0x186E6, 0xFDE8, 0x235A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_103C)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A2(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_EA7 end

    def Function_11_1096(): pass

    label("Function_11_1096")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 100070, 66000, 9050, 0)
    OP_48()
    OP_6D(100070, 48000, 9050, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 67000, 10000, 0)
    OP_89(0x1, 101000, 67000, 9000, 90)
    OP_89(0x2, 99000, 67000, 9000, 270)
    OP_89(0x3, 100000, 67000, 8000, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_1145():
        OP_6D(100070, 0, 9050, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1145)

    def lambda_115D():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_115D)

    def lambda_1175():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1175)
    FadeToBright(1000, 0)
    SetPlaceName(0x11D)

    def lambda_1191():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1191)
    Sleep(7800)

    def lambda_11B1():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11B1)
    Sleep(700)

    def lambda_11D1():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11D1)
    Sleep(600)

    def lambda_11F1():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11F1)
    Sleep(100)

    def lambda_1211():
        OP_8F(0xFE, 0x186E6, 0xFFFFF92A, 0x235A, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1211)
    Sleep(500)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 100420, 0, 4460, 180)
    SetChrPos(0x1, 100420, 0, 4460, 180)
    SetChrPos(0x2, 100420, 0, 4460, 180)
    SetChrPos(0x3, 100420, 0, 4460, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_11_1096 end

    SaveToFile()

Try(main)
